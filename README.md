# votelib

## Run the prototype
1. Install Python 3.9+
2. Install pytest: `pip install pytest`
3. Run `pytest`

You should see a successful test, indicating that we were able to determine a
FPTP winner from the test votes.

## Product vision
* FOR organizations and municipalities administering elections
* WHO need flexibility to cover many different systems of voting, votelib is a
library that handles various voting systems
* THAT supports more than just Winner-Take-All/First-Past-The-Post systems
* UNLIKE other voting libraries, supports command line interaction.
OUR product is free and open source, improving its security by making the
source code available for security researchers

Votelib is a fast and free library whose primary customers are organizations
and municipalities administering elections. Our library is open source, so it
is free to be analyzed by security researchers and the general public.

# Layered software architecture

## Nonfunctional Product Characteristics
- voting results must be accurate, any incorrect result reporting can affect the product
- One may use VoteLib to count a large number of ballots, so performance is important for our software to succeed
## Product Lifetime
- we can evolve our architecture as we can update our products to include differnt voting systems based on clients request
## Software Reuse
- our product can be resused because voting systems is a popular choice when finding best candidates
- we can reuse old files and compare old results with new results 
## Number of users
- our software needs to be responsive and reliable even with large datasets
## Software Compatibility
- Instead of using VoteLib on its own, one may import VoteLib as a component of another larger application to access some or all of the services provided by VoteLib

User Interface -> User Interface Management -> Application Services

## Architecture diagram
![Capture](https://user-images.githubusercontent.com/77586278/112677611-5af52b00-8e40-11eb-9df8-b79baf8c2314.PNG)







