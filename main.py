import sqlite3
import argparse
from model.task import Task
from user import User
import pathlib
import sys


parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('--show_current', action='store_true', help='Show current tasks, you have to do')
parser.add_argument('--show_done', action='store_true', help='Show done tasks, you have done')
parser.add_argument('--database', action='store_true', help='Database Path')
args = parser.parse_args()


if __name__ == "__main__":
    if args.show_current:
        all_task = Task.get_active_done_tasks(True)
        for k, v in User.format_all(all_task).items():
            print(k, ' | '.join(v))
        sys.exit()
    if args.show_done:
        all_task = Task.get_active_done_tasks(False)
        for k, v in User.format_all(all_task).items():
            print(k, ' | '.join(v))
        sys.exit()
    if args.database:
        print(str(pathlib.Path().absolute()) + '/' + Task.__database__)
        sys.exit()

    start = input('To start work enter StartApp ')
    while True:
        next_cmd = input("Enter command: ")
        if next_cmd in ('Quit', 'Q', 'q', 'quit', 'exit', ':q'):
            break
        elif not next_cmd:
            continue
        else:
            next_cmd = next_cmd.split()

        # Next program is working with Add, Del, Find, Print
        if next_cmd[0] == 'Add':  # Add task and date
            try:
                date = User.convert_data(next_cmd[1])
                task = ' '.join(next_cmd[2:])
                save = Task(date, task)
            except:
                print('Something was wrong')
        elif next_cmd[0] == 'Del':  # Main Del
            if len(next_cmd) == 2:
                date = User.convert_data(next_cmd[1])
                result = Task.del_date(date)
                print(f'Deleted {result} events')
            elif len(next_cmd) >= 3:  # Del Date Task
                date = User.convert_data(next_cmd[1])
                task = ' '.join(next_cmd[2:])
                try:
                    Task.del_task(date, task)
                    print('Deleted successfully')
                except:
                    print('Event not found')
        elif next_cmd[0] == 'Find':  # Find Date
            date = User.convert_data(next_cmd[1])
            from_db = Task.find_data(date)
            for i in User.convert_find(from_db):
                print(i)
        elif next_cmd[0] == 'Print':  # Print all task on db
            all_task = Task.print_all()
            for k, v in User.format_all(all_task).items():
                print(k, ' | '.join(v))
        else:
            continue
