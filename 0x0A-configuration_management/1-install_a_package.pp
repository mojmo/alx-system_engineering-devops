# This Puppet manifest ensures that Flask version 2.1.0 is installed using pip3

exec {'install-flask':
require => Exec['werkzeug-installed'],
command => '/usr/bin/pip3 install flask==2.1.0'
}

exec {'werkzeug-installed':
command => '/usr/bin/pip3 install werkzeug==2.1.1'
}
