1. Make Git Repository

	'''python
	mkdir new_repository
	cd new_repository
	git init
	'''

2. Make a file that git will take care of

	'''python
	vim new_file.txt
	git add new_file.txt
	'''

3. Make versions (setting up the writer info)

	'''python
	git config --global user.name "my_nickname"
	git config --global user.email "my_email"
	'''

4. Commit & Add (you must add files before committing in order to include files into version selectively)

5. Compare codes between versions

	'''python
	git log
	# difference between versions
	git diff 'version_id1' .. 'version_id2'
	# difference before adding and after adding
	git diff
	'''
	
