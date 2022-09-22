%global github_owner     igorw
%global github_name      evenement
%global github_version   3.0.1
%global github_commit    531bfb9d15f8aa57454f5f0285b18bec903b8fb7

%global composer_vendor  evenement
%global composer_project evenement

# "php": ">=7.0"
%global php_min_ver 7.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_project}
Epoch:         1
Version:       %{github_version}
Release:       8%{?github_release}%{?dist}

License:       MIT
Summary:       Événement is a very simple event dispatching library for PHP
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: phpunit9
## phpcompatinfo (computed from version 3.0.1)
##     <none>
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 3.0.1)
#     <none>
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Standard "php-{COMPOSER_VENDOR}-{COMPOSER_PROJECT}" naming
Provides:      php-%{composer_vendor}-%{composer_project} = %{epoch}:%{version}-%{release}
# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}


%description
Événement is a very simple event dispatching library for PHP.

It has the same design goals as Silex and Pimple, to empower the user
while staying concise and simple.

It is very strongly inspired by the EventEmitter API found in node.js.

Autoloader: %{_datadir}/php/Evenement/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/Evenement/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Evenement\\', __DIR__);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}
cp -rp src/Evenement %{buildroot}%{phpdir}/


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require_once '%{buildroot}%{_datadir}/php/Evenement/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Evenement\\Tests\\', __DIR__.'/tests/Evenement/Tests');

\Fedora\Autoloader\Dependencies::required([
    __DIR__.'/tests/Evenement/Tests/functions.php'
]);
BOOTSTRAP

: for phpunit8/9
find tests -name \*.php \
  -exec sed \
    -e 's/function setUp()/function setUp():void/' \
    -e 's/function tearDown()/function tearDown():void/' \
    -i {} \;

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit9)
for PHP_EXEC in "" php73 php74 php80; do
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
%doc doc
%{phpdir}/Evenement


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Mar 24 2021 Remi Collet <remi@remirepo.net> - 1:3.0.1-5
- switch to phpunit9

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 2019 Shawn Iwinski <shawn@iwin.ski> - 1:3.0.1-1
- Update to 3.0.1 (RHBZ #1480022)
- Use PHPUnit 6

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 09 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.1.0-1
- Bump the epoch. The previous upgrade to version 3 broke some dependent packages.

* Thu Sep 06 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.0.1-1
- Update to 3.0.1 (#1480022).
- https://github.com/igorw/evenement/blob/v3.0.1/CHANGELOG.md

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Sep 10 2017 Shawn Iwinski <shawn@iwin.ski> - 2.1.0-1
- Update to 2.1.0
- Remove now unneeded patch
- Test with SCLs if available

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 24 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.0.0-3
- Update the patch to work for PHP 5 and PHP 7.

* Tue Jan 17 2017 Shawn Iwinski <shawn@iwin.ski> - 2.0.0-2
- Use php-composer(fedora/autoloader) instead of php-composer(symfony/class-loader)
- Install to %%{_datadir}/php/Evenement instead of %%{_datadir}/php/Evenement/Evenement

* Sat Jan 14 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.0.0-1
- Initial release.
