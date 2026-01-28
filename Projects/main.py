import csv
import os
from datetime import datetime

# ================= GLOBAL =================
USER_FILE = "users.txt"
current_user = None
income_added = False

# ================= USER FILES =================
def data_file():
    return f"data_{current_user}.csv"

def saving_file():
    return f"saving_{current_user}.txt"

# ================= INITIALIZATION =================
def init_user_files():
    if not os.path.exists(data_file()):
        with open(data_file(), 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Type", "Category", "Amount", "Description"])

    if not os.path.exists(saving_file()):
        with open(saving_file(), 'w') as f:
            f.write("0")

# ================= LOGIN SYSTEM =================
def signup():
    print("\n--- SIGN UP ---")
    u = input("Create username: ")
    p = input("Create password: ")

    if not os.path.exists(USER_FILE):
        open(USER_FILE, 'w').close()

    with open(USER_FILE) as f:
        for line in f:
            if line.split(",")[0] == u:
                print("❌ Username already exists")
                return False

    with open(USER_FILE, 'a') as f:
        f.write(f"{u},{p}\n")

    print("✅ Signup successful")
    return True

def login():
    global current_user, income_added
    print("\n--- LOGIN ---")
    u = input("Username: ")
    p = input("Password: ")

    if not os.path.exists(USER_FILE):
        print("❌ No users found. Signup first.")
        return False

    with open(USER_FILE) as f:
        for line in f:
            user, pwd = line.strip().split(",")
            if u == user and p == pwd:
                current_user = u
                income_added = False
                init_user_files()
                print(f"✅ Welcome {u}")
                return True

    print("❌ Invalid login")
    return False

def login_menu():
    while True:
        print("\n===== LOGIN SYSTEM =====")
        print("1. Login")
        print("2. Sign Up")
        print("3. Exit")

        ch = input("Choose (1-3): ")
        if ch == "1":
            if login():
                return
        elif ch == "2":
            signup()
        elif ch == "3":
            exit()
        else:
            print("❌ Invalid choice")

# ================= CATEGORY AI =================
def detect_category(desc):
    d = desc.lower()
    if "food" in d or "pizza" in d:
        return "Food"
    elif "rent" in d:
        return "Rent"
    elif "bus" in d or "uber" in d:
        return "Transport"
    elif "bill" in d:
        return "Bills"
    elif "shopping" in d:
        return "Shopping"
    elif "fee" in d or "tuition" in d or "exam" in d:
        return "Academic Fees"
    else:
        return "Other"

# ================= ADD INCOME =================
def add_income():
    global income_added
    try:
        amt = float(input("Enter income amount: "))
        src = input("Enter income source: ")
        date = datetime.now().strftime("%Y-%m-%d")

        with open(data_file(), 'a', newline='') as f:
            csv.writer(f).writerow([date, "Income", src, amt, src])

        income_added = True
        print("✅ Income added")
    except:
        print("❌ Invalid input")

# ================= READ DATA =================
def read_data():
    income = expense = 0
    income_src = {}
    expense_cat = {}

    with open(data_file()) as f:
        reader = csv.DictReader(f)
        for r in reader:
            amt = float(r["Amount"])
            if r["Type"] == "Income":
                income += amt
                income_src[r["Category"]] = income_src.get(r["Category"], 0) + amt
            else:
                expense += amt
                expense_cat[r["Category"]] = expense_cat.get(r["Category"], 0) + amt

    return income, expense, income_src, expense_cat

# ================= ADD EXPENSE + SAVING ALERT =================
def add_expense():
    if not income_added:
        print("❌ Add income first")
        return

    try:
        amt = float(input("Enter expense amount: "))
        desc = input("Enter expense description: ")
        cat = detect_category(desc)
        date = datetime.now().strftime("%Y-%m-%d")

        with open(data_file(), 'a', newline='') as f:
            csv.writer(f).writerow([date, "Expense", cat, amt, desc])

        print(f"✅ Expense added ({cat})")

        income, expense, _, _ = read_data()
        target = float(open(saving_file()).read())
        if target > 0 and (income - expense) < target:
            print("⚠ SAVING ALERT: You are using your savings!")

    except:
        print("❌ Invalid input")

# ================= RESET =================
def reset_income():
    global income_added
    rows = []
    with open(data_file()) as f:
        for r in csv.DictReader(f):
            if r["Type"] != "Income":
                rows.append(r)

    with open(data_file(), 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=["Date","Type","Category","Amount","Description"])
        w.writeheader()
        w.writerows(rows)

    income_added = False
    print("🔄 Income reset")

def reset_expenses():
    rows = []
    with open(data_file()) as f:
        for r in csv.DictReader(f):
            if r["Type"] != "Expense":
                rows.append(r)

    with open(data_file(), 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=["Date","Type","Category","Amount","Description"])
        w.writeheader()
        w.writerows(rows)

    print("🔄 Expenses reset")

# ================= ANALYSIS =================
def summary():
    i, e, _, _ = read_data()
    print("\nIncome:", i, "\nExpense:", e, "\nBalance:", i - e)

def income_analysis():
    _, _, s, _ = read_data()
    print("\nIncome Sources:")
    for k, v in s.items():
        print(k, ":", v)

def expense_analysis():
    _, _, _, c = read_data()
    print("\nExpense Categories:")
    for k, v in c.items():
        print(k, ":", v)

def set_saving_target():
    try:
        t = float(input("Enter saving target: "))
        open(saving_file(), 'w').write(str(t))
        print("🎯 Saving target set")
    except:
        print("❌ Invalid input")

# ================= MAIN MENU =================
def main_menu():
    while True:
        print(f"\n===== FINANCE TRACKER ({current_user}) =====")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Summary")
        print("4. Income Analysis")
        print("5. Expense Analysis")
        print("6. Set Saving Target")
        print("7. Reset Income")
        print("8. Reset Expenses")
        print("9. Logout")

        ch = input("Choose (1-9): ")

        if ch == "1": add_income()
        elif ch == "2": add_expense()
        elif ch == "3": summary()
        elif ch == "4": income_analysis()
        elif ch == "5": expense_analysis()
        elif ch == "6": set_saving_target()
        elif ch == "7": reset_income()
        elif ch == "8": reset_expenses()
        elif ch == "9":
            print("🔒 Logged out")
            break
        else:
            print("❌ Invalid choice")

# ================= RUN =================
while True:
    login_menu()
    main_menu()
