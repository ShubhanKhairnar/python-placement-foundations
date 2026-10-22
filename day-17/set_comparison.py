#Three things to remember about sets:
#- They contain unique elements.
#- They don't support positional indexing like my_list[0].
#- They're useful for membership checks and comparing groups.

group_a = [101, 102, 103, 104, 104]
group_b = [103, 104, 105, 106]

set_a = set(group_a)
set_b = set(group_b)

common_ids = set_a & set_b

only_a = set_a - set_b 

only_b = set_b - set_a

print("IDs in both groups:", common_ids)
print("IDs only in Group A:", only_a)
print("IDs only in Group B:", only_b)

