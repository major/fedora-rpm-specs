# remirepo/fedora spec file for php-sebastian-exporter4
#
# Copyright (c) 2013-2022 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_without       tests

%global gh_commit    ac230ed27f0f98f597c8a2b6eb7ac563af5e5b9d
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   exporter
# Packagist
%global pk_vendor    sebastian
%global pk_project   %{gh_project}
# Namespace
%global ns_vendor    SebastianBergmann
%global ns_project   Exporter
%global major        4
%global php_home     %{_datadir}/php
%global pear_name    Exporter
%global pear_channel pear.phpunit.de

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        4.0.5
Release:        1%{?dist}
Summary:        Export PHP variables for visualization, version %{major}

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
BuildRequires:  php(language) >= 7.3
BuildRequires:  php-fedora-autoloader-devel >= 1.0.0
%if %{with tests}
# from composer.json, "require-dev": {
#        "phpunit/phpunit": "^9.3",
#        "ext-mbstring": "*"
BuildRequires:  phpunit9 >= 9.3
BuildRequires:  php-mbstring
BuildRequires:  (php-composer(%{pk_vendor}/recursion-context) >= 4.0 with php-composer(%{pk_vendor}/recursion-context) < 5)
%endif

# from composer.json
#        "php": ">=7.3",
#        "sebastian/recursion-context": "^4.0"
Requires:       php(language) >= 7.3
Requires:       (php-composer(%{pk_vendor}/recursion-context) >= 4.0 with php-composer(%{pk_vendor}/recursion-context) < 5)
# from phpcompatinfo report for version 4.0.0
Requires:       php-mbstring
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
Provides the functionality to export PHP variables for visualization.


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
# generate the Autoloader
phpab --template fedora --output src/autoload.php src

cat <<EOF | tee -a src/autoload.php
// Dependency' autoloader
require_once '%{php_home}/%{ns_vendor}/RecursionContext4/autoload.php';
EOF


%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}


%if %{with tests}
%check
mkdir vendor
touch vendor/autoload.php

: Run upstream test suite
ret=0
for cmd in php php74 php80 php81 php82; do
  if which $cmd; then
    $cmd -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php \
      %{_bindir}/phpunit9  --verbose || ret=1
  fi
done
exit $ret
%endif


%files
%license LICENSE
%doc README.md
%doc composer.json
%{php_home}/%{ns_vendor}/%{ns_project}%{major}


%changelog
* Wed Sep 14 2022 Remi Collet <remi@remirepo.net> - 4.0.5-1
- update to 4.0.5

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 15 2021 Remi Collet <remi@remirepo.net> - 4.0.4-1
- update to 4.0.4

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 28 2020 Remi Collet <remi@remirepo.net> - 4.0.3-1
- update to 4.0.3 (no change)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 29 2020 Remi Collet <remi@remirepo.net> - 4.0.2-1
- update to 4.0.2

* Tue Jun 16 2020 Remi Collet <remi@remirepo.net> - 4.0.1-1
- update to 4.0.1
- sources from git snapshot

* Fri Feb  7 2020 Remi Collet <remi@remirepo.net> - 4.0.0-1
- update to 4.0.0
- raise dependency on PHP 7.3
- raise dependency on sebastian/recursion-context 4
- rename to php-sebastian-exporter4
- move to /usr/share/php/SebastianBergmann/Exporter4

* Sun Sep 15 2019 Remi Collet <remi@remirepo.net> - 3.1.2-1
- update to 3.1.2

* Mon Aug 12 2019 Remi Collet <remi@remirepo.net> - 3.1.1-1
- update to 3.1.1

* Thu Dec  6 2018 Remi Collet <remi@remirepo.net> - 3.1.0-5
- cleanup for EL-8

* Tue Feb  6 2018 Remi Collet <remi@remirepo.net> - 3.1.0-3
- use range dependencies on F27+

* Mon Apr  3 2017 Remi Collet <remi@remirepo.net> - 3.1.0-1
- Update to 3.1.0

* Fri Mar  3 2017 Remi Collet <remi@fedoraproject.org> - 3.0.0-1
- update to 3.0.0
- rename to php-sebastian-exporter3
- raise dependency on PHP 7
- raise dependency on recursion-context 3

* Tue Nov 22 2016 Remi Collet <remi@fedoraproject.org> - 2.0.0-1
- update to 2.0.0
- raise dependency on sebastian/recursion-context 2.0
- switch to fedora/autoloader

* Fri Jun 17 2016 Remi Collet <remi@fedoraproject.org> - 1.2.2-1
- update to 1.2.2
- run test suite with both PHP 5 and 7 when available

* Sun Jul 26 2015 Remi Collet <remi@fedoraproject.org> - 1.2.1-1
- update to 1.2.1 (only CS)

* Fri Jan 30 2015 Remi Collet <remi@fedoraproject.org> - 1.2.0-1
- update to 1.2.0

* Sat Jan 24 2015 Remi Collet <remi@fedoraproject.org> - 1.1.0-1
- update to 1.1.0
- add dependency on sebastian/recursion-context

* Sun Oct  5 2014 Remi Collet <remi@fedoraproject.org> - 1.0.2-1
- update to 1.0.2
- enable test suite

* Fri Jul 18 2014 Remi Collet <remi@fedoraproject.org> - 1.0.1-4
- add composer dependencies

* Wed Apr 30 2014 Remi Collet <remi@fedoraproject.org> - 1.0.1-2
- cleanup pear registry

* Sun Apr  6 2014 Remi Collet <remi@fedoraproject.org> - 1.0.1-1
- update to 1.0.1
- get sources from github
- run test suite when build --with tests

* Sun Oct 20 2013 Remi Collet <remi@fedoraproject.org> - 1.0.0-2
- rename to lowercase

* Thu Sep 12 2013 Remi Collet <remi@fedoraproject.org> - 1.0.0-1
- initial package
