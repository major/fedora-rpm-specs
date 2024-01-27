# remirepo/fedora spec file for php-doctrine-reflection
#
# Copyright (c) 2018-2023 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%global bootstrap    0
%global gh_commit    6bcea3e81ab8b3d0abe5fde5300bbc8a968960c7
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     doctrine
%global gh_project   reflection
# packagist
%global pk_vendor    %{gh_owner}
%global pk_project   %{gh_project}
# Namespace
%global ns_vendor    Doctrine
%global ns_project   Common
%global ns_subproj   Reflection
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{pk_vendor}-%{pk_project}
Version:        1.2.4
Release:        3%{?dist}
Summary:        Additional reflection functionality

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
BuildRequires:  php-tokenizer
# From composer.json
#        "doctrine/coding-standard": "^9",
#        "doctrine/common": "^3.3",
#        "phpstan/phpstan": "^1.4.10",
#        "phpstan/phpstan-phpunit": "^1",
#        "phpunit/phpunit": "^7.5 || ^8.5 || ^9.5"
BuildRequires: (php-composer(doctrine/annotations) >= 1.0   with php-composer(doctrine/annotations) < 3)
BuildRequires: (php-composer(doctrine/common)      >= 3.3   with php-composer(doctrine/common)      < 4)
%global phpunit %{_bindir}/phpunit9
BuildRequires:  phpunit9 >= 9.5
%endif

# From composer.json
#        "php": "^7.1 || ^8.0"
#        "doctrine/annotations": "^1.0 || ^2.0"
Requires:       php(language) >= 7.1
Requires:      (php-composer(doctrine/annotations) >= 1.0   with php-composer(doctrine/annotations) < 3)
# From phpcompatinfo report for version 1.0.0
Requires:       php-reflection
Requires:       php-pcre
Requires:       php-tokenizer

# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}
# Split off doctrine/common
Conflicts:      php-doctrine-common < 1:2.9


%description
The Doctrine Reflection project is a simple library used by the various
Doctrine projects which adds some additional functionality on top of the
reflection functionality that comes with PHP. It allows you to get the
reflection information about classes, methods and properties statically.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}/%{ns_subproj}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
: Generate a simple autoloader
%{_bindir}/phpab \
    --output lib/%{ns_vendor}/%{ns_project}/%{ns_subproj}/autoload.php \
    --template fedora \
    lib/%{ns_vendor}/%{ns_project}
cat << 'EOF' | tee -a lib/%{ns_vendor}/%{ns_project}/%{ns_subproj}/autoload.php

// Dependencies
\Fedora\Autoloader\Dependencies::required([
    [
        '%{_datadir}/php/%{ns_vendor}/%{ns_project}/Annotations2/autoload.php',
        '%{_datadir}/php/%{ns_vendor}/%{ns_project}/Annotations/autoload.php',
    ],
]);
EOF


%install
mkdir -p                              %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr lib/%{ns_vendor}/%{ns_project} %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}


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
require "%{_datadir}/php/%{ns_vendor}/%{ns_project}3/autoload.php";
EOF

# we don't want PHPStan (which pull nette framework)
find tests -type f -exec grep -q PHPStan {} \; -delete -print

: Run test suite
ret=0
for cmdarg in "php %{phpunit}" php80 php81 php82 php83; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit9} \
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
%{_datadir}/php/%{ns_vendor}/%{ns_project}/%{ns_subproj}/


%changelog
* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 28 2023 Remi Collet <remi@remirepo.net> - 1.2.4-1
- update to 1.2.4 (no change)
- allow doctrine/annotations v2

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun  1 2022 Remi Collet <remi@remirepo.net> - 1.2.3-1
- update to 1.2.3

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 28 2020 Remi Collet <remi@remirepo.net> - 1.2.2-1
- update to 1.2.2
- switch to phpunit9

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Mar 27 2020 Remi Collet <remi@remirepo.net> - 1.2.1-1
- update to 1.2.1

* Mon Mar 23 2020 Remi Collet <remi@remirepo.net> - 1.2.0-1
- update to 1.2.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan  9 2020 Remi Collet <remi@remirepo.net> - 1.1.0-1
- update to 1.1.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 22 2018 Remi Collet <remi@remirepo.net> - 1.0.0-2
- fix conflicts

* Thu Oct 18 2018 Remi Collet <remi@remirepo.net> - 1.0.0-1
- initial package, version 1.0.0
