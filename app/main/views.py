from datetime import datetime
from flask import render_template, session, redirect, url_for
from flask.ext.login import login_user,logout_user,login_required
from . import main
#from forms import  NameForm
from .. import db
from ..models import User

@main.route('/', methods = ['GET', 'POST'])
def index():
	return render_template('index.html')

@main.route('/main', methods = ['GET', 'POST'])
@login_required
def main():
	return render_template('console.html')