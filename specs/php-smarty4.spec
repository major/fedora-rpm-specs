%global composer_vendor  smarty
%global composer_project smarty

# "php": "^7.1 || ^8.0"
%global php_min_ver 7.1

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-smarty4
Summary:       Smarty - the compiling PHP template engine
Version:       4.5.6
Release:       2%{?dist}
License:       LGPL-3.0-only
URL:           http://www.smarty.net
# Github tarball doesn't include tests
#Source0:       https://github.com/smarty-php/smarty/archive/v%%{version}/smarty-%%{version}.tar.gz
Source0:       smarty-%{version}.tar.gz
Source1:       make_smarty_tarball.sh

BuildArch:     noarch
## Autoloader
BuildRequires: php-fedora-autoloader-devel
# composer.json
BuildRequires: php(language) >= %{php_min_ver}
# Library version value check
BuildRequires: php-cli
# Tests
%if 0%{?fedora}
BuildRequires: phpunit8
BuildRequires: php-pecl-apcu
BuildRequires: php-opcache
BuildRequires: php-memcache
%endif

Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 4.5.4)
Recommends:    php-pecl-apcu
Requires:      php-ctype
Requires:      php-mbstring
%if ! 0%{?el8}
Recommends:    php-memcache
Recommends:    php-memcached
%endif
Requires:      php-opcache
Requires:      php-pdo
Requires:      php-zlib

# php-{COMPOSER_VENDOR}-{COMPOSER_PROJECT}
Provides:      php-%{composer_vendor}-%{composer_project} = %{version}-%{release}
# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
Smarty is a template engine for PHP, facilitating the separation of
presentation (HTML/CSS) from application logic. This implies that PHP
code is application logic, and is separated from the presentation.

Autoloader: %{phpdir}/smarty4/autoload.php


%prep
%setup -q -n smarty-%{version}


%build
# Empty build section, nothing required


%install
: Generate autoloader
phpab --template fedora --output libs/autoload.php libs

mkdir -p %{buildroot}%{phpdir}
cp -rp libs %{buildroot}%{phpdir}/smarty4/


%check
: Library version value check
php -r '
    require_once "%{buildroot}%{phpdir}/smarty4/autoload.php";
    $version = Smarty::SMARTY_VERSION;
    echo "Version $version (expected %{version})\n";
    exit(version_compare("%{version}", "$version", "=") ? 0 : 1);
'
%if 0%{?fedora}
mkdir -p vendor
phpab --template fedora --output vendor/autoload.php libs
# cache tests
rm tests/UnitTests/CacheResourceTests/Apc/CacheResourceCustomApcTest.php
rm tests/UnitTests/CacheResourceTests/Memcache/CacheResourceCustomMemcacheTest.php
# network tests
rm tests/UnitTests/TemplateSource/TagTests/PluginFunction/PluginFunctionFetchTest.php
rm tests/UnitTests/SecurityTests/SecurityTest.php
phpunit8 \
  --verbose \
  --do-not-cache-result \
  --no-coverage \
  --testdox \
  tests
%endif


%files
%license LICENSE
%doc CHANGELOG.md README.md SECURITY.md docs/*
%doc composer.json
%{phpdir}/smarty4/


%changelog
* Fri Sep 12 2025 Xavier Bachelot <xavier@bachelot.org> - 4.5.6-2
- Sync specfile with php-Smarty

* Wed Aug 27 2025 Xavier Bachelot <xavier@bachelot.org> - 4.5.6-1
- Update to 4.5.6

* Mon Aug 19 2024 Xavier Bachelot <xavier@bachelot.org> - 4.5.4-1
- Initial package
