# remirepo/fedora spec file for php-bacon-qr-code2
#
# Copyright (c) 2017-2022 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%bcond_without       tests

%global gh_commit    8674e51bb65af933a5ffaf1c308a660387c35c22
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     Bacon
%global gh_project   BaconQrCode

%global pk_vendor    bacon
%global pk_project   bacon-qr-code

%global ns_vendor    %nil
%global ns_project   %{gh_project}
%global php_home     %{_datadir}/php
%global major        2

Name:           php-%{pk_project}%{major}
Version:        2.0.8
Release:        8%{?dist}
Summary:        QR code generator for PHP

Group:          Development/Libraries
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
%if %{with tests}
# For tests
BuildRequires:  php(language) >= 7.1
BuildRequires:  php-iconv
BuildRequires:  php-imagick
BuildRequires:  php-ctype
BuildRequires:  php-spl
BuildRequires:  php-xmlwriter
BuildRequires:  php-reflection
BuildRequires: (php-composer(dasprid/enum) >= 1.0    with php-composer(dasprid/enum) < 2)
# From composer.json, "require-dev": {
#        "phpunit/phpunit": "^7 | ^8 | ^9",
#        "spatie/phpunit-snapshot-assertions": "^4.2.9",
#        "squizlabs/php_codesniffer": "^3.1",
#        "phly/keep-a-changelog": "^1.4"
%global phpunit %{_bindir}/phpunit9
BuildRequires:  %{phpunit}
# Required by autoloader
BuildRequires:  php-composer(fedora/autoloader)
%endif

# From composer.json, "require": {
#        "php": "^7.1 || ^8.0",
#        "ext-iconv": "*",
#        "dasprid/enum": "^1.0.3"
Requires:       php(language) >= 7.1
Requires:       php-iconv
# From composer.json, "suggest": {
#        "ext-imagick": "to generate QR code images"
Requires:      (php-composer(dasprid/enum) >= 1.0    with php-composer(dasprid/enum) < 2)
Recommends:     php-imagick
# From phpcompatinfo report for version 2.0.0
Requires:       php-ctype
Requires:       php-spl
Requires:       php-xmlwriter
# Required by autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
BaconQrCode is a port of QR code portion of the ZXing library.
It currently only features the encoder part, but could later
receive the decoder part as well.

As the Reed Solomon codec implementation of the ZXing library
performs quite slow in PHP, it was exchanged with the implementation
by Phil Karn.

Autoloader: %{php_home}/%{ns_project}%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

cat << 'EOF' | tee src/autoload.php
<?php
/* Autoloader for %{name} and its dependencies */
require_once '/usr/share/php/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{ns_project}\\', __DIR__);
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/DASPRiD/Enum/autoload.php',
]);

EOF


%build
# Empty build section, most likely nothing required.


%install
: Library
mkdir -p   %{buildroot}%{php_home}
cp -pr src %{buildroot}%{php_home}/%{ns_project}%{major}


%check
%if %{with tests}
if php -r 'exit(PHP_INT_SIZE<8 ? 0 : 1);'
then
  : ignore test suite because of https://github.com/Bacon/BaconQrCode/issues/31
  exit 0
fi

: ignore test using spatie/phpunit-snapshot-assertions
rm test/Integration/ImagickRenderingTest.php

mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require '%{buildroot}%{php_home}/%{ns_project}%{major}/autoload.php';
EOF

ret=0
for cmd in "php %{phpunit}" php80 php81 php82; do
  if which $cmd; then
    set $cmd
    $1 ${2:-%{_bindir}/phpunit9} --verbose || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif


%files
%license LICENSE
%doc composer.json
%doc README.md
%{php_home}/%{ns_project}%{major}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep  4 2024 Miroslav Suchý <msuchy@redhat.com> - 2.0.8-7
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec  8 2022 Remi Collet <remi@remirepo.net> - 2.0.8-1
- update to 2.0.8

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Mar 14 2022 Remi Collet <remi@remirepo.net> - 2.0.7-1
- update to 2.0.7

* Mon Feb  7 2022 Remi Collet <remi@remirepo.net> - 2.0.6-1
- update to 2.0.6 (no change)

* Mon Jan 31 2022 Remi Collet <remi@remirepo.net> - 2.0.5-1
- update to 2.0.5

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 21 2021 Remi Collet <remi@remirepo.net> - 2.0.4-1
- update to 2.0.4

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct 30 2020 Remi Collet <remi@remirepo.net> - 2.0.3-1
- update to 2.0.3 (no change)

* Tue Aug 11 2020 Remi Collet <remi@remirepo.net> - 2.0.2-1
- update to 2.0.2
- switch to phpunit9

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 15 2020 Remi Collet <remi@remirepo.net> - 2.0.1-1
- update to 2.0.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep  2 2019 Remi Collet <remi@remirepo.net> - 2.0.0-1
- update to 2.0.0
- rename to php-bacon-qr-code2
- move installation to /usr/share/php/BaconQrCode2
- raise dependency on PHP 7.1
- add dependency on dasprid/enum
- use phpunit6
- use git snapshot to retrieve test suite
- switch from php-gd to php-imagick

* Thu Oct 19 2017 Remi Collet <remi@remirepo.net> - 1.0.3-1
- Update to 1.0.3

* Mon Jul  3 2017 Remi Collet <remi@remirepo.net> - 1.0.1-4
- run test suite only on 64-bit arch

* Mon Jul  3 2017 Remi Collet <remi@remirepo.net> - 1.0.1-2
- fix directory ownership, from review #1465313

* Tue Jun 27 2017 Remi Collet <remi@remirepo.net> - 1.0.1-1
- initial package, version 1.0.1
- open https://github.com/Bacon/BaconQrCode/pull/29 - phpunit
