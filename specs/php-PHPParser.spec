#
# RPM spec file for php-PHPParser
#
# Copyright (c) 2012-2021 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

# Outdated, see php-nikic-php-parser4
%bcond_with tests

%global github_owner    nikic
%global github_name     PHP-Parser
%global github_version  1.4.1
%global github_commit   f78af2c9c86107aa1a34cd1dbb5bbe9eeb0d9f51
%global github_short    %(c=%{github_commit}; echo ${c:0:7})

%global lib_name        PhpParser
%global lib_name_old    PHPParser

%global php_min_ver     5.3

Name:          php-%{lib_name_old}
Version:       %{github_version}
Release:       24%{?dist}
Summary:       A PHP parser written in PHP - version 1

# Automatically converted from old format: BSD - review is highly recommended.
License:       LicenseRef-Callaway-BSD
URL:           https://github.com/%{github_owner}/%{github_name}
# Upstream tarball don't provide test suite
# Use mksrc.sh to generate a git snapshot tarball
Source0:       %{name}-%{github_version}-%{github_short}.tgz
Source1:       makesrc.sh

# Patch for distribution
Patch0:        %{name}-command.patch

BuildArch:     noarch
# For tests
BuildRequires: php(language) >= %{php_min_ver}
%if %{with tests}
BuildRequires: %{_bindir}/phpunit
%endif
# For tests: phpcompatinfo (computed from version 1.4.1)
BuildRequires: php-ctype
BuildRequires: php-filter
BuildRequires: php-pcre
BuildRequires: php-spl
BuildRequires: php-tokenizer
BuildRequires: php-xmlreader
BuildRequires: php-xmlwriter

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      php-tokenizer
# phpcompatinfo (computed from version 1.4.1)
Requires:      php-filter
Requires:      php-pcre
Requires:      php-spl
Requires:      php-xmlreader
Requires:      php-xmlwriter

Provides:      php-composer(nikic/php-parser) = %{version}


%description
A PHP parser written in PHP to simplify static analysis and code manipulation.

This package provides the library version 1.
The php-nikic-php-parser3 package provides the library version 3.
The php-nikic-php-parser4 package provides the library version 4.

Autoloader: '%{_datadir}/php/%{lib_name}/autoload.php';


%prep
%setup -q -n %{github_name}-%{github_short}

%patch -P0 -p0 -b .rpm
rm lib/%{lib_name}/*rpm


%build
# Empty build section, nothing to build


%install
mkdir -p -m 755 %{buildroot}%{_datadir}/php
cp -rp lib/%{lib_name} %{buildroot}%{_datadir}/php/%{lib_name}

# Compat with old version (< 1.0.0)
mkdir -p -m 755 %{buildroot}%{_datadir}/php/%{lib_name_old}
ln -s ../%{lib_name}/Autoloader.php \
    %{buildroot}%{_datadir}/php/%{lib_name_old}/Autoloader.php


%check
%if %{with tests}
%{_bindir}/phpunit \
    --bootstrap %{buildroot}%{_datadir}/php/%{lib_name}/autoload.php \
    --filter '^((?!(testResolveLocations)).)*$' \
    --verbose
%else
: Test suite disabled
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md doc grammar composer.json
%{_datadir}/php/%{lib_name_old}
%{_datadir}/php/%{lib_name}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep  4 2024 Miroslav Suchý <msuchy@redhat.com> - 1.4.1-23
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 30 2021 Remi Collet <remi@fedoraproject.org> - 1.4.1-14
- outdated package, disable test suite

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb  4 2020 Remi Collet <remi@fedoraproject.org> - 1.4.1-11
- skip 1 failed test with 7.4

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri May 20 2016 Remi Collet <remi@fedoraproject.org> - 1.4.1-4
- drop the php-parse command, provided by php-nikic-php-parser

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Sep 20 2015 Remi Collet <remi@fedoraproject.org> - 1.4.1-1
- update to 1.4.1

* Sun Aug  9 2015 Remi Collet <remi@fedoraproject.org> - 1.4.0-1
- update to 1.4.0
- add a simple autoload.php

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 20 2015 Remi Collet <remi@fedoraproject.org> - 1.3.0-1
- update to 1.3.0

* Wed Feb 25 2015 Remi Collet <remi@fedoraproject.org> - 1.1.0-1
- update to 1.1.0
- use git snapshot as upstream tarball don't provide the test suite
- provide the php-parse command

* Wed Nov  5 2014 Remi Collet <remi@fedoraproject.org> 1.0.2-1
- Update to 1.0.2

* Thu Oct 16 2014 Remi Collet <remi@fedoraproject.org> 1.0.1-1
- Update to 1.0.1

* Fri Sep 12 2014 Remi Collet <remi@fedoraproject.org> 1.0.0-1
- Update to 1.0.0

* Wed Jul 23 2014 Remi Collet <remi@fedoraproject.org> 1.0.0-0.3.beta1
- provide php-composer(nikic/php-parser)
- fix license handling

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.2.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 16 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.0-0.1.beta1
- Updated to 1.0.0-beta1 (BZ #1096697)

* Fri Nov 15 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.9.4-1
- Updated to 0.9.4 (BZ #1001126)
- Spec cleanup

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 31 2012 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.9.3-2
- Added php_min_ver
- Fixed requires for php_min_ver and non-Fedora

* Thu Dec 20 2012 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.9.3-1
- Initial package
