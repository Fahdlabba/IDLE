import tkinter.filedialog
from tkinter import *
from tkinter.filedialog import asksaveasfilename,askopenfilename
import  subprocess
import TKlighter as lg

#color variable
color="#214040"
bgcolor='#1B3434'
fgcolor='white'
purple ="#8732C2"
lightblue="lightblue"
#idle costumize
root=Tk()
root.title("Python Compiler ")
#p1 = PhotoImage(file = 'py.png')
#root.iconphoto(False,p1)
root.geometry("1080x700")
root.resizable(height=True,width=True)
#configuration
panel=PanedWindow(bd=1,relief="raised",orient=VERTICAL)
panel.pack(fill=BOTH,expand=1)
scroll=Scrollbar(root)
scroll.pack(side=RIGHT,fill=Y)
panel2=PanedWindow(bd=1,relief="raised")
panel.add(panel2)
compiler=Text(height=33,width=320,bg=bgcolor,fg=fgcolor,insertbackground="white",font=("Courier",10),yscrollcommand=scroll.set)
panel2.add(compiler)
scroll.config(command =compiler.yview )
#Console
console = Text(panel, height=50, width=180, bg=color, fg="white", yscrollcommand=scroll.set)
panel.add(console)
#path
path=""

#highlighting function
def light(event):
    lg.def_h(compiler,'red')
    lg.print_h(compiler,lightblue)
    lg.if_h(compiler, purple)
    lg.for_h(compiler,purple)
    lg.while_h(compiler, purple)
    lg.return_h(compiler, purple)
    lg.class_h(compiler,purple)
    lg.import_h(compiler,"#A52B0A")
    lg.function_h(compiler,lightblue)
    lg.double_qouts_h(compiler,"orange")
    lg.list_h(compiler,"orange")
    lg.input_h(compiler,lightblue)
    lg.int_h(compiler,lightblue)
    lg.float_h(compiler,lightblue)
    lg.from_h(compiler,purple)
    lg.break_h(compiler,"red")
    lg.try_h(compiler,purple)
    lg.str_h(compiler,"orange")
    lg.open_h(compiler,purple)
    lg.in_h(compiler,purple)
    lg.and_h(compiler,purple)
    lg.dict_h(compiler,lightblue)
    lg.elif_h(compiler,purple)
    lg.else_h(compiler,purple)
    lg.less_than_h(compiler,"orange")
    lg.greater_than_h(compiler,"orange")
    lg.pass_h(compiler,"red")
    lg.continue_h(compiler,"red")
    lg.single_qouts_h(compiler,"orange")
    lg.lambda_h(compiler,"red")
    lg.global_h(compiler,purple)
    lg.with_h(compiler,purple)
    lg.except_h(compiler,purple)
#function

def file_path(loct):
    global path
    path=loct
def open_f(event=" "):
    loct=askopenfilename(filetypes=[("Python Files ","*.py")])
    file=open(loct,'r')
    code=file.read()
    compiler.delete("1.0",END)
    compiler.insert("1.0",code)
    file_path(loct)

def save(event=" "):
   if path=='':
       loct=asksaveasfilename(filetypes=[("Python Files ","*.py")])
   else :
       loct=path
   file=open(loct,"w")
   code=compiler.get('1.0',END )
   file.write(code)
   file_path(loct)
def runer(event=" "):
    if path == '':
        console.insert("1.0",">> Save Your Code Please ")
        return
    command = f'python {path}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    console.delete('1.0',END)
    console.insert('1.0',output)
    console.insert('1.0',">> ")
    console.insert('1.0',"\n")
    console.insert('1.0',path)
    console.insert('1.0', error)

#Menu
menu_bar=Menu(root)
#File Menu
file=Menu(menu_bar,tearoff=0)
file.add_command(label="📂 Open      Crtl+O",command=open_f)
file.add_command(label="💾 Save as   Ctrl+S ",command=save)
file.add_separator()
file.add_command(label="❌ Exit",command=root.quit)
menu_bar.add_cascade(label="File",menu=file)

#run bar
run=Menu(menu_bar,tearoff=0)
run.add_command(label="▶ Run      F5",command=runer)
run.add_command(label="⏯ Debug")
menu_bar.add_cascade(label="Run",menu=run)
#view
view=Menu(menu_bar,tearoff=0)
view.add_command(label="Dark Mode")
view.add_command(label="Ligth Mode")
menu_bar.add_cascade(label="View",menu=view)
root.config(menu=menu_bar)
#shortcut
root.bind('<F5>',runer)
root.bind('<Control-s>',save)
root.bind('<Control-o>',open_f)
compiler.bind('<Key>',light)

#main
root.mainloop()
