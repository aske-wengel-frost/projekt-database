# Projekt-database

## Opgavebeskrivelse
Krav til projektet:

Databasen skal indeholde flere tabeller. Der skal være mindst en en-til-mange eller en mange-til-mange relation mellem tabellerne.
Databasen skal kunne tilgås enten ved hjælp af en GUI eller fra et terminalinput.
I får to moduler i uge 39 og to moduler i uge 40 til at få lavet jeres database og eventuelt GUI.

Den 5. oktober skal I afleverer jeres kode samt et ER-diagram over jeres database.

Den 25. oktober skal I aflevere jeres synopsis. I får modulet den 24. oktober til at lave de sidste finpudsninger på den. I kan ikke nå at skrive hele synopsisen i det modul, den skal være næsten færdig inden modulet.

## Databaseforklaring
Biblioteksdatabase:
Vi laver 3 tabeller:
Tabel 1 vil have følgende kolonner: Bog_id, Bog_Titel, Forfatter, Genre, År og Status (Udlånt eller tilgængeligt)
Tabel 2 vil have følgende kolonner: Lånere_id, Lånere_Navn, Bog_Titel og Udlånt_Dato
Tabel 3 vil have følgende kolonner: Lånere_id og Bog_id


Tabel 1: Bøger
- Kolonner: Bog_id (primær nøgle), Bog_Titel, Forfatter, Genre, År og Status.
- Relationer:
Denne tabel indeholder oplysninger om bøgerne i biblioteket.
Der er ingen direkte relation til de to andre tabeller, men kolonnen "Bog_Titel" bruges som en reference til at forbinde bøger med udlån og lånere.

Tabel 2: Lånere
- Kolonner: Lånere_id (primær nøgle), Lånere_Navn og Bog_Titel.
- Relationer:
Denne tabel indeholder information om bibliotekets lånere, herunder deres navne.
Kolonnen "Bog_Titel" bruges som en fremmed nøgle til at forbinde lånere med de bøger, de har lånt. Dette etablerer en en-til-mange-relation mellem lånere og bøger, da en låner kan have flere bøger udlånt.

Tabel 3: Udlån
- Kolonner: Lånere_id (fremmed nøgle), Bog_id (fremmed nøgle).
- Relationer:
Denne tabel fungerer som en junction-tabel (En mellem tabel som indeholder flere fremmednøgler), der forbinder lånere med de bøger, de har lånt.
Kolonnen "Lånere_id" henviser til en låner i Tabel 2, og kolonnen "Bog_id" henviser til en bog i Tabel 1.
Dette etablerer en mange-til-mange-relation mellem lånere og bøger, da en låner kan låne flere bøger, og en bog kan lånes af flere lånere (forskellige tidspunkter).
Hensigten med det tabel er ikke at se, hvem den nuværende lånere af en bog er (eller omvendt). Tværtimod (og udover at tabellen hjælper med at skabe en mange-til-mange relation mellem tabel 1 og 2), kan man vha. den tabel tjekke alle tidligere lånere af en hvis bog (og omvendt). 

