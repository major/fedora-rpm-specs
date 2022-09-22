#
# Fedora spec file for php-react-socket
#
# Copyright (c) 2017-2021 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     reactphp
%global github_name      socket
%global github_version   1.11.0
%global github_commit    f474156aaab4f09041144fa8b57c7d70aed32a1c

%global composer_vendor  react
%global composer_project socket

# "php": ">=5.3.0"
%global php_min_ver 5.3.0
# "clue/block-react": "^1.5"
%global clue_block_react_min_ver 1.5
%global clue_block_react_max_ver 2.0
# "evenement/evenement": "^3.0 || ^2.0 || ^1.0"
%global evenement_min_ver 1.0
%global evenement_max_ver 4.0
# "react/dns": "^1.8"
%global react_dns_min_ver 1.8
%global react_dns_max_ver 2.0
# "react/event-loop": "^1.2"
%global react_event_loop_min_ver 1.2
%global react_event_loop_max_ver 2.0
# "react/promise": "^2.6.0 || ^1.2.1"
%global react_promise_min_ver 1.2.1
%global react_promise_max_ver 3.0
# "react/promise-stream": "^1.2"
%global react_promise_stream_min_ver 1.2
%global react_promise_stream_max_ver 2.0
# "react/promise-timer": "^1.8"
%global react_promise_timer_min_ver 1.8
%global react_promise_timer_max_ver 2.0
# "react/stream": "^1.2"
%global react_stream_min_ver 1.2
%global react_stream_max_ver 2.0

# "phpunit/phpunit": "^9.3 || ^5.7 || ^4.8.35"
%global phpunit_require phpunit9
%global phpunit_min_ver 9.3
%global phpunit_exec    phpunit9

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
Release:       3%{?github_release}%{?dist}
Summary:       Async, streaming plaintext TCP/IP and secure TLS socket server

License:       MIT
URL:           https://reactphp.org/socket/

# GitHub export does not include tests
# Run php-react-socket-get-source.sh to create full source
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: %{phpunit_require} >= %{phpunit_min_ver}
%if %{with_range_dependencies}
BuildRequires: (php-composer(clue/block-react) >= %{clue_block_react_min_ver} with php-composer(clue/block-react) < %{clue_block_react_max_ver})
BuildRequires: (php-composer(evenement/evenement) >= %{evenement_min_ver} with php-composer(evenement/evenement) < %{evenement_max_ver})
BuildRequires: (php-composer(react/dns) >= %{react_dns_min_ver} with php-composer(react/dns) < %{react_dns_max_ver})
BuildRequires: (php-composer(react/event-loop) >= %{react_event_loop_min_ver} with php-composer(react/event-loop) < %{react_event_loop_max_ver})
BuildRequires: (php-composer(react/promise-stream) >= %{react_promise_stream_min_ver} with php-composer(react/promise-stream) < %{react_promise_stream_max_ver})
BuildRequires: (php-composer(react/promise-timer) >= %{react_promise_timer_min_ver} with php-composer(react/promise-timer) < %{react_promise_timer_max_ver})
BuildRequires: (php-composer(react/promise) >= %{react_promise_min_ver} with php-composer(react/promise) < %{react_promise_max_ver})
BuildRequires: (php-composer(react/stream) >= %{react_stream_min_ver} with php-composer(react/stream) < %{react_stream_max_ver})
%else
BuildRequires: php-composer(clue/block-react) <  %{clue_block_react_max_ver}
BuildRequires: php-composer(clue/block-react) >= %{clue_block_react_min_ver}
BuildRequires: php-composer(evenement/evenement) <  %{evenement_max_ver}
BuildRequires: php-composer(evenement/evenement) >= %{evenement_min_ver}
BuildRequires: php-composer(react/dns) >= %{react_dns_min_ver}
BuildRequires: php-composer(react/dns) <  %{react_dns_max_ver}
BuildRequires: php-composer(react/event-loop) <  %{react_event_loop_max_ver}
BuildRequires: php-composer(react/event-loop) >= %{react_event_loop_min_ver}
BuildRequires: php-composer(react/promise) <  %{react_promise_max_ver}
BuildRequires: php-composer(react/promise) >= %{react_promise_min_ver}
BuildRequires: php-composer(react/promise-timer) >= %{react_promise_timer_min_ver}
BuildRequires: php-composer(react/promise-timer) <  %{react_promise_timer_max_ver}
BuildRequires: php-composer(react/promise-stream) >= %{react_promise_stream_min_ver}
BuildRequires: php-composer(react/promise-stream) <  %{react_promise_stream_max_ver}
BuildRequires: php-composer(react/stream) <  %{react_stream_max_ver}
BuildRequires: php-composer(react/stream) >= %{react_stream_min_ver}
%endif
## phpcompatinfo (computed from version 1.6.0)
BuildRequires: php-filter
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-sockets
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
%if %{with_range_dependencies}
Requires:      (php-composer(evenement/evenement) >= %{evenement_min_ver} with php-composer(evenement/evenement) < %{evenement_max_ver})
Requires:      (php-composer(react/dns) >= %{react_dns_min_ver} with php-composer(react/dns) < %{react_dns_max_ver})
Requires:      (php-composer(react/event-loop) >= %{react_event_loop_min_ver} with php-composer(react/event-loop) < %{react_event_loop_max_ver})
Requires:      (php-composer(react/promise) >= %{react_promise_min_ver} with php-composer(react/promise) < %{react_promise_max_ver})
Requires:      (php-composer(react/promise-timer) >= %{react_promise_timer_min_ver} with php-composer(react/promise-timer) < %{react_promise_timer_max_ver})
Requires:      (php-composer(react/stream) >= %{react_stream_min_ver} with php-composer(react/stream) < %{react_stream_max_ver})
%else
Requires:      php-composer(evenement/evenement) <  %{evenement_max_ver}
Requires:      php-composer(evenement/evenement) >= %{evenement_min_ver}
Requires:      php-composer(react/event-loop) <  %{react_event_loop_max_ver}
Requires:      php-composer(react/event-loop) >= %{react_event_loop_min_ver}
Requires:      php-composer(react/dns) <  %{react_dns_max_ver}
Requires:      php-composer(react/dns) >= %{react_dns_min_ver}
Requires:      php-composer(react/promise) <  %{react_promise_max_ver}
Requires:      php-composer(react/promise) >= %{react_promise_min_ver}
Requires:      php-composer(react/promise-timer) >= %{react_promise_timer_min_ver}
Requires:      php-composer(react/promise-timer) <  %{react_promise_timer_max_ver}
Requires:      php-composer(react/stream) <  %{react_stream_max_ver}
Requires:      php-composer(react/stream) >= %{react_stream_min_ver}
%endif
# phpcompatinfo (computed from version 1.6.0)
Requires:      php-filter
Requires:      php-pcre
Requires:      php-sockets
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Packages have been merged (not provided as class names are different)
Obsoletes:     php-react-socket-client < 0.5

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
Async, streaming plaintext TCP/IP and secure TLS socket server for React PHP.

The socket component provides a more usable interface for a socket-layer server
based on the EventLoop and Stream components.

Autoloader: %{phpdir}/React/Socket/autoload.php


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

\Fedora\Autoloader\Autoload::addPsr4('React\\Socket\\', __DIR__);

\Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}/Evenement/autoload.php',
    '%{phpdir}/React/Dns/autoload.php',
    '%{phpdir}/React/EventLoop/autoload.php',
    '%{phpdir}/React/Promise/autoload.php',
    '%{phpdir}/React/Promise/Timer/autoload.php',
    '%{phpdir}/React/Stream/autoload.php',
));
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/React
cp -rp src %{buildroot}%{phpdir}/React/Socket


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require '%{buildroot}%{phpdir}/React/Socket/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('React\\Tests\\Socket\\\\', __DIR__.'/tests');

\Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}/Clue/React/Block/autoload.php',
    '%{phpdir}/React/Promise/Stream/autoload.php',
));
BOOTSTRAP

: Skip test requiring network access
rm -f tests/IntegrationTest.php

%if 0%{?fedora} >= 36 || 0%{?rhel} >= 9
# https://github.com/reactphp/socket/issues/275 - OpenSSL 3.0
FILTER="--filter '^((?!(testClientUsesTls10WhenCryptoMethodIsExplicitlyConfiguredByClient)).)*$'"
%endif

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which %{phpunit_exec})
for PHP_EXEC in "" php74 php80 php81; do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT $FILTER \
            --bootstrap bootstrap.php \
            --exclude-group internet \
            --verbose || RETURN_CODE=1
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
%{phpdir}/React/Socket


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan 14 2022 Remi Collet <remi@remirepo.net> - 1.11.0-1
- update to 1.11.0
- raise dependency on react/promise-timer 1.8
- raise dependency on clue/block-react 1.5

* Mon Nov 29 2021 Remi Collet <remi@remirepo.net> - 1.10.0-1
- update to 1.10.0

* Wed Aug  4 2021 Remi Collet <remi@remirepo.net> - 1.9.0-1
- update to 1.9.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 12 2021 Remi Collet <remi@remirepo.net> - 1.8.0-1
- update to 1.8.0
- raise dependency on react/dns 1.8
- raise dependency on react/event-loop 1.2
- raise dependency on react/stream 1.2

* Mon Jun 28 2021 Remi Collet <remi@remirepo.net> - 1.7.0-1
- update to 1.7.0
- raise dependency on react/dns 1.7

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Sep 06 2020 Shawn Iwinski <shawn@iwin.ski> - 1.6.0-1
- Update to 1.6.0 (RHBZ #1812925)
- Remove patch merged upstream
- Use PHPUnit 9
- Exclude group "internet" in tests

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 2019 Shawn Iwinski <shawn@iwin.ski> - 1.3.0-1
- Update to 1.3.0 (RHBZ #1600308)
- Use PHPUnit 6

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul  3 2018 Remi Collet <remi@remirepo.net> - 0.8.12-3
- obsolete php-react-socket-client (merged)

* Tue Jul  3 2018 Remi Collet <remi@remirepo.net> - 0.8.12-2
- add missing dependency on react/dns

* Mon Jul 02 2018 Shawn Iwinski <shawn@iwin.ski> - 0.8.12-1
- Update to 0.8.12 (RHBZ #1422067)
- Add range version dependencies for Fedora >= 27 || RHEL >= 8
- Add composer.json to repo

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Shawn Iwinski <shawn@iwin.ski> - 0.4.6-1
- Update to 0.4.6 (RHBZ #1416802)

* Tue Jan 24 2017 Shawn Iwinski <shawn@iwin.ski> - 0.4.5-2
- Restrict evenement/evenement and react/promise dependencies to one major version
- Minor update to SCL tests (only php54 and php55 if rhel)

* Tue Jan 17 2017 Shawn Iwinski <shawn@iwin.ski> - 0.4.5-1
- Initial package
