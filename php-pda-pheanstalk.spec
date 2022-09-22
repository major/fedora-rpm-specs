#
# Fedora spec file for php-pda-pheanstalk
#
# Copyright (c) 2017-2019 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     pda
%global github_name      pheanstalk
%global github_version   4.0.0
%global github_commit    328708b2cb843c214579a9ac3d1730c074038d6a

%global composer_vendor  pda
%global composer_project pheanstalk

# "php": ">=7.1.0"
%global php_min_ver 7.1.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       8%{?github_release}%{?dist}
Summary:       PHP client for beanstalkd queue

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}

# GitHub export does not include tests.
# Run php-pda-pheanstalk-get-source.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
BuildRequires: php-mbstring
## phpcompatinfo (computed from version 4.0.0)
BuildRequires: php-pcre
BuildRequires: php-sockets
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      php-mbstring
# phpcompatinfo (computed from version 4.0.0)
Requires:      php-pcre
Requires:      php-sockets
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
Pheanstalk is a pure PHP 5.3+ client for the beanstalkd workqueue [1]. It has
been actively developed, and used in production by many, since late 2008.

Created by Paul Annesley [2], Pheanstalk is rigorously unit tested and written
using encapsulated, maintainable object oriented design. Community feedback,
bug reports and patches has led to a stable 1.0 release in 2010, a 2.0 release
in 2013, and a 3.0 release in 2014.

Pheanstalk 3.0 introduces PHP namespaces, PSR-1 and PSR-2 coding standards, and
PSR-4 autoloader standard.

beanstalkd up to the latest version 1.4 is supported. All commands and responses
specified in the protocol documentation for beanstalkd 1.3 are implemented.

Autoloader: %{phpdir}/Pheanstalk/autoload.php

[1] http://xph.us/software/beanstalkd/
[2] http://paul.annesley.cc/


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

\Fedora\Autoloader\Autoload::addPsr4('Pheanstalk\\', __DIR__);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}
cp -rp src %{buildroot}%{phpdir}/Pheanstalk


%check
%if %{with_tests}
: Remove tests requiring a running beanstalkd service
rm -f \
    tests/Pheanstalk/BugfixConnectionTest.php \
    tests/Pheanstalk/ConnectionTest.php \
    tests/Pheanstalk/PheanstalkTest.php \
    tests/Pheanstalk/SocketFactoryTest.php

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in php php72 php73 php74; do
    if [ "php" == "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose \
            --bootstrap %{buildroot}%{phpdir}/Pheanstalk/autoload.php \
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
%{phpdir}/Pheanstalk


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 16 2019 Shawn Iwinski <shawn@iwin.ski> - 4.0.0-1
- Update to 4.0.0 (RHBZ #1653281)

* Mon Jun 03 2019 Shawn Iwinski <shawn@iwin.ski> - 3.2.1-1
- Update to 3.2.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Oct 21 2017 Shawn Iwinski <shawn@iwin.ski> - 3.1.0-1
- Initial package
