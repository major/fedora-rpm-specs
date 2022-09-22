#
# Fedora spec file for php-react-promise-stream
#
# Copyright (c) 2018-2022 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     reactphp
%global github_name      promise-stream
%global github_version   1.4.0
%global github_commit    ef05517b99e4363beaa7993d4e2d6c50f1b22a09

%global composer_vendor  react
%global composer_project promise-stream

# "php": ">=5.3"
%global php_min_ver 5.3
# "clue/block-react": "^1.0"
%global clue_block_react_min_ver 1.0
%global clue_block_react_max_ver 2.0
# "react/event-loop": "^1.0 || ^0.5 || ^0.4 || ^0.3"
%global react_event_loop_min_ver 0.3
%global react_event_loop_max_ver 2.0
# "react/promise": "^2.1 || ^1.2"
%global react_promise_min_ver 1.2
%global react_promise_max_ver 3.0
# "react/promise-timer": "^1.0"
%global react_promise_timer_min_ver 1.0
%global react_promise_timer_max_ver 2.0
# "react/stream": "^1.0 || ^0.7 || ^0.6 || ^0.5 || ^0.4.6"
%global react_stream_min_ver 0.4.6
%global react_stream_max_ver 2.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       2%{?github_release}%{?dist}
Summary:       The missing link between Promise-land and Stream-land for ReactPHP

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}

# GitHub export does not include tests
# Run php-react-stream-get-source.sh to create full source
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-sources.sh

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: phpunit9 >= 9.3
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-composer(clue/block-react) >= %{clue_block_react_min_ver} with php-composer(clue/block-react) < %{clue_block_react_max_ver})
BuildRequires: (php-composer(react/event-loop) >= %{react_event_loop_min_ver} with php-composer(react/event-loop) < %{react_event_loop_max_ver})
BuildRequires: (php-composer(react/promise-timer) >= %{react_promise_timer_min_ver} with php-composer(react/promise-timer) < %{react_promise_timer_max_ver})
BuildRequires: (php-composer(react/promise) >= %{react_promise_min_ver} with php-composer(react/promise) < %{react_promise_max_ver})
BuildRequires: (php-composer(react/stream) >= %{react_stream_min_ver} with php-composer(react/stream) < %{react_stream_max_ver})
%else
BuildRequires: php-composer(clue/block-react) <  %{clue_block_react_max_ver}
BuildRequires: php-composer(clue/block-react) >= %{clue_block_react_min_ver}
BuildRequires: php-composer(react/event-loop) <  %{react_event_loop_max_ver}
BuildRequires: php-composer(react/event-loop) >= %{react_event_loop_min_ver}
BuildRequires: php-composer(react/promise-timer) <  %{react_promise_timer_max_ver}
BuildRequires: php-composer(react/promise-timer) >= %{react_promise_timer_min_ver}
BuildRequires: php-composer(react/promise) <  %{react_promise_max_ver}
BuildRequires: php-composer(react/promise) >= %{react_promise_min_ver}
BuildRequires: php-composer(react/stream) <  %{react_stream_max_ver}
BuildRequires: php-composer(react/stream) >= %{react_stream_min_ver}
%endif
##  phpcompatinfo (computed from version 1.2.0)
BuildRequires: php-reflection
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:      (php-composer(react/promise) >= %{react_promise_min_ver} with php-composer(react/promise) < %{react_promise_max_ver})
Requires:      (php-composer(react/stream) >= %{react_stream_min_ver} with php-composer(react/stream) < %{react_stream_max_ver})
%else
Requires:      php-composer(react/promise) <  %{react_promise_max_ver}
Requires:      php-composer(react/promise) >= %{react_promise_min_ver}
Requires:      php-composer(react/stream) <  %{react_stream_max_ver}
Requires:      php-composer(react/stream) >= %{react_stream_min_ver}
%endif
# phpcompatinfo (computed from version 1.2.0)
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
The missing link between Promise-land and Stream-land for ReactPHP [1].

Autoloader: %{phpdir}/React/Promise/Stream/autoload.php

[1] https://reactphp.org/


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

\Fedora\Autoloader\Autoload::addPsr4('React\\Promise\\Stream\\', __DIR__);

\Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}/React/Promise/autoload.php',
    '%{phpdir}/React/Stream/autoload.php',
    __DIR__.'/functions_include.php',
));
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/React/Promise
cp -rp src %{buildroot}%{phpdir}/React/Promise/Stream


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require '%{buildroot}%{phpdir}/React/Promise/Stream/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('React\\Tests\\Promise\\Stream\\', __DIR__.'/tests');

\Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}/Clue/React/Block/autoload.php',
    '%{phpdir}/React/EventLoop/autoload.php',
    '%{phpdir}/React/Promise/Timer/autoload.php',
));
BOOTSTRAP

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit9)
for PHP_EXEC in php php74 php80 php81 php82; do
    if which $PHP_EXEC; then
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
%{phpdir}/React/Promise/Stream


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 20 2022 Remi Collet <remi@remirepo.net> - 1.4.0-1
- update to 1.4.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct 21 2021 Remi Collet <remi@remirepo.net> - 1.3.0-1
- update to 1.3.0
- switch to phpunit9

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 2019 Shawn Iwinski <shawn@iwin.ski> - 1.2.0-1
- Update to 1.2.0 (RHBZ #1783720)
- Use PHPUnit 7

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Apr 21 2018 Shawn Iwinski <shawn@iwin.ski> - 1.1.1-2
- Add range version dependencies for Fedora >= 27 || RHEL >= 8

* Wed Jan 03 2018 Shawn Iwinski <shawn@iwin.ski> - 1.1.1-1
- Initial package
