import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-v0_8')
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Données
années = ['2003-2004', '2015-2016', '2019-2020', '2023-2024']
public = [10, 35, 40, 53]
privé = [20, 22, 26, 40]
effectifs_public = [14781, 35949, 39694, 40112]
effectifs_privé = [3399, 3048, 5117, 7007]
redoublants = [1507, 3784, 3298, 2815]

# Graphique 1: Établissements
x = np.arange(len(années))
ax1.bar(x - 0.2, public, width=0.4, label='Public', color='#1f77b4', alpha=0.8)
ax1.bar(x + 0.2, privé, width=0.4, label='Privé', color='#ff7f0e', alpha=0.8)

ax1.set_title('MOYEN: Évolution des établissements', fontweight='bold', fontsize=14)
ax1.set_xlabel('Année scolaire', fontweight='bold')
ax1.set_ylabel("Nombre d'établissements", fontweight='bold')
ax1.set_xticks(x)
ax1.set_xticklabels(années)
ax1.legend()
ax1.grid(True, alpha=0.3)

# Graphique 2: Effectifs et redoublants
ax2.plot(années, effectifs_public, marker='o', linewidth=2.5, label='Effectifs Public', color='#1f77b4')
ax2.plot(années, effectifs_privé, marker='s', linewidth=2.5, label='Effectifs Privé', color='#ff7f0e')
ax2.bar(x, redoublants, alpha=0.6, label='Redoublants Publics', color='#d62728')

ax2.set_title('MOYEN: Effectifs et redoublants', fontweight='bold', fontsize=14)
ax2.set_xlabel('Année scolaire', fontweight='bold')
ax2.set_ylabel("Nombre d'élèves", fontweight='bold')
ax2.set_xticks(x)
ax2.set_xticklabels(années)
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('moyen_analysis.png', dpi=300, bbox_inches='tight')
plt.show()

print("✅ Graphiques moyen générés avec succès!")
print("📊 Insights:")
print("- Les établissements publics ont été multipliés par 5")
print("- Stagnation des effectifs publics depuis 2019")
print("- Baisse de 26% des redoublants depuis 2015")