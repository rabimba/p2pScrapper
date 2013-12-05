p2pScrapper
===========

>Designed as part of a Proof-Of-Concept for the CS539.501 Research Paper Under  Prof. Timothy Culver.


## System Dependency: ##

Right now the code will only work under Linux. Hence you need to run this in linux. And also some of the codes utilized as part of the urlsnurf requires you to have root access. Hence installing using root is needed.
+	Linux (OS) or Macintosh with Macports (not-tested)
+	Python 2.7.x installed
+	Root user access enabled
+	�torrent installed



## Installation Instruction: ##

- ### Installing BitTorrent ###
	+	The easiest way to install is to run the �install_nix.sh� in the bittorrent folder.
	+	OR $ python setup.py install
- ### Using the Scrapper(To Start The Attack) ######

	+	Import the schema.sql in your mysql database. It will create the relevant databse and the tables in your MySql where the infohash will be stored. Right now it will use a database name rkfake.
	+	Start fake.py as root (or sudo)
	+	Start �Torrent as the announce server. (In "advanced" under preferences)
	+	In �Torrent Force all outgoing connections to be encrypted. (In "BitTorrent" under preferences)
	+	Change �Torrent's port to 3128 for urlsnarf's default
	+	Create a torrent file and seed it with uTorrent
	+	Open that .torrent file with p2pScrapper's Python bittorrent client

