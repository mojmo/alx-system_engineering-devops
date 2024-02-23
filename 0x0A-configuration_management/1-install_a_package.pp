# This Puppet manifest ensures that Flask version 2.1.0 is installed using pip3

exec { 'install flask':
    command => '/usr/bin/pip3 install Flask==2.1.0',
}
