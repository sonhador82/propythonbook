from typing import Dict
from datetime import datetime
import sys
from database.manager import DatabaseManager


db = DatabaseManager('/tmp/bookmarks.sqlite3')


class CreateBookmarksTableCommand:
    def execute(self):
        db.create_table('bookmarks', {
            'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
            'title': 'TEXT NOT NULL',
            'url': 'TEXT NOT NULL',
            'notes': 'TEXT',
            'date_added': 'TEXT NOT NULL'
        })


class AddBookmarkCommand:
    def execute(self, data: Dict):
        data ['date_added'] = datetime.utcnow().isoformat()
        db.add('bookmarks', data)
        return 'Bookmark added!'


class ListBookmarkCommand:
    def __init__(self, order_by='date_added'):
        self.order_by = order_by

    def execute(self):
        return db.select('bookmarks', order_by=self.order_by).fetchall()


class DeleteBookmarkCommand:
    def execute(self, data: Dict):
        db.delete('bookmarks', {'id': data})
        return 'Bookmark deleted!'


class QuitCommand:
    def execute(self):
        sys.exit()
