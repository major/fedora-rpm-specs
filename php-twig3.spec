# fedora/remirepo spec file for php-twig3, from
#
# Fedora spec file for php-twig3
#
# Copyright (c) 2014-2023 Shawn Iwinski <shawn.iwinski@gmail.com>
#                         Remi Collet <remi@fedoraproject.org>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#
%bcond_without tests

%global github_owner     twigphp
%global github_name      Twig
%global github_commit    3ffcf4b7d890770466da3b2666f82ac054e7ec72
%global github_short     %(c=%{github_commit}; echo ${c:0:7})

%global composer_vendor  twig
%global composer_project twig

%global major            3

# "php": ">=7.2.5"
%global php_min_ver 7.2.5
%global phpdir      %{_datadir}/php

Name:          php-%{composer_project}%{major}
Version:       3.5.0
Release:       1%{?dist}
Summary:       The flexible, fast, and secure template engine for PHP

License:       BSD-3-Clause
URL:           https://twig.symfony.com
Source0:       %{name}-%{version}-%{github_short}.tgz
Source1:       makesrc.sh

BUildArch:     noarch
## Autoloader
BuildRequires: php-fedora-autoloader-devel
%if %{with tests}
# For tests
# as we use phpunit9 (for assertFileDoesNotExist)
BuildRequires: php(language) >= 7.3
BuildRequires: (php-composer(psr/container) >= 1.0    with php-composer(psr/container) < 2)
%global phpunit %{_bindir}/phpunit9
BuildRequires: %{phpunit}
## phpcompatinfo (computed from version 3.0.0)
BuildRequires: php-ctype
BuildRequires: php-date
BuildRequires: php-filter
BuildRequires: php-hash
BuildRequires: php-iconv
BuildRequires: php-json
BuildRequires: php-mbstring
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-spl
BuildRequires: php-simplexml
%endif

## composer.json
Requires:      php(language) >= %{php_min_ver}
## phpcompatinfo (computed from version 3.0.0)
Requires:      php-ctype
Requires:      php-date
Requires:      php-filter
Requires:      php-hash
Requires:      php-iconv
Requires:      php-json
Requires:      php-mbstring
Requires:      php-pcre
Requires:      php-reflection
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

## Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}


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

Autoloader: %{phpdir}/Twig%{major}/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create classmap autoloader
phpab --template fedora --output src/autoload.php src


%install
mkdir -p %{buildroot}%{phpdir}
cp -rp src %{buildroot}%{phpdir}/Twig%{major}


%check
: Check library version
%{_bindir}/php -r 'require_once "%{buildroot}%{phpdir}/Twig%{major}/autoload.php";
    exit(version_compare("%{version}", Twig\Environment::VERSION, "=") ? 0 : 1);'

%if %{with tests}
mkdir vendor
phpab --output vendor/autoload.php tests


cat << 'EOF' | tee -a vendor/autoload.php
// This library
require_once '%{buildroot}%{phpdir}/Twig%{major}/autoload.php';
// Dependencies (require-dev)
\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/Psr/Container/autoload.php',
]);
EOF

: Disable listener from symfony/phpunit-bridge 4.4
sed -e '/listener/d' phpunit.xml.dist > phpunit.xml

RETURN_CODE=0
: Upstream tests with SCLs if available
for SCL in "php %{phpunit}" php80 php81 php82; do
    if which $SCL; then
        set $SCL
        $1 ${2:-%{_bindir}/phpunit9} \
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
%{phpdir}/Twig%{major}


%changelog
* Tue Jan  3 2023 Remi Collet <remi@remirepo.net> - 3.5.0-1
- update to 3.5.0

* Thu Sep 29 2022 Remi Collet <remi@remirepo.net> - 3.4.3-1
- update to 3.4.3

* Tue Aug 16 2022 Remi Collet <remi@remirepo.net> - 3.4.2-1
- update to 3.4.2

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 17 2022 Remi Collet <remi@remirepo.net> - 3.4.1-1
- update to 3.4.1

* Mon May 16 2022 Remi Collet <remi@remirepo.net> - 3.4.0-1
- update to 3.4.0

* Wed Apr  6 2022 Remi Collet <remi@remirepo.net> - 3.3.10-1
- update to 3.3.10

* Mon Mar 28 2022 Remi Collet <remi@remirepo.net> - 3.3.9-1
- update to 3.3.9

* Fri Feb  4 2022 Remi Collet <remi@remirepo.net> - 3.3.8-1
- update to 3.3.8

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan  4 2022 Remi Collet <remi@remirepo.net> - 3.3.7-1
- update to 3.3.7

* Mon Jan  3 2022 Remi Collet <remi@remirepo.net> - 3.3.6-1
- update to 3.3.6

* Mon Jan  3 2022 Remi Collet <remi@remirepo.net> - 3.3.5-1
- update to 3.3.5

* Thu Nov 25 2021 Remi Collet <remi@remirepo.net> - 3.3.4-1
- update to 3.3.4 (no change)

* Wed Sep 22 2021 Remi Collet <remi@remirepo.net> - 3.3.3-1
- update to 3.3.3

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 17 2021 Remi Collet <remi@remirepo.net> - 3.3.2-1
- update to 3.3.2

* Wed May 12 2021 Remi Collet <remi@remirepo.net> - 3.3.1-1
- update to 3.3.1

* Mon Feb  8 2021 Remi Collet <remi@remirepo.net> - 3.3.0-1
- update to 3.3.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan  6 2021 Remi Collet <remi@remirepo.net> - 3.2.1-1
- update to 3.2.1

* Wed Oct 28 2020 Remi Collet <remi@remirepo.net> - 3.1.1-1
- update to 3.1.1

* Wed Oct 21 2020 Remi Collet <remi@remirepo.net> - 3.1.0-1
- update to 3.1.0

* Tue Aug 11 2020 Remi Collet <remi@remirepo.net> - 3.0.5-1
- update to 3.0.5
- switch to phpunit9

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul  6 2020 Remi Collet <remi@remirepo.net> - 3.0.4-1
- update to 3.0.4

* Wed Feb 12 2020 Remi Collet <remi@remirepo.net> - 3.0.3-1
- update to 3.0.3

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan  3 2020 Remi Collet <remi@remirepo.net> - 3.0.1-1
- update to 3.0.1

* Thu Nov 21 2019 Remi Collet <remi@remirepo.net> - 3.0.0-2
- fix typo in package description

* Thu Nov 21 2019 Remi Collet <remi@remirepo.net> - 3.0.0-1
- update to 3.0.0
- move to /usr/share/php/Twig3
- raise dependency on PHP 7.2.9
- drop dependency on symfony/polyfill-mbstring

* Tue Nov 12 2019 Remi Collet <remi@remirepo.net> - 2.12.2-1
- update to 2.12.2

* Thu Oct 17 2019 Remi Collet <remi@remirepo.net> - 2.12.1-1
- update to 2.12.1 (no change)
- sources from git snapshot

* Mon Oct  7 2019 Remi Collet <remi@remirepo.net> - 2.12.0-1
- update to 2.12.0
- use phpunit7 and Symfony 4 for test suite

* Tue Jun 18 2019 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.11.3-1
- Update to 2.11.3

* Wed Jun  5 2019 Remi Collet <remi@remirepo.net> - 2.11.2-1
- update to 2.11.2

* Tue Jun  4 2019 Remi Collet <remi@remirepo.net> - 2.11.1-1
- update to 2.11.1

* Mon Jun  3 2019 Remi Collet <remi@remirepo.net> - 2.11.0-1
- update to 2.11.0

* Wed May 15 2019 Remi Collet <remi@remirepo.net> - 2.10.0-1
- update to 2.10.0

* Mon Apr 29 2019 Remi Collet <remi@remirepo.net> - 2.9.0-1
- update to 2.9.0

* Wed Apr 17 2019 Remi Collet <remi@remirepo.net> - 2.8.1-1
- update to 2.8.1

* Mon Mar 25 2019 Remi Collet <remi@remirepo.net> - 2.7.4-1
- update to 2.7.4

* Fri Mar 22 2019 Remi Collet <remi@remirepo.net> - 2.7.3-1
- update to 2.7.3

* Wed Mar 13 2019 Remi Collet <remi@remirepo.net> - 2.7.2-1
- update to 2.7.2

* Tue Mar 12 2019 Remi Collet <remi@remirepo.net> - 2.7.0-1
- update to 2.7.0

* Mon Jan 14 2019 Remi Collet <remi@remirepo.net> - 2.6.2-1
- update to 2.6.2

* Tue Dec 18 2018 Remi Collet <remi@remirepo.net> - 2.6.0-1
- update to 2.6.0
- add dependency on symfony/polyfill-mbstring 1.3

* Fri Jul 13 2018 Remi Collet <remi@remirepo.net> - 2.5.0-1
- update to 2.5.0
- use phpunit6 for test suite

* Tue Apr  3 2018 Remi Collet <remi@remirepo.net> - 2.4.8-1
- update to 2.4.8

* Tue Mar 20 2018 Remi Collet <remi@remirepo.net> - 2.4.7-1
- update to 2.4.7

* Sun Mar  4 2018 Remi Collet <remi@remirepo.net> - 2.4.6-1
- Update to 2.4.6

* Sat Mar  3 2018 Remi Collet <remi@remirepo.net> - 2.4.5-1
- Update to 2.4.5
- use range dependencies on F27+

* Thu Sep 28 2017 Remi Collet <remi@remirepo.net> - 2.4.4-1
- Update to 2.4.4

* Thu Jun  8 2017 Remi Collet <remi@remirepo.net> - 2.4.3-1
- Update to 2.4.3

* Tue Jun  6 2017 Remi Collet <remi@remirepo.net> - 2.4.2-1
- Update to 2.4.2
- add namespaced compat library

* Fri Apr 21 2017 Remi Collet <remi@remirepo.net> - 2.3.2-1
- Update to 2.3.2

* Thu Mar 23 2017 Remi Collet <remi@remirepo.net> - 2.3.0-1
- Update to 2.3.0

* Mon Feb 27 2017 Remi Collet <remi@fedoraproject.org> - 2.2.0-1
- update to 2.2.0
- add dependency on psr/container

* Wed Jan 11 2017 Remi Collet <remi@fedoraproject.org> - 2.1.0-1
- update to 2.1.0

* Fri Jan  6 2017 Remi Collet <remi@fedoraproject.org> - 2.0.0-1
- update to 2.0.0
- rename to php-twig2
- cleanup spec file, no more C extension
- use fedora/autoloader
- raise dependency on PHP version 7

* Fri Dec 23 2016 Remi Collet <remi@fedoraproject.org> - 1.30.0-1
- Update to 1.30.0

* Wed Dec 14 2016 Remi Collet <remi@fedoraproject.org> - 1.29.0-1
- Update to 1.29.0

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

* Mon Oct  3 2016 Remi Collet <remi@fedoraproject.org> - 1.26.0-1
- Update to 1.26.0

* Thu Sep 22 2016 Remi Collet <remi@fedoraproject.org> - 1.25.0-1
- Update to 1.25.0

* Fri Sep  2 2016 Remi Collet <remi@fedoraproject.org> - 1.24.2-1
- Update to 1.24.2

* Mon Jun 27 2016 Remi Collet <remi@fedoraproject.org> - 1.24.1-2
- fix dependency with PHP-7

* Mon May 30 2016 Remi Collet <remi@fedoraproject.org> - 1.24.1-1
- Update to 1.24.1
- disable deprecation warning
- disable extension build with PHP 7

* Tue Jan 26 2016 Remi Collet <remi@fedoraproject.org> - 1.24.0-1
- Update to 1.24.0

* Mon Jan 11 2016 Remi Collet <remi@fedoraproject.org> - 1.23.3-1
- Update to 1.23.3
- run test suite with both PHP 5 and 7 when available

* Thu Nov 05 2015 Remi Collet <remi@fedoraproject.org> - 1.23.1-1
- Update to 1.23.1

* Fri Oct 30 2015 Remi Collet <remi@fedoraproject.org> - 1.23.0-1
- Update to 1.23.0

* Tue Oct 13 2015 Remi Collet <remi@fedoraproject.org> - 1.22.3-1
- Update to 1.22.3

* Sun Oct 11 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.22.2-1
- Updated to 1.22.2 (RHBZ #1262655)
- Added lib and ext version checks

* Wed Sep 23 2015 Remi Collet <remi@fedoraproject.org> - 1.22.2-1
- Update to 1.22.2

* Tue Sep 15 2015 Remi Collet <remi@fedoraproject.org> - 1.22.1-1
- Update to 1.22.1

* Sun Sep 13 2015 Remi Collet <remi@fedoraproject.org> - 1.22.0-1
- Update to 1.22.0

* Sat Sep 12 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.21.2-1
- Updated to 1.21.2 (BZ #1256767)

* Wed Sep  9 2015 Remi Collet <remi@fedoraproject.org> - 1.21.2-1
- Update to 1.21.2

* Wed Aug 26 2015 Remi Collet <remi@fedoraproject.org> - 1.21.1-1
- Update to 1.21.1

* Tue Aug 25 2015 Remi Collet <remi@fedoraproject.org> - 1.21.0-1
- Update to 1.21.0

* Wed Aug 12 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.20.0-1
- Updated to 1.20.0 (BZ #1249259)

* Wed Aug 12 2015 Remi Collet <remi@fedoraproject.org> - 1.20.0-1
- Update to 1.20.0

* Fri Jul 31 2015 Remi Collet <remi@fedoraproject.org> - 1.19.0-1
- Update to 1.19.0

* Mon Jun 22 2015 Remi Collet <rcollet@redhat.com> - 1.18.2-4
- add virtual "rh-php56" provides

* Fri Jun 19 2015 Remi Collet <remi@fedoraproject.org> - 1.18.2-3
- allow build against rh-php56 (as more-php56)

* Mon Jun 15 2015 Remi Collet <remi@fedoraproject.org> - 1.18.2-2
- rebuild for remirepo with rawhide changes (autoloader)

* Thu Jun 11 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.18.2-1
- Updated to 1.18.2 (BZ #1183601)
- Added autoloader

* Sun Jun  7 2015 Remi Collet <remi@fedoraproject.org> - 1.18.2-1
- Update to 1.18.2

* Sun Apr 19 2015 Remi Collet <remi@fedoraproject.org> - 1.18.1-1
- Update to 1.18.1

* Mon Jan 26 2015 Remi Collet <remi@fedoraproject.org> - 1.18.0-1
- Update to 1.18.0

* Wed Jan 14 2015 Remi Collet <remi@fedoraproject.org> - 1.17.0-1
- Update to 1.17.0

* Fri Dec 26 2014 Remi Collet <remi@fedoraproject.org> - 1.16.3-1
- Update to 1.16.3

* Wed Dec 24 2014 Remi Collet <remi@fedoraproject.org> - 1.16.2-1.1
- Fedora 21 SCL mass rebuild

* Fri Oct 17 2014 Remi Collet <remi@fedoraproject.org> - 1.16.2-1
- Update to 1.16.2

* Sat Oct 11 2014 Remi Collet <remi@fedoraproject.org> - 1.16.1-1
- Update to 1.16.1

* Thu Aug 28 2014 Remi Collet <remi@fedoraproject.org> - 1.16.0-2
- allow SCL build
- add backport stuff for EL-5

* Mon Aug 25 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.16.0-2
- Removed obsolete and provide of php-twig-CTwig (never imported into Fedora/EPEL)
- Obsolete php-channel-twig
- Removed comment about optional Xdebug in description (does not provide any new feature)
- Always run extension minimal load test

* Tue Jul 29 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.16.0-1
- Initial package
