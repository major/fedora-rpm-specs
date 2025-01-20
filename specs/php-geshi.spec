Name:           php-geshi
Summary:        Generic syntax highlighter
License:        GPL-2.0-or-later

%global git_commit 7884d22244c6d2de5ac7ffd919ce4add02b36e66
%global git_date 20230219
%global git_short %(c="%{git_commit}"; echo "${c:0:7}")

Version:        1.0.9.1
Release:        18.%{git_date}git%{git_short}%{?dist}

URL:            https://github.com/GeSHi/geshi-1.0
Source0:        %{url}/archive/%{git_commit}/GeSHi-%{git_commit}.tar.gz

# Some of the project files do not pass tests, fix those
Patch1:         0001-fix-LangCheckTest-failures.patch

BuildArch:      noarch

%if 0%{?fedora}
BuildRequires:  phpunit8
%endif
BuildRequires:  php-mbstring
BuildRequires:  php-pcre

Requires:       php-mbstring
Requires:       php-pcre

Provides:       php-composer(geshi/geshi) = %{version}

%description
GeSHi aims to be a simple but powerful highlighting class,
with the following goals:
    * Support for a wide range of popular languages
    * Easy to add a new language for highlighting
    * Highly customisable output formats


%prep
%autosetup -p1 -n geshi-1.0-%{git_commit}

find docs -type f -exec chmod a-x {} ';'
find . -type f -name "*.php" -exec chmod a-x {} ';'


%build
# Nothing to build


%install
mkdir -p %{buildroot}%{_datadir}/php/
cd src
cp -a geshi geshi.php %{buildroot}%{_datadir}/php/


%check
%if 0%{?fedora}
phpunit8 --verbose
%endif


%files
%license LICENSE
%doc BUGS CHANGELOG README.md THANKS
%doc docs/* contrib/
%doc composer.json
%{_datadir}/php/geshi.php
%{_datadir}/php/geshi/


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9.1-18.20230219git7884d22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9.1-17.20230219git7884d22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 25 2024 Christian Krause <chkr@fedoraproject.org> - 1.0.9.1-16.20230219git7884d22
- Disable tests on EPEL (required package phpunit8 not available)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9.1-15.20230219git7884d22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9.1-14.20230219git7884d22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9.1-13.20230219git7884d22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Apr 24 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.0.9.1-12.20230219git7884d22
- Update to latest git snapshot
- Drop Patch0 (now included upstream)
- Migrate License tag to SPDX

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 29 2021 Artur Iwicki <fedora@svgames.pl> - 1.0.9.1-8
- Add Patch2: fix test failures (fixes rhbz#1987813)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Artur Iwicki <fedora@svgames.pl> - 1.0.9.1-5
- Backport a bugfix required by dokuwiki

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 14 2019 Remi Collet <remi@remirepo.net> - 1.0.9.1-2
- provides php-composer(geshi/geshi)
- run upstream test suite

* Mon Oct 21 2019 Artur Iwicki <fedora@svgames.pl> - 1.0.9.1-1
- Update to version 1.0.9.1
- Drop PHP 7.2 deprecation warning patch (merged upstream)

* Fri Oct 04 2019 Xavier Bachelot <xavier@bachelot.org> - 1.0.9.0-1
- Update to 1.0.9.0.
- Clean up specfile.
- Add upstream patch to fix a php 7.2 deprecation warning.
  (Thanks Artur Iwicki)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8.11-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr 10 2013 Xavier Bachelot <xavier@bachelot.org> 1.0.8.11-3
- Bump release for rebuild.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Aug 21 2012 Xavier Bachelot <xavier@bachelot.org> 1.0.8.11-1
- Update to 1.0.8.11.
- Fix remote directory traversal and information disclosure bug.
  (CVE-2012-3521)(RHBZ#850425).
- Fix Requires (RHBZ#848699).

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 28 2011 Xavier Bachelot <xavier@bachelot.org> 1.0.8.10-1
- Update to 1.0.8.10.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jun 15 2010 Xavier Bachelot <xavier@bachelot.org> 1.0.8.8-1
- Update to 1.0.8.8.
- Fix Source0: URL, upstream changed tarball name.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr 15 2009 Xavier Bachelot <xavier@bachelot.org> 1.0.8.3-1
- Update to 1.0.8.3.

* Thu Mar 26 2009 Xavier Bachelot <xavier@bachelot.org> 1.0.8.2-3
- License is actually GPLv2+.
- Remove implicit R: php-common.
- Fix URL:.

* Thu Mar 26 2009 Xavier Bachelot <xavier@bachelot.org> 1.0.8.2-2
- More Requires:.

* Thu Mar 19 2009 Xavier Bachelot <xavier@bachelot.org> 1.0.8.2-1
- Initial build.
