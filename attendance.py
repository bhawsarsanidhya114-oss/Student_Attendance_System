import pandas as pd
import os
class attendance :
    def __init__(self):
        data = {
            "Student_id"   :  ["S001", "S002", "S003", "S004", "S005"],
            "Student_name" : ["rahul","harsh","riya","raj","kavita"],
             "Roll_no"     : [101, 102, 103, 104, 105],
           
        }
        self.df= pd.DataFrame(data)
        if os.path.exists(r"C:\Users\bhaws\OneDrive\Documents\attendance.csv") and os.path.getsize(r"C:\Users\bhaws\OneDrive\Documents\attendance.csv") > 0:
         self.attendance_df = pd.read_csv(r"C:\Users\bhaws\OneDrive\Documents\attendance.csv")
        else:
            self.attendance_df = pd.DataFrame(
                columns=["Student_id", "Date", "Attendance"]
            )

class add_attendance(attendance):
    def display (self):
            while True:
                 print("------ Student Attendance ------")
                 print("1. Add Attendance")
                 print (" 2. show all Student ")
                 print ("3. show all attendance details")     
                 print ("4. Exit") 
                 choice= int(input("enter your number"))
                 match choice:
                      case 1 :
                           student_id = input("Enter your student ID")
                           while student_id not in self.df["Student_id"].values:
                                print("student_id not found")
                                student_id = input("Enter your student ID")
                           Date = input("enter your Date ")     
                           Attendance= input(" Enter your Attendacne (Present,Absent,Leave)")
                           while Attendance not in ["Present","Absent","Leave"]:
                                print("invalid Attendance")
                           Attendance= input(" Enter your Attendacne (Present,Absent,Leave)")    
                           self.attendance_df.loc[len(self.attendance_df)] = [student_id,Date,Attendance]
                           self.attendance_df.to_csv(r"C:\Users\bhaws\OneDrive\Documents\attendance.csv, index=False")
                    
                           print("Attendance Added successfully")  
                           print(os.path.abspath("attendance.csv"))  
                      case 2 :
                              print(self.df)
                      case 3 :
                           attendance_details=pd.merge(
                                self.df,
                                self.attendance_df,
                                 on ="Student_id")
                           print(attendance_details)
                      case 4 :
                           print("thank you")
                           break     
                      case _:
                         print("invalid choice")  

c=add_attendance()  
c.display()
