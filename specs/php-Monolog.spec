#
# Fedora spec file for php-Monolog
#
# Copyright (c) 2012-2022 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     Seldaek
%global github_name      monolog
%global github_version   1.27.1
%global github_commit    904713c5929655dc9b97288b69cfeedad610c9a1

%global composer_vendor  monolog
%global composer_project monolog

# "php": ">=5.3.0"
%global php_min_ver 5.3.0
# "psr/log": "~1.0"
#     NOTE: Min version not 1.0 because autoloader required
%global psrlog_min_ver 1.0.1
%global psrlog_max_ver 2.0
# "sentry/sentry": "^0.13"
%global sentry_min_ver 0.13
%global sentry_max_ver 1.0
# "aws/aws-sdk-php": "^2.4.9 || ^3.0"
#     NOTE: Min version not 2.4.9 because autoloader required
%global aws_min_ver 2.8.13
%global aws_max_ver 4.0
# "swiftmailer/swiftmailer": "~5.3"
%global swift_min_ver 5.3
%global swift_max_ver 6

# Build using "--with tests" to disable tests
%bcond_with tests

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:      php-Monolog
Version:   %{github_version}
Release:   8%{?dist}
Summary:   Sends your logs to files, sockets, inboxes, databases and various web services

License:   MIT
URL:       https://github.com/%{github_owner}/%{github_name}
Source0:   %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

# Fix tests for sentry/sentry >= 0.16.0 (and < 1.0)
#
# Patch adapted for Monolog version 1.21.0 from
#     https://github.com/Seldaek/monolog/pull/880
Patch0:    %{name}-tests-sentry-gte-0-16-0.patch

BuildArch:     noarch
# Tests
%if %{with tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
BuildRequires: php-composer(psr/log) >= %{psrlog_min_ver}
BuildRequires: php-composer(psr/log) <  %{psrlog_max_ver}
## optional
BuildRequires: php-composer(swiftmailer/swiftmailer) >= %{swift_min_ver}
BuildRequires: php-composer(swiftmailer/swiftmailer) <  %{swift_max_ver}
BuildRequires: php-composer(sentry/sentry) >= %{sentry_min_ver}
BuildRequires: php-composer(sentry/sentry) <  %{sentry_max_ver}
BuildRequires: php-composer(aws/aws-sdk-php) >= %{aws_min_ver}
BuildRequires: php-composer(aws/aws-sdk-php) <  %{aws_max_ver}
## phpcompatinfo (computed from version 1.22.0)
BuildRequires: php-curl
BuildRequires: php-date
BuildRequires: php-filter
BuildRequires: php-hash
BuildRequires: php-json
BuildRequires: php-mbstring
BuildRequires: php-openssl
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-sockets
BuildRequires: php-spl
BuildRequires: php-xml
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      php-composer(psr/log) >= %{psrlog_min_ver}
Requires:      php-composer(psr/log) <  %{psrlog_max_ver}
# phpcompatinfo (computed from version 1.22.0)
Requires:      php-curl
Requires:      php-date
Requires:      php-filter
Requires:      php-hash
Requires:      php-json
Requires:      php-mbstring
Requires:      php-openssl
Requires:      php-pcre
Requires:      php-sockets
Requires:      php-spl
Requires:      php-xml
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Standard "php-{COMPOSER_VENDOR}-{COMPOSER_PROJECT}" naming
Provides:      php-%{composer_vendor}-%{composer_project} = %{version}-%{release}
Provides:      php-%{composer_project} = %{version}-%{release}
# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}
Provides:      php-composer(psr/log-implementation) = 1.0.0

# Removed sub-packages
Obsoletes:     %{name}-amqp   < %{version}-%{release}
Provides:      %{name}-amqp   = %{version}-%{release}
Obsoletes:     %{name}-dynamo < %{version}-%{release}
Provides:      %{name}-dynamo = %{version}-%{release}
Obsoletes:     %{name}-mongo  < %{version}-%{release}
Provides:      %{name}-mongo  = %{version}-%{release}
Obsoletes:     %{name}-raven  < %{version}-%{release}
Provides:      %{name}-raven  = %{version}-%{release}

# Weak dependencies
%if 0%{?fedora} >= 21 || 0%{?rhel} >= 8
Suggests:      php-composer(aws/aws-sdk-php)
Suggests:      php-composer(sentry/sentry)
Suggests:      php-composer(swiftmailer/swiftmailer)
Suggests:      php-pecl(amqp)
Suggests:      php-pecl(mongo)
%endif

%description
Monolog sends your logs to files, sockets, inboxes, databases and various web
services. Special handlers allow you to build advanced logging strategies.

This library implements the PSR-3 [1] interface that you can type-hint against
in your own libraries to keep a maximum of interoperability. You can also use it
in your applications to make sure you can always use another compatible logger
at a later time.

[1] http://www.php-fig.org/psr/psr-3/


%prep
%setup -qn %{github_name}-%{github_commit}

: Fix tests for sentry/sentry >= 0.16.0
%patch -P0 -p1


%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/Monolog/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Monolog\\', __DIR__);

\Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}/Psr/Log/autoload.php',
));

\Fedora\Autoloader\Dependencies::optional(array(
    array(
        '%{phpdir}/Aws3/autoload.php',
        '%{phpdir}/Aws/autoload.php',
    ),
    '%{phpdir}/Raven/autoload.php',
    '%{phpdir}/Swift/swift_required.php',
));
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}
cp -pr src/Monolog %{buildroot}%{phpdir}/


%check
%if %{with tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require_once '%{buildroot}%{phpdir}/Monolog/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Monolog\\', __DIR__ . '/tests/Monolog');
BOOTSTRAP

: Remove MongoDBHandlerTest because it requires a running MongoDB server
rm -f tests/Monolog/Handler/MongoDBHandlerTest.php

: Remove GitProcessorTest because it requires a git repo
rm -f tests/Monolog/Processor/GitProcessorTest.php

: Mocking issues
rm -f tests/Monolog/Handler/SocketHandlerTest.php

: Trying to access array offset on value of type null in Raven lib
rm -f tests/Monolog/Handler/RavenHandlerTest.php

: Skip tests known to fail
%if 0%{?rhel} == 6 || 0%{?rhel} == 7
sed 's/function testThrowsOnInvalidEncoding/function SKIP_testThrowsOnInvalidEncoding/' \
    -i tests/Monolog/Formatter/NormalizerFormatterTest.php
%endif

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in "" %{?rhel:php54 php55 php56 php70 php71} php72 php73 php74; do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose --bootstrap bootstrap.php || RETURN_CODE=1
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
%doc doc
%doc composer.json
%{phpdir}/Monolog


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.27.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.27.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.27.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.27.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.27.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.27.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.27.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun  9 2022 Remi Collet <remi@remirepo.net> - 1.27.1-1
- update to 1.27.1

* Mon Mar 14 2022 Remi Collet <remi@remirepo.net> - 1.27.0-1
- update to 1.27.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Sep 20 2021 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.26.1-3
- Fix "FTBFS in Fedora rawhide/f35" (RHBZ #1987804)
- Disable tests by default... REALLY need to get v2 available and dependants
  updated to use v2 instead of this very old verion (i.e. v1)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 31 2021 Remi Collet <remi@remirepo.net> - 1.26.1-1
- update to 1.26.1

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan  6 2021 Remi Collet <remi@remirepo.net> - 1.26.0-1
- update to 1.26.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.25.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 2020 Remi Collet <remi@remirepo.net> - 1.25.5-1
- update to 1.25.5

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.25.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 14 2019 Remi Collet <remi@remirepo.net> - 1.25.2-1
- update to 1.25.2

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.23.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.23.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.23.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.23.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.23.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 09 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.23.0-1
- Update to 1.23.0 (RHBZ #1432274)
- Test with SCLs if available

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Nov 26 2016 Remi Collet <remi@fedoraproject.org> - 1.22.0-1
- update to 1.22.0
- switch from symfony/class-loader to fedora/autoloader
- allow aws/aws-sdk-php version 3
- fix FTBFS with PHP 7.1

* Sun Nov 06 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.21.0-2
- Fix test suite for php-sentry >= 0.16.0
- Modified php-psr-log dependency (min version 1.0.0-8 => 1.0.1)

* Mon Aug 08 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.21.0-1
- Updated to 1.21.0 (RHBZ #1362318)

* Mon Jul 04 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.20.0-1
- Updated to 1.20.0 (RHBZ #1352494)
- Updated autoloader to not use "@include_once"

* Mon Apr 04 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.18.2-1
- Updated to 1.18.2 (RHBZ #1313579)
- Removed patch (accepted upstream and applied to this version)
- Added additional weak dependencies (AMQP and MongoDB)

* Fri Apr 01 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.18.1-2
- Increased PSR log min version for autoloader
- Updated autoloader
- Added weak dependencies

* Fri Mar 25 2016 Remi Collet <remi@remirepo.net> - 1.18.1-1
- update to 1.18.1
- use php-swiftmailer instead of old php-swift-Swift
- install optional dependencies during the build for tests
- add patch for missing property, breaking test suite
  open https://github.com/Seldaek/monolog/pull/757

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 15 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.17.2-1
- Updated to 1.17.2 (RHBZ #1271882)

* Sun Sep 13 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.17.1-1
- Updated to 1.17.1 (RHBZ #1258230)

* Tue Aug 11 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.16.0-1
- Updated to 1.16.0 (RHBZ #1251783)
- Updated autoloader to load dependencies after self registration

* Mon Jul 20 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.15.0-2
- Fix autoloader

* Sun Jul 19 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.15.0-1
- Updated to 1.15.0 (RHBZ #1199105)
- Added autoloader

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jan 04 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.12.0-1
- Updated to 1.12.0 (BZ #1178410)

* Sat Jun 07 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.11.0-1
- Updated to 1.11.0 (BZ #1148336)
- Added php-composer(psr/log-implementation) virtual provide
- %%license usage

* Sat Jun 07 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.10.0-1
- Updated to 1.10.0 (BZ #1105816)
- Removed max PHPUnit dependency
- Added php-composer(monolog/monolog) virtual provide

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 25 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.9.1-1
- Updated to 1.9.1 (BZ #1080872)
- Added option to build without tests ("--without tests")

* Thu Jan 16 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.7.0-3
- Properly obsolete sub-packages

* Wed Jan 15 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.7.0-2
- Removed sub-packages (optional dependencies note in description instead)

* Mon Dec 30 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.7.0-1
- Updated to 1.7.0 (BZ #1030923)
- Added dynamo sub-package
- Spec cleanup

* Sat Aug 17 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.6.0-1
- Updated to version 1.6.0 (BZ #956013)
- Added phpcompatinfo build requires
- php-common -> php(language)
- No conditional php-filter require
- Added php-hash require
- Global raven min and max versions
- Removed MongoDBHandlerTest because it requires a running MongoDB server

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 01 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.4.1-1
- Updated to version 1.4.1 (BZ #893708)
- Updates for "new" Fedora GitHub guidelines
- Updated summary and description
- Added php-PsrLog require
- Added tests (%%check)
- Removed tests sub-package
- Added raven sub-package

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Nov 17 2012 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.1-1
- Updated to upstream version 1.2.1
- Changed %%{lib_name} from monolog to Monolog
- Fixed license
- GitHub archive source
- Added php-pear(pear.swiftmailer.org/Swift), php-curl, and php-sockets requires
- Added optional packages note in %%{description}
- Simplified %%prep
- Added subpackages for AMQP and MongoDB handlers
- Changed RPM_BUILD_ROOT to %%{buildroot}

* Sun Jul 22 2012 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1.0-1
- Initial package
