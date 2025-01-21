# We used to define this dynamically, but the Fedora buildsystem chokes on
# using this for the versioned Requires on tcl(abi), so we hardcode it.
# This sucks, but there is no other clean way around it, because tcl
# (and tclsh) aren't in the default buildroot.
%{!?tcl_version: %global tcl_version 8.6}
%{!?tcl_sitearch: %global tcl_sitearch %{_libdir}/tcl%{tcl_version}}
%global realname zlib

Name:		tcl-%{realname}
Version:	2.0.1
Release:	0.36.svn40%{?dist}
Summary:	Tcl extension for zlib support
License:	MIT
URL:		http://svn.scheffers.net/
# Snapshot of SVN40 downloaded on June 26, 2008
# Originally found at http://svn.scheffers.net/zlib.tar.gz
Source0:	%{realname}.tar.gz
Patch0:	tcl-zlib-configure-c99.patch
BuildRequires: make
BuildRequires:  gcc
BuildRequires:	tcl-devel, tk-devel, zlib-devel
Requires:	tcl(abi) = %{tcl_version}

%description
This is extension is a standalone version of the tclkit [zlib] 
command/extension. See http://wiki.tcl.tk/zlib for command syntax.

%package devel
Requires:	%{name}%{?_isa} = %{version}-%{release}
Summary:	Development files for %{name}
Provides:	tcl-%{realname}-static = %{version}-%{release}

%description devel
Development files for %{name}.

%prep
%autosetup -p1 -n %{realname}

%build
%configure --with-tcl=%{_libdir}
# Can't use smp_mflags here. :(
make

%install
make DESTDIR=%{buildroot} install-binaries install-libraries
install -d %{buildroot}%{tcl_sitearch}
mv %{buildroot}%{_libdir}/%{realname}%{version} %{buildroot}%{tcl_sitearch}/%{realname}%{version}
rm -rf %{buildroot}%{tcl_sitearch}/%{realname}%{version}/zlib.c
chmod -x %{buildroot}%{tcl_sitearch}/%{realname}%{version}/libzlibstub*.a

%files
%doc README ChangeLog
%dir %{tcl_sitearch}/%{realname}%{version}
%{tcl_sitearch}/%{realname}%{version}/*.so
%{tcl_sitearch}/%{realname}%{version}/pkgIndex.tcl

%files devel
%{tcl_sitearch}/%{realname}%{version}/libzlibstub*.a
%{_includedir}/*.h

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-0.36.svn40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-0.35.svn40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-0.34.svn40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-0.33.svn40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-0.32.svn40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov 18 2022 Florian Weimer <fweimer@redhat.com> - 2.0.1-0.31.svn40
- Avoid implicit declaration of exit in configure script

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-0.30.svn40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-0.29.svn40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-0.28.svn40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-0.27.svn40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-0.26.svn40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-0.25.svn40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-0.24.svn40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-0.23.svn40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-0.22.svn40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-0.21.svn40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-0.20.svn40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-0.19.svn40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-0.18.svn40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-0.17.svn40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Tom Callaway <spot@fedoraproject.org> - 2.0.1-0.16.svn40
- modernize spec file

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-0.15.svn40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-0.14.svn40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-0.13.svn40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 2.0.1-0.12.svn40
- Changed requires to require tcl-8.6

* Wed May 21 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 2.0.1-0.11.svn40
- Rebuilt for https://fedoraproject.org/wiki/Changes/f21tcl86

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-0.10.svn40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-0.9.svn40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-0.8.svn40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-0.7.svn40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-0.6.svn40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 19 2009 Tom "spot" Callaway <tcallawa@redhat.com> 2.0.1-0.5.svn40
- drop url from source0

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-0.4.svn40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-0.3.svn40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jan 12 2009 Tom "spot" Callaway <tcallawa@redhat.com> 2.0.1-0.2.svn40
- fix tcl version macro

* Thu Jun 26 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.0.1-0.1.svn40
- initial package for Fedora
