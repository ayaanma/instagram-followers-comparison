# hold followers/following.html files in string
extracted_followers = ''
extracted_following = ''

# hold current follower/following user
compiled_follower = ''
compiled_following = ''

# compiled list of all followers/following
followers_list = []
following_list = []

# reads when to add in account
scanner_on_deck = False
scanning = False

# open follower.html file
with open('followers_1.html', 'r') as followers:
    for line in followers:
        extracted_followers += line

# compile followers
for char in range(len(extracted_followers)):
    # check if instagram link found
    if (extracted_followers[char] == '.' and extracted_followers[char + 1] == 'c' and extracted_followers[char + 2] == 'o' and extracted_followers[char + 3] == 'm' and extracted_followers[char + 4] == '/'):
        scanner_on_deck = True

    # check if instagram link completed
    if (scanner_on_deck and extracted_followers[char - 1] == '"' and extracted_followers[char] == '>'):
        scanning = True
        continue

    # add completed follower into list
    if (scanning and extracted_followers[char] == '<' and extracted_followers[char + 1] == '/' and extracted_followers[char + 2] == 'a' and extracted_followers[char + 3] == '>'):
        followers_list.append(compiled_follower + '\n')
        compiled_follower = ''
        scanner_on_deck = False
        scanning = False

    # add follower letter by letter
    if (scanning):
        compiled_follower += extracted_followers[char]

# open following.html file
with open('following.html', 'r') as following:
    for line in following:
        extracted_following += line

# compile following
for char in range(len(extracted_following)):
    # check is instagram link found
    if (extracted_following[char] == '.' and extracted_following[char + 1] == 'c' and extracted_following[char + 2] == 'o' and extracted_following[char + 3] == 'm' and extracted_following[char + 4] == '/'):
        scanner_on_deck = True

    # check if instagram link completed
    if (scanner_on_deck and extracted_following[char - 1] == '"' and extracted_following[char] == '>'):
        scanning = True
        continue

    # add completed account followed into list
    if (scanning and extracted_following[char] == '<' and extracted_following[char + 1] == '/' and extracted_following[char + 2] == 'a' and extracted_following[char + 3] == '>'):
        following_list.append(compiled_following + '\n')
        compiled_following = ''
        scanner_on_deck = False
        scanning = False

    # add account followed letter by letter
    if (scanning):
        compiled_following += extracted_following[char]

# sort alphabetically for easy comparison, otherwise sorted by most recent followed/following
followers_list.sort()
following_list.sort()

# write information onto respective .txt files
with open('followers.txt', 'w') as followers:
    for item in followers_list:
        followers.write(item)

with open('following.txt', 'w') as following:
    for item in following_list:
        following.write(item)
