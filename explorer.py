import requests

BASE_URL = "https://api.fda.gov/drug/event.json"

fifty_results_url = f'{BASE_URL}?search=patient.drug.activesubstance.activesubstancename:"Metoprolol"+AND+patient.reaction.reactionmeddrapt:"bradycardia"+AND+patient.drug.drugindication="arrythmia"&limit=50'
print(fifty_results_url)

fifty_results_rq = requests.get(fifty_results_url)
fifty_results = fifty_results_rq.json()


count_of_results = fifty_results["meta"]["results"]["total"]

for result in fifty_results:
    for drug in result.get("patient").get("drug"):
        print(drug.get("activesubstance", {}).get("activesubstancename"))
    for reaction in result.get("patient", {}).get("reaction"):
        print(reaction.get("reactionmeddrapt"))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
