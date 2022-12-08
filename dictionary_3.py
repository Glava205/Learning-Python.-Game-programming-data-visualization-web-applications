glossary={
	'user-centered design':'is an iterative design process in which designers focus on the users and their needs in each phase of the design process.',
	'blockchain':' is a shared, immutable ledger that facilitates the process of recording transactions and tracking assets in a business network.',
	'folksonomy':' is a classification system in which end users apply public tags to online items, typically to make those items easier for themselves or others to find later.',
	'artificial neural network':'is an interconnected group of nodes, inspired by a simplification of neurons in a brain.',
	'autoencoder':'is a type of artificial neural network used to learn efficient codings of unlabeled data (unsupervised learning)',
}

for glossar in glossary:
	print(glossar.title()+"\n"+glossary[glossar]+"\n")
