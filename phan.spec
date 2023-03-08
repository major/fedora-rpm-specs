# remirepo/fedora spec file for phan
#
# Copyright (c) 2016-2023 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

# For compatibility with SCL
%undefine __brp_mangle_shebangs

%global gh_commit    4f2870ed6fea320f62f3c3c63f3274d357a7980e
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     phan
#global gh_date      20150820
%global gh_project   phan
%global psr0         Phan
%bcond_without       tests
%global upstream_version 5.4.2
#global upstream_prever  a4

Name:           %{gh_project}
Version:        %{upstream_version}%{?upstream_prever:~%{upstream_prever}}
Release:        1%{?gh_date?%{gh_date}git%{gh_short}}%{?dist}
Summary:        A static analyzer for PHP

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{upstream_version}%{?upstream_prever}-%{?gh_short}.tgz
Source1:        makesrc.sh

# Use fedora autoloader
Patch0:         %{name}-autoload.patch

BuildArch:      noarch
%if %{with tests}
BuildRequires:  php(language) >= 7.2
BuildRequires:  php-ast >= 1.0.16
BuildRequires:  php-var_representation
BuildRequires:  (php-composer(composer/semver)                >= 1.4    with php-composer(composer/semver)                < 4)
BuildRequires:  (php-composer(composer/xdebug-handler)        >= 2.0    with php-composer(composer/xdebug-handler)        < 4)
BuildRequires:  (php-composer(felixfbecker/advanced-json-rpc) >= 3.0.4  with php-composer(felixfbecker/advanced-json-rpc) < 4)
BuildRequires:  (php-composer(microsoft/tolerant-php-parser)  >= 0.1.2  with php-composer(microsoft/tolerant-php-parser)  < 0.2)
BuildRequires:  (php-composer(netresearch/jsonmapper)         >= 1.6    with php-composer(netresearch/jsonmapper)         < 5)
BuildRequires:  (php-composer(sabre/event)                    >= 5.1.3  with php-composer(sabre/event)                    < 6)
BuildRequires:  (php-composer(symfony/console)                >= 4.0    with php-composer(symfony/console)                < 7)
BuildRequires:  (php-composer(symfony/polyfill-php80)         >= 1.19   with php-composer(symfony/polyfill-php80)         < 2)
BuildRequires:  php-reflection
BuildRequires:  php-ctype
BuildRequires:  php-dom
BuildRequires:  php-filter
BuildRequires:  php-json
BuildRequires:  php-mbstring
BuildRequires:  php-pcntl
BuildRequires:  php-pcre
BuildRequires:  php-posix
BuildRequires:  php-spl
BuildRequires:  php-sysvmsg
BuildRequires:  php-sysvsem
# For tests, from composer.json "require-dev": {
#        "phpunit/phpunit": "^8.5.0"
BuildRequires:  phpunit8 >= 8.5
BuildRequires:  php-date
BuildRequires:  php-intl
BuildRequires:  php-soap
%endif
# For autoloader
BuildRequires:  php-composer(fedora/autoloader)

# From composer.json, "require": {
#        "php": "^7.2.0|^8.0.0",
#        "ext-filter": "*",
#        "ext-json": "*",
#        "ext-tokenizer": "*",
#        "composer/semver": "^1.4|^2.0|^3.0",
#        "composer/xdebug-handler": "^2.0|^3.0",
#        "felixfbecker/advanced-json-rpc": "^3.0.4",
#        "microsoft/tolerant-php-parser": "^0.1.2",
#        "netresearch/jsonmapper": "^1.6.0|^2.0|^3.0|^4.0",
#        "sabre/event": "^5.1.3",
#        "symfony/console": "^3.2|^4.0|^5.0|^6.0",
#        "symfony/polyfill-mbstring": "^1.11.0",
#        "symfony/polyfill-php80": "^1.20.0",
# ignore and use the ext instead
#        "tysonandre/var_representation_polyfill": "^0.0.2|^0.1.0"
Requires:       php(language) >= 7.2
Requires:       php-filter
Requires:       php-tokenizer
Requires:       php-json
Requires:       php-var_representation
# From composer.json, "suggest": {
#        "ext-ast": "Needed for parsing ASTs (unless --use-fallback-parser is used). 1.0.1+ is needed, 1.0.16+ is recommended.",
#        "ext-iconv": "Either iconv or mbstring is needed to ensure issue messages are valid utf-8",
#        "ext-igbinary": "Improves performance of polyfill when ext-ast is unavailable",
#        "ext-mbstring": "Either iconv or mbstring is needed to ensure issue messages are valid utf-8",
#        "ext-tokenizer": "Needed for non-AST support and file/line-based suppressions."
Recommends:     php-ast >= 1.0.16
Suggests:       php-igbinary
Suggests:       php-iconv
Requires:       (php-composer(composer/semver)                >= 1.4    with php-composer(composer/semver)                < 4)
Requires:       (php-composer(composer/xdebug-handler)        >= 2.0    with php-composer(composer/xdebug-handler)        < 4)
Requires:       (php-composer(felixfbecker/advanced-json-rpc) >= 3.0.4  with php-composer(felixfbecker/advanced-json-rpc) < 4)
Requires:       (php-composer(nikic/php-parser)               >= 3.1.1  with php-composer(nikic/php-parser)               < 4)
Requires:       (php-composer(microsoft/tolerant-php-parser)  >= 0.1.2  with php-composer(microsoft/tolerant-php-parser)  < 0.2)
Requires:       (php-composer(netresearch/jsonmapper)         >= 1.6    with php-composer(netresearch/jsonmapper)         < 5)
Requires:       (php-composer(sabre/event)                    >= 5.1.3  with php-composer(sabre/event)                    < 6)
Requires:       (php-composer(symfony/console)                >= 4.0    with php-composer(symfony/console)                < 7)
Requires:       (php-composer(symfony/polyfill-php80)         >= 1.19   with php-composer(symfony/polyfill-php80)         < 2)
# From phpcompatinfo report for 2.3.0
Requires:       php-cli
Requires:       php-reflection
Requires:       php-ctype
Requires:       php-dom
Requires:       php-mbstring
Requires:       php-pcntl
Requires:       php-pcre
Requires:       php-posix
Requires:       php-readline
Requires:       php-spl
Requires:       php-sysvmsg
Requires:       php-sysvsem
# For autoloader
Requires:       php-composer(fedora/autoloader)

# Composer
Provides:       php-composer(%{gh_owner}/%{gh_project}) = %{version}


%description
Phan is a static analyzer that looks for common issues and will verify type
compatibility on various operations when type information is available or can
be deduced. Phan does not make any serious attempt to understand flow control
and narrow types based on conditionals.


%prep
%setup -q -n %{gh_project}-%{gh_commit}

%patch0 -p1 -b .rpm

cat << 'EOF' | tee src/autoload.php
<?php
/* Autoloader for etsy/phan and its dependencies */

require_once '%{_datadir}/php/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Phan\\', __DIR__ . '/Phan');
\Fedora\Autoloader\Dependencies::required([
    [
        '%{_datadir}/php/Composer/Semver3/autoload.php',
        '%{_datadir}/php/Composer/Semver2/autoload.php',
        '%{_datadir}/php/Composer/Semver/autoload.php',
    ], [
        '%{_datadir}/php/Composer/XdebugHandler3/autoload.php',
        '%{_datadir}/php/Composer/XdebugHandler2/autoload.php',
    ],
    '%{_datadir}/php/AdvancedJsonRpc3/autoload.php',
    '%{_datadir}/php/Microsoft/PhpParser/autoload.php',
    '%{_datadir}/php/netresearch/jsonmapper/autoload.php',
    '%{_datadir}/php/Sabre/Event5/autoload.php',
    [
        '%{_datadir}/php/Symfony6/Component/Console/autoload.php',
        '%{_datadir}/php/Symfony5/Component/Console/autoload.php',
        '%{_datadir}/php/Symfony4/Component/Console/autoload.php',
    ],
    '%{_datadir}/php/Symfony/Polyfill/autoload.php',
]);
EOF

find . -name \*.rpm -delete
chmod +x src/phan.php


%build
: Nothing to build


%install
: Library
mkdir -p   %{buildroot}%{_datadir}/php/
cp -pr src %{buildroot}%{_datadir}/php/%{psr0}

: Plugins
cp -pr .phan/plugins %{buildroot}%{_datadir}/php/%{psr0}/plugins

: Commands
mkdir -p %{buildroot}%{_bindir}
ln -s ../share/php/%{psr0}/phan.php %{buildroot}%{_bindir}/phan
install -Dpm 755 phan_client %{buildroot}%{_bindir}/phan-client


%check
%if %{with tests}
cat << 'EOF' | tee tests/autoload.php
<?php
require '%{buildroot}%{_datadir}/php/%{psr0}/Phan/Bootstrap.php';
\Fedora\Autoloader\Autoload::addPsr4('Phan\\Tests\\', __DIR__ . '/Phan');
EOF

# NOTICE mosquitto, request and grpc must be disabled
# testHash failing on bigendian
# testConstantsDocumented was written for php-ast 1.0.6 and php <=7.4
%{_bindir}/phpunit8 -d memory_limit=1G \
  --filter '^((?!(testGetProjectRelativePathForPath|testHash|testConstantsDocumented)).)*$' \
  --bootstrap tests/autoload.php --verbose


%else
: Test suite disabled
%endif


%files
%license LICENSE
%doc composer.json
%doc *.md
%{_datadir}/php/%{psr0}
%{_bindir}/phan*


%changelog
* Mon Mar  6 2023 Remi Collet <remi@remirepo.net> - 5.4.2-1
- update to 5.4.2
- raise dependency on microsoft/tolerant-php-parser 0.1.2

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep  8 2022 Remi Collet <remi@remirepo.net> - 5.4.1-1
- update to 5.4.1
- raise dependency on microsoft/tolerant-php-parser 0.1.1

* Tue Aug  9 2022 Remi Collet <remi@remirepo.net> - 5.4.0-1
- update to 5.4.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Feb  2 2022 Remi Collet <remi@remirepo.net> - 5.3.2-1
- update to 5.3.2
- drop support for Symfony 3

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 14 2021 Remi Collet <remi@remirepo.net> - 5.3.1-1
- update to 5.3.1
- raise dependency on ast 1.0.16
- raise dependency on sabre/event 5.1.3

* Mon Nov 15 2021 Remi Collet <remi@remirepo.net> - 5.3.0-1
- update to 5.3.0

* Mon Sep 20 2021 Remi Collet <remi@remirepo.net> - 5.2.1-1
- update to 5.2.1

* Thu Sep  2 2021 Remi Collet <remi@remirepo.net> - 5.2.0-1
- update to 5.2.0

* Mon Aug  9 2021 Remi Collet <remi@remirepo.net> - 5.1.0-1
- update to 5.1.0

* Mon Aug  2 2021 Remi Collet <remi@remirepo.net> - 5.0.0-1
- update to 5.0.0
- raise dependency on microsoft/tolerant-php-parser 0.1
- add dependency on var_representation extension

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 28 2021 Remi Collet <remi@remirepo.net> - 4.0.7-1
- update to 4.0.7
- allow netresearch/jsonmapper 4.0

* Thu May 20 2021 Remi Collet <remi@remirepo.net> - 4.0.6-1
- update to 4.0.6

* Mon May  3 2021 Remi Collet <remi@remirepo.net> - 4.0.5-1
- update to 4.0.5

* Thu Apr 15 2021 Remi Collet <remi@remirepo.net> - 4.0.4-1
- update to 4.0.4
- raise dependency on composer/xdebug-handler 2.0.0

* Wed Feb  3 2021 Remi Collet <remi@remirepo.net> - 4.0.3-1
- update to 4.0.3

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 11 2021 Remi Collet <remi@remirepo.net> - 4.0.2-1
- update to 4.0.2

* Tue Jan  5 2021 Remi Collet <remi@remirepo.net> - 4.0.1-1
- update to 4.0.1
- raise dependency on ast 1.0.10

* Mon Dec 14 2020 Remi Collet <remi@remirepo.net> - 3.2.7-1
- update to 3.2.7

* Mon Nov 30 2020 Remi Collet <remi@remirepo.net> - 3.2.6-1
- update to 3.2.6
- add dependency on symfony/polyfill-php80

* Fri Nov 13 2020 Remi Collet <remi@remirepo.net> - 3.2.4-1
- update to 3.2.4

* Tue Oct 13 2020 Remi Collet <remi@remirepo.net> - 3.2.3-1
- update to 3.2.3
- raise dependency on symfony/console 3.2

* Mon Sep 21 2020 Remi Collet <remi@remirepo.net> - 3.2.2-1
- update to 3.2.2

* Mon Sep 14 2020 Remi Collet <remi@remirepo.net> - 3.2.1-1
- update to 3.2.1
- raise dependency on microsoft/tolerant-php-parser 0.0.23

* Wed Aug 26 2020 Remi Collet <remi@remirepo.net> - 3.2.0-1
- update to 3.2.0
- raise dependency on microsoft/tolerant-php-parser 0.0.22

* Tue Aug 11 2020 Remi Collet <remi@remirepo.net> - 3.1.1-1
- update to 3.1.1
- allow netresearch/jsonmapper 3.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Remi Collet <remi@remirepo.net> - 3.1.0-1
- update to 3.1.0

* Mon Jul  6 2020 Remi Collet <remi@remirepo.net> - 3.0.5-1
- update to 3.0.5
- open https://github.com/phan/phan/issues/4004
  1 test failing on big endian

* Thu Jul  2 2020 Remi Collet <remi@remirepo.net> - 3.0.4-1
- update to 3.0.4

* Mon Jun 22 2020 Remi Collet <remi@remirepo.net> - 3.0.3-1
- update to 3.0.3

* Mon Jun  8 2020 Remi Collet <remi@remirepo.net> - 3.0.2-1
- update to 3.0.2

* Fri Jun  5 2020 Remi Collet <remi@remirepo.net> - 3.0.1-1
- update to 3.0.1
- allow composer/semver version 3

* Mon May 11 2020 Remi Collet <remi@remirepo.net> - 3.0.0-1
- update to 3.0.0
- raise dependency on PHP 7.2
- switch to phpunit8

* Mon May  4 2020 Remi Collet <remi@remirepo.net> - 2.7.2-1
- update to 2.7.2
- allow composer/semver version 2

* Mon Apr 13 2020 Remi Collet <remi@remirepo.net> - 2.7.1-1
- update to 2.7.1

* Thu Apr  2 2020 Remi Collet <remi@remirepo.net> - 2.7.0-1
- update to 2.7.0
- raise dependency on PHP 7.2

* Sat Mar 14 2020 Remi Collet <remi@remirepo.net> - 2.6.1-1
- update to 2.6.1
- allow netresearch/jsonmapper 2.0

* Mon Mar  9 2020 Remi Collet <remi@remirepo.net> - 2.6.0-1
- update to 2.6.0
- raise dependency on microsoft/tolerant-php-parser 0.0.20
- raise dependency on ast 1.0.6

* Thu Feb 20 2020 Remi Collet <remi@remirepo.net> - 2.5.0-1
- update to 2.5.0

* Fri Feb 14 2020 Remi Collet <remi@remirepo.net> - 2.4.9-1
- update to 2.4.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Remi Collet <remi@remirepo.net> - 2.4.8-1
- update to 2.4.8

* Thu Jan 23 2020 Remi Collet <remi@remirepo.net> - 2.4.7-1
- update to 2.4.7

* Thu Jan  2 2020 Remi Collet <remi@remirepo.net> - 2.4.6-1
- update to 2.4.6

* Wed Dec 11 2019 Remi Collet <remi@remirepo.net> - 2.4.5-1
- update to 2.4.5
- allow Symfony 5

* Mon Nov 25 2019 Remi Collet <remi@remirepo.net> - 2.4.4-1
- update to 2.4.4

* Thu Nov 21 2019 Remi Collet <remi@remirepo.net> - 2.4.3-1
- update to 2.4.3
- add explicit dependency on netresearch/jsonmapper

* Tue Nov 12 2019 Remi Collet <remi@remirepo.net> - 2.4.2-1
- update to 2.4.2

* Mon Nov  4 2019 Remi Collet <remi@remirepo.net> - 2.4.1-1
- update to 2.4.1

* Mon Oct 28 2019 Remi Collet <remi@remirepo.net> - 2.4.0-1
- update to 2.4.0

* Mon Oct 21 2019 Remi Collet <remi@remirepo.net> - 2.3.1-1
- update to 2.3.1

* Mon Oct 14 2019 Remi Collet <remi@remirepo.net> - 2.3.0-1
- update to 2.3.0

* Fri Oct  4 2019 Remi Collet <remi@remirepo.net> - 2.2.13-1
- update to 2.2.13
- raise dependency on felixfbecker/advanced-json-rpc 3.0.4

* Mon Sep  9 2019 Remi Collet <remi@remirepo.net> - 2.2.12-1
- update to 2.2.12

* Mon Aug 19 2019 Remi Collet <remi@remirepo.net> - 2.2.11-1
- update to 2.2.11

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 18 2019 Remi Collet <remi@remirepo.net> - 2.2.6-1
- update to 2.2.6

* Mon Jul 15 2019 Remi Collet <remi@remirepo.net> - 2.2.5-1
- update to 2.2.5

* Tue Jul  2 2019 Remi Collet <remi@remirepo.net> - 2.2.4-1
- update to 2.2.4
- raise dependency on microsoft/tolerant-php-parser 0.0.18

* Tue Jun 18 2019 Remi Collet <remi@remirepo.net> - 2.2.3-1
- update to 2.2.3

* Mon Jun 17 2019 Remi Collet <remi@remirepo.net> - 2.2.1-1
- update to 2.2.1

* Sun Jun  2 2019 Remi Collet <remi@remirepo.net> - 2.1.0-1
- update to 2.1.0

* Mon May 20 2019 Remi Collet <remi@remirepo.net> - 2.0.0-1
- update to 2.0.0
- raise dependency on PHP 7.1.0
- raise dependency on ast 1.0.1
- switch to phpunit7

* Fri May 10 2019 Remi Collet <remi@remirepo.net> - 1.3.4-1
- update to 1.3.4

* Mon Apr 29 2019 Remi Collet <remi@remirepo.net> - 1.3.2-1
- update to 1.3.2

* Tue Apr 23 2019 Remi Collet <remi@remirepo.net> - 1.3.1-1
- update to 1.3.1

* Mon Apr  8 2019 Remi Collet <remi@remirepo.net> - 1.2.8-1
- update to 1.2.8

* Sat Mar 23 2019 Remi Collet <remi@remirepo.net> - 1.2.7-1
- update to 1.2.7
- raise dependency on microsoft/tolerant-php-parser 0.0.17

* Sun Mar 10 2019 Remi Collet <remi@remirepo.net> - 1.2.6-1
- update to 1.2.6

* Wed Feb 27 2019 Remi Collet <remi@remirepo.net> - 1.2.5-1
- update to 1.2.5
- add dependecy on mbstring
- add weak dependecy on igbinary

* Tue Feb 19 2019 Remi Collet <remi@remirepo.net> - 1.2.4-1
- update to 1.2.4
- raise dependency on composer/xdebug-handler 1.3.2

* Mon Feb 11 2019 Remi Collet <remi@remirepo.net> - 1.2.3-1
- update to 1.2.3

* Mon Feb  4 2019 Remi Collet <remi@remirepo.net> - 1.2.2-1
- update to 1.2.2

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 19 2019 Remi Collet <remi@remirepo.net> - 1.2.1-1
- update to 1.2.1
- raise dependency on microsoft/tolerant-php-parser 0.0.16

* Sun Jan  6 2019 Remi Collet <remi@remirepo.net> - 1.2.0-1
- update to 1.2.0

* Mon Dec 31 2018 Remi Collet <remi@remirepo.net> - 1.1.10-1
- update to 1.1.10

* Sun Dec 16 2018 Remi Collet <remi@remirepo.net> - 1.1.8-1
- update to 1.1.8

* Sun Dec  9 2018 Remi Collet <remi@remirepo.net> - 1.1.7-1
- update to 1.1.7

* Fri Nov 30 2018 Remi Collet <remi@remirepo.net> - 1.1.5-1
- update to 1.1.5

* Wed Nov 28 2018 Remi Collet <remi@remirepo.net> - 1.1.4-1
- update to 1.1.4

* Wed Nov 21 2018 Remi Collet <remi@remirepo.net> - 1.1.3-1
- update to 1.1.3

* Tue Nov  6 2018 Remi Collet <remi@remirepo.net> - 1.1.2-1
- update to 1.1.2

* Tue Oct 23 2018 Remi Collet <remi@remirepo.net> - 1.1.1-1
- update to 1.1.1

* Tue Oct  9 2018 Remi Collet <remi@remirepo.net> - 1.1.0-1
- update to 1.1.0

* Wed Oct  3 2018 Remi Collet <remi@remirepo.net> - 1.0.7-1
- update to 1.0.7
- raise dependency on microsoft/tolerant-php-parser 0.0.13
- php-ast is optional

* Wed Sep 26 2018 Remi Collet <remi@remirepo.net> - 1.0.6-1
- update to 1.0.6
- sources from git snapshot

* Sat Sep 22 2018 Remi Collet <remi@remirepo.net> - 1.0.5-1
- update to 1.0.5
- open https://github.com/phan/phan/issues/1986 keep the tests
- keep ast mandatory despite it is now optional

* Mon Sep 10 2018 Remi Collet <remi@remirepo.net> - 1.0.4-1
- update to 1.0.4
- add the upstream plugins
- raise dependency on felixfbecker/advanced-json-rpc 3.0.3

* Sat Sep  8 2018 Remi Collet <remi@remirepo.net> - 1.0.3-1
- update to 1.0.3

* Fri Sep  7 2018 Remi Collet <remi@remirepo.net> - 1.0.2-1
- update to 1.0.2
- raise dependency on composer/xdebug-handler 1.3

* Mon Aug 27 2018 Remi Collet <remi@remirepo.net> - 1.0.1-1
- update to 1.0.1
- raise dependency on microsoft/tolerant-php-parser 0.0.13

* Tue Aug 14 2018 Remi Collet <remi@remirepo.net> - 1.0.0-1
- update to 1.0.0

* Mon Jul 23 2018 Remi Collet <remi@remirepo.net> - 0.12.15-1
- update to 0.12.15

* Mon Jul  9 2018 Remi Collet <remi@remirepo.net> - 0.12.14-1
- update to 0.12.14

* Tue Jun 19 2018 Remi Collet <remi@remirepo.net> - 0.12.13-1
- update to 0.12.13
- raise dependency on microsoft/tolerant-php-parser 0.0.11
- raise dependency on composer/xdebug-handler 1.1

* Mon Jun 11 2018 Remi Collet <remi@remirepo.net> - 0.12.12-1
- update to 0.12.12

* Thu May 31 2018 Remi Collet <remi@remirepo.net> - 0.12.11-1
- update to 0.12.11

* Mon May 28 2018 Remi Collet <remi@remirepo.net> - 0.12.10-1
- update to 0.12.10

* Wed May 23 2018 Remi Collet <remi@remirepo.net> - 0.12.9-1
- update to 0.12.9
- raise dependency on microsoft/tolerant-php-parser 0.0.11

* Sun May 13 2018 Remi Collet <remi@remirepo.net> - 0.12.8-1
- update to 0.12.8

* Tue Apr  3 2018 Remi Collet <remi@remirepo.net> - 0.12.5-1
- update to 0.12.5

* Mon Apr  2 2018 Remi Collet <remi@remirepo.net> - 0.12.4-1
- update to 0.12.4

* Mon Mar 26 2018 Remi Collet <remi@remirepo.net> - 0.12.3-1
- update to 0.12.3
- add dependency on composer/xdebug-handler
- raise dependency on microsoft/tolerant-php-parser 0.0.10

* Sat Mar  3 2018 Remi Collet <remi@remirepo.net> - 0.12.2-1
- Update to 0.12.2

* Thu Mar  1 2018 Remi Collet <remi@remirepo.net> - 0.12.1-1
- Update to 0.12.1

* Mon Feb 26 2018 Remi Collet <remi@remirepo.net> - 0.12.0-1
- Update to 0.12.0
- drop dependency on nikic/PHP-Parser
- add dependency on composer/semver
- same version for PHP 7.0, 7.1 and 7.2

* Thu Feb 15 2018 Remi Collet <remi@remirepo.net> - 0.11.3-1
- Update to 0.11.3
- raise dependency on microsoft/tolerant-php-parser 0.0.9

* Mon Feb 12 2018 Remi Collet <remi@remirepo.net> - 0.11.2-1
- Update to 0.11.2

* Mon Jan 22 2018 Remi Collet <remi@remirepo.net> - 0.11.1-1
- Update to 0.11.1
- raise dependency on felixfbecker/advanced-json-rpc 3.0
- add dependency on microsoft/tolerant-php-parser
- allow Symfony 4

* Sat Nov 18 2017 Remi Collet <remi@remirepo.net> - 0.11.0-1
- Update to 0.11.0
- raise dependency on PHP 7.2

* Sat Nov 18 2017 Remi Collet <remi@remirepo.net> - 0.10.2-1
- Update to 0.10.2

* Sat Oct 21 2017 Remi Collet <remi@remirepo.net> - 0.10.1-1
- Update to 0.10.1
- add dependency on felixfbecker/advanced-json-rpc 2.0
- add dependency on sabre/event 5.0

* Mon Sep 25 2017 Remi Collet <remi@remirepo.net> - 0.10.0-1
- Update to 0.10.0
- raise dependency on ast 0.1.5
- add dependency on nikic/php-parser 3.1.1
- move from etsy/phan to phan/phan

* Wed Aug 16 2017 Remi Collet <remi@remirepo.net> - 0.9.4-1
- Update to 0.9.4

* Wed Jul 12 2017 Remi Collet <remi@remirepo.net> - 0.9.3-1
- Update to 0.9.3
- installation layout match upstream tree
- remove phan-prep command (only an example)
- add phan-client command

* Wed Jun 14 2017 Remi Collet <remi@remirepo.net> - 0.9.2-1
- Update to 0.9.2
- allow Symfony 3
- use phpunit 6

* Thu Mar 16 2017 Remi Collet <remi@remirepo.net> - 0.9.1-1
- Update to 0.9.1
- raise dependency on PHP 7.1
- raise dependency on ast 0.1.4

* Fri Jan 27 2017 Remi Collet <remi@remirepo.net> - 0.8.3-1
- update to 0.8.3

* Thu Jan 26 2017 Remi Collet <remi@remirepo.net> - 0.8.2-1
- update to 0.8.2

* Wed Jan 25 2017 Remi Collet <remi@fedoraproject.org> - 0.8.0-1
- update to 0.8.0

* Fri Dec  9 2016 Remi Collet <remi@fedoraproject.org> - 0.7-1
- update to 0.7

* Thu Nov 24 2016 Remi Collet <remi@fedoraproject.org> - 0.6-1
- initial package

