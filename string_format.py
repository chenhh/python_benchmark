import timeit

ITERATIONS = 1_000_000

name = "John Doe"
age = 30

# +
plus_string_elapsed = timeit.timeit(lambda: name + " is " + str(age) + ".", number=ITERATIONS)

# Percent string
percent_string_elapsed = timeit.timeit(lambda: "%s is %s." % (name, age), number=ITERATIONS)

# str.format()
str_format_elapsed = timeit.timeit(lambda: "{} is {}.".format(name, age), number=ITERATIONS)

# f-string
f_string_elapsed = timeit.timeit(lambda: "{name} is {age}.", number=ITERATIONS)

result = (
    f"plus string: {plus_string_elapsed:.3} s\n"
    f"percent string: {percent_string_elapsed:.3} s\n"
    f"str_format: {str_format_elapsed:.3} s\n"
    f"f-string: {f_string_elapsed:.3} s"
)
print(result)