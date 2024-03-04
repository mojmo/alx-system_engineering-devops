# This Puppet manifest configures a new Ubuntu machine to meet the specified requirements:
# 1. Installs nginx on a web server
# 2. Sets nginx to listen on port 80
# 3. creating a custom HTTP header response

exec { 'update packages':
  provider => 'shell',
  command  => 'sudo apt-get -y update',
}

package { 'nginx':
    ensure   => 'present',
    provider => apt,
}

file_line { 'add new HTTP header':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => "add_header X-Served-By \"${hostname}\";"
}

exec {'restart_server':
    provider => shell,
    command  => 'sudo service nginx restart',
}
