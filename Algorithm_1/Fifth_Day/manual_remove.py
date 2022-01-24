->1->2->3->4->5->6

t = r = &1
l = m = 1

t = &3
m = 3 

r = &5
l = 6 

i = 6 - n 

i > 3 => I can use mid pointer t

Let us say n = 3 
i = 3 in this case # i gives me the node before the wanted node

REMOVE:
        rem = &4 
        t.next = &5
        del rem

Let us say n = 2
i = 4 in this case # i gives me the node before the wanted node

#one round of nexting
t = t.next 
t = &4
jump REMOVE

Let us say n = 4 (&3) # our mid element
i = 2 in this case # i gives me the node before the wanted node

# so I should start from head until I hit the previous node
# and do the REMOVE action again

t = &1
i = 2

t = &2
i = 1

rem = t.next 
t.next = t.next.next
del rem
