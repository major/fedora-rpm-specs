Name:           lib765
Version:        0.4.2
Release:        32%{?dist}
Summary:        A library for emulating the uPD765a floppy controller
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://www.seasip.demon.co.uk/Unix/LibDsk
Source0:        http://www.seasip.demon.co.uk/Unix/LibDsk/%{name}-%{version}.tar.gz
BuildRequires: libtool
BuildRequires: gettext
BuildRequires: libdsk-devel
BuildRequires: make

%description
A library for emulating the uPD765a floppy controller as found on the Spectrum
+3, Amstrad CPC and PCW.


%package devel
Summary:    Development files for lib765
Requires:   libdsk-devel
Requires:   %{name} = %{version}-%{release}

%description devel
Development files for lib765.


%prep
%setup -q


%build
#shiped libtool stuff seems broken on x86_64
autoreconf -if
%configure --disable-static
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
find %{buildroot} -name \*\.la -print | xargs rm -f


%ldconfig_scriptlets



%files
%doc ChangeLog
%{_libdir}/lib765.so.*


%files devel
%doc doc/COPYING.LIB doc/765.txt
%{_libdir}/lib765.so
%{_includedir}/765.h


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 0.4.2-31
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 13 2021 Lucian Langa <lucilanga@gnome.eu.org> - 0.4.2-22
- rebuilt for newer libdsk

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 10 2019 Lucian Langa <lucilanga@gnome.eu.org> - 0.4.2-17
- rebuilt for newer libdsk

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 07 2010 Lucian Langa <cooly@gnome.eu.org> - 0.4.2-1
- misc cleanups
- new upstream release

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jun  6 2008 Lucian Langa <cooly@gnome.eu.org> - 0.4.1-4
- Fix for x86_64 builds #449513
- Misc cleanups

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.4.1-3
- Autorebuild for GCC 4.3

* Wed Aug 22 2007 Ian Chapman <packages@amiga-hardware.com> 0.4.1-2
- Release bump for F8 mass rebuild
- Further license clarifications

* Fri Aug 10 2007 Ian Chapman <packages@amiga-hardware.com> 0.4.1-1
- Upgrade to 0.4.1
- Updated license field due to new guidelines

* Thu Jul 05 2007 Ian Chapman <packages@amiga-hardware.com> 0.4.0-1
- Upgrade to 0.4.0
- 'Escaped' several macros in the changelogs
- Corrected summary for devel package

* Sat Sep 16 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.3.4-2
- rebuild

* Sun Apr 02 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.3.4-1
- Bump to new version

* Fri Mar 10 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.3.3-6
- Minor tweak to the spec file

* Thu Mar 9 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.3.3-5
- Bug in the spec file means it didn't compile.

* Tue Mar 7 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.3.3-4
- Added Require for devel package

* Mon Nov 14 2005 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.3.3-3
- now uses %%{?_smp_mflags} during the make process

* Fri Nov 11 2005 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.3.3-2
- renamed spec file

* Fri Nov 11 2005 Paul Howarth <paul@city-fan.org> - 0.3.3-2
- Removed vendor and packager tags
- Use FE standard buildroot
- Unpack tarball quietly
- Remove BuildRoot in %%install rather than %%prep
- Use DESTDIR with make instead of %%makeinstall
- Don't build static lubs
- Add libdsk-devel dep for -devel subpackage

* Mon Oct 17 2005 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 0.3.3-1.2
- Many alterations to bring the spec into line with the rules
- removed *.la files, changes to rpm name and changed to %%configure

* Mon Jul 11 2005 Paul Johnson <paul@all-the-johnsons.co.uk> - 0.3.3-1.1.FC4
- Changed version for FC4

* Mon Feb 28 2005 Ian Chapman <packages@amiga-hardware.com> - 0.3.3-1.iss
- Changelog was duplicated in spec file, fixed.
- Updated to version 0.3.3

* Mon Jul 16 2004 Ian Chapman <packages@amiga-hardware.com> - 0.3.1.1-3.iss
- Updated to Fedora Core 2

* Fri Dec 05 2003 Ian Chapman <packages@amiga-hardware.com> - 0.3.1.1-2
- Minor changes to changelog
- Moved a file from the main package to the devel package
- Improved use of macros

* Sat Dec 01 2003 Ian Chapman <packages@amiga-hardware.com> - 0.3.1.1-1
- Initial Release
