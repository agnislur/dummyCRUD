from extensions import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(db.String(200))
    created_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
    update_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now(), onupdate=db.func.now())

    @property
    def data(self):
        return {
            'id':self.id,
            'name':self.name,
            'email':self.email,
            'password':self.password
        }
    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all(cls):
        r = cls.query.all()
        result =[]

        for i in r:
            result.append(i.data)
        return result
    
    @classmethod
    def get_by_id(cls,id):
        return cls.query.filter(cls.id == id).first()


class User1(db.Model):
    __tablename__ = 'users1'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(db.String(200))
    pekerjaan = db.Column(db.String(200))
    gender = db.Column(db.String(200))
    umur = db.Column(db.String(200))
    created_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
    update_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now(), onupdate=db.func.now())

    @property
    def data(self):
        return {
            'id':self.id,
            'name':self.name,
            'email':self.email,
            'password':self.password,
            'pekerjaan':self.pekerjaan,
            'gender':self.gender,
            'umur':self.gender,

        }
    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all(cls):
        r = cls.query.all()
        result =[]

        for i in r:
            result.append(i.data)
        return result
    
    @classmethod
    def get_by_id(cls,id):
        return cls.query.filter(cls.id == id).first()






