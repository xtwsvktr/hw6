import  sqlite3



db = sqlite3.connect('hw7.db')
c = db.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS
student(
name TEXT,
surname TEXT,
hobby TEXT,
birthday DATE NOT NULL,
grade INTEGER
);
''')

students = [('Андрей', 'Егоров', "2004", 'дота', 10),
            ('Мойдунов', 'Дастан', "2004", 'английский', 9),
            ('Аскарбеков', 'Эмирлан', '2004', 'футбол', 13),
            ('Алымкулов', 'Аман', '2002', 'химбио', 16),
            ('Маматджанов', 'Эмир', '2001', 'баскетбол', 9),
            ('Тян', 'Карина', '2006', 'фотограф', 5),
            ('Ткачук', 'Эмиль', '2004', 'гимнастика', 8),
            ('Мевязов', 'Алим', '2005', 'графический дизайн', 10),
            ('Ткачук', 'Руслан', '2007', 'танцы', 3),
            ('Шишкин', 'Станислав', '2005', 'программирование', 15)]
c.executemany('INSERT INTO student (name, surname, birthday, hobby, grade) VALUES (?, ?, ?, ?, ?)', students)
db.commit()

while True:

    request = int(input("[ Хотите добавить >> напишите >> 1 ] [ а если нет >> 0 ] \nЧто вы хотите >> "))
    print()
    if request == 1:
        name = input('Имя: ')
        surname = input('Фамилия: ')
        hobby = input('Хобби: ')
        birthday = input('День рождения [год-месяц-день]: ')
        grade = int(input('Оценка [до 100]: '))
        c.execute('INSERT INTO student VALUES(?, ?, ?, ?, ?)', (name, surname, hobby, birthday, grade))
        db.commit()
        print()
    else:
        break


while True:
    request = int(input("[ Удалить одного >> напишите >> 1 ] [ Удалить всех >> напишите >> 2 ] [ Не удалять >> напишите >> 0 ] \nЧто вы хотите >> "))
    print()
    if request == 1:
        name_delete = input("Кого удалить (напишите имя): ")
        c.execute("DELETE FROM student WHERE name = ?", (name_delete,))
        print()
    if request == 2:
        c.execute("DELETE FROM student WHERE rowid > 0")
        break
    else:
        break

print("Студенты с фамилией более 10 символов:")
c.execute('SELECT  * FROM student WHERE length(surname) > 10')
for i in c.fetchall():
    print(i)

print()
print("Студенты с именем 'genius':")
c.execute('UPDATE student SET name = "genius" WHERE grade > 10')
c.execute('SELECT rowid, * FROM student WHERE name = "genius"')
for i in c.fetchall():
    print(i)

c.execute('DELETE FROM student WHERE rowid % 2 = 0')
print()
print('Студентов у которых нечетное id: ')
c.execute('SELECT rowid, * FROM student')
for i in c.fetchall():
    print(i)

db.commit()
db.close()