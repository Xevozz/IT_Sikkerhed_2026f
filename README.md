# IT_Sikkerhed_2026f

Dette er et skoleprojekt på Zealand Næstved.

Untitest opgave 1, test af Bart's Unittest's
<img width="1428" height="866" alt="Bart Unittest opgave 1" src="https://github.com/user-attachments/assets/289e9d81-7c87-4355-9f3f-9155c5494287" />

Untitest opgave 2, test af mine egne.

<img width="1433" height="876" alt="Bart Unittest opgave 2" src="https://github.com/user-attachments/assets/01f370a3-195a-4e29-9a0d-cc4c6ee9a2bc" />



Opgave - Teststrategier

Jeg vælger Password, som mit emne.
- Da et login system kan opbygges af brugernavn + kode, låsning efter x antal forsøg.  Længde krav til disse parametre.


Ækvivalensklasser
Regler
- Password længde 8-20 tegn (meget generelt)
- Indeholder mindst ét tal og ét specialtegn

Eksempler
Password = Sikkerhed123! = Godkendt
Password = ab1!! = ikke godkendt (for kort)
Password = over 25 tegn password! = ikke godkendt (for langt)
Password = Sikkerhed! = ikke godkendt (ingen tal)
Password = Sikkerhed123 = ikke godkendt (ingen specialtegn)


Grænseværdier
Regler
- Password længde 8-20 tegn.

Password = 7 tegn = ikke godkendt, 7 tegn.
Password = 8 tegn = godkendt, 8 tegn.
Password = 9 tegn = godkendt, mellem 8-20 tegn.
Password = 9 tegn = godkendt, mellem 8-20 tegn.
Password = 21 tegn = ikke godkendt, over 8-20 tegn.


CRUD
Lavet på en Bruger med:
Create, En bruger kan oprettes
Read, en bruger kan læse sin egen information
Update, man kan opdatere sin information
Delete, En bruger kan slettes
List, indhenter alt information, efterspurgt
- Man kunne tilføje en "lock" efter x antal forsøg, låses brugerens konti.



