# Project-NS-Fietsenstalling
## **Project PROG Fietsenstaling NS**

**Benodigde Modules**
* Pillow    3.4.2
* Image     1.5.5
* Pip       8.1.1
* Pypotp    2.2.1
* Qrcode    5.3
* six       1.10.0

**Over het project**

In dit project moeten we een systeem na bootsen om een fiets te stallen in een systeem. Dit systeem houdt bij wie zijn fiets gestald heeft en de fiets krijgt een bijhorende fietsnummer. als de gebruiker zijn fiets wilt ophalen moet hij zijn fietsnummer en zelf verzonnen PIN code invullen. Tevens als extra verificatie hebben we Google Authenticator ingebouwd gebaseerd op het Time-Based One-Time Password Algorithm (TOTP). Deze geeft een zes cijferige code die in het programma moet worden ingevoerd. Indien de code juist is wordt er pas een actie uit gevoerd
Het project zelf maakt ook gebruik van een SQL-Database waar verschillende informatie naartoe wordt geschreven.

