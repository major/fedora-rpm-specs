#
# Fedora spec file for php-sentry
#
# Copyright (c) 2016-2020 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve the changelog entries
#

%global github_owner     getsentry
%global github_name      sentry-php
%global github_version   0.22.0
%global github_commit    49d4c0c4f2c298c9f15a07416debb5352a209b79

%global composer_vendor  sentry
%global composer_project sentry

# "php": ">=5.2.4"
%global php_min_ver      5.2.4
# "monolog/monolog": "*"
#     NOTE: Min version because autoloader required
#     NOTE: Adding max version to force v1
%global monolog_min_ver  1.15.0
%global monolog_max_ver  2

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

# Range dependencies supported?
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
%global with_range_dependencies 1
%else
%global with_range_dependencies 0
%endif

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_project}
Version:       %{github_version}
Release:       22%{?github_release}%{?dist}
Summary:       PHP client for Sentry

# ASL 2.0:
#     - lib/Raven/Serializer.php
# BSD:
#     - Everything else
# Automatically converted from old format: BSD and ASL 2.0 - review is highly recommended.
License:       LicenseRef-Callaway-BSD AND Apache-2.0
URL:           https://github.com/%{github_owner}/%{github_name}

# GitHub export does not include tests.
# Run php-sentry-get-source.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Library version value check
BuildRequires: php-cli
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
BuildRequires: php-curl
%if %{with_range_dependencies}
BuildRequires: (php-composer(monolog/monolog) >= %{monolog_min_ver} with php-composer(monolog/monolog) < %{monolog_max_ver})
%else
BuildRequires: php-composer(monolog/monolog) < %{monolog_max_ver}
BuildRequires: php-composer(monolog/monolog) >= %{monolog_min_ver}
%endif
## phpcompatinfo (computed from version 0.22.0)
BuildRequires: php-date
BuildRequires: php-hash
BuildRequires: php-mbstring
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-session
BuildRequires: php-spl
BuildRequires: php-zlib
# Conflict because Monolog will load obsoleted package's autoloader and classes.
BuildConflicts: php-Raven
%endif

Requires:      php-cli
Requires:      ca-certificates
# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      php-curl
%if %{with_range_dependencies}
Requires:      (php-composer(monolog/monolog) >= %{monolog_min_ver} with php-composer(monolog/monolog) < %{monolog_max_ver})
%else
Requires:      php-composer(monolog/monolog) < %{monolog_max_ver}
Requires:      php-composer(monolog/monolog) >= %{monolog_min_ver}
%endif
# phpcompatinfo (computed from version 0.22.0)
Requires:      php-date
Requires:      php-hash
Requires:      php-mbstring
Requires:      php-pcre
Requires:      php-reflection
Requires:      php-session
Requires:      php-spl
Requires:      php-zlib

# Standard "php-{COMPOSER_VENDOR}-{COMPOSER_PROJECT}" naming
Provides:      php-%{composer_vendor}-%{composer_project} = %{version}-%{release}
# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

# Rename
Obsoletes:     php-Raven < %{version}
Provides:      php-Raven = %{version}-%{release}
Provides:      php-composer(raven/raven) = %{version}


%description
%{summary} (http://getsentry.com).

Autoloader: %{phpdir}/Raven/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}

: Remove bundled cert
rm -rf lib/Raven/data
sed "/return.*cacert\.pem/s#.*#        return '%{_sysconfdir}/pki/tls/cert.pem';#" \
    -i lib/Raven/Client.php

: Update autoloader require in bin
sed "/require.*Autoloader/s#.*#require_once '%{phpdir}/Raven/Autoloader.php';#" \
    -i bin/sentry


%build
: Create autoloader
cat <<'AUTOLOAD' | tee lib/Raven/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */

require_once dirname(__FILE__).'/Autoloader.php';
Raven_Autoloader::register();

// Required dependency
require_once '%{phpdir}/Monolog/autoload.php';
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}
cp -rp lib/* %{buildroot}%{phpdir}/

mkdir -p %{buildroot}%{_bindir}
install -pm 0755 bin/sentry %{buildroot}%{_bindir}/
: Compat bin
ln -s sentry %{buildroot}%{_bindir}/raven


%check
: Library version value check
%{_bindir}/php -r '
    require_once "%{buildroot}%{phpdir}/Raven/Client.php";
    $version = Raven_Client::VERSION;
    echo "Version $version (expected %{version})\n";
    exit(version_compare("%{version}", "$version", "=") ? 0 : 1);
'

%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
session_start();
require_once '%{buildroot}%{phpdir}/Raven/autoload.php';
BOOTSTRAP

: Run tests
ret=0
for cmd in php php70 php71 php72 php73; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit \
      --filter '^((?!(testCanTraceParamContext|testDoesFixFrameInfo)).)*$' \
      --verbose --bootstrap bootstrap.php || ret=1
  fi
done
exit $ret
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.rst
%doc AUTHORS
%doc CHANGES
%doc composer.json
%{phpdir}/Raven
%{_bindir}/raven
%{_bindir}/sentry


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.22.0-21
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 04 2020 Shawn Iwinski <shawn@iwin.ski> - 0.22.0-11
- Add max Monolog version

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec  6 2018 Remi Collet <remi@remirepo.net> - 0.22.0-6
- skip test relying on uopz extension

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Nov 03 2016 Shawn Iwinski <shawn@iwin.ski> - 0.22.0-1
- Initial package
