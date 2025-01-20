# remirepo/fedora spec file for php-composer-pcre
#
# Copyright (c) 2021-2022 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_without       tests

%global gh_commit    67a32d7d6f9f560b726ab25a061b38ff3a80c560
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
#global gh_date      20150717
%global gh_owner     composer
%global gh_project   pcre
%global ns_vendor    Composer
%global ns_project   Pcre
%global php_home     %{_datadir}/php
%global major        %nil

Name:           php-%{gh_owner}-%{gh_project}%{major}
Version:        1.0.1
Release:        8%{?gh_date:.%{gh_date}git%{gh_short}}%{?dist}
Summary:        PCRE wrapping library version 1

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
# git snapshot to get upstream test suite
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
%if %{with tests}
# For tests
BuildRequires:  php(language) >= 5.3.2
BuildRequires:  php-pcre
BuildRequires:  php-spl
# From composer.json,     "require-dev": {
#        "symfony/phpunit-bridge": "^4.2 || ^5",
#        "phpstan/phpstan": "^1.3",
#        "phpstan/phpstan-strict-rules": "^1.1"
%global         phpunit /usr/bin/phpunit9
BuildRequires:  %{phpunit}
# Autoloader
BuildRequires:  php-fedora-autoloader-devel
%endif

# From composer.json, "require": {
#       "php": "^5.3.2 || ^7.0 || ^8.0"
Requires:       php(language) >= 5.3.2
# From phpcompatinfo report for version 1.0.0
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{gh_owner}/%{gh_project}) = %{version}


%description
PCRE wrapping library that offers type-safe preg_* replacements.

This library gives you a way to ensure preg_* functions do not fail silently,
returning unexpected nulls that may not be handled.

It also makes it easier ot work with static analysis tools like PHPStan or
Psalm as it simplifies and reduces the possible return values from all the
preg_* functions which are quite packed with edge cases.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
: Generate classmap autoloader
phpab --template fedora --output src/autoload.php src


%install
: Library
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}/
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}


%check
%if %{with tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once "%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php";
\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\%{ns_project}', dirname(__DIR__).'/tests');
EOF

ret=0
for cmd in php php74 php80 php81; do
  if which $cmd; then
    $cmd %{phpunit} \
      --verbose || ret=1
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
%dir %{php_home}/%{ns_vendor}
     %{php_home}/%{ns_vendor}/%{ns_project}%{major}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Remi Collet <remi@remirepo.net> - 1.0.1-1
- update to 1.0.1

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec  8 2021 Remi Collet <remi@remirepo.net> - 1.0.0-1
- initial package, version 1.0.0
