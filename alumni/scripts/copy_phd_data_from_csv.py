import csv, re, datetime
from mechweb.models import Academics, Student, StudentBatch, StudentPage, Program, Students, CustomSupervisor

filename = "alumni/scripts/data/tbl_doctorates.csv"
fields = []
rows = []


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


with open(filename, "r") as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)


def split_name(name):
    first_name = middle_name = last_name = None
    name = name.split(" ")
    n = len(name)
    if n > 0:
        first_name = name[0]
    if n > 2:
        middle_name = name[1]
    if n > 1:
        last_name = name[-1]
    return first_name, middle_name, last_name


for row in rows:
    name = re.split("Dr. ", row[1])[1]
    thesis_title = row[2]

    supervisors = re.split(",| and | & ", row[3])
    batch = get_batch(int(row[4]), True)
    leaving_year = datetime.datetime(year=batch.graduation_year, month=5, day=1)
    first_name, middle_name, last_name = split_name(name)
    stud = Student.objects.child_of(batch).filter(title=name, thesis_title=thesis_title).first()
    exists = stud != None
    if not exists:
        stud = Student()
    if first_name:
        stud.first_name = first_name
    if middle_name:
        stud.middle_name = middle_name
    if last_name:
        stud.last_name = last_name
    stud.title = name
    stud.thesis_title = thesis_title
    stud.leaving_year = leaving_year

    if not exists:
        batch.add_child(instance=stud)
    stud.save()
    if not stud.supervisor and not stud.co_supervisor and not stud.custom_supervisor.all():
        if len(supervisors) > 0:
            supervisor = CustomSupervisor(page=stud, full_name=supervisors[0], supervisor_type="supervisor")
            supervisor.save()
        if len(supervisors) > 1:
            co_supervisor = CustomSupervisor(page=stud, full_name=supervisors[1], supervisor_type="co_supervisor")
            co_supervisor.save()

    print(name, batch, supervisors)


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


delete_empty_batches()
