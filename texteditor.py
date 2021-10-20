def main():
	first_action = input("Create new text file (N), open existing text file (O), delete existing file (D) or exit program? (X) ").upper()
	if first_action == "N":
		new_file_name = input("Please enter the name of the new text file: ")
		new_file_content = input("Please enter the content for the new text file: ")
		try:
			f = open(new_file_name, "w")
		except:
			print("File could not be opened. Returning to main menu:")
			main()
		try:
			f.write(new_file_content)
			f.close()
			print("File " + new_file_name + " created. Returning to main menu:")
			main()
		except:
			print("File could not be written. Returning to main menu:")
			main()
	elif first_action == "O":
		open_file_name = input("Please enter the name of the file you want to open: ")
		try:
			f = open(open_file_name, "r")
			print(f.read())
		except:
			print("File could not be opened. Returning to main menu:")
			main()
		edit_or_close = input("Edit text file (E) or close text file (C)? ").upper()
		if edit_or_close == "E":
			new_file_text = input("Please enter the file text as you want it to be: ")
			try:
				f = open(open_file_name, "w")
			except:
				print("File could not be opened. Returning to main menu:")
				main()
			try:
				f.write(new_file_text)
				f.close()
				print("File " + open_file_name + " edited. Returning to main menu:")
				main()
			except:
				print("File could not be changed. Returning to main menu:")
				main()
		elif edit_or_close == "C":
			f.close()
			print("File closed. Returning to main menu:")
			main()
		else:
			print("Invalid input. Returning to main menu:")
			main()
	elif first_action == "D":
		import os
		delete_file = input("Please enter the name of the file you want to delete: ")
		try:
			os.remove(delete_file)
			print("File " + delete_file + " deleted. Returning to main menu:")
			main()
		except:
			print("File could not be deleted. Returning to main menu:")
			main()
	elif first_action == "X":
		print("Text editor exited.")
		quit()
	else:
		print("Invalid input. Please try again.")
		main()

main()