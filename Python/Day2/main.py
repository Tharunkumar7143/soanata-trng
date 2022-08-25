from leave import Leave
from basketleave import BasketOfLeave
from restrictedleave import RestrictedLeave
r1=RestrictedLeave(22769,"tharun kumar",20,"1999-07-22")
print(r1.display_dob())
b1=BasketOfLeave(22769,"tharun kumar",20,"health")
print(b1.displayleave())
l1=Leave(22769,"tharun kumar",20)
print(l1.display())
