class Rekord:
    def __init__(self, NS=None, IdentityV=None, CharacteristicsV=None, HitpointsV=None, SkillsV=None, WeaponsV=None, ArmorV=None):
        if IdentityV==None:
            self.NS = 1
            self.IdentityV = [""] * 9
            self.CharacteristicsV = [""] * 8
            self.HitpointsV = [""] * 8
            self.SkillsV = [""] * 55
            self.WeaponsV = [["" for _ in range(8)] for _ in range(5)]
            self.ArmorV = [""] * 3
        else:
            self.NS = NS
            self.IdentityV = IdentityV
            self.CharacteristicsV = CharacteristicsV
            self.HitpointsV = HitpointsV
            self.SkillsV = SkillsV
            self.WeaponsV = WeaponsV
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
                self.HitpointsV[x+4] = self.HitpointsV[x]
        return error
    def save_skills(self, data):
        error = 0
        for x in range(55):
            self.SkillsV[x] = self.validate_entry_int(data[x].get(), 1, 100)
            if self.SkillsV[x] == "":
                error += 1
        return error
    def save_weapons(self, data):
        error = 0
        for x in range(5):
            self.WeaponsV[x][0] = self.validate_entry_text(data[x][0].get())
            self.WeaponsV[x][1] = self.validate_entry_text(data[x][1].get())
            self.WeaponsV[x][2] = self.validate_entry_text(data[x][2].get())
            self.WeaponsV[x][3] = self.validate_entry_int(data[x][3].get(), 1, 100)
            self.WeaponsV[x][4] = self.validate_entry_text(data[x][4].get())
            self.WeaponsV[x][5] = self.validate_entry_int(data[x][5].get(), 1, 2)
            self.WeaponsV[x][6] = self.validate_entry_int(data[x][6].get(), 0, 20)
            self.WeaponsV[x][7] = self.validate_entry_int(data[x][7].get(), 1, 100)
            for y in range(8):
                if self.WeaponsV[x][y] == "":
                    error += 1
        return error
    def save_armor(self, data):
        error = 0
        self.ArmorV[0] = self.validate_entry_text(data[0].get())
        self.ArmorV[1] = self.validate_entry_int(data[1].get(), 0, 12)
        self.ArmorV[2] = self.validate_entry_text(data[2].get())
        if self.ArmorV[0] == "" or self.ArmorV[1] == "" or self.ArmorV[2] == "":
            error += 1;
        return error
    def save_equipment(self):
        error = 0

        return error
    def next_step(self):
        self.NS += 1
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