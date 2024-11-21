# smoke-guard
Smokeguard project for design challenge semester 1 @ Fontys ICT


Arduino (Sensor) – Deze registreert sigaretten tijdelijk op basis van knop



Python-script – Dit draai ik op mijn laptop

Wat doet het Python-script: Het Python-script is verantwoordelijk voor het versturen van een HTTP-verzoek naar de API. Dit HTTP-verzoek bevat de gegevens van de sigaretenteller die je hebt verhoogd op de Arduino.

Versturen van HTTP-verzoek: Het Python-script maakt een HTTP-verzoek naar je API met de count-waarde, zodat deze kan worden opgeslagen in de database. Dit gebeurt via een API-eindpunt zoals bijvoorbeeld http://192.168.153.127:5000/check_limit.



API – Dit is een webservice die ik draai op mijn vm deze ontvangt gegevens van mijn Python-script.

Wat doet de API: De API ontvangt het HTTP-verzoek van het Python-script. Dit verzoek bevat de count-waarde, die de sigaretenteller bijhoudt.  De API neemt de gegevens en slaat deze op in de database.

Werking API: De API ontvangt een HTTP-verzoek via een eindpunt (bijvoorbeeld /check_limit). Het gegevensveld count (aantal sigaretten) wordt ontvangen en geparsed. Deze gegevens worden ingevoegd in een database voor later gebruik.



Database – De API slaat de gegevens die ontvangen worden van de Python-script in een database op.



.NET MAUI App – Deze app haalt de gegevens op uit de database en toont ze aan de gebruiker.
