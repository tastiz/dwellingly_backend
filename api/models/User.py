class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    account_source = db.Column(db.String(120), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False)
    date_updated = db.Column(db.DateTime, nullable=False)
    properties = db.relationship('Property', backref='user', lazy=True)
    contacts = db.relationship('Contacts', backref = 'user', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.name