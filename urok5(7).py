data = "string"
print(getattr(data, "startswith"))
print(getattr(data, "startswith", None))
print(getattr(data, "reverse", None))