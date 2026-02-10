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


# -- Security Gates -- #

| TestTeknik          | Security Gates           |
|---------------------|--------------------------|
| Ækvivalensklasser   | Code / Dev gate          |
| Grænseværditest     | Code / Dev gate          |
| CRUD (L)            | Code / Dev gate          |
| Decision Table Test | Code / Dev gate          |
| Cycle Process Test  | Integration Gate         |
| Test-Pyramiden      | System / End-to-End Gate |

## Code / Dev Security gate (lokal / test miljø) ##
Følgende teknikker er placeret her, grundet:

### Ækvivalensklasser
- Input validering af Password og Brugernavn
- Sikrer gyldig og ugyldig inout behandles korrekt

### Grænseværditest
- Tester Password længden (8-20ntegn)
- Forebygger svage eller ugyldige passwords

### CRUD (L)
- Tester: Create, Read, Update, Delete og List
- Sikrer korrekt brug af brugerdata

### Decision Table test (Password & bruger)
- tester kombinationer af password krav og brugeroprettelsen


## Integration Security Gate (Integrations miljøet)
Følgende teknikker er placeret her, grundet:

### Cycle Process Test
- tester brugerflows gentagne gange (create, update, authentication & delete)
- sikrer systemets stabilitet over flere cyklusser

## System / End-to-End Security Gate (staging miljøet)

### Test-pyramiden
- validerer vitale brugerrejser
- sikrer at sikkerhedsmæssige funktiuoner, fungere korrekt i systemet.

Ved at inddele disse forskellige test-teknikker i relevante security gates, opnår:
- Tidlig identificering af sikkerhedsproblemer
- Giver en lavere risici for fejl ved release
- Giver en struktureret og sikker udviklingsprocess.

----------------------------------------------------------------------------


# Flat File Database – IT-Sikkerhed (Opgave 1: SVÆR)

# ----- Formålet med denne opgave er at implementere en **flat file database** -----
baseret på JSON-fil, designe og implementere unit tests ved brug af testdesign-teknikker samt dokumentere løsningen.

# ----- Hvorfor er det smart at bruge en flat file DB? -----
En flat file database er fornuftigt brugt i mindre systemer fordi:

- implementationen er simpel og kræver ingen database-server connection
- Data lagres i JSON, let at debugge.
- Den nemt/simpelt sat op, hvilket gør den ideel til prototyper.
- Den kan testes nemt, da JSON-filer kan oprettes og slettes.
- Den passer godt til opgaver, hvor datamængden er begrænset.

I større systemer vil man typisk anvende en rigtig database, men til denne opgave giver en flat file DB rigtig god mening.

---

# ----- Database-design -----
Flat file databasen er implementeret i:
Databasen gemmer brugerdata i en JSON-fil med følgende felter:

- `person_id`
- `first_name`
- `last_name`
- `adress`
- `street_number`
- `password`
- `enabled`

JSON-filen oprettes automatisk, hvis den ikke findes i forvejen. I unit tests anvendes `pytest` &`tmp_path`, så hver test får sin egen JSON-fil.

# ----- Testdesign og funktionalitet -----
Test cases er designet med fokus på:

- CRUD-funktionalitet (Create, Read, Update, Delete)
- Auth-logik (password og enabled-status)
- Persistence (data bliver korrekt skrevet og læst fra JSON)


# ----- Unit tests Screenshot -----


# ----- Given / When / Then -----
Alle test cases er med tydelige kommentarer:

- Given – forudsætning for testdata
- When – handlingen der udføres
- Then – forventet resultat (assert)


# ----- Risici hvis tests ikke består -----
Hver test indeholder en kort kommentar om risikoen, hvis testen fejler, fx:

- Hvis oprettelse af bruger fejler → Resultat = data kan gå tabt.
- Hvis login accepterer forkert password → Resultat = kritisk sikkerhedsfejl.
- Hvis disabled brugere kan logge ind → Resultat = adgangskontrol virker ikke.
- Hvis data ikke kontinuerligt er korrekt → Resultat = systemet opfører sig ustabilt.

--------------------------------------------------------------------------------


# Kryptering + Hashing – IT-Sikkerhed (Opgave 2: SVÆR)

# ----- Hvilke algoritmer er valgt – og hvorfor? -----
- **Kryptering:** `Fernet` (fra `cryptography`)  
  Fernet er en symmetrisk krypteringsløsning, der er nem at bruge korrekt og inkluderer både kryptering og integritetsbeskyttelse (så data ikke kan ændres uden at det opdages).
- **Password hashing:** `PBKDF2-HMAC-SHA256` (Python stdlib `hashlib.pbkdf2_hmac`)  
  Passwords hashes one-way med salt og mange iterationer (key stretching), så brute force bliver markant dyrere.

# ----- Hvad krypteres, og hvad hashes? -----
# Krypteres (persondata / GDPR):**
- `first_name`, `last_name`, `adress`, `street_number`, `email`, `telefon`, `by`

# Hashes (kun password):**
- `password`

Passwords krypteres ikke, fordi de aldrig skal kunne gendannes. De hashes og verificeres ved sammenligning.

# ----- Hvornår krypteres data? -----
Data krypteres før den bliver gemt i JSON-filen.
Det betyder at JSON-filen ikke indeholder klartekst for persondata.

# ----- Hvornår dekrypteres data? -----
Data dekrypteres når det er nødvendigt, fx når en bruger hentes via `get_user_by_id(...)`.
Password dekrypteres aldrig, da det er hashed.

# ----- Hvornår fjernes dekrypteret data fra hukommelsen? -----
Dekrypterede værdier bruges kun lokalt i metoden og forsvinder, når det afsluttes (når funktionen returnerer). Det minimerer eksponering i RAM.

# ----- Hvor ligger implementeringen? -----
- Database: `src/flat_file/flat_file_db.py`
- Kryptering & hashing: `src/flat_file/flat_file_cryptography.py`

# ----- Unit-Tests Screenshot -----




