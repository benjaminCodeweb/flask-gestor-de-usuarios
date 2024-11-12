from src import db, crear_app
from  src.models import User

app = crear_app()

with app.app_context():
    db.create_all()

if __name__ == '__main__': 
    app.run(debug=True)