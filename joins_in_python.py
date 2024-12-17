name = "::Wilfried".casefold()
upper_cased = "".join(
    (
        character.upper() if character != "i" or (character == "i"         and index == 3) else character 
        for index, character in enumerate(name)
    )
)
print(upper_cased)

