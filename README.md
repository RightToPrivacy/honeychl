# honeychl- a simple script with a simple purpose.

Just as learning how hackers make attacks provides the best understanding of network security, learning how privacy is compromised provides us the best lesson in protecting it.

Part of a coming guide/video set to provide an example of a targeted privacy breach. 

Script logs specific time/ip address "honeypot calls home" to a webserver (target loads the remotely hosted embedded content such as simple picture in local downloaded file)- An example of targeted privacy breach.

Backstory: Tor privacy is only as good as the practices/OPSEC in place (operational security).

What is Tor? A popular web browser allowing users to connect to websites through multiple proxies while encrypting the middle connection. It gives many a false sense of privacy.

One area of concern is downloading files over Tor. When you download content over tor (ex: document/guide/program), it is important to note certain filetypes may contain embedded code which connect to a server (aka "calling home"). This has been a known tactic for revealing the identity of users.

This is why it is suggested to only open files downloaded over tor in a secure environment, aka a "sandbox" or even something as simple as using something like Parrot's Anonsurf (routes all network connections through tor including Libre Office if speaking of documents (tested))

Example 1): You want to protect your company/software/documents. You keep embedded "call home" code in all important documents. This way you know who is accessing them.

Example 2): Maybe in an investigation you would send an email to the targeted email addresses including html tag to remotely load an image. Something simple that looks like it belongs in the email like:
<img src="http://company.server/images/logo.jpg">

### HOWTO:

Store honeychl locally on the webserver. When run it checks latest apache webserver log for ip addresses/times who access our remotely hosted embedded code and log those to a file. You can then for example access the file through the webserver.
