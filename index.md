## CS-499 Computer Science Capstone

The artifact I decided to use for the Software Design/Engineering is from CS-340, Advance Programming Concepts.  The artifact is for animal management for an animal shelter, which is why I decided to name the application Animal Shelter.  Animal Shelter is written in python, has basic CRUD operations and also a dashboard with several different charts to help the user quickly ingest data.  

I chose this artifact because I remember completing it in CS-340 and being very frustrated with how the code was laid out and the fact we were using Jupyter Notebook for the user interface (UI).  I knew I could take the artifact and rewrite it in C# and deliver a technically sound application that demonstrated my ability to implement a solution that met the customer’s needs and accomplished industry-specific goals. During this enhancement I was able to finalize the database and created an entity relationship (ER) diagram.

![image](https://user-images.githubusercontent.com/30158121/154820537-606618ca-46d4-47be-94fd-afcc9d2421ea.png)

Creating the ER diagram will help other developers be able to quickly pick-up on how the data is connected and how it can be queried.  Breaking the data up from a flat table to multiple tables help make a logical path to create, read, update and delete data.  It will also help to only pull the data you need, which could speed up query and processing times.  Normally, the ER diagram would be used internally on the development team, however, if the customer has a data analyst or a more technical person, I would use the ER diagram to show how we are representing the data to make sure we are getting the relationships correct. 

During this enhancement I also started implementing domain objects, in order to stop bad data from making it to the data layer.  Shown below is the domain object NotNullOrEmptyString that will check if a string is empty or not and then return a result of either success or failure.  Upon a successful creation of a NotNullOrEmptyString the result will have a value property of the original string value. 

![image](https://github.com/jcarter0149/jcarter0149.github.io/blob/gh-pages/images/DomainClass.png?raw=true)

I put this to use in the custom filter to ensure the username Windows passed was not empty or null.  I also changed the parameter of the IsUserAnAdminOrAssistant, to accept the domain object instead of a string. This will ensure that when the data makes it to the data layer (_roleApplicationService in this instance) it is not empty and the database will not throw an exception or return something that is not expected. 

![image](https://github.com/jcarter0149/jcarter0149.github.io/blob/gh-pages/images/PassingDomainObject.png?raw=true)
![image](https://github.com/jcarter0149/jcarter0149.github.io/blob/gh-pages/images/CreatingDomainObject.png?raw=true)
