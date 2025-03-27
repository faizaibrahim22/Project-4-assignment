def get_first_element(lst):

    print(lst[0])
def get_lst():

    lst = []
    elem =input("Please enter an element of the list or press enter to stop")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")  # User se next input lete hain
    return lst 
def main():
    lst = get_lst()  # User se list lete hain
    get_first_element(lst)  # List ka pehla element print karte hain

if __name__ == '__main__':
    main() 
       