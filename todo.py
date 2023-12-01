task_list = []

def add_task(*task):

    global task_list

    task_list.extend(task)

    return(task_list)

def remove_task(task):

    global task_list

    if task in task_list:

        task_list.remove(task)
    
    else:
        print('You do not have that task')

def change_task(task,new_task):

    global task_list

    if task in task_list:
        index = task_list.index(task)
        task_list[index] = new_task 
    else:
        print('You do not have that task')
    

def view_tasks():
    global task_list 

    return task_list


add_task('test','hello','bye')
remove_task('test')
change_task('hello','hi')
print(view_tasks())
