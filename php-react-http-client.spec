#
# Fedora spec file for php-react-http-client
#
# Copyright (c) 2017-2021 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     reactphp
%global github_name      http-client
%global github_version   0.5.11
%global github_commit    23dddb415b9bd36c81d1c78df63143e65702aa4b

%global composer_vendor  react
%global composer_project http-client

# "php": ">= 5.4.0"
%global php_min_ver 5.4.0
# "clue/block-react": "^1.2"
%global clue_block_react_min_ver 1.2
%global clue_block_react_max_ver 2.0
# "evenement/evenement": "^3.0 || ^2.0 || ^1.0"
%global evenement_min_ver 1.0
%global evenement_max_ver 4.0
# "ringcentral/psr7": "^1.2"
%global ringcentral_psr7_min_ver 1.2
%global ringcentral_psr7_max_ver 2.0
# "react/event-loop": "^1.0 || ^0.5 || ^0.4 || ^0.3"
%global react_event_loop_min_ver 0.3
%global react_event_loop_max_ver 2.0
# "react/promise": "^2.1 || ^1.2.1"
%global react_promise_min_ver 1.2.1
%global react_promise_max_ver 3.0
# "react/promise-stream": "^1.1"
%global react_promise_stream_min_ver 1.1
%global react_promise_stream_max_ver 2.0
# "react/socket": "^1.0 || ^0.8.4"
%global react_socket_min_ver 0.8.4
%global react_socket_max_ver 2.0
# "react/stream": "^1.0 || ^0.7.1"
%global react_stream_min_ver 0.7.1
%global react_stream_max_ver 2.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

# Range dependencies supported?
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
%global with_range_dependencies 1
%else
%global with_range_dependencies 0
%endif

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       4%{?github_release}%{?dist}
Summary:       Asynchronous HTTP client library

License:       MIT
URL:           https://reactphp.org/http-client/

# GitHub export does not include tests
# Run php-react-http-client-get-source.sh to create full source
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
Requires:      php(language) >= %{php_min_ver}
BuildRequires: phpunit7
%if %{with_range_dependencies}
BuildRequires: (php-composer(clue/block-react) >= %{clue_block_react_min_ver} with php-composer(clue/block-react) < %{clue_block_react_max_ver})
BuildRequires: (php-composer(evenement/evenement) >= %{evenement_min_ver} with php-composer(evenement/evenement) < %{evenement_max_ver})
BuildRequires: (php-composer(react/event-loop) >= %{react_event_loop_min_ver} with php-composer(react/event-loop) < %{react_event_loop_max_ver})
BuildRequires: (php-composer(react/promise-stream) >= %{react_promise_stream_min_ver} with php-composer(react/promise-stream) < %{react_promise_stream_max_ver})
BuildRequires: (php-composer(react/promise) >= %{react_promise_min_ver} with php-composer(react/promise) < %{react_promise_max_ver})
BuildRequires: (php-composer(react/socket) >= %{react_socket_min_ver} with php-composer(react/socket) < %{react_socket_max_ver})
BuildRequires: (php-composer(react/stream) >= %{react_stream_min_ver} with php-composer(react/stream) < %{react_stream_max_ver})
BuildRequires: (php-composer(ringcentral/psr7) >= %{ringcentral_psr7_min_ver} with php-composer(ringcentral/psr7) < %{ringcentral_psr7_max_ver})
%else
BuildRequires: php-composer(clue/block-react) <  %{clue_block_react_max_ver}
BuildRequires: php-composer(clue/block-react) >= %{clue_block_react_min_ver}
BuildRequires: php-composer(evenement/evenement) <  %{evenement_max_ver}
BuildRequires: php-composer(evenement/evenement) >= %{evenement_min_ver}
BuildRequires: php-composer(react/event-loop) <  %{react_event_loop_max_ver}
BuildRequires: php-composer(react/event-loop) >= %{react_event_loop_min_ver}
BuildRequires: php-composer(react/promise-stream) <  %{react_promise_stream_max_ver}
BuildRequires: php-composer(react/promise-stream) >= %{react_promise_stream_min_ver}
BuildRequires: php-composer(react/promise) <  %{react_promise_max_ver}
BuildRequires: php-composer(react/promise) >= %{react_promise_min_ver}
BuildRequires: php-composer(react/socket) <  %{react_socket_max_ver}
BuildRequires: php-composer(react/socket) >= %{react_socket_min_ver}
BuildRequires: php-composer(react/stream) <  %{react_stream_max_ver}
BuildRequires: php-composer(react/stream) >= %{react_stream_min_ver}
BuildRequires: php-composer(ringcentral/psr7) <  %{ringcentral_psr7_max_ver}
BuildRequires: php-composer(ringcentral/psr7) >= %{ringcentral_psr7_min_ver}
%endif
## phpcompatinfo (computed from version 0.5.9)
BuildRequires: php-json
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
%if %{with_range_dependencies}
Requires:      (php-composer(evenement/evenement) >= %{evenement_min_ver} with php-composer(evenement/evenement) < %{evenement_max_ver})
Requires:      (php-composer(react/event-loop) >= %{react_event_loop_min_ver} with php-composer(react/event-loop) < %{react_event_loop_max_ver})
Requires:      (php-composer(react/promise) >= %{react_promise_min_ver} with php-composer(react/promise) < %{react_promise_max_ver})
Requires:      (php-composer(react/socket) >= %{react_socket_min_ver} with php-composer(react/socket) < %{react_socket_max_ver})
Requires:      (php-composer(react/stream) >= %{react_stream_min_ver} with php-composer(react/stream) < %{react_stream_max_ver})
Requires:      (php-composer(ringcentral/psr7) >= %{ringcentral_psr7_min_ver} with php-composer(ringcentral/psr7) < %{ringcentral_psr7_max_ver})
%else
Requires:      php-composer(evenement/evenement) <  %{evenement_max_ver}
Requires:      php-composer(evenement/evenement) >= %{evenement_min_ver}
Requires:      php-composer(react/event-loop) <  %{react_event_loop_max_ver}
Requires:      php-composer(react/event-loop) >= %{react_event_loop_min_ver}
Requires:      php-composer(react/promise) <  %{react_promise_max_ver}
Requires:      php-composer(react/promise) >= %{react_promise_min_ver}
Requires:      php-composer(react/socket) <  %{react_socket_max_ver}
Requires:      php-composer(react/socket) >= %{react_socket_min_ver}
Requires:      php-composer(react/stream) <  %{react_stream_max_ver}
Requires:      php-composer(react/stream) >= %{react_stream_min_ver}
Requires:      php-composer(ringcentral/psr7) <  %{ringcentral_psr7_max_ver}
Requires:      php-composer(ringcentral/psr7) >= %{ringcentral_psr7_min_ver}
%endif
# phpcompatinfo (computed from version 0.5.9)
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
%{summary}.

Autoloader: %{phpdir}/React/HttpClient/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('React\\HttpClient\\', __DIR__);

\Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}/Evenement/autoload.php',
    '%{phpdir}/React/EventLoop/autoload.php',
    '%{phpdir}/React/Promise/autoload.php',
    '%{phpdir}/React/Socket/autoload.php',
    '%{phpdir}/React/Stream/autoload.php',
    '%{phpdir}/RingCentral/Psr7/autoload.php',
));
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/React
cp -rp src %{buildroot}%{phpdir}/React/HttpClient


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require '%{buildroot}%{phpdir}/React/HttpClient/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('React\\Tests\\HttpClient\\', __DIR__.'/tests');

\Fedora\Autoloader\Dependencies::required(array(
  '%{phpdir}/Clue/React/Block/autoload.php',
  '%{phpdir}/React/Promise/Stream/autoload.php',
));
BOOTSTRAP

: Skip tests requiring network access
rm -f tests/FunctionalIntegrationTest.php

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit7)
for PHP_EXEC in "" php73 php74 php80; do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose --bootstrap bootstrap.php \
            || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json
%{phpdir}/React/HttpClient/


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Apr  8 2021 Remi Collet <remi@remirepo.net> - 0.5.11-1
- update to 0.5.11

* Wed Apr  7 2021 Remi Collet <remi@remirepo.net> - 0.5.10-9
- fix FTBFS with PHP 8

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 06 2020 Shawn Iwinski <shawn@iwin.ski> - 0.5.10-1
- Update to 0.5.10 (RHBZ #1791054)
- Use PHPUnit 7

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 15 2019 Shawn Iwinski <shawn@iwin.ski> - 0.5.9-5
- Loosen dependency versions to allow for updated dependencies
- Use PHPUnit 6

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Shawn Iwinski <shawn@iwin.ski> - 0.5.9-1
- Update to 0.5.9 (RHBZ #1454517)
- Add range version dependencies for Fedora >= 27 || RHEL >= 8
- Add composer.json to repo

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Apr 08 2017 Shawn Iwinski <shawn@iwin.ski> - 0.4.17-1
- Update to 0.4.17 (RHBZ #1434200)

* Sat Mar 11 2017 Shawn Iwinski <shawn@iwin.ski> - 0.4.16-1
- Update to 0.4.16 (RHBZ #1429266)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 25 2017 Shawn Iwinski <shawn@iwin.ski> - 0.4.15-2
- Minor update to SCL tests (only php55 if rhel)

* Tue Jan 17 2017 Shawn Iwinski <shawn@iwin.ski> - 0.4.15-1
- Initial package
