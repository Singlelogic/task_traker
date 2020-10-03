import sqlite3
import unittest
from task import Task


class TestTask(unittest.TestCase):
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    query_create = 'CREATE TABLE IF NOT EXISTS test_tasks (id INTEGER PRIMARY KEY, date TEXT, task TEXT, done TEXT)'
    cur.execute(query_create)

    Task.__tablename__ = 'test_tasks'
    task1 = Task("2020-10-01", "1")
    task2 = Task("2020-10-02", "2")
    task3 = Task("2020-10-03", "3")
    task4 = Task("2020-10-04", "4")
    task5 = Task("2020-10-05", "5")

    def test_get_date(self):
        self.assertEqual(TestTask.task1.get_date(), "2020-10-01")
        self.assertEqual(TestTask.task2.get_date(), "2020-10-02")
        self.assertEqual(TestTask.task3.get_date(), "2020-10-03")
        self.assertEqual(TestTask.task4.get_date(), "2020-10-04")
        self.assertEqual(TestTask.task5.get_date(), "2020-10-05")

    def test_get_event(self):
        self.assertEqual(TestTask.task1.get_event(), "1")
        self.assertEqual(TestTask.task2.get_event(), "2")
        self.assertEqual(TestTask.task3.get_event(), "3")
        self.assertEqual(TestTask.task4.get_event(), "4")
        self.assertEqual(TestTask.task5.get_event(), "5")

    def test_save(self):
        TestTask.task1.save()
        TestTask.task2.save()
        TestTask.task3.save()
        TestTask.task4.save()
        TestTask.task5.save()
        for i in range(1, 6):
            query_select = f"SELECT * FROM test_tasks WHERE date='2020-10-0{i}' and task='{i}'"
            for row in TestTask.cur.execute(query_select):
                answer = (row[1], row[2])
            self.assertEqual(answer, (f'2020-10-0{i}', f'{i}'))

    def test_z_find_task(self):
        self.assertEqual(Task.find_task("2020-10-01")[0].get_date(), "2020-10-01")
        self.assertEqual(Task.find_task("2020-10-02")[0].get_date(), "2020-10-02")
        self.assertEqual(Task.find_task("2020-10-03")[0].get_date(), "2020-10-03")
        self.assertEqual(Task.find_task("2020-10-04")[0].get_date(), "2020-10-04")
        self.assertEqual(Task.find_task("2020-10-05")[0].get_date(), "2020-10-05")

        self.assertEqual(len(Task.find_task()), 5)

    def test_zz_delete(self):
        conn = sqlite3.connect('db.sqlite3')
        cur = conn.cursor()
        query_delete = f"DROP TABLE IF EXISTS {Task.__tablename__}"
        cur.execute(query_delete)
        conn.close()


if __name__ == "__main__":
    unittest.main()
