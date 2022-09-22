#
# Fedora spec file for php-firephp-firephp-core
#
# Copyright (c) 2015-2021 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     firephp
%global github_name      firephp-core
%global github_version   0.5.3
%global github_commit    2585b6868fe7d3a9d1432b738c3cc547444d0348

%global composer_vendor  firephp
%global composer_project firephp-core

# Build using "--without tests" to disable tests
%bcond_without tests

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       3%{?github_release}%{?dist}
Summary:       Minimal library for sending PHP variables to browsers

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Tests
%if %{with tests}
BuildRequires: phpunit8
## phpcompatinfo (computed from version 0.5.3)
BuildRequires: php(language) >= 5.4.0
BuildRequires: php-json
BuildRequires: php-mbstring
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-spl
%endif
# Autoloader
BuildRequires: php-fedora-autoloader-devel

# phpcompatinfo (computed from version 0.5.3)
Requires:      php(language) >= 5.4.0
Requires:      php-json
Requires:      php-mbstring
Requires:      php-pcre
Requires:      php-reflection
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
FirePHP is a logging system that can display PHP variables in a browser as
an application is navigated. All communication happens via HTTP headers which
means the logging data will not interfere with the normal functioning of the
application.


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create autoloader
%{_bindir}/phpab \
  --template fedora \
  --output  lib/FirePHPCore/autoload.php \
  lib/FirePHPCore/

cat << 'AUTOLOAD' | tee -a lib/FirePHPCore/autoload.php

require_once __DIR__.'/fb.php';
AUTOLOAD


%install
: Lib
mkdir -p %{buildroot}%{phpdir}
cp -rp lib/* %{buildroot}%{phpdir}/


%check
%if %{with tests}
: Skip tests known to fail
sed \
  -e 's/function testTrace/function SKIP_testTrace/' \
  -e 's/function testException/function SKIP_testException/' \
  -i tests/Features/01-Logging.php
rm -f tests/Features/10-IgnoreInTraces.php
sed 's/function testRegisterErrorHandler/function SKIP_testRegisterErrorHandler/' \
  -i tests/Issues.php

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit8)
for PHP_EXEC in php %{?rhel:php55 php56 php70 php71} php72 php73 php74 php80 php81; do
  if [ "php" = "$PHP_EXEC" ] || which $PHP_EXEC; then
    $PHP_EXEC $PHPUNIT --verbose \
      --configuration tests/phpunit.xml \
      --bootstrap %{buildroot}%{phpdir}/FirePHPCore/autoload.php \
      || RETURN_CODE=1
  fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif


%files
# README re-used as license file since it has full license text
%{?_licensedir:%license README.md}
%doc *.md
%doc composer.json
%{phpdir}/FirePHPCore


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Sep 18 2021 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.5.3-1
- Update to 0.5.3 (RHBZ #1750366)
- Fix "FTBFS in Fedora rawhide/f35" (RHBZ #1987812)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Aug 18 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.4.0-1
- Initial package
