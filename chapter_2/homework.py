from classes import Array

MAX_SIZE = 100  # Max size of the array


def project_2_1():
    array = Array(MAX_SIZE)
    array.insert(77)
    array.insert(99)
    array.insert(100)
    array.insert(-49)
    array.insert("alpha")
    array.insert("beta")
    array.insert("charlie")
    array.insert("delta")

    print(array.get_max_num())



def project_2_2():
    array = Array(MAX_SIZE)
    array.insert(77)
    array.insert(99)
    array.insert(100)
    array.insert(-49)
    array.insert("alpha")
    array.insert("beta")
    array.insert("charlie")
    array.insert("delta")

    print(f"Array size before delete_max_num() {len(array)}")
    print(array.delete_max_num())
    print(f"Array size after delete_max_num() {len(array)}")


def project_2_4():
    array = Array(MAX_SIZE)
    array.insert(77)
    array.insert(77)
    array.insert("77")
    array.insert(77)
    array.insert(77)
    array.insert(77)
    array.insert(77)
    array.insert(77)
    array.insert(99)
    array.insert(100)
    array.insert(-49)
    array.insert("alpha")
    array.insert("beta")
    array.insert("charlie")
    array.insert("delta")
    array.insert("delta")
    array.insert("delta")
    array.insert("delta")
    array.insert("Delta")

    print("Array before remove_dupes()")
    array.traverse()
    array.remove_dupes()
    print("Array after remove_dupes()")
    array.traverse()
 


if __name__ == "__main__":
    project_2_4()