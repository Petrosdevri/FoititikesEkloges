import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

fig, ax = plt.subplots(figsize=(12, 10), subplot_kw={'projection': ccrs.PlateCarree()})

ax.add_feature(cfeature.BORDERS)
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)

ax.set_extent([19, 30 ,34, 42])

dapUnis = {
    "ΑΠΘ": (40.6308, 22.9592),
    "ΑΣΠΑΙΤΕ": (38.0433, 23.7860),
    "ΔΙΠΑΕ": (40.6569, 22.8038),
    "ΕΚΠΑ": (37.9691, 23.7796),
    "ΕΛΜΕΠΑ": (35.3192, 25.1024),
    "Παν. Αιγαίου": (39.0851, 26.5689),
    "Παν. Θεσσαλίας": (39.6269, 22.3810),
    "Παν. Μακεδονίας": (40.6250, 22.9600)
}

eaakUnis = {
    "Παν. Κρήτης": (35.3531, 24.4501),
    "Πολ. Κρήτης": (35.5292, 24.0687)
}

otherUnis = {
    "Χαροκόπειο": (37.9612, 23.7082)
}

paspUnis = {
    "ΟΠΑ": (37.9940, 23.7320),
    "Παν. Πατρών": (38.2892, 21.7853),
    "Παν. Πειραιώς": (37.9415, 23.6529)
}

pksUnis = {
    "ΑΣΚΤ": (37.9621, 23.6905),
    "Γεωπονικό": (37.9834, 23.7037),
    "ΔΠΘ": (41.1364, 25.3724),
    "ΕΜΠ": (37.9877, 23.7318),
    "Ιόνιο": (39.6231, 19.9149),
    "Παν. Δυτικής Αττικής": (38.0025, 23.6748),
    "Παν. Δυτικής Μακεδονίας": (40.3220, 21.7908),
    "Παν. Ιωαννίνων": (39.6216, 20.8599),
    "Παν. Πελοποννήσου": (37.5272, 22.3718),
    "Πάντειο": (37.9595, 23.7193),
}

for uni, (lat, lon) in dapUnis.items():
    ax.plot(lon, lat, 'o', color='#4123A1', markersize=2, transform=ccrs.PlateCarree(), label='ΔΑΠ' if uni == 'ΑΠΘ' else '')

for uni, (lat, lon) in eaakUnis.items():
    ax.plot(lon, lat, 'o', color='#6F4441', markersize=2, transform=ccrs.PlateCarree(), label='ΕΑΑΚ' if uni == 'Παν. Κρήτης' else '')

for uni, (lat, lon) in paspUnis.items():
    ax.plot(lon, lat, 'o', color='#21773b', markersize=2, transform=ccrs.PlateCarree(), label='ΠΑΣΠ' if uni == 'ΟΠΑ' else '') # 00D262 

for uni, (lat, lon) in pksUnis.items():
    ax.plot(lon, lat, 'o', color='#CF272A', markersize=2, transform=ccrs.PlateCarree(), label='ΠΚΣ' if uni == 'ΑΣΚΤ' else '')

for uni, (lat, lon) in otherUnis.items():
    ax.plot(lon, lat, 'o', color='#969696', markersize=2, transform=ccrs.PlateCarree(), label='Διάφορα' if uni == 'Χαροκόπειο' else '')


plt.title('Αποτελέσματα Φοιτητικών Εκλογών 2025', fontsize=15)
plt.legend(loc='upper right', title='Υπόμνημα')

plt.savefig('Αποτελέσματα Φοιτητικών Εκλογών 2025.png', dpi=300, bbox_inches='tight')
plt.show()