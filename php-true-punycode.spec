# remirepo/fedora spec file for php-true-punycode
#
# Copyright (c) 2015-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%bcond_without tests

%global gh_commit    a4d0c11a36dd7f4e7cd7096076cab6d3378a071e
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     true
%global gh_project   php-punycode

Name:           php-true-punycode
Version:        2.1.1
Release:        18%{?dist}
Summary:        A Bootstring encoding of Unicode for IDNA

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
BuildRequires:  php(language) >= 5.3
BuildRequires:  php-mbstring
BuildRequires:  %{_bindir}/phpunit
BuildRequires:  php-fedora-autoloader-devel

# From composer.json
#               "symfony/polyfill-mbstring": "^1.3",
#               "php": ">=5.3.0"
Requires:       php(language) >= 5.3
# Simpler, and we don't want symfony/polyfill-mbstring
Requires:       php-mbstring
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(true/punycode) = %{version}


%description
A Bootstring encoding of Unicode for Internationalized Domain Names
in Applications (IDNA).

Autoloader: %{_datadir}/php/TrueBV/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
: Generate a classmap autoloader
%{_bindir}/phpab --template fedora --output src/autoload.php src


%install
mkdir -p   %{buildroot}%{_datadir}/php
cp -pr src %{buildroot}%{_datadir}/php/TrueBV


%check
%if %{with tests}
mkdir vendor
ln -s %{buildroot}%{_datadir}/php/TrueBV/autoload.php vendor/autoload.php

# testEncodeUppercase affected by IDNA2003/2008 changes
: Run test suite
ret=0
for cmd in php php72 php73 php74 php80; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit \
      --filter '^((?!(testEncodeUppercase)).)*$' \
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
%{_datadir}/php/TrueBV


%changelog
* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-13
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 11 2020 Remi Collet <remi@remirepo.net> - 2.1.1-11
- cleanup

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 16 2018 Remi Collet <remi@fedoraproject.org> - 2.1.1-6
- skip 1 test failing with PHP 7.3 reported as
  https://github.com/true/php-punycode/issues/29

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 16 2016 Remi Collet <remi@fedoraproject.org> - 2.1.1-1
- update to 2.1.1 (no change)
- switch to fedora/autoloader

* Wed Aug 10 2016 Remi Collet <remi@fedoraproject.org> - 2.1.0-1
- update to 2.1.0
- add autoloader

* Wed May 25 2016 Remi Collet <remi@fedoraproject.org> - 2.0.3-1
- update to version 2.0.3 (no change)
- use git snapshot for sources with tests

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan  8 2016 Remi Collet <remi@fedoraproject.org> - 2.0.2-1
- update to version 2.0.2

* Wed Sep  2 2015 Remi Collet <remi@fedoraproject.org> - 2.0.1-1
- update to version 2.0.1 (no change)

* Sun Aug  9 2015 Remi Collet <remi@fedoraproject.org> - 2.0.0-1
- update to version 2.0.0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 18 2015 Remi Collet <remi@fedoraproject.org> - 1.1.0-1
- update to version 1.1.0

* Wed Jan  7 2015 Remi Collet <remi@fedoraproject.org> - 1.0.1-1
- initial package
