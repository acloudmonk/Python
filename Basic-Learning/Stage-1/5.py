# Enter temparature in farenhite and change in centigrate and print it

if __name__ == "__main__":
    farenhite_temparature = float(input("Enter temparature in farenhite : "))
    centigrate = (farenhite_temparature - 32) * 5 / 9
    print("Temparature in centigrate is : ", centigrate)
