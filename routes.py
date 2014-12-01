from flask import Flask, request, jsonify
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://looklet:L00klet@prodimages.ny.bluefly.com:3301/www_django'

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'mysql://looklet:L00klet@prodimages.ny.bluefly.com:3301/www_django')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

from flask import Flask, request, jsonify

@app.route('/looklet-shot-list-flask/<int:id>', methods=['GET','POST','PUT'])
def lookletshots():
    if request.method == 'GET':
        results = LookletShotList.query.limit(10).offset(0).all()
        #result = LookletShotList.query.filter_by(id=id).first()

        json_results = []
        for result in results:
            d = {'colorstyle': result.colorstyle,
               'photodate': result.photodate,
               'reshoot': result.reshoot,
               'notes': result.notes,
               'timestamp': result.timestamp,
               'username': result.username}
            json_results.append(d)

        return jsonify(items=json_results)

    elif request.method == 'POST':


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
