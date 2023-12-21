def err( a, id):
    try:
        res = a[id]
        print(f"data at index {id}:")
        return res
    except IndexError:
        return "Index out of range"

a = [1,2,3,4]
id = int(input())
print(err(a,id))
