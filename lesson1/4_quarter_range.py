def show_quarter_range(quarter_num: int) -> object:
    print(f"range values of {quarter_num} quarter:", end=" ")

    if quarter_num == 1:
        print("X > 0, Y > 0")
    elif quarter_num == 2:
        print("X < 0, Y > 0")
    elif quarter_num == 3:
        print("X < 0, Y < 0")
    elif quarter_num == 4:
        print("X > 0, Y < 0")
    else:
        print("incorrect quarter number")


show_quarter_range(1)
show_quarter_range(3)
show_quarter_range(7)
