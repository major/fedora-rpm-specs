#
# RPM spec file for php-pimple1
#
# Copyright (c) 2015 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     silexphp
%global github_name      Pimple
%global github_version   1.1.1
%global github_commit    2019c145fe393923f3441b23f29bbdfaa5c58c4d

%global composer_vendor  pimple
%global composer_project pimple

# "php": ">=5.3.0"
%global php_min_ver 5.3.0

# Build using "--without tests" to disable tests
%global with_tests  %{?_without_tests:0}%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_project}1
Version:       %{github_version}
Release:       18%{?dist}
Summary:       A simple dependency injection container for PHP

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}/tree/1.1
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Autoload generation
BuildRequires: %{_bindir}/phpab
# Tests
%if %{with_tests}
BuildRequires: %{_bindir}/phpunit
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
## phpcompatinfo (computed from version 1.1.1)
BuildRequires: php-spl
%endif

Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 1.1.1)
Requires:      php-spl

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
Pimple is a small dependency injection container for PHP that consists of
just one file and one class.


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Generate autoloader
%{_bindir}/phpab --nolower --output lib/autoload.php lib


%install
mkdir -p %{buildroot}%{phpdir}/Pimple1
cp -pr lib/* %{buildroot}%{phpdir}/Pimple1/


%check
%if %{with_tests}
: Recreate test bootstrap
rm -f tests/bootstrap.php
%{_bindir}/phpab --nolower --output tests/bootstrap.php tests
cat >> tests/bootstrap.php <<'BOOTSTRAP'

require '%{buildroot}%{phpdir}/Pimple1/autoload.php';
BOOTSTRAP

: Run tests
%{_bindir}/phpunit
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc README.rst
%doc composer.json
%{phpdir}/Pimple1


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-16
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 22 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1.1-4
- Wrap tests' build requires in "%%if %%{with_tests}"

* Wed May 20 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1.1-3
- No rename and no conflict because the lib directory was changed from
  "%%{phpdir}/Pimple" to "%%{phpdir}/Pimple1".  This is possible because
  this library is not PSR-0 compliant so we can define whatever lib directory
  we want.

* Sun May 17 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1.1-2
- Add missing %%{_bindir}/phpab build dependency

* Sun May 17 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1.1-1
- Rename of php-Pimple version 1 to php-pimple1
