# Python script used to test calling a button press function 

When then script is ran it will sit waiting for a button press. Once the button is pressed you will get a message saying the box is unlocked.
You can push the button again to display box is unlocked.

### What is happening
When the script is ran the current state of the is_button_up function is False. Causing the program to sit and wait for a buttonpress.
Once the button is pressed the function will return True satisfying the if statement "if box.is_button_up():" under boxtest.py.
Which will print box is unlocked
