#
# Fedora spec file for php-twig
#
# Copyright (c) 2014-2022 Shawn Iwinski <shawn.iwinski@gmail.com>
#                         Remi Collet <remi@fedoraproject.org>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

# Build using "--without tests" to disable tests
%bcond_without   tests

%global github_owner     twigphp
%global github_name      Twig
%global github_version   1.44.7
%global github_commit    0887422319889e442458e48e2f3d9add1a172ad5
%global github_short     %(c=%{github_commit}; echo ${c:0:7})

# Lib
%global composer_vendor  twig
%global composer_project twig

# "php": ">=7.2.5"
%global php_min_ver 7.2.5

%{!?phpdir:      %global phpdir      %{_datadir}/php}
%{!?php_inidir:  %global php_inidir  %{_sysconfdir}/php.d}

Name:          php-%{composer_project}
Version:       %{github_version}
Release:       8%{?dist}
Summary:       The flexible, fast, and secure template engine for PHP

# Automatically converted from old format: BSD - review is highly recommended.
License:       LicenseRef-Callaway-BSD
URL:           http://twig.sensiolabs.org
Source0:       %{name}-%{github_version}-%{github_short}.tgz
Source1:       makesrc.sh

BuildArch: noarch
# as we use phpunit9 (for assertFileDoesNotExist)
BuildRequires: php-devel >= 7.3
# Tests
%if %{with tests}
BuildRequires: (php-composer(symfony/debug) >= 3.4    with php-composer(symfony/debug) < 4)
BuildRequires: (php-composer(psr/container) >= 1.0    with php-composer(psr/container) < 2)
%global phpunit %{_bindir}/phpunit9
BuildRequires: %{phpunit}
## phpcompatinfo (computed from version 1.42.2)
BuildRequires: php-ctype
BuildRequires: php-date
BuildRequires: php-dom
BuildRequires: php-hash
BuildRequires: php-iconv
BuildRequires: php-json
BuildRequires: php-mbstring
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-simplexml
BuildRequires: php-spl
%endif
# Autoloader
BuildRequires: php-fedora-autoloader-devel

# Lib
## composer.json
Requires:      php(language) >= %{php_min_ver}
## phpcompatinfo (computed from version 1.42.2)
Requires:      php-ctype
Requires:      php-date
Requires:      php-dom
Requires:      php-hash
Requires:      php-iconv
Requires:      php-json
Requires:      php-mbstring
Requires:      php-pcre
Requires:      php-reflection
Requires:      php-simplexml
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Lib
## Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}
## Rename
Obsoletes:     php-twig-Twig < %{version}-%{release}
Provides:      php-twig-Twig = %{version}-%{release}
## PEAR
Provides:      php-pear(pear.twig-project.org/Twig) = %{version}

# This pkg was the only one in this channel so the channel is no longer needed
Obsoletes:     php-channel-twig < 1.4


%description
%{summary}.

* Fast: Twig compiles templates down to plain optimized PHP code. The
  overhead compared to regular PHP code was reduced to the very minimum.

* Secure: Twig has a sandbox mode to evaluate untrusted template code. This
  allows Twig to be used as a template language for applications where users
  may modify the template design.

* Flexible: Twig is powered by a flexible lexer and parser. This allows the
  developer to define its own custom tags and filters, and create its own
  DSL.

Autoloader: %{phpdir}/Twig/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}

: Move the PSR-4 compat library
mv src lib/Twig/psr4

: Create lib autoloader
phpab --template fedora --output lib/Twig/autoload.php lib


%build
: nothing


%install
: PSR-0 and PSR-4 Libraries
mkdir -p %{buildroot}%{phpdir}
cp -rp lib/* %{buildroot}%{phpdir}/


%check
: Library version check
%{_bindir}/php -r 'require_once "%{buildroot}%{phpdir}/Twig/autoload.php";
    exit(version_compare("%{version}", Twig_Environment::VERSION, "=") ? 0 : 1);'

%{_bindir}/php -r 'require_once "%{buildroot}%{phpdir}/Twig/autoload.php";
    exit(version_compare("%{version}", Twig\Environment::VERSION, "=") ? 0 : 1);'

%if %{with tests}
: Generate autoloader
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{phpdir}/Twig/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Twig\\Tests\\', dirname(__DIR__) . '/tests');
\Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}/Symfony3/Component/Debug/autoload.php',
    '%{phpdir}/Psr/Container/autoload.php',
));
EOF

: Disable listener from symfony/phpunit-bridge # ^4.4.9|^5.0.9
sed -e '/listener/d' phpunit.xml.dist > phpunit.xml

: Test suite without extension
ret=0
for SCL in "php %{phpunit}" php74 php80 php81 php82; do
    if which $SCL; then
        set $SCL
        $1 ${2:-%{_bindir}/phpunit9} $SKIP \
          --verbose || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif


%files
%license LICENSE
%doc CHANGELOG README.rst composer.json
# Lib
%{phpdir}/Twig


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.44.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep  4 2024 Miroslav Suchý <msuchy@redhat.com> - 1.44.7-7
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.44.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.44.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.44.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.44.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.44.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep 29 2022 Remi Collet <remi@remirepo.net> - 1.44.7-1
- update to 1.44.7

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.44.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.44.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Nov 25 2021 Remi Collet <remi@remirepo.net> - 1.44.6-1
- update to 1.44.6 (no change)
- drop patch merged upstream

* Wed Sep 22 2021 Remi Collet <remi@remirepo.net> - 1.44.5-1
- update to 1.44.5
- add patch for test suite from https://github.com/twigphp/Twig/pull/3563

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.44.4-2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 17 2021 Remi Collet <remi@remirepo.net> - 1.44.4-1
- update to 1.44.4

* Wed May 12 2021 Remi Collet <remi@remirepo.net> - 1.44.3-1
- update to 1.44.3

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.44.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan  6 2021 Remi Collet <remi@remirepo.net> - 1.44.2-1
- update to 1.44.2

* Wed Oct 28 2020 Remi Collet <remi@remirepo.net> - 1.44.1-1
- update to 1.44.1

* Wed Oct 21 2020 Remi Collet <remi@remirepo.net> - 1.44.0-1
- update to 1.44.0
- raise dependency on PHP 7.2.5

* Tue Aug 11 2020 Remi Collet <remi@remirepo.net> - 1.43.1-1
- update to 1.43.1
- switch to phpunit9
- skip 1 more test with PHP 8.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.43.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul  6 2020 Remi Collet <remi@remirepo.net> - 1.43.0-1
- update to 1.43.0
- raise dependency on PHP 7.1.3
- switch to phpunit8

* Wed Feb 12 2020 Remi Collet <remi@remirepo.net> - 1.42.5-1
- update to 1.42.5

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.42.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 12 2019 Remi Collet <remi@remirepo.net> - 1.42.4-1
- update to 1.42.4
- sources from git snapshot

* Tue Aug 27 2019 Remi Collet <remi@remirepo.net> - 1.42.3-1
- update to 1.42.3
- use symfony/debug v3
- use phpunit v7
- raise dependency on PHP 5.5
- drop support of the C extension

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.42.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Shawn Iwinski <shawn@iwin.ski> - 1.42.2-1
- Update to 1.42.2

* Tue Jun  4 2019 Remi Collet <remi@remirepo.net> - 1.42.1-1
- update to 1.42.1

* Mon Jun  3 2019 Remi Collet <remi@remirepo.net> - 1.42.0-1
- update to 1.42.0

* Wed May 15 2019 Remi Collet <remi@remirepo.net> - 1.41.0-1
- update to 1.41.0

* Tue Apr 30 2019 Remi Collet <remi@remirepo.net> - 1.40.1-1
- update to 1.40.1

* Mon Apr 29 2019 Remi Collet <remi@remirepo.net> - 1.40.0-1
- update to 1.40.0

* Wed Apr 17 2019 Remi Collet <remi@remirepo.net> - 1.39.1-1
- update to 1.39.1

* Mon Mar 25 2019 Remi Collet <remi@remirepo.net> - 1.38.4-1
- update to 1.38.4

* Fri Mar 22 2019 Remi Collet <remi@remirepo.net> - 1.38.3-1
- update to 1.38.3

* Wed Mar 13 2019 Remi Collet <remi@remirepo.net> - 1.38.2-1
- update to 1.38.2

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.37.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Remi Collet <remi@remirepo.net> - 1.37.1-1
- update to 1.37.1
- bump dependency on PHP 5.4

* Tue Dec 18 2018 Remi Collet <remi@remirepo.net> - 1.36.0-1
- update to 1.36.0

* Fri Jul 13 2018 Remi Collet <remi@remirepo.net> - 1.35.4-1
- update to 1.35.4

* Tue Mar 20 2018 Remi Collet <remi@remirepo.net> - 1.35.3-1
- update to 1.35.3

* Sun Mar  4 2018 Remi Collet <remi@remirepo.net> - 1.35.2-1
- Update to 1.35.2

* Sat Mar  3 2018 Remi Collet <remi@remirepo.net> - 1.35.1-1
- Update to 1.35.1
- use range dependencies on F27+

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.35.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 28 2017 Remi Collet <remi@remirepo.net> - 1.35.0-1
- Update to 1.35.0

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.34.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.34.4-2
- Rebuild due to bug in RPM (RHBZ #1468476)

* Wed Jul  5 2017 Remi Collet <remi@remirepo.net> - 1.34.4-1
- Update to 1.34.4

* Thu Jun  8 2017 Remi Collet <remi@remirepo.net> - 1.34.3-1
- Update to 1.34.3

* Tue Jun  6 2017 Remi Collet <remi@remirepo.net> - 1.34.2-1
- Update to 1.34.2
- raise dependency on PHP 5.3.3
- add namespaced compat library
- switch to fedora/autoloader
- drop build dependency on symfony/phpunit-bridge

* Mon Apr 24 2017 Remi Collet <remi@remirepo.net> - 1.33.2-1
- Update to 1.33.2

* Thu Mar 23 2017 Remi Collet <remi@remirepo.net> - 1.33.0-1
- Update to 1.33.0

* Mon Feb 27 2017 Remi Collet <remi@fedoraproject.org> - 1.32.0-1
- Update to 1.32.0
- add build dependency on symfony/phpunit-bridge, symfony/debug
  and psr/container

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.31.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Remi Collet <remi@fedoraproject.org> - 1.31.0-1
- Update to 1.31.0

* Thu Dec 29 2016 Remi Collet <remi@fedoraproject.org> - 1.30.0-1
- Update to 1.30.0

* Thu Nov 24 2016 Remi Collet <remi@fedoraproject.org> - 1.28.2-1
- Update to 1.28.2

* Tue Nov 22 2016 Remi Collet <remi@fedoraproject.org> - 1.28.1-1
- Update to 1.28.1

* Fri Nov 18 2016 Remi Collet <remi@fedoraproject.org> - 1.28.0-1
- Update to 1.28.0

* Wed Oct 26 2016 Remi Collet <remi@fedoraproject.org> - 1.27.0-1
- Update to 1.27.0

* Thu Oct  6 2016 Remi Collet <remi@fedoraproject.org> - 1.26.1-1
- Update to 1.26.1

* Tue Oct  4 2016 Remi Collet <remi@fedoraproject.org> - 1.26.0-1
- Update to 1.26.0

* Sun Sep 11 2016 Shawn Iwinski <shawn@iwin.ski> - 1.24.2-1
- Updated to 1.24.2 (RHBZ #1372507)

* Mon Jun 27 2016 Remi Collet <remi@fedoraproject.org> - 1.24.1-2
- rebuild for https://fedoraproject.org/wiki/Changes/php70

* Mon May 30 2016 Remi Collet <remi@fedoraproject.org> - 1.24.1-1
- Update to 1.24.1
- disable deprecation warning in autoloader
- disable extension build with PHP 7

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Remi Collet <remi@fedoraproject.org> - 1.24.0-1
- Update to 1.24.0

* Mon Jan 11 2016 Remi Collet <remi@fedoraproject.org> - 1.23.3-1
- Update to 1.23.3

* Thu Nov 05 2015 Remi Collet <remi@fedoraproject.org> - 1.23.1-1
- Update to 1.23.0
- drop patch merged upstream

* Mon Nov  2 2015 Remi Collet <remi@fedoraproject.org> - 1.23.0-2
- fix BC break in NodeTestCase, add upstream patch from
  https://github.com/twigphp/Twig/pull/1905

* Fri Oct 30 2015 Remi Collet <remi@fedoraproject.org> - 1.23.0-1
- Update to 1.23.0

* Sun Oct 11 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.22.2-1
- Updated to 1.22.2 (RHBZ #1262655)
- Added lib and ext version checks

* Sat Sep 12 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.21.2-1
- Updated to 1.21.2 (BZ #1256767)

* Wed Aug 12 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.20.0-1
- Updated to 1.20.0 (BZ #1249259)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.18.2-1
- Updated to 1.18.2 (BZ #1183601)
- Added autoloader

* Sun Jan 04 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.16.3-1
- Updated to 1.16.3 (BZ #1178412)

* Sat Nov 01 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.16.2-1
- Updated to 1.16.2 (BZ #1159523)
- GitHub owner changed from "fabpot" to "twigphp"
- Single license for lib and ext

* Mon Aug 25 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.16.0-2
- Removed obsolete and provide of php-twig-CTwig (never imported into Fedora/EPEL)
- Obsolete php-channel-twig
- Removed comment about optional Xdebug in description (does not provide any new feature)
- Always run extension minimal load test

* Tue Jul 29 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.16.0-1
- Initial package
