# remirepo/fedora spec file for php-interfasys-lognormalizer
#
# Copyright (c) 2016 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    d5e4c95e0b0ecc886b78aafda3773b3bcf2ec116
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
#global gh_date      20150801
%global gh_owner     interfasys
%global gh_project   lognormalizer
%global with_tests   0%{!?_without_tests:1}
%global ns_vendor    InterfaSys
%global ns_project   LogNormalizer


Name:           php-%{gh_owner}-%{gh_project}
Version:        1.0
Release:        17%{?dist}
Summary:        Parses variables and converts them to string

License:        AGPLv3+
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch
BuildRequires:  php-composer(theseer/autoload)
%if %{with_tests}
BuildRequires:  php(language) >= 5.4.0
BuildRequires:  php-date
BuildRequires:  php-intl
BuildRequires:  php-json
BuildRequires:  php-spl
# From composer.json, "require-dev": {
#    "phpunit/phpunit": "4.*",
#    "codeclimate/php-test-reporter": "dev-master",
#    "codacy/coverage": "dev-master"
BuildRequires:  php-composer(phpunit/phpunit) >= 4
%endif

# From composer.json, "require": {
#    "php": ">=5.4.0"
Requires:       php(language) >= 5.4.0
# From phpcompatinfo report for date 20150801
Requires:       php-json
Requires:       php-spl

Provides:       php-composer(%{gh_owner}/%{gh_project}) = %{version}


%description
Parses variables and converts them to string so that they can be logged.

Based on the Monolog formatter/normalizer.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}



%build
%{_bindir}/phpab -o src/autoload.php src


%install
: Create a PSR-0 tree
mkdir -p   %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr src %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}


%check
%if %{with_tests}
: Run test suite with system PHP
%{_bindir}/phpunit \
    --bootstrap %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php
%else
: Test suite disabled
%endif


%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc *.md
%doc composer.json
%{_datadir}/php/%{ns_vendor}


%changelog
* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Remi Collet <remi@fedoraproject.org> - 1.0-1
- version 1.0 (no change)

* Thu Jan 14 2016 Remi Collet <remi@fedoraproject.org> - 0-0.1.20150801gitd5e4c95
- initial package