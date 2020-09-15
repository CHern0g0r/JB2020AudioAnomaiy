import controller

def print_help(args):
    print('Usage:')
    print('    <command> [params]\n')
    print('Commands:')
    print('    exit')
    print('    reverse [input file] [output file]')
    print('    crop [input file] [list of intervals in seconds]')
    print('    concat [input files list] [output file]')


def reverse(args):
    if len(args) == 2:
        controller.reverse(args[0], args[1])


def crop(args):
    if len(args) > 2:
        controller.crop(args[0], list(map(int, args[1:])))


def concat(args):
    if len(args) > 1:
        controller.concatenate(args[:-1], args[-1])


command_list = {
    'reverse': reverse,
    'crop': crop,
    'concat': concat,
    'help': print_help
}

command = input().split()
while not command[0] == 'exit':
    command_list[command[0]](command[1:])
    command = input().split()