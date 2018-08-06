from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from . import auth
from ..models import User
from .forms import LoginForm

@auth.route('/login', methods=['POST', 'GET'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user is not None and user.varify_password(form.password.data):
			login_user(user)
			flash('Welcome. ', 'success')
			return redirect(url_for('main.index'))
		else:
			flash('Invalid email and/or password.', 'danger')
			return render_template('auth/login.html', form=form)
	return render_template('auth/login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
	logout_user()
	flash('Logged out', 'success')
	return redirect(url_for('auth.login'))

