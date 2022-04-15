from flask import Flask, request, render_template, redirect
import queries as q


app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/add", methods=["GET","POST"])
def add():
  if request.method == "GET":
    #show the user the page with the form
    dept_list = q.get_all_departments();
    return render_template("add.html", dept_list=dept_list)
  else:
    # get all the info from the submitted form
    name = request.form.get("courseName")
    teacher = request.form.get("teacher")
    room = request.form.get("room")
    dept = request.form.get("department")
    # now use the above info to add a new course to the database
    course_id = q.add_new_course(name, teacher, room, dept)
    return render_template("success.html", message="Course Added Successfully!")

@app.route("/show")
def show():
  # get all the courses from the database
  course_list = q.get_all_courses()
  return render_template("show.html", courses=course_list)

@app.route("/edit/<int:id>")
def edit(id):
  if request.method == "GET":
    # grab all the info for one particual course based on the id
    course_info = q.get_course_info(id)
    return render_template("edit.html", info=course_info)
  else: #post method --> form submited
    #get all the form info
    name = request.form.get("courseName")
    teacher = request.form.get("teacher")
    room = request.form.get("room")
    dept = request.form.get("department")
    result = q.update_course(id, name, teacher, room, dept)
    if result == 1:
      return redirect("/show")
    else:
      return "<h2>ERROR COURSE WAS NOT UPDATED</h2>"

@app.route("/add_dept", methods=["GET", "POST"])
def add_dept():
  if request.method == "GET":
    #show the form for the user
    return render_template("addDept.html")
  else: # post method
    # get the info from the form
    deptName = request.form.get("deptName")
    chair = request.form.get("chair")
    # use the info to insert a department
    dept_id = q.add_new_department(deptName, chair)
    return str(dept_id)



if __name__ == "__main__":
  app.run("0.0.0.0", debug=True)