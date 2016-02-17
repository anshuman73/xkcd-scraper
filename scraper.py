# Copyright Anshuman73.
# Visit anshuman73.github.io for more info.
# Released under MIT License.
# Works with Python 2.7

import json
import urllib
import os

def main():
	print 'Querying Total Number of Images as of now...'
	total = json.loads(urllib.urlopen('http://xkcd.com/info.0.json').read())['num']
	print 'Querying complete\n\nTotal of ' + str(total) + ' images found\n\n'
	base_url = 'http://xkcd.com/%s/info.0.json'
	wd = os.getcwd()
	print 'Checking if /images directory exists...\n'
	if not os.path.exists(wd + '/images'):
		print 'Making directory /images\n'
		os.makedirs(wd + '/images')
	for num in xrange(total, 0, -1):
		if num == 404:
			print '\n\nImage 404 is a pathetic little joke -__- Ignoring...\n\n'
			continue
		if num == 1608:
			print '\nComic 1608 is actually an interactive game.\nVisit http://xkcd.com/1608 to play !\n'
			continue

		url = base_url % (num)
		img_metadata = json.loads(urllib.urlopen(url).read())
		extension = img_metadata['img'][img_metadata['img'].rfind(".") : ]
		if not os.path.exists(wd + '/images/' + str(num) + ' - ' + img_metadata['safe_title'] + extension):
			print 'Downloading image ' + str(num) + ' - "' + img_metadata['safe_title'] + '"'
			urllib.urlretrieve(img_metadata['img'], wd + '/images/' + str(num) + ' - ' + img_metadata['safe_title'] + extension)
		else:
			print 'Image ' + str(num) + ' - "' + img_metadata['safe_title'] + '" already exists. Skipping...'


if raw_input('\nPress Enter to start:') == '':
	main()
