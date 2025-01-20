# remirepo/fedora spec file for php-justinrainbow-json-schema5
#
# Copyright (c) 2016-2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%if 0%{?fedora} >= 39 || 0%{?rhel} >= 10
# disable test suite until recent phpunit is supported
%bcond_with          tests
%else
%bcond_without       tests
%endif

%global gh_commit    feb2ca6dd1cebdaf1ed60a4c8de2e53ce11c4fd8
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     justinrainbow
%global gh_project   json-schema
%global php_home     %{_datadir}/php
%global major        5


# Some sample files, only used for tests
#        "json-schema/JSON-Schema-Test-Suite": "1.1.0",
%global ts_commit    f3d5aeb5ffbe9d9a5a0ceb761dc47c7c4c2efa68
%global ts_short     %(c=%{ts_commit}; echo ${c:0:7})
%global ts_owner     json-schema
%global ts_project   JSON-Schema-Test-Suite
%global ts_version   1.2.0

%global eolv1        0
%global eolv2        0

Name:           php-%{gh_owner}-%{gh_project}%{major}
Version:        5.3.0
Release:        3%{?dist}
Summary:        A library to validate a json schema
License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}

# git snapshot to get upstream test suite
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        https://github.com/%{ts_owner}/%{ts_project}/archive/%{ts_commit}/%{ts_project}-%{ts_version}-%{ts_short}.tar.gz
Source2:        %{name}-autoload.php
Source3:        %{name}-makesrc.sh

# Autoloader
Patch0:         %{name}-rpm.patch

BuildArch:      noarch
%if %{with tests}
# For tests
BuildRequires:  php(language) >= 7.1
BuildRequires:  php-curl
BuildRequires:  php-date
BuildRequires:  php-filter
BuildRequires:  php-json
BuildRequires:  php-mbstring
BuildRequires:  php-pcre
BuildRequires:  php-spl
# From composer.json, "require-dev": {
#        "json-schema/json-schema-test-suite": "1.2.0",
#        "friendsofphp/php-cs-fixer": "^2.1",
#        "phpunit/phpunit": "^4.8.35"
BuildRequires:  php-composer(phpunit/phpunit) >= 4.8.35
# Autoloader
BuildRequires:  php-composer(fedora/autoloader)
# For composer schema
BuildRequires:  composer
%endif

# From composer.json, "require": {
#        "php": ">=7.1"
Requires:       php(language) >= 7.1
# From phpcompatinfo report for version 4.0.1
Requires:       php-curl
Requires:       php-date
Requires:       php-filter
Requires:       php-json
Requires:       php-mbstring
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)
%if %{eolv1}
Obsoletes:      php-JsonSchema < 2
%endif
%if %{eolv2}
Obsoletes:      php-justinrainbow-json-schema < 3
%endif
Requires:       php-cli

Provides:       php-composer(%{gh_owner}/%{gh_project}) = %{version}


%description
A PHP Implementation for validating JSON Structures against a given Schema.

This package provides the library version %{major}.

See http://json-schema.org/

Autoloader: %{php_home}/JsonSchema%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit} -a 1

%patch -P0 -p1 -b .rpm
find src -name \*.rpm -delete -print

cp %{SOURCE2} src/JsonSchema/autoload.php

: Needed for the test suite - use composer default path, as easier
mkdir -p vendor/json-schema/JSON-Schema-Test-Suite
mv %{ts_project}-%{ts_commit}/tests \
   vendor/json-schema/JSON-Schema-Test-Suite/tests

: But without online tests
find vendor/json-schema/JSON-Schema-Test-Suite/tests \
   -name \*.json \
   -exec grep -q 'http://' {} \; \
   -exec rm {} \; \
   -print


%build
# Empty build section, most likely nothing required.


%install
: Library
mkdir -p              %{buildroot}%{php_home}
cp -pr src/JsonSchema %{buildroot}%{php_home}/JsonSchema%{major}

: Schemas
mkdir -p              %{buildroot}%{_datadir}/%{name}
cp -pr dist           %{buildroot}%{_datadir}/%{name}/dist

: Command
install -Dpm 0755 bin/validate-json %{buildroot}%{_bindir}/validate-json%{major}


%check
%if %{with tests}
: Test suite autoloader
cat << 'EOF' | tee vendor/autoload.php
<?php
require '%{buildroot}%{php_home}/JsonSchema%{major}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('JsonSchema\\Tests\\', 'tests/');
EOF

export BUILDROOT_SCHEMA=%{buildroot}

: Test the command
sed -e 's:%{php_home}:%{buildroot}%{php_home}:' \
    bin/validate-json > bin/validate-json-test
php bin/validate-json-test \
    composer.json \
    /usr/share/composer/res/composer-schema.json

: Upstream test suite
ret=0
for cmd in php php81 php82 php83; do
  if which $cmd; then
   $cmd -d memory_limit=1G %{_bindir}/phpunit -d memory_limit=1G --verbose || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif


%files
%license LICENSE
%doc composer.json
%doc *.md
%{_bindir}/validate-json%{major}
%{php_home}/JsonSchema%{major}
%{_datadir}/%{name}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul  8 2024 Remi Collet <remi@remirepo.net> - 5.3.0-1
- update to 5.3.0
- raise dependency on PHP 7.1

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Sep 28 2023 Remi Collet <remi@remirepo.net> - 5.2.13-1
- update to 5.2.13
- disable test suite

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Apr 13 2022 Remi Collet <remi@remirepo.net> - 5.2.12-1
- update to 5.2.12

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Remi Collet <remi@remirepo.net> - 5.2.11-1
- update to 5.2.11

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 28 2020 Remi Collet <remi@remirepo.net> - 5.2.10-1
- update to 5.2.10

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 26 2019 Remi Collet <remi@remirepo.net> - 5.2.9-1
- update to 5.2.9

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Remi Collet <remi@remirepo.net> - 5.2.8-1
- update to 5.2.8

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 15 2018 Remi Collet <remi@remirepo.net> - 5.2.7-1
- Update to 5.2.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 22 2017 Remi Collet <remi@remirepo.net> - 5.2.6-1
- Update to 5.2.6

* Wed Oct 11 2017 Remi Collet <remi@remirepo.net> - 5.2.5-1
- Update to 5.2.5

* Thu Oct  5 2017 Remi Collet <remi@remirepo.net> - 5.2.4-1
- Update to 5.2.4

* Tue Oct  3 2017 Remi Collet <remi@remirepo.net> - 5.2.2-1
- Update to 5.2.2

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 17 2017 Remi Collet <remi@remirepo.net> - 5.2.1-1
- Update to 5.2.1

* Thu Mar 23 2017 Remi Collet <remi@remirepo.net> - 5.2.0-1
- Update to 5.2.0

* Wed Feb 22 2017 Remi Collet <remi@fedoraproject.org> - 5.1.0-1
- update to 5.1.0

* Thu Feb 16 2017 Remi Collet <remi@fedoraproject.org> - 5.0.0-1
- rename to php-justinrainbow-json-schema5
- update to 5.0.0

* Thu Feb 16 2017 Remi Collet <remi@fedoraproject.org> - 4.1.0-2
- always provide the command as validate-json4

* Fri Dec 23 2016 Remi Collet <remi@fedoraproject.org> - 4.1.0-1
- update to 4.1.0
- drop patch merged upstream

* Mon Dec 12 2016 Remi Collet <remi@fedoraproject.org> - 4.0.1-1
- rename to php-justinrainbow-json-schema4
- update to 4.0.1

* Fri Oct 21 2016 Remi Collet <remi@fedoraproject.org> - 2.0.5-3
- switch from symfony/class-loader to fedora/autoloader

* Thu Jul 21 2016 Remi Collet <remi@fedoraproject.org> - 2.0.5-2
- fix failed test, FTBFS detected by Koschei
  open https://github.com/justinrainbow/json-schema/pull/292

* Thu Jun  2 2016 Remi Collet <remi@fedoraproject.org> - 2.0.5-1
- update to 2.0.5

* Wed Jun  1 2016 Remi Collet <remi@fedoraproject.org> - 2.0.4-2
- add the validate-json command, dropped from php-JsonSchema

* Wed May 25 2016 Remi Collet <remi@fedoraproject.org> - 2.0.4-1
- update to 2.0.4
- use json-schema/JSON-Schema-Test-Suite 1.2.0

* Wed May 11 2016 Remi Collet <remi@fedoraproject.org> - 2.0.3-1
- update to 2.0.3
- use json-schema/JSON-Schema-Test-Suite 1.1.2

* Fri Apr 29 2016 Remi Collet <remi@fedoraproject.org> - 2.0.1-1
- update to 2.0.1

* Fri Apr 15 2016 Remi Collet <remi@fedoraproject.org> - 2.0.0-1
- initial package, version 2.0.0

