INSERT INTO Usuario (nome,username) VALUES ('John Doe','doe1997');
INSERT INTO Usuario (nome,username) VALUES ('Jane Smith','jane2003');
INSERT INTO Usuario (nome,username) VALUES ('Alice Johnson','alice1999');
INSERT INTO Usuario (nome,username) VALUES ('Bob Brown','bobao');
INSERT INTO Usuario (nome,username) VALUES ('Charlie Davis','charlies1990');

INSERT INTO Projeto (idGerente, data_inicio, nome, descricao, data_fim)
VALUES (1, '2023-01-01', 'Project Alpha', 'Description for Project Alpha', '2023-12-31');

INSERT INTO Projeto (idGerente, data_inicio, nome, descricao, data_fim) 
VALUES (2, '2023-02-01', 'Project Beta', 'Description for Project Beta', '2023-11-30');

INSERT INTO Projeto (idGerente, data_inicio, nome, descricao, data_fim) 
VALUES (1, '2023-03-01', 'Project Gamma', 'Description for Project Gamma', '2023-10-31');

INSERT INTO Projeto (idGerente, data_inicio, nome, descricao, data_fim) 
VALUES (3, '2023-04-01', 'Project Delta', 'Description for Project Delta', '2023-09-30');

INSERT INTO Projeto (idGerente, data_inicio, nome, descricao, data_fim) 
VALUES (2, '2023-05-01', 'Project Epsilon', 'Description for Project Epsilon', '2023-08-31');

INSERT INTO Tarefa (nome, data_criacao, descricao, prazo, status, idProjeto) 
VALUES ('Task 1', '2023-06-01', 'Description for Task 1', '2023-07-01', 'Pending', 1);

INSERT INTO Tarefa (nome, data_criacao, descricao, prazo, status, idProjeto) 
VALUES ('Task 2', '2023-06-05', 'Description for Task 2', '2023-07-05', 'In Progress', 1);

INSERT INTO Tarefa (nome, data_criacao, descricao, prazo, status, idProjeto) 
VALUES ('Task 3', '2023-06-10', 'Description for Task 3', '2023-07-10', 'Completed', 2);

INSERT INTO Tarefa (nome, data_criacao, descricao, prazo, status, idProjeto) 
VALUES ('Task 4', '2023-06-15', 'Description for Task 4', '2023-07-15', 'Pending', 3);


INSERT INTO Usuario_Projeto (idUsuario, idProjeto) VALUES (1, 1);
INSERT INTO Usuario_Projeto (idUsuario, idProjeto) VALUES (2, 1);
INSERT INTO Usuario_Projeto (idUsuario, idProjeto) VALUES (3, 2);
INSERT INTO Usuario_Projeto (idUsuario, idProjeto) VALUES (4, 3);
INSERT INTO Usuario_Projeto (idUsuario, idProjeto) VALUES (5, 3);

INSERT INTO Usuario_Tarefa (idUsuario, idTarefa) VALUES (1, 1);
INSERT INTO Usuario_Tarefa (idUsuario, idTarefa) VALUES (2, 1);
INSERT INTO Usuario_Tarefa (idUsuario, idTarefa) VALUES (3, 2);
INSERT INTO Usuario_Tarefa (idUsuario, idTarefa) VALUES (4, 3);
INSERT INTO Usuario_Tarefa (idUsuario, idTarefa) VALUES (5, 4);
