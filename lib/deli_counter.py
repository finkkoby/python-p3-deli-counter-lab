def line(queue_list):
    if len(queue_list) == 0:
        print("The line is currently empty.")
    else:
        i = 0;
        name_str = []
        while i < len(queue_list):
            name_str.append(f"{i + 1}. {queue_list[i]}")
            i += 1
        names = " ".join(name_str)
        print(f"The line is currently: {names}")
def take_a_number(queue_list, name):
    queue_list.append(name)
    print(f"Welcome, {name}. You are number {len(queue_list)} in line.")
def now_serving(queue_list):
    if len(queue_list) > 0:
        print(f"Currently serving {queue_list[0]}.")
        queue_list.pop(0)
    else:
        print("There is nobody waiting to be served!")

