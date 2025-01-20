# remirepo/fedora spec file for php-icewind-streams
#
# Copyright (c) 2015-2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
# Github information
%global gh_commit    cb2bd3ed41b516efb97e06e8da35a12ef58ba48b
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     icewind1991
%global gh_project   Streams
# Packagist information
%global pk_vendor    icewind
%global pk_name      streams
# Namespace information
%global ns_vendor    Icewind
%global ns_name      Streams

Name:           php-%{pk_vendor}-%{pk_name}
Version:        0.7.8
Release:        2%{?dist}
Summary:        A set of generic stream wrappers

# See SPDX-License-Identifier in src tree
License:        MIT AND AGPL-3.0-or-later
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{url}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch
# For tests
# because of PHPUnit 9
BuildRequires:  php(language) >= 7.3
# From composer.json, "require-dev": {
#               "phpunit/phpunit": "^9",
#               "friendsofphp/php-cs-fixer": "^2",
#               "phpstan/phpstan": "^0.12"
BuildRequires:  phpunit9
BuildRequires:  php-composer(theseer/autoload)
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, "require": {
#      "php": ">=7.1"
Requires:       php(language) >= 7.1
# From phpcompatinfo report for version 0.7.2
Requires:       php-hash
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_name}) = %{version}


%description
Generic stream wrappers for php.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_name}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
: Generate classmap autoloader
%{_bindir}/phpab --template fedora --output src/autoload.php src


%install
# Restore PSR-0 tree
mkdir -p   %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr src %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_name}


%check
cd tests
: Generate a simple autoloader for test suite
%{_bindir}/phpab --output bootstrap.php .
echo "require '%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_name}/autoload.php';" >> bootstrap.php

: Run the test suite
ret=0
for cmd in php php80 php81 php82; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit9 || ret=1
  fi
done
exit $ret


%files
%license LICENSE.txt
%license LICENSES/*txt
%doc composer.json
%doc *.md
%dir %{_datadir}/php/%{ns_vendor}
     %{_datadir}/php/%{ns_vendor}/%{ns_name}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Dec  6 2024 Remi Collet <remi@remirepo.net> - 0.7.8-1
- update to 0.7.8

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Mar 17 2023 Remi Collet <remi@remirepo.net> - 0.7.7-1
- update to 0.7.7

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 10 2022 Remi Collet <remi@remirepo.net> - 0.7.6-1
- update to 0.7.6

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 15 2021 Remi Collet <remi@remirepo.net> - 0.7.5-1
- update to 0.7.5

* Mon Mar 15 2021 Remi Collet <remi@remirepo.net> - 0.7.4-1
- update to 0.7.4

* Wed Mar  3 2021 Remi Collet <remi@remirepo.net> - 0.7.3-1
- update to 0.7.3
- raise dependency on PHP 7.1 (7.3 for build)
- switch to phpunit9

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr  9 2020 Remi Collet <remi@remirepo.net> - 0.7.2-1
- update to 0.7.2
- raise dependency on PHP 5.6
- switch to classmap autoloader

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 18 2019 Remi Collet <remi@remirepo.net> - 0.7.1-1
- update to 0.7.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 25 2018 Remi Collet <remi@remirepo.net> - 0.6.1-1
- update to 0.6.1

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Remi Collet <remi@remirepo.net> - 0.6.0-1
- Update to 0.6.0

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec  5 2016 Remi Collet <remi@fedoraproject.org> - 0.5.2-1
- update to 0.5.2

* Thu Oct 27 2016 Remi Collet <remi@fedoraproject.org> - 0.5.1-1
- update to 0.5.1
- switch from symfony/class-loader to fedora/autoloader

* Fri Jun  3 2016 Remi Collet <remi@fedoraproject.org> - 0.4.1-1
- update to 0.4.1

* Thu Mar 17 2016 Remi Collet <remi@fedoraproject.org> - 0.4.0-1
- update to 0.4.0

* Thu Mar 17 2016 Remi Collet <remi@fedoraproject.org> - 0.3.0-1
- version 0.3.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep  1 2015 Remi Collet <remi@fedoraproject.org> - 0.2.0-1
- initial package, version 0.2.0
