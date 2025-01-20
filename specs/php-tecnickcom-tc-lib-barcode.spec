# remirepo/fedora spec file for php-tecnickcom-tc-lib-barcode
#
# SPDX-FileCopyrightText:  Copyright 2015-2024 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#
%global gh_commit    cd5d8029eeaf6225b9ff4692364c4c473191e487
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global c_vendor     tecnickcom
%global gh_owner     tecnickcom
%global gh_project   tc-lib-barcode
%global php_project  %{_datadir}/php/Com/Tecnick/Barcode
%bcond_without       tests

Name:           php-%{gh_owner}-%{gh_project}
Version:        2.4.2
Release:        2%{?dist}
Summary:        PHP library to generate linear and bidimensional barcodes

License:        LGPL-3.0-or-later
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{?gh_short}.tar.gz

BuildArch:      noarch
%if %{with tests}
# For tests
%global phpunit %{_bindir}/phpunit10
BuildRequires:  phpunit10 >= 10.5.10
BuildRequires:  php(language) >= 8.1
BuildRequires: (php-composer(%{c_vendor}/tc-lib-color) >= 2.2    with php-composer(%{c_vendor}/tc-lib-color) < 3)
BuildRequires:  php-bcmath
BuildRequires:  php-ctype
BuildRequires:  php-date
BuildRequires:  php-gd
BuildRequires:  php-pcre
# Optional but required for test
BuildRequires:  php-pecl-imagick
%endif
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, "require": {
#        "php": ">=8.1"
#        "ext-bcmath": "*",
#        "ext-date": "*",
#        "ext-gd": "*",
#        "ext-pcre": "*",
#        "tecnickcom/tc-lib-color": "^2.2"
Requires:       php(language) >= 8.1
Requires:       php-bcmath
Requires:       php-ctype
Requires:       php-date
Requires:       php-gd
Requires:       php-pcre
Requires:      (php-composer(%{c_vendor}/tc-lib-color) >= 2.2    with php-composer(%{c_vendor}/tc-lib-color) < 3)
# From phpcompatinfo report for version 1.15.5
# none
Requires:       php-composer(fedora/autoloader)

# Composer
Provides:       php-composer(%{c_vendor}/%{gh_project}) = %{version}
# Upstream package name
Provides:       php-%{gh_project} = %{version}


%description
Provides tc-lib-barcode: PHP classes to generate linear and bidimensional
barcodes: CODE 39, ANSI MH10.8M-1983, USD-3, 3 of 9, CODE 93, USS-93,
Standard 2 of 5, Interleaved 2 of 5, CODE 128 A/B/C, 2 and 5 Digits
UPC-Based Extension, EAN 8, EAN 13, UPC-A, UPC-E, MSI, POSTNET, PLANET,
RMS4CC (Royal Mail 4-state Customer Code), CBC (Customer Bar Code),
KIX (Klant index - Customer index), Intelligent Mail Barcode, Onecode,
USPS-B-3200, CODABAR, CODE 11, PHARMACODE, PHARMACODE TWO-TRACKS, Datamatrix
ECC200, QR-Code, PDF417.

Optional dependency: php-pecl-imagick


%prep
%setup -q -n %{gh_project}-%{gh_commit}

: Sanity check
grep -q '^%{version}$' VERSION

: Fix the examples
sed -e 's:^require:////require:' \
    -e 's:^//require:require:'   \
    -i example/*php


%build
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{_datadir}/php/Com/Tecnick/Color/autoload.php',
]);
EOF


%install
mkdir -p   $(dirname %{buildroot}%{php_project})
cp -pr src %{buildroot}%{php_project}


%check
%if %{with tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require '%{buildroot}%{php_project}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Test\\', dirname(__DIR__) . '/test');
EOF

ret=0
for cmdarg in "php %{phpunit}" php81 php82 php83 php84; do
   if which $cmdarg; then
      set $cmdarg
      cp phpunit.xml.dist phpunit.xml
      $1 ${2:-%{_bindir}/phpunit10} --migrate-configuration || :
      $1 ${2:-%{_bindir}/phpunit10} \
        --filter '^((?!(testGetSvg|testGetPng)).)*$' \
        --no-coverage --stderr || ret=1
   fi
done
exit $ret
%else
: Test suite disabled
%endif


%files
%license LICENSE
%doc composer.json
%doc *.md example
%{php_project}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Dec 26 2024 Remi Collet <remi@remirepo.net> - 2.4.2-1
- update to 2.4.2
- raise dependency on PHP 8.1

* Mon Dec 23 2024 Remi Collet <remi@remirepo.net> - 2.4.1-1
- update to 2.4.1 (no change)
- re-license spec file to CECILL-2.1

* Mon Nov 25 2024 Remi Collet <remi@remirepo.net> - 2.4.0-1
- update to 2.4.0

* Mon Oct 28 2024 Remi Collet <remi@remirepo.net> - 2.3.2-1
- update to 2.3.2 (no change)

* Mon Sep  9 2024 Remi Collet <remi@remirepo.net> - 2.3.1-1
- update to 2.3.1 (no change)

* Thu Sep  5 2024 Remi Collet <remi@remirepo.net> - 2.3.0-1
- update to 2.3.0

* Mon Aug 19 2024 Remi Collet <remi@remirepo.net> - 2.2.3-1
- update to 2.2.3 (no change)
- raise dependency on tc-lib-color 2.2

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Apr 12 2024 Remi Collet <remi@remirepo.net> - 2.2.1-1
- update to 2.2.1

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Nov 28 2023 Remi Collet <remi@remirepo.net> - 2.1.2-1
- update to 2.1.2 (no change)

* Wed Nov 22 2023 Remi Collet <remi@remirepo.net> - 2.1.1-1
- update to 2.1.1

* Wed Nov 22 2023 Remi Collet <remi@remirepo.net> - 2.0.7-1
- update to 2.0.7
- raise dependency on PHP 8
- raise dependency on tc-lib-color 2.0

* Mon Oct 23 2023 Remi Collet <remi@remirepo.net> - 1.18.4-1
- update to 1.18.4 (no change)

* Mon Oct 23 2023 Remi Collet <remi@remirepo.net> - 1.18.2-1
- update to 1.18.2

* Thu Oct 12 2023 Remi Collet <remi@remirepo.net> - 1.17.38-1
- update to 1.17.38

* Tue Oct 10 2023 Remi Collet <remi@remirepo.net> - 1.17.33-1
- update to 1.17.33

* Tue Oct 10 2023 Remi Collet <remi@remirepo.net> - 1.17.30-1
- update to 1.17.30

* Wed Sep  6 2023 Remi Collet <remi@remirepo.net> - 1.17.29-1
- update to 1.17.29 (no change)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed May 24 2023 Remi Collet <remi@remirepo.net> - 1.17.25-1
- update to 1.17.25 (no change)

* Fri May  5 2023 Remi Collet <remi@remirepo.net> - 1.17.24-1
- update to 1.17.24 (no change)

* Thu May  4 2023 Remi Collet <remi@remirepo.net> - 1.17.22-1
- update to 1.17.22 (no change)

* Wed May  3 2023 Remi Collet <remi@remirepo.net> - 1.17.20-1
- update to 1.17.20 (no change)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 22 2022 Remi Collet <remi@remirepo.net> - 1.17.19-1
- update to 1.17.19 (no change)

* Tue Dec 13 2022 Remi Collet <remi@remirepo.net> - 1.17.15-1
- update to 1.17.15

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Remi Collet <remi@remirepo.net> - 1.17.14-1
- update to 1.17.14 (no change)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan  3 2022 Remi Collet <remi@remirepo.net> - 1.17.11-1
- update to 1.17.11 (no change)

* Mon Dec 20 2021 Remi Collet <remi@remirepo.net> - 1.17.8-1
- update to 1.17.8

* Thu Nov 11 2021 Remi Collet <remi@remirepo.net> - 1.17.7-1
- update to 1.17.7

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Feb  8 2021 Remi Collet <remi@remirepo.net> - 1.17.6-1
- update to 1.17.6 (no change)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 21 2020 Remi Collet <remi@remirepo.net> - 1.17.1-1
- update to 1.17.1
- switch to classmap autoloader

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Remi Collet <remi@remirepo.net> - 1.16.1-1
- update to 1.16.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.20-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan  3 2020 Remi Collet <remi@remirepo.net> - 1.15.20-1
- update to 1.15.20

* Wed Oct  2 2019 Remi Collet <remi@remirepo.net> - 1.15.16-1
- update to 1.15.16

* Thu Sep 19 2019 Remi Collet <remi@remirepo.net> - 1.15.15-1
- update to 1.15.15

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun  3 2019 Remi Collet <remi@remirepo.net> - 1.15.14-1
- update to 1.15.14

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 25 2018 Remi Collet <remi@remirepo.net> - 1.15.12-1
- update to 1.15.12 (no change)

* Tue May 15 2018 Remi Collet <remi@remirepo.net> - 1.15.11-1
- update to 1.15.11 (no change)

* Mon May 14 2018 Remi Collet <remi@remirepo.net> - 1.15.10-1
- update to 1.15.10 (no change)
- switch to phpunit7
- use range dependencies

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan  2 2018 Remi Collet <remi@remirepo.net> - 1.15.7-1
- Update to 1.15.7

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Feb 12 2017 Remi Collet <remi@remirepo.net.org> - 1.15.6-1
- update to 1.15.6 (no change)
- use phpunit6 on F26+

* Mon Feb  6 2017 Remi Collet <remi@fedoraproject.org> - 1.15.5-1
- update to 1.15.5 (no change)

* Fri Nov 18 2016 Remi Collet <remi@fedoraproject.org> - 1.15.4-1
- update to 1.15.4

* Fri Oct 14 2016 Remi Collet <remi@fedoraproject.org> - 1.15.2-1
- update to 1.15.2

* Mon Sep  5 2016 Remi Collet <remi@fedoraproject.org> - 1.15.0-1
- update to 1.15.0

* Fri Sep  2 2016 Remi Collet <remi@fedoraproject.org> - 1.14.0-1
- update to 1.14.0
- raise dependency on tecnickcom/tc-lib-color >= 1.12.1

* Mon Jul 11 2016 Remi Collet <remi@fedoraproject.org> - 1.9.2-1
- update to 1.9.2

* Tue Jun 14 2016 Remi Collet <remi@fedoraproject.org> - 1.9.0-1
- update to 1.9.0
- raise dependency on tecnickcom/tc-lib-color >= 1.10.0
- raise dependency on php >= 5.4
- run test suite with both PHP 5 and 7 when available

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov  4 2015 Remi Collet <remi@fedoraproject.org> - 1.5.0-1
- update to 1.5.0

* Sun Sep 13 2015 Remi Collet <remi@fedoraproject.org> - 1.4.3-1
- update to 1.4.3
- provide php-composer(tecnickcom/tc-lib-barcode)

* Thu Aug 27 2015 Remi Collet <remi@fedoraproject.org> - 1.4.2-1
- update to 1.4.2

* Tue Aug 25 2015 Remi Collet <remi@fedoraproject.org> - 1.4.1-3
- add patch for PHP 5.3
  https://github.com/tecnickcom/tc-lib-barcode/pull/7

* Wed Aug 12 2015 Remi Collet <remi@fedoraproject.org> - 1.4.1-2
- fix package summary

* Tue Aug 11 2015 Remi Collet <remi@fedoraproject.org> - 1.4.1-1
- update to 1.4.1

* Tue Aug 11 2015 Remi Collet <remi@fedoraproject.org> - 1.4.0-1
- update to 1.4.0

* Sat Aug  8 2015 Remi Collet <remi@fedoraproject.org> - 1.3.1-1
- update to 1.3.1

* Thu Aug  6 2015 Remi Collet <remi@fedoraproject.org> - 1.3.0-1
- update to 1.3.0

* Fri Jul 24 2015 Remi Collet <remi@fedoraproject.org> - 1.2.1-1
- update to 1.2.1 (no change)

* Thu Jul  2 2015 Remi Collet <remi@fedoraproject.org> - 1.2.0-1
- update to 1.2.0

* Wed Jul  1 2015 Remi Collet <remi@fedoraproject.org> - 1.1.3-1
- update to 1.1.3
- drop patch merged upstream

* Wed Jul  1 2015 Remi Collet <remi@fedoraproject.org> - 1.1.2-1
- initial package, version 1.1.2
- open https://github.com/tecnickcom/tc-lib-barcode/pull/2
  PHP < 5.5 compatibility
