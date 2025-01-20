# remirepo/fedora spec file for php-composer-ca-bundle
#
# SPDX-FileCopyrightText:  Copyright 2016-2025 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

%bcond_without       tests

%global gh_commit    08c50d5ec4c6ced7d0271d2862dec8c1033283e6
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     composer
%global gh_project   ca-bundle
%global php_home     %{_datadir}/php

Name:           php-composer-ca-bundle
Version:        1.5.5
Release:        2%{?dist}
Summary:        Lets you find a path to the system CA

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
# git snapshot to get everything, despite .gitattributes
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

# Never bundle a CA file
Patch0:         %{name}-rpm.patch

BuildArch:      noarch
%if %{with tests}
BuildRequires:  php(language) >= 7.2
BuildRequires:  php-openssl
BuildRequires:  php-pcre
BuildRequires:  php-cli
# From composer.json, "require": {
#        "symfony/phpunit-bridge": "^8 || ^9",
#        "phpstan/phpstan": "^1.10",
#        "psr/log": "^1.0",
#        "symfony/process": "^4.0 || ^5.0 || ^6.0 || ^7.0"
BuildRequires:  phpunit10
# Autoloader
BuildRequires:  php-composer(fedora/autoloader)
# ca-certificates
BuildRequires:  %{_sysconfdir}/pki/tls/certs/ca-bundle.crt
%endif

# From composer.json, "require": {
#        "ext-openssl": "*",
#        "ext-pcre": "*",
#        "php": "^7.2 || ^8.0"
Requires:       php(language) >= 7.2
Requires:       php-openssl
Requires:       php-pcre
# From phpcompatinfo report for version 1.0.3
#nothing
# Autoloader
Requires:       php-composer(fedora/autoloader)
# ca-certificates
Requires:       %{_sysconfdir}/pki/tls/certs/ca-bundle.crt

Provides:       php-composer(%{gh_owner}/%{gh_project}) = %{version}


%description
Small utility library that lets you find a path to the system CA bundle.

Autoloader: %{php_home}/Composer/CaBundle/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

%patch -P0 -p0 -b .rpm
find src -name \*.rpm -exec rm {} \;

cat << 'EOF' | tee src/autoload.php
<?php
/* Autoloader for %{gh_owner}/%{gh_project} and its dependencies */

require_once '%{php_home}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Composer\\CaBundle\\', __DIR__);
EOF


%build
# Empty build section, most likely nothing required.


%install
: Library
mkdir -p   %{buildroot}%{php_home}/Composer/
cp -pr src %{buildroot}%{php_home}/Composer/CaBundle


%check
%if %{with tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{php_home}/Composer/CaBundle/autoload.php';
EOF

ret=0
%{_bindir}/phpunit10 --migrate-configuration

for cmd in php php81 php82 php83 php84; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit10 --no-coverage || ret=1
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
%dir %{php_home}/Composer
     %{php_home}/Composer/CaBundle


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jan  9 2025 Remi Collet <remi@remirepo.net> - 1.5.5-1
- update to 1.5.5 (no change)
- re-license spec file to CECILL-2.1

* Thu Nov 28 2024 Remi Collet <remi@remirepo.net> - 1.5.4-1
- update to 1.5.4 (no change)

* Mon Nov  4 2024 Remi Collet <remi@remirepo.net> - 1.5.3-1
- update to 1.5.3

* Wed Sep 25 2024 Remi Collet <remi@remirepo.net> - 1.5.2-1
- update to 1.5.2 (no change)

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul  9 2024 Remi Collet <remi@remirepo.net> - 1.5.1-1
- update to 1.5.1 (no change)

* Fri Mar 15 2024 Remi Collet <remi@remirepo.net> - 1.5.0-1
- update to 1.5.0
- raise dependency on PHP 7.2

* Thu Mar 14 2024 Remi Collet <remi@remirepo.net> - 1.4.2-1
- update to 1.4.2 (no change)

* Mon Feb 26 2024 Remi Collet <remi@remirepo.net> - 1.4.1-1
- update to 1.4.1

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 18 2023 Remi Collet <remi@remirepo.net> - 1.4.0-1
- update to 1.4.0 (no change)
- drop build dependencies on symfony/process and psr/log

* Thu Aug 31 2023 Remi Collet <remi@remirepo.net> - 1.3.7-1
- update to 1.3.7 (no change)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun  8 2023 Remi Collet <remi@remirepo.net> - 1.3.6-1
- update to 1.3.6 (no change)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 11 2023 Remi Collet <remi@remirepo.net> - 1.3.5-1
- update to 1.3.5 (no change)

* Wed Oct 12 2022 Remi Collet <remi@remirepo.net> - 1.3.4-1
- update to 1.3.4 (no change)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Remi Collet <remi@remirepo.net> - 1.3.3-1
- update to 1.3.3 (no change)

* Wed May 25 2022 Remi Collet <remi@remirepo.net> - 1.3.2-1
- update to 1.3.2 (no change)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Oct 30 2021 Remi Collet <remi@remirepo.net> - 1.3.1-1
- update to 1.3.1

* Wed Oct 27 2021 Remi Collet <remi@remirepo.net> - 1.3.0-1
- update to 1.3.0

* Fri Oct  1 2021 Remi Collet <remi@remirepo.net> - 1.2.11-1
- update to 1.2.11 (no change)
- allow Symfony 6

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun  8 2021 Remi Collet <remi@remirepo.net> - 1.2.10-1
- update to 1.2.10 (no change)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 12 2021 Remi Collet <remi@remirepo.net> - 1.2.9-1
- update to 1.2.9

* Mon Aug 24 2020 Remi Collet <remi@remirepo.net> - 1.2.8-1
- update to 1.2.8 (no change)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr  8 2020 Remi Collet <remi@remirepo.net> - 1.2.7-1
- update to 1.2.7

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 14 2020 Remi Collet <remi@remirepo.net> - 1.2.6-1
- update to 1.2.6

* Thu Dec 12 2019 Remi Collet <remi@remirepo.net> - 1.2.5-1
- update to 1.2.5

* Sun Sep  1 2019 Remi Collet <remi@remirepo.net> - 1.2.4-1
- update to 1.2.4 (no change)

* Sat Aug  3 2019 Remi Collet <remi@remirepo.net> - 1.2.3-1
- update to 1.2.3

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 Remi Collet <remi@remirepo.net> - 1.1.4-1
- update to 1.1.4 (no change)

* Thu Oct 18 2018 Remi Collet <remi@remirepo.net> - 1.1.3-1
- update to 1.1.3 (no change)

* Thu Aug  9 2018 Remi Collet <remi@remirepo.net> - 1.1.2-1
- update to 1.1.2 (no change)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 30 2018 Remi Collet <remi@remirepo.net> - 1.1.1-1
- update to 1.1.1 (no change)
- use range dependencies on F27+
- use phpunit6 on F27+

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 30 2017 Remi Collet <remi@remirepo.net> - 1.1.0-1
- Update to 1.1.0
- allow Symfony 2, 3 and 4

* Tue Nov 14 2017 Remi Collet <remi@remirepo.net> - 1.0.9-1
- Update to 1.0.9 (no change)

* Mon Sep 11 2017 Remi Collet <remi@remirepo.net> - 1.0.8-1
- Update to 1.0.8 (no change)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar  6 2017 Remi Collet <remi@remirepo.net> - 1.0.7-1
- Update to 1.0.7
- run upstream test suite

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Nov  3 2016 Remi Collet <remi@fedoraproject.org> - 1.0.6-1
- update to 1.0.6 (no change)

* Wed Nov  2 2016 Remi Collet <remi@fedoraproject.org> - 1.0.5-1
- update to 1.0.5 (no change)

* Thu Oct 20 2016 Remi Collet <remi@fedoraproject.org> - 1.0.4-2
- switch from symfony/class-loader to fedora/autoloader

* Mon Sep  5 2016 Remi Collet <remi@fedoraproject.org> - 1.0.4-1
- update to 1.0.4 (no change)

* Tue Jul 19 2016 Remi Collet <remi@fedoraproject.org> - 1.0.3-1
- update to 1.0.3

* Sat Apr 30 2016 Remi Collet <remi@fedoraproject.org> - 1.0.2-1
- initial package, version 1.0.2

