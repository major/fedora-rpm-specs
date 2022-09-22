#
# Fedora spec file for php-JsonSchema
#
# Copyright (c) 2012-2021 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner   justinrainbow
%global github_name    json-schema
%global github_version 1.6.1
%global github_commit  cc84765fb7317f6b07bd8ac78364747f95b86341
%global github_short   %(c=%{github_commit}; echo ${c:0:7})

%if 0%{?fedora} < 24 && 0%{?rhel} < 8
%global with_script  1
%else
%global with_script  0
%endif

# Upstream recommends 5.3.29, ignored as test suite pass with 5.3.3 in RHEL-6
%global php_min_ver    5.3.2

%global lib_name       JsonSchema
%global phpdir         %{_datadir}/php

# Build using "--without tests" to disable tests
%global with_tests     0%{!?_without_tests:1}

Name:          php-%{lib_name}
Version:       %{github_version}
Release:       19%{?dist}
Summary:       PHP implementation of JSON schema

License:       BSD
URL:           https://github.com/%{github_owner}/%{github_name}
# Use a git snapshot as upstream remove tests from distribution
Source0:       %{name}-%{github_version}-%{github_short}.tgz
# Script to pull the git snapshot
Source2:       %{name}-makesrc.sh

# https://github.com/justinrainbow/json-schema/pull/292
Patch0:        %{name}-pr292.patch
# Minimal patch for PHP 8
Patch1:        %{name}-php8.patch


BuildArch: noarch
%if %{with_tests}
# For tests
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(phpunit/phpunit) >= 3.7
# For tests: phpcompatinfo (computed from v1.6.0)
BuildRequires: php-curl
BuildRequires: php-date
BuildRequires: php-filter
BuildRequires: php-json
BuildRequires: php-mbstring
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-spl
# Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from v1.6.0)
%if %{with_script}
Requires:      php-cli
%endif
Requires:      php-curl
Requires:      php-date
Requires:      php-filter
Requires:      php-json
Requires:      php-mbstring
Requires:      php-pcre
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(justinrainbow/json-schema) = %{version}


%description
A PHP implementation for validating JSON structures against a given schema.
%if %{with_script}
This package provides the library version 1 and the validate-json command.
The php-justinrainbow-json-schema package provides the library version 2.
%else
This package provides the library version 1.
The php-justinrainbow-json-schema package provides the library version 2
and the validate-json command.
%endif
See http://json-schema.org for more details.


%prep
%setup -qn %{github_name}-%{github_commit}
%patch0 -p1
%patch1 -p1

: Create autoloader
cat <<'AUTOLOAD' | tee src/%{lib_name}/autoload.php
<?php
/* Autoloader for %{name} and its' dependencies */

require_once '%{phpdir}/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('JsonSchema\\', __DIR__);
AUTOLOAD


%build
# Empty build section, nothing to build


%install
# Install lib
mkdir -p %{buildroot}%{phpdir}
cp -rp src/* %{buildroot}%{phpdir}/

%if %{with_script}
# Install bin
install -Dpm 0755 bin/validate-json %{buildroot}%{_bindir}/validate-json
%endif


%check
%if %{with_tests}
# Remove empty tests
rm -rf tests/%{lib_name}/Tests/Drafts

mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require '%{buildroot}%{phpdir}/%{lib_name}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('JsonSchema\\Tests\\', __DIR__.'/../tests/JsonSchema/Tests');
EOF

ret=0
for cmd in php php73 php74 php80; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit --verbose || ret=1
  fi
done
exit $ret
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc README.md composer.json
%{phpdir}/%{lib_name}
%if %{with_script}
%{_bindir}/validate-json
%endif


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Mar 31 2021 Remi Collet <remi@remirepo.net> - 1.6.1-16
- add minimal patch for PHP 8

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec  9 2018 Remi Collet <remi@remirepo.net> - 1.6.1-10
- cleanup for EL-8

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 10 2017 Remi Collet <remi@remirepo.net> - 1.6.1-6
- switch to fedora/autoloader
- run test suite against PHP SCLs when available

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Remi Collet <remi@fedoraproject.org> - 1.6.1-4
- fix failed test, FTBFS detected by Koschei
  open https://github.com/justinrainbow/json-schema/pull/292

* Wed Jun  1 2016 Remi Collet <remi@fedoraproject.org> - 1.6.1-3
- drop the validate-json command, moved in php-justinrainbow-json-schema

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Remi Collet <remi@fedoraproject.org> - 1.6.1-1
- update to 1.6.1

* Thu Jan  7 2016 Remi Collet <remi@fedoraproject.org> - 1.6.0-1
- update to 1.6.0
- use a git snapshot as upstream drop tests from distribution

* Tue Sep 22 2015 Remi Collet <remi@fedoraproject.org> - 1.5.0-1
- update to 1.5.0

* Tue Jul 14 2015 Remi Collet <remi@fedoraproject.org> - 1.4.4-1
- update to 1.4.4

* Tue Jul 14 2015 Remi Collet <remi@fedoraproject.org> - 1.4.3-1
- update to 1.4.3
- add autoloader

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 15 2015 Remi Collet <remi@fedoraproject.org> - 1.4.2-1
- update to 1.4.2

* Mon Apr 13 2015 Remi Collet <remi@fedoraproject.org> - 1.4.1-2
- fix tests autoloader (FTBFS detected by Koschei)

* Fri Mar 27 2015 Remi Collet <remi@fedoraproject.org> - 1.4.1-1
- Update to 1.4.1

* Tue Mar 24 2015 Remi Collet <remi@fedoraproject.org> - 1.4.0-1
- Update to 1.4.0

* Sat Aug 30 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.3.7-2
- PHP < 5.4.0 compatibility patch instead of in-spec logic

* Fri Aug 29 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.3.7-1
- Updated to 1.3.7 (BZ #1133519)
- Added option to build without tests ("--without tests")
- Added "php-composer(justinrainbow/json-schema)" virtual provide
- Added PHP < 5.4.0 compatibility for "--dump-schema"
- %%check tweaks
- Added %%license usage

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 07 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.3.6-1
- Updated to 1.3.6 (BZ #1073969)

* Sun Dec 29 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.3.5-1
- Updated to 1.3.5 (BZ #039502)

* Mon Dec 09 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.3.4-1
- Updated to 1.3.4
- php-common => php(language)
- Removed the following build requires:
  -- php-pear(pear.phpunit.de/DbUnit),
  -- php-pear(pear.phpunit.de/PHPUnit_Selenium)
  -- php-pear(pear.phpunit.de/PHPUnit_Story)
- Added bin
- Updated %%check to use PHPUnit's "--include-path" option

* Sun Aug 11 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.3.3-1
- Updated to 1.3.3 (BZ #987401)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 05 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.3.2-1
- Updated to 1.3.2 (BZ #973066)
- Added php-pear(pear.phpunit.de/DbUnit), php-pear(pear.phpunit.de/PHPUnit_Selenium),
  and php-pear(pear.phpunit.de/PHPUnit_Story) build requires
- Removed php-ctype require
- Added php-mbstring require

* Thu Mar 21 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.3.1-1
- Updated to upstream version 1.3.1 (BZ #923726)

* Sun Feb 24 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.3.0-1
- Updated to upstream version 1.3.0 (BZ #912273)

* Mon Feb 04 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.4-1
- Updated to upstream version 1.2.4 (BZ #907127)
- Updates per new Fedora packaging guidelines for Git repos

* Sun Dec 09 2012 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.2-2
- Fixed failing Mock/Koji builds
- Removed "docs" directory from %%doc

* Sat Dec 08 2012 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.2-1
- Updated to upstream version 1.2.2
- Added php-ctype require
- Added PSR-0 autoloader for tests
- Added %%check

* Tue Nov 27 2012 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.1-1
- Initial package
