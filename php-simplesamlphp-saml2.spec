#
# Fedora spec file for php-simplesamlphp-saml2
#
# Copyright (c) 2016-2020 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve the changelog entries
#

%global github_owner     simplesamlphp
%global github_name      saml2
%global github_version   2.3.9
%global github_commit    452217ceae817c712237556f36cc07ec680a21ff

%global composer_vendor  simplesamlphp
%global composer_project saml2

# "php": ">=5.3.3"
%global php_min_ver 5.3.3
# "mockery/mockery": "~0.9"
%global mockery_min_ver 0.9
%global mockery_max_ver 1.0
# "psr/log": "~1.0"
#     NOTE: Min version not 1.0 because autoloader required
%global psr_log_min_ver 1.0.1
%global psr_log_max_ver 2.0
# "robrichards/xmlseclibs": "^2.1.1"
%global robrichards_xmlseclibs_min_ver 2.1.1
%global robrichards_xmlseclibs_max_ver 3.0

# Build using "--with tests" to enable tests
%global with_tests 0%{?_with_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       6%{?github_release}%{?dist}
Summary:       SAML2 PHP library from SimpleSAMLphp

License:       LGPLv2+
URL:           https://github.com/%{github_owner}/%{github_name}

# GitHub export does not include tests.
# Run php-simplesamlphp-saml2-get-source.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-composer(psr/log) >= %{psr_log_min_ver} with php-composer(psr/log) < %{psr_log_max_ver})
BuildRequires: (php-composer(robrichards/xmlseclibs) >= %{robrichards_xmlseclibs_min_ver} with php-composer(robrichards/xmlseclibs) < %{robrichards_xmlseclibs_max_ver})
BuildRequires: (php-composer(mockery/mockery) >= %{mockery_min_ver} with php-composer(mockery/mockery) < %{mockery_max_ver})
%else
BuildRequires: php-composer(psr/log) <  %{psr_log_max_ver}
BuildRequires: php-composer(psr/log) >= %{psr_log_min_ver}
BuildRequires: php-composer(robrichards/xmlseclibs) <  %{robrichards_xmlseclibs_max_ver}
BuildRequires: php-composer(robrichards/xmlseclibs) >= %{robrichards_xmlseclibs_min_ver}
BuildRequires: php-dom
BuildRequires: php-openssl
%if 0%{!?el6:1}
BuildRequires: php-composer(mockery/mockery) <  %{mockery_max_ver}
BuildRequires: php-composer(mockery/mockery) >= %{mockery_min_ver}
%endif
%endif
## phpcompatinfo (computed from version 2.3.9)
BuildRequires: php-date
BuildRequires: php-libxml
BuildRequires: php-mcrypt
BuildRequires: php-pcre
BuildRequires: php-soap
BuildRequires: php-spl
BuildRequires: php-zlib
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      php-dom
Requires:      php-openssl
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:      (php-composer(psr/log) >= %{psr_log_min_ver} with php-composer(psr/log) < %{psr_log_max_ver})
Requires:      (php-composer(robrichards/xmlseclibs) >= %{robrichards_xmlseclibs_min_ver} with php-composer(robrichards/xmlseclibs) < %{robrichards_xmlseclibs_max_ver})
%else
Requires:      php-composer(psr/log) <  %{psr_log_max_ver}
Requires:      php-composer(psr/log) >= %{psr_log_min_ver}
Requires:      php-composer(robrichards/xmlseclibs) <  %{robrichards_xmlseclibs_max_ver}
Requires:      php-composer(robrichards/xmlseclibs) >= %{robrichards_xmlseclibs_min_ver}
%endif
# phpcompatinfo (computed from version 2.3.9)
Requires:      php-date
Requires:      php-libxml
Requires:      php-pcre
Requires:      php-soap
Requires:      php-spl
Requires:      php-zlib
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}


%description
A PHP library for SAML2 related functionality. Extracted from SimpleSAMLphp [1],
used by OpenConext [2]. This library started as a collaboration between
UNINETT [3] and SURFnet [4] but everyone is invited to contribute.

Autoloader: %{phpdir}/SAML2/autoload.php

[1] https://www.simplesamlphp.org/
[2] https://www.openconext.org/
[3] https://www.uninett.no/
[4] https://www.surfnet.nl/


%prep
%setup -qn %{github_name}-%{github_commit}

: Remove upstream temporary autoloader
rm -f src/_autoload.php


%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/SAML2/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('SAML2\\', __DIR__);

\Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}/Psr/Log/autoload.php',
    '%{phpdir}/RobRichards/XMLSecLibs/autoload.php',
));
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}
cp -rp src/* %{buildroot}%{phpdir}/


%check
%if %{with_tests}
: Create pseudo Composer autoloader
mkdir vendor
cat <<'AUTOLOAD' | tee vendor/autoload.php
<?php
require '%{buildroot}%{phpdir}/SAML2/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('SAML2\\', dirname(__DIR__).'/tests/SAML2');
%if 0%{!?el6:1}
require_once '%{phpdir}/Mockery/autoload.php';
%endif
AUTOLOAD

%if 0%{?el6}
: Remove tests requiring Mockery
grep -r --files-with-matches Mockery tests | xargs rm -f
%endif

: Skip test known to fail
sed 's/function testToString/function SKIP_testToString/' \
    -i tests/SAML2/XML/saml/NameIDTest.php

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in "" %{?rhel:php54 php55} php56 php70 php71 php72 php73 php74; do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose --configuration=tools/phpunit \
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
%doc *.md
%doc composer.json
%{phpdir}/SAML2


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb 22 2020 Shawn Iwinski <shawn@iwin.ski> - 2.3.9-1
- Update to 2.3.9
- Fix FTBFS (RHBZ #1799879)
- Disable tests by default

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 12 2018 Shawn Iwinski <shawn@iwin.ski> - 2.3.8-2
- Update range dependencies' conditional to include RHEL 8+

* Sat Mar 10 2018 Shawn Iwinski <shawn@iwin.ski> - 2.3.8-1
- Update to 2.3.8 (RHBZ #1534984, SSPSA 201801-01, CVE-2018-6519, SSPSA 201802-01, CVE-2018-7644, SSPSA 201803-01, CVE-2018-7711)
- License changed from LGPLv2 to LGPLv2+
- Add "get source" script since upstream excludes tests from export
- Use range dependencies on F27+

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep 23 2017 Shawn Iwinski <shawn@iwin.ski> - 2.3.4-5
- Test with SCLs if available
- Add max version constraint to mockery/mockery BuildRequires

* Fri Sep  8 2017 Remi Collet <remi@remirepo.net> - 2.3.4-4
- add maximal version to build dependency, Fix FTBFS from Koshei

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 15 2016 Shawn Iwinski <shawn@iwin.ski> - 2.3.4-1
- Update to 2.3.4 (RHBZ #1405027)

* Sat Dec 03 2016 Shawn Iwinski <shawn@iwin.ski> - 2.3.3-1
- Update to 2.3.3 (RHBZ #1401147)
- 201612-01 (https://simplesamlphp.org/security/201612-01)

* Wed Nov 09 2016 Shawn Iwinski <shawn@iwin.ski> - 2.3.2-1
- Update to 2.3.2 (RHBZ #1393368)
- Change autoloader from php-composer(symfony/class-loader) to
  php-composer(fedora/autoloader)

* Sun Sep 25 2016 Shawn Iwinski <shawn@iwin.ski> - 2.3-1
- Update to 2.3 (RHBZ #1376301)

* Fri Jul 29 2016 Shawn Iwinski <shawn@iwin.ski> - 2.2-2
- Remove upstream temporary autoloader

* Sun Jul 10 2016 Shawn Iwinski <shawn@iwin.ski> - 2.2-1
- Initial package
