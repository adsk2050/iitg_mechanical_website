import datetime
from mechweb.models import Program, ProgramSpecialization, StudentBatch, Students, current_year

current_year = datetime.datetime.now().year

programs = list(Program.objects.all().filter(has_alumni_details=True))
program_specializations = list(ProgramSpecialization.objects.all().filter(has_alumni_details=True))
programs += program_specializations
for program in programs:
    students = program.get_children().type(Students)
    if not len(students):
        continue
    print("updating alumni batch details for program: ", program.title)
    students = students[0]
    batches = students.get_children().type(StudentBatch)
    for batch in batches:
        try:
            batch = StudentBatch.objects.get(id=batch.id)
            if batch.enrollment_year + program.duration < current_year and not batch.alumni_batch:
                batch.alumni_batch = True
                print(batch.alumni_batch)
                batch.save()
        except:
            pass
