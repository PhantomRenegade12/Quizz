print("Bienvenue dans mon quizz sur la cybersécurité !")

playing = input("Est-ce que vous voulez jouer ? ")

if playing.lower() != "oui":
    quit()

print("Ok : le jeu démarre :)")
score = 0

answer = input("Est-ce qu’un cybercriminel peut utiliser des informations trouvées sur vos réseaux sociaux pour deviner vos mots de passe ? ")
if answer.lower() == "oui":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Est-il sûr d'utiliser le même mot de passe pour tous vos comptes ? ")
if answer.lower() == "non":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Faut-il cliquer sur des liens dans des e-mails provenant d’expéditeurs inconnus ? ")
if answer.lower() == "non":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Est-il important de mettre à jour régulièrement vos appareils et logiciels ? ")
if answer.lower() == "oui":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Peut-on partager son mot de passe avec un ami en qui on a confiance ? ")
if answer.lower() == "non":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Peut-on brancher une clé USB trouvée par terre sans risque ? ")
if answer.lower() == "non":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Peut-on partager des informations personnelles sur les réseaux sociaux en toute sécurité ? ")
if answer.lower() == "non":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Est-ce que les cybercriminels peuvent cibler aussi bien les enfants que les adultes ? ")
if answer.lower() == "oui":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Est-il nécessaire d’utiliser une double authentification (2FA) si possible ? ")
if answer.lower() == "oui":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Est-il utile risquer d'utilisé une connexion Wi-Fi publique pour des achats en ligne ? ")
if answer.lower() == "oui":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 10) * 100) + "%.")
