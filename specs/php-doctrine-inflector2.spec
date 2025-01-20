# remirepo/fedora spec file for php-doctrine-inflector2
#
# Copyright (c) 2013-2023 Shawn Iwinski, Remi Collet
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     doctrine
%global github_name      inflector
%global github_version   2.0.8
%global major            2
%global github_commit    f9301a5b2fb1216b2b08f02ba04dc45423db6bff

%global composer_vendor  doctrine
%global composer_project inflector

# "php": "^7.2 || ^8.0"
%global php_min_ver 7.2

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}%{major}
Version:       %{github_version}
Release:       6%{?github_release}%{?dist}
Summary:       Common string manipulations with regard to casing and singular/plural rules

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}

# GitHub export does not include tests.
# Run php-doctrine-inflector-get-source.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: phpunit9 >= 9.5
BuildRequires: php(language) >= %{php_min_ver}
## phpcompatinfo (computed from version 2.0.1)
BuildRequires: php-mbstring
BuildRequires: php-pcre
BuildRequires: php-spl
%endif
# Autoloader
BuildRequires: php-fedora-autoloader-devel

# composer.json
Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 2.0.1)
Requires:      php-mbstring
Requires:      php-pcre
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
Doctrine Inflector is a small library that can perform string manipulations
with regard to upper-/lowercase and singular/plural forms of words.

Autoloader: %{phpdir}/Doctrine/Inflector%{major}/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create autoloader
phpab --template fedora --output lib/Doctrine/Inflector/autoload.php lib


%install
mkdir -p %{buildroot}%{phpdir}/Doctrine
cp -rp lib/Doctrine/Inflector %{buildroot}%{phpdir}/Doctrine/Inflector%{major}


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require_once '%{buildroot}%{phpdir}/Doctrine/Inflector%{major}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr0('Doctrine\\Tests', __DIR__.'/tests');
BOOTSTRAP

: Upstream tests
RETURN_CODE=0
for PHP_EXEC in "" php80 php81 php82 php83; do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC; then
        phpunit9 --verbose --bootstrap bootstrap.php \
            || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif


%files
%license LICENSE
%doc *.md
%doc composer.json
%dir %{phpdir}/Doctrine
     %{phpdir}/Doctrine/Inflector%{major}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 20 2023 Remi Collet <remi@remirepo.net> - 2.0.8-1
- update to 2.0.8

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Oct 21 2022 Remi Collet <remi@remirepo.net> - 2.0.6-1
- update to 2.0.6

* Fri Sep  9 2022 Remi Collet <remi@remirepo.net> - 2.0.5-1
- update to 2.0.5

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 25 2021 Remi Collet <remi@remirepo.net> - 2.0.4-1
- update to 2.0.4
- switch to phpunit9

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun  2 2020 Remi Collet <remi@remirepo.net> - 2.0.3-1
- update to 2.0.3

* Tue May 26 2020 Remi Collet <remi@remirepo.net> - 2.0.2-1
- update to 2.0.2

* Mon May 11 2020 Remi Collet <remi@remirepo.net> - 2.0.1-1
- update to 2.0.1
- rename to php-doctrine-inflector2
- move to /usr/share/php/Doctrine/Inflector2

* Mon May 11 2020 Remi Collet <remi@remirepo.net> - 1.4.1-1
- update to 1.4.1
- raise dependency on PHP 7.2
- switch to phpunit8
- switch to classmap autoloader

* Wed Nov 13 2019 Remi Collet <remi@remirepo.net> - 1.3.1-1
- update to 1.3.1

* Sun Apr 22 2018 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.3.0-1
- Update to 1.3.0 (RHBZ #1473993)
- Add get source script
- Add composer.json to repo

* Sat May 13 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1.0-4
- Switch autoloader to php-composer(fedora/autoloader)
- Test with SCLs if available

* Sun Jan 03 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1.0-1
- Updated to 1.1.0 (RHBZ #1279884)

* Sat Jun 27 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.1-5
- Updated autoloader with trailing separator

* Wed Jun 24 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.1-4
- Added autoloader

* Sun Dec 28 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.1-2
- %%license usage

* Sun Dec 28 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.1-1
- Updated to 1.0.1 (BZ #1176943)

* Fri Jun 20 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0-4.20131221gita81c334
- Added php-composer(%%{composer_vendor}/%%{composer_project}) virtual provide
- Added option to build without tests ("--without tests")

* Sat Jan 11 2014 Remi Collet <rpms@famillecollet.com> 1.0-2.20131221gita81c334
- backport for remi repo

* Mon Jan 06 2014 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0-2.20131221gita81c334
- Conditional %%{?dist}

* Mon Dec 23 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0-1.20131221gita81c334
- Initial package
