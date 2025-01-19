%global api_ver 5.0

%global glibmm_version 2.46.1

Name:           libgdamm
Version:        4.99.11
Release:        22%{?dist}
Summary:        C++ wrappers for libgda
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://www.gtkmm.org/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/libgdamm/4.99/%{name}-%{version}.tar.xz
BuildRequires:  gcc-c++
BuildRequires:  glibmm24-devel >= %{glibmm_version}
BuildRequires:  libgda5-devel
BuildRequires:  libgda5-bdb

Requires:       glibmm24%{?_isa} >= %{glibmm_version}

%description
C++ wrappers for libgda. libgdamm is part of a set of powerful
C++ bindings for the GNOME libraries, which provide additional
functionality above GTK+/gtkmm.

%package devel
Summary:        Headers/Libraries for developing programs that use libgdamm
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains headers and libraries that programmers will need 
to develop applications which use libgdamm.

%package        doc
Summary:        API documentation for %{name}
BuildArch:      noarch
BuildRequires:  doxygen graphviz
BuildRequires: make
Requires:       glibmm24-doc

%description    doc
This package contains the full API documentation for %{name}.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%ldconfig_scriptlets


%files
%license COPYING
%doc AUTHORS NEWS
%{_libdir}/*.so.*


%files devel
%{_includedir}/libgdamm-%{api_ver}
%{_libdir}/*.so
%{_libdir}/libgdamm-%{api_ver}
%{_libdir}/pkgconfig/*.pc

%files doc
%license COPYING
%doc %{_datadir}/devhelp/books/%{name}-%{api_ver}
%doc %{_docdir}/%{name}-%{api_ver}


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.11-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 4.99.11-21
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.11-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.11-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.11-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.11-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.11-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 04 2022 Gwyn Ciesla <gwync@protonmail.com> - 4.99.11-15
- libgda rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.11-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.11-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Sep 21 2016 Tom Callaway <spot@fedoraproject.org> - 4.99.11-1
- update to 4.99.11

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 22 2015 Kalev Lember <klember@redhat.com> - 4.99.10-1
- Update to 4.99.10
- Tighten deps with the _isa macro
- Use license macro for COPYING
- Use make_install macro

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.99.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 4.99.8-5
- Rebuilt for GCC 5 C++11 ABI change

* Sat Mar 14 2015 Kalev Lember <kalevlember@gmail.com> - 4.99.8-4
- Rebuilt for gcc5 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.99.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.99.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 17 2014 Kalev Lember <kalevlember@gmail.com> - 4.99.8-1
- Update to 4.99.8

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.99.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.99.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Oct 21 2012 Haïkel Guémar <hguemar@fedoraproject.org> - 4.99.6-1
- upstream 4.99.6 (api 5.0)
- cleanup spec

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.3-3
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Oct 11 2011 Haïkel Guémar <haikel.guemar@sysfera.com> - 4.1.3-1
- upstream 4.1.3

* Mon Jul 04 2011 Karsten Hopp <karsten@redhat.com> 4.1.2-2
- buildrequire mm-common
- fix pkg-config call to figure out doctooldir

* Mon Feb 28 2011 Haïkel Guémar <hguemar@fedoraproject.org> - 4.1.2-1
- Update to upstream 4.1.2
- put doc in sub-package

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Oct 26 2010 Haïkel Guémar <hguemar@fedoraproject.org> - 4.1.1-1
- Update to upstream 4.1.1

* Sat Jul 31 2010 Haïkel Guémar <hguemar@fedoraproject.org> - 3.99.20-1
- Update to upstream 3.99.20

* Wed Apr 28 2010 Haïkel Guémar <hguemar@fedoraproject.org> - 3.99.19-1
- Update to upstream 3.99.19

* Sat Sep 26 2009 Denis Leroy <denis@poolshark.org> - 3.99.17.1-1
- Update to upstream 3.99.17.1
- Added documentation under gtk-doc

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.99.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jun 25 2009 Denis Leroy <denis@poolshark.org> - 3.99.15-1
- Update to upstream 3.99.15, as part of glom update

* Mon Mar 23 2009 Denis Leroy <denis@poolshark.org> - 3.99.14-1
- Update to upstream 3.99.14

* Wed Mar  4 2009 Denis Leroy <denis@poolshark.org> - 3.99.12-1
- Update to upstream 3.99.12

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.99.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 23 2009 Denis Leroy <denis@poolshark.org> - 3.99.11-1
- Update to upstream 3.99.11, to match libgda version

* Wed Jan 21 2009 Denis Leroy <denis@poolshark.org> - 3.99.8-1
- Update to upstream 3.99.8 (4.0 API)

* Thu Nov 20 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 3.0.1-2
- fix source url

* Fri Oct  3 2008 Denis Leroy <denis@poolshark.org> - 3.0.1-1
- Update to upstream 3.0.1, bugfix release

* Mon Mar 17 2008 Denis Leroy <denis@poolshark.org> - 3.0.0-1
- Update to upstream 3.0.0

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.9.81-2
- Autorebuild for GCC 4.3

* Sat Jan 26 2008 Denis Leroy <denis@poolshark.org> - 2.9.81-1
- Update to upstream 2.9.81, needed a rebuild for libgda anyway

* Wed Sep 12 2007 Denis Leroy <denis@poolshark.org> - 2.9.8-1
- Update to 2.9.8, a bugfix release

* Thu Aug 23 2007 Tom "spot" Callaway <tcallawa@redhat.com> 2.9.7-2
- rebuild for license tag, ppc32

* Mon Jul 23 2007 Tom "spot" Callaway <tcallawa@redhat.com> 2.9.7-1
- back from the dead

* Mon Sep 11 2006 Tom "spot" Callaway <tcallawa@redhat.com> 1.3.7-4
- look who's alive again!

* Tue Feb 28 2006 Tom "spot" Callaway <tcallawa@redhat.com> 1.3.7-3
- FC5 time

* Thu Aug 11 2005 Tom "spot" Callaway <tcallawa@redhat.com> 1.3.7-2
- cleanups, additional devel Requires

* Sat Aug  6 2005 Tom "spot" Callaway <tcallawa@redhat.com> 1.3.7-1
- initial package for Fedora Extras
