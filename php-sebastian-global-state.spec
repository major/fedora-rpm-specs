# spec file for php-sebastian-global-state
#
# Copyright (c) 2014-2016 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    bc37d50fea7d017d3d340f230811c9f1d7280af4
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   global-state
%global php_home     %{_datadir}/php/SebastianBergmann
%if %{bootstrap}
%global with_tests   %{?_with_tests:1}%{!?_with_tests:0}
%else
%global with_tests   %{?_without_tests:0}%{!?_without_tests:1}
%endif

Name:           php-sebastian-global-state
Version:        1.1.1
Release:        16%{?dist}
Summary:        Snapshotting of global state

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch
BuildRequires:  php(language) >= 5.3.3
BuildRequires:  php-fedora-autoloader-devel
%if %{with_tests}
# from composer.json, "require-dev": {
#        "phpunit/phpunit": "~4.2"
BuildRequires:  php-composer(phpunit/phpunit) > 4.2
%endif

# from composer.json, "require": {
#        "php": ">=5.3.3"
Requires:       php(language) >= 5.3.3
# from composer.json, "suggest": {
#        "ext-uopz": "*"
%if 0%{?fedora} > 21
Suggests:       php-uopz
%endif
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(sebastian/global-state) = %{version}


%description
Snapshotting of global state,
factored out of PHPUnit into a stand-alone component.


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
# Generate the Autoloader
phpab --template fedora --output src/autoload.php src

# For the test suite
phpab --template fedora --output tests/autoload.php tests/_fixture/


%install
mkdir -p   %{buildroot}%{php_home}
cp -pr src %{buildroot}%{php_home}/GlobalState


%check
%if %{with_tests}
mkdir vendor
cat <<EOF | tee vendor/autoload.php
<?php
require 'SebastianBergmann/GlobalState/autoload.php';
require 'tests/autoload.php';
EOF

: Run upstream test suite
%{_bindir}/php -d include_path=.:%{buildroot}%{_datadir}/php:%{_datadir}/php \
%{_bindir}/phpunit --verbose

%else
: bootstrap build with test suite disabled
%endif


%files
%doc LICENSE README.md composer.json
%dir %{php_home}
%{php_home}/GlobalState


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-14
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Oct 21 2016 Remi Collet <remi@fedoraproject.org> - 1.1.1-4
- switch to fedora/autoloader

* Thu Oct 13 2016 Remi Collet <remi@fedoraproject.org> - 1.1.1-3
- add optional dependency on uopz extension

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 12 2015 Remi Collet <remi@fedoraproject.org> - 1.1.1-1
- update to 1.1.1

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Dec  5 2014 Remi Collet <remi@fedoraproject.org> - 1.0.0-1
- initial package