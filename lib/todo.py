class ToDo():
    def __init__(self):
        self.task_list = []
    
    def add(self, task):
        if(task == ''):
            raise Exception('No task given!')
        self.task_list.append(task)
    