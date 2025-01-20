#
# Fedora spec file for php-egulias-email-validator
#
# Copyright (c) 2014-2020 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     egulias
%global github_name      EmailValidator
%global github_version   1.2.17
%global github_commit    19674b35a0a3456be1b96e137098d31ed386fb61

%global composer_vendor  egulias
%global composer_project email-validator

# "php": ">= 5.3.3"
%global php_min_ver 5.3.3
# "doctrine/lexer": "^1.0.1"
%global doctrine_lexer_min_ver 1.0.1
%global doctrine_lexer_max_ver 2.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       12%{?github_release}%{?dist}
Summary:       A library for validating emails

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Tests
%if %{with_tests}
BuildRequires: php-composer(phpunit/phpunit)
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-composer(doctrine/lexer) >= %{doctrine_lexer_min_ver} with php-composer(doctrine/lexer) < %{doctrine_lexer_max_ver})
%else
BuildRequires: php-composer(doctrine/lexer) <  %{doctrine_lexer_max_ver}
BuildRequires: php-composer(doctrine/lexer) >= %{doctrine_lexer_min_ver}
%endif
## phpcompatinfo (computed from version 1.2.14)
BuildRequires: php-filter
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:      (php-composer(doctrine/lexer) >= %{doctrine_lexer_min_ver} with php-composer(doctrine/lexer) < %{doctrine_lexer_max_ver})
%else
Requires:      php-composer(doctrine/lexer) <  %{doctrine_lexer_max_ver}
Requires:      php-composer(doctrine/lexer) >= %{doctrine_lexer_min_ver}
%endif
# phpcompatinfo (computed from version 1.2.14)
Requires:      php-pcre
Requires:      php-reflection
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
%{summary}.

Autoloader: %{phpdir}/Egulias/EmailValidator/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}


%build

: Create autoloader
cat <<'AUTOLOAD' | tee src/Egulias/EmailValidator/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Egulias\\EmailValidator\\', __DIR__);

\Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}/Doctrine/Common/Lexer/autoload.php',
));
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}
cp -rp src/* %{buildroot}%{phpdir}/


%check
%if %{with_tests}
: Skip testValidEmailsWithWarningsCheck and testInvalidEmailsWithDnsCheckAndStrictMode
# because Koji does not have network access so assertEquals(expected_warnings, actual_warnings)
# fails because EmailValidator::DNSWARN_NO_RECORD is not an expected warning
sed -e 's/function testValidEmailsWithWarningsCheck/function SKIP_testValidEmailsWithWarningsCheck/' \
    -e 's/function testInvalidEmailsWithDnsCheckAndStrictMode/function SKIP_testInvalidEmailsWithDnsCheckAndStrictMode/' \
    -i tests/egulias/Tests/EmailValidator/EmailValidatorTest.php

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in "" %{?rhel:php54 php55} php56 php70 php71 php72 php73 php74 php80; do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose \
            --bootstrap %{buildroot}%{phpdir}/Egulias/EmailValidator/autoload.php \
            || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc README.md
%doc composer.json
%dir %{phpdir}/Egulias
     %{phpdir}/Egulias/EmailValidator


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.17-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.17-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.17-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.17-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.17-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.17-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 13 2020 Remi Collet <remi@remirepo.net> - 1.2.17-1
- update to 1.2.17 (no change)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan  2 2020 Remi Collet <remi@remirepo.net> - 1.2.16-1
- update to 1.2.16

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep 26 2018 Remi Collet <remi@remirepo.net> - 1.2.15-1
- update to 1.2.15

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 24 2018 Remi Collet <remi@remirepo.net> - 1.2.14-1
- update to 1.2.14
- use range dependencies (F27+, EL-8)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun May 14 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.13-3
- Switch autoloader to php-composer(fedora/autoloader)
- Test with SCLs if available

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 08 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.13-1
- Updated to 1.2.13 (RHBZ #1336594)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 04 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.11-1
- Updated to 1.2.11 (RHBZ #1280283)

* Sun Oct 11 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.10-1
- Updated to 1.2.10 (RHBZ #1270623)
- Modified autoloader to load dependencies after self-registration

* Sat Jun 27 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.9-1
- Updated to 1.2.9 (RHBZ #1215684)
- Added autoloader

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 05 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.7-1
- Updated to 1.2.7 (BZ #1178809)

* Sun Dec 07 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.6-1
- Updated to 1.2.6 (BZ #1171051)

* Sun Nov 09 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.5-1
- Updated to 1.2.5

* Thu Nov 06 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.4-2
- Skip testValidEmailsWithWarningsCheck because Koji build fails

* Mon Nov 03 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.4-1
- Updated to 1.2.4

* Mon Oct 27 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.3-1
- Updated to 1.2.3

* Wed Sep 10 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.2-1
- Initial package
