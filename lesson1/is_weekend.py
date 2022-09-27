def is_weekend(day_num: int) -> bool:
    if not(1 <= day_num <= 7):
        raise Exception(f"{day_num} : is not week day number!")
    return day_num == 6 or day_num == 7


dayNum: int = int(input("insert week day num: "))
if is_weekend(dayNum):
    print(f'it\'s weekend')
else:
    print(f'it\'s not weekend')
