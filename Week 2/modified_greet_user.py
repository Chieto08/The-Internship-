def greet_alice_and_bob(username):
    if username == "Alice" or username == "Bob":
        return "Good day " + username + "."

print(greet_alice_and_bob("Alice"))
