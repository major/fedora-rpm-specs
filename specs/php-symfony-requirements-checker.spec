# remirepo/fedora spec file for php-symfony-requirements-checker
#
# Copyright (c) 2020-2021 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    cf8893f384348a338157d637e170fe8fb2356016
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     symfony
%global gh_project   requirements-checker
# Packagist
%global pk_vendor    %{gh_owner}
%global pk_project   %{gh_project}
# Namespace
%global ns_vendor    Symfony
%global ns_project   Requirements
%global php_home     %{_datadir}/php

Name:           php-%{pk_vendor}-%{pk_project}
Version:        2.0.1
Release:        9%{?gh_date:.%{gh_date}git%{gh_short}}%{?dist}
Summary:        Check Symfony requirements and give recommendations

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{?gh_short}.tar.gz

# Use our autoloader
Patch0:         %{name}-bin.patch

BuildArch:      noarch

BuildRequires:  php(language) >= 5.3.9
BuildRequires:  php-reflection
BuildRequires:  php-ctype
BuildRequires:  php-date
BuildRequires:  php-dom
BuildRequires:  php-iconv
BuildRequires:  php-intl
BuildRequires:  php-json
BuildRequires:  php-pcre
BuildRequires:  php-spl
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, "require": {
#        "php": ">=5.3.9"
Requires:       php(language) >= 5.3.9
# From phpcompatinfo report for version 2.0.0
Requires:       php-reflection
Requires:       php-ctype
Requires:       php-date
Requires:       php-dom
Requires:       php-iconv
Requires:       php-intl
Requires:       php-json
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project})   = %{version}


%description
Checks requirements for running Symfony and gives useful recommendations
to optimize PHP for Symfony.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}
%patch -P0 -p1 -b .rpm


%build
: Create autoloader
phpab --template fedora --output src/autoload.php src


%install
mkdir -p    %{buildroot}%{php_home}/%{ns_vendor}/
cp -pr src  %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}

install -Dpm 755 bin/requirements-checker.php %{buildroot}%{_bindir}/%{name}


%check
: Check autoloader
php -r '
require "%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}/autoload.php";
exit(class_exists("Symfony\\Requirements\\Requirement") ? 0 : 1);
'


%files
%license LICENSE
%doc *composer.json
%doc *.rst
%{_bindir}/%{name}
%dir %{php_home}/%{ns_vendor}/
     %{php_home}/%{ns_vendor}/%{ns_project}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec  1 2021 Remi Collet <remi@remirepo.net> - 2.0.1-1
- update to 2.0.1

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Oct 12 2020 Remi Collet <remi@remirepo.net> - 2.0.0-1
- initial package
