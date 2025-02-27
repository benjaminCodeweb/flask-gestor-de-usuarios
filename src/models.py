from  .  import  db
class User(db.Model):
    __tablename__ = 'users'

    id =  db.Column(db.Integer, primary_key = True)
    first_name =  db.Column(db.String(50), nullable = False)
    last_name =  db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(50), nullable = False)
    image_url = db.Column(db.String(200), nullable = True)

    def __repr__ (self) -> str:
        return f"<User {self.first_name} {self.last_name}>"