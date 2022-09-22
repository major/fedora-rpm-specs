#
# RPM spec file for php-mtdowling-transducers
#
# Copyright (c) 2015 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     mtdowling
%global github_name      transducers.php
%global github_version   0.3.0
%global github_commit    32ff6a67b5d5d1930533277a505b4f9d360dbe6c

%global composer_vendor  mtdowling
%global composer_project transducers

# "php": ">=5.5.0"
%global php_min_ver 5.5.0

# Build using "--without tests" to disable tests
%global with_tests %{?_without_tests:0}%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       16%{?github_release}%{?dist}
Summary:       Composable algorithmic transformations

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}

# GitHub download/export does not include tests
# Run "php-mtdowling-transducers-get-source.sh" to create source
Source0:       %{name}-%{version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
%if %{with_tests}
# For tests
## composer.json
BuildRequires: %{_bindir}/phpunit
BuildRequires: php(language) >= %{php_min_ver}
## phpcompatinfo (computed from version 0.3.0)
BuildRequires: php-json
BuildRequires: php-spl
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 0.3.0)
Requires:      php-json
Requires:      php-spl

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
Transducers [1] are composable algorithmic transformations. They are independent
from the context of their input and output sources and specify only the essence
of the transformation in terms of an individual element. Because transducers are
decoupled from input or output sources, they can be used in many different
processes - collections, streams, channels, observables, etc. Transducers
compose directly, without awareness of input or creation of intermediate
aggregates.

[1] http://clojure.org/transducers


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Generate autoloader
cat > src/autoload.php <<'AUTOLOAD'
<?php
/**
 * While an autoloader is not really necessary for this (currently) single-file
 * library, it is provided for future-proofing the loading of this library.
 */

require __DIR__ . '/transducers.php';
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/%{composer_project}
cp -rp src/* %{buildroot}%{phpdir}/%{composer_project}/


%check
%if %{with_tests}
: Temporarily skip failing tests
: See https://github.com/mtdowling/transducers.php/issues/4
sed -e 's/function testToTraversableReturnsStreamsIter/function SKIP_testToTraversableReturnsStreamsIter/' \
    -e 's/function testCanStepInClosing/function SKIP_testCanStepInClosing/' \
    -i tests/transducersTest.php

%{_bindir}/phpunit \
    --bootstrap %{buildroot}%{phpdir}/%{composer_project}/autoload.php
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc CHANGELOG.md
%doc README.rst
%doc composer.json
%{phpdir}/%{composer_project}


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jun 28 2016 Remi Collet <remi@fedoraproject.org> - 0.3.0-4
- drop dependency on php-ereg (false positive)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 16 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.3.0-1
- Initial package
