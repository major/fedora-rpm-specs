#
# Fedora spec file for php-react-stream
#
# Copyright (c) 2017-2021 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     reactphp
%global github_name      stream
%global github_version   1.2.0
%global github_commit    7a423506ee1903e89f1e08ec5f0ed430ff784ae9

%global composer_vendor  react
%global composer_project stream

# "php": ">=5.3.8"
%global php_min_ver 5.3.8
# "clue/stream-filter": "~1.2"
%global clue_stream_filter_min_ver 1.2
%global clue_stream_filter_max_ver 2.0
# "evenement/evenement": "^3.0 || ^2.0 || ^1.0"
%global evenement_min_ver 1.0
%global evenement_max_ver 4.0
# "react/event-loop": "^1.0 || ^0.5 || ^0.4 || ^0.3.5"
%global react_event_loop_min_ver 0.3.5
%global react_event_loop_max_ver 2.0

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
Summary:       Basic readable and writable stream interfaces that support piping

License:       MIT
URL:           https://reactphp.org/stream/

# GitHub export does not include tests
# Run php-react-stream-get-source.sh to create full source
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: phpunit7
%if %{with_range_dependencies}
BuildRequires: (php-composer(clue/stream-filter) >= %{clue_stream_filter_min_ver} with php-composer(clue/stream-filter) < %{clue_stream_filter_max_ver})
BuildRequires: (php-composer(evenement/evenement) >= %{evenement_min_ver} with php-composer(evenement/evenement) < %{evenement_max_ver})
BuildRequires: (php-composer(react/event-loop) >= %{react_event_loop_min_ver} with php-composer(react/event-loop) < %{react_event_loop_max_ver})
%else
BuildRequires: php-composer(clue/stream-filter) <  %{clue_stream_filter_max_ver}
BuildRequires: php-composer(clue/stream-filter) >= %{clue_stream_filter_min_ver}
BuildRequires: php-composer(evenement/evenement) <  %{evenement_max_ver}
BuildRequires: php-composer(evenement/evenement) >= %{evenement_min_ver}
BuildRequires: php-composer(react/event-loop) <  %{react_event_loop_max_ver}
BuildRequires: php-composer(react/event-loop) >= %{react_event_loop_min_ver}
%endif
# phpcompatinfo (computed from version 1.1.1)
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
%if %{with_range_dependencies}
Requires:      (php-composer(evenement/evenement) >= %{evenement_min_ver} with php-composer(evenement/evenement) < %{evenement_max_ver})
Requires:      (php-composer(react/event-loop) >= %{react_event_loop_min_ver} with php-composer(react/event-loop) < %{react_event_loop_max_ver})
%else
Requires:      php-composer(evenement/evenement) <  %{evenement_max_ver}
Requires:      php-composer(evenement/evenement) >= %{evenement_min_ver}
Requires:      php-composer(react/event-loop) <  %{react_event_loop_max_ver}
Requires:      php-composer(react/event-loop) >= %{react_event_loop_min_ver}
%endif
# phpcompatinfo (computed from version 1.1.1)
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
Basic readable and writable stream interfaces that support piping.

In order to make the event loop easier to use, this component introduces the
concept of streams. They are very similar to the streams found in PHP itself,
but have an interface more suited for async I/O.

Mainly it provides interfaces for readable and writable streams, plus a file
descriptor based implementation with an in-memory write buffer.

This component depends on événement, which is an implementation of the
EventEmitter.

Autoloader: %{phpdir}/React/Stream/autoload.php


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

\Fedora\Autoloader\Autoload::addPsr4('React\\Stream\\', __DIR__);

\Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}/Evenement/autoload.php',
    '%{phpdir}/React/EventLoop/autoload.php',
));
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/React
cp -rp src %{buildroot}%{phpdir}/React/Stream


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require '%{buildroot}%{phpdir}/React/Stream/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('React\\Tests\\Stream\\', __DIR__.'/tests');

\Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}/Clue/StreamFilter/autoload.php',
));
BOOTSTRAP

: Skip tests requiring network access
rm -f tests/FunctionalInternetTest.php

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
%{phpdir}/React/Stream


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 12 2021 Remi Collet <remi@remirepo.net> - 1.2.0-1
- update to 1.2.0

* Wed Apr  7 2021 Remi Collet <remi@remirepo.net> - 1.1.1-5
- fix FTBFS with PHP 8

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 06 2020 Shawn Iwinski <shawn@iwin.ski> - 1.1.1-1
- Update to 1.1.1 (RHBZ #1830919)
- Use PHPUnit 7

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 2019 Shawn Iwinski <shawn@iwin.ski> - 1.1.0-1
- Update to 1.1.0 (RHBZ #1600309)
- Use PHPUnit 6

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 01 2018 Shawn Iwinski <shawn@iwin.ski> - 0.7.7-1
- Update to 0.7.7 (RHBZ #1431349)
- Add range version dependencies for Fedora >= 27 || RHEL >= 8
- Add composer.json to repo

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 26 2017 Shawn Iwinski <shawn@iwin.ski> - 0.4.6-1
- Update to 0.4.6 (RHBZ #1416595)

* Tue Jan 24 2017 Shawn Iwinski <shawn@iwin.ski> - 0.4.5-2
- Retrict evenement/evenement dependency to one major version
- Minor update to SCL tests (only php54 and php55 if rhel)

* Tue Jan 17 2017 Shawn Iwinski <shawn@iwin.ski> - 0.4.5-1
- Initial package
