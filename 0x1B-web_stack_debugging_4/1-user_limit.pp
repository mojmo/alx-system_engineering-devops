# Increase the file limit for the holberton user in /etc/security/limits.conf

# Increase the soft file limit for the holberton user in /etc/security/limits.conf
exec { 'increase-soft-file-limit-for-holberton-user':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => ['/usr/local/bin/', '/bin/'],
}

# Increase the hard file limit for the holberton user in /etc/security/limits.conf
exec { 'increase-hard-file-limit-for-holberton-user':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => ['/usr/local/bin/', '/bin/'],
}

