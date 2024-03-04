# This Puppet manifest configures a new Ubuntu machine to meet the specified requirements:
# 1. Installs nginx on a web server
# 2. Sets nginx to listen on port 80
# 3. creating a custom HTTP header response

exec { 'update packages':
  provider => 'shell',
  command  => 'sudo apt-get -y update',
}

package { 'nginx':
    ensure => 'present',
}

exec {'root_page':
    provider    => shell,
    command     => 'sudo echo Hello World! > /var/www/html/index.html',
}

exec { 'add_header':
    provider    => shell,
    command     => 'HOSTNAME=$(hostname); sudo sed -i "s/listen 80 default_server;/listen 80 default_server;\\n\tadd_header X-Served-By "$HOSTNAME";/" /etc/nginx/sites-available/default',
}


exec {'restart_server':
    provider    => shell,
    command     => 'sudo service nginx restart',
}

