from distutils.core import setup
import py2exe, sys, os

from glob import glob
data_files = [("Microsoft.VC90.CRT", glob(r'C:\Documents and Settings\Integration Lab\Desktop\Microsoft.VC90.CRT\*.*')),
'empty map with goal and robot',
'work.glade']
setup( data_files=data_files )




sys.argv.append('py2exe')
setup(
 options = {
                  'py2exe': {
                      'packages':'encodings',
                      # Optionally omit gio, gtk.keysyms, and/or rsvg if you're not using them
                      'includes': 'cairo, pango, pangocairo, atk, gobject, gio, gtk.keysyms, rsvg',
                  }
              },
  zipfile=None,
  console = ['rimulator.py'],
)

##setup(
##    options = {
##    'py2exe' : {
##        'compressed': 2,
##        'optimize': 2,
##        'bundle_files': 1,
##        'excludes': excludes}
##        },
##    zipfile=None, console = [ 'rimulator.py' ] )


