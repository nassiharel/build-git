
def start(args):
    print('algorithm: start')
  
    input = args['input']
    array = input[0]
    order = input[1]
    if order == 'asc':
        reverse = False
    elif order == 'desc':
        reverse = True
    else:
        raise Exception('order not supported')

    list.sort(array, reverse=reverse)
    return array


