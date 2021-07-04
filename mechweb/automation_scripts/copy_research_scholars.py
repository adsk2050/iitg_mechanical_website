from mechweb.models import Academics, Student, StudentBatch, StudentPage, Program, Students

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


def get_batch(year):
    global researchScholars, StudentBatch
    batch = StudentBatch.objects.child_of(researchScholars).filter(enrollment_year=year).first()
    if not batch:
        batch = StudentBatch(title="{year} Batch".format(year=year), enrollment_year=year)
        researchScholars.add_child(instance=batch)
        batch.save()
        print("Created batch :", batch)
    return batch


def copy_student(stud):
    global get_batch, Student
    date = stud.enrolment_year
    # print(year.year)
    batch = get_batch(date.year)
    if Student.objects.child_of(batch).filter(webmail=stud.email_id).exists():
        print("{student} skipped".format(student=stud))
        return

    def get_title(stud):
        name = stud.first_name
        if len(stud.middle_name):
            name += " " + stud.middle_name
        if len(stud.last_name):
            name += " " + stud.last_name
        return name

    new_stud = Student(
        title=get_title(stud),
        first_name=stud.first_name,
        middle_name=stud.middle_name,
        last_name=stud.last_name,
        webmail=stud.email_id,
        roll_no=stud.roll_no,
        enrollment_year=stud.enrolment_year,
        leaving_year=stud.leaving_year,
        is_exchange=stud.is_exchange,
        contact_number=stud.contact_number,
        hostel_address=stud.hostel_address,
        photo=stud.photo,
        intro=stud.intro,
        body=stud.body,
        website=stud.website,
        supervisor=stud.faculty_advisor,
    )
    batch.add_child(instance=new_stud)
    new_stud.save()
    print(new_stud.title + " added")


students = StudentPage.objects.all()
cnt = 0
for student in students:
    if student.get_programme_display() == "Research Scholar":
        copy_student(student.specific)
exit()