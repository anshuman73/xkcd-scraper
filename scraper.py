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
	print 'Checking if /images directory exists...'
	if not os.path.exists(wd + '/images'):
		print 'Making directory /images'
		os.makedirs(wd + '/images')
	for num in xrange(1, total + 1):
		if num == 404:
			print '\n\nImage 404 is a pathetic little joke -__- Ignoring...\n\n'
			continue

		url = base_url % (num)
		img_metadata = json.loads(urllib.urlopen(url).read())
		print 'Downloading image ' + str(num) + ' - ' + img_metadata['title']
		urllib.urlretrieve(img_metadata['img'], wd + '/images/' + str(num) + ' - ' + img_metadata['title'])


if raw_input('\nPress Enter to start: \n') == '':
	main()