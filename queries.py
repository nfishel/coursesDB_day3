from cs50 import SQL

# connect to database
db = SQL("sqlite:///courses.db")


# C.R.U.D. functions to query the database

# this function will add a new course to our courses table
def add_new_course(name, teacher, room, dept):
  query = """INSERT INTO courses
                (name, teacher, room, department)
                VALUES (?, ?, ?, ?)"""
  row_id = db.execute(query, name, teacher, room, dept)
  return row_id

# this function will grab all the courses from the database
def get_all_courses():
  #query = """SELECT * FROM courses ORDER BY department"""
  query = """SELECT 
                courses.id, 
                courses.name, 
                teacher, 
                room, 
                departments.name AS dept 
             FROM courses 
             JOIN departments ON 
                courses.department = departments.id"""
  # this will return a list of dictionaries
  return db.execute(query)


# this funciton will get all the info for a specific course based on the id
def get_course_info(id):
  query = """SELECT * FROM courses WHERE id = ?"""
  # return the one dictionary from the list
  return db.execute(query, id)[0]
  

# this function will update a course info based on the id
def update_course(id, name, teacher, room, dept):
  query = """UPDATE courses SET
                name = ?,
                teacher = ?,
                room = ?,
                department = ?
             WHERE id = ?"""
  return db.execute(query, name, teacher, room, dept, id)


# this function will delete a course from the table
def remove_course(id):
  query = """DELETE FROM courses WHERE id = ?"""
  return db.execute(query, id)



# this function will add a new department to the departments table
def add_new_department(deptName, chair):
  query = """INSERT INTO departments
                (name, chair)
                VALUES (?, ?)"""
  return db.execute(query, deptName, chair)


# this function will get all the departments
def get_all_departments():
  query = """SELECT * FROM departments"""
  return db.execute(query)