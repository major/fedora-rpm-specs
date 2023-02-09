# remirepo/fedora spec file for php-doctrine-persistence2
#
# Copyright (c) 2018-2023 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%global bootstrap    0
%global gh_commit    e36f22765f4d10a7748228babbf73da5edfeed3c
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     doctrine
%global gh_project   persistence
%global major        2
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

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        2.5.7
Release:        1%{?dist}
Summary:        Doctrine Persistence abstractions, version %{major}

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
#        "composer/package-versions-deprecated": "^1.11",
#        "phpstan/phpstan": "~1.4.10 || 1.9.4",
#        "doctrine/annotations": "^1 || ^2",
#        "doctrine/coding-standard": "^9 || ^11",
#        "doctrine/common": "^3.0",
#        "phpunit/phpunit": "^7.5.20 || ^8.5 || ^9.5",
#        "symfony/cache": "^4.4 || ^5.4 || ^6.0",
#        "vimeo/psalm": "4.30.0 || 5.3.0"
BuildRequires: (php-composer(doctrine/annotations)   >= 1.0   with php-composer(doctrine/annotations)   < 3)
BuildRequires: (php-composer(doctrine/cache)         >= 1.11  with php-composer(doctrine/cache)         < 3)
BuildRequires: (php-composer(doctrine/collections)   >= 1.0   with php-composer(doctrine/collections)   < 2)
BuildRequires: (php-composer(doctrine/event-manager) >= 1     with php-composer(doctrine/event-manager) < 3)
BuildRequires: (php-composer(doctrine/common)        >= 3.0   with php-composer(doctrine/common)        < 4)
BuildRequires: (php-composer(doctrine/deprecations)  >= 0.5.3 with php-composer(doctrine/deprecations)  < 2)
BuildRequires: (php-composer(symfony/cache)          >= 4.4   with php-composer(symfony/cache)          < 7)
BuildRequires: (php-composer(psr/cache)              >= 1.0   with php-composer(psr/cache)              < 2)
%global phpunit %{_bindir}/phpunit9
BuildRequires:  phpunit9 >= 9.5
%endif

# From composer.json
#        "php": "^7.1 || ^8.0"
#        "doctrine/cache": "^1.11 || ^2.0",
#        "doctrine/collections": "^1.0",
#        "doctrine/event-manager": "^1 || ^2",
#        "psr/cache": "^1.0 || ^2.0 || ^3.0",
#        "doctrine/deprecations": "^0.5.3 || ^1"
Requires:       php(language) >= 7.1
Requires:      (php-composer(doctrine/cache)         >= 1.11  with php-composer(doctrine/cache)         < 3)
Requires:      (php-composer(doctrine/collections)   >= 1.0   with php-composer(doctrine/collections)   < 2)
Requires:      (php-composer(doctrine/event-manager) >= 1     with php-composer(doctrine/event-manager) < 3)
Requires:      (php-composer(doctrine/deprecations)  >= 0.5.3 with php-composer(doctrine/deprecations)  < 2)
# ignore v2 and v3
Requires:      (php-composer(psr/cache)              >= 1.0   with php-composer(psr/cache)              < 2)
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

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_subproj}%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv src/%{ns_subproj} \
   src/%{ns_subproj}%{major}
mv src/%{ns_project}/%{ns_subproj} \
   src/%{ns_project}/%{ns_subproj}%{major}


%build
: Generate a simple autoloader
%{_bindir}/phpab \
    --output src/%{ns_subproj}%{major}/autoload.php \
    --template fedora \
    src
cat << 'EOF' | tee -a src/%{ns_subproj}%{major}/autoload.php

// Dependencies
\Fedora\Autoloader\Dependencies::required([
    '%{_datadir}/php/Psr/Cache/autoload.php',
    '%{_datadir}/php/%{ns_vendor}/Deprecations/autoload.php',
    [
        '%{_datadir}/php/%{ns_vendor}/%{ns_project}/Cache2/autoload.php',
        '%{_datadir}/php/%{ns_vendor}/%{ns_project}/Cache/autoload.php',
    ],
    '%{_datadir}/php/%{ns_vendor}/%{ns_project}/Collections/autoload.php',
    [
        '%{_datadir}/php/%{ns_vendor}/EventManager2/autoload.php',
        '%{_datadir}/php/%{ns_vendor}/%{ns_project}/EventManager/autoload.php',
    ],
]);
EOF


%install
mkdir -p   %{buildroot}%{_datadir}/php
cp -pr src %{buildroot}%{_datadir}/php/%{ns_vendor}


%check
%if %{with_tests}
: Generate autoloader
mkdir vendor
%{_bindir}/phpab \
    --output vendor/autoload.php \
    --template fedora \
    tests

cat << 'EOF' | tee -a vendor/autoload.php
require "%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_subproj}%{major}/autoload.php";
\Fedora\Autoloader\Dependencies::required([
    '%{_datadir}/php/%{ns_vendor}/Common3/autoload.php',
    [
        '%{_datadir}/php/%{ns_vendor}/%{ns_project}/Annotations2/autoload.php',
        '%{_datadir}/php/%{ns_vendor}/%{ns_project}/Annotations/autoload.php',
    ], [
        '%{_datadir}/php/Symfony6/Component/Cache/autoload.php',
        '%{_datadir}/php/Symfony5/Component/Cache/autoload.php',
        '%{_datadir}/php/Symfony4/Component/Cache/autoload.php',
    ],
]);
EOF

# we don't want PHPStan (which pull nette framework)
find tests -type f -exec grep -q PHPStan {} \; -delete -print

: Run test suite
ret=0
for cmdarg in "php %{phpunit}" php80 php81 php82; do
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
%license LICENSE
%doc *.md
%doc composer.json
%{_datadir}/php/%{ns_vendor}/%{ns_project}/%{ns_subproj}%{major}
%{_datadir}/php/%{ns_vendor}/%{ns_subproj}%{major}


%changelog
* Tue Feb  7 2023 Remi Collet <remi@remirepo.net> - 2.5.7-1
- update to 2.5.7

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan  3 2023 Remi Collet <remi@remirepo.net> - 2.5.6-1
- update to 2.5.6
- allow doctrine/annotations v2

* Thu Oct 13 2022 Remi Collet <remi@remirepo.net> - 2.5.5-1
- update to 2.5.5
- allow doctrine/event-manager v2

* Mon Aug  8 2022 Remi Collet <remi@remirepo.net> - 2.5.4-1
- update to 2.5.4

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May  9 2022 Remi Collet <remi@remirepo.net> - 2.5.3-1
- update to 2.5.3

* Tue May  3 2022 Remi Collet <remi@remirepo.net> - 2.5.2-1
- update to 2.5.2
- allow doctrine/deprecations 1

* Tue Apr 19 2022 Remi Collet <remi@remirepo.net> - 2.5.1-1
- update to 2.5.1

* Mon Apr 11 2022 Remi Collet <remi@remirepo.net> - 2.5.0-1
- update to 2.5.0

* Tue Mar 29 2022 Remi Collet <remi@remirepo.net> - 2.4.1-1
- update to 2.4.1

* Tue Mar 15 2022 Remi Collet <remi@remirepo.net> - 2.4.0-1
- update to 2.4.0

* Fri Jan 21 2022 Remi Collet <remi@remirepo.net> - 2.3.0-3
- fix autoloader

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 10 2022 Remi Collet <remi@remirepo.net> - 2.3.0-1
- update to 2.3.0

* Fri Oct 29 2021 Remi Collet <remi@remirepo.net> - 2.2.3-1
- update to 2.2.3

* Wed Aug 11 2021 Remi Collet <remi@remirepo.net> - 2.2.2-1
- update to 2.2.2

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed May 19 2021 Remi Collet <remi@remirepo.net> - 2.2.1-1
- update to 2.2.1
- raise dependency on doctrine/cache v1.11 and v2
- add dependency on doctrine/deprecations
- add dependency on psr/cache

* Mon May 17 2021 Remi Collet <remi@remirepo.net> - 2.2.0-1
- update to 2.2.0
- drop runtime dependency on doctrine/reflection
- add build dependency on doctrine/common v3
- add build dependency on symfony/cache v4

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 26 2020 Remi Collet <remi@remirepo.net> - 2.1.0-1
- update to 2.1.0
- switch to phpunit9

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 14 2020 Remi Collet <remi@remirepo.net> - 2.0.0-1
- update to 2.0.0
- rename to php-doctrine-persistence2
- install in /usr/share/php/Doctrine/Persistence2

* Mon Mar 23 2020 Remi Collet <remi@remirepo.net> - 1.3.7-1
- update to 1.3.7 (no change)
- raise dependency on doctrine/reflection 1.2

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

* Wed Apr 24 2019 Remi Collet <remi@remirepo.net> - 1.1.1-1
- update to 1.1.1

* Thu Nov 22 2018 Remi Collet <remi@remirepo.net> - 1.1.0-1
- update to 1.1.0

* Thu Oct 18 2018 Remi Collet <remi@remirepo.net> - 1.0.1-1
- initial package, version 1.0.1
