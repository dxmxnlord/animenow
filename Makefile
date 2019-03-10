
default:
	@echo "creating directories..."
	@mkdir ~/animenow
	
install:
	@echo "installing animenow..."
	@echo "copying files to appropriate directories..."
	@cd main; \
	cp -p bars.py ~/animenow; \
	cp -p main.py ~/animenow; \
	cp -rp counter ~/animenow; \
	cp -rp data ~/animenow; \
	cp -rp main ~/animenow; \
	cp -p start.sh ~/animenow
	@echo "giving permissions..."
	@cd ~/animenow; \
	chmod 777 start.sh; \
	echo "creating binary..."; \
	touch animenow.sh; \
	echo "#!/bin/bash" >> animenow.sh; \
	echo "cd ~/animenow" >> animenow.sh; \
	echo "./start.sh" >> animenow.sh; \
	chmod 777 animenow.sh; \
	sudo cp animenow.sh /usr/bin/; \
	cd /usr/bin/; \
	sudo mv animenow.sh animenow
	@cd ~/animenow; \
	rm animenow.sh
	@echo "...done installing"
	@cd ..; \
	rm -fr animenow

uninstall:
	@echo "uninstalling..."
	@rm -fr ~/animenow; \
	cd /usr/bin/; \
	sudo rm animenow
	@echo "...done uninstalling"

.PHONY: default install clean
