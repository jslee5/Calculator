#
# Jason Lee
# 4/22/2023
# This Program builds a grade calculator GUI application
#
import tkinter as tk


class GradeCalculator:
    def __init__(self):
        # Creates the main window
        self.main_window = tk.Tk()
        self.main_window.title('Grade Calculator')
        self.main_window.geometry('260x125')

        # Makes the three frames to hold the input fields
        self.tests_frame = tk.Frame(self.main_window)
        self.labs_frame = tk.Frame(self.main_window)
        self.exams_frame = tk.Frame(self.main_window)

        # label and input fields for tests
        self.tests_label = tk.Label(self.tests_frame, text='Tests Grade:')
        self.tests_entry = tk.Entry(self.tests_frame, width=10)
        self.tests_label.pack(side='left')
        self.tests_entry.pack(side='left')

        # label and input fields for labs
        self.labs_label = tk.Label(self.labs_frame, text='Labs Grade:')
        self.labs_entry = tk.Entry(self.labs_frame, width=10)
        self.labs_label.pack(side='left')
        self.labs_entry.pack(side='left')

        # label and input fields for exams
        self.exams_label = tk.Label(self.exams_frame, text='Exams Grade:')
        self.exams_entry = tk.Entry(self.exams_frame, width=10)
        self.exams_label.pack(side='left')
        self.exams_entry.pack(side='left')

        # Creates the frame for the grade average
        self.average_frame = tk.Frame(self.main_window)
        self.average_label = tk.Label(
            self.average_frame, text='Grade Average:')
        self.average_result = tk.Label(self.average_frame, text='------')
        self.average_label.pack(side='left')
        self.average_result.pack(side='left')

        # button to calculate the average
        self.calculate_button = tk.Button(
            self.main_window, text='Calculate', command=self.calculate_average)

        # button to quit the program
        self.quit_button = tk.Button(
            self.main_window, text='Quit', command=self.main_window.destroy)

        # Pack the frames and buttons into the main window
        self.tests_frame.pack()
        self.labs_frame.pack()
        self.exams_frame.pack()
        self.average_frame.pack()
        self.calculate_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Starts the main loop
        tk.mainloop()

    def calculate_average(self):
        try:
            # Get the values from the input fields
            tests_grade = float(self.tests_entry.get())
            labs_grade = float(self.labs_entry.get())
            exams_grade = float(self.exams_entry.get())

            # Calculate the average
            average = (tests_grade * 0.2) + \
                (labs_grade * 0.3) + (exams_grade * 0.5)
            letter_grade = self.get_letter_grade(average)

            # Update the average label
            self.average_result.config(text=f'{average:.1f} ({letter_grade})')
        except ValueError:
            # Handle errors if input cannot be converted to float
            self.average_result.config(text='Error')

    def get_letter_grade(self, average):
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'


# GradeCalculator class instance
calculator = GradeCalculator()
