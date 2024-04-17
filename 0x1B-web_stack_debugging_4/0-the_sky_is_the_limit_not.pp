# Increase the ULIMIT in the Nginx default configuration file

# Increase the ULIMIT in the Nginx default configuration file
exec { 'fix_for_nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
}

# Restart Nginx to apply the new ULIMIT
exec { 'nginx-restart':
  command => '/etc/init.d/nginx restart',
  path    => '/etc/init.d/'
}

