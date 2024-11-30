list_of_names = ["John Stones", "Hzxry Kxne", "Raheem Sterling", "Jordan Pickford", "Harry Maguire", "Declan Rice", "Jack Grealish", "Mason Mount", "Kalvin Phillips", "Kyle Walker", "Luke Shaw", "Kieran Trippier", "Jadon Sancho", "Dominic Calvert-Lewin", "Bukayo Saka", "Phil Foden", "Ben Chilwell", "Conor Coady", "Reece James", "Tyrone Mings", "Sam Johnstone", "Ben White", "Aaron Ramsdale", "Jesse Lingard", "Marcos Alonso", "Patrick Bamford", "James Ward-Prowse", "Ollie Watkins", "Ben Godfrey", "Emile Smith Rowe", "John Stones", "Harry Kane", "Raheem Sterling", "Jordan Pickford", "Harry Maguire", "Declan Rice", "Jack Grealish", "Mason Mount", "Kalvin Phillips", "Kyle Walker", "Luke Shaw", "Kieran Trippier", "Jadon Sancho", "Dominic Calvert-Lewin", "Bukayo Saka", "Phil Foden", "Ben Chilwell", "Conor Coady", "Reece James", "Tyrone Mings", "Sam Johnstone", "Ben White", "Aaron Ramsdale", "Jesse Lingard", "Marcos Alonso", "Patrick Bamford", "James Ward-Prowse", "Ollie Watkins", "Ben Godfrey", "Emile Smith Rowe", "John Stones", "Harry Kane", "Raheem Sterling", "Jordan Pickford", "Harry Maguire", "Declan Rice", "Jack Grealish", "Mason Mount", "Kalvin Phillips", "Kyle Walker", "Luke Shaw", "Kieran Trippier", "Jadon Sancho", "Dominic Calvert-Lewin", "Bukayo Saka", "Phil Foden", "Ben Chilwell", "Conor Coady", "Reece James", "Tyrone Mings", "Sam Johnstone", "Ben White", "Aaron Ramsdale", "Jesse Lingard", "Marcos Alonso", "Patrick Bamford", "James Ward-Prowse", "Ollie Watkins", "Ben Godfrey", "Emile Smith Rowe", "John Stones", "Harry Kane"]

search_name = "Hzxry Kxne"
match = dict()
for name in list_of_names:
    match[name] = 0
   
    
    for search_letter in search_name:    
        cpt = 0
        for letter in name:
            if letter == search_letter:
                cpt += 1
        match[name] = cpt
        
        
        
print(match)
                
            