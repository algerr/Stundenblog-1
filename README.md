# VocabNow
Computer Science project 2022

## Blogeintrag-15.08.2022

Heute fand die erste Informatikstunde statt, in der wir uns mit der Frage beschäftigt haben, was im Informatikunterricht behandelt werden wird. Dabei wurde klar erläutert, dass der Informatikunterricht an der Stormarnschule sehr individuell und projektorientiert stattfindet und somit kein Frontalunterricht entsteht. Die Projektideen, werden sich in 2er Gruppen überlegt und daraufhin bis zu einer Deadline im Dezember erarbeitet und dokumentierte durch Blogeinträge in jeder Stunde, wie diesem hier für den 15. August. Was die Projekte angeht, ist die Entscheidung jeder Gruppe selbst überlassen. Von visuellen Blocksprachen über Websprachen wie Javascript bis zu C/++ ist alles möglich. Auch Hardware kann mit Hilfe von Arduinos sowie Zubehör und Bibliotheken programmiert werden. Aufgrund der großen Vielzahl an Möglichkeiten, kamen wir in der ersten Stunde noch nicht auf unsere Idee. Eine grundlegende Vorstellung hatten wir jedoch: Unsere Idee sollte softwarebasiert sein.

## Blogeintrag-22.08.2022

Um eine Sprache zu erlernen sind sie einfach notwendig und spätestens seit der weiterführenden Schule sind sie aus dem Leben eines jeden von uns nicht mehr wegzudenken. **Vokabeln**. Doch ein Problem, das leider bisher keine Lösung hatte, stand dem "leichten Lernen nebenbei" schon immer im Weg. Um Vokabeln zu lernen muss entweder analog oder digital nachgeschlagen und mit voller Konzentration auf das jeweilige Medium geschaut werden, damit das Erlernen erfolgreich ist. Doch sich diese Zeit zu nehmen, ist für viele Menschen heutzutage gar nicht möglich, da noch so viele andere Dinge zu erledigen sind. Deshalb ist unsere Idee, einen Vokabeltrainer zu entwickeln, durch den man ganz nebenbei mit Spracherkennung Vokabeln lernen kann **VocabNow**. Man nimmt seine Kopfhörer und schon kann man, während z.B. die Hausarbeit erledigt wird, seinen Wortschatz erweitern und man muss sich keine Zeit nehmen, um auf altmodische Art und Weise Vokabeln zu lernen. Als Entwicklungsumgebung (IDE) verwenden wir [Replit.com](https://www.replit.com), da diese uns eine ferngesteuerte Arbeit ermöglicht, sodass bei Krankheit und nach dem Unterricht am Projekt weitergearbeitet werden kann. Der Name **VocabNow** rührt daher, dass unser Vokabeltrainer ein Lernen auf Knopfdruck ermöglichen soll. In jeder Situation und Lage soll es möglich sein, seinen Wortschatz zu erweitern, ohne sich auf sein Handy zu konzentrieren. Stand 22. August 2022 gibt es keinen anderen Vokabeltrainer, der diese Möglichkeit bietet. Für die Spracherkennung wird „WebKitSpeechRecognition“ aus der Webspeech API, bereitgestellt durch das Mozilla Developer Network, genutzt. Darüberhinaus haben wir für den Anfang eine Datenbank mit 10 englischen Vokabeln erstellt, welche als Probelauf dienen soll, um zu zeigen, ob das Ganze funktioniert. Für die [MySQL-Datenbank](https://www.mysql.com/) wird  [RemoteMySQL](https://remotemysql.com/) genutzt, was uns das Erstellen und Verwalten online möglich macht. Zu Beginn bestand das Problem, mehrere Datensätze für dieselbe Vokabel zu haben. Nach kurzer Zeit fanden wir jedoch heraus, wie sich ein Datensatz löschen lässt. Die nächste Herausforderung war jedoch nun die zufällige Ausgabe einer Vokabel, da das Vokabellernen in der immer gleichen Reihenfolge auf Dauer keinen Sinn ergibt. Leider funktionierte das Ganze bis zum Ende der Stunde nicht wirklich, sodass wir uns der Lösung dieses Problems in der nächsten Stunde widmen werden.

## Blogeintrag-25.08.2022

Da uns das Problem der letzten Stunde mit der zufälligen Ausgabe von Vokabeln auch danach noch beschäftigte, arbeiteten wir zu Hause daran weiter und fanden bald eine Lösung. Dafür wurde in der Datenbank im Table *Eng_De* ein Wert **Vocab** eingegeben, der von nun an alle Vokabeln von Englisch zu Deutsch im Format **Englisch_Deutsch** beinhaltet. Damit ist nun die zufällige Ausgabe von Vokabeln leicht und der ausgegebene Wert muss nur im Unterstrich getrennt werden, sodass die englische und deutsche Vokabel einzeln verwendet werden können. Da Laurenz leider krankheitsbedingt abwesend war und Daniel über keine weitreichenden Programmierkenntnisse verfügte, widmete er sich der Erstellung der Webseite, über die VocabNow später laufen soll. Er erlernte in den beiden Doppelstunden die Grundlagen der Auszeichnungssprache **HTML (Hyper-Text-Markup-Language)**. Außerdem überlegte er sich, was man noch in die App einbauen könne. So entstand die Idee, dem Nutzer die Bedienung der Seite erheblich zu erleichtern, sodass, wie im vorigen Blogeintrag bereits beschrieben, ein Vokabellernen auf Knopfdruck möglich ist. Doch durch die Möglichkeit, am Projekt auch ferngesteuert zu arbeiten, konnte auch Laurenz seinen Teil leisten, indem er am Backend, der Entwicklung des Systems hinter der Webseite, weiterarbeitete.

## Blogeintrag-29.08.2022

Da Laurenz leider aufgrund von Krankheit nicht anwesend sein konnte, fokussierte sich Daniel heute auf das Erlernen der Programmiersprache Javascript, die bei einer Webseite für Funktionalität sorgt. Des Weiteren fing er an, die bisherigen Blogeinträge im Repository auf GitHub hochzuladen. Somit kann Laurenz die Blogeinträge später noch überarbeiten, sodass sie alle beisammen auf dem neusten Stand sind.
