import uuid

# Mock data for products
products = [
    {
        "name": "FungaShield",
        "description": "Broad-spectrum fungicide for various crops",
        "tags": ["fungicide", "broad-spectrum", "protective"],
    },
    {
        "name": "InsectAway",
        "description": "Powerful insecticide for controlling a wide range of pests",
        "tags": ["insecticide", "pest control", "crop protection"],
    },
    {
        "name": "HerbClear",
        "description": "Selective herbicide for weed control in cereals",
        "tags": ["herbicide", "weed control", "cereals"],
    },
    {
        "name": "GrowBoost",
        "description": "Plant growth regulator for enhancing crop yield",
        "tags": ["growth regulator", "yield enhancement", "crop management"],
    },
    {
        "name": "SoilEnrich",
        "description": "Soil amendment to improve nutrient availability",
        "tags": ["soil amendment", "nutrient management", "fertility"],
    },
    {
        "name": "BioDefend",
        "description": "Organic pesticide derived from natural sources",
        "tags": ["organic", "biopesticide", "eco-friendly"],
    },
    {
        "name": "RootGuard",
        "description": "Systemic fungicide for root disease prevention",
        "tags": ["fungicide", "systemic", "root protection"],
    },
    {
        "name": "LeafShine",
        "description": "Foliar fertilizer for rapid nutrient absorption",
        "tags": ["fertilizer", "foliar", "nutrient boost"],
    },
    {
        "name": "MiteStop",
        "description": "Acaricide for controlling mites in fruit crops",
        "tags": ["acaricide", "mite control", "fruit crops"],
    },
    {
        "name": "SeedShield",
        "description": "Seed treatment for protection against soil-borne pathogens",
        "tags": ["seed treatment", "pathogen control", "crop establishment"],
    },
]


# Add a unique ID to each product
for product in products:
    product["id"] = str(uuid.uuid4())


def get_all_products():
    return products
