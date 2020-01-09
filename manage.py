from application import manager, db

from flask_script.commands import ShowUrls, Server

from flask_migrate import MigrateCommand
import os
import sys
from models import *
from flask import current_app

manager.add_command('db', MigrateCommand)
manager.add_command('urls', ShowUrls)
manager.add_command('runserver', Server(port=8000))


@manager.command
def init_db():
    '''
    this command is drop databases
    :return:
    '''
    command = input('Are you sure? You will init your database if you input yes or y db start init:\n')
    if command.lower().strip() == 'yes' or command.lower().strip() == 'y':
        db.drop_all()
        db.create_all()
        print('db init finsh')


@manager.command
def drop_db():
    '''
    command is drop databases
    '''
    command = input('Are you sure? You will drop your database if you input yes or y db start init:\n')
    if command.lower().strip() == 'yes' or command.lower().strip() == 'y':
        db.drop_all()
        print('db drop finsh')


@manager.command
def test():
    '''
    command is find project test.py and run
    :return:
    '''
    if len(sys.argv) >= 1 and sys.argv[1] == 'test':
        return os.system('nosetests -w {BaseDir}'.format(BaseDir=current_app.root_path))


if __name__ == '__main__':
    manager.run()
