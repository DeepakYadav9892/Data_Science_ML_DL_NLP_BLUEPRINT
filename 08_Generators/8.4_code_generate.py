def local_chai():
    yield "Masala chai "
    yield "Ginger chai"
    yield "Elaichi chai"

def imported_chai():
    yield from local_chai()
    yield from imported_chai()

for chai in full_menu():
    print(chai)

def chai_stall():
    try:
        while True:
            order=yield "Waiting fo chai order"
    except:
        print("Stall closed , No more chai ")

stall=chai_stall()
print(next(stall))
stall.close()