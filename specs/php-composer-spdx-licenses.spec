# remirepo/fedora spec file for php-composer-spdx-licenses
#
# Copyright (c) 2015-2023 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    560bdcf8deb88ae5d611c80a2de8ea9d0358cc0a
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
#global gh_date      20150717
%global gh_owner     composer
%global gh_project   spdx-licenses
%global php_home     %{_datadir}/php
%bcond_without       tests

Name:           php-composer-spdx-licenses
Version:        1.5.8
Release:        5%{?gh_date:.%{gh_date}git%{gh_short}}%{?dist}
Summary:        SPDX licenses list and validation library

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
# git snapshot to get upstream test suite
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

# Resources path
Patch0:         %{name}-rpm.patch

BuildArch:      noarch
%if %{with tests}
# For tests
BuildRequires:  php(language) >= 5.3.2
BuildRequires:  php-json
BuildRequires:  php-pcre
BuildRequires:  php-spl
# From composer.json, "require-dev": {
#        "phpunit/phpunit": "phpunit/phpunit": "^4.8.35 || ^5.7 || 6.5 - 7",
# ignore min version, test suite passes with 9.6.13
BuildRequires: phpunit9
# Autoloader
BuildRequires:  php-composer(fedora/autoloader)
%endif

# From composer.json, "require": {
#        "php": "^5.3.2 || ^7.0 || ^8.0",
Requires:       php(language) >= 5.3.2
# From phpcompatinfo report for version 1.6.0 (SpdxLicenses.php only)
Requires:       php-json
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{gh_owner}/%{gh_project}) = %{version}


%description
SPDX licenses list and validation library.

Originally written as part of composer/composer,
now extracted and made available as a stand-alone library.


%prep
%setup -q -n %{gh_project}-%{gh_commit}

%patch -P0 -p0 -b .rpm
find . -name \*.rpm -delete -print


%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/* Autoloader for %{name} and its dependencies */
require_once '%{_datadir}/php/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Composer\\Spdx\\', __DIR__);
AUTOLOAD


%install
: Library
pushd src
for fic in *
do
  if ! grep $fic ../.gitattributes; then
    install -Dpm 0644 $fic %{buildroot}%{php_home}/Composer/Spdx/$fic
  fi
done
popd

: Resources
cp -pr res   %{buildroot}%{_datadir}/%{name}


%check
%if %{with tests}
# ignored as related class not installed
rm tests/SpdxLicensesUpdaterTest.php

export BUILDROOT_SPDX=%{buildroot}

# compatibility with recent PHPUnit
sed -e  '/setUp()/s/$/:void/' -i tests/*.php

ret=0
for cmd in php php80 php81 php82 php83; do
  if which $cmd; then
    $cmd -d memory_limit=1G ${2:-%{_bindir}/phpunit9} \
      --bootstrap %{buildroot}%{php_home}/Composer/Spdx/autoload.php \
      --no-coverage \
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
%dir %{php_home}/Composer
     %{php_home}/Composer/Spdx
%{_datadir}/%{name}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Nov 20 2023 Remi Collet <remi@remirepo.net> - 1.5.8-1
- update to 1.5.8 (SPDX 3.22)
- switch to phpunit9

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 23 2022 Remi Collet <remi@remirepo.net> - 1.5.7-1
- update to 1.5.7 (SPDX 3.17)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Nov 18 2021 Remi Collet <remi@remirepo.net> - 1.5.6-1
- update to 1.5.6 (SPDX 3.15)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec  4 2020 Remi Collet <remi@remirepo.net> - 1.5.5-1
- update to 1.5.5 (SPDX 3.11)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 16 2020 Remi Collet <remi@remirepo.net> - 1.5.4-1
- update to 1.5.4 (SPDX 3.9)

* Fri Feb 14 2020 Remi Collet <remi@remirepo.net> - 1.5.3-1
- update to 1.5.3 (SPDX 3.8)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug  1 2019 Remi Collet <remi@remirepo.net> - 1.5.2-1
- update to 1.5.2 (SPDX 3.6)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 26 2019 Remi Collet <remi@remirepo.net> - 1.5.1-1
- update to 1.5.1 (SPDX 3.4)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov  2 2018 Remi Collet <remi@remirepo.net> - 1.5.0-1
- update to 1.5.0 (SPDX 3.3)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 14 2018 Remi Collet <remi@remirepo.net> - 1.4.0-1
- update to 1.4.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Feb  1 2018 Remi Collet <remi@remirepo.net> - 1.3.0-1
- Update to 1.3.0

* Thu Jan  4 2018 Remi Collet <remi@remirepo.net> - 1.2.0-1
- Update to 1.2.0
- use phpunit6 on Fedora

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr  4 2017 Remi Collet <remi@remirepo.net> - 1.1.6-1
- Update to 1.1.6

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 20 2016 Remi Collet <remi@fedoraproject.org> - 1.1.5-2
- switch from symfony/class-loader to fedora/autoloader

* Wed Sep 28 2016 Remi Collet <remi@fedoraproject.org> - 1.1.5-1
- version 1.1.5 (new licenses)

* Wed May  4 2016 Remi Collet <remi@fedoraproject.org> - 1.1.4-1
- version 1.1.4 (new licenses)

* Fri Mar 25 2016 Remi Collet <remi@fedoraproject.org> - 1.1.3-1
- version 1.1.3 (new licenses)
- run test suite with both PHP 5 and 7 when available

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct  5 2015 Remi Collet <remi@fedoraproject.org> - 1.1.2-1
- version 1.1.2 (new licenses)

* Tue Sep  8 2015 Remi Collet <remi@fedoraproject.org> - 1.1.1-1
- version 1.1.1

* Mon Jul 20 2015 Remi Collet <remi@fedoraproject.org> - 1.1.0-2
- fix permissions

* Fri Jul 17 2015 Remi Collet <remi@fedoraproject.org> - 1.1.0-1
- version 1.1.0

* Fri Jul 17 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-1.20150717git572abf7
- new snapshot (issue #6 fixed, uneeded dep on justinrainbow/json-schema)

* Fri Jul 17 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-1.20150716git96c33d0
- initial package, version 1.0.0 + pr4
