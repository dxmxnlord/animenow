
default:
	@echo "creating directories..."
	@mkdir ~/Animenow
	
install:
	@echo "installing animenow..."
	@echo "copying files to appropriate directories..."
	@cd main; \
	cp -p bars.py ~/Animenow; \
	cp -p main.py ~/Animenow; \
	cp -rp counter ~/Animenow; \
	cp -rp data ~/Animenow; \
	cp -rp main ~/Animenow; \
	cp -p start.sh ~/Animenow
	@echo "giving permissions..."
	@cd ~/Animenow; \
	chmod 777 start.sh; \
	echo "creating binary..."; \
	touch animenow.sh; \
	echo "#!/bin/bash" >> animenow.sh; \
	echo "cd ~/Animenow" >> animenow.sh; \
	echo "./start.sh" >> animenow.sh; \
	chmod 777 animenow.sh; \
	sudo cp animenow.sh /usr/bin/; \
	cd /usr/bin/; \
	sudo mv animenow.sh animenow
	@cd ~/Animenow; \
	rm animenow.sh
	@echo "...done installing"
	@cd ..; \
	rm -fr animenow
	@cd

uninstall:
	@echo "uninstalling..."
	@rm -fr ~/Animenow; \
	cd /usr/bin/; \
	sudo rm animenow
	@echo "...done uninstalling"

.PHONY: default install uninstall
