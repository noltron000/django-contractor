from django.test import TestCase
from django.utils import timezone

from polls.models import Question


class QuestionApiTests(TestCase):
	def test_list_returns_questions(self):
		question = Question.objects.create(question_text='A question', pub_date=timezone.now())

		response = self.client.get('/api/polls/')

		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(response.json()), 1)
		self.assertEqual(response.json()[0]['id'], question.id)
		self.assertEqual(response.json()[0]['question_text'], 'A question')

	def test_list_returns_at_most_twenty_questions(self):
		Question.objects.bulk_create([
			Question(question_text='Question {}'.format(number), pub_date=timezone.now())
			for number in range(21)
		])

		response = self.client.get('/api/polls/')

		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(response.json()), 20)

	def test_detail_returns_question(self):
		question = Question.objects.create(question_text='A question', pub_date=timezone.now())

		response = self.client.get('/api/polls/{}'.format(question.id))

		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.json()['id'], question.id)
		self.assertEqual(response.json()['question_text'], 'A question')

	def test_detail_returns_404_for_missing_question(self):
		response = self.client.get('/api/polls/999')

		self.assertEqual(response.status_code, 404)
