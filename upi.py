bills = {
    "cust1" : 250,
    "cust2" : 340,
    "cust3" : 600
}

def payment(id):
    if id in bills:
        return f"The bill of cust1: {bills[id]}"
    else:
        return "Invalid customer id"
    

if __name__ == "__main__":
    payment("cust1")
    payment("cust2")
    payment("cust3")
    payment("cust")