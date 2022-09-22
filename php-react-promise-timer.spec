#
# Fedora spec file for php-react-promise-timer
#
# Copyright (c) 2017-2021 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     reactphp
%global github_name      promise-timer
%global github_version   1.9.0
%global github_commit    aa7a73c74b8d8c0f622f5982ff7b0351bc29e495

%global composer_vendor  react
%global composer_project promise-timer

#  "php": ">=5.3"
%global php_min_ver 5.3
# "react/event-loop": "^1.2"
%global react_event_loop_min_ver 1.2
%global react_event_loop_max_ver 2.0
# "react/promise": "^3.0 || ^2.7.0 || ^1.2.1"
# ignore v3 not yet packaged
%global react_promise_min_ver 1.2.1
%global react_promise_max_ver 3.0

# Build using "--without tests" to disable tests
%bcond_without tests

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       2%{?github_release}%{?dist}
Summary:       Trivial timeout implementation for Promises

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}

# GitHub export does not include tests
# Run php-react-promise-timer-get-source.sh to create full source
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with tests}
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
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-composer(react/event-loop) >= %{react_event_loop_min_ver} with php-composer(react/event-loop) < %{react_event_loop_max_ver})
BuildRequires: (php-composer(react/promise) >= %{react_promise_min_ver} with php-composer(react/promise) < %{react_promise_max_ver})
%else
BuildRequires: php-react-event-loop <  %{react_event_loop_max_ver}
BuildRequires: php-react-event-loop >= %{react_event_loop_min_ver}
BuildRequires: php-react-promise <  %{react_promise_max_ver}
BuildRequires: php-react-promise >= %{react_promise_min_ver}
%endif
## phpcompatinfo (computed from version 1.6.0)
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:      (php-composer(react/event-loop) >= %{react_event_loop_min_ver} with php-composer(react/event-loop) < %{react_event_loop_max_ver})
Requires:      (php-composer(react/promise) >= %{react_promise_min_ver} with php-composer(react/promise) < %{react_promise_max_ver})
%else
Requires:      php-react-event-loop <  %{react_event_loop_max_ver}
Requires:      php-react-event-loop >= %{react_event_loop_min_ver}
Requires:      php-react-promise <  %{react_promise_max_ver}
Requires:      php-react-promise >= %{react_promise_min_ver}
%endif
# phpcompatinfo (computed from version 1.6.0)
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
%{summary}.

Autoloader: %{phpdir}/React/Promise/Timer/autoload.php


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

\Fedora\Autoloader\Autoload::addPsr4('React\\Promise\\Timer\\', __DIR__);

\Fedora\Autoloader\Dependencies::required(array(
    __DIR__.'/functions_include.php',
    '%{phpdir}/React/EventLoop/autoload.php',
    '%{phpdir}/React/Promise/autoload.php',
));
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/React/Promise
cp -rp src %{buildroot}%{phpdir}/React/Promise/Timer


%check
%if %{with tests}
: Create tests bootstrap
mkdir vendor
cat <<'BOOTSTRAP' | tee vendor/autoload.php
<?php
require '%{buildroot}%{phpdir}/React/Promise/Timer/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('React\\Tests\\Promise\\Timer\\', dirname(__DIR__).'/tests');
BOOTSTRAP

: Upstream tests
RETURN_CODE=0
for CMDARG in "php %{phpunit}" php74 php80 php81 php82; do
    if which $CMDARG; then
    set $CMDARG
        $1 ${2:-%{_bindir}/phpunit9} --verbose \
            || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif


%files
%license LICENSE
%doc *.md
%doc composer.json
%{phpdir}/React/Promise/Timer


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Remi Collet <remi@remirepo.net> - 1.9.0-1
- update to 1.9.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec  7 2021 Remi Collet <remi@remirepo.net> - 1.8.0-1
- update to 1.8.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 12 2021 Remi Collet <remi@remirepo.net> - 1.7.0-1
- update to 1.7.0
- raise dependency on react/event-loop 1.2

* Wed Mar 24 2021 Remi Collet <remi@remirepo.net> - 1.6.0-1
- update to 1.6.0
- switch to phpunit9

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 2019 Shawn Iwinski <shawn@iwin.ski> - 1.5.1-1
- Update to 1.5.1 (RHBZ #1693418)
- Use PHPUnit 6

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 01 2018 Shawn Iwinski <shawn@iwin.ski> - 1.5.0-1
- Update to 1.5.0 (RHBZ #1480034)
- Add range version dependencies for Fedora >= 27 || RHEL >= 8
- Add composer.json to repo

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 24 2017 Shawn Iwinski <shawn@iwin.ski> - 1.1.1-2
- Retrict react/promise dependency to one major version
- Minor update to SCL tests (only php54 and php55 if rhel)

* Tue Jan 17 2017 Shawn Iwinski <shawn@iwin.ski> - 1.1.1-1
- Initial package
