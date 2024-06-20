from marshmallow import Schema, fields
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.service.usuario_service import authenticate, register_usuario
from app import login_manager

auth_bp = Blueprint('auth', __name__)

class UsuarioSchema(Schema):
    nome = fields.Str(required=False)
    username = fields.Str(required=False)
    password = fields.Str(required=False)
    data_nascimento = fields.Str(required=False)


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        usuario_schema = UsuarioSchema()
        usuario_data = usuario_schema.load(request.form)
            
        try:
            register_usuario(usuario_data)
        except Exception as e:
            flash(str(e))
            return render_template('register.html')

        flash('User created successfully!')
        return redirect(url_for('auth.login'))
    return render_template('register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        try:
            user = authenticate(username, password)
            if user:
                login_user(user)
                flash('Login successful!')
                return redirect(url_for('projeto.listar_projetos', user_id=user.id))
            else:
                flash('Invalid username or password.')
                return render_template('login.html')
            
        except Exception as e:
            flash(str(e))
            return render_template('login.html')
    return render_template('login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('auth.login'))