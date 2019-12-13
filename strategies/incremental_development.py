from pprint import pprint

tree = {
    'one': [
        'abc',
        'def',
        'ghi',
        {
            'four': 4,
            'five': 5
        }
    ],
    'two': [
        'jkl',
        'mno',
        'BLUE',
        {
            'six': 6,
            'seven': 7
        }
    ],
    'three': [
        'qrs',
        'BLUE',
        'BLUE',
        {
            'eight': 'BLUE',
            'nine': 9
        }
    ]
}

problem = '''
    Given a target find path to it, starting with any node in tree
    tree['two'][3]['seven'] -> 7
'''

strategy = '''
    Solve related by simpler problem
    Incremental development
'''


def countem(node, target):
    """ Count the number of Occurences of target """
    if node == target:
        return 1
    return 0


def countem(node, target):
    """ Count the number of Occurences of target """
    if node == target:
        return 1
    if isinstance(node, list):
        return sum(countem(child, target) for child in node)
    return 0


def countem(node, target):
    """ Count the number of Occurences of target """
    if node == target:
        return 1
    elif isinstance(node, list):
        return sum(countem(child, target) for child in node)
    elif isinstance(node, dict):
        return sum(countem(child, target) for child in node.values())
    return 0


def path_to(node, target):
    if node == target:
        return f' -> {target!r}'
    elif isinstance(node, list):
        for child_id, child in enumerate(node):
            path = path_to(child, target)
            if path != '':
                return f'[{child_id}]{path}'
    elif isinstance(node, dict):
        for key, child in node.items():
            path = path_to(child, target)
            if path != '':
                return f'[{key!r}]{path}'
    return ''


if __name__ == "__main__":

    print('node: green', 'target: blue', countem('green', 'blue'))
    print(countem('blue', 'blue'))

    colors = ['red', 'blue', 'blue', 'green', ['blue', 'green', 'red']]
    print(f'node: {colors}', 'target: blue', countem(colors, 'blue'))

    colors = ['red', 'blue', 'blue', 'green', {'BLUE': 'blue', 'GREEN': 'green', 'RED':'red'}]
    print(f'node: {colors}', 'target: blue', countem(colors, 'blue'))

    print(f'node: {tree}', 'target: 7', countem(tree, 7))

    print(path_to(tree, 7))
    print(path_to('abc', 'abc'))
    print(path_to(['?', '?', 'abc', '?'], 'abc'))
    print(path_to(['?', '?', ['?', '?', 'abc'], '?'], 'abc'))
    print(path_to(tree, 'abc'))