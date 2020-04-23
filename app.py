from flask_restful import Resource, Api
from flask import Flask, Response, request, json, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:3306/kampus'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)



# ini adalamat materi pertemuan 6
class Mhs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nim = db.Column(db.String(10), unique=True)
    nama = db.Column(db.String(20))
    kelas = db.Column(db.String(20))
    alamat= db.Column(db.String(20))

    def __init__(self, nim, nama, kelas, alamat):
        self.nim = nim
        self.nama = nama
        self.kelas = kelas
        self.alamat = alamat

    @staticmethod
    def get_all_users():
        return Mhs.query.all()


class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('nim', 'nama', 'alamat')


user_schema = UserSchema()
users_schema = UserSchema(many=True)


@app.route('/mahasiswa', methods=['POST'])
def add_user():
    nim = request.json['nim']
    nama = request.json['nama']
    alamat = request.json['alamat']

    new_mhs = Mhs(nim, nama, alamat)

    db.session.add(new_mhs)
    db.session.commit()

    return user_schema.jsonify(new_mhs)

@app.route('/mahasiswa', methods=['GET'])
def get_users():
    all_users = Mhs.get_all_users()
    result = users_schema.dump(all_users)
    return jsonify(result)

@app.route('/mahasiswa/<id>', methods=['GET'])
def get_user(id):
  mahasiswa = Mhs.query.get(id)
  return user_schema.jsonify(mahasiswa)

@app.route('/mahasiswa/<id>', methods=['PUT'])
def update_user(id):
  mahasiswa = Mhs.query.get(id)

  nim = request.json['nim']
  nama = request.json['nama']
  alamat = request.json['alamat']

  mahasiswa.nim = nim
  mahasiswa.nama = nama
  mahasiswa.alamat = alamat

  db.session.commit()

  return user_schema.jsonify(mahasiswa)

@app.route('/mahasiswa/<id>', methods=['DELETE'])
def delete_product(id):
  mahasiswa = Mhs.query.get(id)
  db.session.delete(mahasiswa)
  db.session.commit()

  return user_schema.jsonify(mahasiswa)
# materi pertemuan 6 berakhir di sini


if __name__ == '__main__':
    app.run()
