The PaintBall project uses the pygame library.
A game window opens and you move the ball with the joystick.
At the moment the game only supports Xbox , PlayStation controllers and Nintendo Switch controller; in the project there is a Unitest folder where I can test the controllers.
When I start the tests and if the controller test is successful, an xml file is created containing all the characteristics of the controller.
I then used the pyinstaller library to render the game into an .exe file.



https://github.com/ultron3/PaintBall/assets/104757961/2478283c-e331-46ec-90d2-24f8dee157b3



Now through a storage device I can save game progress, send a notification of saving success, for notifications I use the win10toast library.
Added folder where I input the xml files so I can read the tags.
