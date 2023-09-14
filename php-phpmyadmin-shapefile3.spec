# remirepo/fedora spec file for php-phpmyadmin-shapefile3
#
# Copyright (c) 2017-2023 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%global gh_commit    c8240ec25d04c8d03ca83ab7eed7aec165b57a1e
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     phpmyadmin
%global gh_project   shapefile
%global with_tests   0%{!?_without_tests:1}
%global ns_vendor    PhpMyAdmin
%global ns_project   ShapeFile
%global major        3

Name:           php-%{gh_owner}-%{gh_project}%{major}
Version:        3.0.2
Release:        1%{?dist}
Summary:        ESRI ShapeFile library for PHP, version %{major}

License:        GPL-2.0-or-later
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{?gh_short}.tar.gz

BuildArch:      noarch
%if %{with_tests}
BuildRequires:  php(language) >= 7.1
# For tests, from composer.json "require-dev": {
#        "phpmyadmin/coding-standard": "^3.0.0",
#        "phpstan/phpstan": "^1.4.10",
#        "phpstan/phpstan-phpunit": "^1.0",
#        "phpunit/phpunit": "^7.5 || ^8.5 || ^9.6 || ^10.3"
%global phpunit %{_bindir}/phpunit10
BuildRequires:  phpunit10 >= 10.3
%endif
# For autoloader
BuildRequires:  php-composer(fedora/autoloader)

# From composer.json, "require": {
#        "php": "^7.1 || ^8.0"
Requires:       php(language) >= 7.1
# From phpcompatinfo report for 1.2
#   nothing
# From composer.json, "suggest": {
#        "ext-dbase": "For dbf files parsing"
%if 0%{?fedora} >= 21
Suggests:       php-dbase
%endif
# For generated autoloader
Requires:       php-composer(fedora/autoloader)

# Composer
Provides:       php-composer(%{gh_owner}/%{gh_project}) = %{version}


%description
Currently the 2D and 3D variants except MultiPatch of the ShapeFile format
as defined in [1].

The library currently supports reading and editing of ShapeFiles and the
Associated information (DBF file). There are a lot of things that can be
improved in the code, if you are interested in developing, helping with the
documentation, making translations or offering new ideas please contact us.

[1] https://www.esri.com/library/whitepapers/pdfs/shapefile.pdf

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/* Autoloader for %{name} and its dependencies */
require_once '%{_datadir}/php/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\%{ns_project}\\', __DIR__);
AUTOLOAD


%install
: Library
mkdir -p   %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr src %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}


%check
%if %{with_tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require '%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php';
EOF

ret=0
for cmd in "php %{phpunit}" "php80 %{_bindir}/phpunit9" php81 php82 php83; do
  if which $cmd; then
    set $cmd
    $1 ${2:-%{_bindir}/phpunit10} --no-coverage || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc composer.json
%doc *.md
%dir %{_datadir}/php/%{ns_vendor}/
     %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}


%changelog
* Tue Sep 12 2023 Remi Collet <remi@remirepo.net> - 3.0.2-1
- update to 3.0.2

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Feb  8 2021 Remi Collet <remi@remirepo.net> - 3.0.1-1
- update to 3.0.1
- rename to php-phpmyadmin-shapefile3
- install in /usr/share/php/PhpMyAdmin/ShapeFile3
- raise dependency on PHP 7.1
- switch to phpunit9

* Mon May 15 2017 Remi Collet <remi@remirepo.net> - 2.1-1
- Update to 2.1

* Mon Jan 23 2017 Remi Collet <remi@remirepo.net> - 2.0-1
- update to 3.0 with vendor namespace

* Sat Jan 21 2017 Remi Collet <remi@remirepo.net> - 1.2-1
- initial package

