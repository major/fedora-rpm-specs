#
# Fedora spec file for php-gliph
#
# Copyright (c) 2013-2017 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     sdboyer
%global github_name      gliph
%global github_version   0.1.8
%global github_commit    db9e4b77622f91e2d338cc45f83c2cd0e3cf0e1e

%global composer_vendor  sdboyer
%global composer_project gliph

# "php": ">=5.3"
%global php_min_ver      5.3.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_project}
Version:       %{github_version}
Release:       18%{?github_release}%{?dist}
Summary:       A graph library for PHP

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}

# Run "php-gliph-get-source.sh" to create source
Source0:       %{name}-%{version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with_tests}
BuildRequires: php-composer(phpunit/phpunit)
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
## phpcompatinfo (computed from version 0.1.8)
BuildRequires: php-reflection
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 0.1.8)
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Standard "php-{COMPOSER_VENDOR}-{COMPOSER_PROJECT}" naming
Provides:      php-%{composer_vendor}-%{composer_project} = %{version}-%{release}
# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
Gliph is a graph library for PHP. It provides graph building blocks and
data structures for use by other PHP applications. It is (currently) designed
for use with in-memory graphs, not for interaction with a graph database like
Neo4J (http://neo4j.org/).

Autoloader: %{phpdir}/Gliph/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}


%build

: Create autoloader
cat <<'AUTOLOAD' | tee src/Gliph/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Gliph\\', __DIR__);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}
cp -rp src/* %{buildroot}%{phpdir}/


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require_once '%{buildroot}%{phpdir}/Gliph/autoload.php';
\Fedora\Autoloader\Autoload::addPsr0('Gliph', __DIR__.'/tests');
BOOTSTRAP

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in "" %{?rhel:php54 php55} php56 php70 php71 php72; do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose --bootstrap bootstrap.php . \
            || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json
%{phpdir}/Gliph


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun May 14 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.1.8-7
- Switch autoloader to php-composer(fedora/autoloader)
- Test with SCLs if available

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jul 11 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.1.8-4
- Added missing autoloader require

* Sat Jul 11 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.1.8-3
- Added autoloader
- Added tests
- Added standard "php-{COMPOSER_VENDOR}-{COMPOSER_PROJECT}" naming provides

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.1.8-1
- Updated to 0.1.8 (BZ #1125361)

* Sat Jul 19 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.1.6-1
- Updated to 0.1.6 (BZ #1119424)
- Added "php-composer(sdboyer/gliph)" virtual provide

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Nov 06 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.1.5-1
- Updated to 0.1.5
- Removed tests (git export-ignored upstream)

* Thu Oct 24 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.1.4-1.20131024git8da23c6
- Updated to latest snapshot (commit 8da23c6397354e9acc7a7e6f8d2a782fdf21ab54)
  which includes LICENSE
- "php-common" -> "php(language)"
- Added PHPUnit min/max versions

* Wed Oct 23 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.1.4-1
- Initial package
