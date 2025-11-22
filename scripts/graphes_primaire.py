import matplotlib.pyplot as plt
import numpy as np

# Configuration
plt.style.use('seaborn-v0_8')
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Données
années = ['2003-2004', '2009-2010', '2015-2016', '2019-2020', '2023-2024']
public = [41181, 52991, 55674, 56631, 61320]
privé_fr = [2853, 2554, 3893, 5442, 7240]
privé_ar = [4679, 4163, 2188, 3779, 2747]

# Graphique 1: Effectifs par secteur
bar_width = 0.25
x = np.arange(len(années))
ax1.bar(x - bar_width, public, width=bar_width, label='Public', color='#1f77b4', alpha=0.8)
ax1.bar(x, privé_fr, width=bar_width, label='Privé Francophone', color='#ff7f0e', alpha=0.8)
ax1.bar(x + bar_width, privé_ar, width=bar_width, label='Privé Arabophone', color='#2ca02c', alpha=0.8)

ax1.set_title('PRIMAIRE: Effectifs par secteur éducatif', fontweight='bold', fontsize=14)
ax1.set_xlabel('Année scolaire', fontweight='bold')
ax1.set_ylabel("Nombre d'élèves", fontweight='bold')
ax1.set_xticks(x)
ax1.set_xticklabels(années, rotation=45)
ax1.legend()
ax1.grid(True, alpha=0.3)

# Graphique 2: Taux de scolarisation
taux_admission = [50.7, 73.6, 72.2, 101.4, 109.0]
taux_scolarisation = [49.5, 72.9, 78.0, 94.0, 99.02]

ax2.plot(années, taux_admission, marker='o', linewidth=2.5, label='Taux Brut d\'Admission', color='#e377c2')
ax2.plot(années, taux_scolarisation, marker='s', linewidth=2.5, label='Taux Brut de Scolarisation', color='#17becf')

ax2.set_title('PRIMAIRE: Évolution des taux de scolarisation', fontweight='bold', fontsize=14)
ax2.set_xlabel('Année scolaire', fontweight='bold')
ax2.set_ylabel('Taux (%)', fontweight='bold')
ax2.legend()
ax2.grid(True, alpha=0.3)
ax2.set_ylim(0, 120)

plt.tight_layout()
plt.savefig('primaire_analysis.png', dpi=300, bbox_inches='tight')
plt.show()

print("✅ Graphiques primaire générés avec succès!")
print("📊 Insights:")
print("- Le public domine avec 61 320 élèves en 2023-2024")
print("- Le privé francophone a doublé depuis 2015")
print("- Les taux dépassent 100%, objectif de scolarisation universelle atteint")