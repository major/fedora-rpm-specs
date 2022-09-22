#
# Fedora spec file for php-ringcentral-psr7
#
# Copyright (c) 2018-2021 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     ringcentral
%global github_name      psr7
%global github_version   1.3.0
%global github_commit    360faaec4b563958b673fb52bbe94e37f14bc686

%global composer_vendor  ringcentral
%global composer_project psr7

# "php": ">=5.3"
%global php_min_ver 5.3
# "psr/http-message": "~1.0"
%global psr_http_message_min_ver 1.0
%global psr_http_message_max_ver 2.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       4%{?github_release}%{?dist}
Summary:       PSR-7 message implementation

Group:         Development/Libraries
License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

# For PHP 8
Patch0:        %{name}-php8.patch

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-composer(psr/http-message) >= %{psr_http_message_min_ver} with php-composer(psr/http-message) < %{psr_http_message_max_ver})
%else
BuildRequires: php-composer(psr/http-message) <  %{psr_http_message_max_ver}
BuildRequires: php-composer(psr/http-message) >= %{psr_http_message_min_ver}
%endif
## phpcompatinfo for version 1.2.2
BuildRequires: php-hash
BuildRequires: php-pcre
BuildRequires: php-spl
BuildRequires: php-zlib
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:      (php-composer(psr/http-message) >= %{psr_http_message_min_ver} with php-composer(psr/http-message) < %{psr_http_message_max_ver})
%else
Requires:      php-composer(psr/http-message) <  %{psr_http_message_max_ver}
Requires:      php-composer(psr/http-message) >= %{psr_http_message_min_ver}
%endif
# phpcompatinfo for version 1.2.2
Requires:      php-hash
Requires:      php-pcre
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}
Provides:      php-composer(psr/http-message-implementation) = 1.0

%description
This repository contains a partial PSR-7 [1] message implementation, several
stream decorators, and some helpful functionality like query string parsing.
Currently missing ServerRequestInterface and UploadedFileInterface; a pull
request for these features is welcome.

Autoloader: %{phpdir}/RingCentral/Psr7/autoload.php

[1] http://www.php-fig.org/psr/psr-7/


%prep
%setup -qn %{github_name}-%{github_commit}
%patch0 -p1


%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('RingCentral\\Psr7\\', __DIR__);

\Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}/Psr/Http/Message/autoload.php',
    __DIR__.'/functions_include.php',
));
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/RingCentral
cp -rp src %{buildroot}%{phpdir}/RingCentral/Psr7


%check
%if %{with_tests}
: Create mock Composer autoloader for test bootstrap
mkdir vendor
ln -s %{buildroot}%{phpdir}/RingCentral/Psr7/autoload.php vendor/autoload.php

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in php %{?rhel:php54 php55 php56 php70 php71} php72 php73 php74 php80; do
    if [ "php" == "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose || RETURN_CODE=1
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
%dir %{phpdir}/RingCentral
     %{phpdir}/RingCentral/Psr7


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Nov  5 2020 Remi Collet <remi@remirepo.net> - 1.3.0-1
- update to 1.3.0
- add patch for PHP 8 from
  https://github.com/ringcentral/psr7/pull/8

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Apr 21 2018 Shawn Iwinski <shawn@iwin.ski> - 1.2.2-1
- Update to 1.2.2
- Add range version dependencies for Fedora >= 27 || RHEL >= 8

* Wed Jan 03 2018 Shawn Iwinski <shawn@iwin.ski> - 1.2.1-1
- Initial package
