from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivy.properties import ObjectProperty
from kivymd.uix.button import MDIconButton
from kivy.lang import Builder
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.pickers import MDTimePicker

from kivy.core.window import Window

# for mobile:
Window.size = (360, 600)


class ClassSlot(MDBoxLayout):
    """Holds the class Type, Day, Start Time and End Time"""

    class_type = ObjectProperty(None)
    day = ObjectProperty(None)
    start_time = ObjectProperty(None)
    end_time = ObjectProperty(None)

    DAYS = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
    ]

    def __init__(self, group, **kwargs):
        self.group = group
        items = [
            {
                "text": day,
                "viewclass": "OneLineListItem",
                "on_release": lambda x=day: self.handle_day_press(x),
                "height": 40,
            }
            for day in self.DAYS
        ]
        self.menu = MDDropdownMenu(items=items, width_mult=2)
        self.time_picker = MDTimePicker()
        self.time_picker.bind(time=self.get_time)

        super().__init__(**kwargs)

    def show_time_picker(self, title):
        self.time_picker.title = title
        self.time_picker.open()

    def get_time(self, instance, time):
        if "Start" in self.time_picker.title:
            self.start_time.text = time.strftime("%H:%M")
        elif "End" in self.time_picker.title:
            self.end_time.text = time.strftime("%H:%M")

    def show_days_menu(self, btn):
        self.menu.caller = btn
        self.menu.open()

    def handle_day_press(self, day):
        self.menu.caller.text = day
        self.menu.dismiss()

    def delete_slot(self):
        pass


class CourseGroup(MDCard):
    """Holds the course group name and the classes in the group"""

    course_label = ObjectProperty(None)
    slots = ObjectProperty(None)

    def __init__(self, text, **kwargs):
        super().__init__(**kwargs)
        self.course_label.text = f"[b]{text.upper()}[/b]"

    def add_class_slot(self):
        self.slots.add_widget(ClassSlot(group=self))


class AddCourseGroup(MDBoxLayout):
    """Holds the input and submit button for a course group"""

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
        course.add_class_slot()
        course_identifier.text = ""


if __name__ == "__main__":
    CourseSchedulingApp().run()
