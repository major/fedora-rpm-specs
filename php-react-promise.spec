#
# Fedora spec file for php-react-promise
#
# Copyright (c) 2014-2022 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     reactphp
%global github_name      promise
%global github_version   2.9.0
%global github_commit    234f8fd1023c9158e2314fa9d7d0e6a83db42910

%global composer_vendor  react
%global composer_project promise

# "php": ">=5.4.0"
%global php_min_ver 5.4.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       2%{?github_release}%{?dist}
Summary:       A lightweight implementation of CommonJS Promises/A for PHP

License:       MIT
URL:           https://reactphp.org/promise/

# GitHub export does not include tests
# Run php-react-promise-get-source.sh to create full source
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with_tests}
BuildRequires: phpunit9
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
## phpcompatinfo (computed from version 2.8.0)
BuildRequires: php-json
BuildRequires: php-reflection
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 2.8.0)
Requires:      php-json
Requires:      php-reflection
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
A lightweight implementation of CommonJS Promises/A [1] for PHP.

Autoloader: %{phpdir}/React/Promise/autoload.php

[1] http://wiki.commonjs.org/wiki/Promises/A


%prep
%setup -qn %{github_name}-%{github_commit}

: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('React\\Promise\\', __DIR__);

\Fedora\Autoloader\Dependencies::required(array(
    __DIR__.'/functions_include.php',
));
AUTOLOAD


%build
# Empty build section, nothing required


%install
mkdir -p %{buildroot}%{phpdir}/React
cp -rp src %{buildroot}%{phpdir}/React/Promise


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require_once '%{buildroot}%{phpdir}/React/Promise/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('React\\Promise\\', __DIR__.'/tests');
\Fedora\Autoloader\Autoload::addPsr4('React\\Promise\\', __DIR__.'/tests/fixtures');
BOOTSTRAP

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit9)
for PHP_EXEC in "" php74 php80 php81; do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose --bootstrap bootstrap.php \
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
%dir %{phpdir}/React
     %{phpdir}/React/Promise


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Feb 11 2022 Remi Collet <remi@remirepo.net> - 2.9.0-1
- update to 2.9.0
- Use PHPUnit 9

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 06 2020 Shawn Iwinski <shawn@iwin.ski> - 2.8.0-1
- Update to 2.8.0 (RHBZ #1835048)
- Use PHPUnit 7

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 2019 Shawn Iwinski <shawn@iwin.ski> - 2.7.1-1
- Update to 2.7.1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 01 2018 Shawn Iwinski <shawn@iwin.ski> - 2.7.0-1
- Update to 2.7.0 (RHBZ #1590046)
- Add composer.json to repo

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 24 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.5.0-1
- Updated to 2.5.0 (RHBZ #1408344)
- Use php-composer(fedora/autoloader)
- Run upstream tests with SCLs if they are available

* Mon May 30 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.4.1-1
- Updated to 2.4.1 (RHBZ #1332742)

* Mon Apr 04 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.4.0-1
- Updated to 2.4.0 (RHBZ #1319558)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 22 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.2.0-7
- Minor updates

* Sun Jun 28 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.2.0-6
- Autoloader updates

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 12 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.2.0-4
- Use new $fedoraClassLoader concept in autoloader

* Mon Jun 01 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.2.0-3
- Use include path in autoloader

* Mon Jun 01 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.2.0-2
- Added autoloader

* Sun Jan 04 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.2.0-1
- Updated to 2.2.0 (BZ #1178411)

* Mon Oct 27 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.1.0-1
- Updated to 2.1.0

* Wed Oct 15 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.0.0-1
- Initial package
