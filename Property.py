class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    ticket_receiver = db.relationship('Contact', backref='property', lazy=True)
    address = db.Column(db.String(120), nullable=False)
    property_type = db.Column(db.String(50), nullable=False)
    units = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(240), nullable=False)
    property_owner = db.relationship('User', backref='property', lazy=True) #user
    property_manager = db.relationship('User', backref='property', lazy=True) #user
    emergency_contact = db.relationship('Contact', backref='property', lazy=True)
    tenants = db.relationship('User', backref='property', lazy=True)

    def __repr__(self):
        return '<Property %r>' % self.name