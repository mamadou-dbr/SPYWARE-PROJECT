PROJET FINAL - SPYWARE
 Vous devez réaliser un spyware (logiciel espion) exclusivement en Python 3. Il est composé de deux élements : un client et un
 serveur. Il doit répondre aux exigences suivantes.
 Le projet est à réaliser seul ou par groupe de 2 MAXIMUM !
 Le rendu du projet est le 31 janvier 2024 à 23h59.
 # Exigences techniques client
 Le programme doit être opérationnel sur les systèmes Windows et Linux.
 Le programme doit être utilisable en tant que programma exécutable 
.exe
 sous Windows.
 Il doit embarquer les fonctionnalités suivantes :
 Enregistrer les frappes de clavier dans un fichier caché sur le système de la victime.
 Envoyer le fichier de façon sécurisé au serveur via une socket réseau.
 S'arrêter si il reçoit l'ordre du serveur et supprimer le fichier de capture.
 S'arrêter automatiquement au bout de maximum 10 minutes de capture si le serveur est injoignable.
 # Exigences techniques serveur
 Il doit réceptionner les données du client via une socket sécurisée.
 Il écoute sur un port TCP depuis une machine externe et différente de la victime.
 Il réceptionne les données reçus et les enregistre dans un fichier unique pour chaque victime (format 
<date/heure>-keyboard.txt 
).
 <ip-victime>
Il doit envoyer un message au spyware via la socket lui demandant de s'arrêter lorsque le serveur s'éteint. Pour ce faire,
 vous devez récupérer les signaux envoyés au serveur (ex : ctrl+c sur le processus).
 Il doit embarquer les arguments suivants :-h/--help
 : affiche l'aide et les différentes options.-l/--listen <port>
 : se met en écoute sur le port TCP saisi par l'utilisateur et attend les données du spyware.-s/--show
 : affiche la liste des fichiers réceptionnées par le programme.-r/--readfile <nom_fichier>
 : affiche le contenu du fichier stocké sur le serveur du spyware. Le contenu doit
 être parfaitement lisible.-k/--kill
 : arrête toute les instances de serveurs en cours, avertit le spyware de s'arrêter et de supprimer la
 capture.
 # Fonctionnalités supplémentaires
 Permettre d'accepter plusieurs spywares en parallèle.
 Implémenter des fonctionnalités supplémentaires pour le spyware.
 Implémenter des fonctionnalités de contournement d'antivirus.
 1 / 2
projet-final.md
 18/10/2023
 # Notation
 Qualité du code (fonctions, classes, organisation, etc)
 Fonctionnement du code
 Respect du cahier des charges
 Commentaires au sein du code
 # Règles
 Votre code est analysé dynamiquement par un programme automatique. Il permet de détecter le partage et l'apparition de code
 généré par une IA. Toute tentative de triche amenera à une note de 01/20 pour l'ensemble du ou des groupes
