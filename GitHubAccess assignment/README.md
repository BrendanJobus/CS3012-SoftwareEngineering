# Visualizing Software Engineering
This project generates a d3.js tree graph, with the signed in GitHub user as the root node, and all their followers as child nodes, and so on. It goes *two* levels deep, because d3 pretty much just crashes after that (too many nodes).
Nodes are *collapsible*, meaning you can click on nodes to hide its children.

The root node is coloured green, intermediate nodes are a greyish colour, leaf nodes are pink, and collapsed nodes are a dark purple:

![Example](screens/examplescreenshot.jpg)

The project assumes there is a local instance of monogdb running. Set the `FLASK_APP` variable to the project folder, then you need to use the command `flask init-db [your GitHub username]`. This will prompt you for your password, then generate the tree structure needed for the visualization and store the data in the *github_data* database, in a collection called *trees*.

![CLI](screens/cliscreenshot.jpg)

Finally, do `flask run` and browse to [the login screen](http://localhost:5000/auth/login).

![login](screens/loginscreenshot.jpg)
