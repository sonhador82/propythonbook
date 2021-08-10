from commands import commands


class Option:
    def __init__(self, name, command, prep_call=None):
        self.name = name
        self.command = command
        self.prep_call = prep_call

    def choose(self):
        data = self.prep_call() if self.prep_call else None
        message = self.command.execute(data) if data else self.command.execute()
        print(message)

    def __str__(self):
        return self.name


def print_options(options):
    for shortcut, option in options.items():
        print(f'({shortcut}) {option}')
        print()


def option_choise_is_valid(choice, options):
    return choice in options or choice.upper() in options


def get_option_choice(options):
    choice = input("Choose: ")
    while not option_choise_is_valid(choice, options):
        print("Bad choice")
        choice = input("Choose: ")
    return options[choice.upper()]


def get_user_input(label, required=True):
    value = input(f'{label}: ') or None
    while required and not value:
        value = input(f'{label}: ') or None
    return value


def get_new_bookmark_data():
    return {
        'title': get_user_input('Title'),
        'url': get_user_input('Url'),
        'notes': get_user_input('Notes', required=False)
    }


def get_bookmark_id_for_deletion():
    return get_new_bookmark_data('Enter ID to delete: ')


if __name__ == '__main__':
    print("Welcome to bark!")
    commands.CreateBookmarksTableCommand().execute()
    options = {
        'A': Option('Add bookmark', commands.AddBookmarkCommand(), prep_call=get_new_bookmark_data),
        'B': Option('Show bookmarks by date', commands.ListBookmarkCommand()),
        'T': Option('Show bookmarks by title', commands.ListBookmarkCommand(order_by='title')),
        'D': Option('Delete bookmark', commands.DeleteBookmarkCommand(), prep_call=get_bookmark_id_for_deletion),
        'Q': Option('Quit', commands.QuitCommand())
    }
    print_options(options)
    chosen_option = get_option_choice(options)
    chosen_option.choose()


