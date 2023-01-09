# Izrada mentorskog sustava kao web aplikacije za predmet Programiranje na Internetu
 
Aplikacija omogucije:
*	Za studente:
    - Registraciju i autentikaciju
	- Upis/ispis predmeta
	- Promjena položeno/nepoloženo za upisane predmete
*	Za mentore:
	- Autentikaciju
	- Pregled liste studenata
	- Pregled i promjenu liste predmeta
	- Promjenu upisa za bilo kojeg studenta 
*	Za admina:
	- Sve funkcionalnosti koje imaju mentor i student
	- Pregled i uređivanje lista studenata i mentora


## Opis zadatka

U bazu su dodana tri korisnika (mentor, redovni i izvanredni student) sa e-mail adresom kao korisničkim imenom i šifrom.

Odabir studenata sa liste (za mentore), link za svakog studenta vodi na njegov upisni list.
Pregled predmeta (za mentore), linkovi omogućuju pregled i editiranje podataka o predmetu.
Upisni list (pogled mentora za studenta), dugmad omogućuje promjenu upisa (upiši/ispiši/položeno).

Na upisnom listu se prikazuje lista neupisanih predmeta i lista upisanih/položenih predmeta podijeljenih po semestrima (ovisno o statusu studenta). 
Izgled i funkcionalnosti upisnog lista su iste za studente i mentore (osim izbornika u vrhu stranice). 
Izbornik za studente ima samo stavku „logout“ i prikazuje se samo pripadajući upisni list. 
Izbornik za mentore ima „logout“, „predmeti“ i „studenti“ preko kojih pristupa ostalim prikazima.

Kôd je pisan u radnom okviru Django. Realiziran i organiziran kôd prema MVC (MVT) arhitekturi. 
Strukturu koja je relativno laka za proširiti sa manjim dodatnim funkcionalnostima (npr. dodati i prikazati zbroj upisanih ECTS bodova). 
