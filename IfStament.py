
is_tall = False

is_male = True

if is_male and is_tall:
    print("You are a male and tall")

elif is_male and not(is_tall):
    print("You are a male and not tall")

elif is_tall and not(is_male):
    print("You are tall but not a male")

if not is_male and not is_tall:
    print("You are not a male or tall")

