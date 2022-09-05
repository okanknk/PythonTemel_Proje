# Bir listeyi duzlestiren flatten fonksiyonu
fl_list = []
def flat(lst):
    for i in lst:
        if isinstance(i,list):
            flat(i)
        else:
            fl_list.append(i)

in_list1 = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
flat(in_list1)
print(fl_list)

# Bir listenin icindeki elemanlari tersine donduren, eger listenin icinde liste bulunuyorsa 
# onun elemanlarini da tersine donduren fonksiyon
def rev(lst):
    lst = lst[::-1]
    for i in range(len(lst)):
        lst[i] = lst[i][::-1]
    print(lst)

in_list2 = [[1,2],[3,4],[5,6,7]]
rev(in_list2)