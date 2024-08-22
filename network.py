import instaloader

def priv_error(p):
    if (p.is_private):
        print(f"critical error: profile {p.username} is private - followers can't be accessed.")
        exit()

print("network finder - find common nodes between two targets")
print("loading instaloader...")
L = instaloader.Instaloader()

print("logging in...")
L.login(input("username: "), input("password: "))

target1 = input("target 1 usename: " )
print(f"creating profile {target1}...")
p1 = instaloader.Profile.from_username(L.context, target1)

target2 = input("target 2 usename: " )
print(f"creating profile {target2}...")
p2 = instaloader.Profile.from_username(L.context, target2)

priv_error(p1)
priv_error(p2)
    
print("getting followers from 1...")
f1 = set(p1.get_followers())

print("getting followers from 2...")
f2 = set(p2.get_followers())

print("comparing followers...")
common = set(f1) & set(f2)
common_list = list(common)

for user in common_list:
    print(f"username: {user.username}")

    
