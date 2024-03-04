# This Puppet manifest configures a new Ubuntu machine to meet the specified requirements:
# 1. Installs nginx on a web server
# 2. Sets nginx to listen on port 80
# 3. creating a custom HTTP header response

package { 'nginx':
    ensure => 'present',
}

file_line { 'add new HTTP header':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'add_header X-Served-By $hostname;'
}

service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx']
}
