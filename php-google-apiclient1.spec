#
# Fedora spec file for php-google-apiclient1
#
# Copyright (c) 2014-2021 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     google
%global github_name      google-api-php-client
%global github_version   1.1.7
%global github_commit    400f250a30ae1dd4c4a0a4f750fe973fc70e6311

%global composer_vendor  google
%global composer_project apiclient

# "php": ">=5.2.1"
%global php_min_ver 5.2.1

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}1
Version:       %{github_version}
Release:       16%{?dist}
Summary:       Client library for Google APIs (version 1)

License:       ASL 2.0
URL:           https://developers.google.com/api-client-library/php/
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

# PHP 8 fixes
Patch0:        %{name}-php8-fixes.patch

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
## phpcompatinfo (computed from version 1.1.7)
BuildRequires: php-curl
BuildRequires: php-date
BuildRequires: php-filter
BuildRequires: php-json
BuildRequires: php-openssl
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-session
BuildRequires: php-spl
%endif

Requires:      ca-certificates
# composer.json
Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 1.1.7)
Requires:      php-curl
Requires:      php-date
Requires:      php-json
Requires:      php-openssl
Requires:      php-pcre
Requires:      php-reflection
Requires:      php-spl

# Weak dependencies
%if 0%{?fedora} >= 21
Suggests:      php-pecl(apcu)
Suggests:      php-pecl(memcache)
Suggests:      php-pecl(memcached)
%endif

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

# Package rename (php-google-apiclient => php-google-apiclient1)
Obsoletes:     php-google-apiclient < 2:1.1.7-4
Provides:      php-google-apiclient = 2:%{version}-%{release}
Conflicts:     owncloud < 9.1.4-5
Conflicts:     nextcloud < 10.0.4-2

%description
Google APIs Client Library for PHP provides access to many Google APIs.
It is designed for PHP client-application developers and offers simple,
flexible, powerful API access.

Examples are available in the %{name}-examples package.

Autoloader: %{phpdir}/Google1/autoload.php


%package examples

Summary:  Client library for Google APIs: Examples
Requires: %{name} = %{version}-%{release}

# Package rename (php-google-apiclient => php-google-apiclient1)
Obsoletes:     php-google-apiclient-examples < 2:1.1.7-4
Provides:      php-google-apiclient-examples = 2:%{version}-%{release}

%description examples
%{summary}


%prep
%setup -qn %{github_name}-%{github_commit}

: PHP 8 fixes
%patch0 -p1

: Unbundle CA cert
rm -f src/Google/IO/cacerts.pem
sed "s#dirname(__FILE__)\s*.\s*'/cacerts.pem'#'%{_sysconfdir}/pki/tls/certs/ca-bundle.crt'#" \
    -i src/Google/IO/{Stream,Curl}.php

: Update examples autoload require
sed "s#.*require.*autoload.*#require_once '%{phpdir}/Google1/autoload.php';#" \
    -i examples/*.php


%build
# Empty build section, nothing required


%install
mkdir -p %{buildroot}%{phpdir}
cp -rp src/Google %{buildroot}%{phpdir}/Google1


%check
: Ensure unbundled CA cert is referenced
grep '%{_sysconfdir}/pki/tls/certs/ca-bundle.crt' --quiet \
    %{buildroot}%{phpdir}/Google1/IO/{Curl,Stream}.php

%if %{with_tests}
: Skip tests requiring network access
rm -f tests/general/ApiBatchRequestTest.php

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in php %{?rhel:php54 php55 php56 php70} php71 php72 php73 php74 php80 php81; do
    if [ "php" == "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif


%{!?_licensedir:%global license %%doc}

%files
%license LICENSE
%doc *.md
%doc composer.json
%{phpdir}/Google1

%files examples
%doc examples/*


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Sep 13 2021 Shawn Iwinski <shawn@iwin.ski> - 1.1.7-14
- Patch to allow PHP 8 to fix FTBFS (RHBZ #1987815)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 28 2017 Shawn Iwinski <shawn@iwin.ski> - 1.1.7-4
- Package rename (php-google-apiclient => php-google-apiclient1)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Oct 18 2016 James Hogarth <james.hogarth@gmail.com> - 2:1.1.7-2
- Missed an %%{epoch} for the examples subpackage

* Tue Oct 18 2016 James Hogarth <james.hogarth@gmail.com> - 2:1.1.7-1
- Downgrade to 1.1.7 (RHBZ #1386167)

* Sun Jul 24 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1.8-1
- Updated to 1.1.8 (RHBZ #1275453)
- Added weak dependencies
- Always ensure unbundled CA cert is referenced

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Oct 11 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1.5-1
- Updated to 1.1.5 (RHBZ #1266282)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 22 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1.4-1
- Updated to 1.1.4 (BZ #1222260)
- Added spec license header
- Removed autoload patch
- Added option to build without tests

* Fri Jan 02 2015 Adam Williamson <awilliam@redhat.com> - 1.1.2-2
- update autoloader relocation patch to match latest upstream submission

* Sat Dec 20 2014 Adam Williamson <awilliam@redhat.com> - 1.1.2-1
- new upstream release 1.1.2
- relocate autoloader to make it work with systemwide installation

* Sat Dec 20 2014 Adam Williamson <awilliam@redhat.com> - 1.0.6-0.3.beta
- use new %%license directory
- add Packagist/Composer provide

* Fri Nov 07 2014 Adam Williamson <awilliam@redhat.com> - 1.0.6-0.2.beta
- apply CA trust store path substitution to Curl as well as Stream

* Fri Nov 07 2014 Adam Williamson <awilliam@redhat.com> - 1.0.6-0.1.beta
- new upstream release 1.0.6-beta

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-0.3.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 19 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.3-0.2.beta
- Backported commit c6949531d2399f81a5e15caf256f156dd68e00e9 for OwnCloud
- Sub-packaged examples

* Sat Feb 08 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.3-0.1.beta
- Initial package
