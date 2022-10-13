# remirepo/Fedora spec file for php-laminas-diactoros2
#
# Copyright (c) 2015-2022 Shawn Iwinski, Remi Collet
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global gh_owner     laminas
%global gh_project   laminas-diactoros
%global gh_commit    b3c7e9262b4fbec801d8df2370cdebb4f5d3a0ae
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Diactoros
%global major        2

# https://github.com/php-http/psr7-integration-tests/tags
%global gh_psr7_owner     php-http
%global gh_psr7_name      psr7-integration-tests
%global gh_psr7_version   1.1.1
%global gh_psr7_commit    dbc81e59655c3d927ba62b2cd38be9af334590fc
%global gh_psr7_short     %(c=%{gh_psr7_commit}; echo ${c:0:7})

# https://github.com/http-interop/http-factory-tests/tags
%global gh_factory_owner   http-interop
%global gh_factory_name    http-factory-tests
%global gh_factory_version 0.9.0
%global gh_factory_commit  642056c5360e8a74779cbf133afbc8aa2c174e15
%global gh_factory_short   %(c=%{gh_factory_commit}; echo ${c:0:7})

# Build using "--without tests" to disable tests
%bcond_without tests

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{gh_project}%{major}
Version:       2.19.0
Release:       1%{?gh_release}%{?dist}
Summary:       PSR HTTP Message implementations v%{major}

License:       BSD
URL:           https://github.com/%{gh_owner}/%{gh_project}

# GitHub export does not include tests.
# Run makesrc.sh to create full source.
Source0:       %{name}-%{version}-%{gh_short}.tgz
Source1:       makesrc.sh
# Temporarily bundled, only used for tests
Source2:       %{gh_psr7_owner}-%{gh_psr7_name}-%{gh_psr7_version}-%{gh_psr7_short}.tgz
Source3:       %{gh_psr7_owner}-%{gh_psr7_name}-get-source.sh
# Temporarily bundled, only used for tests
Source4:       php-%{gh_factory_owner}-%{gh_factory_name}-%{gh_factory_version}-%{gh_factory_short}.tgz
Source5:       php-%{gh_factory_owner}-%{gh_factory_name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with tests}
## composer.json
BuildRequires: php(language) >= 8.0
BuildRequires: (php-composer(psr/http-message)                           >= 1.0 with php-composer(psr/http-message)                           < 2)
BuildRequires: (php-composer(psr/http-factory)                           >= 1.0 with php-composer(psr/http-factory)                           < 2)
#    "require-dev": {
#        "ext-curl": "*",
#        "ext-dom": "*",
#        "ext-gd": "*",
#        "ext-libxml": "*",
#        "http-interop/http-factory-tests": "^0.9.0",
#        "laminas/laminas-coding-standard": "~2.4.0",
#        "php-http/psr7-integration-tests": "^1.1.1",
#        "phpunit/phpunit": "^9.5.25"
#        "psalm/plugin-phpunit": "^0.17.0",
#        "vimeo/psalm": "^4.28"
#    },
%global phpunit %{_bindir}/phpunit9
BuildRequires:  phpunit9 >= 9.5.25
BuildRequires:  php-curl
BuildRequires:  php-dom
BuildRequires:  php-gd
BuildRequires:  php-libxml
## phpcompatinfo (computed from version 2.4.0)
BuildRequires:  php-date
BuildRequires:  php-gmp
BuildRequires:  php-json
BuildRequires:  php-pcre
BuildRequires:  php-reflection
BuildRequires:  php-shmop
BuildRequires:  php-spl
%endif
## Autoloader
BuildRequires:  php-fedora-autoloader-devel

# composer.json
#    "require": {
#        "php": "~8.0.0 || ~8.1.0 || ~8.2.0",
#        "psr/http-factory": "^1.0",
#        "psr/http-message": "^1.0"
Requires:       php(language) >= 8.0
Requires:      (php-composer(psr/http-message)                           >= 1.0 with php-composer(psr/http-message)                           < 2)
Requires:      (php-composer(psr/http-factory)                           >= 1.0 with php-composer(psr/http-factory)                           < 2)
# phpcompatinfo (computed from version 2.4.0)
Requires:       php-json
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}

Provides:       php-composer(psr/http-factory-implementation) = 1.0
Provides:       php-composer(psr/http-message-implementation) = 1.0


%description
A PHP package containing implementations of the accepted PSR-7 HTTP message
interfaces [1], as well as a "server" implementation similar to node's
http.Server [2].

Documentation: https://docs.laminas.dev/%{gh_project}/

Autoloader: %{phpdir}/%{namespace}/%{library}%{major}/autoload.php

[1] http://www.php-fig.org/psr/psr-7/
[2] http://nodejs.org/api/http.html


%prep
%setup -qn %{gh_project}-%{gh_commit} -a2 -a4

mv %{gh_psr7_name}-%{gh_psr7_commit} psr7
mv %{gh_factory_name}-%{gh_factory_commit} factory
mv LICENSE.md LICENSE


%build
: Create autoloader
phpab --template fedora --output src/autoload.php src
cat <<'AUTOLOAD' | tee -a src/autoload.php
if (!function_exists('Laminas\\Diactoros\\createUploadedFile')) {
  \Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}/Psr/Http/Message/autoload.php',
    '%{phpdir}/Psr/Http/Message/http-factory-autoload.php',
    __DIR__.'/functions/create_uploaded_file.php',
    __DIR__.'/functions/marshal_headers_from_sapi.php',
    __DIR__.'/functions/marshal_method_from_sapi.php',
    __DIR__.'/functions/marshal_protocol_version_from_sapi.php',
    __DIR__.'/functions/marshal_uri_from_sapi.php',
    __DIR__.'/functions/normalize_server.php',
    __DIR__.'/functions/normalize_uploaded_files.php',
    __DIR__.'/functions/parse_cookie_header.php',
  ));
}
AUTOLOAD


%install
: Laminas library
mkdir -p   %{buildroot}%{php_home}/%{namespace}/
cp -pr src %{buildroot}%{php_home}/%{namespace}/%{library}%{major}


%check
%if %{with tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php

require_once '%{buildroot}%{phpdir}/%{namespace}/%{library}%{major}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{namespace}Test\\%{library}\\', __DIR__.'/test');
\Fedora\Autoloader\Autoload::addPsr4('Http\\Psr7Test\\', __DIR__.'/psr7/src');
\Fedora\Autoloader\Autoload::addPsr4('Interop\\Http\\Factory\\', __DIR__.'/factory/test');
BOOTSTRAP

sed -e 's:vendor/http-interop/http-factory-tests:factory:' \
    phpunit.xml.dist >phpunit.xml

: Upstream tests
# Skip tests requiring network access
RETURN_CODE=0
for CMDARG in "php %{phpunit}" php80 php81 php82; do
    if which $CMDARG; then
        set $CMDARG
        $1 ${2:-%{_bindir}/phpunit9} \
           --bootstrap bootstrap.php \
           --filter '^((?!(testReasonPhraseDefaultsAgainstIana|testIsNotSeekable|testIsNotWritable|testIsNotReadable|testRewindNotSeekable)).)*$' \
           --verbose || RETURN_CODE=1
    fi
done

exit $RETURN_CODE
%else
: Tests skipped
%endif


%files
%license LICENSE COPYRIGHT.md
%doc README.md
%doc composer.json
%{php_home}/%{namespace}/%{library}%{major}


%changelog
* Tue Oct 11 2022 Remi Collet <remi@remirepo.net> - 2.19.0-1
- update to 2.19.0
- raise dependency on PHP 8.0

* Tue Sep 20 2022 Remi Collet <remi@remirepo.net> - 2.17.0-1
- update to 2.17.0
- raise dependency on PHP 7.4

* Mon Aug  1 2022 Remi Collet <remi@remirepo.net> - 2.14.0-1
- update to 2.14.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul  7 2022 Remi Collet <remi@remirepo.net> - 2.13.0-1
- update to 2.13.0

* Wed Jul  6 2022 Remi Collet <remi@remirepo.net> - 2.12.0-1
- update to 2.12.0

* Thu Jun 30 2022 Remi Collet <remi@remirepo.net> - 2.11.2-1
- update to 2.11.2

* Wed Jun 29 2022 Remi Collet <remi@remirepo.net> - 2.11.1-1
- update to 2.11.1

* Tue May 17 2022 Remi Collet <remi@remirepo.net> - 2.11.0-1
- update to 2.11.0

* Thu May  5 2022 Remi Collet <remi@remirepo.net> - 2.10.0-1
- update to 2.10.0

* Thu Apr  7 2022 Remi Collet <remi@remirepo.net> - 2.9.2-1
- update to 2.9.2

* Wed Mar 30 2022 Remi Collet <remi@remirepo.net> - 2.9.0-1
- update to 2.9.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Sep 24 2021 Remi Collet <remi@remirepo.net> - 2.8.0-1
- update to 2.8.0
- drop dependency on laminas-zendframework-bridge

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed May 19 2021 Remi Collet <remi@remirepo.net> - 2.6.0-1
- update to 2.6.0

* Wed Apr 14 2021 Remi Collet <remi@remirepo.net> - 2.5.1-1
- update to 2.5.1 (no change)
- drop ZF compatibility

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 21 2021 Remi Collet <remi@remirepo.net> - 2.5.0-2
- fix test suite path, from review #1900513

* Thu Nov 19 2020 Remi Collet <remi@remirepo.net> - 2.5.0-1
- update to 2.5.0
- raise dependency on PHP 7.3
- switch to phpunit9

* Fri Sep  4 2020 Remi Collet <remi@remirepo.net> - 2.4.1-1
- update to 2.4.1 (no change)

* Thu Sep  3 2020 Remi Collet <remi@remirepo.net> - 2.4.0-1
- update to 2.4.0

* Wed Jul  8 2020 Remi Collet <remi@remirepo.net> - 2.3.1-1
- update to 2.3.1

* Tue Apr 28 2020 Remi Collet <remi@remirepo.net> - 2.3.0-1
- update to 2.3.0

* Mon Mar 30 2020 Remi Collet <remi@remirepo.net> - 2.2.3-1
- update to 2.2.3 (no change)

* Thu Jan 23 2020 Remi Collet <remi@remirepo.net> - 2.2.2-2
- fix autoloader, ensure functions are not defined twice

* Wed Jan 22 2020 Remi Collet <remi@remirepo.net> - 2.2.2-1
- update to 2.2.2
- rename to php-laminas-diactoros2
- install to /usr/share/php/Laminas/Diactoros2
- raise dependency on PHP 7.1
- add dependency on psr/http-factory
- switch to phpunit7

* Fri Jan 17 2020 Remi Collet <remi@remirepo.net> - 1.8.7p1-2
- cleanup

* Wed Jan  8 2020 Remi Collet <remi@remirepo.net> - 1.8.7p1-1
- switch to Laminas
- update to 1.8.7p1

* Fri Aug 30 2019 Remi Collet <remi@remirepo.net> - 1.8.7-1
- update to 1.8.7

* Thu Sep  6 2018 Remi Collet <remi@remirepo.net> - 1.8.6-1
- update to 1.8.6
- bundle php-http/psr7-integration-tests only used for tests

* Mon Aug 20 2018 Remi Collet <remi@remirepo.net> - 1.8.5-1
- update to 1.8.5

* Thu Aug 02 2018 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.8.4-1
- Update to 1.8.4 (RHBZ #1504401 / ZF2018-01 / CVE-2018-14773 / CVE-2018-14774)

* Wed May 30 2018 Remi Collet <remi@remirepo.net> - 1.7.2-1
- update to 1.7.2

* Fri Mar 30 2018 Remi Collet <remi@remirepo.net> - 1.7.1-1
- update to 1.7.1
- use range dependencies on F27+

* Fri Jan  5 2018 Remi Collet <remi@remirepo.net> - 1.7.0-1
- Update to 1.7.0

* Tue Dec  5 2017 Remi Collet <remi@remirepo.net> - 1.6.1-2
- switch to classmap autoloader for consistency
- provide php-autoloader(zendframework/zend-diactoros)

* Thu Nov  2 2017 Remi Collet <remi@remirepo.net> - 1.6.1-1
- Update to 1.6.1
- use phpunit6 on F26+

* Sun Oct 08 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.6.0-1
- Updated to 1.6.0 (RHBZ #1491486)

* Sun Sep 10 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.4.1-1
- Updated to 1.4.1 (RHBZ #1482723)

* Sat Apr 08 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.4.0-1
- Updated to 1.4.0 (RHBZ #1440332)

* Sat Mar 11 2017 Remi Collet <remi@fedoraproject.org> - 1.3.10-2
- change URL to documentation site
- simplify documentation

* Sun Mar 05 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.3.10-1
- Updated to 1.3.10 (RHBZ #1411062)
- Test with SCLs if available

* Mon Jan 23 2017 Remi Collet <remi@remirepo.net> - 1.3.10-1
- update to 1.3.10

* Wed Jan 18 2017 Remi Collet <remi@remirepo.net> - 1.3.9-1
- update to 1.3.9

* Fri Jan  6 2017 Remi Collet <remi@remirepo.net> - 1.3.8-1
- update to 1.3.8

* Sat Dec 03 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.3.7-1
- Updated to 1.3.7 (RHBZ #1318837)
- Switch autoloader from php-composer(symfony/class-loader) to
  php-composer(fedora/autoloader)

* Wed Oct 12 2016 Remi Collet <remi@remirepo.net> - 1.3.7-1
- update to 1.3.7

* Thu Sep  8 2016 Remi Collet <remi@remirepo.net> - 1.3.6-1
- update to 1.3.6

* Wed Apr  6 2016 Remi Collet <remi@remirepo.net> - 1.3.5-1
- update to 1.3.5

* Mon Jan 04 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.3.3-1
- Updated to 1.3.3 (RHBZ #1285581)

* Mon Oct 26 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1.4-1
- Updated to 1.1.4 (RHBZ #1272627)

* Sun Oct 18 2015 Remi Collet <remi@remirepo.net> - 1.1.4-1
- update to 1.1.4

* Tue Aug 11 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1.3-1
- Updated to 1.1.3 (RHBZ #1252195)
- Updated autoloader to load dependencies after self registration

* Tue Aug 11 2015 Remi Collet <remi@remirepo.net> - 1.1.3-1
- update to 1.1.3

* Mon Jul 20 2015 Remi Collet <remi@remirepo.net> - 1.1.2-1
- add EL-5 stuff, backport for #remirepo

* Wed Jul 15 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1.2-1
- Update to 1.1.2
- Fix license
- Update description
- Use full path in autoloader

* Wed Jul 08 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1.1-1
- Initial package
