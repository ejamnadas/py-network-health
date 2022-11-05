import ping

# ruckus zd
ping.check_ping('172.16.34.66', 'ruckus zd')

# internet connectivty check
ping.check_ping('8.8.8.8', 'internet connectivity check')

# internet connectivty check (dns works)
ping.check_ping('google.com', 'internet connectivity and DNS check')