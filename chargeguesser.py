import tkinter as tk
from regression import predict

HEIGHT = 700
WIDTH = 800

blue = "#D0E8FF"

def charge_calculator(age, sex, bmi, children, smoker, region):
	charges = predict(age, sex, bmi, children, smoker, region)
	charges_rounded = round(float(charges[0]), 2)

	charges_label['text'] = 'Your estimated charges are ' + str(charges_rounded)

root = tk.Tk()
root.title("Charge estimator")

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

frame = tk.Frame(root, bg = blue)
frame.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.8)

lower_frame = tk.Frame(frame, bg = blue)
lower_frame.place(relx = 0, rely = 0.7, relwidth = 1, relheight = 0.3)

label = tk.Label(frame, text = "Input the following data and we will estimate your charges!")
label.pack()

age_label = tk.Label(frame, text = "Age", bg = blue)
age_label.pack()
age_entry = tk.Entry(frame, bg = "#F2F2F2")
age_entry.pack()

sex_label = tk.Label(frame, text = "Sex (male/female)", bg = blue)
sex_label.pack()
sex_entry = tk.Entry(frame, bg = "#F2F2F2")
sex_entry.pack()

bmi_label = tk.Label(frame, text = "BMI", bg = blue)
bmi_label.pack()
bmi_entry = tk.Entry(frame, bg = "#F2F2F2")
bmi_entry.pack()

children_label = tk.Label(frame, text = "How many kids do you have?", bg = blue)
children_label.pack()
children_entry = tk.Entry(frame, bg = "#F2F2F2")
children_entry.pack()

smoker_label = tk.Label(frame, text = "Do you smoke? (yes/no)", bg = blue)
smoker_label.pack()
smoker_entry = tk.Entry(frame, bg = "#F2F2F2")
smoker_entry.pack()

region_label = tk.Label(frame, text = "Which region are you from? (northwest/northeast/southwest/southeast)", bg = blue)
region_label.pack()
region_entry = tk.Entry(frame, bg = "#F2F2F2")
region_entry.pack()



button = tk.Button(lower_frame, text = "Calculate!!", bg = "gray", fg = "black", \
	command = lambda: charge_calculator(age_entry.get(), sex_entry.get(), bmi_entry.get(), children_entry.get(), smoker_entry.get(), region_entry.get()))
button.place(relx = .35, rely = .1, relwidth = 0.3, relheight = .3)

charges_label = tk.Label(lower_frame, bg = blue)
charges_label.place(relx = 0.35, rely = 0.5)



root.mainloop()