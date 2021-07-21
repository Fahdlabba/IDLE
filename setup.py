from cx_Freeze import setup, Executable
setup(name = "Python IDLE" ,
      version = "0.1" ,
      description = "" ,
      executables = [Executable("main.py")])