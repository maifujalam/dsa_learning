print("File Name is %s" %__name__)
if __name__ == "__main__":
    print("It is called by itself")
else:
    print("It is called by others module %s"%__name__)