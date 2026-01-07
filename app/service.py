# def process_value(value):
#     if value:
#         return {"result": value * 2}
#     return "invalid"
# ==> FIX
def process_value(value: int) -> int:
    if value <= 0:
        raise ValueError("value must be a positive integer")
    return value * 2
