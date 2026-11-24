# Django Tutorial
Done for coursework @MakeSchool.
Completed by Nolan Kovacik.
See `LICENSE.md` for more information.

## Run Locally
Requires Python 3.10 or later.

1. Fork or clone this project and `cd` into its root directory.
1. Create a virtual environment: `python -m venv .venv`.
1. Activate it: `.venv\Scripts\Activate.ps1` in PowerShell, or `source .venv/bin/activate` on macOS/Linux.
1. Install dependencies: `python -m pip install -r requirements.txt`.
1. Apply migrations: `python manage.py migrate`.
1. Start the server: `python manage.py runserver` and visit `http://127.0.0.1:8000/polls/`.

The SQLite database is tracked in Git. Back it up before migrating if you need to preserve its contents.

## Run Tests
1. `python manage.py test`

## Polls API
- `GET /api/polls/` lists up to 20 questions.
- `GET /api/polls/<id>` returns one question.

## Update Database Structure
1. Run `python manage.py migrate`.
1. Make your changes to the database models.
	- These can usually be found in a `models.py` file.
1. Run `python manage.py makemigrations <app>`
	- One example of `<app>` is `polls`.
1. Run `python manage.py migrate` again.

**\*NOTE**: If you are going to make changes to the database more than once, step 1 may be superfluous.

### Remembering Commands
If you have trouble remembering which command does what, this tidbit from Stack Overflow may help you&hellip;
- `python manage.py makemigrations <app>`: Create the migrations (generate the SQL commands).
- `python manage.py migrate`: Run the migrations (execute the SQL commands).

## Other Useful Commands
- `python manage.py shell`: Run the Django Shell.
- `python manage.py createsuperuser`: Create a new superuser.

## Credits
Many thanks to the Django team, their [tutorial], and their great documentation.
Thanks also to @Dani from Make School, and her team.


[tutorial]: https://docs.djangoproject.com/en/3.0/intro/tutorial01/
