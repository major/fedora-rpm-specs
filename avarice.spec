Name:           avarice
Version:        2.13
Release:        17%{?dist}
Summary:        Program for interfacing the Atmel JTAG ICE to GDB

License:        GPLv2
URL:            http://sourceforge.net/projects/avarice
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Patch0:		%{name}-2.13-pragma.patch
Patch1:		%{name}-2.13-uchar.patch

BuildRequires:  gcc-c++
BuildRequires:  binutils-static, libusb-devel
BuildRequires:  perl-interpreter
BuildRequires: make

%description
Program for interfacing the Atmel JTAG ICE to GDB to allow users to
debug their embedded AVR target

%prep
%setup -q
%patch0 -p1 -b .pragma
%patch1 -p1 -b .uchar


%build
export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
export LIBS="-ldl"
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT


%files
%doc AUTHORS ChangeLog NEWS
%license COPYING
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*


%changelog
* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Jeff Law <law@redhat.com> - 2.13-12
- Force C++14 as the code is not ready for C++17

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 27 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.13-3
- Add BR: perl (F26FTBFS, RHBZ#1423193)
- Introduce %%license.
- Modernize spec.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 18 2016 Lucian Langa <lucilanga@gnome.eu.org> - 2.13-1
- cleanup spec file
- add compilation fixes patches
- update to latest upstream

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 20 2011 Lucian Langa <cooly@gnome.eu.org> - 2.12-1
- drop patch - fixed upstream
- new upstream release

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 01 2010 Lucian Langa <cooly@gnome.eu.org> - 2.10-5
- use binutils-static in BR (#609858)

* Tue Jun 22 2010 Lucian Langa <cooly@gnome.eu.org> - 2.10-4
- use upstream patch0 to fix gcc issues

* Tue Jun 22 2010 Lucian Langa <cooly@gnome.eu.org> - 2.10-3
- bump rel to have a clean upgrade path

* Tue Jun 22 2010 Lucian Langa <cooly@gnome.eu.org> - 2.10-2
- add libusb-devel as BR (#483709)

* Fri Jan 29 2010 Lucian Langa <cooly@gnome.eu.org> - 2.10-1
- new upstream release

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jul 14 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.6-3
- fix license tag

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.6-2
- Autorebuild for GCC 4.3

* Mon Mar 12 2007 Trond Danielsen <trond.danielsen@fedoraproject.org> - 2.6-1
- Initial version.
