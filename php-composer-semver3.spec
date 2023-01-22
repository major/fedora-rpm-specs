# remirepo/fedora spec file for php-composer-semver3
#
# Copyright (c) 2015-2022 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_without       tests

%global gh_commit    3953f23262f2bff1919fc82183ad9acb13ff62c9
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
#global gh_date      20150717
%global gh_owner     composer
%global gh_project   semver
%global ns_vendor    Composer
%global ns_project   Semver
%global php_home     %{_datadir}/php
%global major        3

Name:           php-%{gh_owner}-%{gh_project}%{major}
Version:        3.3.2
Release:        3%{?gh_date:.%{gh_date}git%{gh_short}}%{?dist}
Summary:        Semver library version %{major}

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
# git snapshot to get upstream test suite
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
%if %{with tests}
# For tests
BuildRequires:  php(language) >= 5.3.2
BuildRequires:  php-pcre
BuildRequires:  php-spl
# From composer.json,     "require-dev": {
#        "symfony/phpunit-bridge": "^4.2 || ^5",
#        "phpstan/phpstan": "^1.4"
%global         phpunit /usr/bin/phpunit
BuildRequires:  %{phpunit}
# Autoloader
BuildRequires:  php-fedora-autoloader-devel
%endif

# From composer.json, "require": {
#        "php": "^5.3.2 || ^7.0 || ^8.0",
Requires:       php(language) >= 5.3.2
# From phpcompatinfo report for version 3.0.0
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{gh_owner}/%{gh_project}) = %{version}


%description
Semver library version %{major} that offers utilities, version constraint
parsing and validation.

Originally written as part of composer/composer, now extracted and
made available as a stand-alone library.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
: Generate classmap autoloader
phpab --template fedora --output src/autoload.php src


%install
: Library
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}/
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}


%check
%if %{with tests}
ret=0
for cmd in php php74 php80 php81; do
  if which $cmd; then
    $cmd %{phpunit} \
      --bootstrap %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php \
      --verbose || ret=1
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
%dir %{php_home}/%{ns_vendor}
     %{php_home}/%{ns_vendor}/%{ns_project}%{major}


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Apr  4 2022 Remi Collet <remi@remirepo.net> - 3.3.2-1
- update to 3.3.2

* Wed Mar 16 2022 Remi Collet <remi@remirepo.net> - 3.3.1-1
- update to 3.3.1

* Tue Mar 15 2022 Remi Collet <remi@remirepo.net> - 3.3.0-1
- update to 3.3.0

* Sat Feb  5 2022 Remi Collet <remi@remirepo.net> - 3.2.9-1
- update to 3.2.9

* Fri Feb  4 2022 Remi Collet <remi@remirepo.net> - 3.2.8-1
- update to 3.2.8

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan  4 2022 Remi Collet <remi@remirepo.net> - 3.2.7-1
- update to 3.2.7

* Mon Oct 25 2021 Remi Collet <remi@remirepo.net> - 3.2.6-1
- update to 3.2.6

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue May 25 2021 Remi Collet <remi@remirepo.net> - 3.2.5-1
- update to 3.2.5

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 13 2020 Remi Collet <remi@remirepo.net> - 3.2.4-1
- update to 3.2.4

* Fri Nov 13 2020 Remi Collet <remi@remirepo.net> - 3.2.3-1
- update to 3.2.3

* Thu Oct 15 2020 Remi Collet <remi@remirepo.net> - 3.2.2-1
- update to 3.2.2

* Mon Sep 28 2020 Remi Collet <remi@remirepo.net> - 3.2.1-1
- update to 3.2.1

* Wed Sep  9 2020 Remi Collet <remi@remirepo.net> - 3.2.0-1
- update to 3.2.0

* Wed Sep  9 2020 Remi Collet <remi@remirepo.net> - 3.1.0-1
- update to 3.1.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun  3 2020 Remi Collet <remi@remirepo.net> - 3.0.0-1
- update to 3.0.0
- rename to php-composer-semver3
- install in /usr/share/php/Composer/Semver3

* Wed Apr 22 2020 Remi Collet <remi@remirepo.net> - 2.0.0-1
- update to 2.0.0
- rename to php-composer-semver2
- install in /usr/share/php/Composer/Semver2
- switch to classmap autoloader

* Tue Jan 14 2020 Remi Collet <remi@remirepo.net> - 1.5.1-1
- update to 1.5.1

* Wed Mar 20 2019 Remi Collet <remi@remirepo.net> - 1.5.0-1
- update to 1.5.0

* Thu Oct 20 2016 Remi Collet <remi@fedoraproject.org> - 1.4.2-2
- switch from symfony/class-loader to fedora/autoloader

* Thu Sep  1 2016 Remi Collet <remi@fedoraproject.org> - 1.4.2-1
- update to 1.4.2

* Thu Jun  2 2016 Remi Collet <remi@fedoraproject.org> - 1.4.1-1
- update to 1.4.1

* Wed Mar 30 2016 Remi Collet <remi@fedoraproject.org> - 1.4.0-1
- update to 1.4.0

* Fri Feb 26 2016 Remi Collet <remi@fedoraproject.org> - 1.3.0-1
- update to 1.3.0
- run test suite with both PHP 5 and 7 when available

* Tue Nov 10 2015 Remi Collet <remi@fedoraproject.org> - 1.2.0-1
- update to 1.2.0

* Wed Nov  4 2015 Remi Collet <remi@fedoraproject.org> - 1.1.0-1
- update to 1.1.0

* Sun Oct  4 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-1
- initial package, version 1.0.0
