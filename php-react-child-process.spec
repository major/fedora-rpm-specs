#
# Fedora spec file for php-react-child-process
#
# Copyright (c) 2017-2021 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     reactphp
%global github_name      child-process
%global github_version   0.6.4
%global github_commit    a778f3fb828d68caf8a9ab6567fd8342a86f12fe

%global composer_vendor  react
%global composer_project child-process

# "php": ">=5.3.0"
%global php_min_ver 5.3.0
# "evenement/evenement": "^3.0 || ^2.0 || ^1.0"
%global evenement_min_ver 2.0
%global evenement_max_ver 4.0
# "react/event-loop": "^1.2"
%global react_event_loop_min_ver 1.2
%global react_event_loop_max_ver 2.0
# "react/socket": "^1.8"
%global react_socket_min_ver 1.8
%global react_socket_max_ver 2.0
# "react/stream": "^1.2"
%global react_stream_min_ver 1.2
%global react_stream_max_ver 2.0
# "sebastian/environment": "^5.0 || ^3.0 || ^2.0 || ^1.0"
%global sebastian_environment_min_ver 1.0
%global sebastian_environment_max_ver 6

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       3%{?github_release}%{?dist}
Summary:       Library for executing child processes

License:       MIT
URL:           https://reactphp.org/child-process/

# GitHub export does not include tests
# Run php-react-cache-get-source.sh to create full source
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
# "phpunit/phpunit": "^9.3 || ^5.7 || ^4.8.35"
%global phpunit %{_bindir}/phpunit9
BuildRequires: phpunit9 >= 9.3
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-composer(evenement/evenement) >= %{evenement_min_ver} with php-composer(evenement/evenement) < %{evenement_max_ver})
BuildRequires: (php-composer(react/event-loop) >= %{react_event_loop_min_ver} with php-composer(react/event-loop) < %{react_event_loop_max_ver})
BuildRequires: (php-composer(react/socket) >= %{react_socket_min_ver} with php-composer(react/socket) < %{react_socket_max_ver})
BuildRequires: (php-composer(react/stream) >= %{react_stream_min_ver} with php-composer(react/stream) < %{react_stream_max_ver})
BuildRequires: (php-composer(sebastian/environment) >= %{sebastian_environment_min_ver} with php-composer(sebastian/environment) < %{sebastian_environment_max_ver})
%else
BuildRequires: php-composer(evenement/evenement) <  %{evenement_max_ver}
BuildRequires: php-composer(evenement/evenement) >= %{evenement_min_ver}
BuildRequires: php-composer(react/event-loop) <  %{react_event_loop_max_ver}
BuildRequires: php-composer(react/event-loop) >= %{react_event_loop_min_ver}
BuildRequires: php-composer(react/socket) <  %{react_socket_max_ver}
BuildRequires: php-composer(react/socket) >= %{react_socket_min_ver}
BuildRequires: php-composer(react/stream) <  %{react_stream_max_ver}
BuildRequires: php-composer(react/stream) >= %{react_stream_min_ver}
# use the one pulled by PHPUnit
#BuildRequires: php-composer(sebastian/environment) <  %%{sebastian_environment_max_ver}
#BuildRequires: php-composer(sebastian/environment) >= %%{sebastian_environment_min_ver}
%endif
## phpcompatinfo (computed from version 0.6.1)
BuildRequires: php-iconv
BuildRequires: php-pcntl
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:      (php-composer(evenement/evenement) >= %{evenement_min_ver} with php-composer(evenement/evenement) < %{evenement_max_ver})
Requires:      (php-composer(react/event-loop) >= %{react_event_loop_min_ver} with php-composer(react/event-loop) < %{react_event_loop_max_ver})
Requires:      (php-composer(react/stream) >= %{react_stream_min_ver} with php-composer(react/stream) < %{react_stream_max_ver})
%else
Requires:      php-composer(evenement/evenement) <  %{evenement_max_ver}
Requires:      php-composer(evenement/evenement) >= %{evenement_min_ver}
Requires:      php-composer(react/event-loop) <  %{react_event_loop_max_ver}
Requires:      php-composer(react/event-loop) >= %{react_event_loop_min_ver}
Requires:      php-composer(react/stream) <  %{react_stream_max_ver}
Requires:      php-composer(react/stream) >= %{react_stream_min_ver}
%endif
# phpcompatinfo (computed from version 0.6.1)
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
%{summary}.

Autoloader: %{phpdir}/React/ChildProcess/autoload.php


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

\Fedora\Autoloader\Autoload::addPsr4('React\\ChildProcess\\', __DIR__);

\Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}/Evenement/autoload.php',
    '%{phpdir}/React/EventLoop/autoload.php',
    '%{phpdir}/React/Stream/autoload.php',
));
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/React
cp -rp src %{buildroot}%{phpdir}/React/ChildProcess


%check
%if %{with_tests}
: Create tests bootstrap
mkdir vendor
cat <<'BOOTSTRAP' | tee vendor/autoload.php
<?php
require '%{buildroot}%{phpdir}/React/ChildProcess/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('React\\Tests\\ChildProcess\\', dirname(__DIR__).'/tests');

\Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}/React/Socket/autoload.php',
));
BOOTSTRAP

: Upstream tests
RETURN_CODE=0
for CMDARG in "php %{phpunit}" php73 php80; do
    if which $CMDARG; then
    set $CMDARG
        $1 ${2:-%{_bindir}/phpunit9} --verbose \
            --filter '^((?!(testProcessPidNotSameDueToShellWrapper)).)*$' \
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
%{phpdir}/React/ChildProcess


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct 12 2021 Remi Collet <remi@remirepo.net> - 0.6.4-1
- update to 0.6.4

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 12 2021 Remi Collet <remi@remirepo.net> - 0.6.3-1
- update to 0.6.3
- raise dependency on react/event-loop 1.2
- raise dependency on react/stream 1.2
- raise build dependency on react/socket 1.8

* Wed Mar 24 2021 Remi Collet <remi@remirepo.net> - 0.6.2-1
- update to 0.6.2
- switch to phpunit9
- sources from git snapshot

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 2019 Shawn Iwinski <shawn@iwin.ski> - 0.6.1-1
- Update to 0.6.1 (RHBZ #1677881)
- Use PHPUnit 7

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 01 2018 Shawn Iwinski <shawn@iwin.ski> - 0.5.2-1
- Update to 0.5.2 (RHBZ #1482155)
- Add range version dependencies for Fedora >= 27 || RHEL >= 8
- Add composer.json to repo

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Apr 08 2017 Shawn Iwinski <shawn@iwin.ski> - 0.4.3-1
- Update to 0.4.3 (RHBZ #1432449)

* Sat Mar 11 2017 Shawn Iwinski <shawn@iwin.ski> - 0.4.2-1
- Update to 0.4.2 (RHBZ #1431348)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 24 2017 Shawn Iwinski <shawn@iwin.ski> - 0.4.1-2
- Retrict sebastian/environment dependency to one major version
- Minor update to SCL tests (only php55 if rhel)

* Tue Jan 17 2017 Shawn Iwinski <shawn@iwin.ski> - 0.4.1-1
- Initial package
