from mechweb.models import Academics, Student, StudentBatch, StudentPage, Program, Students
from datetime import date

todays_date = date.today()
current_year = todays_date.year

acads = Academics.objects.first()
prog = Program.objects.all().filter(title="Ph.D").first()
if not prog:
    prog = Program(title="Ph.D")
    acads.add_child(instance=prog)
    prog.save()
    print("Created new program: Ph.D")

researchScholars = Students.objects.child_of(prog).first()
if not researchScholars:
    researchScholars = Students(title="Research Scholors")
    prog.add_child(instance=researchScholars)
    researchScholars.save()
    print("Created students page: Research Scholors")


def get_batch(year, graduated=False):
    global researchScholars, StudentBatch
    batch = None
    if not graduated:
        batch = StudentBatch.objects.child_of(researchScholars).filter(enrollment_year=year).first()
    else:
        batch = StudentBatch.objects.child_of(researchScholars).filter(graduation_year=year).first()

    if not batch:
        if not graduated:
            batch = StudentBatch(title="{year} Batch".format(year=year), enrollment_year=year)
        else:
            batch = StudentBatch(title="{year} Graduated".format(year=year), graduation_year=year, alumni_batch=True)
        researchScholars.add_child(instance=batch)
        batch.save()
        print("Created batch :", batch)
    return batch


def copy_student(old_stud):
    global get_batch, Student, researchScholars
    date = old_stud.enrolment_year
    batch = get_batch(date.year)
    stud = Student.objects.descendant_of(researchScholars).filter(webmail=old_stud.email_id).first()

    def get_title(stud):
        name = stud.first_name
        if len(stud.middle_name):
            name += " " + stud.middle_name
        if len(stud.last_name):
            name += " " + stud.last_name
        return name

    exists = stud != None
    if not exists:
        stud = Student()
    stud.title = get_title(old_stud)
    stud.first_name = old_stud.first_name
    stud.middle_name = old_stud.middle_name
    stud.last_name = old_stud.last_name
    stud.webmail = old_stud.email_id
    stud.roll_no = old_stud.roll_no
    stud.enrollment_year = old_stud.enrolment_year
    stud.leaving_year = old_stud.leaving_year
    stud.is_exchange = old_stud.is_exchange
    stud.contact_number = old_stud.contact_number
    stud.hostel_address = old_stud.hostel_address
    stud.photo = old_stud.photo
    stud.intro = old_stud.intro
    stud.body = old_stud.body
    stud.website = old_stud.website
    stud.supervisor = old_stud.faculty_advisor

    if not exists:
        batch.add_child(instance=stud)
    stud.save()
    if exists:
        print("Updated student: ", stud)
    else:
        print("Copied student: ", stud)


students = StudentPage.objects.all()

for student in students:
    if student.get_programme_display() == "Research Scholar":
        copy_student(student.specific)


def moveToGraduatedBatch(stud):
    global get_batch
    year = stud.leaving_year
    batch = get_batch(year.year, True)
    batch.move
    if batch.id != stud.get_parent().id:
        print("Moving student {stud} to batch: {batch}".format(stud=stud.title, batch=batch.title))
        stud.move(batch, "last-child")


def create_graduated_batch():
    global moveToGraduatedBatch, researchScholars
    global current_year
    copied_students = Student.objects.descendant_of(researchScholars).all()
    for student in copied_students:
        if student.enrollment_year.year < current_year - 2 and student.leaving_year and student.leaving_year.year <= current_year:
            moveToGraduatedBatch(student)


def delete_empty_batches():
    global researchScholars, StudentBatch
    batches = StudentBatch.objects.child_of(researchScholars).all().order_by("title")
    for batch in batches:
        print(batch, batch.get_children().count())
        if not batch.graduation_year and batch.alumni_batch:
            print("Marking as an alumni batch:", batch)
            batch.alumni_batch = False
            batch.save()
        if batch.get_children().count() == 0:
            print("Deleting empty batch: ", batch)
            batch.delete()


create_graduated_batch()
delete_empty_batches()

exit()
