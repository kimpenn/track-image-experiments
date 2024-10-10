# globals used as choices
PROBE_TYPES = (
    ("H&E", "H&E"),
    ("DAPI", "DAPI"),
    ("Antibody", "Antibody"),
    ("smFISH", "smFISH"),
)

FISH_TECHNOLOGIES = (
    ("smHCR", "smHCR"),
    ("HCR", "HCR"),
    ("Sellaris", "Sellaris"),
    ("inHouse", "inHouse"),
    ("hiFISH", "hiFISH"),
    ("Oligopaint", "Oligopaint"),
    ("n/a", "Not Applicable"),
)

FLOURESCENT_MOLECULES = (
    ("DAPI", "DAPI"),
    ("GFP", "GFP"),
    ("Alexa Flour 488", "Alexa Flour 488"),
    ("FITC", "FITC"),
    ("Cy3", "Cy3"),
    ("Atto 550", "Atto 550"),
    ("Cy5", "Cy5"),
    ("mCherry", "mCherry"),
    ("Cy5.5", "Cy5.5"),
    ("Alexa Flour 647", "Alexa Flour 647"),
    ("Alexa Flour 750", "Alexa Flour 750"),
    ("Brightfield", "Brightfield"),
    ("DIC", "DIC"),
)

PANEL_IDS = (
    ("H&E", "H&E"),
    ("DAPI", "DAPI"),
    ("Test_Panel", "Test_Panel"),
    ("Jean's FISH panel", "Jean's FISH panel"),
    ("Uterus OSP", "Uterus OSP"),
    ("Fallopian OSP", "Fallopian OSP"),
)

IMAGING_SUCCESS_OPTIONS = (
    ("Yes", "Yes"),
    ("No", "No"),
    ("Adjust working dilution", "Adjust working dilution"),
    ("Overexposed", "Overexposed"),
    ("Underexposed", "Underexposed"),
)
