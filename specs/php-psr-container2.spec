# remirepo/fedora spec file for php-psr-container2
#
# Copyright (c) 2017-2021 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%global gh_commit    c71ecc56dfe541dbd90c5360474fbc405f8d5963
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     php-fig
%global gh_project   container

%global major        2

%global pk_vendor    psr
%global pk_project   container

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:      php-%{pk_vendor}-%{pk_project}%{major}
Version:   2.0.2
Release:   9%{?dist}
Summary:   Common Container Interface version %{major}

License:   MIT
URL:       https://github.com/%{gh_owner}/%{gh_project}
Source0:   %{url}/archive/%{gh_commit}/%{name}-%{version}-%{gh_commit}.tar.gz

BuildArch: noarch
# For tests
BuildRequires: php(language) >= 7.4.0
BuildRequires: php-cli
BuildRequires: php-composer(fedora/autoloader)

# From composer.json,    "require": {
#        "php": ">=7.4.0"
Requires:  php(language) >= 7.4.0
# phpcompatinfo (computed from version 1.0.0)
#     <none>
# Autoloader
Requires:  php-composer(fedora/autoloader)

# Composer
Provides:  php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
This package holds all interfaces/classes/traits related to PSR-11.

Note that this is not a container implementation of its own. 

Autoloader: %{_datadir}/php/Psr/Container%{major}/autoload.php


%prep
%setup -qn %{gh_project}-%{gh_commit}

: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/* Autoloader for %{pk_vendor}/%{pk_project} and its dependencies */

require_once '%{_datadir}/php/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Psr\\Container\\', __DIR__);
AUTOLOAD


%build
# Empty build section, nothing to build


%install
mkdir -p   %{buildroot}%{_datadir}/php/Psr
cp -rp src %{buildroot}%{_datadir}/php/Psr/Container%{major}


%check
: Test autoloader
php -r '
require "%{buildroot}%{_datadir}/php/Psr/Container%{major}/autoload.php";
exit (interface_exists("Psr\\Container\\ContainerInterface") ? 0 : 1);
'


%files
%license LICENSE
%doc *.md
%doc composer.json
%dir %{_datadir}/php/Psr
     %{_datadir}/php/Psr/Container%{major}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov  8 2021 Remi Collet <remi@remirepo.net> - 2.0.2-1
- update to 2.0.2

* Mon Oct 25 2021 Remi Collet <remi@remirepo.net> - 2.0.1-1
- update to 2.0.1
- rename to php-psr-container2
- install in /usr/share/php/Psr/Container2

* Wed Apr 14 2021 Remi Collet <remi@remirepo.net> - 1.1.1-1
- update to 1.1.1
- raise dependency on PHP 7.2

* Mon Feb 27 2017 Remi Collet <remi@remirepo.net> - 1.0.0-1
- Initial package, version 1.0.0

