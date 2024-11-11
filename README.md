# smoke-guard
Smokeguard project for design challenge semester 1 @ Fontys ICT


Arduino (Sensor) – Deze registreert sigaretten tijdelijk op basis van knop



Python-script – Dit draai ik op mijn laptop

Wat doet het Python-script: Het Python-script is verantwoordelijk voor het versturen van een HTTP-verzoek naar de API. Dit HTTP-verzoek bevat de gegevens van de sigaretenteller die je hebt verhoogd op de Arduino.

Versturen van HTTP-verzoek: Het Python-script maakt een HTTP-verzoek (meestal een POST of PUT verzoek) naar je API met de count-waarde, zodat deze kan worden opgeslagen in de database. Dit gebeurt via een API-eindpunt zoals bijvoorbeeld http://192.168.153.127:5000/insert_record, afhankelijk van hoe je API is opgezet.



API – Dit is een webservice die ik draai op mijn vm deze ontvangt gegevens van mijn Python-script.

Wat doet de API: De API ontvangt het HTTP-verzoek van het Python-script. Dit verzoek bevat de count-waarde, die de sigaretenteller bijhoudt.  De API neemt de gegevens en slaat deze op in de database.

Werking API: De API ontvangt een HTTP-verzoek via een eindpunt (bijvoorbeeld /insert_record). Het gegevensveld count (aantal sigaretten) wordt ontvangen en geparsed. Deze gegevens worden ingevoegd in een database voor later gebruik, bijvoorbeeld met de juiste tijdstempel en eventueel een gebruikers-ID of profiel-ID.



Database – De API slaat de gegevens die ontvangen worden van de Python-script in een database op.



.NET MAUI App – Deze app haalt de gegevens op uit de API en toont ze aan de gebruiker.

Wat de app doet: De app stuurt een HTTP GET-verzoek naar de API en vraagt de laatst opgeslagen gegevens op (de sigarettentellerdata). Dit wordt gedaan door middel van een API-aanroep. De app maakt gebruik van een ApiService-klasse die via een HTTP-client een verzoek naar de API stuurt. Als de gegevens met succes worden opgehaald, worden ze geconverteerd naar een lijst van records (bijvoorbeeld een lijst met objecten die het aantal sigaretten, de tijd, etc. bevatten).

Visuele weergave in de app: Nadat de gegevens zijn opgehaald, toont de app deze in een ListView. De ListView toont bijvoorbeeld elke count (sigaretten), samen met andere relevante informatie zoals de tijdstempel van wanneer het aantal is verhoogd.

Hier versturen we de ontvangen records naar een list view voor de display van de counter.

