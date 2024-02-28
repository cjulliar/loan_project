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

state_list = [[state_names[i], state_abreviations[i]] for i in len(state_names)]

# Entreprise avec moins de deux ans d'existence
new_exist_list = [
    ["Oui", "New"],
    ["Non", "Existing"],
    ["Non défini", "0"],
]

urban_rural_list = [
    ["Milieu urbain", "Urban"],
    ["Milieu rural", "Rural"],
    ["Non défini", "Other"],
]

# Ligne de crédit renouvelable
rev_line_list = [
    ["Oui", "Y"],
    ["Non", "N"],
    ["Non défini", "0"]
]

# Application en une page correspond à oui
low_doc_list = [
    ["Oui", "Y"],
    ["Non", "N"],
    ["Non défini", "0"]
]

real_estate_list = [
    ["Oui", "Y"],
    ["Non", "N"],
]

mis_status = [
    ["Incapacité de rembourser", 0],
    ["Capable de rembourser", 1]
]