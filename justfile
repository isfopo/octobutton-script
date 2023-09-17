install:
	python3 scripts/install.py --name Octobutton

watch:
	python3 scripts/watch.py --version 'Live 11.3.10'

close-set:
	pkill -x Ableton Live 11 Suite

open-set:
	open set/devset.als

reload:
	just install && just close-set && sleep 1 && just open-set

rename:
	python3 scripts/rename.py