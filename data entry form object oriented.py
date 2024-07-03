from tkinter import Tk, Button, Label, LabelFrame, Entry,StringVar,Spinbox,messagebox, Checkbutton
from tkinter import ttk

class main:
    def __init__(self,root):
        self.root = root
        self.user_information()
        self.course_information()
        self.terms_and_conditions()
        self.entry_button()


    # user information
    def user_information(self):
        user_info_frame =LabelFrame(root,  text="User Information")
        user_info_frame.grid(row=0, column=0,padx=10, pady=10)

        firstname_label = Label(user_info_frame,text="First Name")
        firstname_label.grid(row=0,column=0)
        self.firstname_entry = Entry(user_info_frame)
        self.firstname_entry.grid(row=1,column=0)

        lastname_label = Label(user_info_frame,text="Last Name")
        lastname_label.grid(row=0,column=1)
        self.lastname_entry = Entry(user_info_frame)
        self.lastname_entry.grid(row=1,column=1)

        title_label = Label(user_info_frame, text="Title")
        title_label.grid(row= 0,column=2)
        self.title_combobox = ttk.Combobox(user_info_frame, values=["", "Mr." , "Ms." , "Dr.", "Eng."])
        self.title_combobox.grid(row=1,column=2)

        age_label = Label(user_info_frame, text="Age")
        age_label.grid(row=2,column=0)
        self.age_spinbox = Spinbox(user_info_frame, from_=18, to=100)
        # spinbox e unlimited porjonto number show korar jonno to= 'infinity' likhte hoi 
        self.age_spinbox.grid(row=3,column=0)

        nationality_label = Label(user_info_frame, text="Nationality")
        nationality_label.grid(row=2, column=1)
        self.nationality_combobox = ttk.Combobox(user_info_frame,values=["", "Bangladesh", "India", "Pakistan","Soudi Arab", "America", "Europ"])
        self.nationality_combobox.grid(row=3, column=1)

        # to apply padding for all childrens of the user_info_frame
        for widget in user_info_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)

    # cource info frame
    def course_information(self):
        course_frame =LabelFrame(root)
        course_frame.grid(row=1,column=0, sticky='we',padx=10)

        registration_label =Label(course_frame, text="Registration Status")
        registration_label.grid(row=0,column=0)

        self.reg_checkbox_var =StringVar()
        self.registration_checkbox = Checkbutton(course_frame, text="Currently registered", variable=self.reg_checkbox_var, onvalue="Registered", offvalue="Not Registered")
        # kono akta checkbox er value k database e save korar jonno alada akta variable use korte hoi
        # karon .get method diye check box er kono value pawa jai na
        # tai akta string variable create kore sekhane checkbox er  output k string hisebe rakha jai
        # upor er syntex onujayi code ta likhte ho
        # aikhane  check box ti on thakle online="registered" kaj korbe and variable ti te registered store hobe
        # r check box ti off thakle offline="not registered" kaj korbe and varibale e not registered store hobe
        # aita new sikhlam...


        self.registration_checkbox.grid(row=1,column=0)

        number_cource_label =Label(course_frame, text="Completed Cources")
        number_cource_label.grid(row=0, column=1)
        self.number_cource_spinbox = Spinbox(course_frame, from_=0, to=5)
        self.number_cource_spinbox.grid(row=1,column=1)

        number_semester_label = Label(course_frame, text="Semesters")
        number_semester_label.grid(row=0, column=2)
        self.number_semester_spinbox = Spinbox(course_frame, from_=1, to= 8)
        self.number_semester_spinbox.grid(row=1,column=2)

        # to apply padding for all childrens of the course_frame
        for widget in course_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)


    def terms_and_conditions(self):
        # Terms frame
        terms_frame = LabelFrame(root, text="Terms and conditions")
        terms_frame.grid(row=2, column=0, sticky='ew', padx=10)

        self.terms_check_var = StringVar()
        self.terms_check = Checkbutton(terms_frame, text="I agree the terms and conditions.", variable=self.terms_check_var, 
                                            onvalue="checked", offvalue="not checked")
        self.terms_check.grid(row=0, column=0)


    def enter_data(self):
        first_name = self.firstname_entry.get()
        last_name = self.lastname_entry.get()
        title = self.title_combobox.get()
        age = self.age_spinbox.get()
        nationality = self.nationality_combobox.get()
        completed_course = self.number_cource_spinbox.get()
        semesters =self.number_semester_spinbox.get()
        registured_or_not_registered = self.reg_checkbox_var.get()
        checked_or_uncheked = self.terms_check_var.get()
        def data():
            print("First name: ", first_name, "Last name: ", last_name)
            print("Title: ", title, "Age: ", age, "Nationality: ", nationality)
            print("# courses: ", completed_course, "Semesters: ", semesters)
            print("----------------------------------------------")
        if first_name and last_name:
            if age:
                if nationality:
                    if semesters:
                        if registured_or_not_registered == "Registered":
                            if checked_or_uncheked == "checked":
                                data()
                            else:
                                messagebox.showwarning(title = "Error", message = " You can't accept our terms and conditions.")
                        else:
                            messagebox.showwarning(title = "Error", message = " You are not registered.")
                    else:
                        messagebox.showwarning(title = "Error", message = " Semesters also required.")
                else:
                    messagebox.showwarning(title = "Error", message = " Nationality must be required.")
            else:
                messagebox.showwarning(title = "Error", message = " Age must be required.")

        else:
            messagebox.showwarning(title = "Error", message = " First name and last name must be required.")
 
    def entry_button(self):
        # buttons
        button = Button(root, text="Enter data", command=self.enter_data)
        button.grid(row=3, column=0, sticky="ew", padx=20, pady=10)
    
    

if __name__ == "__main__":
    root = Tk()
    application = main(root)
    root.resizable(width=False, height=False)
    root.mainloop()