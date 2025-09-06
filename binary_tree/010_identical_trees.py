def idnetical(p,q):
    if not p or not q:
        return  p==q
    return p.val==q.val and idnetical(p.left, q.left) and idnetical(p.right, q.right)