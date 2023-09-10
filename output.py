# use an appropriate path to import
from verifier.verifier import Verifier

# Use normal SMTP to connect to the server
normal_verifier = Verifier(source_addr='user@example.com') # No proxy
results = normal_verifier.verify('myemail@example.com')

# Use socks proxy to connect over SMTP


socks_verifier =  Verifier(
    source_addr='user@example.com',
    proxy_type='socks5',
    proxy_addr='socks5.your-proxy-provider.com',
    proxy_port=1080,
    proxy_username='funky-username',
    proxy_password='crazy-password'
)
results = socks_verifier.verify('myemail@example.com')