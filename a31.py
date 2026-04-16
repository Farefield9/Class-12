import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
blood_group=["A+", "A+", "AB-", "O+", "B+", "O-", "A+", "AB+", "O+", "A+"]
pl.title("STUDENTS' BLOOD GROUP")
pl.xlabel("Blood Groups")
pl.ylabel("Number of Students")
pl.hist(blood_group, bins=6)
pl.show()
pl.savefig("studentsbloodgroup.jpg")
