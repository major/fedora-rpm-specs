# remirepo/fedora spec file for php-phpunit-PHP-CodeCoverage
#
# Copyright (c) 2013-2021 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%global bootstrap    0
%global gh_commit    ef7b2f56815df854e66ceaee8ebe9393ae36a40d
#global gh_date      20150924
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   php-code-coverage
%global php_home     %{_datadir}/php
%global pear_name    PHP_CodeCoverage
%global pear_channel pear.phpunit.de
%global major        4.0
%global minor        8
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-phpunit-PHP-CodeCoverage
Version:        %{major}.%{minor}
Release:        11%{?dist}
Summary:        PHP code coverage information

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}-%{gh_short}.tar.gz

Patch1:         https://patch-diff.githubusercontent.com/raw/sebastianbergmann/php-code-coverage/pull/554.patch

BuildArch:      noarch
BuildRequires:  php(language) >= 5.6
BuildRequires:  php-fedora-autoloader-devel
%if %{with_tests}
# From composer.json, "require-dev": {
#        "phpunit/phpunit": "^5.7",
#        "ext-xdebug": "^2.1.4"
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires:  (php-composer(phpunit/phpunit) >= 5.7                  with php-composer(phpunit/phpunit) < 6)
BuildRequires:  (php-composer(phpunit/php-file-iterator) >= 1.3        with php-composer(phpunit/php-file-iterator) <  2)
BuildRequires:  (php-composer(phpunit/php-token-stream) >= 1.4.2       with php-composer(phpunit/php-token-stream) <  3)
BuildRequires:  (php-composer(phpunit/php-text-template) >= 1.2        with php-composer(phpunit/php-text-template) <  2)
BuildRequires:  (php-composer(sebastian/code-unit-reverse-lookup) >= 1 with php-composer(sebastian/code-unit-reverse-lookup) <  2)
BuildRequires:  (php-composer(sebastian/environment) >= 1.3.2          with php-composer(sebastian/environment) <  3)
BuildRequires:  (php-composer(sebastian/version) >= 1.0                with php-composer(sebastian/version) <  3)
%else
BuildRequires:  php-phpunit-PHPUnit >= 5.7
BuildRequires:  php-phpunit-File-Iterator >= 1.3
BuildRequires:  php-phpunit-PHP-TokenStream >= 1.4.2
BuildRequires:  php-phpunit-Text-Template
BuildRequires:  php-sebastian-code-unit-reverse-lookup
BuildRequires:  php-phpunit-environment >= 1.3.2
BuildRequires:  php-phpunit-Version
%endif
BuildRequires:  php-xdebug
%endif

# From composer.json, require
#        "php": "^5.6 || ^7.0",
#        "ext-dom": "*",
#        "ext-xmlwriter": "*"
#        "phpunit/php-file-iterator": "^1.3",
#        "phpunit/php-token-stream": "^1.4.2 || ^2.0",
#        "phpunit/php-text-template": "^1.2",
#        "sebastian/code-unit-reverse-lookup": "^1.0",
#        "sebastian/environment": "^1.3.2 || ^2.0",
#        "sebastian/version": "^1.0 || ^2.0"
Requires:       php(language) >= 5.6
Requires:       php-dom
Requires:       php-xmlwriter
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:       (php-composer(phpunit/php-file-iterator) >= 1.3        with php-composer(phpunit/php-file-iterator) <  2)
Requires:       (php-composer(phpunit/php-token-stream) >= 1.4.2       with php-composer(phpunit/php-token-stream) <  3)
Requires:       (php-composer(phpunit/php-text-template) >= 1.2        with php-composer(phpunit/php-text-template) <  2)
Requires:       (php-composer(sebastian/code-unit-reverse-lookup) >= 1 with php-composer(sebastian/code-unit-reverse-lookup) <  2)
Requires:       (php-composer(sebastian/environment) >= 1.3.2          with php-composer(sebastian/environment) <  3)
Requires:       (php-composer(sebastian/version) >= 1.0                with php-composer(sebastian/version) <  3)
%else
Requires:       php-phpunit-File-Iterator >= 1.3
Requires:       php-phpunit-PHP-TokenStream >= 1.4.2
Requires:       php-phpunit-Text-Template
Requires:       php-sebastian-code-unit-reverse-lookup
Requires:       php-phpunit-environment >= 1.3.2
Requires:       php-phpunit-Version
%endif
# From composer.json, suggest
#        "ext-xdebug": "^2.5.1",
# From phpcompatinfo report for version 4.0.4
Requires:       php-reflection
Requires:       php-date
Requires:       php-json
Requires:       php-spl
Requires:       php-tokenizer
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(phpunit/php-code-coverage) = %{version}

# For compatibility with PEAR mode
Provides:       php-pear(%{pear_channel}/%{pear_name}) = %{version}


%description
Library that provides collection, processing, and rendering functionality
for PHP code coverage information.


%prep
%setup -q -n %{gh_project}-%{gh_commit}
%patch1 -p1


%build
%{_bindir}/phpab \
  --template fedora \
  --output src/autoload.php \
  src

cat << 'EOF' | tee -a src/autoload.php
// Dependencies
\Fedora\Autoloader\Dependencies::required([
    'File/Iterator/Autoload.php',
    [
        'SebastianBergmann/PhpTokenStream2/autoload.php',
        'PHP/Token/Stream/Autoload.php',
    ],
    'Text/Template/Autoload.php',
    'SebastianBergmann/CodeUnitReverseLookup/autoload.php',
    'SebastianBergmann/Environment/autoload.php',
    'SebastianBergmann/Version/autoload.php',
]);
EOF


%install
# Restore PSR-0 tree
mkdir -p   %{buildroot}%{php_home}/SebastianBergmann
cp -pr src %{buildroot}%{php_home}/SebastianBergmann/CodeCoverage


%if %{with_tests}
%check
if ! php -v | grep Xdebug
then EXT="-d zend_extension=xdebug.so"
fi

cat << 'EOF' | tee tests/bootstrap.php
<?php
require '%{buildroot}%{php_home}/SebastianBergmann/CodeCoverage/autoload.php';
require __DIR__ . '/TestCase.php';
define('TEST_FILES_PATH', __DIR__ . '/_files/');
EOF


ret=0
for cmd in php php73 php74 php80; do
  if which $cmd; then
    VER=$($cmd -r "echo PHP_VERSION_ID;")
    FILTER="testForClassWithAnonymousFunction|testTextForClassWithAnonymousFunction|testGetLinesToBeIgnored3|testCloverForClassWithAnonymousFunction"
    if [ $VER -ge 80000 ]; then
      FILTER="$FILTER|testForFileWithIgnoredLines|testCanBeConstructedForPhpdbgWithoutGivenFilterObject|testCloverForFileWithIgnoredLines"
      FILTER="$FILTER|testGetLinesToBeIgnoredOneLineAnnotations|testAddingADirectoryToTheWhitelistWorks"
    fi

    $cmd $EXT \
      -d include_path=.:%{buildroot}%{php_home}:%{php_home} \
      %{_bindir}/phpunit \
        --filter "^((?!($FILTER)).)*$" \
        --verbose || ret=1
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
%doc README.md
%doc composer.json
%doc ChangeLog-%{major}.md
%{php_home}/SebastianBergmann/CodeCoverage


%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Mar 18 2021 Remi Collet <remi@remirepo.net> - 4.0.8-6
- skip test failing on PHP 8

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.8-5.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.8-5.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.8-5.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.8-5.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.8-5.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec  6 2018 Remi Collet <remi@remirepo.net> - 4.0.8-5
- cleanup for EL-8

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.8-3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.8-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov  6 2017 Remi Collet <remi@remirepo.net> - 4.0.8-3
- adapt autoloader for php-sebastian-php-token-stream2

* Fri Nov  3 2017 Remi Collet <remi@remirepo.net> - 4.0.8-2
- fix FTBFS from Koschei, add patch for PHP 7.2 from
  https://github.com/sebastianbergmann/php-code-coverage/pull/554
- ignore test failing, know by upstream (travis)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.8-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Apr  2 2017 Remi Collet <remi@remirepo.net> - 4.0.8-1
- Update to 4.0.8

* Wed Mar  1 2017 Remi Collet <remi@fedoraproject.org> - 4.0.7-1
- Update to 4.0.7

* Thu Feb 23 2017 Remi Collet <remi@fedoraproject.org> - 4.0.6-1
- Update to 4.0.6
- drop patch merged upstream

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.5-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 22 2017 Remi Collet <remi@fedoraproject.org> - 4.0.5-1
- Update to 4.0.5
- add upstream patch for test suite to fix
  https://github.com/sebastianbergmann/php-code-coverage/issues/495
- open https://github.com/sebastianbergmann/php-code-coverage/pull/504

* Mon Nov 28 2016 Remi Collet <remi@fedoraproject.org> - 4.0.3-1
- Update to 4.0.3

* Wed Nov 23 2016 Remi Collet <remi@fedoraproject.org> - 4.0.2-2
- set serialize_precision=14 for the test suite
  to fix FTBFS with PHP 7.1

* Tue Nov  1 2016 Remi Collet <remi@fedoraproject.org> - 4.0.2-1
- Update to 4.0.2
- switch to fedora-autoloader

* Tue Jul 26 2016 Remi Collet <remi@fedoraproject.org> - 4.0.1-1
- Update to 4.0.1

* Fri Jun  3 2016 Remi Collet <remi@fedoraproject.org> - 4.0.0-1
- Update to 4.0.0
- namespace changed from PHP to SebastianBergmann
- raise build dependency on phpunit >= 5.4

* Sat May 28 2016 Remi Collet <remi@fedoraproject.org> - 3.3.3-1
- Update to 3.3.3

* Wed May 25 2016 Remi Collet <remi@fedoraproject.org> - 3.3.2-1
- Update to 3.3.2

* Wed May  4 2016 Remi Collet <remi@fedoraproject.org> - 3.3.1-2
- add upstream patch for environment 1.3.6
  https://github.com/sebastianbergmann/php-code-coverage/pull/435

* Fri Apr  8 2016 Remi Collet <remi@fedoraproject.org> - 3.3.1-1
- Update to 3.3.1

* Thu Mar 10 2016 Remi Collet <remi@fedoraproject.org> - 3.3.0-1
- Update to 3.3.0
- raise dependency on PHP >= 5.6
- raise dependency on php-token-stream >= 1.4.2
- add dependency on sebastian/code-unit-reverse-lookup

* Thu Mar 10 2016 Remi Collet <remi@fedoraproject.org> - 3.3.0-0
- Update to 3.3.0, bootstrap build

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct  7 2015 Remi Collet <remi@fedoraproject.org> - 2.2.4-1
- update to 2.2.4

* Mon Sep 14 2015 Remi Collet <remi@fedoraproject.org> - 2.2.3-1
- update to 2.2.3

* Tue Aug  4 2015 Remi Collet <remi@fedoraproject.org> - 2.2.2-1
- update to 2.2.2
- raise dependency on sebastian/environment ^1.3.2

* Sun Aug  2 2015 Remi Collet <remi@fedoraproject.org> - 2.2.1-1
- update to 2.2.1 (no change)
- raise dependency on sebastian/environment ~1.3.1

* Sat Aug  1 2015 Remi Collet <remi@fedoraproject.org> - 2.2.0-1
- update to 2.2.0
- raise dependency on sebastian/environment ~1.3

* Sun Jul 26 2015 Remi Collet <remi@fedoraproject.org> - 2.1.9-1
- update to 2.1.9 (only cleanup)

* Mon Jul 13 2015 Remi Collet <remi@fedoraproject.org> - 2.1.8-1
- update to 2.1.8

* Thu Jul  2 2015 Remi Collet <remi@fedoraproject.org> - 2.1.7-2
- fix autoloader

* Tue Jun 30 2015 Remi Collet <remi@fedoraproject.org> - 2.1.7-1
- update to 2.1.7

* Fri Jun 19 2015 Remi Collet <remi@fedoraproject.org> - 2.1.6-1
- update to 2.1.6

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun  9 2015 Remi Collet <remi@fedoraproject.org> - 2.1.5-1
- update to 2.1.5

* Sun Jun  7 2015 Remi Collet <remi@fedoraproject.org> - 2.1.4-1
- update to 2.1.4

* Wed Jun  3 2015 Remi Collet <remi@fedoraproject.org> - 2.1.3-1
- update to 2.1.3

* Mon May 25 2015 Remi Collet <remi@fedoraproject.org> - 2.0.17-1
- update to 2.0.17

* Mon Apr 13 2015 Remi Collet <remi@fedoraproject.org> - 2.0.16-1
- update to 2.0.16

* Sun Jan 25 2015 Remi Collet <remi@fedoraproject.org> - 2.0.15-1
- update to 2.0.15

* Fri Dec 26 2014 Remi Collet <remi@fedoraproject.org> - 2.0.14-1
- update to 2.0.14

* Wed Dec  3 2014 Remi Collet <remi@fedoraproject.org> - 2.0.13-1
- update to 2.0.13

* Thu Sep  4 2014 Remi Collet <remi@fedoraproject.org> - 2.0.11-2
- add BR on php-pecl-xdebug (thanks to Koschei)

* Sun Aug 31 2014 Remi Collet <remi@fedoraproject.org> - 2.0.11-1
- update to 2.0.11
- raise dependency on phpunit/php-token-stream ~1.3
- enable tests during build
- drop optional dependency on XDebug

* Mon Aug 11 2014 Remi Collet <remi@fedoraproject.org> - 2.0.10-1
- update to 2.0.10
- fix license handling

* Mon Jul 07 2014 Remi Collet <remi@fedoraproject.org> - 2.0.9-1
- update to 2.0.9

* Wed Jun 25 2014 Remi Collet <remi@fedoraproject.org> - 2.0.8-3
- composer dependencies

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Remi Collet <remi@fedoraproject.org> - 2.0.8-1
- update to 2.0.8

* Tue May  6 2014 Remi Collet <remi@fedoraproject.org> - 2.0.6-1
- update to 2.0.6 for PHPUnit 4
- sources from github
- drop dependency on php-ezc-ConsoleTools
- add dependencies on php-phpunit-environment, php-phpunit-Version
- run test when build --with tests option

* Tue Apr 01 2014 Remi Collet <remi@fedoraproject.org> - 1.2.17-1
- Update to 1.2.17

* Tue Feb 25 2014 Remi Collet <remi@fedoraproject.org> - 1.2.16-1
- Update to 1.2.16

* Mon Feb 03 2014 Remi Collet <remi@fedoraproject.org> - 1.2.15-1
- Update to 1.2.15

* Fri Jan 31 2014 Remi Collet <remi@fedoraproject.org> - 1.2.14-1
- Update to 1.2.14
- raise dependency on Text_Template 1.2.0

* Tue Sep 10 2013 Remi Collet <remi@fedoraproject.org> - 1.2.13-1
- Update to 1.2.13

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 08 2013 Remi Collet <remi@fedoraproject.org> - 1.2.12-1
- Update to 1.2.12

* Fri May 24 2013 Remi Collet <remi@fedoraproject.org> - 1.2.11-1
- Update to 1.2.11

* Mon May 13 2013 Remi Collet <remi@fedoraproject.org> - 1.2.10-1
- Update to 1.2.10

* Wed Feb 27 2013 Remi Collet <remi@fedoraproject.org> - 1.2.9-1
- Update to 1.2.9

* Thu Feb 14 2013 Remi Collet <remi@fedoraproject.org> - 1.2.8-1
- Update to 1.2.8

* Sun Dec  2 2012 Remi Collet <remi@fedoraproject.org> - 1.2.7-1
- Version 1.2.7 (stable) - API 1.2.0 (stable)

* Mon Oct 22 2012 Remi Collet <remi@fedoraproject.org> - 1.2.6-1
- Version 1.2.6 (stable) - API 1.2.0 (stable)
- raise dependency: php 5.3.3, PHP_TokenStream 1.1.3

* Wed Aug 01 2012 Remi Collet <remi@fedoraproject.org> - 1.1.3-1
- Version 1.1.3 (stable) - API 1.1.0 (stable)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Feb 23 2012 Remi Collet <remi@fedoraproject.org> - 1.1.2-1
- Version 1.1.2 (stable) - API 1.1.0 (stable)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov 04 2011 Remi Collet <remi@fedoraproject.org> - 1.1.1-1
- Version 1.1.1 (stable) - API 1.1.0 (stable)

* Tue Nov 01 2011 Remi Collet <remi@fedoraproject.org> - 1.1.0-1
- Version 1.1.0 (stable) - API 1.1.0 (stable)
- no more phpcov script in bindir

* Fri Aug 19 2011 Remi Collet <remi@fedoraproject.org> - 1.0.5-1
- Version 1.0.5 (stable) - API 1.0.3 (stable)
- remove PEAR hack (only needed for EPEL)
- raise PEAR dependency to 1.9.2

* Tue May  3 2011 Remi Collet <Fedora@famillecollet.com> - 1.0.4-2
- rebuild for doc in /usr/share/doc/pear

* Wed Feb 16 2011 Remi Collet <Fedora@famillecollet.com> - 1.0.4-1
- Version 1.0.4 (stable) - API 1.0.3 (stable)
- LICENSE CHANGELOG now provided by upstream

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 02 2011 Remi Collet <Fedora@famillecollet.com> - 1.0.3-1
- Version 1.0.3 (stable) - API 1.0.3 (stable)

* Wed Nov 17 2010 Remi Collet <Fedora@famillecollet.com> - 1.0.2-1
- Version 1.0.2 (stable) - API 1.0.0 (stable)

* Thu Nov 04 2010 Remi Collet <Fedora@famillecollet.com> - 1.0.0-1.1
- lower PEAR dependency to allow f13 and el6 build
- fix URL

* Sun Sep 26 2010 Remi Collet <Fedora@famillecollet.com> - 1.0.0-1
- initial generated spec + clean

