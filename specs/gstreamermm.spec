%bcond mingw %[0%{?fedora} && !0%{?flatpak}]

%global api_ver 1.0
%global branch 1.10
%global mingw32_pkg_name mingw32-%{name}
%global mingw64_pkg_name mingw64-%{name}

Name:           gstreamermm
Version:        1.10.0
Release:        25%{?dist}

Summary:        C++ wrapper for GStreamer library

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://www.gtkmm.org/
Source0:        https://download.gnome.org/sources/gstreamermm/%{branch}/%{name}-%{version}.tar.xz
Patch0:         https://gitlab.gnome.org/GNOME/gstreamermm/-/merge_requests/4.patch
Patch1:         %{name}-tests.patch
# Fix mingw build issues, based on:
# https://gstreamer.freedesktop.org/documentation/video/gstvideooverlay.html?gi-language=c#gstvideooverlay-and-gtk
Patch2:         %{name}-mingw.patch
# Don't hardcode -std=c++11 or -std=c++0x
Patch3:         %{name}-nostdcxx.patch

BuildRequires:  gcc-c++
BuildRequires: glibmm24-devel >= 2.21.1
# Enable GUI examples build as a test
BuildRequires: gtkmm30-devel >= 3.0
BuildRequires: gstreamer1-devel
BuildRequires: gstreamer1-plugins-base-devel
# Required for building tests
BuildRequires: gtest-devel
BuildRequires: libxml++-devel >= 2.14.0
BuildRequires: doxygen graphviz m4
%if %{with mingw}
BuildRequires: mingw32-filesystem
BuildRequires: mingw64-filesystem
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw32-glibmm24
BuildRequires: mingw64-glibmm24
BuildRequires: mingw32-gtkmm30
BuildRequires: mingw64-gtkmm30
BuildRequires: mingw32-gstreamer1
BuildRequires: mingw64-gstreamer1
BuildRequires: mingw32-gstreamer1-plugins-base
BuildRequires: mingw64-gstreamer1-plugins-base
%endif


%description
GStreamermm is a C++ wrapper library for the multimedia library
GStreamer (http://gstreamer.freedesktop.org).  It is designed to allow
C++ development of applications that work with multi-media.


%package        devel
Summary:        Headers for developing programs that will use %{name}
Requires:       %{name} = %{version}-%{release}

%description devel
This package contains the static libraries and header files needed for
developing gstreamermm applications.


%package          doc
Summary:          Developer's documentation for the gstreamermm library
BuildArch:        noarch
BuildRequires:    doxygen graphviz
BuildRequires: make
Requires:         glibmm24-doc

%description      doc
This package contains developer's documentation for the GStreamermm
library. Gstreamermm is the C++ API for the GStreamer library.

The documentation can be viewed either through the devhelp
documentation browser or through a web browser.

%if %{with mingw}
%package -n mingw32-gstreamermm
Summary: MingwGW Windows C++ wrapper for GStreamer library
BuildArch: noarch

%description -n mingw32-gstreamermm
GStreamermm is a C++ wrapper library for the multimedia library
GStreamer (http://gstreamer.freedesktop.org).  It is designed to allow
C++ development of applications that work with multi-media.

%package -n mingw32-gstreamermm-devel
Summary:        Development files for %{name}
Requires:       mingw32-%{name} = %{version}-%{release}

%description -n mingw32-gstreamermm-devel
The mingw32-%{name}-devel package contains libraries and header files for
developing applications that use mingw32-%{name}.

%package -n mingw64-gstreamermm
Summary: MingwGW Windows C++ wrapper for GStreamer library
BuildArch: noarch

%description -n mingw64-gstreamermm
GStreamermm is a C++ wrapper library for the multimedia library
GStreamer (http://gstreamer.freedesktop.org).  It is designed to allow
C++ development of applications that work with multi-media.

%package -n mingw64-gstreamermm-devel
Summary:        Development files for %{name}
Requires:       mingw64-%{name} = %{version}-%{release}

%description -n mingw64-gstreamermm-devel
The mingw64-%{name}-devel package contains libraries and header files for
developing applications that use mingw64-%{name}.

%{?mingw_debug_package}
%endif

%prep
%setup -q
%patch 0 -p1
%patch 1 -p1 -b .tests
%patch 2 -p1 -b .mingw
%patch 3 -p1 -b .nostdcxx


%build
mkdir %{_target_os}
pushd %{_target_os}
%define _configure ../configure
mkdir -p gstreamer/src
%configure
%make_build
popd

%if %{with mingw}
%mingw_configure
%mingw_make_build
%endif


%install
pushd %{_target_os}
%make_install
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'
popd

%if %{with mingw}
%mingw_make_install
%mingw_debug_install_post

rm -rv %{buildroot}{%{mingw32_docdir},%{mingw64_docdir}}/%{name}-%{api_ver}
%endif

%check
pushd %{_target_os}
%make_build check
popd


%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/*.so.*

%files devel
%{_includedir}/%{name}-%{api_ver}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/%{name}-%{api_ver}

%files doc
%license COPYING
%doc %{_docdir}/%{name}-%{api_ver}/
%doc %{_datadir}/devhelp/books/%{name}-%{api_ver}/

%if %{with mingw}
%files -n mingw32-gstreamermm
%doc AUTHORS ChangeLog NEWS README
%{mingw32_bindir}/libgstreamermm-1.0-1.dll

%files -n mingw32-gstreamermm-devel
%{mingw32_libdir}/%{name}-%{api_ver}
%{mingw32_libdir}/libgstreamermm-1.0.dll.a
%{mingw32_libdir}/pkgconfig/gstreamermm-1.0.pc
%{mingw32_includedir}/%{name}-%{api_ver}
%{mingw32_datadir}/devhelp/books/%{name}-%{api_ver}

%files -n mingw64-gstreamermm
%doc AUTHORS ChangeLog NEWS README
%{mingw64_bindir}/libgstreamermm-1.0-1.dll

%files -n mingw64-gstreamermm-devel
%{mingw64_libdir}/%{name}-%{api_ver}
%{mingw64_libdir}/libgstreamermm-1.0.dll.a
%{mingw64_libdir}/pkgconfig/gstreamermm-1.0.pc
%{mingw64_includedir}/%{name}-%{api_ver}
%{mingw64_datadir}/devhelp/books/%{name}-%{api_ver}
%endif

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.10.0-24
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Mar 25 2023 Dominik Mierzejewski <dominik@greysector.net> - 1.10.0-19
- add missing build dependencies on mingw g++

* Wed Feb 01 2023 Dominik Mierzejewski <dominik@greysector.net> - 1.10.0-18
- fix FTBFS with gtest-1.13.0 (fixes rhbz#2165230)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 22 2022 Robert Scheck <robert@fedoraproject.org> - 1.10.0-16
- Build mingw32/64 packages only on Fedora branches (#2144671)

* Fri Nov 04 2022 Dominik Mierzejewski <dominik@greysector.net> - 1.10.0-15
- put mingw devel files in corresponding -devel subpackages

* Wed Oct 19 2022 Dominik Mierzejewski <dominik@greysector.net> - 1.10.0-14
- add mingw builds as subpackages (#1825263)
- use upstream patch for fixing build against newer glib

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jul 25 2021 Dominik Mierzejewski <rpm@greysector.net> - 1.10.0-11
- fix build
- use modern macros
- fix compilation and enable tests
- disable the two failing tests for now (#1986201)
- switch to HTTPS URLs

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Mar 06 2020 Kalev Lember <klember@redhat.com> - 1.10.0-7
- Fix incorrect gstreamer-devel (0.10) dep in the -devel subpackage

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 28 2018 hguemar <hguemar@nozarashi.seireitei> - 1.10.0-1
- Upstream 1.10.0
- Fix dir ownership  in doc subpackage
- Some cleanup in spec

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jun  7 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 1.4.3-1
- Upstream 1.4.3
- Based on Ankur Sinha work (RHBZ#1315852)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.10.11-7
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Kalev Lember <kalevlember@gmail.com> - 0.10.11-6
- Rebuilt for GCC 5 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 17 2012 Haïkel Guémar <hguemar@fedoraproject.org> - 0.10.11-1
- upstream 0.10.11 (bugfixes: memleaks and library startup speed-up)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 17 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.10.10-3
- Add gstreamermm-0.10.10-glib2-2.31.patch to work around glib2 API changes.
  (Fix mass rebuild FTBFS). 

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Aug 07 2011 Haïkel Guémar <hguemar@fedoraproject.org> - 0.10.10-1
- upstream 0.10.10
- remove DSO linking patch

* Tue Apr 19 2011 Haïkel Guémar <hguemar@fedoraproject.org> - 0.10.9-1
- upstream 0.10.9
- temporary patch to fix DSO linking issue with code generator

* Tue Feb 22 2011 Haïkel Guémar <hguemar@fedoraproject.org> - 0.10.8-3
- split doc into subpackage

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Oct 24 2010 Haïkel Guémar <hguemar@fedoraproject.org> - 0.10.8-1
- Update to upstream 0.10.8

* Fri Apr 30 2010 Haïkel Guémar <hguemar@fedoraproject.org> - 0.10.7-1
- Update to upstream 0.10.7

* Mon Jan  4 2010 Denis Leroy <denis@poolshark.org> - 0.10.6-1
- Update to upstream 0.10.6

* Sat Nov  7 2009 Denis Leroy <denis@poolshark.org> - 0.10.5.2-1
- Update to 0.10.5.2
- Fix devhelp doc setup

* Mon Sep 14 2009 Denis Leroy <denis@poolshark.org> - 0.10.5-1
- Update to upstream 0.10.5
- doc patch upstreamed

* Wed Sep  2 2009 Denis Leroy <denis@poolshark.org> - 0.10.4-2
- Rebuild for new glibmm24
- Added patch to remove beautify_docs

* Thu Aug 20 2009 Denis Leroy <denis@poolshark.org> - 0.10.4-1
- Update to upstream 0.10.4

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 26 2009 Denis Leroy <denis@poolshark.org> - 0.10.2-1
- Update to upstream 0.10.2

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 23 2009 Denis Leroy <denis@poolshark.org> - 0.10.1-1
- Update to upstream 0.10.1
- No longer uses gstreamerbase include dir

* Sun Dec 28 2008 Denis Leroy <denis@poolshark.org> - 0.9.8-2
- Rebuild for pkgconfig

* Fri Dec 26 2008 Denis Leroy <denis@poolshark.org> - 0.9.8-1
- Update to upstream 0.9.8
- Disabled parallel make

* Fri Oct 10 2008 Denis Leroy <denis@poolshark.org> - 0.9.7-1
- Update to upstream 0.9.7

* Wed Sep  3 2008 Denis Leroy <denis@poolshark.org> - 0.9.6-1
- Update to upstream 0.9.6

* Sat May 31 2008 Denis Leroy <denis@poolshark.org> - 0.9.5-1
- Update to upstream 0.9.5
- Fixed gstreamer plugin BuildRequires

* Fri Feb 22 2008 Denis Leroy <denis@poolshark.org> - 0.9.4-1
- Updated to upstream 0.9.4

* Sun Feb 17 2008 Denis Leroy <denis@poolshark.org> - 0.9.2-1
- First draft
