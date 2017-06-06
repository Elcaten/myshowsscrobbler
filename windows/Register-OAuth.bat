for /f "delims=" %%i in ('where python') do set python=%%i
REG ADD HKEY_CLASSES_ROOT\myshows /v "URL Protocol" /t REG_SZ /d "" /f
REG ADD HKEY_CLASSES_ROOT\myshows\shell\open\command /ve /d "\"%python%\" \"D:\Dropbox\Dev\myshowsscrobbler\myshowsscrobbler\fetchtoken.py\" %%1" /t REG_SZ /f