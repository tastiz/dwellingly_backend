# need to create a many to many relationship with properties, possibly tickets?


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(50), nullable=False)
    user = db.relationship('User', backref='contact', lazy=True)

    def __repr__(self):
        return '<Contact %r>' % self.name