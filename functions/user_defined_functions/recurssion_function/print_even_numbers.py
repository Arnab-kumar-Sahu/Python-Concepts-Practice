def display(n):
    if n==0:
        return
    if n%2==0:
        print(n)
    display(n-1)
display(int(input("enter range")))
# print in alternate order
def display_rev_order(n):
    if n==0:
        return
    display_rev_order(n-1)
    if n%2==0:
        print(n)
display_rev_order(int(input("enter range")))