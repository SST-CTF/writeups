# Voting!!!
###### 400 Points

### Problem
When Uncle Stan decides to run for mayor, Dipper and Mabel had to deal with the transformation of his hapless uncle in this candidate. But anyone can enter the pre-election headquarters, just also need to get some votes... [Link to voting page]

### Description
Clicking the link brings us to a simple voter login page, obvisously we don't have an account yet so we register for one. Registration asks for a username, password, email, and a CAPTCHA. Looking at the source, we can see the captcha contents are stored in plaintext in the HTML, interesting. At this point we create an account and click the email confirmation link, and login. We have one vote, if we don't vote for anyone that vote is retained. Another important observation is that clicking the cofirmation link resets the # of votes to one. 

Using this fact to craft a script that automatically spams the confirmation link. This is an obscure and terrible scripting language on macs called 'AppleScript', I'm sorry.

```AppleScript
to goToWebPage(theWebPage)
tell application "Safari"
activate
set URL of document 1 to theWebPage
end tell
end goToWebPage

to closeWebPage(thePageName)
tell application "Safari"
repeat with t in tabs of windows
tell t
if name starts with thePageName then close
end tell
end repeat
end tell
end closeWebPage

repeat
goToWebPage("http://10.0.1.123:8888/voting/activate?token=%242b%2412%24dTwbV8DS.0cCi0gQXXmG..1zbv7VJ.9V53Z9IUnPhdSMM.hf5101C&user=z1")
delay 0.5
closeWebPage("Login page")
end repeat
```
In another tab I setup an [autoclicking bot](http://www.murgaa.com/auto-clicker-mac/) pointed at our user profile. After about five minutes of AFK we had collected about 250 points. Logging into the user profile gave us the flag: **:(**
