#
# Fedora spec file for php-react-event-loop
#
# Copyright (c) 2017-2022 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     reactphp
%global github_name      event-loop
%global github_version   1.3.0
%global github_commit    187fb56f46d424afb6ec4ad089269c72eec2e137

%global composer_vendor  react
%global composer_project event-loop

# "php": ">=5.4.0"
%global php_min_ver 5.4.0

# Build using "--without tests" to disable tests
%bcond_without tests

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       2%{?github_release}%{?dist}
Summary:       Event loop abstraction layer that libraries can use for evented I/O

License:       MIT
URL:           https://reactphp.org/event-loop/

# GitHub export does not include tests
# Run php-react-event-loop-get-source.sh to create full source
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: phpunit9
## phpcompatinfo (computed from version 1.1.0)
BuildRequires: php-date
BuildRequires: php-pcntl
BuildRequires: php-posix
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 1.1.0)
Requires:      php-pcntl
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
Event loop abstraction layer that libraries can use for evented I/O.

In order for async based libraries to be interoperable, they need to use
the same event loop. This component provides a common LoopInterface that
any library can target. This allows them to be used in the same loop, with
one single run call that is controlled by the user.

In addition to the interface there are some implementations provided:
* StreamSelectLoop: This is the only implementation which works out of the box
      with PHP. It does a simple select system call. It's not the most
      performant of loops, but still does the job quite well.
* LibEventLoop: This uses the libevent pecl extension. libevent itself supports
      a number of system-specific backends (epoll, kqueue).
* LibEvLoop: This uses the libev pecl extension (github). It supports the same
      backends as libevent.
* ExtEventLoop: This uses the event pecl extension. It supports the same
      backends as libevent.

All of the loops support these features:
* File descriptor polling
* One-off timers
* Periodic timers
* Deferred execution of callbacks

Autoloader: %{phpdir}/React/EventLoop/autoload.php


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

\Fedora\Autoloader\Autoload::addPsr4('React\\EventLoop\\', __DIR__);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/React
cp -rp src %{buildroot}%{phpdir}/React/EventLoop

find %{buildroot}%{phpdir}/React/EventLoop | sed 's#%{buildroot}##' | sort


%check
%if %{with tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require '%{buildroot}%{phpdir}/React/EventLoop/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('React\\Tests\\EventLoop\\', __DIR__.'/tests');
BOOTSTRAP

: Fix autoloader path
sed -e '/autoload.php/s:^.*$:require "%{buildroot}%{phpdir}/React/EventLoop/autoload.php";:' -i tests/bin/*.php

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit9)
for PHP_EXEC in "" php74 php80 php81; do
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
%license LICENSE
%doc *.md
%doc composer.json
%dir %{phpdir}/React
     %{phpdir}/React/EventLoop


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Mar 17 2022 Remi Collet <remi@remirepo.net> - 1.3.0-1
- update to 1.3.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 12 2021 Remi Collet <remi@remirepo.net> - 1.2.0-1
- update to 1.2.0

* Wed Mar 24 2021 Remi Collet <remi@remirepo.net> - 1.1.1-1
- update to 1.1.1
- switch to phpunit9

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 2019 Shawn Iwinski <shawn@iwin.ski> - 1.1.0-1
- Update to 1.1.0 (RHBZ #1599719)
- Use PHPUnit 7

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 01 2018 Shawn Iwinski <shawn@iwin.ski> - 0.5.2-1
- Update to 0.5.2 (RHBZ #1564315)
- Add range version dependencies for Fedora >= 27 || RHEL >= 8
- Add composer.json to repo

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Apr 29 2017 Shawn Iwinski <shawn@iwin.ski> - 0.4.3-1
- Update to 0.4.3 (RHBZ #1446188)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Shawn Iwinski <shawn@iwin.ski> - 0.4.2-2
- Minor update to SCL tests (only php55 if rhel)

* Tue Jan 17 2017 Shawn Iwinski <shawn@iwin.ski> - 0.4.2-1
- Initial package
