#
# Fedora spec file for php-nikic-fast-route
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries

%bcond_without tests

%global gh_commit    181d480e08d9476e61381e04a71b34dc0432e812
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     nikic
%global gh_project   FastRoute
%global pk_project   fast-route
%global php_home     %{_datadir}/php

Name:           php-%{gh_owner}-%{pk_project}
Version:        1.3.0
Release:        9%{?dist}
Summary:        Fast implementation of a regular expression based router

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source:         https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch
%if %{with tests}
# For tests
BuildRequires:  php(language) >= 5.4
BuildRequires:  php-pcre
BuildRequires:  php-spl
# From composer.json, "require-dev": {
#        "phpunit/phpunit": "^4.8.35|~5.7"
BuildRequires:  php-composer(phpunit/phpunit) >= 4.8.35
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, "require": {
#        "php": ">=5.4",
Requires:       php(language) >= 5.4
# From phpcompatinfo report for version 1.3.0
Requires:       php-pcre
Requires:       php-spl
# Autoloader
BuildRequires:  php-composer(fedora/autoloader)

Provides:       php-composer(%{gh_owner}/%{pk_project}) = %{version}


%description
Fast implementation of a regular expression based router.

Documentation:
http://nikic.github.io/2014/02/18/Fast-request-routing-using-regular-expressions.html

Autoloader: %{php_home}/%{gh_project}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
require_once __DIR__ . '/functions.php';
EOF

phpab --template fedora --output test/bootstrap.php test
cat << 'EOF' | tee -a test/bootstrap.php
require_once '%{buildroot}%{php_home}/%{gh_project}/autoload.php';
EOF


%install
#: Library
mkdir -p                %{buildroot}%{php_home}
cp -pr src              %{buildroot}%{php_home}/%{gh_project}


%check
%if %{with tests}
# ensure tests are not ran against local sources
rm -rf src

: Run upstream test suite
ret=0
for cmd in php php72 php73 php74 php80; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit --verbose || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif


%files
%license LICENSE
%doc composer.json
%doc *.md
%{php_home}/%{gh_project}


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Dec 21 2020 Remi Collet <remi@remirepo.net> - 1.3.0-6
- add classmap autoloader

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 14 2018 Remi Collet <remi@remirepo.net> - 1.3.0-1
- Update to 1.3.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Johan Cwiklinski <johan AT x-tnd DOT be> - 1.2.0-1
- Last upstream release

* Mon Jan 02 2017 Johan Cwiklinski <johan AT x-tnd DOT be> - 1.1.0-2
- Bump version

* Mon Jan 02 2017 Johan Cwiklinski <johan AT x-tnd DOT be> - 1.1.0-1
- Last upstream release

* Sat Jun 25 2016 Johan Cwiklinski <johan AT x-tnd DOT be> - 1.0.1-1
- Last upstream release

* Fri May 06 2016 Johan Cwiklinski <johan AT x-tnd DOT be> - 1.0.0-2
- Fix package name

* Fri May 06 2016 Johan Cwiklinski <johan AT x-tnd DOT be> - 1.0.0-1
- Initial packaging
