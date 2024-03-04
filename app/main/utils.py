import json
import os
from requests import Request, Session

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

STATE_CHOICES = [(state_abreviations[i], state_names[i]) for i in range(len(state_names))]

# Entreprise avec moins de deux ans d'existence
NEW_EXIST_CHOICES = [
    ("New", "Oui"),
    ("Existing", "Non"),
    ("0", "Non défini"),
]

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

REAL_ESTATE_CHOICES = [
    ("Y", "Oui"),
    ("N", "Non")
]

MIS_STATUS_CHOICES = [
    ("0", "Incapacité de rembourser"),
    ("1", "Capable de rembourser")
]


def api_call(application):

    url = os.getenv("API_URL")

    headers = {
        "Accepts": "application/json",
    }

    session = Session()
    session.headers.update(headers)

    company = application["company"]

    features = [
        company["state"],
        application["bank"],
        application["bank_state"],
        application["term"],
        company["num_employees"],
        application["new_exist"],
        company["franchise_code"],
        company["urban_rural"],
        application["rev_line_cr"],
        application["low_doc"],
        application["gr_appv"],
        application["sba_appv"],
        company["zip"],
        company["naics"],
        application["real_estate"],
    ]

    features = json.dumps(features)
    response = session.post(url, data=features)
    result = json.loads(response.text)

    return result