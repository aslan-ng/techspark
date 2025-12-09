from techspark.embedding import create_embedding
from techspark.instructor import Instructor
from techspark.class_object import Class
from techspark.match import match_items


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

    def search_classes_by_name(self, name: str, threshold=0.6, num_results=None):
        result = []
        classes = [class_instance.title for class_instance in self.classes]
        matches = match_items(name, classes, threshold=threshold, num_results=num_results)
        for match in matches:
            result.append(self.classes[match["index"]])
        return result


class CourseManager:

    def __init__(self):
        self.courses = []

    def add(self, course: Course):
        self.courses.append(course)

    def search_classes_by_name(self, name: str, threshold=0.6, num_results=None):
        result = []
        classes = [class_instance.title for class_instance in self.classes]
        matches = match_items(name, classes, threshold=threshold, num_results=num_results)
        for match in matches:
            result.append(self.classes[match["index"]])
        return result


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