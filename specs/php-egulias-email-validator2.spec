# remirepo/fedora spec file for php-egulias-email-validator2
#
# Copyright (c) 2014-2021 Shawn Iwinski, Remi Collet
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     egulias
%global github_name      EmailValidator
%global github_version   2.1.25
%global github_commit    0dbf5d78455d4d6a41d186da50adc1122ec066f4
%global github_short     %(c=%{github_commit}; echo ${c:0:7})
%global major            2

%global composer_vendor  egulias
%global composer_project email-validator

# "php": ">= 5.5"
%global php_min_ver 5.5
# "doctrine/lexer": "^1.0.1"
%global doctrine_lexer_min_ver 1.0.1
%global doctrine_lexer_max_ver 2.0

# Build using "--without tests" to disable tests
%bcond_without tests

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}%{major}
Version:       %{github_version}
Release:       11%{?github_release}%{?dist}
Summary:       A library for validating emails

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{name}-%{github_version}-%{github_short}.tgz
Source1:       makesrc.sh

# adapt for recent PHPUnit
Patch0:        %{name}-phpunit.patch

BuildArch:     noarch
# Tests
%if %{with tests}
## composer.json (require-dev)
#    "dominicsayers/isemail": "^3.0.7",
#    "phpunit/phpunit": "^4.8.36|^7.5.15",
#    "satooshi/php-coveralls": "^1.0.1"
%if 0%{?fedora} >= 31 || 0%{?rhel} >= 9
BuildRequires: (php-composer(doctrine/lexer) >= %{doctrine_lexer_min_ver} with php-composer(doctrine/lexer) <  %{doctrine_lexer_max_ver})
%global phpunit %{_bindir}/phpunit9
%else
BuildRequires:  php-doctrine-lexer  >= %{doctrine_lexer_min_ver}
%global phpunit %{_bindir}/phpunit8
%endif
BuildRequires:  %{phpunit}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
## phpcompatinfo (computed from version 2.1.2)
BuildRequires: php-dom
BuildRequires: php-filter
BuildRequires: php-intl
BuildRequires: php-pcre
BuildRequires: php-spl
## Autoloader
BuildRequires: php-fedora-autoloader-devel
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:     (php-composer(doctrine/lexer) >= %{doctrine_lexer_min_ver} with php-composer(doctrine/lexer) <  %{doctrine_lexer_max_ver})
# phpcompatinfo (computed from version 2.1.2)
Requires:      php-intl
Requires:      php-pcre
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
%{summary}.

Autoloader: %{phpdir}/Egulias/EmailValidator%{major}/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}
%patch -P0 -p1 -b .phpunit


%build
: Create autoloader
phpab --template fedora \
      --output src/autoload.php \
      src

cat <<'AUTOLOAD' | tee -a src/autoload.php

\Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}/Doctrine/Common/Lexer/autoload.php',
));
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/Egulias
cp -rp src %{buildroot}%{phpdir}/Egulias/EmailValidator%{major}


%check
%if %{with tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once "%{buildroot}%{phpdir}/Egulias/EmailValidator%{major}/autoload.php";
\Fedora\Autoloader\Autoload::addPsr4('Egulias\\Tests\\', dirname(__DIR__) . "/tests");
EOF

: Skip online tests
rm tests/EmailValidator/Validation/DNSCheckValidationTest.php
rm tests/EmailValidator/Validation/SpoofCheckValidationTest.php

: Upstream tests
ret=0
for cmdarg in "php %{phpunit}" "php72 %{_bindir}/phpunit8" php73 php74 php80; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit9} \
      --verbose || ret=1
  fi
done
exit $ret
%else
: Tests skipped
%endif


%files
%license LICENSE
%doc README.md
%doc composer.json
%dir %{phpdir}/Egulias
     %{phpdir}/Egulias/EmailValidator%{major}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.25-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.25-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.25-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.25-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.25-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.25-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.25-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.25-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan  6 2021 Remi Collet <remi@remirepo.net> - 2.1.25-1
- update to 2.1.25

* Mon Nov 16 2020 Remi Collet <remi@remirepo.net> - 2.1.24-1
- update to 2.1.24

* Mon Nov  2 2020 Remi Collet <remi@remirepo.net> - 2.1.23-1
- update to 2.1.23

* Mon Sep 28 2020 Remi Collet <remi@remirepo.net> - 2.1.22-1
- update to 2.1.22

* Mon Sep 21 2020 Remi Collet <remi@remirepo.net> - 2.1.21-1
- update to 2.1.21

* Mon Sep  7 2020 Remi Collet <remi@remirepo.net> - 2.1.20-1
- update to 2.1.20

* Tue Aug 11 2020 Remi Collet <remi@remirepo.net> - 2.1.19-1
- update to 2.1.19
- switch to phpunit9

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 17 2020 Remi Collet <remi@remirepo.net> - 2.1.18-1
- update to 2.1.18
- open https://github.com/egulias/EmailValidator/pull/244
  fix tests path
- switch to classmap autoloader

* Fri Feb 14 2020 Remi Collet <remi@remirepo.net> - 2.1.17-1
- update to 2.1.17

* Thu Feb 13 2020 Remi Collet <remi@remirepo.net> - 2.1.16-1
- update to 2.1.16

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Remi Collet <remi@remirepo.net> - 2.1.15-1
- update to 2.1.15

* Tue Jan 14 2020 Remi Collet <remi@remirepo.net> - 2.1.14-1
- update to 2.1.14 (no change)

* Thu Jan  2 2020 Remi Collet <remi@remirepo.net> - 2.1.13-1
- update to 2.1.13 (no change)
- use phpunit7

* Fri Dec 20 2019 Remi Collet <remi@remirepo.net> - 2.1.12-1
- update to 2.1.12 (no change)

* Mon Aug 19 2019 Remi Collet <remi@remirepo.net> - 2.1.11-1
- update to 2.1.11

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 21 2019 Remi Collet <remi@remirepo.net> - 2.1.10-1
- update to 2.1.10

* Tue Jun 25 2019 Remi Collet <remi@remirepo.net> - 2.1.9-1
- update to 2.1.9

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec  6 2018 Remi Collet <remi@remirepo.net> - 2.1.7-1
- update to 2.1.7

* Wed Sep 26 2018 Remi Collet <remi@remirepo.net> - 2.1.6-1
- update to 2.1.6 (no change)

* Mon Aug 20 2018 Remi Collet <remi@remirepo.net> - 2.1.5-1
- update to 2.1.5

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 12 2018 Remi Collet <remi@remirepo.net> - 2.1.4-1
- update to 2.1.4
- use range dependencies
- use phpunit6

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 16 2017 Remi Collet <remi@remirepo.net> - 2.1.3-1
- Update to 2.1.3

* Wed Oct  4 2017 Remi Collet <remi@remirepo.net> - 2.1.2-1
- Update to 2.1.2
- rename to php-egulias-email-validator2
- raise dependency on PHP 5.5

* Sun May 14 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.13-3
- Switch autoloader to php-composer(fedora/autoloader)
- Test with SCLs if available

* Mon Aug 08 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.13-1
- Updated to 1.2.13 (RHBZ #1336594)

* Mon Jan 04 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.11-1
- Updated to 1.2.10 (RHBZ #1280283)

* Sun Oct 11 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.10-1
- Updated to 1.2.10 (RHBZ #1270623)
- Modified autoloader to load dependencies after self-registration

* Sat Jun 27 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.9-1
- Updated to 1.2.9 (RHBZ #1215684)
- Added autoloader

* Mon Jan 05 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.7-1
- Updated to 1.2.7 (BZ #1178809)

* Sun Dec 07 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.6-1
- Updated to 1.2.6 (BZ #1171051)

* Sun Nov 09 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.5-1
- Updated to 1.2.5

* Thu Nov  6 2014 Remi Collet <remi@fedoraproject.org> - 1.2.4-1
- backport for remi repository

* Mon Nov 03 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.4-1
- Updated to 1.2.4

* Mon Oct 27 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.3-1
- Updated to 1.2.3

* Wed Sep 10 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.2-1
- Initial package
