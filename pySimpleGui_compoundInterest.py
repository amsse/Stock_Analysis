# importing the required widgets and methods from the tkinter library  
from tkinter import *  
  
# defining the reset function  
def reset():  
    # deleting the entries in all entry fields  
    principalField.delete(0, END)  
    rateField.delete(0, END)  
    numberField.delete(0, END)  
    timeField.delete(0, END)  
    resultField.delete(0, END)  
  
    # setting the focus to the principal field  
    principalField.focus_set()  
  
# defining the function to calculate the compound interest  
def compound_interest():  
    # getting the values from the entry fields  
    principal = float(principalField.get())  
    rate_of_interest = float(rateField.get())  
    number = float(numberField.get())  
    time = float(timeField.get())  
  
    # calculating the compound interest  
    amount = principal * pow((1 + (rate_of_interest / (100 * number))), number * time)  
    ci = amount - principal  
    # printing the resultant value in result field  
    resultField.insert(10, ci)  
  
# main function  
if __name__ == "__main__":  
    # creating an instance of the Tk() class  
    guiWindow = Tk()
    
    # defining the title for the GUI window  
    guiWindow.title("Compound Interest Calculator")
    
    # defining the geometry for the window  
    guiWindow.geometry("600x600+500+250")
    
    # disabling the resizable option  
    guiWindow.resizable(0, 0)
    
    # setting the background color for the window  
    guiWindow.configure(bg = "#017d22")  
  
    # heading on the window  
    guiLabel = Label(  
        guiWindow,  
        text = "by AMS - Jan, 2023",  
        font = ("Arial Bold", 10),  
        fg = "#211600",  
        bg = "#017d22"  
    )
    
    # placing the label on the window  
    guiLabel.place(  
        x = 60,  
        y = 10  
    )  
  
    # creating a 'Principal Amount' label  
    labelOne = Label(  
        guiWindow,  
        text = "Principal Amount:",
        font = ("Arial Bold", 16),
        fg = "#211600",  
        bg = "#017d22"  
    )
    
    # creating a 'Rate of Interest' label  
    labelTwo = Label(  
        guiWindow,  
        text = "Rate of Interest (%):",
        font = ("Arial Bold", 16),
        fg = "#211600",  
        bg = "#017d22"  
    )
    
    # creating a 'Number of Times' label  
    labelThree = Label(  
        guiWindow,  
        text = "Number of Times (n):",
        font = ("Arial Bold", 16),
        fg = "#211600",  
        bg = "#017d22"  
    )  
    # creating a 'Time Period' label  
    labelFour = Label(  
        guiWindow,  
        text = "Time Period (Years):",
        font = ("Arial Bold", 16),
        fg = "#211600",  
        bg = "#017d22"  
    )
    
    # creating a 'Compound Interest' label  
    labelFive = Label(  
        guiWindow,  
        text = "Compounded Interest:",
        font = ("Arial Bold", 16),
        fg = "#211600",  
        bg = "#017d22"  
        )  
  
    # using the place() method to place  
    # the above labels on the window  
    labelOne.place(x = 72, y = 120)  
    labelTwo.place(x = 72, y = 160)  
    labelThree.place(x = 72, y = 200)  
    labelFour.place(x = 72, y = 240)  
    labelFive.place(x = 72, y = 380)  
  
    # entry field for the principal amount  
    principalField = Entry(  
        guiWindow,
        font = ("Arial Bold", 16),
        bg = "#fcf9e8",  
        fg = "#211600"  
    )
    
    # entry field for the rate of interest  
    rateField = Entry(  
        guiWindow,
        font = ("Arial Bold", 16),
        bg = "#fcf9e8",  
        fg = "#211600"  
    )  
    # entry field for the number  
    numberField = Entry(  
        guiWindow,
        font = ("Arial Bold", 16),
        bg = "#fcf9e8",  
        fg = "#211600"  
    )
    
    # entry field for the time period  
    timeField = Entry(  
        guiWindow,
        font = ("Arial Bold", 16),
        bg = "#fcf9e8",  
        fg = "#211600"  
    )
    
    # entry field for the result  
    resultField = Entry(  
        guiWindow,
        font = ("Arial Bold", 16),
        bg = "#fcf9e8",  
        fg = "#211600"  
    )  
  
    # using the place() method to place  
    # the above fields on the window  
    principalField.place(x = 300, y = 120)  
    rateField.place(x = 300, y = 160)  
    numberField.place(x = 300, y = 200)  
    timeField.place(x = 300, y = 240)  
    resultField.place(x = 300, y = 380)  
  
    # creating a Result button  
    resultButton = Button(  
        guiWindow,  
        text = "CALCULATE",  
        bg = "#135e96",  
        fg = "#fcf9e8",  
        command = compound_interest  
    )
    
    # creating a Reset button  
    resetButton = Button(  
        guiWindow,  
        text = "RESET",  
        bg = "#d63638",  
        fg = "#fcf0f1",  
        command = reset  
    )
    
    # using the place() method to place  
    # the above buttons on the window  
    resultButton.place(x = 300, y = 280)  
    resetButton.place(x = 300, y = 500)      
  
    # running the window  
    guiWindow.mainloop() 