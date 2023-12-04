# Turn a line of text into 2 lists, first containing Game ID and second played games
def splitIntoParts(lineoftext):
    id_and_cubes = lineoftext.split(":")
    game_id = id_and_cubes[0]
    cubes = id_and_cubes[1].split(";")
    # Strip "Game: ", we only need id as int
    game_id = int(game_id.strip("Game: "))

    return game_id, cubes

# Return the amount of cubes in a game (1 or 2 digits)
def getAmount(input_str):
    try:
        number = int(input_str[0:2])
        return number
    except ValueError:
        return int(input_str[0])

# Count the maximum occurence of each color with information we have
def countCubes(gamelist):
    blu_max = 0
    grn_max = 0
    red_max = 0
    # Check all games
    for game in gamelist:
        # Tidy up
        game = game.strip("\n")
        # Separate colors
        colors = game.split(",")
        
        for color in colors:
            # No whitespaces
            color = color.strip(" ")
            amount = getAmount(color)
            # Check color and save amount if it's largest so far
            if "blue" in color:
                if amount > blu_max:
                    blu_max = amount
            elif "green" in color:
                if amount > grn_max:
                    grn_max = amount
            elif "red" in color:
                if amount > red_max:
                    red_max = amount

    return blu_max, grn_max, red_max

if __name__ == "__main__":
    # Open file to be used
    input_file = open("C:\\Users\\Miika\\Documents\\AOC23\\day02\\input.txt", "r")

    # Hande the file line by line
    sum = 0
    power_sum = 0
    for line in input_file:
        # Get game id and max amount of colors
        id, games = splitIntoParts(line)        
        blue, green, red = countCubes(games)

        # Check if there is correct amount of cubes (job01)
        if blue <= 14 and green <= 13 and red <= 12:
            sum += id
        
        # Calculate and add the power
        power_sum += blue*green*red

    print(f"Job 1: {sum}")
    print(f"Job 2: {power_sum}")

    input_file.close()