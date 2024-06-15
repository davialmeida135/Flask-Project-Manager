from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from service.usuario_service import register_usuario, delete_usuario, authenticate
from app.db.usuario import Usuario

auth_bp = Blueprint('auth', __name__)

#TODO apenas esqueleto esta feito

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nome = request.form['nome']
        username = request.form['username']
        password = request.form['password']

        try:
            register_usuario(nome, username, password)
        except Exception as e:
            flash(str(e))
            return render_template('register.html')

        flash('User created successfully!')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = authenticate(username, password)
        if user:
            login_user(user)
            flash('Login successful!')
            return redirect(url_for('main.index'))
        else:
            flash('Invalid username or password.')
            return render_template('auth/login.html')
    return render_template('auth/login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('auth.login'))