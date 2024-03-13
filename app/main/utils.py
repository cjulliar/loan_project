state_names = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut",
    "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa",
    "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan",
    "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire",
    "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma",
    "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee",
    "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
]

state_abreviations = [
    "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID",
    "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS",
    "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK",
    "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"
]

# Listes des états US 
STATE_CHOICES = [(state_abreviations[i], state_names[i]) for i in range(len(state_names))]


NAICS_CHOICES = [
    ("11", "Agriculture, sylviculture, pêche et chasse"),
    ("21", "Mines, carrières et extraction de pétrole et de gaz"),
    ("22", "Services publics"),
    ("23", "Construction"),
    ("31", "Industrie manufacturière (code 31)"),
    ("32", "Industrie manufacturière (code 32)"),
    ("33", "Industrie manufacturière (code 33)"),
    ("42", "Commerce de gros"),
    ("44", "Commerce de détail (code 44)"),
    ("45", "Commerce de détail (code 45)"),
    ("48", "Transport et entreposage (code 48)"),
    ("49", "Transport et entreposage (code 49)"),
    ("51", "Information"),
    ("52", "Finance et assurance"),
    ("53", "Immobilier, location et crédit-bail"),
    ("54", "Services professionnels, scientifiques et techniques"),
    ("55", "Gestion de sociétés et d'entreprises"),
    ("56", "Services administratifs, de soutien, de gestion des déchets et d'assainissement"),
    ("61", "Services d'enseignement"),
    ("62", "Soins de santé et assistance sociale"),
    ("71", "Arts, spectacles et loisirs"),
    ("72", "Hébergement et restauration"),
    ("81", "Autres services (sauf administration publique)"),
    ("92", "Administration publique"),
]

# Entreprise avec moins de deux ans d'existence
NEW_EXIST_CHOICES = [
    ("New", "Oui"),
    ("Existing", "Non"),
    ("0", "Non défini"),
]

# Milieu urbain ou rural
URBAN_RURAL_CHOICES = [
    ("Urban", "Milieu urbain"),
    ("Rural", "Milieu rural"),
    ("0", "Non défini"),
]

# Ligne de crédit renouvelable
REV_LINE_CHOICES = [
    ("Y", "Oui"),
    ("N", "Non"),
    ("0", "Non défini")
]

# Application en une page correspond à oui
LOW_DOC_CHOICES = [
    ("Y", "Oui"),
    ("N", "Non"),
    ("0", "Non défini")
]

# Prêt associé à de l'immobilier
REAL_ESTATE_CHOICES = [
    ("Y", "Oui"),
    ("N", "Non")
]

# Prédiction du modèle
MIS_STATUS_CHOICES = [
    ("0", "Incapacité de rembourser"),
    ("1", "Capable de rembourser")
]