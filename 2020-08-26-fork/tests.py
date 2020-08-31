from api import db
from api.models.task import Task

if __name__ == "__main__":
    # Insere uma tarefa
    task = Task('lembrete', 'Estudar Flask!')
    db.session.add(task)
    db.session.commit()

    # Exibir tarefas cadastradas no banco
    tasks = Task.query.all()
    for task in tasks:
        print(task.title, task.content)
