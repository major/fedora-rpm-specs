Name:           ccrypt
Version:        1.10
Release:        28%{?dist}
Summary:        Secure encryption and decryption of files and streams

License:        GPLv2+
URL:            http://ccrypt.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

Patch0:         ccrypt-1.10-include_crypt_h.patch

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires: make

%description
ccrypt is a utility for encrypting and decrypting files and streams.
It was designed as a replacement for the standard unix crypt utility,
which is notorious for using a very weak encryption algorithm.

%prep
%autosetup -p 1

%build
%configure --disable-static
%make_build

%install
%make_install
%find_lang %{name}

%check
%make_build check

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README doc/cypfaq01.txt
%license COPYING
%{_mandir}/man*/*.*
%{_bindir}/cc*

%changelog
* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 1.10-19
- Rebuilt for libcrypt.so.2 (#1666033)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 06 2018 Fabian Affolter <mail@fabian-affolter.ch> - 1.10-17
- Fix BR

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 21 2018 Björn Esser <besser82@fedoraproject.org> - 1.10-15
- Add patch to include <crypt.h> if needed
- Minor improvements to spec file

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 1.10-14
- Rebuilt for switch to libxcrypt

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 25 2017 Fabian Affolter <mail@fabian-affolter.ch> - 1.10-11
- Update spec file

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Oct 07 2014 Fabian Affolter <mail@fabian-affolter.ch> - 1.10-7
- Update spec file

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 07 2013 Fabian Affolter <mail@fabian-affolter.ch> - 1.10-2
- Minor changes to match updated guidelines

* Sun Oct 21 2012 Fabian Affolter <mail@fabian-affolter.ch> - 1.10-1
- Update to new upstream version 1.10

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Nov 26 2011 Fabian Affolter <mail@fabian-affolter.ch> - 1.9-3
- Rebuilt

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Sep 17 2009 Fabian Affolter <mail@fabian-affolter.ch> - 1.9-1
- Updated to new upstream version 1.9

* Tue Jun 16 2009 Fabian Affolter <mail@fabian-affolter.ch> - 1.8-1
- Update to new upstream version 1.8

* Wed Apr 22 2009 Fabian Affolter <mail@fabian-affolter.ch> - 1.7-4
- Let check pass (on i386 only 3 of 4 tests are successful)

* Sun Mar 08 2009 Fabian Affolter <mail@fabian-affolter.ch> - 1.7-3
- Add check
- Add Patch for maketables

* Mon Feb 02 2009 Fabian Affolter <mail@fabian-affolter.ch> - 1.7-2
- Fix description

* Tue Jan 20 2009 Fabian Affolter <mail@fabian-affolter.ch> - 1.7-1
- Initial spec for Fedora

