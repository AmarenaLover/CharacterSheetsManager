import random
import yaml
import os, sys
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import Character


# from Character import Rekord


def display_sheet(character):
    # colors = ["red", "green", "blue", "orange", "purple", "yellow", "pink", "brown", "cyan"]
    colors = ["grey"] * 9

    path = r'characterSheets'
    path = "{}{}".format("characterSheets\\", character)
    slash = ' / '
    max_str = '(max)'

    # os.path.join("characterSheets\\", character)

    def parse_yaml_to_class(yaml_file_path, class_type):
        with open(yaml_file_path, 'r') as file:
            data = yaml.safe_load(file)
            return class_type(**data)

    postac = parse_yaml_to_class(path, Character.Record)

    print(postac)

    clear_main_window()
    # window.state('zoomed')
    x = 480
    y = 190

    titleFrame = tk.Frame().pack()
    tk.Label(titleFrame, text=postac.IdentityV[0]).pack()
    body = tk.Frame(window)
    body.pack(fill=tk.BOTH, expand=True)

    def on_configure(event):
        content.update_idletasks()
        content_scrollbar.configure(scrollregion=content.bbox("all"))
        content_scrollbar.create_window((0, 0), window=content, width=window.winfo_width(), anchor=tk.NW)

    content_scrollbar = tk.Canvas(body)
    content_scrollbar.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar = tk.Scrollbar(body, command=content_scrollbar.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    content_scrollbar.configure(yscrollcommand=scrollbar.set)
    content = tk.Frame(content_scrollbar)
    content.columnconfigure(0, weight=1)
    content.columnconfigure(1, weight=0)
    content.columnconfigure(2, weight=1)

    content_scrollbar.bind("<Configure>", on_configure)

    uP = 2
    uFP = 20

    buttonsFrame = tk.Frame(window, background=colors[8])
    buttonsFrame.pack(side=BOTTOM)
    tk.Button(buttonsFrame, text="Wyjście", command=on_button_displayCS_click, width=15).grid(row=0, column=0, padx=10,
                                                                                              pady=10)
    tk.Button(buttonsFrame, text="Rzut kośćmi", command=roll_dice, width=15).grid(row=0, column=1, padx=10, pady=10)
    tk.Button(buttonsFrame, text="Edycja", width=15).grid(row=0, column=2, padx=10, pady=10)
    tk.Button(buttonsFrame, text="Usuń", command=lambda name_d=path: delete_character(name=name_d), width=15).grid(
        row=0, column=3, padx=10, pady=10)

    identityFrame = tk.Frame(content)
    identityFrame.grid(row=0, column=1, pady=uFP)
    characteristicsFrame = tk.Frame(content)
    characteristicsFrame.grid(row=1, column=1, pady=uFP)
    hitpointsFrame = tk.Frame(content)
    hitpointsFrame.grid(row=2, column=1, pady=uFP)
    skillsFrame = tk.Frame(content)
    skillsFrame.grid(row=3, column=1, pady=uFP)
    weaponFrame = tk.Frame(content)
    weaponFrame.grid(row=4, column=1, pady=uFP)
    armorFrame = tk.Frame(content)
    armorFrame.grid(row=5, column=1, pady=uFP)

    # equipmentFrame       = tk.Frame(content, background=colors[6]).grid(row=6, column=1, pady=10)

    def get_roll_V(first_V):
        roll_V = "{}{}{}{}{}".format(str(first_V), slash, str(int((first_V + 2) / 5)), slash,
                                     str(int((first_V + 10) / 20)))
        return roll_V

    header1 = tk.Label(content, text="DANE BADACZA")
    header1.grid(row=0, column=0, padx=10, pady=10, sticky="NE")
    header2 = tk.Label(content, text="CECHY")
    header2.grid(row=1, column=0, padx=10, pady=10, sticky="NE")
    header3 = tk.Label(content, text="PUNKTY TRAFIEŃ")
    header3.grid(row=2, column=0, padx=10, pady=10, sticky="NE")
    header4 = tk.Label(content, text="UMIEJĘTNOŚCI")
    header4.grid(row=3, column=0, padx=10, pady=10, sticky="NE")
    header5 = tk.Label(content, text="BROŃ")
    header5.grid(row=4, column=0, padx=10, pady=10, sticky="NE")
    header6 = tk.Label(content, text="PANCERZ")
    header6.grid(row=5, column=0, padx=10, pady=10, sticky="NE")
    header7 = tk.Label(content, text="EKWIPUNEK")
    header7.grid(row=6, column=0, padx=10, pady=10, sticky="NE")

    for x in range(9):
        tk.Label(identityFrame, text=postac.IdentityL[x]).grid(row=x, column=0, padx=uP, pady=uP, sticky="e")
        tk.Label(identityFrame, text=postac.IdentityV[x]).grid(row=x, column=1, padx=uP, pady=uP, sticky="w")
    for x in range(8):
        tk.Label(characteristicsFrame, text=postac.CharacteristicsL[x]).grid(row=x, column=0, padx=uP, pady=uP,
                                                                             sticky="e")
        roll_CH_V = get_roll_V(postac.CharacteristicsV[x] * 5)
        tk.Label(characteristicsFrame, text=roll_CH_V).grid(row=x, column=1, padx=uP, pady=uP, sticky="e")
    for x in range(4):
        tk.Label(hitpointsFrame, text=postac.HitpointsL[x]).grid(row=x, column=0, padx=uP, pady=uP, sticky="e")
        displayed_hp = "{}{}{}{}".format(postac.HitpointsV[x], slash, postac.HitpointsV[x + 4], max_str)
        tk.Label(hitpointsFrame, text=displayed_hp).grid(row=x, column=1, padx=uP, pady=uP, sticky="w")
    tk.Label(skillsFrame, width=20).grid(row=0, column=2)
    for x in range(28):
        tk.Label(skillsFrame, text=postac.SkillsL[(x * 2)]).grid(row=x, column=0, padx=uP, pady=uP, sticky="e")
        roll_S_V = get_roll_V(postac.SkillsV[(x * 2)])
        tk.Label(skillsFrame, text=roll_S_V).grid(row=x, column=1, padx=uP, pady=uP, sticky="e")
        if x == 27:
            continue
        else:
            tk.Label(skillsFrame, text=postac.SkillsL[(x * 2) + 1]).grid(row=x, column=3, padx=uP, pady=uP, sticky="e")
            roll_S_V = get_roll_V(postac.SkillsV[(x * 2) + 1])
            tk.Label(skillsFrame, text=roll_S_V).grid(row=x, column=4, padx=uP, pady=uP, sticky="e")
    if (postac.WeaponsNb) == 0:
        tk.Label(weaponFrame, text="Brak broni").grid(row=0, column=y, padx=uP, pady=uP)
    else:
        for y in range(9):
            tk.Label(weaponFrame, text=postac.WeaponL[y]).grid(row=0, column=y, padx=uP, pady=uP)
        for x in range(postac.WeaponsNb):
            for y in range(8):
                tk.Label(weaponFrame, text=postac.WeaponsL[x]).grid(row=x + 1, column=0, padx=uP, pady=uP)
                tk.Label(weaponFrame, text=postac.WeaponsV[x][y]).grid(row=x + 1, column=y + 1, padx=uP, pady=uP)
    for x in range(3):
        tk.Label(armorFrame, text=postac.ArmorL[x]).grid(row=0, column=x, padx=uP, pady=uP)
        tk.Label(armorFrame, text=postac.ArmorV[x]).grid(row=1, column=x, padx=uP, pady=uP)


# titleFrame.grid(row=0, column=0, columnspan=4, rowspan=1)
# identityFrame.grid(row=1, column=0, columnspan=1, rowspan=2)
# characteristicsFrame.grid(row=1, column=1, columnspan=1, rowspan=2)
# hitpointsFrame.grid(row=1, column=2, columnspan=1, rowspan=1)
# armorFrame.grid(row=2, column=2, columnspan=1, rowspan=1)
# skillsFrame.grid(row=1, column=3, columnspan=1, rowspan=4)
# weaponFrame.grid(row=3, column=0, columnspan=3, rowspan=1)
# equipmentFrame.grid(row=4, column=0, columnspan=3, rowspan=1)
# buttonsFrame.grid(row=5, column=0, columnspan=4, rowspan=1)

def delete_character(name):
    if messagebox.askyesno("Uwaga", "Czy chcesz usunąć aktualną postać?") == True:
        if messagebox.askyesno("Uwaga", "Czy NA PEWNO chcesz usunąć aktualną postać?") == True:
            if os.path.isfile(name):
                os.remove(name)
                messagebox.showinfo("Potwierdzenie", "Postać usunięto pomyślnie!")
                on_button_displayCS_click()


def roll_dice():
    roll_window = tk.Tk()
    roll_window.minsize(600, 200)
    roll_window.maxsize(600, 200)
    window.title("Rzut kośćmi")


    header = tk.Frame(roll_window)
    header.pack(side=tk.TOP)
    body = tk.Frame(roll_window)
    body.pack(side=tk.TOP)
    footer = tk.Frame(roll_window)
    footer.pack(side=tk.BOTTOM)

    def get_randomizer(upper):
        res = "Wynik rzutu: " + str(random.randint(1, upper))
        tk.Label(body, text=res).grid(row=2, column=0, padx=10, pady=10, columnspan=4)

    tk.Button(body, text="1k2", command=lambda up=2: get_randomizer(up), width=15).grid(row=0, column=0, padx=10,
                                                                                        pady=10)
    tk.Button(body, text="1k4", command=lambda up=4: get_randomizer(up), width=15).grid(row=0, column=1, padx=10,
                                                                                        pady=10)
    tk.Button(body, text="1k6", command=lambda up=6: get_randomizer(up), width=15).grid(row=0, column=2, padx=10,
                                                                                        pady=10)
    tk.Button(body, text="1k8", command=lambda up=8: get_randomizer(up), width=15).grid(row=0, column=3, padx=10,
                                                                                        pady=10)
    tk.Button(body, text="1k10", command=lambda up=10: get_randomizer(up), width=15).grid(row=1, column=0, padx=10,
                                                                                          pady=10)
    tk.Button(body, text="1k12", command=lambda up=12: get_randomizer(up), width=15).grid(row=1, column=1, padx=10,
                                                                                          pady=10)
    tk.Button(body, text="1k20", command=lambda up=20: get_randomizer(up), width=15).grid(row=1, column=2, padx=10,
                                                                                          pady=10)
    tk.Button(body, text="1k100", command=lambda up=100: get_randomizer(up), width=15).grid(row=1, column=3, padx=10,
                                                                                            pady=10)

    tk.Label(header, text="RZUT KOŚCIĄ").grid(row=0, column=0)
    tk.Button(footer, text="Zamknij okno", command=roll_window.destroy, width=15).grid(row=0, column=0, padx=10,
                                                                                       pady=10)
    roll_window.mainloop()


def path_for_apte(rel_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, rel_path)


def on_button_displayCS_click():
    path = r'characterSheets\.'
    files = []
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            files.append(f)
    numb = len(files)
    if numb == 0:
        messagebox.showinfo("Uwaga", "Nie ma żadnych dostępnych kart postaci!")
    else:
        if numb > 10:
            messagebox.showinfo("Uwaga",
                                "W bazie jest za dużo postaci, nie wszystkie zostaną wyświetlone, skontaktuj się z producentem!")
        clear_main_window()
        header1 = tk.Label(window, text="DOSTĘPNE POSTACIE")
        header1.pack()
        table = tk.Frame()
        table.pack()
        footer1 = tk.Frame()
        footer1.pack(side=BOTTOM)
        for x in enumerate(files):
            if x[0] < 10:
                label_id = tk.Label(table, text=x[0] + 1).grid(row=x[0], column=0, padx=10, pady=10, sticky="e")
                character_id = tk.Label(table, text=x[1]).grid(row=x[0], column=1, padx=10, pady=10, sticky="e")
                tk.Button(table, text="Otwórz", command=lambda name=x[1]: display_sheet(name), width=15).grid(row=x[0],
                                                                                                              column=2,
                                                                                                              padx=10,
                                                                                                              pady=10,
                                                                                                              sticky="w")
        button_prev = tk.Button(footer1, text="Cofnij", command=menu, width=15)
        button_prev.grid(row=0, column=0, padx=10, pady=10, sticky="e")


def on_button_createCS_click_S():
    if check_yml_files() <= 10:
        postac = Character.Record()
        on_button_createCS_click(postac)
    else:
        messagebox.showinfo("Uwaga", "Za dużo kart postaci, należy jakąś usunąć!")


def check_yml_files():
    # files = []
    # path = os.path.join(r'characterSheets')
    # for f in os.listdir(path):
    #     if os.path.isfile(os.path.join(path, f)):
    #         files.append(f)
    # return len(files)
    return len([f for f in os.listdir(os.path.join(r'characterSheets')) if os.path.isfile(os.path.join(r'characterSheets', f))])


def save_to_yml(file, postac):
    character_data = yaml.dump(postac.__dict__)
    with open(file, "w") as file:
        file.write(character_data)
    postac.NS = 1
    menu()


def on_button_createCS_click(postac):
    window.title("Interaktywna karta postaci w systemie BRP - Tworzenie postaci")
    uW = 15  # Universal Width
    create_entry = [None] * 55
    create_entry_w = [['0' for _ in range(8)] for _ in range(5)]
    create_label = [None] * 55

    def back():
        postac.prev_step()
        on_button_createCS_click(postac)

    # dict = {1: displayIdentity,
    #         2: dispalyCharacteristics}
    # dict[postac.NS]()
    if postac.NS == 1:
        def save_identity():
            if postac.save_identity(create_entry) == 0:
                postac.next_step()
            else:
                messagebox.showinfo("Uwaga", "Wpisano nieprawidłową wartość!")
            on_button_createCS_click(postac)
        def display_identity():
            header1 = tk.Label(window, text="DANE BADACZA")
            header1.pack()
            table = tk.Frame()
            table.pack()
            footer1 = tk.Frame()
            footer1.pack(side=BOTTOM)
            for x in range(9):
                create_entry[x] = tk.Entry(table, width=30)
                create_entry[x].insert(0, postac.IdentityV[x])
                create_label[x] = tk.Label(table, text=postac.IdentityL[x])
                create_label[x].grid(row=x, column=0, padx=10, pady=10, sticky="e")
                create_entry[x].grid(row=x, column=1, padx=10, pady=10, sticky="w")
            button_next = tk.Button(footer1, text="Dalej", command=save_identity, width=uW)
            button_prev = tk.Button(footer1, text="Cofnij", command=back, width=uW)
            button_next.grid(row=0, column=1, padx=10, pady=10, sticky="w")
            button_prev.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        clear_main_window()
        display_identity()
    elif postac.NS == 2:
        def save_characteristics():
            if postac.save_characteristics(create_entry) == 0:
                postac.next_step()
            else:
                messagebox.showinfo("Uwaga", "Wpisano nieprawidłową wartość!")
            on_button_createCS_click(postac)

        def display_characteristics():
            header1 = tk.Label(window, text="CECHY")
            header1.pack()
            table = tk.Frame()
            table.pack()
            footer1 = tk.Frame()
            footer1.pack(side=BOTTOM)
            for x in range(8):
                create_entry[x] = tk.Entry(table, width=30)
                create_entry[x].insert(0, postac.CharacteristicsV[x])
                create_label[x] = tk.Label(table, text=postac.CharacteristicsL[x])
                create_label[x].grid(row=x, column=0, padx=10, pady=10, sticky="e")
                create_entry[x].grid(row=x, column=1, padx=10, pady=10, sticky="e")
            button_next = tk.Button(footer1, text="Dalej", command=save_characteristics, width=uW)
            button_prev = tk.Button(footer1, text="Cofnij", command=back, width=uW)
            button_next.grid(row=0, column=1, padx=10, pady=10, sticky="w")
            button_prev.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        clear_main_window()
        display_characteristics()
    elif postac.NS == 3:
        def save_hitpoints():
            if postac.save_hitpoints(create_entry) == 0:
                postac.next_step()
            else:
                messagebox.showinfo("Uwaga", "Wpisano nieprawidłową wartość!")
            on_button_createCS_click(postac)

        def display_hitpoints():
            header1 = tk.Label(window, text="PUNKTY TRAFIEŃ")
            header1.pack()
            table = tk.Frame()
            table.pack()
            footer1 = tk.Frame()
            footer1.pack(side=BOTTOM)
            for x in range(4):
                create_entry[x] = tk.Entry(table, width=30)
                create_entry[x].insert(0, postac.HitpointsV[x])
                create_label[x] = tk.Label(table, text=postac.HitpointsL[x])
                create_label[x].grid(row=x, column=0, padx=10, pady=10, sticky="e")
                create_entry[x].grid(row=x, column=1, padx=10, pady=10, sticky="e")
            button_next = tk.Button(footer1, text="Dalej", command=save_hitpoints, width=uW)
            button_prev = tk.Button(footer1, text="Cofnij", command=back, width=uW)
            button_next.grid(row=0, column=1, padx=10, pady=10, sticky="w")
            button_prev.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        clear_main_window()
        display_hitpoints()
    elif postac.NS == 4:
        def save_skills():
            if postac.save_skills(create_entry) == 0:
                postac.next_step()
            else:
                messagebox.showinfo("Uwaga", "Wpisano nieprawidłową wartość!")
            on_button_createCS_click(postac)

        def display_skills():
            def on_configure(event):
                table.update_idletasks()
                tableM.configure(scrollregion=table.bbox("all"))
                tableM.create_window((0, 0), window=table, width=window.winfo_width(), anchor=tk.NW)

            header1 = tk.Label(text="UMIEJĘTNOŚCI")
            header1.pack()
            body1 = tk.Frame()
            body1.pack(fill=tk.BOTH, expand=True)
            tableM = tk.Canvas(body1)
            tableM.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            scrollbar = tk.Scrollbar(body1, command=tableM.yview)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            tableM.configure(yscrollcommand=scrollbar.set)

            table = tk.Frame(tableM)
            table.columnconfigure(0, weight=1)
            table.columnconfigure(1, weight=0)
            table.columnconfigure(2, weight=0)
            table.columnconfigure(3, weight=0)
            table.columnconfigure(4, weight=0)
            table.columnconfigure(5, weight=1)

            footer1 = tk.Frame()
            footer1.pack(side=BOTTOM)
            for x in range(28):
                create_entry[(x * 2)] = tk.Entry(table, width=30)
                create_entry[(x * 2)].insert(0, postac.SkillsV[(x * 2)])
                create_label[(x * 2)] = tk.Label(table, text=postac.SkillsL[x * 2])
                create_label[(x * 2)].grid(row=x, column=1, padx=10, pady=10, sticky="e")
                create_entry[(x * 2)].grid(row=x, column=2, padx=10, pady=10, sticky="e")
                if x == 27:
                    continue
                else:
                    create_entry[(x * 2) + 1] = tk.Entry(table, width=30)
                    create_entry[(x * 2) + 1].insert(0, postac.SkillsV[(x * 2) + 1])
                    create_label[(x * 2) + 1] = tk.Label(table, text=postac.SkillsL[(x * 2) + 1])
                    create_label[(x * 2) + 1].grid(row=x, column=3, padx=10, pady=10, sticky="e")
                    create_entry[(x * 2) + 1].grid(row=x, column=4, padx=10, pady=10, sticky="e")

            tableM.bind("<Configure>", on_configure)

            button_next = tk.Button(footer1, text="Dalej", command=save_skills, width=uW)
            button_prev = tk.Button(footer1, text="Cofnij", command=back, width=uW)
            button_next.grid(row=0, column=1, padx=10, pady=10, sticky="w")
            button_prev.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        clear_main_window()
        display_skills()
    elif postac.NS == 5:
        def del_weapon(id):
            postac.del_weapon(id)
            on_button_createCS_click()

        def save_weapon():
            if postac.save_weapon(create_entry) != 0:
                messagebox.showinfo("Uwaga", "Wpisano nieprawidłową wartość!")
            on_button_createCS_click()

        def save_weapons():
            postac.next_step()
            on_button_createCS_click(postac)

        def display_weapons():
            header1 = tk.Label(text="BROŃ")
            header1.pack()
            body1 = tk.Frame()
            body1.pack()
            footer1 = tk.Frame()
            footer1.pack(side=BOTTOM)
            for x in range(9):
                tk.Label(body1, text=postac.WeaponL[x]).grid(row=0, column=x, padx=10, pady=10)
            for x in range(0, postac.WeaponsNb):
                tk.Label(body1, text=postac.WeaponsL[x]).grid(row=x + 1, column=0, padx=10, pady=10)
                tk.Label(body1, text=postac.WeaponsV[x][0]).grid(row=x + 1, column=1, padx=10, pady=10)
                tk.Label(body1, text=postac.WeaponsV[x][1]).grid(row=x + 1, column=2, padx=10, pady=10)
                tk.Label(body1, text=postac.WeaponsV[x][2]).grid(row=x + 1, column=3, padx=10, pady=10)
                tk.Label(body1, text=postac.WeaponsV[x][3]).grid(row=x + 1, column=4, padx=10, pady=10)
                tk.Label(body1, text=postac.WeaponsV[x][4]).grid(row=x + 1, column=5, padx=10, pady=10)
                tk.Label(body1, text=postac.WeaponsV[x][5]).grid(row=x + 1, column=6, padx=10, pady=10)
                tk.Label(body1, text=postac.WeaponsV[x][6]).grid(row=x + 1, column=7, padx=10, pady=10)
                tk.Label(body1, text=postac.WeaponsV[x][7]).grid(row=x + 1, column=8, padx=10, pady=10)
                tk.Button(body1, text="-", command=lambda id=x: del_weapon(id), width=3).grid(row=x + 1, column=9,
                                                                                              padx=10, pady=10,
                                                                                              sticky="w")
            if postac.WeaponsNb < 5:
                tk.Label(body1, text=postac.WeaponsL[postac.WeaponsNb]).grid(row=x + 2, column=0, padx=10, pady=10)
                create_entry[0] = tk.Entry(body1, width=5)
                create_entry[1] = tk.Entry(body1, width=5)
                create_entry[2] = tk.Entry(body1, width=5)
                create_entry[3] = tk.Entry(body1, width=5)
                create_entry[4] = tk.Entry(body1, width=5)
                create_entry[5] = tk.Entry(body1, width=5)
                create_entry[6] = tk.Entry(body1, width=5)
                create_entry[7] = tk.Entry(body1, width=5)
                create_entry[0].grid(row=x + 2, column=1, padx=10, pady=10)
                create_entry[1].grid(row=x + 2, column=2, padx=10, pady=10)
                create_entry[2].grid(row=x + 2, column=3, padx=10, pady=10)
                create_entry[3].grid(row=x + 2, column=4, padx=10, pady=10)
                create_entry[4].grid(row=x + 2, column=5, padx=10, pady=10)
                create_entry[5].grid(row=x + 2, column=6, padx=10, pady=10)
                create_entry[6].grid(row=x + 2, column=7, padx=10, pady=10)
                create_entry[7].grid(row=x + 2, column=8, padx=10, pady=10)
                tk.Button(body1, text="+", command=save_weapon, width=3).grid(row=x + 2, column=9, padx=10, pady=10,
                                                                              sticky="w")

            button_next = tk.Button(footer1, text="Dalej", command=save_weapons, width=uW)
            button_prev = tk.Button(footer1, text="Cofnij", command=back, width=uW)
            button_next.grid(row=0, column=1, padx=10, pady=10, sticky="w")
            button_prev.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        clear_main_window()
        display_weapons()
    elif postac.NS == 6:
        def save_armor():
            if postac.save_armor(create_entry) == 0:
                postac.next_step()
            else:
                messagebox.showinfo("Uwaga", "Wpisano nieprawidłową wartość!")
            on_button_createCS_click(postac)

        def display_armor():
            header1 = tk.Label(text="PANCERZ")
            header1.pack()
            body1 = tk.Frame()
            body1.pack()
            footer1 = tk.Frame()
            footer1.pack(side=BOTTOM)
            for x in range(3):
                create_entry[x] = tk.Entry(body1, width=30)
                create_entry[x].insert(0, postac.ArmorV[x])
                create_label[x] = tk.Label(body1, text=postac.ArmorL[x])
                create_label[x].grid(row=0, column=x, padx=10, pady=10)
                create_entry[x].grid(row=1, column=x, padx=10, pady=10)
            button_next = tk.Button(footer1, text="Dalej", command=save_armor, width=uW)
            button_prev = tk.Button(footer1, text="Cofnij", command=back, width=uW)
            button_next.grid(row=0, column=1, padx=10, pady=10, sticky="w")
            button_prev.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        clear_main_window()
        display_armor()
    elif postac.NS == 7:
        def save_equipment():
            if postac.save_equipment() == 0:
                postac.next_step()
            else:
                messagebox.showinfo("Uwaga", "Wpisano nieprawidłową wartość!")
            on_button_createCS_click(postac)

        def display_equipment():
            header1 = tk.Label(text="EKWIPUNEK")
            header1.pack()
            body1 = tk.Frame()
            body1.pack()
            footer1 = tk.Frame()
            footer1.pack(side=BOTTOM)

            button_next = tk.Button(footer1, text="Dalej", command=save_equipment, width=uW)
            button_prev = tk.Button(footer1, text="Cofnij", command=back, width=uW)
            button_next.grid(row=0, column=1, padx=10, pady=10, sticky="w")
            button_prev.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        clear_main_window()
        display_equipment()
    elif postac.NS == 0:
        postac.NS = 1
        if messagebox.askyesno("Wyjście", "Czy na pewno chcesz przerwać tworzenie postaci?"):
            menu()
        else:
            on_button_createCS_click(postac)
    elif postac.NS == 8:
        if messagebox.askyesno("Potwierdzenie", "Czy na pewno chcesz dodać utworzoną postać?") == True:
            path = os.path.join(r'characterSheets')
            file_name = "{}{}".format(postac.IdentityV[0], ".yaml")
            files = []
            for f in os.listdir(path):
                if os.path.isfile(os.path.join(path, f)):
                    files.append(f)
            if file_name in files:
                if messagebox.askyesno("Potwierdzenie",
                                       "Już istnieje postać o takiej nazwie, czy chcesz ją nadpisać?") == True:
                    save_to_yml(os.path.join(path, file_name), postac)
                else:
                    postac.NS = 7
                    on_button_createCS_click(postac)
            else:
                save_to_yml(os.path.join(path, file_name), postac)
        else:
            postac.NS = 7
            on_button_createCS_click(postac)



def on_button_option_click():
    # pass
    print("Button O clicked!")


def on_button_exit_click():
    if messagebox.askyesno("Wyjście", "Czy na pewno chcesz wyjść?") == True:
        window.destroy()


def clear_main_window():
    for widget in window.winfo_children():
        widget.destroy()


def menu():
    window.title("Interaktywna karta postaci w systemie BRP")
    clear_main_window()

    uW = 20  # Universal Width - Szerokość dla wszystkich guzików menu

    body = tk.Frame()
    body.pack()
    tk.Button(body, text="Wyświetl kartę postaci", command=on_button_displayCS_click, width=uW).grid(row=1, column=0,
                                                                                                     pady=20)
    tk.Button(body, text="Utwórz nową postać", command=on_button_createCS_click_S, width=uW).grid(row=2, column=0,
                                                                                                  pady=20)
    tk.Button(body, text="Opcje", command=on_button_option_click, width=uW).grid(row=3, column=0, pady=20)
    tk.Button(body, text="Wyjście", command=on_button_exit_click, width=uW).grid(row=4, column=0, pady=20)

    footer = tk.Frame()
    footer.pack(side=tk.BOTTOM, pady=10)

    global brp_logo
    try:
        brp_logo = ImageTk.PhotoImage(Image.open(os.path.join("BRP_logo.png")).resize((100, 100)))
        tk.Label(footer, image=brp_logo).grid(row=0, column=0, padx=10)
        bottom_label = tk.Label(footer,
                                text="To oprogramowanie opiera się na zasadach gry udostępnionych\nprzez Chaosium Inc. zgodnie z licencją BRP Open Game License, Version 1.0.",
                                font=("Arial", 10))
        bottom_label.grid(row=0, column=1, padx=10)
    except Exception:
        print("error during printing image")


def main():
    global window
    window = tk.Tk()
    window.geometry("800x600")
    window.minsize(800, 600)
    menu()
    window.mainloop()


if __name__ == "__main__":
    main()
