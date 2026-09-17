import pyodbc
import pandas as pd
import os
class attendance :
    def __init__(self):
         self.conn = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=localhost;"
            "DATABASE=AttendanceDB;"
            "Trusted_Connection=yes;"
        )

         query = "SELECT * FROM Students"

         self.df = pd.read_sql(query, self.conn)

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
                           while student_id not in self.df["Student_ID"].values:
                                print("student_id not found")
                                student_id = input("Enter your student ID")
                           Date = input("enter your Date ")     
                           Attendance= input(" Enter your Attendacne (Present,Absent,Leave)")
                           while Attendance not in ["Present","Absent","Leave"]:
                                print("invalid Attendance")
                                Attendance= input(" Enter your Attendacne (Present,Absent,Leave)")    
                           cursor = self.conn.cursor()

                           cursor.execute(
                              """
                             INSERT INTO Attendance
                             (Student_ID, Attendance_Date, Status)
                              VALUES (?, ?, ?)
                                """,
                             student_id,
                             Date,
                             Attendance
                                        )

                           self.conn.commit()

                           cursor.close()

                           print("Attendance Added Successfully")
                           
                          
                      case 2 :
                              print(self.df)
                      case 3 :
                            attendance_query = "SELECT * FROM Attendance"

                            attendance_df = pd.read_sql(
                             attendance_query,
                             self.conn
                                      )

                            attendance_details = pd.merge(
                            self.df,
                            attendance_df,
                             on="Student_ID"
                                      )

                            print(attendance_details)
                      case 4 :
                           print("thank you")
                           break     
                      case _:
                         print("invalid choice")  

c=add_attendance()  
c.display()
