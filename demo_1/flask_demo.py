from flask import Flask,render_template,url_for,Markup
from flask_sqlalchemy import SQLAlchemy
from Config import Config
#plotly库
from plotly.offline import plot
from plotly.graph_objs import *
import numpy as np
app=Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


class User(db.Model):
	__tablename__='user'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80))
	email = db.Column(db.String(120))
	def __init__(self, username, email):
		self.username = username
		self.email = email
	
# @app.route('/')
# def hello_world():
# 	db.create_all()
# 	admin = User('admin','admin@example.com')
# 	guest = User('guest','guest@example.com')
# 	db.session.add(admin)
# 	db.session.add(guest)
# 	db.session.commit()
# 	return 'hello world'+str(url_for('next_index'))


@app.route('/login/')
def next_index():
	data=User.query.filter(User.username=='admin').first()
	print(data)
	return render_template('1.html')

def scatter():
  #产生数据
    N = 1000
    random_x = np.random.randn(N)
    random_y = np.random.randn(N)
#生成图表
    # Create a trace
    trace = Scatter(
        x = random_x,
        y = random_y,
        mode = 'markers'
    )
    layout = Layout(
         xaxis=XAxis( title='x 轴' ),
         yaxis=YAxis( type='log', title='GNP' )
    )

    data = [trace]
    fig = Figure(data=data, layout=layout)
    
    #返回plot对象
    return plot(fig,output_type='div')


@app.route("/")
def hello():
    my_plot_div = plot([Scatter(x=[1, 2, 3], y=[3, 1, 6])], output_type='div')
    my_plot_div2 = plot([Scatter(x=[1, 5, 3], y=[1, 1, 6])], output_type='div')
    my_plot_div1=scatter()
    return render_template('results.html',
                            div_placeholder=Markup(my_plot_div),
                            div_newmap=Markup(my_plot_div2),
                            div_newmap3=Markup(my_plot_div1),
                            )






if __name__=='__main__':
	app.run(debug=True)
