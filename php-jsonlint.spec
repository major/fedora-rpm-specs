#
# Fedora spec file for php-jsonlint
#
# Copyright (c) 2013-2022 Shawn Iwinski <shawn.iwinski@gmail.com>
#                         Remi Collet <remi@fedoraproject.org>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner   Seldaek
%global github_name    jsonlint
%global github_version 1.9.0
%global github_commit  4211420d25eba80712bff236a98960ef68b866b7

# "php": "^5.3 || ^7.0 || ^8.0"
%global php_min_ver    5.3

# Build using "--without tests" to disable tests
%bcond_without tests

Name:          php-%{github_name}
Version:       %{github_version}
Release:       3%{?dist}
Summary:       JSON Lint for PHP

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
# git snapshot to retrieve upstream test suite
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

# Bin usage without Composer autoloader
Patch0:        %{name}-bin-without-composer-autoloader.patch

BuildArch:     noarch
%if %{with tests}
# For tests: composer.json
BuildRequires: php(language) >= %{php_min_ver}
%global phpunit %{_bindir}/phpunit8
BuildRequires: phpunit8 >= 8.5.13
# For tests: phpcompatinfo (computed from version 1.8.2)
BuildRequires: php-json
BuildRequires: php-pcre
# For autoloader
BuildRequires: php-fedora-autoloader-devel
%endif

Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 1.8.2)
Requires:      php-cli
Requires:      php-pcre
# For autoloader
Requires:      php-composer(fedora/autoloader)

Provides:      php-composer(seld/jsonlint) = %{version}


%description
%{summary}.

This library is a port of the JavaScript jsonlint
(https://github.com/zaach/jsonlint) library.

Bin: %{_bindir}/jsonlint-php [1]

Autoloader: %{_datadir}/php/Seld/JsonLint/autoload.php

[1] Package python2-demjson installs %{_bindir}/jsonlint so this package's bin
    script has been renamed to %{_bindir}/jsonlint-php


%prep
%setup -q -n %{github_name}-%{github_commit}

%patch0 -p1 -b .rpm


%build
: Generate autoloader
phpab \
  --template fedora \
  --output src/Seld/JsonLint/autoload.php \
  src/Seld/JsonLint


%install
# Lib
mkdir -p %{buildroot}%{_datadir}/php/Seld
cp -rp src/Seld/JsonLint %{buildroot}%{_datadir}/php/Seld/

# Bin
mkdir -p %{buildroot}%{_bindir}
install -pm 0755 bin/jsonlint %{buildroot}%{_bindir}/jsonlint-php


%check
%if %{with tests}

ret=0
for cmd in "php %{phpunit}" php74 php80 php81; do
  if which $cmd; then
    set $cmd
    $1 ${2:-%{_bindir}/phpunit8} \
      --bootstrap %{buildroot}%{_datadir}/php/Seld/JsonLint/autoload.php \
      --no-coverage \
      --verbose || ret=1
  fi
done
exit $ret
%else
: Tests skipped
%endif


%files
%license LICENSE
%doc *md
%doc composer.json
%dir %{_datadir}/php/Seld
     %{_datadir}/php/Seld/JsonLint
%{_bindir}/jsonlint-php


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Apr  4 2022 Remi Collet <remi@remirepo.net> - 1.9.0-1
- update to 1.9.0

* Thu Mar 31 2022 Remi Collet <remi@remirepo.net> - 1.8.9-1
- update to 1.8.9
- switch to phpunit8

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Mar 24 2021 Remi Collet <remi@remirepo.net> - 1.8.3-3
- switch to phpunit7

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 12 2020 Remi Collet <remi@remirepo.net> - 1.8.3-1
- update to 1.8.3
- sources from git snapshot

* Wed Aug 26 2020 Remi Collet <remi@remirepo.net> - 1.8.2-1
- update to 1.8.2
- switch to classmap autoloader

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 25 2019 Remi Collet <remi@remirepo.net> - 1.7.2-1
- update to 1.7.2

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Remi Collet <remi@remirepo.net> - 1.7.1-1
- Update to 1.7.1 (no change)

* Thu Jan  4 2018 Remi Collet <remi@remirepo.net> - 1.7.0-1
- Update to 1.7.0

* Wed Dec 20 2017 Remi Collet <remi@remirepo.net> - 1.6.2-1
- Update to 1.6.2 (no change)
- use phpunit6 on Fedora

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 19 2017 Remi Collet <remi@remirepo.net> - 1.6.1-1
- Update to 1.6.1

* Tue Mar  7 2017 Remi Collet <remi@remirepo.net> - 1.6.0-1
- Update to 1.6.0
- generate autoloader in spec

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 13 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.5.0-2
- Rename bin from %%{_bindir}/jsonlint to %%{_bindir}/jsonlint-php to avoid
  conflict with package python2-demjson (RHBZ #1409281)

* Tue Nov 15 2016 Remi Collet <remi@fedoraproject.org> - 1.5.0-1
- update to 1.5.0

* Mon Nov 14 2016 Remi Collet <remi@fedoraproject.org> - 1.4.1-3
- add patch for PHP 7.1
  open https://github.com/Seldaek/jsonlint/pull/37

* Fri Oct 21 2016 Remi Collet <remi@fedoraproject.org> - 1.4.1-2
- switch from symfony/class-loader to fedora/autoloader

* Thu Sep 15 2016 Remi Collet <remi@fedoraproject.org> - 1.4.1-1
- Updated to 1.4.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 26 2015 Remi Collet <remi@fedoraproject.org> - 1.4.0-1
- Updated to 1.4.0
- run test suite with both PHP 5 and 7 when available

* Wed Oct 14 2015 Remi Collet <remi@fedoraproject.org> - 1.3.1-3
- add autoloader

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan  5 2015 Remi Collet <remi@fedoraproject.org> - 1.3.1-1
- Updated to 1.3.1

* Thu Sep 11 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.3.0-1
- Updated to 1.3.0 (BZ #1138911)

* Sat Aug 23 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.0-2
- %%license usage

* Wed Aug 20 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.0-1
- Updated to 1.2.0 (BZ #1124228)
- Added option to build without tests ("--without tests")
- Added bin

* Mon Jun 09 2014 Remi Collet <remi@fedoraproject.org> - 1.1.2-2
- fix FTBFS, include path during test
- upstream patch for latest PHPUnit
- provides php-composer(seld/jsonlint)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Nov 15 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1.2-1
- Updated to upstream version 1.1.2 (BZ #1026717)
- php-common => php(language)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 12 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1.1-1
- Updated to upstream version 1.1.1 (BZ #910280)
- Updates per new Fedora packaging guidelines for Git repos

* Mon Jan 07 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1.0-1
- Initial package
