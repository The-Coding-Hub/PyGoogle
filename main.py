import webbrowser

query = input("Enter what you want to find: ")
to_open = "https://google.com/search?q=" + query

webbrowser.open(to_open)