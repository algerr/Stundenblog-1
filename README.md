![Blogeinträge-header png](https://user-images.githubusercontent.com/111282979/203018930-fa86261e-0910-4fc8-a5cf-bf9099fd51e4.png)

|[Blogeintrag-15.08.22](#blogeintrag-15082022)|[Blogeintrag-22.08.22](#blogeintrag-22082022)|[Blogeintrag-25.08.22](#blogeintrag-25082022)|[Blogeintrag-29.08.22](#blogeintrag-29082022)|
:-------------------:|-------------------:|-------------------:|-------------------:|
[Blogeintrag-05.09.22](#blogeintrag-05092022)|[Blogeintrag-08.09.22](#blogeintrag-08092022)|[Blogeintrag-12.09.22](#blogeintrag-12092022)|[Blogeintrag-19.09.22](#blogeintrag-19092022)|[Blogeintrag-22.09.22](#blogeintrag-22092022)|
[Blogeintrag-26.09.22](#blogeintrag-26092022)|[Blogeintrag-06.10.22](#blogeintrag-06102022)|[Blogeintrag-24.10.22](#blogeintrag-24102022)|[Blogeintrag-03.11.22](#blogeintrag-03112022)|
[Blogeintrag-07.11.22](#blogeintrag-07112022)|[Blogeintrag-14.11.22](#blogeintrag-14112022)|[Blogeintrag-17.11.22](#blogeintrag-17112022)|[Blogeintrag-21.11.22](#blogeintrag-21112022)|
[Blogeintrag-12.12.22](#blogeintrag-12122022)|

## Blogeintrag-15.08.2022

Heute fand die erste Informatikstunde statt, in der wir uns mit der Frage beschäftigt haben, was im Informatikunterricht behandelt wird. Dabei wurde klar erläutert, dass der Informatikunterricht an der Stormarnschule sehr individuell und projektorientiert stattfindet und somit kein Frontalunterricht entsteht. Die Projektideen werden sich in 2er Gruppen überlegt und daraufhin bis zu einer Deadline im Dezember erarbeitet und durch Blogeinträge in jeder Stunde dokumentiert, wie bei diesem hier für den 15. August. Was die Projekte angeht, ist die Entscheidung jeder Gruppe selbst überlassen. Von visuellen Blocksprachen über Websprachen wie Javascript bis zu C/++ ist alles möglich. Auch Hardware kann mit Hilfe von Arduinos sowie Zubehör und Bibliotheken programmiert werden. Aufgrund der großen Vielzahl an Möglichkeiten, kamen wir in der ersten Stunde noch nicht auf unsere Idee. Eine grundlegende Vorstellung hatten wir jedoch: Unsere Idee sollte softwarebasiert sein.

## Blogeintrag-22.08.2022

Wer eine Sprache erlernen will, kann sie nicht umgehen und spätestens seit der weiterführenden Schule sind sie aus dem Leben eines jeden von uns nicht mehr wegzudenken. **Vokabeln**. Doch ein Problem, das leider bisher keine Lösung hatte, stand dem "leichten Lernen nebenbei" schon immer im Weg. Um Vokabeln zu lernen muss entweder analog oder digital nachgeschlagen und mit voller Konzentration auf das jeweilige Medium geschaut werden, damit das Erlernen erfolgreich ist. Doch sich diese Zeit zu nehmen, ist für viele Menschen heutzutage gar nicht möglich, da noch so viele andere Dinge zu erledigen sind. Deshalb ist unsere Idee, einen Vokabeltrainer zu entwickeln, durch den man ganz nebenbei mit Spracherkennung Vokabeln lernen kann **VocabNow**. Man nimmt seine Kopfhörer und schon kann man, während z.B. die Hausarbeit erledigt wird, seinen Wortschatz erweitern und man muss sich keine Zeit nehmen, um auf altmodische Art und Weise Vokabeln zu lernen. Als Entwicklungsumgebung (IDE) verwenden wir [Replit.com](https://www.replit.com), da diese uns eine ferngesteuerte Arbeit ermöglicht, sodass bei Krankheit und nach dem Unterricht am Projekt weitergearbeitet werden kann. Der Name **VocabNow** rührt daher, dass unser Vokabeltrainer ein Lernen auf Knopfdruck ermöglichen soll. In jeder Situation und Lage soll es möglich sein, seinen Wortschatz zu erweitern, ohne sich auf sein Handy konzentrieren zu müssen. Stand 22. August 2022 gibt es keinen anderen Vokabeltrainer, der diese Möglichkeit bietet. Für die Spracherkennung wird „WebKitSpeechRecognition“ aus der Webspeech API, bereitgestellt durch das [Mozilla Developer Network](https://developer.mozilla.org/de/), genutzt. Darüberhinaus haben wir für den Anfang eine Datenbank mit 10 englischen Vokabeln erstellt, welche als Probelauf dienen soll, um zu zeigen, ob das Ganze funktioniert. Für die [MySQL-Datenbank](https://www.mysql.com/) wird  [RemoteMySQL](https://remotemysql.com/) genutzt, was uns das Erstellen und Verwalten online möglich macht. Zu Beginn bestand das Problem, mehrere Datensätze für dieselbe Vokabel zu haben. Nach kurzer Zeit fanden wir jedoch heraus, wie sich ein Datensatz löschen ließ. Die nächste Herausforderung bestand jedoch nun darin, eine zufällige Vokabel ausgeben zu können, da das Vokabellernen in der immer gleichen Reihenfolge auf Dauer keinen Sinn ergibt. Leider funktionierte das Ganze bis zum Ende der Stunde nicht wirklich, sodass wir uns der Lösung dieses Problems in der nächsten Stunde widmen werden.

[![image](https://user-images.githubusercontent.com/111282979/205522504-f448b185-96fb-4b62-862a-c1130ec3594f.png)](https://www.replit.com)
[![image](https://user-images.githubusercontent.com/111282979/205522709-038dc572-3013-45fd-9f64-c4ca51cd3599.png)](https://www.mysql.com)

## Blogeintrag-25.08.2022

Da uns das Problem der letzten Stunde mit der zufälligen Ausgabe von Vokabeln auch danach noch beschäftigte, arbeiteten wir zu Hause daran weiter und fanden bald eine Lösung. Dafür wurde in der Datenbank im Table *Eng_De* ein Wert **Vocab** eingegeben, der von nun an alle Vokabeln von Englisch zu Deutsch im Format **Englisch_Deutsch** beinhaltet. Damit ist die zufällige Ausgabe von Vokabeln nun ein Kinderspiel und der ausgegebene Wert muss nur im Unterstrich getrennt werden, sodass die englische und deutsche Vokabel einzeln verwendet werden können. Da Laurenz leider krankheitsbedingt abwesend war und Daniel über keine weitreichenden Programmierkenntnisse verfügte, widmete er sich der Erstellung der Webseite, über die VocabNow später laufen soll. Er erlernte in den beiden Doppelstunden die Grundlagen der Auszeichnungssprache [**HTML (Hyper-Text-Markup-Language)**](https://de.wikipedia.org/wiki/Hypertext_Markup_Language). Außerdem überlegte er sich, was man noch in die App einbauen könne. So entstand die Idee, dem Nutzer die Bedienung der Seite erheblich zu erleichtern, sodass, wie im vorigen Blogeintrag bereits beschrieben, ein Vokabellernen auf Knopfdruck möglich ist. Doch durch die Möglichkeit, am Projekt auch ferngesteuert zu arbeiten, konnte auch Laurenz seinen Teil leisten, indem er am "Backend", der Entwicklung des Systems hinter der Webseite, weiterarbeitete.

![image](https://user-images.githubusercontent.com/65679099/207005106-61316a9c-2c84-46e5-a528-ffb6986166a6.png)
![carbon (11)](https://user-images.githubusercontent.com/65679099/207887451-e52651a4-5fbc-48c1-aac7-e682d1e1534e.png)

## Blogeintrag-29.08.2022

Da Laurenz leider krankheitsbedingt nicht anwesend sein konnte, fokussierte sich Daniel heute auf das Erlernen der Programmiersprache Javascript, die bei einer Webseite für Funktionalität sorgt. Des Weiteren fing er an, die bisherigen Blogeinträge im Repository auf GitHub hochzuladen. Somit kann Laurenz die Blogeinträge später noch überarbeiten, sodass sie alle beisammen auf dem neusten Stand sind.

## Blogeintrag-05.09.2022

Heute war Laurenz wieder da, weshalb nun endlich eine effiziente Arbeit an unserem Projekt möglich war. Nun haben wir uns damit befasst, mit [**CSS (Cascading-Style-Sheets)**](https://de.wikipedia.org/wiki/Cascading_Style_Sheets) die Webseite nutzerfreundlich zu machen. An der, von Daniel erstellten Webseite der letzten Stunde, arbeiteten wir weiter und nahmen besonders in Bezug auf den Hintergrund Änderungen vor. Uns stand der Sinn nach etwas außergewöhnlichem, wie z.B. der Hintergrundfarbenkombination aus Königsblau (#4169e1), Lindgrün (#3bb78f), Dunkelcyan (#0bab64), wobei Königsblau (#4169e1) die eigentliche Hintergrundfarbe sein sollte und Lindgrün (#3bb78f) mit Dunkelcyan (#0bab64) das Muster bilden sollte. Wir hatten auch noch speziell versucht, für das Muster einen "Linear-Gradienten" einzubauen, um einen konstanten Farbübergang zu ermöglichen. Letztendlich haben wir uns dann doch dazu entschieden, den "Linear-Gradienten" nicht zu benutzen, weil das gewünschte Ergebnis leider nicht erzielt werden konnte. Vielleicht können wir das ja in der nächsten Stunde beenden.

![image](https://user-images.githubusercontent.com/111282979/205522775-52654479-3df5-4e7d-89f0-909ed80267f1.png)

## Blogeintrag-08.09.2022
In den letzten Tagen haben wir uns mit der Frage auseinandergesetzt, wie wir einen Hintergrund erstellen können, der unsere Nutzer bei Laune hält und amüsant wirkt. Dabei sind wir auf die Idee gekommen einen ["Particles-JS"](https://particles.js.org/) Hintergrund zu erstellen. Der Hintergrund, welchen wir gewählt, bzw. erstellt haben, soll die Wirkung eines leeren Weltraums vermitteln, was wiederum beruhigend wirken soll, um aus dem stressigen Altag herauszukommen und entspanntes Lernen zu ermöglichen. Als Farbenschrift haben wir uns für Orange entschieden, weil das die Spontanität beflügelt und Lebensfreude verleiht. Zudem ist Orange auch in der Lage, Selbstvertrauen und Unabhängigkeit bei unseren Nutzern zu implizieren. Darüberhinaus bauten wir unseren "Slogan" in unsere Webseite ein. "Lerne, wann und wo du willst." Dieser "Slogan" charakterisiert ziemlich präzise die Absicht hinter unserem Projekt. Der Vokabeltrainer soll überall und zu jederzeit abrufbar sein. Der Nutzer soll entscheiden können, wann und wo er lernen möchte. Nachdem nun das Design soweit fertig war, erstellten wir den lange geplanten "Button", wodurch mit einem Klick die Weiterleitung zum "Start" des Vokabeltrainers erfolgen sollte. Nun bestand die Schwierigkeit darin, unsere Spracherkennung, das ["Webkitspeechrecognition"](https://developer.mozilla.org/en-US/docs/Web/API/SpeechRecognition), einzubauen. Mit diesem Problem werden wir uns dann in der nächsten Stunde auseinandersetzen.

![image](https://user-images.githubusercontent.com/65679099/207006861-6e88dd1a-216d-49bd-bc9c-0903ac8de394.png)

## Blogeintrag-12.09.2022

In dieser Doppelstunde haben wir uns ausgiebig damit auseinandergesetzt, das ["Webkitspeechrecognition"](https://developer.mozilla.org/en-US/docs/Web/API/SpeechRecognition) in unsere Website einzubauen. Während die Schwierigkeiten anfangs schier unüberwindbar schienen waren sie mithilfe der Dokumentation gut lösbar. Als Zusatz wollten wir ebenfalls noch einen Geräusch einbauen, das die richtige Antwort akustisch erkennbar machen sollte. Zwar funktionierte die Wiedergabe der Audiodatei auf Windows, jedoch leider nicht auf iOS. Dieses Problem scheint, da das automatische Abspielen von Audiodateien im Browser von iOS blockiert wird, momentan unlösbar. Deshalb widmeten wir uns der Integration der [MySQL-Datenbank](https://www.mysql.com/). Diese Aufgabe begleitet uns in die nächste Stunde.

![blogeintrag laurenz 1](https://user-images.githubusercontent.com/111282979/205521938-bb3dd0ce-d1d9-4088-a279-ec8eae2bb287.png) ![image](https://user-images.githubusercontent.com/111282979/205522878-e2d70ea1-f1f7-433c-85d9-8a7a5ea865c1.png)

## Blogeintrag-19.09.2022

Nach mehreren Versuchen, die [MySQL-Datenbank](https://www.mysql.com/) einzubauen, fiel uns auf, dass es auch noch eine einfachere Methode gab, die Vokabeln abzurufen und die passende Übersetzung dazu zu erhalten. Nach intensivem Überlegen sind wir zu dem Entschluss gekommen, eine Art Wörterbuch statt der [MySQL-Datenbank](https://www.mysql.com/) zu nutzen.
[**JSON (Javascript Object Notation)](https://www.json.org/json-de.html) ist ein Programmiersprachen unabhängiges Textformat, das sich sehr zur Datenverarbeitung eignet. Nach anfänglichen Schwierigkeiten, lies sich die [JSON](https://www.json.org/json-de.html)-Wörterbuch-Technik dann doch integrieren.

## Blogeintrag-22.09.2022

Nun ist der Vokabeltrainer schon sehr weit gediehen. Der Vokabeltrainer ist bereits in der Lage ungefähr die Hälfte der Vokabeln zu erkennen. Leider muss sich die Seite nach jeder Vokabel aktualisieren, um ein zufällige weitere auszugeben. Diese beiden Mängel sind nun noch zu beheben. Nach der ersten Stunde haben wir es nun geschafft, nachdem die richtige Vokabel erkannt wurde, die nächste Vokabel direkt auszugeben, aber das Problem, dass nicht jede Übersetzung erkannt wurde, bestand leider weiterhin. Selbst nach dem Ende der beiden heutigen Informatikstunden wurde das Problem mit der Spracherkennung immer noch nicht behoben. Daran arbeiten wir in der nächsten Stunde weiter.

![blogeintrag laurenz 2](https://user-images.githubusercontent.com/111282979/205522000-f3d112cd-4f45-480d-a452-b73058150949.png)


## Blogeintrag-26.09.2022

Die Spracherkennung wurde heute nochmal mehrmals getestet und funktioniert einwandfrei. Eine Vorlesestimme, welche die abgefragten Vokabeln vorliest, wurde ebenfalls eingebaut, funktioniert aber leider nicht auf iOS, wegen der bereits genannten Sicherheitsblockade. Zum Glück bezieht sich dies nur auf Webseiten, weshalb wir das Problem mit der Umwandlung unseres Vokabeltrainers in eine App beheben können sollten. Ebenfalls hatten wir uns überlegt, eine Funktion einzubauen, um Vokabeln, die man nicht kennt, überspringen zu können. Das soll erfolgen können, wenn die Spracherkennenung den Begriff "Weiter" vernimmt. Leider ist dies nun zu unserer größten Herausforderung geworden, weshalb wir uns damit noch mehr auseinandersetzen werden. Stattdessen haben wir aber bereits einen Zähler für richtige und falsche Vokbalen eingefügt, damit man eine Quote sieht, wie gut, bzw. schlecht man die Vokabeln kann. Die grüne "0" steht dabei für die Anzahl der richtig beantworteten Vokabeln und die rote "0" für die nicht beantworteten Vokabeln.

![carbon (7)](https://user-images.githubusercontent.com/65679099/207882704-c49daf65-b4e2-4f20-8d63-061a4aefebc2.png)


## Blogeintrag-06.10.2022

Heute beschäftigen wir uns damit, die Text-To-Speech-Funktion in unseren Vokabeltrainer einzubauen, sodass die gefragte Vokabel automatisch vorgelesen wird. Zudem möchten wir einen "Button" einbauen, der es dem Nutzer ermöglichen soll, direkt auf Knopfdruck zurück zum Menü zu gelangen. Der Einbau des Buttons lief relativ schnell, während das Einbauen der Tex-To-Speech-Funktion Zeit benötigte. Mit dem Online-Dienst "[AppsGeyser]("https://www.apssgeyser.com)" konnten wir die Webseite bereits zu einer Android App konvertieren. Nach der Konvertierung war die App leider nicht richtig benutzbar, weshalb wir in der nächsten Stunde daran weiterarbeiten werden und auch schon versuchen, die App auch für iOS zugänglich zu machen.

![image](https://user-images.githubusercontent.com/111282979/205522951-00921a66-bb98-4ff6-95fa-8a468d7bb3c5.png)


## Blogeintrag-24.10.2022

Leider scheiterte das "VocabNow"-Projekt daran, dass ein Apple-Developer-Account benötigt wird, um Apps für iOS zu veröffentlichen, sodass man diese herunterladen kann. Leider ist es aktuell mit unseren finanziellen Mitteln jedoch nicht möglich, die jährliche Gebühr von 100€ für den Account zu stemmen. Deshalb entschlossen wir uns, in den Herbstferien dazu, ein neues Projekt zu beginnen, welches nicht aufgrund von finanziellen Problemen scheitern sollte. Wir überlegten uns eine Evolutionssimulation und waren innerhalb der Ferien mit dem Projekt schon sehr weit. Der Frust des gescheiterten VocabNow-Projekts hatte uns viel Motivation verliehen. Heute arbeiteten wir an einzelnen Details, wie der Behebung des Problems, dass sich mehrere Wesen auf einem Feld befinden können und fügten noch exaktere Kommentare , um die Funktionen unseres neuen Projekts verständlich darzulegen. Auch die Umbenennung einiger Variablen ermöglicht nun eine bessere Orientierung im Quelltext.

## Blogeintrag-03.11.2022

Da die Funktionen des Projektes nun größtenteils endgültig sind, haben wir die heutige Doppelstunde damit verbracht, die Dokumentation auf GitHub sowie die Blogeinträge zu verschönern. Während Daniel die Blogeinträge überarbeitete, verschönerte Laurenz den Quelltext und versah in mit den letzten, nötigen Kommentaren. Um eine bessere Übersichtlichkeit zu erschaffen, haben wir die Daten der Blogeinträge in einer Tabelle am Anfang aufgelistet. So kann man direkt zum gewünschten Datum springen. Zudem haben wir weitere Grafiken hinzugefügt. 
Am Anfang der Dokumentaton ist nun ein GIF von der laufenden Simulation zu sehen.

## Blogeintrag-07.11.2022

In der heutigen Doppelstunde haben wir weiterhin an den genannten Plänen vom 03.11.2022 gearbeitet. Weitere Grafiken und Texte haben wir hinzugefügt. Dabei haben wir [Carbon](https://carbon.now.sh/) für die Darstellung der Quelltextausschnitte genutzt, um die Dokumentation ansprechender und schöner zu gestalten.
Für die Erstellung weiterer Grafiken, wie beispielsweise dem Genom, haben wir den kostenlosen Service [Canva](https://canva.com/) genutzt.

[![image](https://user-images.githubusercontent.com/111282979/207607695-f59cfdbe-e0de-4130-9376-e7e96c5d09e6.png)](https://carbon.now.sh/)
[![image](https://user-images.githubusercontent.com/111282979/207607990-3a563ed5-2677-4991-8928-ec93aa2e8a44.png)](https://canva.com/)


## Blogeintrag-14.11.2022

Trotz dessen, dass Herr Buhl in dieser Doppelstunde krankheitsbedingt ausfallen musste, konnten wir selbstständig an unserem Projekt weiterarbeiten. Wir hatten hierzu Kommentare im Quelltext überarbeitet und die Erklärungstexte nochmals verbessert formuliert, weil diese, unserer Ansicht nach, nicht verständlich genug waren. Außerdem haben wir noch passende Abbildungen zu den Texten zur Visualisierung hinzugefügt. Bei der Bearbeitung ist uns noch aufgefallen, dass die Quellen bei den verschiedensten Dingen fehlten, weshalb wir diese raussuchen mussten, und in die passenden Zeilen in den einzelnen Texten ergänzt haben. 
![image](https://user-images.githubusercontent.com/111282979/207611589-f3a4b4bd-9eb1-4fba-8cff-06e6685572c4.png)


## Blogeintrag-17.11.22 

Die heutige Arbeit war sehr erfolgreich, da wir dazu im Stande waren, die Überschriften und Banner für die Dokumentation des Projektes zu erstellen. Darüberhinaus erstellten wir weitere Tabellen, um genauere Details, wie beispielsweise den Mutationswert verständlicher zu erklären.
Ein Aspekt, an dem wir noch ausgiebig arbeiteten war die Erklärung, wie die zufällige Bewegung der Wesen zustandekommt.

## Blogeintrag-21.11.22

In dieser Doppelstunde haben wir die Erklärung der zufälligen Bewegungen vervollständigt. Daraufhin, da nun der gesamte Quelltext doumentiert ist, haben wir noch die letzte Funktion erklärt. Die *Main()*-Funktion. In dieser werden die gesamten Variablen, die als Parameter genutzt werden, initialisiert und letztendlich die Simulation gestartet. 
Darüberhinaus würden noch weitere Grafiken und Quelltextausschnitte behilflich sein, um dem Leser das Ganze noch verständlicher darzulegen.

## Blogeintrag-12.12.22 

Heute haben wir uns damit beschäftigt Phython auf dem PC von Herr Buhl zu installieren. Dies war eine Vorraussetzung, um Herr Buhl unser Programm vorstellen zu können. Darüberhinaus haben wir noch zusätzlich einige Modulle für Phython installiert, um unsere Anwendung auf diesem PC ausführen zu können. Wie bereits auch schon die Wochen zuvor, haben wir das Design unserer Projektseite noch weiter optimiert und einige Dinge verbssert bzw. überarbeitet. Wie es sich herausgestellt hatte, waren einige Kommentare, die wir zuvor überarbeitet hatten, nicht gespeichert worden, sodass wir diesen Prozess nochmal wiederholen mussten. 

## Blogeintrag-15.12.22

Nun sind wir am letzten Tag unseres Informatikprojekts angelangt. Jetzt galt es vor der eigentlichen Abgabe am morgigen Tag nocheinmal alles zu revidieren, um mögliche Fehler zu entdecken und auszubessern. Dabei haben wir noch einiges sowohl bei der Orthographie als auch Interpunktion verbessert. Als krönenden Abschluss haben wir gemeinsam eine Art Animation mit "Adobe After Effect noch zusätlichfür unsere Projektseite erstellt, welche als eine Art Symbol dienen soll. Die Animation haben wir zum Schluss an Beginn unserer Projektseite gepackt, weil wir davon überzeugt sind, dass diese Animation durch ihre besonderen Eigenschaften, die Aufmerksamkeit des Empfängers weckt.

## Quellen zum ehemaligen Projekt "VocabNow" 

- [Zum ferngesteuerten Arbeiten](https://replit.com/)
- [Zur Erstellung der Vokabeldatenbank](https://www.mysql.com/)
- [Zum Erstellen der Überschrift der Blogeinträge](https://leviarista.github.io/github-profile-header-generator/)
- https://developer.mozilla.org/en-US/?retiredLocale=dehttps://de.wikipedia.org/wiki/Hypertext_Markup_Language
- [Die Spracherkunng von VocabNow](https://developer.mozilla.org/en-US/docs/Web/API/SpeechRecognition)
- https://de.wikipedia.org/wiki/Cascading_Style_Sheets
- https://de.wikipedia.org/wiki/Hypertext_Markup_Language
- [Das Design von VocabNow](https://particles.js.org/)
- [Alternative Datenbank zu MySQL](https://www.json.org/json-de.html)


