original = "sixdle.txt"
output = "sixdle"

assert original != output

with open(original, "r") as i:
    with open(output, "w+") as o:
        o.write(i.readlines()[0].replace(" ", "\n"))