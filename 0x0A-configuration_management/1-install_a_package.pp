# Installing a package using puppet
package { 'flask':
  ensure   => '2.1.0',
  provider => 'python-pip3',
}
