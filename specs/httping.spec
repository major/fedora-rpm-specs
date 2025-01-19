%global debug_package %{nil}

Name:           httping
Version:        3.6
Release:        2%{?dist}
Summary:        Ping alike tool for http requests

License:        GPL-1.0-or-later AND OpenSSL
URL:            https://github.com/folkertvanheusden/HTTPing/
Source0:        https://github.com/folkertvanheusden/HTTPing/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         9524733e67454518ee1075a47f3c21166543e620.patch
Patch1:         7f76370729c594180348f94feb4216fd14e12abd.patch

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  gettext
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  openssl-devel-engine

%description
Httping is like 'ping' but for HTTP requests. Give it an URL, and it will 
show you how long it takes to connect, send a request and retrieve the
reply (only the headers). Be aware that the transmission across the network
also takes time.

%prep
%autosetup -n HTTPing-%{version} -p1

%build
%cmake -DUSE_TUI=1 -DCMAKE_INSTALL_PREFIX=/usr
%cmake_build

%install
%cmake_install
rm -rf %{buildroot}/%{_docdir}

%files
%doc README.md plot-json.py
%license LICENSE
%{_bindir}/httping
%{_mandir}/httping.1

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Sep 28 2024 Fabian Affolter <mail@fabian-affolter.ch> - 3.6-1
- Update ot latest upstream release
- Fix rhbz#2300841

* Wed Aug 07 2024 Miroslav Suchý <msuchy@redhat.com> - 2.9-5
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jul 30 2023 Filipe Rosset <rosset.filipe@gmail.com> - 2.9-1
- Update to 2.9 fixes rhbz#2113442

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 2.5-13
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 06 2018 Fabian Affolter <mail@fabian-affolter.ch> - 2.5-5
- Fix BR

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 14 2017 Fabian Affolter <mail@fabian-affolter.ch> - 2.5-1
- Update to new upstream release 2.5

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 17 2015 Fabian Affolter <mail@fabian-affolter.ch> - 2.4-1
- Update to new upstream release 2.4

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 17 2014 Fabian Affolter <mail@fabian-affolter.ch> - 2.3.4-1
- Update to new upstream release 2.3.4

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 26 2013 Fabian Affolter <mail@fabian-affolter.ch> - 2.3.3-1
- Update to new upstream release 2.3.3

* Thu Feb 14 2013 Fabian Affolter <mail@fabian-affolter.ch> - 1.5.7-1
- Update to new upstream release 1.5.7

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Nov 10 2012 Fabian Affolter <mail@fabian-affolter.ch> - 1.5.5-1
- Update to new upstream release 1.5.5

* Sat Sep 29 2012 Fabian Affolter <mail@fabian-affolter.ch> - 1.5.4-1
- Update to new upstream release 1.5.4

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 19 2010 Dan Horák <dan[at]danny.cz> - 1.4.1-1
- Update to new upstream version 1.4.1

* Wed Sep  2 2009 Ville Skyttä <ville.skytta@iki.fi> - 1.3.1-2
- Fix -debuginfo (let rpmbuild strip the binary) - #520852

* Mon Aug 31 2009 Dan Horák <dan[at]danny.cz> - 1.3.1-1
- Update to new upstream version 1.3.1
- Update the strndup patch

* Thu Jul 16 2009 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.0-1
- Update to new upstream version

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 24 2009 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.9-3
- Change license to GPL+

* Tue Dec 30 2008 manuel "lonely wolf" wolfshant <wolfy@fedoraproject.org> - 1.2.9-2
- Remove duplicate definition of string functions
- Fix Makefile and use "make install"

* Mon Dec 29 2008 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.9-1
- Initial spec for Fedora
