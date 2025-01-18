Name: cpl
Version: 7.3.2
Release: 9%{?dist}
Summary: ESO library for automated astronomical data-reduction tasks

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: http://www.eso.org/sci/software/cpl/
Source: https://ftp.eso.org/pub/dfs/pipelines/libraries/cpl/%{name}-%{version}.tar.gz
Patch0: cpl-i386.patch

BuildRequires: gcc
BuildRequires: make
BuildRequires: cfitsio-devel >= 3.450
BuildRequires: wcslib-devel >= 4.24
BuildRequires: fftw-devel > 3.3.4

%description
The Common Pipeline Library (CPL) comprises a set of ISO-C libraries 
that provide a comprehensive, efficient and robust software toolkit. 
It forms a basis for the creation of automated astronomical data-reduction 
tasks (known as "pipelines") for ESO (European Southern Observatory) 
instruments. The CPL was developed to standardize the way 
VLT (Very Large Telescope) instrument pipelines are built, 
to shorten their development cycle and to ease their maintenance. 

%package devel
Summary: Libraries, includes, etc. used to develop an application with %{name}
Requires: %{name} = %{version}-%{release}
%description devel
These are the header files and libraries needed to develop a %{name}
application

%prep
%setup -q
%patch 0 -p1

%build
%configure --disable-static
# http://fedoraproject.org/wiki/PackagingGuidelines#Beware_of_Rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%ldconfig_scriptlets

%files
%doc AUTHORS BUGS COPYING NEWS
%license COPYING 
%{_libdir}/*so.*

%files devel
%doc README
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/cext.pc

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 7.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 7.3.2-8
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 09 2024 Sergio Pascual <sergiopr@fedoraproject.org> - 7.3.2-6
- Rebuilt to fix rhbz#2260903

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 09 2024 Sergio Pascual <sergiopr@fedoraproject.org> - 7.3.2-3
- Rebuilt for wcslib 8.2

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Apr 30 2023 Sergio Pascual <sergiopr@fedoraproject.org> - 7.3.2-1
- New upstream source (7.3.2)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 29 2022 Maxwell G <gotmax@e.email> - 7.2.3-2
- Rebuild for cfitsio 4.2

* Wed Dec 28 2022 Sergio Pascual <sergiopr@fedoraproject.org> - 7.2.3-1
- New upstream source (7.2.3)

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Sergio Pascual <sergiopr@fedoraproject.org> - 7.2.2-1
- New upstream source (7.2.2)

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct 07 2021 Sergio Pascual <sergiopr@fedoraproject.org> - 7.1.4-1
- New upstream source (7.1.4)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Feb 16 2021 Sergio Pascual <sergiopr@fedoraproject.org> - 7.1.3-1
- New upstream source (7.1.3)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Mar 19 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 7.1.2-3
- EVR bump for rebuild (wcslib 7)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 16 2019 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 7.1.2-1
- Update to 7.1.2 (#1742085)

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 25 2019 Sergio Pascual <sergiopr@fedoraproject.org> - 7.1.1-1
- New upstream source (7.1.1)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 03 2018 Sergio Pascual <sergiopr@fedoraproject.org> - 7.1-1
- New upstream source
- Patch to fix problems in i386 with SSE2 enabled

* Tue Aug 21 2018 Sergio Pascual <sergiopr@fedoraproject.org> - 7.0-11
- EVR bump for rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat May 26 2018 Christian Dersch <lupinix@mailbox.org> - 7.0-9
- rebuilt for cfitsio 3.450

* Fri Feb 23 2018 Christian Dersch <lupinix@mailbox.org> - 7.0-8
- rebuilt for cfitsio 3.420 (so version bump)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Apr 18 2016 Sergio Pascual <sergiopr@fedoraproject.org> - 7.0-3
- Upload the source...

* Thu Apr 14 2016 Sergio Pascual <sergiopr@fedoraproject.org> - 7.0-2
- EVR bump to rebuild with new wcslib

* Wed Apr 06 2016 Sergio Pascual <sergiopr@fedoraproject.org> - 7.0-1
- New upstream source 7.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 03 2015 Sergio Pascual <sergiopr@fedoraproject.org> - 6.6.1-1
- New upstream source 6.6.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 13 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 6.4.2-1
- New upstream source 6.4.2

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 09 2014 Sergio Pascual <sergiopr@fedoraproject.org> 6.3.1-3
- Rebuilt for new cfitsio (3.360)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 16 2013 Sergio Pascual <sergiopr@fedoraproject.org> - 6.3.1-1
- New upstream source 6.3.1
- EVR bump to rebuild with new cfitsio 3.350

* Sat Mar 23 2013 Sergio Pascual <sergiopr@fedoraproject.org> - 6.2-2
- EVR bump to rebuild with new cfitsio 3.340

* Thu Feb 14 2013 Sergio Pascual <sergiopr@fedoraproject.org> - 6.2-1
- New upstream source 6.2
- Updated URL and Source0 URL
- Merged patches

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jan 18 2012 Sergio Pascual <sergiopr at fedoraproject.org> - 5.3.1-4
- Using system fftw libraries

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Aug 24 2011 Sergio Pascual <sergiopr at fedoraproject.org> - 5.3.1-2
- Rebuilt to match new wcslib 4.8

* Thu Mar 17 2011 Sergio Pascual <sergiopr@fedoraproject.org> - 5.3.1-1
- New upstream source

* Wed Feb 23 2011 Sergio Pascual <sergiopr at fedoraproject.org> - 5.2.0-4
- Rebuilt to match new wcslib 4.7

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Nov 10 2010 Sergio Pascual <sergiopr at fedoraproject.org> - 5.2.0-4
- Rebuilt to match new wcslib 4.6.3

* Wed Nov 10 2010 Sergio Pascual <sergiopr at fedoraproject.org> - 5.2.0-3
- Rebuilt to match new wcslib 4.5.6

* Fri May 21 2010 Sergio Pascual <sergiopr at fedoraproject.org> - 5.2.0-2
- New upstream source

* Wed Mar 10 2010 Sergio Pascual <sergiopr at fedoraproject.org> - 5.0.1-3
- Rebuilt to match new cfitsio 3.240

* Tue Nov 03 2009 Sergio Pascual <sergiopr at fedoraproject.org> - 5.0.1-2
- Rebuilt for cfitsio-3.210-2

* Wed Oct 28 2009 Sergio Pascual <sergiopr at fedoraproject.org> - 5.0.1-1
- New upstream source

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May 08 2009 Sergio Pascual <sergiopr at fedoraproject.org> 4.2.0-3
- Enabled wcslib support

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 18 2008 Sergio Pascual <sergiopr at fedoraproject.org> 4.2.0-1
- New upstream source

* Sun Apr 06 2008 Sergio Pascual <sergiopr at fedoraproject.org> 4.1.0-1
- New upstream source

* Sat Feb 09 2008 Sergio Pascual <sergiopr at fedoraproject.org> 4.0.1-2
- Updated upstream sources.
- Fixing multilib bug (bz#340941)

* Tue Oct 09 2007 Sergio Pascual <sergiopr at fedoraproject.org> 3.1-2
- Updated qfits patch to build in 64 bits systems

* Tue Sep 25 2007 Sergio Pascual <sergiopr at fedoraproject.org> 3.1-1
- Minor changes

* Thu Sep 13 2007 Sergio Pascual <sergiopr at fedoraproject.org> 3.1-0.3
- Updated license tag

* Thu May 03 2007 Sergio Pascual <sergiopr at fedoraproject.org> 3.1-0.2
- Added dir for recipes.

* Thu Apr 26 2007 Sergio Pascual <sergiopr at fedoraproject.org> 3.1-0.1
- Initial spec file.
