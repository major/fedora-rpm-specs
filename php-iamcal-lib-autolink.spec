# spec file for php-iamcal-lib-autolink
#
# Copyright (c) 2016-2017 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    b3a86d8437e5d635fb85b155a86288d94f6a924d
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     iamcal
%global gh_project   lib_autolink
%global with_tests   0%{!?_without_tests:1}


Name:           php-iamcal-lib-autolink
Version:        1.7
Release:        14%{?dist}
Summary:        Adds anchors to urls in a text

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
# Used to retrieve a git snapshot with test suite
Source1:        makesrc.sh

BuildArch:      noarch
# For tests
%if %{with_tests}
BuildRequires:  php-cli
BuildRequires:  php-pcre
%endif

# From composer.json, nothing
# From phpcompatinfo report for 1.7
Requires:       php-pcre

Provides:       php-composer(%{gh_owner}/%{gh_project}) = %{version}


%description
Find URLs in HTML that are not already links, and make them into links.

Autoloader: %{_datadir}/php/%{name}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
: Nothing


%install
: Single file, only functions
install -Dpm 0644 lib_autolink.php %{buildroot}%{_datadir}/php/%{name}/lib_autolink.php

# from composer.json, "autoload": {
#    "files": ["lib_autolink.php"]
ln -s lib_autolink.php %{buildroot}%{_datadir}/php/%{name}/autoload.php


%check
%if %{with_tests}
sed -e 's/\$this/$thiz/' -i t/testmore.php

for cmd in php php56 php70 php71 php72; do
  if which $cmd; then
    for unit in t/*.t; do
      $cmd $unit | tee -a tests.log
    done
  fi
done

grep -q '^not ok' tests.log && exit 1 || exit 0
%else
: Test suite disabled
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json
%{_datadir}/php/%{name}


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Oct  5 2017 Remi Collet <remi@fedoraproject.org> - 1.7-4
- fix tests for recent PHP, FTBFS from Koschei

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Apr 26 2016 Remi Collet <remi@fedoraproject.org> - 1.7-1
- initial package, version 1.7

