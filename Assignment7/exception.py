try :
   import test.h
except ImportError:
   print("Error: No module found.")
else :
   print("Import successful.")


try :
   x = 1 / 0
   print(x)
except ZeroDivisionError:
   print("Error: Division by zero.")
else :
   print("Successfully Divided.")


try:
   fd = open("testfile", "r")
   fd.write("Opened the file in write mode.")
except IOError:
   print("Error: File not Found.")
else:
   print("Written content in the file successfully.")


try :
   x = '2' + 6
   print(x)
except TypeError:
   print("Error: Type doesn't match.")
else :
   print("Addition successful.")


try :
   x = 5 * test
   print(x)
except NameError:
   print("Error: Variable not defined.")
else :
   print("Calculation successful.")
