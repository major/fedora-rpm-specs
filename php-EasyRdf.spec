#
# Fedora spec file for php-EasyRdf
#
# Copyright (c) 2013-2020 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#

%global github_owner     njh
%global github_name      easyrdf
%global github_version   0.9.1
%global github_commit    acd09dfe0555fbcfa254291e433c45fdd4652566

%global composer_vendor  easyrdf
%global composer_project easyrdf

# "php": ">=5.2.8"
%global php_min_ver 5.2.8

%if 0%{?el6}
%global raptor_pkg raptor
%else
%global raptor_pkg raptor2
%endif

# Redland support if Fedora < 26 or EL 6
%if 0%{?fedora}
%if 0%{?fedora} < 25
%global redland_support 1
%else
%global redland_support 0
%endif
%else
%global redland_support 0%{?el6:1}
%endif

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-EasyRdf
Version:       0.9.1
Release:       6%{?dist}
Summary:       A PHP library designed to make it easy to consume and produce RDF

License:       BSD
URL:           http://www.easyrdf.org

# GitHub export does not include tests.
# Run php-EasyRdf-get-source.sh to create full source.
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

# Upstream patches
## Fix PHP 7.1 bug
## https://github.com/njh/easyrdf/commit/4ed264051ed407d59c2fde4128be176e96e8f22a
## https://github.com/njh/easyrdf/commit/4ed264051ed407d59c2fde4128be176e96e8f22a.patch
Patch0:        4ed264051ed407d59c2fde4128be176e96e8f22a.patch
## Fix potential bugs and incomplete docs
## https://github.com/njh/easyrdf/commit/5eb5154fec8b3d3df666628ba2f3636c0fa385c3
## https://github.com/njh/easyrdf/commit/5eb5154fec8b3d3df666628ba2f3636c0fa385c3.patch
Patch1:        5eb5154fec8b3d3df666628ba2f3636c0fa385c3.patch
## Fix PHP 7.4 deprecation
## https://github.com/njh/easyrdf/commit/656a86feff97afaff2b1ff7dbc7cc696b66e8a06
## https://github.com/njh/easyrdf/commit/656a86feff97afaff2b1ff7dbc7cc696b66e8a06.patch
## NOTE: Modified for un-namespaced version 0.9: `lib/ParsedUri.php` => `lib/EastRdf/ParsedUri.php`
Patch2:        %{name}-fix-php-7-4.patch

BuildArch:     noarch
# Tests
%if %{with_tests}
BuildRequires: graphviz
BuildRequires: graphviz-gd
BuildRequires: %{raptor_pkg}
%if %{redland_support}
BuildRequires: php-redland
%endif
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
## phpcompatinfo (computed from version 0.9.1)
BuildRequires: php-ctype
BuildRequires: php-date
BuildRequires: php-dom
BuildRequires: php-json
BuildRequires: php-libxml
BuildRequires: php-mbstring
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-simplexml
BuildRequires: php-spl
BuildRequires: php-xml
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo requires (computed from version 0.9.1)
Requires:      php-ctype
Requires:      php-date
Requires:      php-dom
Requires:      php-json
Requires:      php-libxml
Requires:      php-mbstring
Requires:      php-pcre
Requires:      php-simplexml
Requires:      php-spl
Requires:      php-xml
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Weak dependencies
%if 0%{?fedora} >= 21
Suggests:      graphviz
Suggests:      graphviz-gd
Suggests:      %{raptor_pkg}
%if %{redland_support}
Suggests:      php-redland
%endif
%endif

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

Obsoletes:     %{name}-test

%description
EasyRdf is a PHP library designed to make it easy to consume and produce RDF
(http://en.wikipedia.org/wiki/Resource_Description_Framework). It was designed
for use in mixed teams of experienced and inexperienced RDF developers. It is
written in Object Oriented PHP and has been tested extensively using PHPUnit.

After parsing EasyRdf builds up a graph of PHP objects that can then be walked
around to get the data to be placed on the page. Dump methods are available to
inspect what data is available during development.

Data is typically loaded into a EasyRdf_Graph object from source RDF documents,
loaded from the web via HTTP. The EasyRdf_GraphStore class simplifies loading
and saving data to a SPARQL 1.1 Graph Store.

SPARQL queries can be made over HTTP to a Triplestore using the
EasyRdf_Sparql_Client class. SELECT and ASK queries will return an
EasyRdf_Sparql_Result object and CONSTRUCT and DESCRIBE queries will
return an EasyRdf_Graph object.

Autoloader: %{phpdir}/EasyRdf/autoload.php


%package doc
Summary: Documentation for %{name}

%description doc
%{summary}.


%prep
%setup -qn %{github_name}-%{github_commit}

# Fix PHP 7.1 bug
%patch0 -p1
# Fix potential bugs and incomplete docs
%patch1 -p1
# Fix PHP 7.4 deprecation
%patch2 -p1


%build
: Create autoloader
cat <<'AUTOLOAD' | tee lib/EasyRdf/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr0('EasyRdf_', dirname(__DIR__));
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}
cp -rp lib/* %{buildroot}%{phpdir}/


%check
%if %{with_tests}
: Create PHPUnit config
cat <<'PHPUNIT' | tee phpunit.xml
<?xml version="1.0" encoding="UTF-8"?>
<phpunit
    bootstrap="%{buildroot}%{phpdir}/EasyRdf/autoload.php"
    colors="true">
    <testsuites>
      <testsuite name="EasyRdf Library">
        <directory suffix="Test.php">./test/EasyRdf/</directory>
      </testsuite>
    </testsuites>
</phpunit>
PHPUNIT

: Skip tests that sometimes cause timeout exceptions
sed -e 's/testSerialiseSvg/SKIP_testSerialiseSvg/' \
    -e 's/testSerialiseSvg/SKIP_testSerialisePng/' \
    -i test/EasyRdf/Serialiser/GraphVizTest.php

%if 0%{?fedora} >= 31
: Skip test known to fail on f31+
sed 's/function testAddInvalidObject/function SKIP_testAddInvalidObject/' \
    -i test/EasyRdf/GraphTest.php \
    -i test/EasyRdf/ResourceTest.php
%endif

%if !%{redland_support}
: No redland support
rm -f test/EasyRdf/Parser/RedlandTest.php
%endif

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in php php71 php72 php73 php74; do
    if [ "php" == "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE.md
%doc CHANGELOG.md
%doc README.md
%doc composer.json
%{phpdir}/EasyRdf.php
%{phpdir}/EasyRdf

%files doc
%doc docs
%doc examples


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb 22 2020 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.9.1-1
- Update to 0.9.1
- Switch source to GitHub as download from www.easyrdf.org is corrupt
- Fix FTBFS (RHBZ #1799864)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov  2 2017 Remi Collet <remi@remirepo.net> - 0.9.0-8
- add upstream patch for PHP 7.1
- add upstream patch for PHP 7.2

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 22 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.9.0-6
- Fix FTBS in rawhide (RHBZ #1424061)
- Skip tests known to fail since PHP 7.1 (see https://github.com/njh/easyrdf/issues/276)
- Add SCL tests if available
- Use php-composer(fedora/autoloader)
- Move optional dependencies from description to weak dependencies (Suggests)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Oct 09 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.9.0-4
- No Redland support for Fedora 25+ (RHBZ #1350621)

* Sun Oct 09 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.9.0-3
- No Redland support for Fedora 26+ (RHBZ #1350621)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jun 28 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.9.0-1
- Updated to 0.9.0 (RHBZ #1163321)
- Added autoloader

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Nov 18 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.8.0-5
- Modified raptor and redland logic

* Fri Nov 14 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.8.0-4
- No raptor or redland for el7

* Thu Nov 13 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.8.0-3
- Added php-composer(easyrdf/easyrdf) virtual provide
- Added option to build without tests ("--without tests")
- Reduce PHP min version from 5.3.3 to 5.2.8 (per composer.json)
- %%license usage

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 02 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.8.0-1
- Updated to 0.8.0
- Updated PHP min version from 5.2.8 to 5.3.3
- Added php-[libxml,mbstring,reflection,simplexml] requires
- Removed pre-0.8.0 fixes
- Updated %%check to use PHPUnit directly and skip tests that sometimes cause
  timeout exceptions

* Fri Nov 15 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.7.2-5
- Removed test sub-package
- php-common => php(language)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 04 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.7.2-3
- Added note in %%description about optional dependencies
- Temporarily skip "EasyRdf_Serialiser_GraphVizTest::testSerialiseSvg" test
  for Fedora > 18

* Mon Jan 28 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.7.2-2
- Tests run by default (i.e. without "--with tests")
- Fixes for tests
- Removed Mac files
- Separated docs into sub-package

* Sun Jan 27 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.7.2-1
- Initial package
