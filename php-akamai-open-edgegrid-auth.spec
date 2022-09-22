#
# Fedora spec file for php-akamai-open-edgegrid-auth
#
# Copyright (c) 2016-2017 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     akamai
%global github_name      AkamaiOPEN-edgegrid-php
%global github_version   1.0.1
%global github_commit    7ff4d64153cf432bacfa3ffd70393bea3a930f36

%global composer_vendor  akamai-open
%global composer_project edgegrid-auth

# "php": ">=5.3"
%global php_min_ver 5.3

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       11%{?github_release}%{?dist}
Summary:       Implements the Akamai {OPEN} EdgeGrid Authentication

License:       ASL 2.0
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Autoloader
BuildRequires: php-fedora-autoloader-devel
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
## phpcompatinfo (computed from version 1.0.1)
BuildRequires: php-date
BuildRequires: php-hash
BuildRequires: php-json
BuildRequires: php-pcre
BuildRequires: php-reflection
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 1.0.1)
Requires:      php-date
Requires:      php-hash
Requires:      php-pcre
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Weak dependencies
%if 0%{?fedora} >= 21
Suggests:      php-composer(akamai-open/edgegrid-client)
%endif

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

# Broken out from client as of version 0.6.0
Conflicts:     php-akamai-open-edgegrid-client < 0.6.0

%description
This library implements the Akamai {OPEN} EdgeGrid Authentication scheme.

For more information visit the Akamai {OPEN} Developer Community [1].

Autoloader: %{phpdir}/Akamai/Open/EdgeGrid/autoload-auth.php

[1] https://developer.akamai.com/


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create autoloader
%{_bindir}/phpab --template fedora --output src/autoload-auth.php src/


%install
mkdir -p %{buildroot}%{phpdir}/Akamai/Open/EdgeGrid
cp -rp src/* %{buildroot}%{phpdir}/Akamai/Open/EdgeGrid/


%check
%if %{with_tests}
: Remove logging from PHPUnit config
sed '/log/d' phpunit.xml.dist > phpunit.xml

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in "" %{?rhel:php54 php55} php56 php70 php71 php72; do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC; then
       $PHP_EXEC $PHPUNIT \
          --bootstrap %{buildroot}%{phpdir}/Akamai/Open/EdgeGrid/autoload-auth.php \
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
%dir %{phpdir}/Akamai
%dir %{phpdir}/Akamai/Open
%dir %{phpdir}/Akamai/Open/EdgeGrid
     %{phpdir}/Akamai/Open/EdgeGrid/Authentication
     %{phpdir}/Akamai/Open/EdgeGrid/Authentication.php
     %{phpdir}/Akamai/Open/EdgeGrid/autoload-auth.php


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 08 2017 Shawn Iwinski <shawn@iwin.ski> - 1.0.1-1
- Update to 1.0.1 (RHBZ #1487623)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Shawn Iwinski <shawn@iwin.ski> - 1.0.0-1
- Update to 1.0.0 (RHBZ #1452924)

* Sat Apr 29 2017 Shawn Iwinski <shawn@iwin.ski> - 1.0.0-0.2.beta2
- Update to 1.0.0beta2 (RHBZ #1446830)

* Sat Mar 11 2017 Shawn Iwinski <shawn@iwin.ski> - 1.0.0-0.1.beta1
- Update to 1.0.0beta1 (RHBZ #1413360)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 26 2016 Shawn Iwinski <shawn@iwin.ski> - 0.6.2-1
- Update to 0.6.2 (RHBZ #1408684)

* Sat Dec 24 2016 Shawn Iwinski <shawn@iwin.ski> - 0.6.1-1
- Update to 0.6.1 (RHBZ #1405779)
- Run upstream tests with SCLs if they are available

* Fri Dec 09 2016 Shawn Iwinski <shawn@iwin.ski> - 0.6.0-2
- Temporarily skip test known to fail for PHP 7.1 (see
  https://github.com/akamai-open/AkamaiOPEN-edgegrid-php/issues/2 )
- Use php-composer(fedora/autoloader)

* Mon Oct 10 2016 Shawn Iwinski <shawn@iwin.ski> - 0.6.0-1
- Initial package
