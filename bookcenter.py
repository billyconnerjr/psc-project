from app import create_app, db
from app.models import User, Book

app = create_app()

#making the shell
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Book': Book}