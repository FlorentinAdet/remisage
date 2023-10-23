# Liste pour stocker les tâches
tasks = []

# Boucle principale
while True:
    print("\nMenu:")
    print("1. Ajouter une tâche")
    print("2. Afficher les tâches")
    print("3. Marquer une tâche comme terminée")
    print("4. Supprimer une tâche")
    print("5. Quitter")

    choice = input("Choisissez une option : ")

    if choice == '1':
        task_description = input("Entrez la description de la tâche : ")
        print("fonction add")
    elif choice == '2':
        print("fonction list task")
    elif choice == '3':
        print("fonction task done")
    elif choice == '4':
        print("fonction task supprimer")
    elif choice == '5':
        break
    else:
        print("Option invalide. Veuillez réessayer.")

print("Application de gestion de tâches terminée.")
