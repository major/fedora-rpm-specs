%{!?tcl_version: %define tcl_version %(echo 'puts $tcl_version' | tclsh)}
%{!?tcl_sitearch: %define tcl_sitearch %{_libdir}/tcl%{tcl_version}}

Name:           itk
Version:        4.1.0
Release:        13%{?dist}
Summary:        Object oriented extensions to Tk

License:        TCL
URL:            http://incrtcl.sourceforge.net/itcl/
Source0:        https://downloads.sourceforge.net/incrtcl/%{name}%{version}.tar.gz
Patch0:         itk-libdir.patch
Patch1:         itk-soname.patch
Patch2:         itcl4.0.0-linuxloading.patch
Patch4:         itk-tolowercase.patch

Requires:       tcl(abi) = 8.6 itcl tk
BuildRequires:  gcc
BuildRequires:  tk-devel itcl-devel
BuildRequires: make

%description
[incr Tk] is Tk extension that provides object-oriented features that are
missing from the Tk extension to Tcl.  The OO features provided by itk are
useful for building megawidgets.

%package devel
Summary:  Development headers and libraries for linking against itk
Requires:       %{name} = %{version}-%{release}
%description devel
Development headers and libraries for linking against itk.

%prep
%setup -q -n %{name}%{version}
%patch -P0 -p1 -b .libdir
%patch -P1 -p1 -b .soname
%patch -P2 -p1 -b .linuxloading
%patch -P4 -p1 -b .tolowercase

%build
%configure
%make_build

%install
%make_install


%files
%{_libdir}/*.so
%dir %{tcl_sitearch}/itk%{version}
%{tcl_sitearch}/%{name}%{version}/*.tcl
%{tcl_sitearch}/%{name}%{version}/*.itk
%{tcl_sitearch}/%{name}%{version}/tclIndex
%{_mandir}/mann/*.gz
%license license.terms

%files devel
%{_includedir}/*.h
# What happened to itk's stub library and itkConfig.sh?

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 18 2019 Orion Poplawski <orion@cora.nwra.com> - 4.1.0-1
- Update to 4.1.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 5 2015 Orion Poplawski <orion@cora.nwra.com> - 4.0.1-1
- Update to 4.0.1

* Thu Aug 28 2014 Dmitrij S. Kryzhevich <krege@land.ru> - 4.0.0-4
- Fix RHBZs #1116860, #1105506, #1116853.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Orion Poplawski <orion@cora.nwra.com> - 4.0.0-1
- Update to 4.0.0 for Tcl 8.6
- Cleanup spec

* Wed May 21 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 3.4-11
- Rebuilt for https://fedoraproject.org/wiki/Changes/f21tcl86

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 11 2009 Wart <wart@kobold.org> - 3.4-4
- Fix bad logic for locating itk.tcl from the C bindings (bz #485252)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb 9 2008 Wart <wart at kobold.org> - 3.4-2
- Rebuild for gcc 4.3
- Add patch to add soname to library

* Fri Jan 11 2008 Wart <wart at kobold.org> - 3.4-1
- Update to latest CVS head for tcl 8.5 compatibility

* Wed Dec 19 2007 Wart <wart at kobold.org> - 3.3-0.8.RC1
- Move libitk shared library to %%{_libdir} so that applications
  linked against itk can find it. (BZ #372791)

* Sun Aug 19 2007 Wart <wart at kobold.org> - 3.3-0.7.RC1
- License tag clarification
- Better download URL
- Clean up %%files section

* Wed Mar 28 2007 Wart <wart at kobold.org> - 3.3-0.6.RC1
- Rebuild for tcl 8.4 downgrade

* Thu Feb 8 2007 Wart <wart at kobold.org> - 3.3-0.5.RC1
- Rebuild for tcl 8.5a5

* Mon Aug 28 2006 Wart <wart at kobold.org> - 3.3-0.4.RC1
- Rebuild for Fedora Extras

* Thu Jun 1 2006 Wart <wart at kobold.org> - 3.3-0.3.RC1
- Fixed Requires: for -devel subpackage

* Wed Jan 11 2006 Wart <wart at kobold.org> - 3.3-0.2.RC1
- Fix quoting bug that is exposed by bash >= 3.1

* Mon Jan 9 2006 Wart <wart at kobold.org> - 3.3-0.1.RC1
- New itk package from newly separated itk upstream sources.
