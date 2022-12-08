from collections import OrderedDict

glossary=OrderedDict()

glossary['user-centered design']='is an iterative design process in which designers focus on the users and their needs in each phase of the design process.',
glossary['blockchain']=' is a shared, immutable ledger that facilitates the process of recording transactions and tracking assets in a business network.',
glossary['folksonomy']=' is a classification system in which end users apply public tags to online items, typically to make those items easier for themselves or others to find later.',
glossary['artificial neural network']='is an interconnected group of nodes, inspired by a simplification of neurons in a brain.',
glossary['autoencoder']='is a type of artificial neural network used to learn efficient codings of unlabeled data (unsupervised learning)',
glossary['API']='Application Programming Interface'
glossary['Access Control List']='is a list of rules that specifies which users or systems are granted or denied access to a particular object or system resource.'
glossary['AdBlock']=' is one of the most popular ad blockers worldwide with more than 60 million users on Chrome, Safari, Firefox, Edge as well as Android.'
glossary['Agile Software Development']='practices include requirements discovery and solutions improvement through the collaborative effort of self-organizing and cross-functional teams with their customer(s)/end user(s),[2] adaptive planning, evolutionary development, early delivery, continual improvement, and flexible responses to changes in requirements, capacity, and understanding of the problems to be solved.'
glossary['Back End']='software development and interface with third party APIs/'

for word,value in glossary.items():
	print("\n"+str(word)+" "+str(value)) 
