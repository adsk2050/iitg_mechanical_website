from mechweb.models import CoursePage, CourseStructure,Course,Program,ProgramSpecialization,EffectiveTimePeriod,Semester,Academics,MechHomePage

masters_specializations = [
    'Aerodynamics & Propulsion',
    'Manufacturing Science and Engineering',
    'Computational Mechanics',
    'Fluids and Thermal',
    'Machine Design'
]


def add_semesters(etp,semesters):
    for sem_count in range(1,semesters+1):
        sem_obj = Semester(
            title= "Sem "+str(sem_count),
            semester_number =sem_count
        )
        etp.add_child(instance=sem_obj)
        sem_obj.save()

def init_program_and_sem():
    home = MechHomePage.objects.first()
    print("Creating academics page...",end="\t")

    acads = Academics(
        title = "Academics",
    )
    home.add_child(instance=acads)
    home.save()

    print("done")

    programs = [
        'B.Tech',
        'M.Tech',
        'Phd'
    ]

    for program in programs:
        if program!='M.Tech':
            title =""
            if program=='B.Tech':
                title="Undergraduate"
            else:
                title ="PG Courses & Electives"
            program_obj = Program(
                title = title
            )
            acads.add_child(instance=program_obj)
            program_obj.save()
            print( title+" created!")
            etp = EffectiveTimePeriod(
                title="latest"
            )
            program_obj.add_child(instance=etp)
            etp.save()
            print("Effective time period created for "+title)
            if program=="B.Tech":
                add_semesters(etp,8)

        else:
            program_obj= Program(
                title="Masters"
            )
            acads.add_child(instance=program_obj)
            program_obj.save()
            for specialization in masters_specializations:
                s_obj = ProgramSpecialization(
                    title= specialization
                )
                program_obj.add_child(instance=s_obj)
                s_obj.save()
                etp = EffectiveTimePeriod(
                    title="latest"
                )
                s_obj.add_child(instance=etp)
                etp.save()
                add_semesters(etp,4)




def copy_course():
    def get(parent,title):
        for child in parent.get_children():
            if child.title==title:
                return child
        return None
    def get_specif(mtech,title):
        for specif in mtech.get_children():
            if specif.title==title:
                return specif
        return None
    def get_course(course):
        new_course = Course(
            title = course.title,
            name = course.name,
            code = course.code,
            photo = course.photo,
            lectures = course.lectures,
            tutorials = course.tutorials,
            practicals = course.practicals,
            credits = course.credits,
            course_type = course.course_type,
            description = course.description,
            course_page_link = course.course_page_link,
            document = course.document,
        )
        print(course.title)
        return new_course


    home = MechHomePage.objects.first()
    acads = home.get_children().type(Academics)[0]

    courses = CoursePage.objects.all()

    for course in courses:

        if course.seven or (course.course_type!=0 and course.course_type!=3):
            prog = get(acads,"PG Courses & Electives")
            etp = prog.get_children()[0]
            new_course = get_course(course)
            etp.add_child(instance=new_course)
            new_course.save()

        if(course.zero and course.zero_sem):
            sem = course.zero_sem
            prog = get(acads,"Undergraduate")
            sem = get(prog.get_children()[0],"Sem "+str(sem))
            new_course = get_course(course)
            print("UG "+sem.title)
            sem.add_child(instance=new_course)
            new_course.save()

        prog = get(acads,"Masters")
        specialization =None
        sem = None
        if course.one and course.one_sem:
            specialization = get_specif(prog,masters_specializations[0])
            sem = course.one_sem
            etp = specialization.get_children()[0]
            new_course = get_course(course)
            sem = get(etp,"Sem "+str(sem))
            sem.add_child(instance=new_course)
            new_course.save()
        if course.two and course.two_sem:
            specialization = get_specif(prog,masters_specializations[1])
            sem = course.two_sem
            etp = specialization.get_children()[0]
            new_course = get_course(course)
            sem = get(etp,"Sem "+str(sem))
            sem.add_child(instance=new_course)
            new_course.save()
        if course.three and course.three_sem:
            specialization = get_specif(prog,masters_specializations[2])
            sem = course.three_sem
            etp = specialization.get_children()[0]
            new_course = get_course(course)
            sem = get(etp,"Sem "+str(sem))
            sem.add_child(instance=new_course)
            new_course.save()
        if course.four and course.four_sem:
            specialization = get_specif(prog,masters_specializations[3])
            sem = course.four_sem
            etp = specialization.get_children()[0]
            new_course = get_course(course)
            sem = get(etp,"Sem "+str(sem))
            sem.add_child(instance=new_course)
            new_course.save()
        if course.five and course.five_sem:
            specialization = get_specif(prog,masters_specializations[4])
            sem = course.five_sem
            etp = specialization.get_children()[0]
            new_course = get_course(course)
            sem = get(etp,"Sem "+str(sem))
            sem.add_child(instance=new_course)
            new_course.save()





# open the shell using python manage.py shell and use this script like this:

# from mechweb.automation_scripts.copy_courses import *
# init_program_and_sem()
# copy_course()
