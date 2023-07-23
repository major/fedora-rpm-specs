# remirepo/fedora spec file for php-phpunit-PHPUnit
#
# Copyright (c) 2010-2023 Remi Collet
# Copyright (c) 2006-2009 Christopher Stone
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please, preserve the changelog entries
#

# For compatibility with SCL
%undefine __brp_mangle_shebangs

%global gh_commit    b7803aeca3ccb99ad0a506fa80b64cd6a56bbc0c
#global gh_date      20150927
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   phpunit
%global php_home     %{_datadir}/php
%global pear_name    PHPUnit
%global pear_channel pear.phpunit.de
%global major        5.7
%global minor        27

Name:           php-phpunit-PHPUnit
Version:        %{major}.%{minor}
Release:        20%{?dist}
Summary:        The PHP Unit Testing framework version 5

License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz

# Autoload template, from version 3.7
Source2:        %{gh_project}-5.4.0-Autoload.php.in

# Fix command for autoload
Patch0:         %{gh_project}-rpm.patch
# Minimal fix for PHP 8
Patch1:         %{gh_project}-php8.patch

BuildArch:      noarch
BuildRequires:  php(language) >= 5.6
BuildRequires:  %{_bindir}/phpab
BuildRequires:  (php-composer(phpunit/php-file-iterator) >= 1.4     with php-composer(phpunit/php-file-iterator) <  2)
BuildRequires:  (php-composer(phpunit/php-text-template) >= 1.2     with php-composer(phpunit/php-text-template) <  2)
BuildRequires:  (php-composer(phpunit/php-code-coverage) >= 4.0.4   with php-composer(phpunit/php-code-coverage) <  5)
BuildRequires:  (php-composer(phpunit/php-timer) >= 1.0.6           with php-composer(phpunit/php-timer) <  2)
BuildRequires:  (php-composer(phpunit/phpunit-mock-objects) >= 3.2  with php-composer(phpunit/phpunit-mock-objects) <  4)
BuildRequires:  (php-composer(phpspec/prophecy) >= 1.6.2            with php-composer(phpspec/prophecy) <  2)
BuildRequires:  (php-composer(sebastian/comparator) >= 1.2.4        with php-composer(sebastian/comparator) <  2)
BuildRequires:  (php-composer(sebastian/diff) >= 1.4.3              with php-composer(sebastian/diff) <  2)
BuildRequires:  (php-composer(sebastian/environment) >= 1.3.4       with php-composer(sebastian/environment) <  3)
BuildRequires:  (php-composer(sebastian/exporter) >= 2.0            with php-composer(sebastian/exporter) <  3)
BuildRequires:  (php-composer(sebastian/global-state) >= 1.1        with php-composer(sebastian/global-state) <  2)
BuildRequires:  (php-composer(sebastian/object-enumerator) >= 2.0   with php-composer(sebastian/object-enumerator) <  3)
BuildRequires:  (php-composer(sebastian/resource-operations) >= 1.0 with php-composer(sebastian/resource-operations) <  2)
BuildRequires:  (php-composer(sebastian/version) >= 2.0.1           with php-composer(sebastian/version) <  3)
BuildRequires:  (php-composer(myclabs/deep-copy) >= 1.3             with php-composer(myclabs/deep-copy) <  2)
BuildRequires:  (php-composer(phpunit/php-invoker) >= 1.1           with php-composer(phpunit/php-invoker) <  2)
BuildRequires:  (php-composer(doctrine/instantiator) >= 1.0.4       with php-composer(doctrine/instantiator) <  2)
BuildRequires:  (php-composer(sebastian/recursion-context) >= 2.0   with php-composer(sebastian/recursion-context) <  3)
BuildRequires:  php-symfony4-yaml
# Autoloader
BuildRequires:  php-composer(fedora/autoloader)

# From composer.json, "require": {
#        "php": "^5.6 || ^7.0",
#        "phpunit/php-file-iterator": "~1.4",
#        "phpunit/php-text-template": "~1.2",
#        "phpunit/php-code-coverage": "^4.0.4",
#        "phpunit/php-timer": "^1.0.6",
#        "phpunit/phpunit-mock-objects": "^3.2",
#        "phpspec/prophecy": "^1.6.2",
#        "symfony/yaml": "~2.1|~3.0|~4.0",
#        "sebastian/comparator": "^1.2.4",
#        "sebastian/diff": "^1.4.3",
#        "sebastian/environment": "^1.3.4 || ^2.0",
#        "sebastian/exporter": "~2.0",
#        "sebastian/global-state": "^1.1",
#        "sebastian/object-enumerator": "~2.0",
#        "sebastian/resource-operations": "~1.0",
#        "sebastian/version": "^1.0.6|^2.0.1",
#        "myclabs/deep-copy": "~1.3",
#        "ext-dom": "*",
#        "ext-json": "*",
#        "ext-mbstring": "*",
#        "ext-xml": "*",
#        "ext-libxml": "*"
Requires:       php(language) >= 5.6
Requires:       php-cli
Requires:       (php-composer(phpunit/php-file-iterator) >= 1.4     with php-composer(phpunit/php-file-iterator) <  2)
Requires:       (php-composer(phpunit/php-text-template) >= 1.2     with php-composer(phpunit/php-text-template) <  2)
Requires:       (php-composer(phpunit/php-code-coverage) >= 4.0.4   with php-composer(phpunit/php-code-coverage) <  5)
Requires:       (php-composer(phpunit/php-timer) >= 1.0.6           with php-composer(phpunit/php-timer) <  2)
Requires:       (php-composer(phpunit/phpunit-mock-objects) >= 3.2  with php-composer(phpunit/phpunit-mock-objects) <  4)
Requires:       (php-composer(phpspec/prophecy) >= 1.6.2            with php-composer(phpspec/prophecy) <  2)
Requires:       (php-composer(sebastian/comparator) >= 1.2.4        with php-composer(sebastian/comparator) <  2)
Requires:       (php-composer(sebastian/diff) >= 1.4.3              with php-composer(sebastian/diff) <  2)
Requires:       (php-composer(sebastian/environment) >= 1.3.4       with php-composer(sebastian/environment) <  3)
Requires:       (php-composer(sebastian/exporter) >= 2.0            with php-composer(sebastian/exporter) <  3)
Requires:       (php-composer(sebastian/global-state) >= 1.1        with php-composer(sebastian/global-state) <  2)
Requires:       (php-composer(sebastian/object-enumerator) >= 2.0   with php-composer(sebastian/object-enumerator) <  3)
Requires:       (php-composer(sebastian/resource-operations) >= 1.0 with php-composer(sebastian/resource-operations) <  2)
Requires:       (php-composer(sebastian/version) >= 2.0.1           with php-composer(sebastian/version) <  3)
Requires:       (php-composer(myclabs/deep-copy) >= 1.3             with php-composer(myclabs/deep-copy) <  2)
# Supported versions
Recommends:      phpunit9
Recommends:      phpunit10
Requires:       php-symfony4-yaml
Requires:       php-dom
Requires:       php-json
Requires:       php-mbstring
Requires:       php-xml
Requires:       php-libxml
# From composer.json, "suggest": {
#        "phpunit/php-invoker": "~1.1",
#        "ext-xdebug": "*"
Requires:       (php-composer(phpunit/php-invoker) >= 1.1           with php-composer(phpunit/php-invoker) <  2)
# For our autoload patch
Requires:       (php-composer(doctrine/instantiator) >= 1.0.4       with php-composer(doctrine/instantiator) <  2)
Requires:       (php-composer(sebastian/recursion-context) >= 2.0   with php-composer(sebastian/recursion-context) <  3)
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 5.6.0
Requires:       php-reflection
Requires:       php-openssl
Requires:       php-pcntl
Requires:       php-pcre
Requires:       php-phar
Requires:       php-spl


Provides:       php-composer(phpunit/phpunit) = %{version}
# For compatibility with PEAR mode
Provides:       php-pear(%{pear_channel}/%{pear_name}) = %{version}
# Package have been rename
Obsoletes:      php-pear-PHPUnit < 4
Provides:       php-pear-PHPUnit = %{version}-%{release}
# Project
Provides:       phpunit = %{version}-%{release}


%description
PHPUnit is a family of PEAR packages that supports the development of
object-oriented PHP applications using the concepts and methods of Agile
Software Development, Extreme Programming, Test-Driven Development and
Design-by-Contract Development by providing an elegant and robust framework
for the creation, execution and analysis of Unit Tests.

This package provides the version 5 of PHPUnit,
available using the phpunit command.

This version have reached its end of life in Feb 2018,
so consider using a supported version,
see https://phpunit.de/supported-versions.html

Documentation: https://phpunit.readthedocs.io/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

%patch0 -p1 -b .rpm
# Restore PSR-0 tree
mv src PHPUnit
%patch1 -p1 -b .php8

find . \( -name \*.rpm -o -name \*.php8 \) -delete -print


%build
%{_bindir}/phpab \
  --output   PHPUnit/Autoload.php \
  --template %{SOURCE2} \
  PHPUnit

%{_bindir}/phpab \
  --output   tests/autoload.php \
  --exclude  '*/BankAccountTest2.php' \
  --exclude  '*/Regression/Trac/783/OneTest.php' \
  tests


%install
mkdir -p       %{buildroot}%{php_home}
cp -pr PHPUnit %{buildroot}%{php_home}/PHPUnit

install -D -p -m 755 phpunit %{buildroot}%{_bindir}/phpunit


%check
OPT="--testsuite=small --no-coverage"

ret=0
for cmd in php php73 php74 php80 php81; do
   if which $cmd; then
      VER=$($cmd -r  'echo PHP_VERSION_ID;');
      if [ $VER -ge 80000 ]; then
        FILTER="testStaticAttributesBackupPre"
      fi
      if [ -n "$FILTER" ]; then
        OPT="$OPT --filter '^((?!($FILTER)).)*$'"
      fi
      $cmd ./phpunit $OPT --verbose
   fi
done
exit $ret


%post
if [ -x %{_bindir}/pear ]; then
   %{_bindir}/pear uninstall --nodeps --ignore-errors --register-only \
      %{pear_channel}/%{pear_name} >/dev/null || :
fi


%files
%doc README.md composer.json ChangeLog-%{major}.md
%{!?_licensedir:%global license %%doc}
%license LICENSE

%{_bindir}/phpunit
%{php_home}/PHPUnit


%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.27-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Mar 31 2023 Remi Collet <remi@remirepo.net> - 5.7.27-19
- additional fix for PHP 8

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.27-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.27-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.27-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 23 2021 Remi Collet <remi@remirepo.net> - 5.7.27-16
- additional fix for PHP 8

* Fri Sep 10 2021 Remi Collet <remi@remirepo.net> - 5.7.27-15
- add minimal fix for PHP 8.1

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.27-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Mar 25 2021 Remi Collet <remi@remirepo.net> - 5.7.27-13
- switch to Symfony 4

* Thu Mar 25 2021 Remi Collet <remi@remirepo.net> - 5.7.27-12
- recommend using a supported version

* Fri Mar 19 2021 Remi Collet <remi@remirepo.net> - 5.7.27-11
- add minimal fix for PHP 8

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.27-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.27-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.27-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.27-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 18 2019 Remi Collet <remi@remirepo.net> - 5.7.27-6
- improve package description

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.27-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec  4 2018 Remi Collet <remi@remirepo.net> - 5.7.27-4
- cleanup for EL-8

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.27-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.27-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Feb  1 2018 Remi Collet <remi@remirepo.net> - 5.7.27-1
- Update to 5.7.27
- raise dependency on sebastian/version 2.0.1
- undefine __brp_mangle_shebangs
- use range dependencies on F27+

* Mon Dec 18 2017 Remi Collet <remi@remirepo.net> - 5.7.26-1
- Update to 5.7.26

* Wed Nov 15 2017 Remi Collet <remi@remirepo.net> - 5.7.25-1
- Update to 5.7.25

* Sun Oct 15 2017 Remi Collet <remi@remirepo.net> - 5.7.23-1
- Update to 5.7.23

* Sun Sep 24 2017 Remi Collet <remi@remirepo.net> - 5.7.22-1
- Update to 5.7.22

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.21-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 24 2017 Remi Collet <remi@remirepo.net> - 5.7.21-1
- Update to 5.7.21

* Mon May 22 2017 Remi Collet <remi@remirepo.net> - 5.7.20-1
- Update to 5.7.20 (no change)
- raise dependency on sebastian/diff 1.4.3

* Mon Apr  3 2017 Remi Collet <remi@remirepo.net> - 5.7.19-1
- Update to 5.7.19

* Mon Mar 20 2017 Remi Collet <remi@remirepo.net> - 5.7.17-1
- Update to 5.7.17

* Wed Mar 15 2017 Remi Collet <remi@remirepo.net> - 5.7.16-1
- Update to 5.7.16

* Sat Mar  4 2017 Remi Collet <remi@remirepo.net> - 5.7.15-2
- fix dependency on sebastian/recursion-context

* Thu Mar  2 2017 Remi Collet <remi@remirepo.net> - 5.7.15-1
- Update to 5.7.15

* Sun Feb 19 2017 Remi Collet <remi@fedoraproject.org> - 5.7.14-1
- update to 5.7.14

* Fri Feb 10 2017 Remi Collet <remi@fedoraproject.org> - 5.7.13-1
- update to 5.7.13

* Wed Feb  8 2017 Remi Collet <remi@fedoraproject.org> - 5.7.12-1
- update to 5.7.12

* Tue Feb  7 2017 Remi Collet <remi@fedoraproject.org> - 5.7.11-2
- add max version for some build dependencies
- only allow Symfony 2
- handle redirect to composer installed PHPUnit v6

* Sun Feb  5 2017 Remi Collet <remi@fedoraproject.org> - 5.7.11-1
- update to 5.7.11
- raise dependency on sebastian/comparator 1.2.4
- raise dependency on sebastian/global-state 1.1

* Sat Jan 28 2017 Remi Collet <remi@fedoraproject.org> - 5.7.9-1
- update to 5.7.9

* Fri Jan 27 2017 Remi Collet <remi@fedoraproject.org> - 5.7.8-2
- add upstream patch

* Thu Jan 26 2017 Remi Collet <remi@fedoraproject.org> - 5.7.8-1
- update to 5.7.8
- temporary ignore testNoTestCases

* Thu Jan 26 2017 Remi Collet <remi@fedoraproject.org> - 5.7.7-1
- update to 5.7.7

* Mon Jan 23 2017 Remi Collet <remi@fedoraproject.org> - 5.7.6-1
- update to 5.7.6

* Thu Dec 29 2016 Remi Collet <remi@fedoraproject.org> - 5.7.5-1
- update to 5.7.5

* Wed Dec 14 2016 Remi Collet <remi@fedoraproject.org> - 5.7.4-1
- update to 5.7.4

* Fri Dec  9 2016 Remi Collet <remi@fedoraproject.org> - 5.7.3-1
- update to 5.7.3
- raise dependency on phpspec/prophecy 1.6.2

* Sun Dec  4 2016 Remi Collet <remi@fedoraproject.org> - 5.7.2-1
- update to 5.7.2

* Fri Dec  2 2016 Remi Collet <remi@fedoraproject.org> - 5.7.1-1
- update to 5.7.1

* Fri Dec  2 2016 Remi Collet <remi@fedoraproject.org> - 5.7.0-1
- update to 5.7.0

* Mon Nov 28 2016 Remi Collet <remi@fedoraproject.org> - 5.6.7-1
- update to 5.6.7

* Tue Nov 22 2016 Remi Collet <remi@fedoraproject.org> - 5.6.5-1
- update to 5.6.5
- raise dependency on sebastian/comparator 1.2.2
- raise dependency on sebastian/exporter 2.0
- raise dependency on sebastian/object-enumerator 2.0

* Mon Nov 14 2016 Remi Collet <remi@fedoraproject.org> - 5.6.3-1
- update to 5.6.3

* Mon Oct 31 2016 Remi Collet <remi@fedoraproject.org> - 5.6.2-2
- fix autoloader (don't use symfony one for symfony components)

* Tue Oct 25 2016 Remi Collet <remi@fedoraproject.org> - 5.6.2-1
- update to 5.6.2 (no change)
- switch to fedora/autoloader

* Fri Oct  7 2016 Remi Collet <remi@fedoraproject.org> - 5.6.1-1
- update to 5.6.1

* Fri Oct  7 2016 Remi Collet <remi@fedoraproject.org> - 5.6.0-1
- update to 5.6.0
- drop dependency on php-tidy

* Mon Oct  3 2016 Remi Collet <remi@fedoraproject.org> - 5.5.7-1
- Update to 5.5.7 (no change)
- sources from github

* Mon Oct  3 2016 Remi Collet <remi@fedoraproject.org> - 5.5.6-1
- Update to 5.5.6
- sources from a git snapshot

* Wed Sep 21 2016 Remi Collet <remi@fedoraproject.org> - 5.5.5-1
- Update to 5.5.5

* Wed Aug 31 2016 Remi Collet <remi@fedoraproject.org> - 5.5.4-1
- Update to 5.5.4

* Fri Aug  5 2016 Remi Collet <remi@fedoraproject.org> - 5.5.0-1
- Update to 5.5.0

* Tue Jul 26 2016 Remi Collet <remi@fedoraproject.org> - 5.4.8-1
- Update to 5.4.8 (no change)
- raise dependency on phpunit/php-code-coverage >= 4.0.1

* Thu Jul 21 2016 Remi Collet <remi@fedoraproject.org> - 5.4.7-1
- Update to 5.4.7

* Wed Jun 15 2016 Remi Collet <remi@fedoraproject.org> - 5.4.5-1
- Update to 5.4.5

* Thu Jun  9 2016 Remi Collet <remi@fedoraproject.org> - 5.4.4-1
- Update to 5.4.4
- raise dependency on phpunit/php-code-coverage >= 4.0
- raise dependency on phpunit/phpunit-mock-objects >= 3.2

* Wed May 11 2016 Remi Collet <remi@fedoraproject.org> - 5.3.4-1
- Update to 5.3.4

* Wed Apr 13 2016 Remi Collet <remi@fedoraproject.org> - 5.3.2-1
- Update to 5.3.2
- add dependency on sebastian/object-enumerator
- raise dependency on phpunit/phpunit-mock-objects >= 3.1

* Tue Mar 15 2016 Remi Collet <remi@fedoraproject.org> - 5.2.12-1
- Update to 5.2.12

* Thu Mar 10 2016 Remi Collet <remi@fedoraproject.org> - 5.2.10-1
- Update to 5.2.10
- raise dependency on PHP >= 5.6
- raise dependency on php-file-iterator >= 1.4
- raise dependency on php-code-coverage >= 3.3.0
- raise dependency on phpunit-mock-objects >= 3.0
- raise dependency on sebastian/diff >= 1.2
- add dependency on sebastian/resource-operations
- add dependency on myclabs/deep-copy

* Thu Feb 11 2016 Remi Collet <remi@fedoraproject.org> - 4.8.23-1
- Update to 4.8.23

* Tue Feb  2 2016 Remi Collet <remi@fedoraproject.org> - 4.8.22-1
- Update to 4.8.22

* Wed Nov 11 2015 Remi Collet <remi@fedoraproject.org> - 4.8.17-1
- Update to 4.8.17

* Thu Oct 22 2015 Remi Collet <remi@fedoraproject.org> - 4.8.15-1
- Update to 4.8.15

* Sat Oct 17 2015 Remi Collet <remi@fedoraproject.org> - 4.8.14-1
- Update to 4.8.14

* Mon Oct 12 2015 Remi Collet <remi@fedoraproject.org> - 4.8.12-1
- Update to 4.8.12

* Wed Oct  7 2015 Remi Collet <remi@fedoraproject.org> - 4.8.11-1
- Update to 4.8.11

* Fri Oct  2 2015 Remi Collet <remi@fedoraproject.org> - 4.8.10-1
- Update to 4.8.10

* Sun Sep 27 2015 Remi Collet <remi@fedoraproject.org> - 4.8.9-2
- add --atleast-version command option, backported from 5.0

* Mon Sep 21 2015 Remi Collet <remi@fedoraproject.org> - 4.8.9-1
- Update to 4.8.9

* Sun Sep 20 2015 Remi Collet <remi@fedoraproject.org> - 4.8.8-1
- Update to 4.8.8

* Mon Sep 14 2015 Remi Collet <remi@fedoraproject.org> - 4.8.7-1
- Update to 4.8.7 (no change)

* Tue Aug 25 2015 Remi Collet <remi@fedoraproject.org> - 4.8.6-1
- Update to 4.8.6

* Fri Aug  7 2015 Remi Collet <remi@fedoraproject.org> - 4.8.0-1
- Update to 4.8.0
- raise dependency on sebastian/environment 1.3
- rely on include_path for all dependencies
- add Changelog in documentation

* Mon Jul 13 2015 Remi Collet <remi@fedoraproject.org> - 4.7.7-1
- Update to 4.7.7 (no change)

* Tue Jun 30 2015 Remi Collet <remi@fedoraproject.org> - 4.7.6-1
- Update to 4.7.6

* Tue Jun 30 2015 Remi Collet <remi@fedoraproject.org> - 4.7.5-2
- use $fedoraClassLoader autoloader

* Sun Jun 21 2015 Remi Collet <remi@fedoraproject.org> - 4.7.5-1
- Update to 4.7.5

* Thu Jun 18 2015 Remi Collet <remi@fedoraproject.org> - 4.7.4-1
- Update to 4.7.4
- raise dependency on phpunit/php-timer >= 1.0.6

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 Remi Collet <remi@fedoraproject.org> - 4.7.3-1
- Update to 4.7.3

* Sun Jun  7 2015 Remi Collet <remi@fedoraproject.org> - 4.7.2-1
- Update to 4.7.2

* Fri Jun  5 2015 Remi Collet <remi@fedoraproject.org> - 4.7.1-1
- Update to 4.7.1
- raise dependency on phpunit/php-code-coverage ~2.1
- improve autoloader

* Wed Jun  3 2015 Remi Collet <remi@fedoraproject.org> - 4.6.10-1
- Update to 4.6.10

* Fri May 29 2015 Remi Collet <remi@fedoraproject.org> - 4.6.9-1
- Update to 4.6.9

* Thu May 28 2015 Remi Collet <remi@fedoraproject.org> - 4.6.8-1
- Update to 4.6.8 (no change)

* Tue May 26 2015 Remi Collet <remi@fedoraproject.org> - 4.6.7-3
- ensure compatibility with SCL

* Tue May 26 2015 Remi Collet <remi@fedoraproject.org> - 4.6.7-2
- detect and redirect to composer installed version #1157910

* Mon May 25 2015 Remi Collet <remi@fedoraproject.org> - 4.6.7-1
- Update to 4.6.7 (no change)

* Wed Apr 29 2015 Remi Collet <remi@fedoraproject.org> - 4.6.5-1
- Update to 4.6.5

* Mon Apr 13 2015 Remi Collet <remi@fedoraproject.org> - 4.6.4-1
- Update to 4.6.4

* Tue Apr  7 2015 Remi Collet <remi@fedoraproject.org> - 4.6.2-1
- Update to 4.6.2

* Fri Apr  3 2015 Remi Collet <remi@fedoraproject.org> - 4.6.1-1
- Update to 4.6.1

* Fri Apr  3 2015 Remi Collet <remi@fedoraproject.org> - 4.6.0-1
- Update to 4.6.0
- raise dependencies on file-iterator 1.4 and diff 1.2

* Sun Mar 29 2015 Remi Collet <remi@fedoraproject.org> - 4.5.1-1
- Update to 4.5.1

* Tue Feb 24 2015 Remi Collet <remi@fedoraproject.org> - 4.5.0-1
- Update to 4.5.0
- add dependency on phpspec/prophecy
- raise dependencies on sebastian/comparator >= 1.1,
  sebastian/environment >= 1.2, sebastian/exporter >= 1.2
  and doctrine/instantiator >= 1.0.4 (for autoloader file)

* Sun Jan 25 2015 Remi Collet <remi@fedoraproject.org> - 4.4.4-1
- Update to 4.4.4
- add dependency on sebastian/recursion-context

* Sun Jan 18 2015 Remi Collet <remi@fedoraproject.org> - 4.4.2-1
- Update to 4.4.2

* Sun Dec 28 2014 Remi Collet <remi@fedoraproject.org> - 4.4.1-1
- Update to 4.4.1

* Fri Dec  5 2014 Remi Collet <remi@fedoraproject.org> - 4.4.0-1
- Update to 4.4.0
- add dependency on sebastian/global-state

* Tue Nov 11 2014 Remi Collet <remi@fedoraproject.org> - 4.3.5-1
- Update to 4.3.5
- define date.timezone in phpunit command to avoid warning

* Sat Oct 25 2014 Remi Collet <remi@fedoraproject.org> - 4.3.4-1
- Update to 4.3.4
- raise dependency on phpunit/php-file-iterator >= 1.3.2

* Fri Oct 17 2014 Remi Collet <remi@fedoraproject.org> - 4.3.3-1
- Update to 4.3.3

* Thu Oct 16 2014 Remi Collet <remi@fedoraproject.org> - 4.3.2-1
- Update to 4.3.2
- new upstream patch for "no colors" patch
- raise dependency on sebastian/environment >= 1.1

* Mon Oct  6 2014 Remi Collet <remi@fedoraproject.org> - 4.3.0-2
- only enable colors when output to a terminal (from 4.4)
- open https://github.com/sebastianbergmann/phpunit/pull/1458

* Fri Oct  3 2014 Remi Collet <remi@fedoraproject.org> - 4.3.0-1
- Update to 4.3.0
- drop dependencies on ocramius/instantiator and ocramius/lazy-map
- add dependency on doctrine/instantiator
- raise dependency on phpunit/phpunit-mock-objects >= 2.3

* Sun Aug 31 2014 Remi Collet <remi@fedoraproject.org> - 4.2.4-1
- Update to 4.2.4

* Mon Aug 18 2014 Remi Collet <remi@fedoraproject.org> - 4.2.2-1
- Update to 4.2.2

* Sun Aug 17 2014 Remi Collet <remi@fedoraproject.org> - 4.2.1-1
- Update to 4.2.1

* Mon Aug 11 2014 Remi Collet <remi@fedoraproject.org> - 4.2.0-1
- Update to 4.2.0
- raise dependency on phpunit/phpunit-mock-objects >= 2.2
- add dependency on ocramius/instantiator, ocramius/lazy-map
  and symfony/class-loader

* Fri Jul 18 2014 Remi Collet <remi@fedoraproject.org> - 4.1.4-1
- Update to 4.1.4
- composer dependencies
- add missing documentation and license

* Fri Jun 13 2014 Remi Collet <remi@fedoraproject.org> - 4.1.3-1
- Update to 4.1.3

* Sat Jun  7 2014 Remi Collet <remi@fedoraproject.org> - 4.1.2-1
- Update to 4.1.2 (no change)
- improve test suite bootstraping
- add composer provide

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 26 2014 Remi Collet <remi@fedoraproject.org> - 4.1.1-1
- Update to 4.1.1

* Tue May  6 2014 Remi Collet <remi@fedoraproject.org> - 4.1.0-2
- fix some autoload issues

* Sat May  3 2014 Remi Collet <remi@fedoraproject.org> - 4.1.0-1
- Update to 4.1.0
- sources from github
- run tests during build
- add dependencies on php-phpunit-comparator, php-phpunit-diff,
  php-phpunit-environment, php-phpunit-exporter, php-phpunit-Version

* Sun Apr 06 2014 Remi Collet <remi@fedoraproject.org> - 3.7.34-1
- Update to 3.7.34

* Mon Feb 03 2014 Remi Collet <remi@fedoraproject.org> - 3.7.31-1
- Update to 3.7.31 (no change)

* Fri Jan 31 2014 Remi Collet <remi@fedoraproject.org> - 3.7.30-1
- Update to 3.7.30

* Wed Jan 15 2014 Remi Collet <remi@fedoraproject.org> - 3.7.29-1
- Update to 3.7.29 (stable)

* Thu Oct 17 2013 Remi Collet <remi@fedoraproject.org> - 3.7.28-1
- Update to 3.7.28
- add Spec license header
- open https://github.com/sebastianbergmann/phpunit/issues/1029

* Mon Sep 16 2013 Remi Collet <remi@fedoraproject.org> - 3.7.27-1
- Update to 3.7.27 (no change)

* Tue Sep 10 2013 Remi Collet <remi@fedoraproject.org> - 3.7.25-1
- Update to 3.7.25 (no change)

* Tue Aug 20 2013 Remi Collet <remi@fedoraproject.org> - 3.7.24-1
- Update to 3.7.24

* Mon Aug 05 2013 Remi Collet <remi@fedoraproject.org> - 3.7.23-1
- Update to 3.7.23
- raise dependency on phpunit/PHP_Timer 1.0.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 08 2013 Remi Collet <remi@fedoraproject.org> - 3.7.22-1
- Update to 3.7.22

* Fri May 24 2013 Remi Collet <remi@fedoraproject.org> - 3.7.21-1
- Update to 3.7.21

* Mon May 13 2013 Remi Collet <remi@fedoraproject.org> - 3.7.20-1
- Update to 3.7.20

* Mon Mar 25 2013 Remi Collet <remi@fedoraproject.org> - 3.7.19-1
- Update to 3.7.19
- requires pear.symfony.com/Yaml >= 2.0.0, <= 2.2.99

* Sat Mar 23 2013 Remi Collet <remi@fedoraproject.org> - 3.7.18-1
- Update to 3.7.18
- Raise dependency on pear.symfony.com/Yaml >= 2.2.0

* Thu Feb 14 2013 Remi Collet <remi@fedoraproject.org> - 3.7.14-1
- Update to 3.7.14

* Sun Jan 13 2013 Remi Collet <remi@fedoraproject.org> - 3.7.13-1
- Version 3.7.13 (stable) - API 3.7.0 (stable)

* Thu Jan 10 2013 Remi Collet <remi@fedoraproject.org> - 3.7.12-1
- Version 3.7.12 (stable) - API 3.7.0 (stable)

* Wed Jan  9 2013 Remi Collet <remi@fedoraproject.org> - 3.7.11-1
- Version 3.7.11 (stable) - API 3.7.0 (stable)

* Sun Dec  2 2012 Remi Collet <remi@fedoraproject.org> - 3.7.10-1
- Version 3.7.10 (stable) - API 3.7.0 (stable)

* Wed Nov 07 2012 Remi Collet <remi@fedoraproject.org> - 3.7.9-1
- Version 3.7.9 (stable) - API 3.7.0 (stable)

* Mon Oct 22 2012 Remi Collet <remi@fedoraproject.org> - 3.7.8-1
- Version 3.7.8 (stable) - API 3.7.0 (stable)
- add Conflicts for max version of PHP_CodeCoverage and PHPUnit_MockObject
- raise dependencies: php 5.3.3, PHP_CodeCoverage 1.2.1,
  PHP_Timer 1.0.2, Yaml 2.1.0 (instead of YAML from symfony 1)

* Sat Aug 04 2012 Remi Collet <remi@fedoraproject.org> - 3.6.12-1
- Version 3.6.12 (stable) - API 3.6.0 (stable)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 07 2012 Remi Collet <remi@fedoraproject.org> - 3.6.11-1
- Version 3.6.11 (stable) - API 3.6.0 (stable)

* Fri Jan 27 2012 Remi Collet <remi@fedoraproject.org> - 3.6.10-1
- Version 3.6.10 (stable) - API 3.6.0 (stable)
- raise PHP_Invokers >= 1.1.0

* Tue Jan 24 2012 Remi Collet <remi@fedoraproject.org> - 3.6.9-1
- Version 3.6.9 (stable) - API 3.6.0 (stable)

* Sat Jan 21 2012 Remi Collet <remi@fedoraproject.org> - 3.6.8-1
- Version 3.6.8 (stable) - API 3.6.0 (stable)

* Thu Jan 05 2012 Remi Collet <remi@fedoraproject.org> - 3.6.7-1
- Version 3.6.7 (stable) - API 3.6.0 (stable)

* Mon Jan 02 2012 Remi Collet <remi@fedoraproject.org> - 3.6.6-1
- Version 3.6.6 (stable) - API 3.6.0 (stable)

* Mon Dec 19 2011 Remi Collet <remi@fedoraproject.org> - 3.6.5-1
- Version 3.6.5 (stable) - API 3.6.0 (stable)

* Sat Nov 26 2011 Remi Collet <remi@fedoraproject.org> - 3.6.4-1
- Version 3.6.4 (stable) - API 3.6.0 (stable)

* Fri Nov 11 2011 Remi Collet <remi@fedoraproject.org> - 3.6.3-1
- Version 3.6.3 (stable) - API 3.6.0 (stable)

* Fri Nov 04 2011 Remi Collet <remi@fedoraproject.org> - 3.6.2-1
- Version 3.6.2 (stable) - API 3.6.0 (stable)

* Tue Nov 01 2011 Remi Collet <remi@fedoraproject.org> - 3.6.0-1
- Version 3.6.0 (stable) - API 3.6.0 (stable)

* Fri Aug 19 2011 Remi Collet <remi@fedoraproject.org> - 3.5.15-1
- Version 3.5.15 (stable) - API 3.5.7 (stable)
- raise PEAR dependency to 1.9.3

* Fri Jun 10 2011 Remi Collet <Fedora@famillecollet.com> - 3.5.14-1
- Version 3.5.14 (stable) - API 3.5.7 (stable)

* Tue May  3 2011 Remi Collet <Fedora@famillecollet.com> - 3.5.13-2
- rebuild for doc in /usr/share/doc/pear

* Tue Mar  8 2011 Remi Collet <Fedora@famillecollet.com> - 3.5.13-1
- Version 3.5.13 (stable) - API 3.5.7 (stable)
- remove PEAR hack (only needed for EPEL)
- raise PEAR dependency to 1.9.2
- remove duplicate dependency (YAML)

* Thu Feb 24 2011 Remi Collet <Fedora@famillecollet.com> - 3.5.12-1
- Version 3.5.12 (stable) - API 3.5.7 (stable)

* Wed Feb 16 2011 Remi Collet <Fedora@famillecollet.com> - 3.5.11-1
- Version 3.5.11 (stable) - API 3.5.7 (stable)
- new dependency on php-pear(XML_RPC2)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 20 2011 Remi Collet <Fedora@famillecollet.com> - 3.5.10-1
- Version 3.5.10 (stable) - API 3.5.7 (stable)

* Tue Jan 18 2011 Remi Collet <Fedora@famillecollet.com> - 3.5.9-1
- Version 3.5.9 (stable) - API 3.5.7 (stable)

* Tue Jan 11 2011 Remi Collet <Fedora@famillecollet.com> - 3.5.7-1
- Version 3.5.7 (stable) - API 3.5.7 (stable)
- README, CHANGELOG and LICENSE are now in the tarball

* Mon Dec 20 2010 Remi Collet <Fedora@famillecollet.com> - 3.5.6-1
- Version 3.5.6 (stable) - API 3.5.4 (stable)
- move README.mardown to README (was Changelog, now links to doc)
- add CHANGELOG
- not more doc provided by upstream

* Mon Nov 22 2010 Remi Collet <Fedora@famillecollet.com> - 3.5.5-1
- Version 3.5.5 (stable) - API 3.5.4 (stable)

* Wed Nov 17 2010 Remi Collet <Fedora@famillecollet.com> - 3.5.4-1
- Version 3.5.4 (stable) - API 3.5.4 (stable)

* Wed Oct 27 2010 Remi Collet <Fedora@famillecollet.com> - 3.5.3-1
- Update to 3.5.3
- new requires and new packages for extensions of PHPUnit
  PHPUnit_MockObject, PHPUnit_Selenium, DbUnit
- lower PEAR dependency to allow el6 build
- define timezone during build

* Thu Jul 22 2010 Remi Collet <Fedora@famillecollet.com> - 3.4.15-1
- Update to 3.4.15

* Sat Jun 19 2010 Remi Collet <Fedora@famillecollet.com> - 3.4.14-1
- Update to 3.4.14

* Sat May 22 2010 Remi Collet <Fedora@famillecollet.com> - 3.4.13-1
- Update to 3.4.13
- add README.markdown (Changelog)

* Wed Apr 07 2010 Remi Collet <Fedora@famillecollet.com> - 3.4.12-1
- Update to 3.4.12

* Thu Feb 18 2010 Remi Collet <Fedora@famillecollet.com> - 3.4.11-1.1
- Update to 3.4.11

* Wed Feb 10 2010 Remi Collet <Fedora@famillecollet.com> - 3.4.10-1
- Update to 3.4.10

* Sun Jan 24 2010 Remi Collet <Fedora@famillecollet.com> - 3.4.9-1
- Update to 3.4.9

* Sat Jan 16 2010 Remi Collet <Fedora@famillecollet.com> - 3.4.7-1
- Update to 3.4.7
- rename from php-pear-PHPUnit to php-phpunit-PHPUnit
- update dependencies (PEAR 1.8.1, YAML, php-soap)

* Sat Sep 12 2009 Christopher Stone <chris.stone@gmail.com> 3.3.17-1
- Upstream sync

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 02 2009 Remi Collet <Fedora@famillecollet.com> - 3.3.16-1
- Upstream sync
- Fix requires (remove hint) and raise PEAR version to 1.7.1
- rename %%{pear_name}.xml to %%{name}.xml

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov  8 2008 Christopher Stone <chris.stone@gmail.com> 3.3.4-1
- Upstream sync

* Thu Oct 23 2008 Christopher Stone <chris.stone@gmail.com> 3.3.2-1
- Upstream sync
- Remove no longer needed Obsolete/Provides

* Thu Oct 09 2008 Christopher Stone <chris.stone@gmail.com> 3.3.1-1
- Upstream sync

* Thu Oct 09 2008 Christopher Stone <chris.stone@gmail.com> 3.2.21-1
- Upstream sync
- Add php-xml to Requires (bz #464758)

* Thu May 22 2008 Christopher Stone <chris.stone@gmail.com> 3.2.19-1
- Upstream sync

* Thu Feb 21 2008 Christopher Stone <chris.stone@gmail.com> 3.2.15-1
- Upstream sync

* Wed Feb 13 2008 Christopher Stone <chris.stone@gmail.com> 3.2.13-1
- Upstream sync

* Sun Nov 25 2007 Christopher Stone <chris.stone@gmail.com> 3.2.1-1
- Upstream sync

* Sat Sep 08 2007 Christopher Stone <chris.stone@gmail.com> 3.1.8-1
- Upstream sync

* Sun May 06 2007 Christopher Stone <chris.stone@gmail.com> 3.0.6-1
- Upstream sync

* Thu Mar 08 2007 Christopher Stone <chris.stone@gmail.com> 3.0.5-3
- Fix testdir
- Fix Provides version

* Wed Mar 07 2007 Christopher Stone <chris.stone@gmail.com> 3.0.5-2
- Add Obsoletes/Provides for php-pear(PHPUnit2)
- Requires php-pear(PEAR) >= 1.5.0
- Own %%{pear_testdir}/%%{pear_name}
- Remove no longer needed manual channel install
- Simplify %%doc
- Only unregister old phpunit on upgrade

* Mon Feb 26 2007 Christopher Stone <chris.stone@gmail.com> 3.0.5-1
- Upstream sync

* Wed Feb 21 2007 Christohper Stone <chris.stone@gmail.com> 3.0.4-1
- Upstream sync

* Mon Jan 29 2007 Christopher Stone <chris.stone@gmail.com> 3.0.3-1
- Upstream sync

* Sun Jan 14 2007 Christopher Stone <chris.stone@gmail.com> 3.0.2-1
- Upstream sync

* Fri Jan 05 2007 Christopher Stone <chris.stone@gmail.com> 3.0.1-1
- Upstream sync

* Wed Dec 27 2006 Christopher Stone <chris.stone@gmail.com> 3.0.0-1
- Initial Release
