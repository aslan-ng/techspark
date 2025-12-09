weekdays_abreviations = {
    "Monday": "M",
    "Tuesday": "T",
    "Wednesday": "W",
    "Thursday": "R",
    "Friday": "F",
    "Saturday": "S",
    "Sunday": "U",
}


def create_embedding(text: str):
    return None

class Instructor:

    def __init__(
        self,
        name: str,
        role: str,
        description: str = "",
        embedding = None,
    ):
        self.name = name
        self.role = role
        self.description = description
        self.embedding = embedding

    def create_embedding(self):
        text = f"role: {self.role}"
        if self.description:
            text += f"\ndescription: {self.description}"
        self.embedding = create_embedding()


class InstructorManager:

    def __init__(self):
        self.instructors = []

    def add(self, instructor: Instructor):
        self.instructors.append(instructor)

    def find_by_name(self, name: str):
        return None  #####
    
    def find_by_role(self, role: str):
        return None #####
    
    def find_by_description(self, description: str):
        description_embedding = create_embedding(description)
        return None #####


class Course:

    def __init__(
        self,
        title: str, # Course title
        number: int,  # Course number
        units: int,  # Number of units
        description: str = ""  # Manage and provide information about courses."
    ):
        self.title = title
        self.number = number
        self.units = units
        self.description = description
        self.classes = []

    def add(
        self,
        instructor: Instructor,
        section,
        schedule,
        semester
    ):
        instance = Class(
            instructor=instructor,
            section=section,
            schedule=schedule,
            semester=semester
        )
        self.classes.append(instance)
        return instance
    
    def reset_classes(self):
        self.classes = []


class Class():

    def __init__(
            self,
            instructor: str,
            section,
            schedule,
            semester
        ):
        self.instructor = instructor
        self.section = section
        self.schedule = schedule
        self.semester = semester


if __name__ == "__main__":

    course_1 = Course(
        title="Wood Working 1",
        number=24201,
        units=3,
        description="Introduction to wood working.",
    )

    course_2 = Course(
        title="Manual Machining",
        number=24104,
        units=3,
        description="Introduction to manual machining.",
    )

    courses = [course_1, course_2]
    for course in courses:
        print("Course titles: ", course.title)

    course_1_class_1 = course_1.add(
        instructor="Justin",
        section="A1",
        schedule="TR 10:00-11:50AM",
        semester="Fall 2024",
    )
    course_1_class_2 = course_1.add(
        instructor="Justin",
        section="A2",
        schedule="TR 10:00-11:50AM",
        semester="Fall 2024",
    )

    course_2_class_1 = course_2.add(
        instructor="Ed",
        section="B2",
        schedule="W 10:00-11:50AM",
        semester="Fall 2024",
    )
    
    course_instaces = [
        course_1_class_1,
        course_1_class_2,
        course_2_class_1,
    ]