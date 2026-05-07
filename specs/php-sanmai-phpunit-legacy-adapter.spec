# remirepo/fedora spec file for php-sanmai-phpunit-legacy-adapter
#
# SPDX-FileCopyrightText:  Copyright 2020-2026 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

%bcond_without       tests

%global gh_owner     sanmai
%global gh_project   phpunit-legacy-adapter
%global ns_project   LegacyPHPUnit
%global tag          %{version}
%global forgeurl     https://github.com/%{gh_owner}/%{gh_project}

Name:           php-%{gh_owner}-%{gh_project}
Summary:        PHPUnit Legacy Versions Adapter
License:        Apache-2.0
Version:        8.2.3
Release:        1%{?dist}
%forgemeta
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildArch:      noarch
%if %{with tests}
BuildRequires:  phpunit8  >= 8.5.29
BuildRequires:  phpunit9  >= 9.5.24
BuildRequires:  phpunit10 >= 10.1.2
BuildRequires:  phpunit11 >= 11.5.55
BuildRequires:  phpunit12 >= 12.5.24
BuildRequires:  phpunit13 >= 13.1.8
%endif
BuildRequires:  php-fedora-autoloader-devel

Requires:       php(language) >= 7.1
# From composer.json
#    ignore phpunit dependency
# From phpcompatinfo
#    Only Core and standard
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{gh_owner}/%{gh_project}) = %{version}


%description
PHPUnit Legacy Versions Adapter.

This version is compatible with phpunit version 7, 8, 9 and 10.

Autoloader: %{_datadir}/php/%{ns_project}/autoload.php


%prep
%forgesetup


%build
# Generate a simple classmap autoloader
%{_bindir}/phpab \
   --template fedora \
   --output src/autoload.php \
   src


%install
mkdir -p   %{buildroot}%{_datadir}/php/
cp -pr src %{buildroot}%{_datadir}/php/%{ns_project}


%check
%if %{with tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require '%{buildroot}%{_datadir}/php/%{ns_project}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Tests\\%{ns_project}\\', dirname(__DIR__)  .'/tests');
EOF

: run upstream test suite with all php and phpunit versions
ret=0
for cmd in php82 php83 php84 php85
do
  if which $cmd; then
    $cmd %{_bindir}/phpunit8 --verbose || ret=1
  fi
done
for cmd in php82 php83 php84 php85
do
  if which $cmd; then
    $cmd %{_bindir}/phpunit9 --verbose || ret=1
  fi
done
if [ -x %{_bindir}/phpunit10 ]; then
  for cmd in php82 php83 php84 php85
  do
    if which $cmd; then
      $cmd %{_bindir}/phpunit10 || ret=1
    fi
  done
fi
if [ -x %{_bindir}/phpunit11 ]; then
  for cmd in php82 php83 php84 php85
  do
    if which $cmd; then
      $cmd %{_bindir}/phpunit11 || ret=1
    fi
  done
fi
if [ -x %{_bindir}/phpunit12 ]; then
  for cmd in php83 php84 php85
  do
    if which $cmd; then
      $cmd %{_bindir}/phpunit12 || ret=1
    fi
  done
fi
if [ -x %{_bindir}/phpunit13 ]; then
  for cmd in php84 php85
  do
    if which $cmd; then
      $cmd %{_bindir}/phpunit13 || ret=1
    fi
  done
fi
exit $ret
%else
: Test suite disabled
%endif


%files
%license LICENSE
%doc *.md
%doc composer.json
%{_datadir}/php/%{ns_project}


%changelog
* Sun May  3 2026 Remi Collet <remi@remirepo.net> - 8.2.3-1
- update to 8.2.2 (no change)
- tests: add phpunit13

* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Jun 26 2025 Remi Collet <remi@remirepo.net> - 8.2.2-7
- tests: remove phpunit7, add phpunit11 and phpunit12
- re-license spec file to CECILL-2.1

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue May 30 2023 Remi Collet <remi@remirepo.net> - 8.2.2-1
- update to 8.2.2 (no change)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Dec 22 2020 Remi Collet <remi@fedoraproject.org> - 8.2.1-1
- initial package
