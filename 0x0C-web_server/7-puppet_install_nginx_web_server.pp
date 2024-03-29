# Configures a new Ubuntu machine to respect following requirements
# Requirements:
#   Install nginx on your web-01 server
#   Nginx should be listening on port 80
#   When querying Nginx at its root / with a GET request (requesting a page) using curl,
#   it must return a page that contains the string Hello World!
#   Configure your Nginx server so that /redirect_me is redirecting to another page.
#   The redirection must be a “301 Moved Permanently”

package { 'nginx':
    ensure => 'present',
}

exec {'root_page':
    provider    => shell,
    command     => 'sudo echo Hello World! > /var/www/html/index.html',
}

exec { 'redirect':
    provider    =>  shell,
    command     =>  'sudo sed -i "s/listen 80 default_server;/listen 80 default_server;\\n\\tlocation \/redirect_me {\\n\\t\\treturn 301 https:\/\/oluwaseundasilva.hashnode.dev\/;\\n\\t}/" /etc/nginx/sites-available/default',
}

exec {'restart_server':
    provider    => shell,
    command     => 'sudo service nginx restart',
}

