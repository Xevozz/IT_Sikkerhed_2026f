# IT_Sikkerhed_2026f

Dette er et skoleprojekt på Zealand Næstved.

Untitest opgave 1, test af Bart's Unittest's
<img width="1428" height="866" alt="Bart Unittest opgave 1" src="https://github.com/user-attachments/assets/289e9d81-7c87-4355-9f3f-9155c5494287" />

Untitest opgave 2, test af mine egne.

<img width="1433" height="876" alt="Bart Unittest opgave 2" src="https://github.com/user-attachments/assets/01f370a3-195a-4e29-9a0d-cc4c6ee9a2bc" />



# -- Opgave - Teststrategier -- # 
Jeg vælger Password, som mit emne.
- Da et login system kan opbygges af brugernavn + kode, låsning efter x antal forsøg.  Længde krav til disse parametre.


# -- Ækvivalensklasser -- #
Regler
- Password længde 8-20 tegn (meget generelt)
- Indeholder mindst ét tal og ét specialtegn

|   | Eksempel       | Type              | Godkendt / ikke godkendt |
|---|----------------|-------------------|--------------------------|
| 1 | Sikkerhed123!  | Gyldig            | Godkendt                 |
| 2 | ab1!           | For kort          | ikke godkendt            |
| 3 | Over 25 Tegn   | For langt         | ikke godkendt            |
| 4 | Sikkerhed!     | intet tal         | ikke godkendt            |
| 5 | Sikkerhed123   | intet specialtegn | ikke godkendt            |


# -- Grænseværdier -- #
Regler
- Password længde 8-20 tegn.

|   | Eksempel | Type       |                      | Godkendt / ikke godkendt |
|---|----------|------------|----------------------|--------------------------|
| 1 | 7 tegn   | lige under | under 8- 20 tegn     | ikke godkendt            |
| 2 | 8 tegn   | lige på    | lige på 8- 20 tegn   | godkendt                 |
| 3 | 9 tegn   | lige over  | lige over 8- 20 tegn | godkendt                 |
| 4 | 21 tegn  | intet tal  | over 8- 20 tegn      | ikke godkendt            |


# -- CRUD -- #
Lavet på en Bruger med:
Create, En bruger kan oprettes
Read, en bruger kan læse sin egen information
Update, man kan opdatere sin information
Delete, En bruger kan slettes
List, indhenter alt information, efterspurgt
- Man kunne tilføje en "lock" efter x antal forsøg, låses brugerens konti.


# -- Cycle Process test -- #
I dette projekt andvendes cycle process testen på en bruger.
følgende gentagne trin:
1. Oprettelse af bruger (Create)
2. Læsning af brugerdata (Read)
3. Opdatering af bruger password (Update)
4. Authentification af brugeren (korrekt data om bruger)
5. Sletning af en bruger (Delete)
6. Processen kan gentages for flere brugere.
Testen validere, at denne cyclus kan gennemføres gentagne gange i træk, uden at lave inkonsistente data i systemet, og at fejl håndteres korrekt ved diverse operationer. Så man ikke ender med "død/tom-data" i databasen.

# -- Test-Pyramiden -- #
Test-pyramiden er en teststrategi, som beskriver hvordan test bør fordelens, på diverse niveauer.

## Test Pyramiden, Bottom up ## 
er den tilgang jeg har valgt, da fokus primært er Unit-tests. Her er punkter som fx. tidlige fejl,som opdages ved at køre unit-test tidligt i processen. Samt hurtig eksekvering af tests.

Så vi kan bruge Unit-tests til at validere:
- CRUD-funktioner
- password-validering
igennem fx. Create_user, Update_user, Delete_user. funktionerne.
Hvilket skaber et godt miljø, hvor fejl opdages tidligt for de primære funktioner.

## Test Pyramiden Top Down ## 
Starter med End-to-End og UI-tests og bevæger sig derefter ned mod Unit-tests.

Fordele:
- hurtigt overblik over "brugerrejsen" da UI er mere i fokus
- Validere systemets samlede funktionalitet.

Ulemper:
- test er betydeligt langsomere
- fejl kan være sværere at lokalisere
- risici for at data-inputtet bliver for "overvældende"

## Test Pyramiden, Konsolidering med tooling ##
Gør brug af automatiserede testværktøjer (PyTest) så man opnår:
- hurtigt overblik
- hurtig eksekvering
- høj test dækning

i henhold til dette projekt.
- mange unit-test lavet i samme test-miljø Pytest.
- færre, men mere mplrettede tests.
- test køres automatisk via terminal og CI-pipelines.

# -- Decision table test -- #
I Dette projekt benyttes Decision Table test, til at validere brugeroprettelse og authentificering med fokus på passwrods

krav:
- er brugernavnet unikt ?
- overholder Password længdekravet (8-20 tegn) ?
- indeholder password mindst ét tal ?
- indeholder password mindst ét specialtegn ?

Resultater:
- bruger oprettes
- adgang gives
- adgang nægtes
- fejl besked (weakpassword / already exists)

|   | unikt brugernavn | 8-20 tegn | Tal i password | Specialtegn i password | Resultat              |
|---|------------------|-----------|----------------|------------------------|-----------------------|
| 1 | Ja               | Ja        | Ja             | Ja                     | Bruger oprettes       |
| 2 | Ja               | Nej       | Ja             | Ja                     | Afvist (WeakPassword  |
| 3 | Ja               | Ja        | Nej            | Ja                     | Afvist (WeakPassword  |
| 4 | Ja               | Ja        | Ja             | Nej                    | Afvist (WeakPassword  |
| 5 | Ja               | Nej       | Nej            | Nej                    | Afvist (WeakPassword  |
| 6 | Nej              | Ja        | Ja             | Ja                     | Afvist (AlreadyExists |
| 7 | Nej              | -         | -              | -                      | Afvist (AlreadyExists |

Anvendelse i koden.
Decision Table-reglerne er direkte implementeret og testet i følgende funktioner:
- Create_user()
- _validate_password()
- authenticate_user()

Decision table test hjælper IT-sikekrheden ved at:
- sikre at password reglerne overholdes
- reducere risici for svage passwords
- forhindre un-authorized brugeroprettelse
Dette sikrer at forskellige kombinationer af input, ikke fører til uforudset eller atypisk systemadfærd.








