
# coding: utf-8

# # Setup Sublime Text 3 for Python

# In Terminal, run
# 
# ```bash
# sudo ln -s /Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl /usr/local/bin/subl
# ```

# In ST3:
# - Click **View > Show Console** to open ST3 console and run:
# ```py
# import urllib.request,os,hashlib; h = 'df21e130d211cfc94d9b0905775a7c0f' + '1e3d39e33b79698005270310898eea76'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); by = urllib.request.urlopen( 'http://packagecontrol.io/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); print('Error validating download (got %s instead of %s), please try manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by)
# ```
# - Click **cmd+shift+P** and use *Install Package*.

# Use mjhea0's settings:
# - [Preferences.sublime-settings
# ](https://github.com/mjhea0/sublime-setup-for-python/blob/master/dotfiles/Preferences.sublime-settings)
# - [Python.sublime-settings](https://github.com/mjhea0/sublime-setup-for-python/blob/master/dotfiles/Python.sublime-settings)
#     

# References:
# - https://realpython.com/blog/python/setting-up-sublime-text-3-for-full-stack-python-development/
# - https://github.com/mjhea0/sublime-setup-for-python

# In[ ]:

[Home](https://yang-zhang.github.io/)

