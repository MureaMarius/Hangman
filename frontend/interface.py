import random
import tkinter.messagebox
from tkinter import *
import re
from PIL import ImageTk, Image
from backend import parser as prs

buttons = [
    'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L',
    'Z', 'X', 'C', 'V', 'B', 'N', 'M']


class StartDisplay:
    def __init__(self, master):
        self.master = master
        self.master.title("HANGMAN")
        self.master.geometry('600x500')

        self.frame = Frame(self.master, width=600, height=500, relief=RAISED)
        self.frame.grid(row=0, column=0, sticky=NSEW)

        image_with_hangman = ImageTk.PhotoImage(
            Image.open('C:\\Users\\murea\\Desktop\\Python\\Proiecte Python\\Hangman '
                       'Project\\utility\\HangmanImage.jpg'))

        self.hangman_image = Label(self.frame, image=image_with_hangman, borderwidth=0, compound=CENTER)
        self.hangman_image.image = image_with_hangman
        self.hangman_image.place(relx=0.5, rely=0.5, anchor='center')

        self.play_button = Button(self.frame, text="JOACĂ", command=self.category_menu_selection,
                                  activeforeground="#FFFFFF", activebackground="Green")
        self.play_button.place(x=450, y=200)
        self.play_button.configure(width=15, height=2)

    def category_menu_selection(self):
        self.master.destroy()
        self.master = Tk()
        self.app = CategoryMenuDisplay(self.master)
        self.master.mainloop()


class CategoryMenuDisplay:
    def __init__(self, master):
        self.master = master
        self.master.title("HANGMAN")
        self.master.geometry('600x500')

        self.frame = Frame(self.master, background='white', width=600, height=500, relief=RAISED)
        self.frame.grid(row=0, column=0, sticky=NSEW)

        image_with_hangman = ImageTk.PhotoImage(
            Image.open('C:\\Users\\murea\\Desktop\\Python\\Proiecte Python\\Hangman '
                       'Project\\utility\\HangmanImage_OnlyWord.jpg'))
        self.hangman_image = Label(self.frame, image=image_with_hangman, borderwidth=0)
        self.hangman_image.image = image_with_hangman
        self.hangman_image.place(x=0, y=350)

        self.main_text = Label(self.frame, text='Selectează categoria', background='white')
        self.main_text.place(x=200, y=0)
        self.main_text.config(font=("Courier bold", 16))

        self.movies_category = Button(self.frame, text='Filme', activebackground="Green",
                                      command=lambda: self.play_window('Filme'))
        self.movies_category.config(font=("Courier bold", 16), width=7, height=1)
        self.movies_category.place(x=150, y=100)

        self.food_category = Button(self.frame, text='Mâncare', activebackground="Green",
                                      command=lambda: self.play_window('Mancare'))
        self.food_category.config(font=("Courier bold", 16), width=7, height=1)
        self.food_category.place(x=150, y=170)

        self.domain_category = Button(self.frame, text='Domenii', activebackground="Green",
                                      command=lambda: self.play_window('Domenii'))
        self.domain_category.config(font=("Courier bold", 16), width=7, height=1)
        self.domain_category.place(x=150, y=240)

        self.it_category = Button(self.frame, text='IT', activebackground="Green",
                                  command=lambda: self.play_window('IT'))
        self.it_category.config(font=("Courier bold", 16), width=7, height=1)
        self.it_category.place(x=350, y=100)

        self.cities_category = Button(self.frame, text='Orașe', activebackground="Green",
                                      command=lambda: self.play_window('Orase'))
        self.cities_category.config(font=("Courier bold", 16), width=7, height=1)
        self.cities_category.place(x=350, y=170)

        self.people_category = Button(self.frame, text='Oameni', activebackground="Green",
                                      command=lambda: self.play_window('Oameni'))
        self.people_category.config(font=("Courier bold", 16), width=7, height=1)
        self.people_category.place(x=350, y=240)

        self.back = Button(self.frame, text='Back', activebackground="Green", command=self.back_to_start_display)
        self.back.config(font=("Courier bold", 16), width=7, height=1)
        self.back.place(x=10, y=25)

    def play_window(self, selected_category: str):
        self.master.destroy()
        self.master = Tk()
        self.app = PlayWindowDisplay(self.master, selected_category)
        self.master.mainloop()

    def back_to_start_display(self):
        self.master.destroy()
        self.master = Tk()
        self.app = StartDisplay(self.master)
        self.master.mainloop()


class PlayWindowDisplay:
    def __init__(self, master, selected_category: str):
        self.is_category_selected = True
        self.list_of_words_with_hints = []
        self.list_of_words_without_hints = []
        self.selected_word = ''
        self.random_letter = ''
        self.list_of_letters = []
        self.number_of_guesses = 5
        self.number_of_guessed_letter = 0
        self.number_of_word_letters = 0

        if self.is_category_selected:
            self.is_category_selected = False
            self.list_of_words_without_hints = prs.list_extractor(selected_category, 0)
            self.list_of_words_with_hints = prs.list_extractor(selected_category, 1)

        self.category = selected_category
        self.master = master
        self.master.title("HANGMAN")
        self.master.geometry('1200x700')

        self.frame = Frame(self.master, background='white', width=1200, height=700, relief=RAISED)
        self.frame.grid(row=0, column=0, sticky=NSEW)

        image = ImageTk.PhotoImage(
            Image.open('C:\\Users\\murea\\Desktop\\Python\\Proiecte Python\\Hangman '
                       'Project\\utility\\Tool.png'))
        self.hang = Label(self.frame, image=image, borderwidth=0)
        self.hang.image = image
        self.hang.place(x=0, y=0)

        self.cuvant = Button(self.frame, text='Cuvânt', activebackground="Green", command=self.give_the_word)
        self.cuvant.config(font=("Courier bold", 16), width=7, height=1)
        self.cuvant.place(x=970, y=100)

        self.hint = Button(self.frame, text='Hint', activebackground="Green", command=self.give_the_hint)
        self.hint.config(font=("Courier bold", 16), width=7, height=1)
        self.hint.place(x=970, y=50)

        self.back = Button(self.frame, text='Back', activebackground="Green", command=self.back_to_category_selection_menu)
        self.back.config(font=("Courier bold", 16), width=7, height=1)
        self.back.place(x=10, y=25)

        self.create_the_keyboard()

        self.frame.pack()

    def create_the_keyboard(self):
        width = 900
        height = 200
        on_the_row = 0
        row = 0
        for letter in buttons:
            btn = Button(self.frame, text=letter, activebackground="Green",
                         command=lambda x=letter: self.put_the_letter(x))
            btn.config(font=("Courier bold", 16), width=2, height=1)
            btn.place(x=width, y=height)

            on_the_row += 1
            if on_the_row == 7 and row != 3:
                on_the_row = 0
                row += 1
                height += 45
                width = 900
            else:
                width += 35

            if row == 3:
                row = 0
                width = 935

    def give_the_word(self):
        for widget in self.frame.winfo_children():
            if str(widget).__contains__('line') or str(widget).__contains__('letter') or str(widget).__contains__('head') \
                    or 'tail' in str(widget) or str(widget).__contains__('right_arm') or str(widget).__contains__('left_arm') \
                    or str(widget).__contains__('right_foot') or str(widget).__contains__('left_foot') or str(widget).__contains__('hint'):
                widget.destroy()

        self.selected_word = random.choice(self.list_of_words_without_hints)
        self.random_letter = random.choice(self.selected_word)
        self.list_of_words_without_hints.remove(self.selected_word)
        self.number_of_word_letters = len(self.selected_word)
        self.number_of_guessed_letter = len(re.findall(self.random_letter, self.selected_word))
        self.number_of_guesses = 5

        position_x = 450
        position_y = 600

        line_number = 0
        letter_number = 0
        for character in self.selected_word:
            if character == self.random_letter:
                horizontal = Frame(self.frame, bg='black', height=5, width=50, name=f'line {line_number}')
                horizontal.place(x=position_x, y=position_y)

                letter = Label(self.frame, text=character, background='white',
                               name=f'letter {character + str(letter_number)}')
                letter.place(x=position_x + 25, y=position_y - 30, anchor='center')
                letter.config(font=("Courier bold", 30))
            else:
                horizontal = Frame(self.frame, bg='black', height=5, width=50, name=f'line {line_number}')
                horizontal.place(x=position_x, y=position_y)

            position_x += 70
            line_number += 1
            letter_number += 1

    def put_the_letter(self, letter):
        position_x = 475
        position_y = 570

        number = 0
        missed = False
        for character in self.selected_word:
            if letter == character and letter != self.random_letter:
                letter_label = Label(self.frame, text=character, background='white',
                                     name=f'letter {character + str(number)}')
                letter_label.place(x=position_x, y=position_y, anchor='center')
                letter_label.config(font=("Courier bold", 30))

                self.number_of_guessed_letter += 1
                number += 1
            elif letter not in self.selected_word and not missed:
                missed = True
                if self.number_of_guesses == 5:
                    image = ImageTk.PhotoImage(
                        Image.open('C:\\Users\\murea\\Desktop\\Python\\Proiecte Python\\Hangman '
                                   'Project\\utility\\Head.PNG'))
                    self.hang = Label(self.frame, image=image, borderwidth=0, background='black', name='head')
                    self.hang.image = image
                    self.hang.place(x=470, y=70)

                    self.number_of_guesses -= 1
                elif self.number_of_guesses == 4:
                    image = ImageTk.PhotoImage(
                        Image.open('C:\\Users\\murea\\Desktop\\Python\\Proiecte Python\\Hangman '
                                   'Project\\utility\\Tail.PNG'))
                    self.hang = Label(self.frame, image=image, borderwidth=0, background='black', name='tail')
                    self.hang.image = image
                    self.hang.place(x=505, y=152)

                    self.number_of_guesses -= 1
                elif self.number_of_guesses == 3:
                    image = ImageTk.PhotoImage(
                        Image.open('C:\\Users\\murea\\Desktop\\Python\\Proiecte Python\\Hangman '
                                   'Project\\utility\\LeftArm.PNG'))
                    self.hang = Label(self.frame, image=image, borderwidth=0, background='black', name='left_arm')
                    self.hang.image = image
                    self.hang.place(x=430, y=150)

                    self.number_of_guesses -= 1
                elif self.number_of_guesses == 2:
                    image = ImageTk.PhotoImage(
                        Image.open('C:\\Users\\murea\\Desktop\\Python\\Proiecte Python\\Hangman '
                                   'Project\\utility\\RightArm.PNG'))
                    self.hang = Label(self.frame, image=image, borderwidth=0, background='black', name='right_arm')
                    self.hang.image = image
                    self.hang.place(x=520, y=150)

                    self.number_of_guesses -= 1
                elif self.number_of_guesses == 1:
                    image = ImageTk.PhotoImage(
                        Image.open('C:\\Users\\murea\\Desktop\\Python\\Proiecte Python\\Hangman '
                                   'Project\\utility\\LeftFoot.PNG'))
                    self.hang = Label(self.frame, image=image, borderwidth=0, background='black', name='left_foot')
                    self.hang.image = image
                    self.hang.place(x=435, y=295)

                    self.number_of_guesses -= 1
                elif self.number_of_guesses == 0:
                    image = ImageTk.PhotoImage(
                        Image.open('C:\\Users\\murea\\Desktop\\Python\\Proiecte Python\\Hangman '
                                   'Project\\utility\\RightFoot.PNG'))
                    self.hang = Label(self.frame, image=image, borderwidth=0, background='black', name='right_foot')
                    self.hang.image = image
                    self.hang.place(x=510, y=295)

                    tkinter.messagebox.showerror('Game Over', '!!! AI PIERDUT !!!')

            position_x += 70

            if self.number_of_guessed_letter == self.number_of_word_letters:
                tkinter.messagebox.showinfo('Game Over', '!!! AI CÂȘTIGAT !!!')

    def give_the_hint(self):
        selected_hint = ''
        for list_with_hint in self.list_of_words_with_hints:
            if list_with_hint[0] == self.selected_word:
                selected_hint = list_with_hint[1]

        hint_label = Label(self.frame, text=selected_hint, background='white', name='hint')
        hint_label.place(x=10, y=650)
        hint_label.config(font=("Courier bold", 16))

    def back_to_category_selection_menu(self):
        self.master.destroy()
        self.master = Tk()
        self.app = CategoryMenuDisplay(self.master)
        self.master.mainloop()
