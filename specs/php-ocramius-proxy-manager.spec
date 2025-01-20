#
# Fedora spec file for php-ocramius-proxy-manager
#
# Copyright (c) 2015-2021 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner      Ocramius
%global github_name       ProxyManager
%global github_version    2.2.3
%global github_commit     4d154742e31c35137d5374c998e8f86b54db2e2f
%global github_short      %(c=%{github_commit}; echo ${c:0:7})

%global composer_vendor   ocramius
%global composer_project  proxy-manager

# "php": "^7.2.0"
%global php_min_ver 7.2
# "zendframework/zend-code": "^3.3.0"
%global zf_min_ver  3.3
%global zf_max_ver  4

# Build using "--with tests" to enable tests
%bcond_with tests

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       13%{?github_release}%{?dist}
Summary:       OOP proxy wrappers utilities

License:       MIT
URL:           http://ocramius.github.io/ProxyManager/
Source0:       %{name}-%{github_version}-%{github_short}.tgz
# git snapshot to retrieve test suite
Source1:       makesrc.sh

# Hardcode library version
# drop dependency on ocramius/package-versions
Patch0:        %{name}-rpm.patch

BuildArch:     noarch
# Autoloader
BuildRequires: php-fedora-autoloader-devel
%if %{with tests}
# Tests
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: (php-autoloader(zendframework/zend-code) >= %{zf_min_ver}  with php-autoloader(zendframework/zend-code) <  %{zf_max_ver})
BuildRequires: php-composer(ocramius/generated-hydrator) >= 2
## phpcompatinfo (computed from version 2.2.0)
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-spl
BuildRequires: phpunit7
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:     (php-autoloader(zendframework/zend-code) >= %{zf_min_ver}  with php-autoloader(zendframework/zend-code) <  %{zf_max_ver})
# phpcompatinfo (computed from version 2.2.0)
Requires:      php-pcre
Requires:      php-reflection
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Weak dependencies
%if 0%{?fedora} >= 21
Suggests:      php-composer(ocramius/generated-hydrator)
Suggests:      php-autoloader(zendframework/zend-json)
Suggests:      php-autoloader(zendframework/zend-soap)
Suggests:      php-autoloader(zendframework/zend-stdlib)
Suggests:      php-autoloader(zendframework/zend-xmlrpc)
%endif
# For autoloader
Conflicts:     php-ocramius-generated-hydrator < 2

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}


%description
This library aims at providing abstraction for generating various kinds
of proxy classes.

Autoloader: %{phpdir}/ProxyManager/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}

%patch -P0 -p0
sed -e 's/@VERSION@/%{version}/' \
    -e 's/@COMMIT@/%{github_commit}/' \
    -i src/ProxyManager/Version.php
grep ' return' src/ProxyManager/Version.php


%build
: Generate autoloader
%{_bindir}/phpab --template fedora --output src/ProxyManager/autoload.php src/ProxyManager

cat <<'AUTOLOAD' | tee -a src/ProxyManager/autoload.php

\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/Zend/Code/autoload.php',
]);
\Fedora\Autoloader\Dependencies::optional([
    '%{phpdir}/GeneratedHydrator/autoload.php',
    '%{phpdir}/Zend/Json/autoload.php',
    '%{phpdir}/Zend/Soap/autoload.php',
    '%{phpdir}/Zend/Stdlib/autoload.php',
    '%{phpdir}/Zend/XmlRpc/autoload.php',
]);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}
cp -rp src/* %{buildroot}%{phpdir}/


%check
%if %{with tests}
: Create tests autoload
mkdir vendor
%{_bindir}/phpab --output vendor/autoload.php tests
cat << 'EOF' | tee -a vendor/autoload.php
require_once '%{buildroot}%{phpdir}/ProxyManager/autoload.php';
EOF

: Zend => Laminas
if [ -d /usr/share/php/Laminas ]
then sed -i "s/'Zend/'Laminas/" \
     tests/ProxyManagerTest/ProxyGenerator/RemoteObject/MethodGenerator/RemoteObjectMethodTest.php
fi

rm tests/language-feature-scripts/lazy-loading-value-holder-internal-php-classes.phpt

: Run tests
RETURN_CODE=0
for PHP_EXEC in php php73 php74 php80; do
    if [ "php" == "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC %{_bindir}/phpunit7 \
            --filter '^((?!(testCodeGeneration)).)*$' \
            --verbose \
            || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif


%files
%license LICENSE
%doc *.md
%doc composer.json
%{phpdir}/ProxyManager


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Feb 07 2023 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.2.3-8
- Disable tests by default
- FTBFS (RHBZ #2046826)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Mar 24 2021 Remi Collet <remi@remirepo.net> - 2.2.3-3
- skip tests failing with PHP 8
- switch to phpunit7

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 11 2021 Remi Collet <remi@remirepo.net> - 2.2.3-1
- update to 2.2.3

* Fri Jul 31 2020 Merlin Mathesius <mmathesi@redhat.com> - 2.2.2-4
- Minor conditional fix for ELN

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Feb 23 2020 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.2.2-3
- Fix FTBFS (RHDB #1799874)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 29 2019 Remi Collet <remi@remirepo.net> - 2.2.2-1
- update to 2.2.2
- raise dependency on PHP 7.2
- raise dependency on zend-code 3.3
- use zendframework component autoloaders instead of framework one

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May  4 2017 Remi Collet <remi@remirepo.net> - 2.1.1-1
- Update to 2.1.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 30 2016 Remi Collet <remi@fedoraproject.org> - 2.1.0-1
- update to 2.1.0
- raise dependency on php 7.1
- raise dependency on zendframework/zend-code 3.1
- raise dependency on ocramius/generated-hydrator 2

* Sun Oct 30 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.2-2
- Remove test file completely instead of skipping only test in it

* Tue Oct 18 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.2-1
- Update to 1.0.2 (RHBZ #1251784)
- Add weak dependencies
- Use dependencies' autoloaders
- Temporarily skip tests on Fedora 25+ (RHBZ #1350615)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 29 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.0-2
- Fix autoloader to load all optional pkgs
- Some spec cleanup

* Sat May 16 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.0-1
- Initial package
