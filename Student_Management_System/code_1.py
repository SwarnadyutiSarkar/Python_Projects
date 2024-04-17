import sqlite3

# Initialize SQLite database
def initialize_db():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    
    # Create students table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        grade INTEGER NOT NULL
    )
    ''')
    
    conn.commit()
    conn.close()

# Add a new student
def add_student(name, age, grade):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO students (name, age, grade) VALUES (?, ?, ?)
    ''', (name, age, grade))
    
    conn.commit()
    conn.close()

# Display all students
def display_students():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Grade: {student[3]}")
    
    conn.close()

# Update student details
def update_student(id, name, age, grade):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    UPDATE students SET name=?, age=?, grade=? WHERE id=?
    ''', (name, age, grade, id))
    
    conn.commit()
    conn.close()

# Delete a student
def delete_student(id):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM students WHERE id=?', (id,))
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    initialize_db()
    
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            grade = int(input("Enter student grade: "))
            add_student(name, age, grade)
        
        elif choice == '2':
            display_students()
        
        elif choice == '3':
            id = int(input("Enter student ID to update: "))
            name = input("Enter new name: ")
            age = int(input("Enter new age: "))
            grade = int(input("Enter new grade: "))
            update_student(id, name, age, grade)
        
        elif choice == '4':
            id = int(input("Enter student ID to delete: "))
            delete_student(id)
        
        elif choice == '5':
            break
        
        else:
            print("Invalid choice. Please try again.")
