Summary:	Remote control utility for Canon cameras
Name:		multican
Version:	0.0.5
Release:	31%{?dist}
Source0:	http://iweb.dl.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}-%{version}.tar.gz
URL:		http://multican.sourceforge.net/
License:	GPLv2
Patch0:		multican-usbid.patch
Patch1:		multican-gcc10.patch
BuildRequires: make
BuildRequires:  gcc
BuildRequires:	libusb-devel >= 0.1.12
Requires:	libusb >= 0.1.12

%description
Multican is Canon EOS class USB remote control utility for 300D, 350D,
30D, 20D and 5D. It is possible to control more of Canon cameras in
the same time up to six cameras attached. Multican allows scripted
remote control of multiple cameras.

%package devel
Summary: Development library for multican
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, libraries needed to develop
applications that use multican library to access Canon cameras.

%prep
%autosetup

%build
make CFLAGS="$RPM_OPT_FLAGS -fPIC"

%install
rm -rf $RPM_BUILD_ROOT
make	BINDIR="$RPM_BUILD_ROOT%{_bindir}" \
	LIBDIR="$RPM_BUILD_ROOT%{_libdir}" \
	INCLDIR="$RPM_BUILD_ROOT%{_includedir}" \
	install

%ldconfig_scriptlets

%files
%doc COPYING README
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%doc TODO ChangeLog
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Jindrich Novy <jnovy@redhat.com> - 0.0.5-25
- upload the proper upstream tarball
- fix build with gcc-10

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 10 2009 Jindrich Novy <jnovy@redhat.com> 0.0.5-8
- add IDs for EOS 5D Mark II and 450D
- fix source URL

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Aug 02 2008 Jindrich Novy <jnovy@redhat.com> 0.0.5-5
- fix source URL

* Mon Feb 25 2008 Jindrich Novy <jnovy@redhat.com> 0.0.5-4
- manual rebuild because of gcc-4.3 (#434191)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.0.5-3
- Autorebuild for GCC 4.3

* Thu Aug 23 2007 Jindrich Novy <jnovy@redhat.com> 0.0.5-2
- update License
- rebuild for BuildID

* Tue Feb 20 2007 Jindrich Novy <jnovy@redhat.com> 0.0.5-1
- update to 0.0.5
- new devel package now provides shared library and headers

* Sun Dec 17 2006 Jindrich Novy <jnovy@redhat.com> 0.0.4-2
- rebuild to avoid EVR problems with FC5 multican

* Tue Nov 07 2006 Jindrich Novy <jnovy@redhat.com> 0.0.4-1
- initial build
