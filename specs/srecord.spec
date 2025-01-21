Name:		srecord
Version:	1.65.0
Release:	4%{?dist}
Summary:	Manipulate EPROM load files
License:	GPL-3.0-or-later AND LGPL-3.0-or-later
# see also https://github.com/sierrafoxtrot/srecord
URL:		http://srecord.sourceforge.net/
Source0:	http://downloads.sourceforge.net/srecord/srecord-%{version}-Source.tar.gz
# https://github.com/sharkcz/srecord/tree/fedora-1.65
# - switch to a shared library with a sane name
# - don't install runtime deps
Patch0:		srecord-1.65-fedora.patch
BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	git-core
BuildRequires:	libgcrypt-devel
# for building docs
BuildRequires:	doxygen
BuildRequires:	ghostscript
BuildRequires:	groff
BuildRequires:	netpbm-progs
BuildRequires:	psutils

%description
The SRecord package is a collection of powerful tools for manipulating
EPROM load files.

- The SRecord package understands a number of file formats: Motorola
  S-Record, Intel, Tektronix, Binary.  These file formats may be read
  and written.  Also C array definitions, for output only.

- The SRecord package has a number of tools: srec_cat for copying and
  and converting files, srec_cmp for comparing files and srec_info for
  printing summaries.

- The SRecord package has a number for filters: checksum to add checksums
  to the data, crop to keep address ranges, exclude to remove address
  ranges, fill to plug holes in the data, length to insert the data
  length, maximum to insert the data address maximum, minimum to insert
  the data address minimum, offset to adjust addresses, and split for
  wide data buses and memory striping.

More than one filter may be applied to each input file.  Different filters
may be applied to each input file.  All filters may be applied to all
file formats.

%package devel
Summary:	Development headers and libraries for srecord
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Development headers and libraries for developing applications against
srecord.


%prep
%autosetup -p1 -n %{name}-%{version}-Source


%build
%cmake
%cmake_build


%install
%cmake_install

# the generated html docs are huge and unlikely to be used ...
rm -rf %{buildroot}%{_defaultdocdir}/%{name}/htdocs


%check
%ctest


%files
%license LICENSE
%{_defaultdocdir}/%{name}/
%{_bindir}/srec_*
%{_libdir}/lib%{name}.so.%{version}
%{_mandir}/man1/srec_*.1*
%{_mandir}/man3/%{name}*.3*
%{_mandir}/man5/srec_*.5*

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.65.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.65.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.65.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Aug 15 2023 Dan Horák <dan[at]danny.cz> - 1.65.0-1
- update to 1.65

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.64-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.64-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.64-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.64-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.64-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.64-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.64-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.64-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.64-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.64-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.64-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.64-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.64-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.64-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.64-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 1.64-10
- Rebuilt for Boost 1.63

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.64-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 1.64-8
- Rebuilt for Boost 1.60

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.64-7
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.64-6
- rebuild for Boost 1.58

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.64-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.64-4
- Rebuilt for GCC 5 C++11 ABI change

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 1.64-3
- Rebuild for boost 1.57.0

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.64-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 23 2014 Tom Callaway <spot@fedoraproject.org> - 1.64-1
- update to 1.64

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.63-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 1.63-2
- Rebuild for boost 1.55.0

* Mon Apr 14 2014 Tom Callaway <spot@fedoraproject.org> - 1.63-1
- update to 1.63

* Fri Aug 16 2013 Tom Callaway <spot@fedoraproject.org> - 1.62-4
- use unversioned docdir

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.62-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 1.62-2
- Rebuild for boost 1.54.0

* Fri Jun  7 2013 Tom Callaway <spot@fedoraproject.org> - 1.62-1
- update to 1.62

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.61-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan  7 2013 Tom Callaway <spot@fedoraproject.org> - 1.61-1
- update to 1.61

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.60-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 25 2012 Tom Callaway <spot@fedoraproject.org> - 1.60-1
- update to 1.60

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.57-3
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.57-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Jun 11 2011 Tom Callaway <spot@fedoraproject.org> 1.57-1
- update to 1.57

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.56-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 29 2010 jkeating - 1.56-2
- Rebuilt for gcc bug 634757

* Sat Sep 18 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 1.56-1
- update to 1.56

* Thu Jul 15 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 1.55-2
- BuildRequires: libtool

* Thu Jul 15 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 1.55-1
- update to 1.55

* Fri Jan 29 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 1.54-1
- update to 1.54, adds library

* Thu Nov 12 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.53-1
- update to 1.53

* Sat Sep 12 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.51-1
- Update to 1.51

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.50-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 10 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.50-2
- add BuildRequires: libgcrypt-devel

* Fri Jul 10 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.50-1
- update to 1.50

* Wed Mar  4 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.47-1
- update to 1.47

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.46-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 16 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.46-2
- fix gcc 4.4 compile issues (cstdio)

* Tue Jan 13 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.46-1
- update to 1.46

* Thu Nov 20 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.45-1
- update to 1.45

* Tue Mar 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.39-2
- BR: boost-devel

* Mon Mar 10 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.39-1
- update to 1.39

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.36-2
- Autorebuild for GCC 4.3

* Sat Aug 11 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.36-1
- Update to 1.36.
- License: GPLv3+.

* Sat Jun 23 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.35-1
- Update to 1.35.

* Tue May 22 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.33-1
- Update to 1.33.

* Tue Apr 24 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.32-1
- Update to 1.32.

* Thu Apr  5 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.31-1
- Update to 1.31.

* Fri Mar 23 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.30-1
- Update to 1.30.

* Tue Mar 13 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.29-1
- Update to 1.29.

* Thu Mar  8 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.28-1
- Update to 1.28.

* Wed Jan 31 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.27-1
- Update to 1.27.

* Sun Sep 10 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.26-2
- Rebuild for FC6.

* Tue Jun 20 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.26-1
- Update to 1.26.

* Wed Mar  8 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.24-1
- Update to 1.24.

* Wed Feb 15 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.23-2
- Rebuild.

* Fri Sep 23 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.23-1
- Update to 1.23.

* Thu Sep 15 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.22-2
- Updated the source tarball (PATCHLEVEL "1.22.D002").
  The author repackages updates without changing the tarball version (ARGH!).

* Mon Sep 12 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.22-1
- Update to 1.22.

* Sun Aug  7 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.21-1
- Version 1.21.
