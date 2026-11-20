import re
from app import app, failed

def csrf(c):
    html = c.get("/login").get_data(as_text=True)
    return re.search(r'name="csrf" value="(\w+)"', html).group(1)

def run():
    c = app.test_client()
    assert c.get("/dashboard").status_code == 302            # protected
    r = c.post("/login", data={"csrf": "bad", "username": "student", "password": "x"})
    assert r.status_code == 400                               # CSRF enforced
    r = c.post("/login", data={"csrf": csrf(c), "username": "student", "password": "wrong"})
    assert r.status_code == 401                               # bad password
    r = c.post("/login", data={"csrf": csrf(c), "username": "nobody", "password": "x"})
    assert r.status_code == 401 and b"Incorrect username or password" in r.data
    r = c.post("/login", data={"csrf": csrf(c), "username": "student", "password": "Lab@2026!"})
    assert r.status_code == 302                               # success
    assert b"Welcome, student" in c.get("/dashboard").data
    c.post("/logout")
    assert c.get("/dashboard").status_code == 302             # logged out
    failed.clear()
    c2 = app.test_client()
    for _ in range(5):
        c2.post("/login", data={"csrf": csrf(c2), "username": "student", "password": "no"})
    r = c2.post("/login", data={"csrf": csrf(c2), "username": "student", "password": "Lab@2026!"})
    assert r.status_code == 429                               # lockout
    print("All tests passed")

run()
