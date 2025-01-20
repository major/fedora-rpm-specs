# spec file for php-mikey179-vfsstream
#
# Copyright (c) 2014-2024 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    fe695ec993e0a55c3abdda10a9364eb31c6f1bf0
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     bovigo
%global gh_project   vfsStream
%global pk_owner     mikey179
%global pk_project   vfsstream
%global with_tests   %{?_without_tests:0}%{!?_without_tests:1}

Name:           php-%{pk_owner}-%{pk_project}
Version:        1.6.12
Release:        3%{?dist}
Summary:        PHP stream wrapper for a virtual file system

# Automatically converted from old format: BSD-3-Clause - review is highly recommended.
License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch
BuildRequires:  php(language) >= 7.1
BuildRequires:  %{_bindir}/phpab
%if %{with_tests}
# From composer.json, "require-dev": {
#        "phpunit/phpunit": "^7.5||^8.5||^9.6",
#        "yoast/phpunit-polyfills": "^2.0"
BuildRequires:  phpunit9 >= 9.6
BuildRequires: (php-composer(yoast/phpunit-polyfills) >= 2.0 with php-composer(yoast/phpunit-polyfills) < 3)
%endif

# From composer.json, "require": {
#        "php": ">=7.1.0"
Requires:       php(language) >= 7.1
# From phpcompatifo report for 1.6.0
Requires:       php-date
Requires:       php-dom
Requires:       php-pcre
Requires:       php-posix
Requires:       php-spl
Requires:       php-xml
Requires:       php-zip

# provides both cases for compatibility
Provides:       php-composer(%{pk_owner}/%{pk_project}) = %{version}
Provides:       php-composer(%{pk_owner}/%{gh_project}) = %{version}


%description
vfsStream is a PHP stream wrapper for a virtual file system that may be
helpful in unit tests to mock the real file system.

It can be used with any unit test framework, like PHPUnit or SimpleTest.

To use this library, you just have to add, in your project:
  require_once '%{_datadir}/php/org/bovigo/vfs/autoload.php';


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
: Generate autoloader
%{_bindir}/phpab \
    --output src/main/php/org/bovigo/vfs/autoload.php \
             src/main/php/org/bovigo/vfs


%install
mkdir -p                %{buildroot}%{_datadir}/php
cp -pr src/main/php/org %{buildroot}%{_datadir}/php/org


%if %{with_tests}
%check
# erratic result in mock
rm src/test/php/org/bovigo/vfs/vfsStreamWrapperLargeFileTestCase.php

: Use installed tree and autoloader
mkdir vendor
cat << 'EOF' | tee -a vendor/autoload.php
<?php
require_once '%{buildroot}%{_datadir}/php/org/bovigo/vfs/autoload.php';
require_once '%{_datadir}/php/Yoast/PHPUnitPolyfills2/autoload.php';
EOF

ret=0
for cmd in php php81 php82 php83 php84; do
  if which $cmd; then
    VER=$($cmd -r 'echo PHP_VERSION_ID;')
    $cmd %{_bindir}/phpunit9 \
      --filter '^((?!(unregisterThirdPartyVfsScheme|unregisterWhenNotInRegisteredState)).)*$' \
      --verbose --no-coverage || ret=1
  fi
done
exit $ret
%endif


%files
%license LICENSE
%doc *.md
%doc composer.json

%dir %{_datadir}/php/org
%dir %{_datadir}/php/org/bovigo
     %{_datadir}/php/org/bovigo/vfs


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep  4 2024 Miroslav Suchý <msuchy@redhat.com> - 1.6.12-2
- convert license to SPDX

* Fri Aug 30 2024 Remi Collet <remi@remirepo.net> - 1.6.12-1
- update to 1.6.12
- raise dependency on PHP 7.1
- add build dependency on yoast/phpunit-polyfills 2.0

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 11 2022 Remi Collet <remi@remirepo.net> - 1.6.11-1
- update to 1.6.11

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 30 2022 Remi Collet <remi@remirepo.net> - 1.6.10-2
- add upstream patch for 8.2
- skip test suite with PHP >= 8.1

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Sep 27 2021 Remi Collet <remi@remirepo.net> - 1.6.10-1
- update to 1.6.10

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 19 2021 Remi Collet <remi@remirepo.net> - 1.6.9-1
- update to 1.6.9

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 31 2019 Remi Collet <remi@remirepo.net> - 1.6.8-1
- update to 1.6.8

* Fri Aug  2 2019 Remi Collet <remi@remirepo.net> - 1.6.7-1
- update to 1.6.7

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr  9 2019 Remi Collet <remi@remirepo.net> - 1.6.6-2
- fix vendor

* Tue Apr  9 2019 Remi Collet <remi@remirepo.net> - 1.6.6-1
- update to 1.6.6 (no change)
- project ownership have moved to bovigo

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 16 2018 Remi Collet <remi@remirepo.net> - 1.6.5-5
- ignore 1 failed test related to behavior change in 7.3
  open https://github.com/mikey179/vfsStream/pull/172

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar  5 2018 Remi Collet <remi@remirepo.net> - 1.6.5-3
- provides both mikey179/vfsstream and mikey179/vfsStream

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Aug  4 2017 Remi Collet <remi@remirepo.net> - 1.6.5-1
- Update to 1.6.5

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jul 18 2016 Remi Collet <remi@fedoraproject.org> - 1.6.4-1
- update to 1.6.4

* Wed Apr 13 2016 Remi Collet <remi@fedoraproject.org> - 1.6.3-1
- update to 1.6.3

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 13 2016 Remi Collet <remi@fedoraproject.org> - 1.6.2-1
- update to 1.6.2

* Fri Dec  4 2015 Remi Collet <remi@fedoraproject.org> - 1.6.1-1
- update to 1.6.1

* Wed Oct  7 2015 Remi Collet <remi@fedoraproject.org> - 1.6.0-1
- update to 1.6.0
- add generated autoloader

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar 29 2015 Remi Collet <remi@fedoraproject.org> - 1.5.0-1
- update to 1.5.0
- create source from git snapshot for test suite
  see https://github.com/mikey179/vfsStream/issues/108

* Sun Sep 14 2014 Remi Collet <remi@fedoraproject.org> - 1.4.0-1
- update to 1.4.0

* Tue Jul 22 2014 Remi Collet <remi@fedoraproject.org> - 1.3.0-1
- update to 1.3.0
- fix license handling

* Fri Jun  6 2014 Remi Collet <remi@fedoraproject.org> - 1.2.0-2
- provides php-composer(mikey179/vfsstream)

* Tue May 13 2014 Remi Collet <remi@fedoraproject.org> - 1.2.0-1
- initial package
