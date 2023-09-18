from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivy.properties import ObjectProperty
from kivy.lang import Builder

from kivy.core.window import Window

# for mobile:
Window.size = (360, 600)


class ClassSlot(MDBoxLayout):
    """Holds the class Type, Day, Start Time and End Time"""

    pass


class CourseGroup(MDCard):
    """Holds the course group name and the classes in the group"""

    course_label = ObjectProperty(None)
    slots = ObjectProperty(None)

    def __init__(self, text, **kwargs):
        super().__init__(**kwargs)
        self.course_label.text = f"[b]{text.upper()}[/b]"


class AddCourseGroup(MDBoxLayout):
    """Holds the input and submit button for a course group"""

    course_groups = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def validate_course(self, course_identifier, submit_button):
        course_identifier.text = course_identifier.text.lstrip()
        text = course_identifier.text.rstrip()
        if not text or len(text) > 70:
            submit_button.disabled = True
            course_identifier.text = ""
            return False
        submit_button.disabled = False
        return True


class CourseSchedulingApp(MDApp):
    courses = []

    def build(self):
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_hue = "200"
        self.load_all_kv_files()
        return Builder.load_file("libs/main.kv")

    def load_all_kv_files(self) -> None:
        super().load_all_kv_files("libs")

    def add_new_course(self, course_identifier):
        ## TODO: add course to database
        course = CourseGroup(course_identifier.text)
        self.courses.append(course)
        self.root.ids.course_grid.add_widget(course)
        course_identifier.text = ""


if __name__ == "__main__":
    CourseSchedulingApp().run()
