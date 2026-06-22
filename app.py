from flask import Flask, render_template, request
import csv

app = Flask(__name__)


# ---------------- HOME ----------------

@app.route("/")
def home():

    return render_template("index.html")


# ---------------- CUSTOMER ----------------

@app.route("/customer")
def customer():

    return render_template("customer.html")


@app.route("/save_customer", methods=["POST"])
def save_customer():

    customer_id = request.form["customer_id"]

    customer_name = request.form["customer_name"]

    email = request.form["email"]

    phone = request.form["phone"]

    policy_number = request.form["policy_number"]

    with open("data/customers.csv", "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            customer_id,
            customer_name,
            email,
            phone,
            policy_number
        ])

    return render_template("index.html")


# ---------------- POLICY ----------------

@app.route("/policy")
def policy():

    return render_template("policy.html")


@app.route("/save_policy", methods=["POST"])
def save_policy():

    policy_id = request.form["policy_id"]

    customer_id = request.form["customer_id"]

    insurance_type = request.form["insurance_type"]

    premium_amount = request.form["premium_amount"]

    with open("data/policies.csv", "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            policy_id,
            customer_id,
            insurance_type,
            premium_amount
        ])

    return render_template("index.html")


# ---------------- CLAIM ----------------

@app.route("/claim")
def claim():

    return render_template("claim.html")


@app.route("/save_claim", methods=["POST"])
def save_claim():

    claim_id = request.form["claim_id"]

    policy_id = request.form["policy_id"]

    claim_amount = int(request.form["claim_amount"])

    reason = request.form["reason"]

    if claim_amount <= 50000:

        status = "Approved"

    else:

        status = "Under Review"

    with open("data/claims.csv", "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            claim_id,
            policy_id,
            claim_amount,
            reason,
            status
        ])

    return render_template("index.html")


# ---------------- DASHBOARD ----------------

@app.route("/dashboard")
def dashboard():

    total_customers = 0

    total_policies = 0

    total_claims = 0

    approved_claims = 0

    under_review_claims = 0

    try:

        with open("data/customers.csv", "r") as file:

            total_customers = sum(1 for row in file)

    except:

        pass

    try:

        with open("data/policies.csv", "r") as file:

            total_policies = sum(1 for row in file)

    except:

        pass

    try:

        with open("data/claims.csv", "r") as file:

            reader = csv.reader(file)

            for row in reader:

                total_claims += 1

                if len(row) >= 5:

                    if row[4] == "Approved":

                        approved_claims += 1

                    elif row[4] == "Under Review":

                        under_review_claims += 1

    except:

        pass

    return render_template(
        "dashboard.html",

        total_customers=total_customers,

        total_policies=total_policies,

        total_claims=total_claims,

        approved_claims=approved_claims,

        under_review_claims=under_review_claims
    )


# ---------------- SEARCH ----------------

@app.route("/search")
def search():

    return render_template(
        "search.html",

        customer=None
    )


@app.route("/search_customer", methods=["POST"])
def search_customer():

    customer_id = request.form["customer_id"]

    customer = None

    try:

        with open("data/customers.csv", "r") as file:

            reader = csv.reader(file)

            for row in reader:

                if row[0] == customer_id:

                    customer = row

                    break

    except:

        pass

    return render_template(
        "search.html",

        customer=customer
    )


# ---------------- DELETE ----------------

@app.route("/delete")
def delete():

    return render_template("delete.html")


@app.route("/delete_customer", methods=["POST"])
def delete_customer():

    customer_id = request.form["customer_id"]

    updated_rows = []

    try:

        with open("data/customers.csv", "r") as file:

            reader = csv.reader(file)

            for row in reader:

                if row[0] != customer_id:

                    updated_rows.append(row)

        with open("data/customers.csv", "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerows(updated_rows)

    except:

        pass

    return render_template("index.html")


# ---------------- EDIT ----------------

@app.route("/edit")
def edit():

    return render_template("edit.html")


@app.route("/edit_customer", methods=["POST"])
def edit_customer():

    customer_id = request.form["customer_id"]

    customer_name = request.form["customer_name"]

    email = request.form["email"]

    phone = request.form["phone"]

    policy_number = request.form["policy_number"]

    updated_rows = []

    try:

        with open("data/customers.csv", "r") as file:

            reader = csv.reader(file)

            for row in reader:

                if row[0] == customer_id:

                    updated_rows.append([
                        customer_id,
                        customer_name,
                        email,
                        phone,
                        policy_number
                    ])

                else:

                    updated_rows.append(row)

        with open("data/customers.csv", "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerows(updated_rows)

    except:

        pass

    return render_template("index.html")


if __name__ == "__main__":

    app.run(debug=True)