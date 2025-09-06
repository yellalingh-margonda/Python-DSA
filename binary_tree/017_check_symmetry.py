def symmetry(t1, t2):
    if not t1 and not t2:
        return True
    if not t1 or not t2:
        return False
    return t2.val==t1.val and symmetry(t1.left, t2.right) and symmetry(t1.right, t2.left)