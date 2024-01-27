# remirepo/fedora spec file for php-doctrine-persistence
#
# Copyright (c) 2018-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%global bootstrap    0
%global gh_commit    7a6eac9fb6f61bba91328f15aa7547f4806ca288
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     doctrine
%global gh_project   persistence
# packagist
%global pk_vendor    %{gh_owner}
%global pk_project   %{gh_project}
# Namespace
%global ns_vendor    Doctrine
%global ns_project   Common
%global ns_subproj   Persistence
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{pk_vendor}-%{pk_project}
Version:        1.3.8
Release:        9%{?dist}
Summary:        Doctrine Persistence abstractions

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
BuildRequires:  php-fedora-autoloader-devel
%if %{with_tests}
BuildRequires:  php(language) >= 7.1
BuildRequires:  php-reflection
BuildRequires:  php-pcre
BuildRequires:  php-spl
# From composer.json
#        "phpstan/phpstan": "^0.11",
#        "doctrine/coding-standard": "^6.0",
#        "phpunit/phpunit": "^7.0 || ^8.0 || ^9.0",
#        "vimeo/psalm": "^3.11"
BuildRequires: (php-composer(doctrine/annotations)   >= 1.0   with php-composer(doctrine/annotations)   < 2)
BuildRequires: (php-composer(doctrine/cache)         >= 1.0   with php-composer(doctrine/cache)         < 2)
BuildRequires: (php-composer(doctrine/collections)   >= 1.0   with php-composer(doctrine/collections)   < 2)
BuildRequires: (php-composer(doctrine/event-manager) >= 1.0   with php-composer(doctrine/event-manager) < 2)
BuildRequires: (php-composer(doctrine/reflection)    >= 1.2   with php-composer(doctrine/reflection)    < 2)
BuildRequires:  phpunit9
%endif

# From composer.json
#        "php": "^7.1 || ^8.0"
#        "doctrine/annotations": "^1.0",
#        "doctrine/cache": "^1.0",
#        "doctrine/collections": "^1.0",
#        "doctrine/event-manager": "^1.0",
#        "doctrine/reflection": "^1.2"
Requires:       php(language) >= 7.1
Requires:      (php-composer(doctrine/annotations)   >= 1.0   with php-composer(doctrine/annotations)   < 2)
Requires:      (php-composer(doctrine/cache)         >= 1.0   with php-composer(doctrine/cache)         < 2)
Requires:      (php-composer(doctrine/collections)   >= 1.0   with php-composer(doctrine/collections)   < 2)
Requires:      (php-composer(doctrine/event-manager) >= 1.0   with php-composer(doctrine/event-manager) < 2)
Requires:      (php-composer(doctrine/reflection)    >= 1.2   with php-composer(doctrine/reflection)    < 2)
# From phpcompatinfo report for version 1.0.0
Requires:       php-reflection
Requires:       php-pcre
Requires:       php-spl

# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}
# Split off doctrine/common
Conflicts:      php-doctrine-common < 1:2.10


%description
The Doctrine Persistence project is a set of shared interfaces and
functionality that the different Doctrine object mappers share.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_subproj}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
: Generate a simple autoloader
%{_bindir}/phpab \
    --output lib/%{ns_vendor}/%{ns_subproj}/autoload.php \
    --template fedora \
    lib/%{ns_vendor}
cat << 'EOF' | tee -a lib/%{ns_vendor}/%{ns_subproj}/autoload.php

// Dependencies
\Fedora\Autoloader\Dependencies::required([
    '%{_datadir}/php/%{ns_vendor}/%{ns_project}/Annotations/autoload.php',
    '%{_datadir}/php/%{ns_vendor}/%{ns_project}/Cache/autoload.php',
    '%{_datadir}/php/%{ns_vendor}/%{ns_project}/Collections/autoload.php',
    '%{_datadir}/php/%{ns_vendor}/%{ns_project}/EventManager/autoload.php',
    '%{_datadir}/php/%{ns_vendor}/%{ns_project}/Reflection/autoload.php',
]);
EOF


%install
mkdir -p                %{buildroot}%{_datadir}/php
cp -pr lib/%{ns_vendor} %{buildroot}%{_datadir}/php/%{ns_vendor}
ln -s  ../../%{ns_subproj}/autoload.php \
       %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}/%{ns_subproj}/autoload.php


%check
%if %{with_tests}
: Generate autoloader
mkdir vendor
%{_bindir}/phpab \
    --output vendor/autoload.php \
    --template fedora \
    tests

cat << 'EOF' | tee -a vendor/autoload.php
require "%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}/%{ns_subproj}/autoload.php";
EOF

# we don't want PHPStan (which pull nette framework)
find tests -type f -exec grep -q PHPStan {} \; -delete -print

: Run test suite
ret=0
# TODO php80 exception message differs
for cmd in php73 php74 php80; do
  if which $cmd; then
    VER=$($cmd -r 'echo PHP_VERSION_ID;')
    [ $VER -ge 80000 ] && SKIP="--filter '^((?!(testGetManagerForInvalidClass|testGetManagerForInvalidAliasedClass)).)*$'"

    $cmd %{_bindir}/phpunit9 $SKIP \
        --bootstrap vendor/autoload.php \
        --verbose || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json
%{_datadir}/php/%{ns_vendor}/%{ns_project}/*
%{_datadir}/php/%{ns_vendor}/%{ns_subproj}


%changelog
* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 11 2020 Remi Collet <remi@remirepo.net> - 1.3.8-1
- update to 1.3.8
- switch to phpunit9

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 23 2020 Remi Collet <remi@remirepo.net> - 1.3.7-1
- update to 1.3.7 (no change)
- raise dependency on doctrine/reflection 1.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Remi Collet <remi@remirepo.net> - 1.3.6-1
- update to 1.3.6
- raise dependency on doctrine/reflection 1.1

* Wed Jan 15 2020 Remi Collet <remi@remirepo.net> - 1.3.5-1
- update to 1.3.5

* Fri Jan 10 2020 Remi Collet <remi@remirepo.net> - 1.3.4-1
- update to 1.3.4

* Fri Dec 13 2019 Remi Collet <remi@remirepo.net> - 1.3.3-1
- update to 1.3.3

* Fri Dec 13 2019 Remi Collet <remi@remirepo.net> - 1.3.2-1
- update to 1.3.2

* Fri Dec 13 2019 Remi Collet <remi@remirepo.net> - 1.3.1-1
- update to 1.3.1
- use new namespace Doctrine\Persistence
  and provide compatibility Doctrine\Common\Persistence

* Wed Nov 13 2019 Remi Collet <remi@remirepo.net> - 1.2.0-1
- update to 1.2.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Remi Collet <remi@remirepo.net> - 1.1.1-1
- update to 1.1.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 22 2018 Remi Collet <remi@remirepo.net> - 1.1.0-1
- update to 1.1.0

* Thu Oct 18 2018 Remi Collet <remi@remirepo.net> - 1.0.1-1
- initial package, version 1.0.1
