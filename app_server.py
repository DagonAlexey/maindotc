from flask import Flask, jsonify, request
from pony.orm import *
from pony import orm
db = Database('sqlite', 'mydb.sqlite', create_db=True)
class Notes(db.Entity):
    id = PrimaryKey(int, auto=True)
    title = Required(str)
    content = Required(str)

db.generate_mapping(create_tables=True)
orm.set_sql_debug(True)

@db_session
def print_notes():
    all_notes = []
    n = select(p for p in Notes)
    for p in n:
        d = {'id': p.id, 'title': p.title, 'content': p.content}
        all_notes.append(d)
    return all_notes


@db_session
def add_notes_(_title, _content):
    Notes(title=_title, content=_content)
    commit()

@db_session
def del_notes_(del_id):
    Notes.select(lambda p: p.id == del_id ).delete(bulk=True)
    commit()

@db_session
def change_notes_(change_id, _title, _content):
    row = Notes[change_id]
    row.title=_title
    row.content=_content
    commit()

app_server = Flask(__name__)
app_client = app_server.test_client()

notes =  print_notes()

@app_server.route('/', methods=['GET'])
def get_notes():
    return jsonify(print_notes())

@app_server.route('/', methods=['POST'])
def add_notes():
    recording = request.json
    add_notes_(recording['title'], recording['content'])
    return jsonify(notes)

@app_server.route('/<int:del_id>', methods=['DELETE'])
def del_notes(del_id):
    del_notes_(del_id)
    return jsonify(notes)


@app_server.route('/<int:change_id>', methods=['PUT'])
def change_notes(change_id):
    recording = request.json
    change_notes_(change_id, recording['title'], recording['content'])
    return jsonify(notes)

if __name__ == "__main__":
    app_server.run(debug=True)