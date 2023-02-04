master_process = []
sub_process = []

###########-----Master  Process----#############
def append_master_process(id):
    if id not in master_process:
        master_process.append(id)
    return

def remove_master_process(id):
    if id in master_process:
        master_process.remove(id)
        return True
    else:
        return False

def get_master_process():
    return master_process


###########---Sub Process--############
def append_sub_process(id):
    if id not in sub_process:
        sub_process.append(id)
    return

def remove_sub_process(id):
    if id in sub_process:
        sub_process.remove(id)
        return True
    else:
        return False

def get_sub_process():
    return sub_process