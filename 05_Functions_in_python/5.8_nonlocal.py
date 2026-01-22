def update_order():
    chai_type ="elaichi chai"
    def kitchen():
        nonlocal chai_type
        chai_type="Kesar"
    kitchen()
    print("After kitchen update:",chai_type)
update_order()
