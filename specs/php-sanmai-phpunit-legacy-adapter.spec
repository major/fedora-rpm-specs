# remirepo/fedora spec file for php-sanmai-phpunit-legacy-adapter
#
# Copyright (c) 2020-2023 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_without       tests

%global gh_commit    aa08b49eac291a49f50e9a094f23b267cc5a9bec
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_date      20150618
%global gh_owner     sanmai
%global gh_project   phpunit-legacy-adapter
%global ns_project   LegacyPHPUnit

Name:           php-%{gh_owner}-%{gh_project}
Version:        8.2.2
Release:        6%{?dist}
Summary:        PHPUnit Legacy Versions Adapter

License:        Apache-2.0
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch
%if %{with tests}
BuildRequires:  phpunit7
BuildRequires:  phpunit8
BuildRequires:  phpunit9
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
%setup -q -n %{gh_project}-%{gh_commit}


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
for cmd in php80 php81 php82
do
  if which $cmd; then
    $cmd %{_bindir}/phpunit7 --verbose || ret=1
  fi
done
for cmd in php80 php81 php82
do
  if which $cmd; then
    $cmd %{_bindir}/phpunit8 --verbose || ret=1
  fi
done
for cmd in php80 php81 php82
do
  if which $cmd; then
    $cmd %{_bindir}/phpunit9 --verbose || ret=1
  fi
done
if [ -x %{_bindir}/phpunit10 ]; then
  for cmd in php80 php81 php82
  do
    if which $cmd; then
      $cmd %{_bindir}/phpunit9 --verbose || ret=1
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
