from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder

from kivy.core.window import Window

# for mobile:
Window.size = (360, 600)


class AddCourseGroup(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def add_new_course(self, course_identifier):
        ## TODO: add course to database
        print(course_identifier.text)
        course_identifier.text = ""

    def validate_course(self, course_identifier, submit_button):
        course_identifier.text = course_identifier.text.strip()
        if not course_identifier.text or len(course_identifier.text) > 70:
            submit_button.disabled = True
            course_identifier.text = ""
            return False
        submit_button.disabled = False
        return True


class CourseSchedulingApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_hue = "200"
        self.load_all_kv_files()
        return Builder.load_file("libs/main.kv")

    def load_all_kv_files(self) -> None:
        super().load_all_kv_files("libs")


if __name__ == "__main__":
    CourseSchedulingApp().run()
