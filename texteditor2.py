def main():
	first_action = input("Create new text file (N), open existing text file (O), delete existing file (D) or exit program? (X) ").upper()
	if first_action == "N":
		new_file_name = input("Please enter the name of the new text file: ")
		new_file_content = input("Please enter the content for the new text file: ")
		try:
			with open(new_file_name, mode="w") as file:
				file.write(new_file_content)
			print("File " + new_file_name + " created. Returning to main menu:")
			main()
		except:
			print("File could not be created. Returning to main menu:")
			main()
	elif first_action == "O":
		open_file_name = input("Please enter the name of the file you want to open: ")
		try:
			with open(open_file_name) as file:
				data = file.read()
				print(data)
		except:
			print("File could not be opened. Returning to main menu:")
			main()
		edit_or_return = input("Edit text file (E) or return to the main menu (R)? ").upper()
		if edit_or_return == "E":
			new_file_text = input("Please enter the file text as you want it to be: ")
			try:
				with open(open_file_name, mode="w") as file:
					file.write(new_file_text)
				print("File " + open_file_name + " edited. Returning to main menu:")
				close(open_file_name)
				main()
			except:
				print("File could not be edited. Returning to main menu:")
				main()
		elif edit_or_return == "R":
			print("Returning to main menu:")
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