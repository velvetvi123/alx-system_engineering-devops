# Setup New Ubuntu server with nginx
# and add a custom HTTP header

exec { 'update system':
        command => '/usr/bin/apt-get update',
}

package { 'nginx':
	ensure => 'installed',
	require => Exec['update system']
}

file {'/var/www/html/index.html':
	content => 'Hello World!'
}

exec {'redirect_me':
	command => 'new_string="server_name _;\n\trewrite ^\/redirect_me https:\/\/github.com\/velvetvi123 permanent;"
sudo sed -i "s/server_name _;/$new_string/" /etc/nginx/sites-enabled/default',
	provider => 'shell'
}

exec {'HTTP header':
	command => 'sed -i "/server_name _/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-enabled/default',
	provider => 'shell'
}

service {'nginx':
	ensure => running,
	require => Package['nginx']
}
