# remirepo/Fedora spec file for php-laminas-diactoros
#
# Copyright (c) 2015-2021 Shawn Iwinski, Remi Collet
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global gh_owner     laminas
%global gh_project   laminas-diactoros
%global zf_name      zend-diactoros
%global gh_commit    6991c1af7c8d2c8efee81b22ba97024781824aaa
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Diactoros

%global gh_psr7_owner     php-http
%global gh_psr7_name      psr7-integration-tests
%global gh_psr7_version   0
%global gh_psr7_commit    5dfefb2da33ca24ae20c971b725c9a6fe7403008
%global gh_psr7_short     %(c=%{gh_psr7_commit}; echo ${c:0:7})

# "php": "^5.6 || ^7.0"
%global php_min_ver 5.6
# "psr/http-message": "^1.0"
%global psr_http_message_min_ver 1.0
%global psr_http_message_max_ver 2.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{gh_project}
Version:       1.8.7p2
Release:       7%{?gh_release}%{?dist}
Summary:       PSR HTTP Message implementations

License:       BSD
URL:           https://github.com/%{gh_owner}/%{gh_project}

# GitHub export does not include tests.
# Run makesrc.sh to create full source.
Source0:       %{name}-%{version}-%{gh_short}.tgz
Source1:       makesrc.sh
# Temporarily bundled, no release, only used for tests
Source2:       %{gh_psr7_owner}-%{gh_psr7_name}-%{gh_psr7_version}-%{gh_psr7_short}.tgz
Source3:       %{gh_psr7_owner}-%{gh_psr7_name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0 with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
BuildRequires: (php-composer(psr/http-message) >= %{psr_http_message_min_ver}   with php-composer(psr/http-message) <  %{psr_http_message_max_ver})
%global phpunit %{_bindir}/phpunit7
BuildRequires:  %{phpunit}
BuildRequires:  php-dom
BuildRequires:  php-libxml
## phpcompatinfo (computed from version 1.8.7p1)
### NOTE: curl, gd, gmp, and shmop are all optional for
###       LaminasTest\Diactoros\StreamTest::getResourceFor67()
###       (test/StreamTest.php) but the first one found wins
###       so only curl is chosen as a requirement here.
BuildRequires:  php-curl
BuildRequires:  php-dom
BuildRequires:  php-json
BuildRequires:  php-libxml
BuildRequires:  php-pcre
BuildRequires:  php-reflection
BuildRequires:  php-shmop
BuildRequires:  php-spl
%endif
## Autoloader
BuildRequires:  php-fedora-autoloader-devel

# composer.json
Requires:       php(language) >= %{php_min_ver}
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0 with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
Requires:      (php-composer(psr/http-message) >= %{psr_http_message_min_ver}   with php-composer(psr/http-message) <  %{psr_http_message_max_ver})
# phpcompatinfo (computed from version 1.8.7p1)
Requires:       php-json
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

# Composer
# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 1.8.7p1
Provides:       php-zendframework-%{zf_name}              = %{version}
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}
Provides:       php-composer(psr/http-message-implementation) = 1.0


%description
A PHP package containing implementations of the accepted PSR-7 HTTP message
interfaces [1], as well as a "server" implementation similar to node's
http.Server [2].

Documentation: https://docs.laminas.dev/%{gh_project}/

Autoloader: %{phpdir}/%{namespace}/Diactoros/autoload.php

[1] http://www.php-fig.org/psr/psr-7/
[2] http://nodejs.org/api/http.html


%prep
%setup -qn %{gh_project}-%{gh_commit} -a2

mv %{gh_psr7_name}-%{gh_psr7_commit} psr7
mv LICENSE.md LICENSE


%build
: Create autoloader
phpab --template fedora --output src/autoload.php src
cat <<'AUTOLOAD' | tee -a src/autoload.php
if (!function_exists('Laminas\\Diactoros\\createUploadedFile')) {
  \Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}/Psr/Http/Message/autoload.php',
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

cat << 'EOF' | tee zf.php
<?php
require_once '%{php_home}/Fedora/Autoloader/autoload.php';
$dir = dirname(dirname(__DIR__)) . '/%{namespace}/%{library}';
if (!function_exists('Zend\\Diactoros\\createUploadedFile')) {
  \Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/ZendFrameworkBridge/autoload.php',
    $dir . '/autoload.php',
    $dir . '/functions/create_uploaded_file.legacy.php',
    $dir . '/functions/marshal_headers_from_sapi.legacy.php',
    $dir . '/functions/marshal_method_from_sapi.legacy.php',
    $dir . '/functions/marshal_protocol_version_from_sapi.legacy.php',
    $dir . '/functions/marshal_uri_from_sapi.legacy.php',
    $dir . '/functions/normalize_server.legacy.php',
    $dir . '/functions/normalize_uploaded_files.legacy.php',
    $dir . '/functions/parse_cookie_header.legacy.php',
  ]);
}
EOF


%install
: Laminas library
mkdir -p   %{buildroot}%{php_home}/%{namespace}/
cp -pr src %{buildroot}%{php_home}/%{namespace}/%{library}

: Zend equiv
mkdir -p      %{buildroot}%{php_home}/Zend/%{library}
cp -pr zf.php %{buildroot}%{php_home}/Zend/%{library}/autoload.php


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php

require_once '%{buildroot}%{phpdir}/%{namespace}/Diactoros/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{namespace}Test\\Diactoros\\', __DIR__.'/test');
\Fedora\Autoloader\Autoload::addPsr4('Http\\Psr7Test\\', __DIR__.'/psr7/src');

\Fedora\Autoloader\Dependencies::required(array(
    __DIR__.'/test/TestAsset/Functions.php',
    __DIR__.'/test/TestAsset/SapiResponse.php',
));
BOOTSTRAP

: Upstream tests
# Skip testReasonPhraseDefaultsAgainstIana requiring network access
RETURN_CODE=0
for CMDARG in "php %{phpunit}" php73 php74 php80; do
    if which $CMDARG; then
        set $CMDARG
        $1 ${2:-%{_bindir}/phpunit7} \
           --bootstrap bootstrap.php \
           --filter '^((?!(testReasonPhraseDefaultsAgainstIana)).)*$' \
           --verbose || RETURN_CODE=1
    fi
done

: check compat autoloader
php -r '
require "%{buildroot}%{php_home}/Zend/%{library}/autoload.php";
exit (class_exists("\\Zend\\%{library}\\Request") ? 0 : 1);
'

exit $RETURN_CODE
%else
: Tests skipped
%endif


%files
%license LICENSE
%doc *.md
%doc composer.json
%{php_home}/Zend/%{library}
%{php_home}/%{namespace}/%{library}


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.7p2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.7p2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.7p2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Mar 25 2021 Remi Collet <remi@remirepo.net> - 1.8.7p2-4
- switch to phpunit7

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.7p2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.7p2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 30 2020 Remi Collet <remi@remirepo.net> - 1.8.7p2-1
- update to 1.8.7p2 (no change)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.7p1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Remi Collet <remi@remirepo.net> - 1.8.7p1-3
- fix autoloader, ensure functions are not defined twice

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
