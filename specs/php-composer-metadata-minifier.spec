# remirepo/fedora spec file for php-composer-metadata-minifier
#
# Copyright (c) 2021 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%bcond_without       tests

%global gh_commit    c549d23829536f0d0e984aaabbf02af91f443207
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
#global gh_date      20150717
%global gh_owner     composer
%global gh_project   metadata-minifier
%global php_home     %{_datadir}/php
%global ns_vendor    Composer
%global ns_project   MetadataMinifier

Name:           php-%{gh_owner}-%{gh_project}
Version:        1.0.0
Release:        10%{?gh_date:.%{gh_date}git%{gh_short}}%{?dist}
Summary:        Library that handles metadata minification and expansion

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
# git snapshot to get upstream test suite
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
%if %{with tests}
# For tests
BuildRequires:  php(language) >= 5.3.2
# From composer.json, "require-dev": {
#        "symfony/phpunit-bridge": "^4.2 || ^5",
#        "phpstan/phpstan": "^0.12.55",
#        "composer/composer": "^2"
BuildRequires: composer >= 2
%global phpunit %{_bindir}/phpunit9
BuildRequires: phpunit9
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, "require": {
#        "php": "^5.3.2 || ^7.0 || ^8.0",
Requires:       php(language) >= 5.3.2
# From phpcompatinfo report for version 1.0
# nothing
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{gh_owner}/%{gh_project}) = %{version}


%description
Small utility library that handles metadata minification and expansion.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}/autoload.php \

%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
: Generate classmap autoloader
phpab -t fedora -o src/autoload.php src


%install
: Library
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}


%check
%if %{with tests}
mkdir vendor
# Composer autoloader (single build dependency)
ln -s  %{php_home}/%{ns_vendor}/autoload.php vendor/autoload.php

# use auto_prepend_file as in composer autoloader
ret=0
for cmd in "php %{phpunit}" php73 php74 php80; do
  if which $cmd; then
    set $cmd
    $1 -d memory_limit=1G \
       -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}/autoload.php \
      ${2:-%{_bindir}/phpunit9} \
        --no-coverage \
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
     %{php_home}/%{ns_vendor}/%{ns_project}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Apr 27 2021 Remi Collet <remi@remirepo.net> - 1.0.0-1
- initial package, version 1.0.0
