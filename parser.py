def get_token(lst):
    if not lst:
        return '', []
    if lst[0] == '(' or lst[0] == ')':
        return lst[0], lst[1:]
    if lst[0] == ' ':
        return '', lst[1:]

    tokens = get_token(lst[1:])

    if tokens[0] != ')':
        return lst[0] + tokens[0], tokens[1]
    else:
        return lst[0], [tokens[0]] + tokens[1]


def tokenize(string):

    if string == '' or not string:
        return []

    if string[0] == ' ':
        string = string[1:]

    # ensures that the space removed was not a trailing space
    if string == '' or not string:
        return []

    tokens = get_token([c for c in string])

    return [tokens[0]] + tokenize(''.join(tokens[1]))


def get_semantic_tree_r(input_, L):
    if len(input_) == 0:
        return L[0]
    token = input_.pop(0)
    if token == '(':
        return get_semantic_tree_r(input_,
                                   L + [get_semantic_tree_r(input_, [])])
    elif token == ')':
        return L
    else:
        return get_semantic_tree_r(input_, L + [getatom(token)])


def get_semantic_tree(input_):
    return [] if not input_ else get_semantic_tree_r(tokenize(input_), [])


def getatom(token):
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            return token


#print get_token([c for c in 'sqrt 3)'])
#print get_token([c for c in '(sqrt 3)'])
