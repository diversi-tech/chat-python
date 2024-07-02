# Define the Course class
class Course:
    def __init__(self, courseId, courseName, courseDescription, createdAt, updatedAt):
        self.courseId = courseId
        self.courseName = courseName
        self.courseDescription = courseDescription
        self.createdAt = createdAt
        self.updatedAt = updatedAt