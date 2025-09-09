# Can you change the value inside a list which is contained in set S
# no and we cannot not add list in sets because its mutable and non hashable
#  sets contain only hashable immutable


# s={8,7,12,"Abdul",[1,2]} #flase
ss={8,7,12,"Abdul", (1,2)} #true

# s.update() not do it because in set no indexing
# print(s)

