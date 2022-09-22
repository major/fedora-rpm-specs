#
# Fedora spec file for php-robrichards-xmlseclibs
#
# Copyright (c) 2016-2019 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve the changelog entries
#

%global github_owner     robrichards
%global github_name      xmlseclibs
%global github_version   2.1.1
%global github_commit    118450a141ac2336be1b5e5e91a22229441b0277

%global composer_vendor  robrichards
%global composer_project xmlseclibs

# "php": ">= 5.3"
%global php_min_ver 5.3

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       7%{?github_release}%{?dist}
Summary:       A PHP library for XML Security

License:       BSD
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Tests
%if %{with_tests}
BuildRequires: php-composer(phpunit/phpunit)
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
## composer.json: optional
BuildRequires: php-mcrypt
BuildRequires: php-openssl
## phpcompatinfo (computed from version 2.1.1)
BuildRequires: php-dom
BuildRequires: php-hash
BuildRequires: php-pcre
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
# composer.json: suggest
Requires:      php-openssl
# phpcompatinfo (computed from version 2.1.1)
Requires:      php-dom
Requires:      php-hash
Requires:      php-pcre
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Weak dependencies
%if 0%{?fedora} >= 21
## composer.json: suggest
Suggests:      php-mcrypt
%endif

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}


%description
xmlseclibs is a library written in PHP for working with XML Encryption and
Signatures.

NOTE: php-mcrypt will not be automatically installed as a dependency of this
package so it will need to be "manually" installed if it is required --
specifically for the following XMLSecurityKey encryption types:
- XMLSecurityKey::AES128_CBC
- XMLSecurityKey::AES192_CBC
- XMLSecurityKey::AES256_CBC
- XMLSecurityKey::TRIPLEDES_CBC

Autoloader: %{phpdir}/RobRichards/XMLSecLibs/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('RobRichards\\XMLSecLibs\\', __DIR__);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/RobRichards/XMLSecLibs
cp -rp src/* %{buildroot}%{phpdir}/RobRichards/XMLSecLibs/


%check
%if %{with_tests}
: Use autoloader
sed 's#require.*xmlseclibs.*#require_once "%{buildroot}%{phpdir}/RobRichards/XMLSecLibs/autoload.php";#' \
    -i tests/*.phpt

: Skip tests known to fail
rm -f \
    tests/extract-win-cert.phpt \
    tests/withcomment-id-uri-object.phpt \
    tests/withcomment-id-uri.phpt

: Disable deprecation warning with php 7.1
for test in tests/*phpt; do
  echo -e "\n--INI--\nerror_reporting=24575" >>$test
done

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in "" %{?rhel:php54 php55} php56 php70 php71 php72 php73 php74; do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose tests || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc CHANGELOG.txt
%doc composer.json
%doc README.md
%dir %{phpdir}/RobRichards
     %{phpdir}/RobRichards/XMLSecLibs


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 06 2019 Shawn Iwinski <shawn@iwin.ski> - 2.1.1-1
- Update to 2.1.1 (CVE-2019-3465)
- https://simplesamlphp.org/security/201911-01

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 30 2017 Shawn Iwinski <shawn@iwin.ski> - 2.0.1-4
- Switch autoloader to php-composer(fedora/autoloader)
- Test with SCLs if available

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov 25 2016 Remi Collet <remi@fedoraproject.org> - 2.0.1-2
- fix FTBFS, disable deprecation messages

* Sun Sep 11 2016 Shawn Iwinski <shawn@iwin.ski> - 2.0.1-1
- Updated to 2.0.1 (RHBZ #1374415)

* Thu Jul 14 2016 Shawn Iwinski <shawn@iwin.ski> - 2.0.0-2.20160105git84313ca
- Updated to latest snapshot
- Moved php-openssl from weak dependency to hard dependency
- Added php-mcrypt weak dependency and added information to %%description about
  when it is required

* Sun Jul 10 2016 Shawn Iwinski <shawn@iwin.ski> - 2.0.0-1
- Initial package
