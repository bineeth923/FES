
def is_admin(user):
    return user.groups.filter(name='Creater').exists()

def is_student(user):
    return user.groups.filter(name='Student').exists()

def is_teacher(user):
    return user.groups.filter(name='Teacher').exists()