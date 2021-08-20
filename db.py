from pony.orm import *
from pony import orm
db = Database('sqlite', 'mydb.sqlite', create_db=True)
class Notes(db.Entity):
    id = PrimaryKey(int, auto=True)
    title = Required(str)
    content = Required(str)

db.generate_mapping(create_tables=True)
orm.set_sql_debug(True)



