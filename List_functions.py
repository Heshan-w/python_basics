nums = [1, 4, 23, 65, 33, 65, 23, 7]
teams = ["heats", "rockets", "lakers", "bucks"]

print("extend func")
# "extend" function combines two lists eg:
nums.extend(teams)
print(nums)


nums = [1, 4, 23, 65, 33, 65, 23, 7]
teams = ["heats", "rockets", "lakers", "bucks"]

print("index func")
# "index" function finds the index the parameter passed is stored in (throws an error if parameter is not present in list)
print(nums.index(65))
print(teams.index("rockets"))

print("count func")
# "count" function outputs how many times the parameter passed in is present in the list
print(nums.count(65))
print(teams.count("lakers"))

print("pop func")
#  "pop" function removes the last index from the list
nums.pop()
teams.pop()
print(nums)
print(teams)

print("insert func")
# "insert" function inserts a new data item to a list, 1st parameter is the position to be inserted to, 2nd is the data value to be entered
nums.insert(2, 990)
teams.insert(0, "pistons")
print(nums)
print(teams)

print("sort func")
# sorts the list in ascending order
nums.sort()
teams.sort()
print(nums)
print(teams)

print("reverse func")
# sorts the list in descending order
nums.reverse()
teams.reverse()
print(nums)
print(teams)

nums = [1, 4, 23, 65, 33, 65, 23, 7]
teams = ["heats", "rockets", "lakers", "bucks"]

print("copy func")
# copies one list to a new list
nums2 = nums.copy()
teams2 = teams.copy()
print(nums2)
print(teams2)

print("clear func")
# clears all data on the list
nums.clear()
teams.clear()
print(nums)
print(teams)
