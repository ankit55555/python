import sqlite3
import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

#setting connection
conn = sqlite3.connect('scheme_database.db')
# conn.execute('''CREATE TABLE scheme(scheme_code INT PRIMARY KEY  NOT NULL,scheme_name  TEXT    NOT NULL);''')



# fetch the data from mftool
from mftool import Mftool
mf = Mftool()
all_scheme_codes = mf.get_scheme_codes()
print(type(all_scheme_codes))


#inserting data into table 
for i in all_scheme_codes.keys():
    conn.execute("insert into scheme values (?,?)",(i,all_scheme_codes[i]))

for row in conn.execute('SELECT * FROM scheme'):
    print(row)
conn.commit()
conn.close()




# endpoints for homepage
@app.route('/', methods=['GET'])
def home():
    return '''<h1>This is the homepage</h1>
<p>It will give a list of mutual funds scheme and scheme codes</p>'''


#endpoints for mutual funds scheme and scheme codes
@app.route('/api/mutual', methods=['GET'])
def api_all():
    return jsonify(all_scheme_codes)

app.run(port=5005)