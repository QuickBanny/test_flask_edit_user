from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from . import main
from .forms import AddUserForm, EditUserForm
from ..models import User
from app import db

@main.route('/')
def index():
	list_users = User.query.all()
	return render_template('main/index.html', current_user=current_user, list_users = list_users)


@main.route('/add_user', methods=['GET', 'POST'])
@login_required
def add_user():
	if current_user.admin == True:
		form = AddUserForm()
		if form.validate_on_submit():
			user = User(email = form.email.data,
						password = form.password.data,
						admin = False)
			db.session.add(user)
			db.session.commit()
			flash('A confirmation add user.', 'success')
			return redirect(url_for('main.index'))
		return render_template('main/add_user.html', form=form)
	return redirect(url_for('main.index'))

@main.route('/edit_user/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_user(id):
	if current_user.admin == True:
		user = User.query.get_or_404(id)
		form = EditUserForm(user=user)
		if form.validate_on_submit():
			user.email = form.email.data
			user.admin = form.admin.data
			db.session.add(user)
			db.session.commit()
			return redirect(url_for('main.index'))
		form.email.data = user.email
		form.admin.data = user.admin
		return render_template('main/edit_user.html', form=form)
	return redirect(url_for('main.index'))

@main.route('/delete_user/<int:id>', methods=['GET'])
@login_required
def delete_user(id):
	if current_user.admin == True:
		user = User.query.get_or_404(id)
		db.session.delete(user)
		db.session.commit()
		flash('Delete success. ', 'danger')
		return redirect(url_for('main.index'))
	return redirect(url_for('main.index'))
