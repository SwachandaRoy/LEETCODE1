curr = head
pre = None
nxt = None
while(curr):
    nxt = curr.next # hold the next address of curr
    curr.next = pre # connect current to pre " <- " (reverse node)
    pre = curr # move previous
    curr = nxt # move curr 
    
return pre
