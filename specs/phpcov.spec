# fedora/remirepo spec file for phpcov
#
# Copyright (c) 2013-2023 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_without tests

# For compatibility with SCL
%undefine __brp_mangle_shebangs

%global gh_commit    05307478b8f4b2a50c508d6f4eca15704cf7c1fd
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   phpcov
%global php_home     %{_datadir}/php
# Packagist
%global pk_vendor    phpunit
%global pk_project   phpcov
# Namespace
%global ns_vendor    SebastianBergmann
%global ns_project   PHPCOV


Name:           %{pk_project}
Version:        9.0.2
Release:        5%{?dist}
Summary:        CLI frontend for PHP_CodeCoverage

License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

# Fix autoload for RPM
Patch0:         %{gh_project}-rpm.patch

BuildArch:      noarch
BuildRequires:  php(language) >= 8.1
BuildRequires:  php-fedora-autoloader-devel
%if %{with tests}
BuildRequires:  phpunit10
BuildRequires:  (php-composer(phpunit/php-code-coverage) >= 10.1   with php-composer(phpunit/php-code-coverage) < 11)
BuildRequires:  (php-composer(phpunit/php-file-iterator) >= 4.0    with php-composer(phpunit/php-file-iterator) < 5)
BuildRequires:  (php-composer(sebastian/cli-parser)      >= 2.0    with php-composer(sebastian/cli-parser)      < 3)
BuildRequires:  (php-composer(sebastian/diff)            >= 5.0    with php-composer(sebastian/diff)            < 6)
BuildRequires:  (php-composer(sebastian/version)         >= 4.0    with php-composer(sebastian/version)         < 5)
BuildRequires:  php-pecl(Xdebug) >= 3
%endif

# from composer.json
#        "php": ">=8.1",
#        "phpunit/phpunit": "^10.0",
#        "phpunit/php-code-coverage": "^10.0",
#        "phpunit/php-file-iterator": "^4.0",
#        "sebastian/cli-parser": "^2.0",
#        "sebastian/diff": "^5.0",
#        "sebastian/version": "^4.0"
Requires:       php(language) >= 8.1
Requires:       phpunit10
Requires:       (php-composer(phpunit/php-code-coverage) >= 10.1.5 with php-composer(phpunit/php-code-coverage) < 11)
Requires:       (php-composer(phpunit/php-file-iterator) >= 4.0    with php-composer(phpunit/php-file-iterator) < 5)
Requires:       (php-composer(sebastian/cli-parser)      >= 2.0    with php-composer(sebastian/cli-parser)      < 3)
Requires:       (php-composer(sebastian/diff)            >= 5.0    with php-composer(sebastian/diff)            < 6)
Requires:       (php-composer(sebastian/version)         >= 4.0    with php-composer(sebastian/version)         < 5)
# from phpcompatinfo report for version 4.0.0
# none

Obsoletes:      php-phpunit-phpcov < 4
Provides:       php-phpunit-phpcov = %{version}
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
%{pk_project} is a command-line frontend for the PHP_CodeCoverage library.


%prep
%setup -q -n %{gh_project}-%{gh_commit}

%patch -P0 -p0 -b .rpm


%build
phpab \
  --template fedora \
  --output   src/autoload.php \
  src

cat << 'EOF' | tee -a src/autoload.php
// Dependencies
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/PHPUnit10/autoload.php',
    '%{php_home}/%{ns_vendor}/CodeCoverage10/autoload.php',
    '%{php_home}/%{ns_vendor}/FileIterator4/autoload.php',
    '%{php_home}/%{ns_vendor}/CliParser2/autoload.php',
    '%{php_home}/%{ns_vendor}/Diff5/autoload.php',
    '%{php_home}/%{ns_vendor}/Version4/autoload.php',
]);
EOF


%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}

install -D -p -m 755 %{pk_project} %{buildroot}%{_bindir}/%{pk_project}


%check
%if %{with tests}
mkdir vendor
ln -s %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}/autoload.php vendor/autoload.php

if ! php -v | grep Xdebug
then EXT="-d zend_extension=xdebug.so"
fi

# test with hardcoded path in data
rm tests/end-to-end/execute/valid-script-argument-with-cli-include-with-text-report.phpt
rm tests/end-to-end/merge/valid-directory-with-text-report.phpt
rm tests/end-to-end/merge/valid-directory-with-text-report-stdout.phpt
rm tests/end-to-end/patch-coverage/valid-arguments-with-valid-path-prefix.phpt

ret=0
for cmd in php php81 php82 php83; do
  if which $cmd; then
    $cmd $EXT -d xdebug.mode=coverage %{_bindir}/phpunit10 --testsuite end-to-end || ret=1
  fi
done
exit $ret;
%else
: Test suite skipped
%endif


%files
%license LICENSE
%doc README.md
%doc composer.json
%{php_home}/%{ns_vendor}/%{ns_project}
%{_bindir}/%{pk_project}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Sep 13 2023 Remi Collet <remi@remirepo.net> - 9.0.2-1
- update to 9.0.2
- raise dependency on phpunit/php-code-coverage 10.1.5

* Mon Sep 11 2023 Remi Collet <remi@remirepo.net> - 9.0.1-1
- update to 9.0.1

* Fri Sep  1 2023 Remi Collet <remi@remirepo.net> - 9.0.0-1
- update to 9.0.0
- raise dependency on PHP 8.1
- raise dependency on phpunit/phpunit 10
- raise dependency on phpunit/php-code-coverage 10
- raise dependency on phpunit/php-file-iterator 4
- raise dependency on sebastian/cli-parser 2
- raise dependency on sebastian/diff 5
- raise dependency on sebastian/version 4

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Mar 24 2022 Remi Collet <remi@remirepo.net> - 8.2.1-1
- update to 8.2.1

* Tue Mar 22 2022 Remi Collet <remi@remirepo.net> - 8.2.0-5
- fix for phpunit/php-code-coverage 9.2.13
  from https://github.com/sebastianbergmann/phpcov/pull/116

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jan 29 2021 Remi Collet <remi@remirepo.net> - 8.2.0-2
- fix test suite and FTBFS

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct  2 2020 Remi Collet <remi@remirepo.net> - 8.2.0-1
- update to 8.2.0
- raise dependency on phpunit/php-code-coverage 9.2

* Wed Sep 23 2020 Remi Collet <remi@remirepo.net> - 8.1.2-1
- update to 8.1.2 (no change)
- raise dependency on phpunit/php-code-coverage 9.1.11

* Fri Sep 11 2020 Remi Collet <remi@remirepo.net> - 8.1.1-1
- update to 8.1.1 (no change)

* Thu Aug 13 2020 Remi Collet <remi@remirepo.net> - 8.1.0-1
- update to 8.1.0
- sources from git snapshot
- add dependency on phpunit/php-file-iterator
- add dependency on sebastian/cli-parser
- drop depency on sebastian/finder-facade
- drop dependency on Symfony
- raise dependency on phpunit/phpunit 9.3
- raise dependency on phpunit/php-code-coverage 9.1

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Mar  5 2020 Remi Collet <remi@remirepo.net> - 7.0.2-1
- update to 7.0.2
- raise dependency on PHP 7.3
- raise dependency on phpunit/phpunit 9
- raise dependency on phpunit/php-code-coverage 8
- raise dependency on sebastian/diff 4
- raise dependency on sebastian/finder-facade 2
- raise dependency on sebastian/version 3
- allow Symfony 5

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 18 2019 Remi Collet <remi@remirepo.net> - 6.0.1-1
- update to 6.0.1 (no change)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 20 2019 Remi Collet <remi@remirepo.net> - 6.0.0-1
- update to 6.0.0
- raise dependency on PHP 7.2
- raise dependency on phpunit/php-code-coverage 7
- switch from phpunit7 to phpunit8
- ensure XDebug is enabled to run the test suite

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb  6 2018 Remi Collet <remi@remirepo.net> - 5.0.0-1
- Update to 5.0.0
- raise dependency on PHP 7.1
- only for phpunit7
- raise dependency on phpunit/php-code-coverage 6
- raise dependency on sebastian/diff 3

* Fri Feb  2 2018 Remi Collet <remi@remirepo.net> - 4.0.5-1
- Update to 4.0.5
- allow phpunit7
- use package names on EL and Fedora < 27

* Thu Jan 18 2018 Remi Collet <remi@remirepo.net> - 4.0.4-1
- Update to 4.0.4 (no change)
- raise dependency on symfony/console 3
- use range dependency on F27

* Sun Nov 19 2017 Remi Collet <remi@remirepo.net> - 4.0.3-1
- Update to 4.0.3
- Allow Symfony 4

* Sun Oct 22 2017 Remi Collet <remi@remirepo.net> - 4.0.2-1
- Update to 4.0.2
- raise dependency on phpunit/php-code-coverage 5.2.1
- drop dependency on php-phpunit-diff
- add dependency on php-sebastian-diff2

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Apr 28 2017 Remi Collet <remi@remirepo.net> - 4.0.1-1
- Update to 4.0.1

* Mon Apr 24 2017 Remi Collet <remi@remirepo.net> - 4.0.0-2
- fix composer provide (from review #1420384)
- fix composer.json perm

* Wed Feb  8 2017 Remi Collet <remi@fedoraproject.org> - 4.0.0-1
- rename to phpcov
- update to 4.0.0
- change dependencies to PHPUnit v6

* Fri Jun  3 2016 Remi Collet <remi@fedoraproject.org> - 3.1.0-1
- Update to 3.1.0
- raise dependency on phpunit/php-code-coverage >= 4.0
- drop the autoloader template, simply generate it

* Mon Apr 18 2016 Remi Collet <remi@fedoraproject.org> - 3.0.0-3
- allow sebastian/version 2.0

* Sat Jan  9 2016 Remi Collet <remi@fedoraproject.org> - 3.0.0-1
- update to 3.0.0
- raise minimal PHP version to 5.6
- raise dependencies on phpunit ~5.0, php-code-coverage ~3.0
- allow symfony 3
- run test suite with both PHP 6 and 7 when available

* Mon Oct  5 2015 Remi Collet <remi@fedoraproject.org> - 2.0.2-1
- update to 2.0.2
- allow PHPUnit 5

* Wed Jun 25 2014 Remi Collet <remi@fedoraproject.org> - 2.0.1-1
- update to 2.0.1
- composer dependencies

* Wed Apr 30 2014 Remi Collet <remi@fedoraproject.org> - 2.0.0-1
- update to 2.0.0
- sources from github

* Thu Sep 12 2013 Remi Collet <remi@fedoraproject.org> - 1.1.0-1
- initial package
