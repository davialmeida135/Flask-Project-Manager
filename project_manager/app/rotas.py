import random
import string
import datetime
from flask import (
    abort,
    Blueprint, 
    redirect, 
    request, 
    render_template, 
    url_for
)

from .db import get_db
from .db import usuario,tarefa,projeto

main = Blueprint("main", __name__)

@main.context_processor
def get_room_types():
    room_types = []
    return dict(room_types=room_types)

@main.get("/")
def index():
    #projeto.create_projeto(1,datetime.datetime.now(),"projetaoaoaoao","descriptiotnt", datetime.datetime.now(),[1,2,3])
    #tarefa.create_tarefa("novatarefa", datetime.datetime.now(), "descrição legal", datetime.datetime.now(), "em andamento", 1, [1,2,3])
    #tarefa.update_tarefa(1,"Editada", datetime.datetime.now(), "descrição muito massa", datetime.datetime.now(), "em andamento", 1, [1,3])
    
    return render_template("create_tarefa.html")