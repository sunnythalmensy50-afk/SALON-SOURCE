class Salon:
    def __init__(self, nom, membres=[]):
        self.nom = nom
        self.membres = membres  # Liste d'utilisateurs
        self.historique_fulgurances = []

    def get_poids_représentatif(self):
        # La force du vote dépend de la taille du salon
        n = len(self.membres)
        return 0.5 if n < 5 else 1.0 if n < 20 else 1.5

    def processus_admission(self, candidat, question):
        print(f"\n--- Admission au Salon {self.nom} ---")
        # 3 tours pour valider l'équilibre (Science, Art, Santé, Politique, IDH)
        for tour in range(1, 4):
            print(f"Tour {tour} : Vote facultatif des membres...")
            
            # Ici, la logique du vote constructif (5 critères)
            resultat_vote = self.simuler_vote_constructif(question)
            
            if resultat_vote["equilibre"] > 0.8:
                self.membres.append(candidat)
                return "ADMIS : Votre pensée équilibre le salon."
            
            if tour == 3:
                return "REFUSÉ : L'équilibre n'est pas atteint."
        return "REFUSÉ."
def simuler_vote_constructif(self, question):
        # Analyse de la répartition sur les 5 piliers
        # Le résultat fait avancer la problématique du salon
        return {"equilibre": 0.85, "feedback": "Renforce le pôle Santé/Éthique"}
