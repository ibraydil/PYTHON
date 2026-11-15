def ft_count_harvest_recursive(start=1, a=None):
    if a is None:
        a = int(input("Days until harvest: "))
    if start <= a:
        print("Day", start)
        ft_count_harvest_recursive(start + 1, a)
    else:
        print("Harvest time!")
