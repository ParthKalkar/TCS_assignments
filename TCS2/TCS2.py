# Parth Kalkar, TCS-Final-Part-B

import sys
# The following implementation just checks the each state indivdually and handles them.
# The several if else clauses are for the states.

# The following is the use of file handling
input = open("input.txt", "r")
output = open("output.txt", "a")
open("output.txt", "w").close()
string = input.readline()
v = ["Z", "-"]
ind = 0
state = 0
i = 0
if string.count('#') != 1:
    output.write("Invalid input")
    output.close()
    sys.exit()
for let in string:
    if let != "#" and let != "1" and let != "0":
        output.write("Invalid input")
        output.close()
        sys.exit()
if string[0] == "0" and string[1] != "#":
    output.write("Invalid input")
    output.close()
    sys.exit()
true = True
ok = False
string += "-"
while true and not ok: # I check several conditions here specifying the validity of our input string and continue looping
    t = ""
    t = t + "q" + str(state) + ", "
    for j in range(len(string)):
        if (j == i):
            t = t + "^"
        if string[j] != "-":
            t = t + string[j]
    t = t + ", "
    for j in range(len(v)):
        if j == ind:
            t = t + "^"
        if v[j] != "-":
           t = t + str(v[j])
    output.write(t)
    output.write("\n")
    if state == 0:
        if string[i] == '1' and v[ind] == "Z":
            ind = ind + 1
        elif string[i] == '0' and v[ind] == "Z":
            ind = ind + 1
        elif string[i] == '1' and v[ind] == "-":
            v[ind] = "1"
            v.append("-")
            i = i + 1
            ind = ind + 1
        elif string[i] == '0' and v[ind] == "-":
            v[ind] = "0"
            v.append("-")
            i = i + 1
            ind = ind + 1
        elif string[i] == '#' and v[ind] == "-":
            i = i + 1
            ind = ind - 1
            state = 1
        else:
            true = False
    elif state == 1:
        if string[i] == '1' and v[ind] == '1':
            i = i + 1
            ind = ind - 1
        elif string[i] == '1' and v[ind] == '0':
            i += 1
            ind -= 1
        elif string[i] == '0' and v[ind] == '0':
            i += 1
            ind -= 1
        elif string[i] == '0' and v[ind] == '1':
            i += 1
            ind -= 1
        elif string[i] == '-' and (v[ind] == '0' or v[ind] == "1"):
            state = 4
        elif string[i] == '-' and v[ind] == "Z":
            i -= 1
            state = 2
        else:
            true = False


    elif state == 3:
        if string[i] == "1" and v[ind] == "1":
            i = i + 1
            ind += 1
        elif string[i] == "0" and v[ind] == "0":
            i = i + 1
            ind += 1
        elif string[i] == "0" and v[ind] == "1":
            state = 4
        else:
            true = False

    elif state == 2:
        if (string[i] == "0" or string[i] == "1") and v[ind] == "Z":
            i -= 1
        elif string[i] == "#" and v[ind] == "Z":
            i += 1
            ind += 1
            state = 3
        else:
            true = False

    elif state == 4:
        ok = True

if ok: # My function to check if the string is accepted and adds it to the output file
    output.write("YES")
    output.close()
else: # Else no
    output.write(t)
    output.write("\n")
    output.write("NO")
    output.close()