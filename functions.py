def get_todos(filepath = "todos.txt"):
    """

    :param filepath:
    :return:  the list of to-do items
    """
    with open(filepath,'r') as f:
        todos_local = f.readlines()
    return todos_local

def write_todos(todos_arg, filepath = "todos.txt"):
    with open(filepath,'w') as f:
        f.writelines(todos_arg)