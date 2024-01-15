class Record:
    def __init__(self, NS=None, IdentityV=None, CharacteristicsV=None, HitpointsV=None, SkillsV=None, WeaponsV=None,
                 WeaponsNb=None, ArmorV=None):
        if IdentityV == None:
            self.NS = 1
            self.IdentityV = [""] * 9
            self.CharacteristicsV = [""] * 8
            self.HitpointsV = [""] * 8
            self.SkillsV = [""] * 55
            self.WeaponsV = [["" for _ in range(8)] for _ in range(5)]
            self.WeaponsNb = 0
            self.ArmorV = [""] * 3
        else:
            self.NS = NS
            self.IdentityV = IdentityV
            self.CharacteristicsV = CharacteristicsV
            self.HitpointsV = HitpointsV
            self.SkillsV = SkillsV
            self.WeaponsV = WeaponsV
            self.WeaponsNb = WeaponsNb
            self.ArmorV = ArmorV

    IdentityL = ["Imię i nazwisko: ",
                 "Rasa: ",
                 "Płeć: ",
                 "Wiek: ",
                 "Sylwetka: ",
                 "Zawód: ",
                 "Dominująca ręka: ",
                 "Cechy charakterystyczne: ",
                 "Opis: "]
    CharacteristicsL = ["Siła: ",
                        "Kondycja: ",
                        "Budowa Ciała: ",
                        "Zręczność: ",
                        "Wygląd: ",
                        "Intelekt: ",
                        "Moc: ",
                        "Wykształcenie: "]
    HitpointsL = ["Punkty Ruchu: ",
                  "Punkty życia: ",
                  "Punkty magii: ",
                  "Modyfikator Obrażeń: "]
    SkillsL = [
        "Wycena: ",
        "Sztuka: ",
        "Artyleria: ",
        "Targowanie: ",
        "Bójka: ",
        "Broń energetyczna: ",
        "Broń palna: ",
        "Chwytak: ",
        "Ciężka broń: ",
        "Ciężka maszyneria: ",
        "Dowodzenie: ",
        "Etykieta: ",
        "Gry: ",
        "Jazda: ",
        "Język: ",
        "Latanie: ",
        "Medycyna: ",
        "Napęd: ",
        "Naprawa: ",
        "Nauczanie: ",
        "Nauka: ",
        "Nawigacja: ",
        "Ocena: ",
        "Perswazja: ",
        "Pierwsza pomoc: ",
        "Pilot: ",
        "Pływanie: ",
        "Precyzyjna manipulacja: ",
        "Projekcja: ",
        "Przebranie: ",
        "Psychoterapia: ",
        "Punkt: ",
        "Rozbiórka: ",
        "Rzemiosło: ",
        "Rzucanie: ",
        "Rzut: ",
        "Skok: ",
        "Skradanie: ",
        "Słuchanie: ",
        "Status: ",
        "Strategia: ",
        "Sztuka: ",
        "Sztuki walki: ",
        "Szybka rozmowa: ",
        "Śledzenie: ",
        "Targowanie: ",
        "Ukrycie: ",
        "Umiejętności techniczne: ",
        "Czytanie i pisanie: ",
        "Unik: ",
        "Walka wręcz: ",
        "Wgląd: ",
        "Wiedza: ",
        "Wspinaczka: ",
        "Wykonanie: ",
        "Zmysł: ",
        "Zręczność"]
    WeaponsL = [
        "Broń 1: ",
        "Broń 2: ",
        "Broń 3: ",
        "Broń 4: ",
        "Broń 5: ", ]
    WeaponL = ["ID",
               "Broń",
               "Zdolność",
               "Spacjalność",
               "Baza %",
               "Obrażenia",
               "Ręce",
               "Penetracja",
               "Zasięg (metry)"]
    ArmorL = [
        "Pancerz",
        "Klasa pancerza",
        "Modyfikator"]

    def save_identity(self, data):
        error = 0
        for x in range(9):
            self.IdentityV[x] = self.validate_entry_text(data[x].get())
            if self.IdentityV[x] == "":
                error += 1
        if self.IdentityV[0]=="Brak danych": error=-1
        return error

    def save_characteristics(self, data):
        error = 0
        for x in range(8):
            self.CharacteristicsV[x] = self.validate_entry_int(data[x].get(), 3, 18)
            if self.CharacteristicsV[x] == "":
                error += 1
        return error

    def save_hitpoints(self, data):
        error = 0
        for x in range(4):
            self.HitpointsV[x] = self.validate_entry_int(data[x].get(), 2, 56)
            if self.HitpointsV[x] == "":
                error += 1
            else:
                self.HitpointsV[x + 4] = self.HitpointsV[x]
        return error

    def save_skills(self, data):
        error = 0
        for x in range(55):
            self.SkillsV[x] = self.validate_entry_int(data[x].get(), 1, 100)
            if self.SkillsV[x] == "":
                error += 1
        return error

    def save_weapon(self, data):
        error = 0
        self.WeaponsV[self.WeaponsNb][0] = self.validate_entry_text(data[0].get())
        self.WeaponsV[self.WeaponsNb][1] = self.validate_entry_text(data[1].get())
        self.WeaponsV[self.WeaponsNb][2] = self.validate_entry_text(data[2].get())
        self.WeaponsV[self.WeaponsNb][3] = self.validate_entry_int(data[3].get(), 1, 100)
        self.WeaponsV[self.WeaponsNb][4] = self.validate_entry_text(data[4].get())
        self.WeaponsV[self.WeaponsNb][5] = self.validate_entry_int(data[5].get(), 1, 2)
        self.WeaponsV[self.WeaponsNb][6] = self.validate_entry_int(data[6].get(), 0, 20)
        self.WeaponsV[self.WeaponsNb][7] = self.validate_entry_int(data[7].get(), 1, 100)
        for y in range(8):
            if self.WeaponsV[self.WeaponsNb][y] == "":
                error += 1
        if error == 0: self.WeaponsNb += 1
        return error

    def del_weapon(self, data):
        self.WeaponsV[data][0] = "-"
        self.WeaponsV[data][1] = "-"
        self.WeaponsV[data][2] = "-"
        self.WeaponsV[data][3] = "-"
        self.WeaponsV[data][4] = "-"
        self.WeaponsV[data][5] = "-"
        self.WeaponsV[data][6] = "-"
        self.WeaponsV[data][7] = "-"
        self.WeaponsV[data] = self.WeaponsV[self.WeaponsNb - 1]
        self.WeaponsNb -= 1

    def save_armor(self, data):
        error = 0
        self.ArmorV[0] = self.validate_entry_text(data[0].get())
        self.ArmorV[1] = self.validate_entry_int(data[1].get(), 0, 12)
        self.ArmorV[2] = self.validate_entry_text(data[2].get())
        if self.ArmorV[0] == "" or self.ArmorV[1] == "" or self.ArmorV[2] == "":
            error += 1
        return error

    def save_equipment(self):
        error = 0

        return error

    def next_step(self):
        self.NS += 1
        print(self.NS)

    def prev_step(self):
        self.NS -= 1

    def validate_entry_text(self, text):
        try:
            if len(text) > 0:
                return text
            else:
                return "Brak danych"
        except ValueError:
            return ""

    def validate_entry_int(self, number, front_end, back_end):
        try:
            if number == "":
                return front_end
            else:
                number = int(number)
                if front_end <= number and number <= back_end:
                    return number
                else:
                    return ""
        except ValueError:
            return ""
