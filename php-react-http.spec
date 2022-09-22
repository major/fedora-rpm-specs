#
# Fedora spec file for php-react-http
#
# Copyright (c) 2017-2022 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     reactphp
%global github_name      http
%global github_version   1.6.0
%global github_commit    59961cc4a5b14481728f07c591546be18fa3a5c7

%global composer_vendor  react
%global composer_project http

# "php": ">=5.3.0"
%global php_min_ver 5.3.0
# "clue/block-react": "^1.5"
%global clue_block_react_min_ver 1.5
%global clue_block_react_max_ver 2.0
# "clue/http-proxy-react": "^1.3", ignored as only used in examples
# "clue/reactphp-ssh-proxy": "^1.0", ignored as only used in examples
# "clue/socks-react": "^1.0", ignored as only used in examples
# "evenement/evenement": "^3.0 || ^2.0 || ^1.0"
%global evenement_min_ver 1.0
%global evenement_max_ver 4.0
# "react/promise": "^2.3 || ^1.2.1"
%global react_promise_min_ver 1.2.1
%global react_promise_max_ver 3.0
# "react/promise-stream": "^1.1"
%global react_promise_stream_min_ver 1.1
%global react_promise_stream_max_ver 2.0
# "react/socket": "^1.9"
%global react_socket_min_ver 1.9
%global react_socket_max_ver 2.0
# "react/stream": "^1.2"
%global react_stream_min_ver 1.2
%global react_stream_max_ver 2.0
# "ringcentral/psr7": "^1.2"
%global ringcentral_psr7_min_ver 1.2
%global ringcentral_psr7_max_ver 2.0
# "react/event-loop": "^1.2",
%global react_event_loop_min_ver 1.2
%global react_event_loop_max_ver 2.0
# "psr/http-message": "^1.0"
%global psr_http_message_min_ver 1.0
%global psr_http_message_max_ver 2.0
# "psr/http-message": "^1.0"
%global fig_http_message_util_min_ver 1.1
%global fig_http_message_util_max_ver 2

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
Release:       2%{?github_release}%{?dist}
Summary:       Library for building an evented http server

License:       MIT
URL:           https://reactphp.org/http/

# GitHub export does not include tests
# Run php-react-http-get-source.sh to create full source
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
%if 0%{?fedora} >= 32 || 0%{?rhel} >= 9
# "phpunit/phpunit": "^9.3 || ^5.7 || ^4.8.35"
%global phpunit %{_bindir}/phpunit9
BuildRequires: phpunit9 >= 9.3
%else
%global phpunit %{_bindir}/phpunit
BuildRequires: php-phpunit-PHPUnit >= 4.8.35
%endif
%if %{with_range_dependencies}
BuildRequires: (php-composer(clue/block-react) >= %{clue_block_react_min_ver} with php-composer(clue/block-react) < %{clue_block_react_max_ver})
BuildRequires: (php-composer(evenement/evenement) >= %{evenement_min_ver} with php-composer(evenement/evenement) < %{evenement_max_ver})
BuildRequires: (php-composer(react/event-loop) >= %{react_event_loop_min_ver} with php-composer(react/event-loop) < %{react_event_loop_max_ver})
BuildRequires: (php-composer(react/promise-stream) >= %{react_promise_stream_min_ver} with php-composer(react/promise-stream) < %{react_promise_stream_max_ver})
BuildRequires: (php-composer(react/promise) >= %{react_promise_min_ver} with php-composer(react/promise) < %{react_promise_max_ver})
BuildRequires: (php-composer(react/socket) >= %{react_socket_min_ver} with php-composer(react/socket) < %{react_socket_max_ver})
BuildRequires: (php-composer(react/stream) >= %{react_stream_min_ver} with php-composer(react/stream) < %{react_stream_max_ver})
BuildRequires: (php-composer(ringcentral/psr7) >= %{ringcentral_psr7_min_ver} with php-composer(ringcentral/psr7) < %{ringcentral_psr7_max_ver})
BuildRequires: (php-composer(psr/http-message) >= %{psr_http_message_min_ver} with php-composer(psr/http-message) < %{psr_http_message_max_ver})
BuildRequires: (php-composer(fig/http-message-util) >= %{fig_http_message_util_min_ver} with php-composer(fig/http-message-util) < %{fig_http_message_util_max_ver})
%else
BuildRequires: php-clue-block-react <  %{clue_block_react_max_ver}
BuildRequires: php-clue-block-react >= %{clue_block_react_min_ver}
BuildRequires: php-evenement <  %{evenement_max_ver}
BuildRequires: php-evenement >= %{evenement_min_ver}
BuildRequires: php-react-event-loop <  %{react_event_loop_max_ver}
BuildRequires: php-react-event-loop >= %{react_event_loop_min_ver}
BuildRequires: php-react-promise-stream <  %{react_promise_stream_max_ver}
BuildRequires: php-react-promise-stream >= %{react_promise_stream_min_ver}
BuildRequires: php-react-promise <  %{react_promise_max_ver}
BuildRequires: php-react-promise >= %{react_promise_min_ver}
BuildRequires: php-react-socket <  %{react_socket_max_ver}
BuildRequires: php-react-socket >= %{react_socket_min_ver}
BuildRequires: php-react-stream <  %{react_stream_max_ver}
BuildRequires: php-react-stream >= %{react_stream_min_ver}
BuildRequires: php-ringcentral-psr7 <  %{ringcentral_psr7_max_ver}
BuildRequires: php-ringcentral-psr7 >= %{ringcentral_psr7_min_ver}
BuildRequires: php-psr-http-message <  %{psr_http_message_max_ver}
BuildRequires: php-psr-http-message >= %{psr_http_message_min_ver}
BuildRequires: php-composer(fig/http-message-util) <  %{fig_http_message_util_max_ver}
BuildRequires: php-composer(fig/http-message-util) >= %{fig_http_message_util_min_ver}
%endif
## phpcompatinfo (computed from version 1.1.0)
BuildRequires: php-reflection
BuildRequires: php-simplexml
BuildRequires: php-date
BuildRequires: php-json
BuildRequires: php-pcre
BuildRequires: php-sockets
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
%if %{with_range_dependencies}
Requires:      (php-composer(evenement/evenement) >= %{evenement_min_ver} with php-composer(evenement/evenement) < %{evenement_max_ver})
Requires:      (php-composer(react/event-loop) >= %{react_event_loop_min_ver} with php-composer(react/event-loop) < %{react_event_loop_max_ver})
Requires:      (php-composer(react/promise-stream) >= %{react_promise_stream_min_ver} with php-composer(react/promise-stream) < %{react_promise_stream_max_ver})
Requires:      (php-composer(react/promise) >= %{react_promise_min_ver} with php-composer(react/promise) < %{react_promise_max_ver})
Requires:      (php-composer(react/socket) >= %{react_socket_min_ver} with php-composer(react/socket) < %{react_socket_max_ver})
Requires:      (php-composer(react/stream) >= %{react_stream_min_ver} with php-composer(react/stream) < %{react_stream_max_ver})
Requires:      (php-composer(ringcentral/psr7) >= %{ringcentral_psr7_min_ver} with php-composer(ringcentral/psr7) < %{ringcentral_psr7_max_ver})
Requires:      (php-composer(psr/http-message) >= %{psr_http_message_min_ver} with php-composer(psr/http-message) < %{psr_http_message_max_ver})
Requires:      (php-composer(fig/http-message-util) >= %{fig_http_message_util_min_ver} with php-composer(fig/http-message-util) < %{fig_http_message_util_max_ver})
%else
Requires:      php-evenement <  %{evenement_max_ver}
Requires:      php-evenement >= %{evenement_min_ver}
Requires:      php-react-event-loop <  %{react_event_loop_max_ver}
Requires:      php-react-event-loop >= %{react_event_loop_min_ver}
Requires:      php-react-promise-stream <  %{react_promise_stream_max_ver}
Requires:      php-react-promise-stream >= %{react_promise_stream_min_ver}
Requires:      php-react-promise <  %{react_promise_max_ver}
Requires:      php-react-promise >= %{react_promise_min_ver}
Requires:      php-react-socket <  %{react_socket_max_ver}
Requires:      php-react-socket >= %{react_socket_min_ver}
Requires:      php-react-stream <  %{react_stream_max_ver}
Requires:      php-react-stream >= %{react_stream_min_ver}
Requires:      php-ringcentral-psr7 <  %{ringcentral_psr7_max_ver}
Requires:      php-ringcentral-psr7 >= %{ringcentral_psr7_min_ver}
Requires:      php-psr-http-message <  %{psr_http_message_max_ver}
Requires:      php-psr-http-message >= %{psr_http_message_min_ver}
Requires:      php-composer(fig/http-message-util) <  %{fig_http_message_util_max_ver}
Requires:      php-composer(fig/http-message-util) >= %{fig_http_message_util_min_ver}
%endif
# phpcompatinfo (computed from version 1.1.0)
Requires:      php-date
Requires:      php-pcre
Requires:      php-sockets
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
Library for building an evented http server.

This component builds on top of the Socket component to implement HTTP. Here
are the main concepts:

* Server: Attaches itself to an instance of React\Socket\ServerInterface,
      parses any incoming data as HTTP, emits a request event for each request.
* Request: A ReadableStream which streams the request body and contains meta
      data which was parsed from the request header.
* Response A WritableStream which streams the response body. You can set the
      status code and response headers via the writeHead() method.

Autoloader: %{phpdir}/React/Http/autoload.php


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

\Fedora\Autoloader\Autoload::addPsr4('React\\Http\\', __DIR__);

\Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}/Evenement/autoload.php',
    '%{phpdir}/React/EventLoop/autoload.php',
    '%{phpdir}/React/Promise/autoload.php',
    '%{phpdir}/React/Promise/Stream/autoload.php',
    '%{phpdir}/React/Socket/autoload.php',
    '%{phpdir}/React/Stream/autoload.php',
    '%{phpdir}/RingCentral/Psr7/autoload.php',
    '%{phpdir}/Psr/Http/Message/autoload.php',
    '%{phpdir}/Fig/Http/Message/autoload.php',
));
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/React
cp -rp src %{buildroot}%{phpdir}/React/Http


%check
%if %{with_tests}
: Create tests bootstrap
mkdir vendor
cat <<'BOOTSTRAP' | tee vendor/autoload.php
<?php
require '%{buildroot}%{phpdir}/React/Http/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('React\\Tests\\Http\\', dirname(__DIR__).'/tests');

\Fedora\Autoloader\Dependencies::required(array(
  '%{phpdir}/Clue/React/Block/autoload.php',
));
BOOTSTRAP

: Skip test requiring network access and/or fail in restrictive buildroot env -- i.e. Bodhi
FILTER="testSuccessfulResponseEmitsEnd|testPostDataReturnsData|testPostJsonReturnsData\
|testCanAccessHttps|testVerifyPeerDisabledForBadSslResolves|testCancelPendingConnectionEmitsClose"

: Upstream tests
RETURN_CODE=0
for CMDARG in "php %{phpunit}" php74 php80 php81; do
    if which $CMDARG; then
        set $CMDARG
        $1 ${2:-%{_bindir}/phpunit9} \
            --filter "^((?!($FILTER)).)*\$" \
            --verbose \
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
%{phpdir}/React/Http


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb  3 2022 Remi Collet <remi@remirepo.net> - 1.6.0-1
- update to 1.6.0
- raise dependency on clue/block-react 1.5
- add dependency on fig/http-message-util

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Aug  5 2021 Remi Collet <remi@remirepo.net> - 1.5.0-1
- update to 1.5.0
- raise dependency on react/socket 1.9

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 12 2021 Remi Collet <remi@remirepo.net> - 1.4.0-1
- update to 1.4.0
- raise dependency on react/event-loop 1.2
- raise dependency on react/socket 1.8
- raise dependency on react/stream 1.2

* Tue Apr 13 2021 Remi Collet <remi@remirepo.net> - 1.3.0-1
- update to 1.3.0

* Wed Mar 24 2021 Remi Collet <remi@remirepo.net> - 1.2.0-1
- update to 1.2.0
- add dependency on react/event-loop
- add dependency on psr/http-message
- raise dependency on react/socket 1.6
- raise dependency on react/stream 1.1
- switch to phpunit9

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 06 2020 Shawn Iwinski <shawn@iwin.ski> - 0.8.6-1
- Update to 0.8.6 (RHBZ #1790302)
- Use PHPUnit 7

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 2019 Shawn Iwinski <shawn@iwin.ski> - 0.8.5-1
- Update to 0.8.5 (RHBZ #1767189)
- Use PHPUnit 6

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Shawn Iwinski <shawn@iwin.ski> - 0.8.3-1
- Update to 0.8.3 (RHBZ #1421136)
- Add range version dependencies for Fedora >= 27 || RHEL >= 8
- Add composer.json to repo

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 24 2017 Shawn Iwinski <shawn@iwin.ski> - 0.4.2-2
- Minor update to SCL tests (only php55 if rhel)

* Tue Jan 17 2017 Shawn Iwinski <shawn@iwin.ski> - 0.4.2-1
- Initial package
