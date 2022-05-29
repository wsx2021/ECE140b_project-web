from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.renderers import render_to_response
from pyramid.response import FileResponse
import mysql.connector as mysql
import os

db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']
db_name = os.environ['MYSQL_DATABASE']
db_host = os.environ['MYSQL_HOST']

def get_home(req):
  # Connect to the database and retrieve the users
  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  cursor.execute("select first_name, last_name, position, description from Users;")
  records = cursor.fetchall()
  db.close()

  return render_to_response('templates/home.html', {'users': records}, request=req)

def get_kvp(req):
  # Connect to the database and retrieve the users
  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  cursor.execute("select first_name, last_name, position, description from Users;")
  records = cursor.fetchall()
  db.close()
  print("kvp page")
  return render_to_response('templates/kvp.html', {'users': records}, request=req)

def get_product(req):
  # Connect to the database and retrieve the users
  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  cursor.execute("select first_name, last_name, position, description from Users;")
  records = cursor.fetchall()
  db.close()
  print("kvp page")
  return render_to_response('templates/product.html', {'users': records}, request=req)  

def get_design(req):
  # Connect to the database and retrieve the users
  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  cursor.execute("select first_name, last_name, position, description from Users;")
  records = cursor.fetchall()
  db.close()

  return render_to_response('templates/ui_example.html', {'users': records}, request=req)  

def get_mvp(req):
  # Connect to the database and retrieve the users
  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  cursor.execute("select first_name, last_name, position, description from Users;")
  records = cursor.fetchall()
  db.close()

  return render_to_response('templates/mvp.html', {'users': records}, request=req)  

def get_revenue(req):
  # Connect to the database and retrieve the users
  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  cursor.execute("select first_name, last_name, position, description from Users;")
  records = cursor.fetchall()
  db.close()

  return render_to_response('templates/revenue.html', {'users': records}, request=req) 

def get_source(req):
  # Connect to the database and retrieve the users
  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  cursor.execute("select first_name, last_name, position, description from Users;")
  records = cursor.fetchall()
  db.close()

  return render_to_response('templates/source.html', {'users': records}, request=req) 

def get_pivot(req):
  # Connect to the database and retrieve the users
  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  cursor.execute("select first_name, last_name, position, description from Users;")
  records = cursor.fetchall()
  db.close()

  return render_to_response('templates/pivot.html', {'users': records}, request=req) 


''' Route Configurations '''
if __name__ == '__main__':
  config = Configurator()

  config.include('pyramid_jinja2')
  config.add_jinja2_renderer('.html')

  config.add_route('get_home', '/')
  config.add_view(get_home, route_name='get_home')
  config.add_route('get_home_page', '/home')
  config.add_view(get_home, route_name='get_home_page')
  config.add_route('kvp', '/kvp')
  config.add_view(get_kvp, route_name='kvp')
  config.add_route('product', '/product')
  config.add_view(get_product, route_name='product')
  config.add_route('ui_example', '/ui_example')
  config.add_view(get_design, route_name='ui_example')
  config.add_route('mvp', '/mvp')
  config.add_view(get_mvp, route_name='mvp')
  config.add_route('revenue', '/revenue')
  config.add_view(get_revenue, route_name='revenue')

  config.add_route('source', '/source')
  config.add_view(get_source, route_name='source')
  config.add_route('pivot', '/pivot')
  config.add_view(get_pivot, route_name='pivot')

  config.add_static_view(name='/', path='./public', cache_max_age=3600)

  app = config.make_wsgi_app()
  server = make_server('0.0.0.0', 6000, app)
  server.serve_forever()