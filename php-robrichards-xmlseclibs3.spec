#
# Fedora spec file for php-robrichards-xmlseclibs3
#
# Copyright (c) 2017-2020 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve the changelog entries
#

%global github_owner     robrichards
%global github_name      xmlseclibs
%global github_version   3.1.1
%global github_commit    f8f19e58f26cdb42c54b214ff8a820760292f8df

%global composer_vendor  robrichards
%global composer_project xmlseclibs

# "php": ">= 5.4"
%global php_min_ver 5.4

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}3
Version:       %{github_version}
Release:       5%{?github_release}%{?dist}
Summary:       A PHP library for XML Security (version 3)

License:       BSD
URL:           https://github.com/%{github_owner}/%{github_name}

# GitHub export does not include tests
# Run php-robrichards-xmlseclibs3-get-source.sh to create full source
Source0:       %{name}-%{version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with_tests}
BuildRequires: php-composer(phpunit/phpunit)
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-openssl
## phpcompatinfo (computed from version 3.1.1)
BuildRequires: php-dom
BuildRequires: php-hash
BuildRequires: php-pcre
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      php-openssl
# phpcompatinfo (computed from version 3.1.1)
Requires:      php-dom
Requires:      php-hash
Requires:      php-pcre
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}


%description
xmlseclibs is a library written in PHP for working with XML Encryption and
Signatures.

Autoloader: %{phpdir}/RobRichards/XMLSecLibs3/autoload.php


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
mkdir -p %{buildroot}%{phpdir}/RobRichards
cp -rp src %{buildroot}%{phpdir}/RobRichards/XMLSecLibs3


%check
%if %{with_tests}
: Use autoloader
sed 's#require.*xmlseclibs.*#require_once "%{buildroot}%{phpdir}/RobRichards/XMLSecLibs3/autoload.php";#' \
    -i tests/*.phpt

: Skip tests known to fail
rm -f tests/extract-win-cert.phpt

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in "" php70 php71 php72 php73 php74; do
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
     %{phpdir}/RobRichards/XMLSecLibs3


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Sep 05 2020 Shawn Iwinski <shawn@iwin.ski> - 3.1.1-1
- Update to 3.1.1 (RHBZ #1826916)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 06 2019 Shawn Iwinski <shawn@iwin.ski> - 3.0.4-1
- Update to 3.0.4 (RHBZ #1769353 / CVE-2019-3465)
- https://simplesamlphp.org/security/201911-01

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 26 2018 Remi Collet <remi@remirepo.net> - 3.0.3-1
- update to 3.0.3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 08 2017 Shawn Iwinski <shawn@iwin.ski> - 3.0.1-1
- Update to 3.0.1 (RHBZ #1487196)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 12 2017 Shawn Iwinski <shawn@iwin.ski> - 3.0.0-1
- Initial package
