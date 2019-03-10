#!/bin/bash

cd ~/animenow
while [ true ]; do
	clear
	python3 -c "import main; main.disp_options()"
	echo 
	read -p "> " input
	clear
	cd main
	if [ $input -eq 1 ]; then
		python3 -c "import addtowatchlist; addtowatchlist.add_to_watchlist()"
		echo
		read holder
	fi
	if [ $input -eq 2 ]; then
		python3 -c "import deletefromwatchlist; deletefromwatchlist.delete_from_watchlist()"
		echo
		read holder
	fi
	if [ $input -eq 3 ]; then
		python3 -c "import clearwatchlist; clearwatchlist.clear_watchlist()"
		echo
		read holder
	fi
	if [ $input -eq 4 ]; then
		python3 -c "import checkwatchlist; checkwatchlist.check_watchlist()"
		echo
		read holder
	fi
	if [ $input -eq 5 ]; then
		python3 -c "import os;os.chdir('..');import bars;os.chdir('main');import displaywatchlist; bars.display_watchlist_bar();displaywatchlist.display_watchlist()"
		echo
		read holder
	fi
	if [ $input -eq 6 ]; then
		cd ..
		cd counter
		while [ true ]; do
			clear
			echo
			python3 -c "import maincounter; maincounter.counter_menu()"
			echo
			read -p "> " subinput
			clear
			if [ $subinput -eq 1 ]; then
				echo
				python3 -c "import os;os.chdir('..');import bars;os.chdir('counter');import displaycounter; bars.display_counter_bar();displaycounter.display_counter()"
				echo
				read subholder
			fi
			if [ $subinput -eq 2 ]; then
				python3 -c "import addcounter; addcounter.add_episode()"
				echo
				read subholder
			fi
			if [ $subinput -eq 3 ]; then
				python3 -c "import subtractcounter; subtractcounter.subtract_episode()"
				echo
				read subholder
			fi
			if [ $subinput -eq 4 ]; then
				python3 -c "import changecounter; changecounter.change_episode()"
				echo
				read subholder
			fi
			if [ $subinput -eq 5 ]; then
				cd ..
				cd main
				break
			fi
		done
	fi
	if [ $input -eq 7 ]; then
		python3 -c "import downloadshow; downloadshow.download_episode()"
		echo
		read holder
	fi
	if [ $input -eq 8 ]; then
		exit
	fi
	cd ..
done
