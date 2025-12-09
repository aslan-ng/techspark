from techspark.embedding import create_embedding


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