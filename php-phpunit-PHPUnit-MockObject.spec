# remirepo/fedora spec file for php-phpunit-PHPUnit-MockObject
#
# Copyright (c) 2013-2021 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    a23b761686d50a560cc56233b9ecf49597cc9118
#global gh_date      20150902
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   phpunit-mock-objects
%global php_home     %{_datadir}/php
%global pear_name    PHPUnit_MockObject
%global pear_channel pear.phpunit.de
%global major        3.4
%global minor        4
%if %{bootstrap}
%global with_tests   %{?_with_tests:1}%{!?_with_tests:0}
%else
%global with_tests   %{?_without_tests:0}%{!?_without_tests:1}
%endif

Name:           php-phpunit-PHPUnit-MockObject
Version:        %{major}.%{minor}
Release:        10%{?dist}
Summary:        Mock Object library for PHPUnit

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}-%{gh_short}.tar.gz

# Temporary workaround, under investigation
Patch0:         %{gh_project}-3.0.0-rpm.patch
# For 7.4
Patch1:         %{gh_project}-php74.patch
# For 8.0
Patch2:         %{gh_project}-php80.patch

BuildArch:      noarch
BuildRequires:  php-fedora-autoloader-devel
%if %{with_tests}
BuildRequires:  php(language) >= 5.6
# From composer.json, "require-dev": {
#        "phpunit/phpunit": "^5.4"
BuildRequires:  php-composer(phpunit/phpunit) >= 5.4
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires:  (php-composer(phpunit/php-text-template) >= 1.2   with php-composer(phpunit/php-text-template) <  2)
BuildRequires:  (php-composer(doctrine/instantiator) >= 1.0.2     with php-composer(doctrine/instantiator) <  2)
BuildRequires:  (php-composer(sebastian/exporter) >= 1.2          with php-composer(sebastian/exporter) <  3)
%else
BuildRequires:  php-phpunit-Text-Template >= 1.2
BuildRequires:  php-doctrine-instantiator >= 1.0.2
BuildRequires:  php-phpunit-exporter      >= 1.2
%endif
%endif

# From composer.json, "require": {
#        "php": "^5.6 || ^7.0",
#        "phpunit/php-text-template": "^1.2",
#        "doctrine/instantiator": "^1.0.2",
#        "sebastian/exporter": "^1.2 || ^2.0"
Requires:       php(language) >= 5.6
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:       (php-composer(phpunit/php-text-template) >= 1.2   with php-composer(phpunit/php-text-template) <  2)
Requires:       (php-composer(doctrine/instantiator) >= 1.0.2     with php-composer(doctrine/instantiator) <  2)
Requires:       (php-composer(sebastian/exporter) >= 1.2          with php-composer(sebastian/exporter) <  3)
%else
Requires:       php-phpunit-Text-Template >= 1.2
Requires:       php-doctrine-instantiator >= 1.0.2
Requires:       php-phpunit-exporter      >= 1.2
%endif
# From composer.json, "suggest": {
#        "ext-soap": "*"
Requires:       php-soap
# From phpcompatinfo report for version 3.2.0
Requires:       php-pcre
Requires:       php-reflection
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From composer.json, "conflict": {
#        "phpunit/phpunit": "<5.4.0"
Conflicts:      php-composer(phpunit/phpunit) < 5.4


Provides:       php-composer(phpunit/phpunit-mock-objects) = %{version}


%description
Mock Object library for PHPUnit


%prep
%setup -q -n %{gh_project}-%{gh_commit}

%patch0 -p0
%patch1 -p1
%patch2 -p1

find . -name \*.orig -exec rm {} \; -print


%build
phpab \
  --template fedora \
  --output src/Framework/MockObject/Autoload.php \
  src/Framework/MockObject

cat <<EOF | tee -a src/Framework/MockObject/Autoload.php
/* dependencies */
require_once 'Text/Template/Autoload.php';
require_once 'Doctrine/Instantiator/autoload.php';
require_once 'SebastianBergmann/Exporter/autoload.php';
EOF


%install
mkdir -p   %{buildroot}%{php_home}
cp -pr src %{buildroot}%{php_home}/PHPUnit


%if %{with_tests}
%check
: Generate autoloader for tests
phpab --output tests/_fixture/autoload.php tests/_fixture/

: Fix bootstrap - vendor/autoload used in tests
mkdir vendor
ln -s %{buildroot}%{php_home}/PHPUnit/Framework/MockObject/Autoload.php vendor/autoload.php

cat <<EOF >>tests/bootstrap.php
require __DIR__ . '/_fixture/autoload.php';
EOF

FILTER="testGetMockForSingletonWithReflectionSuccess"

: Run tests - set include_path to ensure PHPUnit autoloader use it
ret=0
for cmd in php php73 php74 php80; do
  if which $cmd; then
    $cmd -d include_path=.:%{buildroot}%{php_home}:%{php_home} \
      %{_bindir}/phpunit \
        --filter "^((?!($FILTER)).)*$" \
        --no-coverage || ret=1
  fi
done
exit $ret
%endif


%post
if [ -x %{_bindir}/pear ]; then
   %{_bindir}/pear uninstall --nodeps --ignore-errors --register-only \
      %{pear_channel}/%{pear_name} >/dev/null || :
fi


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc CONTRIBUTING.md README.md composer.json
%dir %{php_home}/PHPUnit
%dir %{php_home}/PHPUnit/Framework
     %{php_home}/PHPUnit/Framework/MockObject


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Mar 18 2021 Remi Collet <remi@remirepo.net> - 3.4.4-6
- fix more deprecated usages

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-5.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-5.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-5.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 21 2019 Remi Collet <remi@remirepo.net> - 3.4.4-5
- fix deprecated usage of ReflectionType::__toString()

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-4.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec  6 2018 Remi Collet <remi@remirepo.net> - 3.4.4-4
- cleanup for EL-8

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb  2 2018 Remi Collet <remi@remirepo.net> - 3.4.4-3
- use range dependencies on F27+

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul  4 2017 Remi Collet <remi@remirepo.net> - 3.4.4-1
- Update to 3.4.4

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.3-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec  9 2016 Remi Collet <remi@fedoraproject.org> - 3.4.3-1
- Update to 3.4.3

* Sun Nov 27 2016 Remi Collet <remi@fedoraproject.org> - 3.4.2-1
- Update to 3.4.2

* Tue Nov 22 2016 Remi Collet <remi@fedoraproject.org> - 3.4.1-1
- Update to 3.4.1 (no change)
- allow sebastian/exporter 2.0
- switch to fedora/autoloader

* Mon Oct 10 2016 Remi Collet <remi@fedoraproject.org> - 3.4.0-1
- Update to 3.4.0

* Tue Oct  4 2016 Remi Collet <remi@fedoraproject.org> - 3.3.1-1
- Update to 3.3.1

* Mon Oct  3 2016 Remi Collet <remi@fedoraproject.org> - 3.3.0-1
- Update to 3.3.0

* Wed Sep  7 2016 Remi Collet <remi@fedoraproject.org> - 3.2.7-1
- Update to 3.2.7

* Wed Aug 31 2016 Remi Collet <remi@fedoraproject.org> - 3.2.6-1
- Update to 3.2.6

* Sun Jun 12 2016 Remi Collet <remi@fedoraproject.org> - 3.2.3-1
- Update to 3.2.3
- ensure cannot be installed with old PHPUnit
- raise build dependency on phpunit >= 5.4

* Thu Apr 21 2016 Remi Collet <remi@fedoraproject.org> - 3.1.3-1
- Update to 3.1.3

* Thu Mar 10 2016 Remi Collet <remi@fedoraproject.org> - 3.0.6-1
- Update to 3.0.6
- raise dependency on PHP >= 5.6
- run test suite with both PHP 5 and 7 when available

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct  2 2015 Remi Collet <remi@fedoraproject.org> - 2.3.8-1
- update to 2.3.8

* Fri Aug 21 2015 Remi Collet <remi@fedoraproject.org> - 2.3.7-1
- update to 2.3.7

* Sun Jul 26 2015 Remi Collet <remi@fedoraproject.org> - 2.3.6-1
- update to 2.3.6 (only cleanup)

* Sat Jul  4 2015 Remi Collet <remi@fedoraproject.org> - 2.3.5-1
- update to 2.3.5

* Thu Jul  2 2015 Remi Collet <remi@fedoraproject.org> - 2.3.4-3
- fix autoloader

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 Remi Collet <remi@fedoraproject.org> - 2.3.4-1
- update to 2.3.4

* Fri May 29 2015 Remi Collet <remi@fedoraproject.org> - 2.3.3-1
- update to 2.3.3
- fix regression (thanks to Koschei)

* Thu May 28 2015 Remi Collet <remi@fedoraproject.org> - 2.3.2-1
- update to 2.3.2

* Thu Apr  2 2015 Remi Collet <remi@fedoraproject.org> - 2.3.1-1
- update to 2.3.1

* Fri Oct  3 2014 Remi Collet <remi@fedoraproject.org> - 2.3.0-1
- update to 2.3.0 for PHPUnit 4.3.0
- drop dependency on ocramius/instantiator
- add depencency on doctrine/instantiator

* Fri Oct  3 2014 Remi Collet <remi@fedoraproject.org> - 2.3.0-0
- bootstrap build

* Sun Sep  7 2014 Remi Collet <remi@fedoraproject.org> - 2.2.1-1
- update to 2.2.1
- enable test suite

* Mon Aug 11 2014 Remi Collet <remi@fedoraproject.org> - 2.2.0-1
- update to 2.2.0
- add dependency on ocramius/instantiator
- fix license handling

* Mon Jul 07 2014 Remi Collet <remi@fedoraproject.org> - 2.1.5-1
- update to 2.1.5

* Thu Jun 12 2014 Remi Collet <remi@fedoraproject.org> - 2.1.4-1
- update to 2.1.4
- add upstream patch to fix unserialize issue
  https://github.com/sebastianbergmann/phpunit-mock-objects/pull/176

* Sat Jun  7 2014 Remi Collet <remi@fedoraproject.org> - 2.1.3-1
- update to 2.1.3

* Sat Jun  7 2014 Remi Collet <remi@fedoraproject.org> - 2.1.2-1
- update to 2.1.2
- add composer provide

* Fri May 30 2014 Remi Collet <remi@fedoraproject.org> - 2.1.0-3
- upstream fix for php 5.4.29 and 5.5.13 (#1103223)

* Tue May  6 2014 Remi Collet <remi@fedoraproject.org> - 2.1.0-2
- workaround to autoload issue during check

* Sat May  3 2014 Remi Collet <remi@fedoraproject.org> - 2.1.0-1
- update to 2.1.0 for PHPUnit 4.1
- sources from gthub
- run tests when build --with tests option

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jan 13 2013 Remi Collet <remi@fedoraproject.org> - 1.2.3-1
- Version 1.2.3 (stable) - API 1.2.0 (stable)

* Mon Nov  5 2012 Remi Collet <remi@fedoraproject.org> - 1.2.2-1
- Version 1.2.2 (stable) - API 1.2.0 (stable)

* Mon Oct 22 2012 Remi Collet <remi@fedoraproject.org> - 1.2.1-1.1
- Version 1.2.1 (stable) - API 1.2.0 (stable)
- raise dependencies: php 5.3.3, PHPUnit 3.7.0

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 19 2012 Remi Collet <remi@fedoraproject.org> - 1.1.1-1
- Version 1.1.1 (stable) - API 1.1.0 (stable)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 01 2011 Remi Collet <remi@fedoraproject.org> - 1.1.0-1
- Version 1.1.0 (stable) - API 1.1.0 (stable)

* Fri Jun 10 2011 Remi Collet <Fedora@famillecollet.com> - 1.0.9-1
- Version 1.0.9 (stable) - API 1.0.4 (stable)
- remove PEAR hack (only needed for EPEL)
- raise PEAR dependency to 1.9.2

* Tue May  3 2011 Remi Collet <Fedora@famillecollet.com> - 1.0.8-2
- rebuild for doc in /usr/share/doc/pear

* Wed Feb 16 2011 Remi Collet <Fedora@famillecollet.com> - 1.0.8-1
- Version 1.0.8 (stable) - API 1.0.4 (stable)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Feb 05 2011 Remi Collet <Fedora@famillecollet.com> - 1.0.7-1
- Version 1.0.7 (stable) - API 1.0.4 (stable)

* Tue Jan 18 2011 Remi Collet <Fedora@famillecollet.com> - 1.0.6-1
- Version 1.0.6 (stable) - API 1.0.4 (stable)

* Tue Jan 18 2011 Remi Collet <Fedora@famillecollet.com> - 1.0.5-1
- Version 1.0.5 (stable) - API 1.0.4 (stable)
- CHANGELOG and LICENSE are now in the tarball

* Mon Nov 22 2010 Remi Collet <Fedora@famillecollet.com> - 1.0.3-1
- Version 1.0.3 (stable) - API 1.0.3 (stable)

* Wed Nov 17 2010 Remi Collet <Fedora@famillecollet.com> - 1.0.2-1
- Version 1.0.2 (stable) - API 1.0.0 (stable)

* Fri Nov 05 2010 Remi Collet <Fedora@famillecollet.com> - 1.0.1-2
- lower PEAR dependency to allow el6 build
- fix URL

* Mon Oct 25 2010 Remi Collet <Fedora@famillecollet.com> - 1.0.1-1
- Version 1.0.1 (stable) - API 1.0.0 (stable)

* Sun Sep 26 2010 Remi Collet <Fedora@famillecollet.com> - 1.0.0-1
- initial generated spec + clean

