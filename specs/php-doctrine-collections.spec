#
# Fedora spec file for php-doctrine-collections
#
# Copyright (c) 2013-2022 Shawn Iwinski, Remi Collet
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     doctrine
%global github_name      collections
%global github_version   1.8.0
%global github_commit    2b44dd4cbca8b5744327de78bafef5945c7e7b5e

%global composer_vendor  doctrine
%global composer_project collections

# "php": "^7.1.3 || ^8.0"
%global php_min_ver 7.1.3
# "doctrine/deprecations": "^0.5.3 || ^1"
%global doctrine_depr_min_ver 1
%global doctrine_depr_max_ver 2

# Build using "--without tests" to disable tests
%bcond_without tests

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       7%{?github_release}%{?dist}
Summary:       Collections abstraction library

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}

# GitHub export does not include tests.
# Run php-doctrine-collections-get-source.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with tests}
## composer.json
%global phpunit %{_bindir}/phpunit9
BuildRequires: %{phpunit}
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: (php-composer(doctrine/deprecations) >= %{doctrine_depr_min_ver} with php-composer(doctrine/deprecations) < %{doctrine_depr_max_ver})
## phpcompatinfo (computed from version 1.6.0)
BuildRequires: php-pcre
BuildRequires: php-spl
%endif
# Autoloader
BuildRequires: php-fedora-autoloader-devel

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:     (php-composer(doctrine/deprecations) >= %{doctrine_depr_min_ver} with php-composer(doctrine/deprecations) < %{doctrine_depr_max_ver})
# phpcompatinfo (computed from version 1.6.0)
Requires:      php-pcre
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

# Extracted from Doctrine Common as of version 2.4
Conflicts:     php-pear(pear.doctrine-project.org/DoctrineCommon) < 2.4

%description
%{summary}.

Autoloader: %{phpdir}/Doctrine/Common/Collections/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create autoloader
phpab --template fedora \
      --output lib/Doctrine/Common/Collections/autoload.php \
      lib/Doctrine/Common/Collections

cat <<'AUTOLOAD' | tee -a lib/Doctrine/Common/Collections/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/Doctrine/Deprecations/autoload.php',
]);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}
cp -rp lib/* %{buildroot}%{phpdir}/


%check
%if %{with tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require_once '%{buildroot}%{phpdir}/Doctrine/Common/Collections/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Doctrine\\Tests\\', __DIR__.'/tests/Doctrine/Tests');
BOOTSTRAP

: Upstream tests
SCL_RETURN_CODE=0
for CMD in "php %{phpunit}" php74 php80 php81 php82; do
    if which $CMD; then
        set $CMD
        $1 ${2:-%{_bindir}/phpunit9} --verbose --bootstrap bootstrap.php \
            || SCL_RETURN_CODE=1
    fi
done
exit $SCL_RETURN_CODE
%else
: Tests skipped
%endif


%files
%license LICENSE
%doc *.md
%doc composer.json
%dir %{phpdir}/Doctrine
%dir %{phpdir}/Doctrine/Common
     %{phpdir}/Doctrine/Common/Collections


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Sep 30 2022 Remi Collet <remi@remirepo.net> - 1.8.0-1
- update to 1.8.0

* Mon Sep 26 2022 Remi Collet <remi@remirepo.net> - 1.7.3-1
- update to 1.7.3

* Fri Sep  9 2022 Remi Collet <remi@remirepo.net> - 1.7.2-1
- update to 1.7.2
- switch to classmap autoloader
- add dependency on doctrine/deprecations

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 11 2021 Remi Collet <remi@remirepo.net> - 1.6.8-1
- update to 1.6.8

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.7-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 11 2020 Remi Collet <remi@remirepo.net> - 1.6.7-1
- update to 1.6.7
- add upstream patch for recent PHPUnit

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Remi Collet <remi@remirepo.net> - 1.6.6-1
- update to 1.6.6

* Tue May 26 2020 Remi Collet <remi@remirepo.net> - 1.6.5-1
- update to 1.6.5

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 13 2019 Remi Collet <remi@remirepo.net> - 1.6.4-1
- update to 1.6.4

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 11 2019 Remi Collet <remi@remirepo.net> - 1.6.2-1
- update to 1.6.2

* Tue Mar 26 2019 Remi Collet <remi@remirepo.net> - 1.6.1-1
- update to 1.6.1

* Mon Mar 25 2019 Remi Collet <remi@remirepo.net> - 1.6.0-1
- update to 1.6.0
- raise dependency on PHP 7.1.3
- use PHPUnit 7 for test suite

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 05 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.5.0-1
- Update to 1.5.0 (RHBZ #1473990)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 04 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.4.0-1
- Updated to 1.4.0 (RHBZ #1415530)
- Switched autoloader to php-composer(fedora/autoloader)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jun 27 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.3.0-3
- Updated autoloader with trailing separator

* Wed Jun 24 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.3.0-2
- Added autoloader dependencies

* Wed Jun 24 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.3.0-1
- Updated to 1.3.0 (RHBZ #1211818)
- Added autoloader
- %%license usage

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 20 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2-3
- Added php-composer(%%{composer_vendor}/%%{composer_project}) virtual provide
- Added option to build without tests ("--without tests")

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 12 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2-1
- Updated to 1.2 (BZ #1061117)

* Mon Jan 06 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1-3.20131221git8198717
- Minor syntax changes

* Fri Jan 03 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1-2.20131221git8198717
- Conditional %%{?dist}
- Added conflict w/ PEAR-based DoctrineCommon pkg (version < 2.4)

* Mon Dec 23 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1-1.20131221git8198717
- Initial package
