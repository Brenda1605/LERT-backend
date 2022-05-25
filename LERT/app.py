from flask import jsonify, Flask
from sqlalchemy import *
from LERT.db import database, session
from LERT.user.views import user
from LERT.administrator.views import admin
from LERT.icaAdmin.views import icaAdmin
from LERT.resource.views import resource
from LERT.expense.views import expense
from LERT.resourceExpense.views import resourceExpense

from db2_Connection import Db2Connection

app = Flask(__name__)

def create_app():
    app.config.from_object('config.DevelopmentConfig')
    database
    session
  
app.register_blueprint(user)
app.register_blueprint(admin)
app.register_blueprint(icaAdmin)
app.register_blueprint(resource)
app.register_blueprint(expense)
app.register_blueprint(resourceExpense)

#sentence = "SELECT * FROM OOLONG"
#rows = connection.get_all(sentence)
#print(rows)
#connection._create_connection_sqlAlchemy()

# @app.route("/")
# def hello():
#     return "<h1 style='color:blue'>Hello There!</h1>"

# @app.route("/user")
# def get_user():
#     Dictionary ={'id':'eduCBA' , 'user_name':'Premium' , 'user_last_name':'2709 days'}
#     return jsonify(Dictionary)

if __name__ == "__main__":
    create_app().run()