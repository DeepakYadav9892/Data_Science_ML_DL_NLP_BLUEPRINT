def brew_chai(flavor):
   if flavor not in ["masala","ginger","elaichi"]:
      raise ValueError("Unsopported chai flavor")
   print(f"brewing {flavor} chai.....")



brew_chai("mint")

