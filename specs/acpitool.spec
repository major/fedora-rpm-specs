Summary: Command line ACPI client
Name: acpitool
Version: 0.5.1
Release: 36%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: https://sourceforge.net/projects/acpitool/
BuildRequires: gcc-c++
BuildRequires: make

Source0:	https://sourceforge.net/projects/acpitool/files/acpitool/%{version}/acpitool-%{version}.tar.bz2
Patch0:		ac_adapter.patch
Patch1:		battery.patch
Patch2:		kernel3.patch
Patch3:		wakeup.patch
Patch4:		var-line.patch
Patch5:		typos.patch
Patch6:		cleanup.patch
Patch7:		cache-size.patch

%description
AcpiTool is a Linux ACPI client. It's a small command line application, 
intended to be a replacement for the apm tool. Besides "basic" ACPI 
information like battery status, AC presence, putting the laptop to
sleep, Acpitool also supports various extensions for Toshiba, Asus and 
IBM Thinkpad laptops, allowing you to change the LCD brightness level, 
toggle fan on/off, and more. 


%prep
%setup -q
%patch -P0 -p1 -b .ac_adapter
%patch -P1 -p1 -b .battery
%patch -P2 -p1 -b .kernel3
%patch -P3 -p1 -b .wakeup
%patch -P4 -p1 -b .var-line
%patch -P5 -p1 -b .typos
%patch -P6 -p1 -b .cleanup
%patch -P7 -p1 -b .cache-size

%build
%configure
make %{?_smp_mflags}

%install
rm -fr $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc AUTHORS ChangeLog COPYING INSTALL README TODO
%{_bindir}/acpitool
%{_mandir}/man1/acpitool*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.5.1-35
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-25
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 28 2019 Al Stone <ahs3@redhat.com> - 0.5.1-21
- Cache size was being reported incorrectly (cpufreq was being used
  instead).  Pulled in patch submitted with bug report once verified.
  Closes BZ#1701278.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 26 2018 Al Stone <ahs3@redhat.com> - 0.5.1-19
- Remove commented out acpitool-0.5-gcc43.patch; it's no longer needed and
  just clutters up the spec file
- Merge in patches from Debian (Arch uses very similar but not exactly
  identical nor as extensive patches).  Closes BZ#1625002.
- Add a new patch to clean up g++ warning about implicit casts
- Fixed upstream to more recent location on sf.net

* Mon Jul 23 2018 Al Stone <ahs3@redhat.com> - 0.5.1-18
- Add in BuildRequires for C++.  Closes BZ1603341.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.5.1-10
- Rebuilt for GCC 5 C++11 ABI change

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-4
- Rebuilt for c++ ABI breakage

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 26 2009 Steven M. Parrish <smparrish@gmail.com> 0.5.1-1
- various minor fixes (fixing memleaks, removing of limit on thermal zones)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Sep 18 2008 Patrice Dumas <pertusus@free.fr> 0.5-1
- update to 0.5

* Mon Jul 14 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.4.7-5
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.4.7-4
- Autorebuild for GCC 4.3

* Thu Jan  3 2008 Patrice Dumas <pertusus@free.fr> 0.4.7-3
- fixes for gcc 4.3

* Thu May 24 2007 Patrice Dumas <pertusus@free.fr> 0.4.7-2
- update to 0.4.7

* Fri Oct  6 2006 Patrice Dumas <pertusus@free.fr> 0.4.6-2
- set Group to Applications/System (fix #209230)

* Mon Aug 28 2006 Patrice Dumas <pertusus@free.fr> 0.4.6-1
- update to 0.4.6

* Sun May 21 2006 Patrice Dumas <pertusus@free.fr> 0.4.5-1
- update to 0.4.5

* Thu Feb 16 2006 Patrice Dumas <pertusus@free.fr> 0.4.4-1.1
- new version
- remove now unneeded patch

* Thu Nov 10 2005 Patrice Dumas <pertusus@free.fr> 0.3.0-3
- add patch to avoid ignoring CXXFLAGS

* Fri Nov  4 2005 Patrice Dumas <pertusus@free.fr> 0.3.0-2
- update using fedora core conventions, some cleanings

* Tue Aug 24 2004 Robert Ambrose <rna@muttsoft.com>
- Created .spec file.

