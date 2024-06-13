from Website import create_website
from Website import db
from Website.models import User
from werkzeug.security import generate_password_hash

app = create_website()

def init_superUser(email, password):
    new_user = new_user = User(email=email, superuser=True, first_name='admin', password=generate_password_hash(
                password, method='pbkdf2:sha256'))
    with app.app_context():
        db.session.add(new_user)
        db.session.commit()
    print(f'User {email} has been added.')


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print("Usage: python insert_user.py <username> <email>")
    else:
        username = sys.argv[1]
        email = sys.argv[2]
        init_superUser(username, email)