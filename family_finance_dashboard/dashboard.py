import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "data.json"

def load_data():
    if DATA_FILE.exists():
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {"members": []}

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def input_member():
    name = input("Member name: ")
    income = float(input("Annual income: "))
    assets = float(input("Total assets: "))
    debt = float(input("Total debt: "))
    interest_rate = float(input("Average debt interest rate (%): "))
    return {
        "name": name,
        "income": income,
        "assets": assets,
        "debt": debt,
        "interest_rate": interest_rate
    }

def summarize(data):
    for m in data["members"]:
        net_worth = m["assets"] - m["debt"]
        print(f"{m['name']} - Net worth: ${net_worth:,.2f} | Income: ${m['income']:,.2f}")


def main():
    data = load_data()
    while True:
        choice = input("Add member (a), summary (s), quit (q): ").lower().strip()
        if choice == 'a':
            member = input_member()
            data["members"].append(member)
            save_data(data)
        elif choice == 's':
            summarize(data)
        elif choice == 'q':
            break
        else:
            print("Unknown option")

if __name__ == "__main__":
    main()
