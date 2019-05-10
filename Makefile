



default:
	@echo "creating directories..."
	@touch user.txt; \
	echo $(shell whoami) >> "user.txt"
	@mkdir ~/Animenow
	
install:
	@echo "installing animenow..."
	@echo "copying files to appropriate directories..."
	@export user=$(shell cat user.txt); \
	cd main; \
	cp -p bars.py /home/$${user}/Animenow; \
	cp -p main.py /home/$${user}/Animenow; \
	cp -rp counter /home/$${user}/Animenow; \
	cp -rp data /home/$${user}/Animenow; \
	cp -rp main /home/$${user}/Animenow; \
	cp -p start.sh /home/$${user}/Animenow; \
	echo "giving permissions..."; \
	cd /home/$${user}/Animenow; \
	chmod 777 start.sh; \
	echo "creating binary..."; \
	touch animenow.sh; \
	echo "#!/bin/bash" >> animenow.sh; \
	echo "cd /home/$${user}/Animenow" >> animenow.sh; \
	echo "./start.sh" >> animenow.sh; \
	chmod 777 animenow.sh; \
	sudo cp animenow.sh /usr/bin/; \
	cd /usr/bin/; \
	sudo mv animenow.sh animenow; \
	cd /home/$${user}/Animenow; \
	rm animenow.sh; \
	echo "...done installing"; \
	cd ..; \
	rm -fr animenow

uninstall:
	@echo "uninstalling..."
	@export user=$(shell cat user.txt); \
	rm -fr /home/$${user}/Animenow; \
	cd /usr/bin/; \
	sudo rm animenow
	@echo "...done uninstalling"

.PHONY: default install uninstall
