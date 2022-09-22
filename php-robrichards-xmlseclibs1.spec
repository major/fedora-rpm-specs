#
# Fedora spec file for php-robrichards-xmlseclibs1
#
# Copyright (c) 2016-2020 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve the changelog entries
#

%global github_owner     robrichards
%global github_name      xmlseclibs
%global github_version   1.4.3
%global github_commit    03211d45fc71ef05bb0d6b3bd5f715da60d4a22c

%global composer_vendor  robrichards
%global composer_project xmlseclibs

# "php": ">= 5.2"
%global php_min_ver 5.2

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}1
Version:       %{github_version}
Release:       6%{?github_release}%{?dist}
Summary:       A PHP library for XML Security (version 1)

License:       BSD
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Tests
%if %{with_tests}
BuildRequires: php-composer(phpunit/phpunit)
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
## composer.json: optional
BuildRequires: php-mcrypt
BuildRequires: php-openssl
## phpcompatinfo (computed from version 1.4.3)
BuildRequires: php-dom
BuildRequires: php-hash
## Autoloader
BuildRequires: php-composer(theseer/autoload)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
# composer.json: suggest
Requires:      php-openssl
# phpcompatinfo (computed from version 1.4.3)
Requires:      php-dom
Requires:      php-hash

# Weak dependencies
%if 0%{?fedora} >= 21
## composer.json: suggest
Suggests:      php-mcrypt
%endif

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}


%description
xmlseclibs is a library written in PHP for working with XML Encryption and
Signatures.

NOTE: php-mcrypt will not be automatically installed as a dependency of this
package so it will need to be "manually" installed if it is required --
specifically for the following XMLSecurityKey encryption types:
- XMLSecurityKey::AES128_CBC
- XMLSecurityKey::AES192_CBC
- XMLSecurityKey::AES256_CBC
- XMLSecurityKey::TRIPLEDES_CBC

Autoloader: %{phpdir}/robrichards-xmlseclibs/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create autoloader
%{_bindir}/phpab --nolower --output src/autoload.php src


%install
mkdir -p %{buildroot}%{phpdir}/robrichards-xmlseclibs
cp -rp src/* %{buildroot}%{phpdir}/robrichards-xmlseclibs/


%check
%if %{with_tests}
: Use autoloader
sed 's#require.*xmlseclibs.*#require_once "%{buildroot}%{phpdir}/robrichards-xmlseclibs/autoload.php";#' \
    -i tests/*.phpt

: Skip tests known to fail
rm -f tests/extract-win-cert.phpt

: Disable deprecation warning with php 7.1
for test in tests/*phpt; do
  echo -e "\n--INI--\nerror_reporting=24575" >>$test
done

: Run tests
%{_bindir}/phpunit tests
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc CHANGELOG.txt
%doc composer.json
%doc README.md
%{phpdir}/robrichards-xmlseclibs


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Apr 05 2020 Shawn Iwinski <shawn@iwin.ski> - 1.4.3-1
- Update to 1.4.3 (RHBZ #1771533, CVE-2019-3465)
- https://nvd.nist.gov/vuln/detail/CVE-2019-3465

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov 25 2016 Remi Collet <remi@fedoraproject.org> - 1.4.2-2
- fix FTBFS, disable deprecation messages

* Sun Sep 11 2016 Shawn Iwinski <shawn@iwin.ski> - 1.4.2-1
- Updated to 1.4.2 (RHBZ #1374416)

* Thu Jul 14 2016 Shawn Iwinski <shawn@iwin.ski> - 1.4.1-2.20160518git2e20c8d
- Updated to latest 1.4 snapshot
- Moved php-openssl from weak dependency to hard dependency
- Added php-mcrypt weak dependency and added information to %%description about
  when it is required

* Sun Jul 10 2016 Shawn Iwinski <shawn@iwin.ski> - 1.4.1-1
- Initial package
