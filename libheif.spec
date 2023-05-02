%global somajor 1

# Unable to ship this in Fedora
%bcond_with hevc

Name:           libheif
Version:        1.15.2
Release:        1%{?dist}
Summary:        HEIF and AVIF file format decoder and encoder

License:        LGPL-3.0-or-later and MIT
URL:            https://github.com/strukturag/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         https://patch-diff.githubusercontent.com/raw/strukturag/libheif/pull/815.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(aom)
BuildRequires:  pkgconfig(dav1d)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
%if ! (0%{?rhel} && 0%{?rhel} <= 9)
BuildRequires:  pkgconfig(rav1e)
%endif
%if ! ((0%{?rhel} && 0%{?rhel} <= 9) || (0%{?fedora} && 0%{?fedora} < 38))
BuildRequires:  pkgconfig(SvtAv1Enc)
%endif

%description
libheif is an ISO/IEC 23008-12:2017 HEIF and AVIF (AV1 Image File Format)
file format decoder and encoder.

%files
%license COPYING
%doc README.md
%{_libdir}/*.so.%{somajor}{,.*}
%dir %{_libdir}/%{name}
%if ! (0%{?rhel} && 0%{?rhel} <= 9)
%{_libdir}/%{name}/%{name}-rav1e.so
%endif
%if ! ((0%{?rhel} && 0%{?rhel} <= 9) || (0%{?fedora} && 0%{?fedora} < 38))
%{_libdir}/%{name}/%{name}-svtenc.so
%endif

# ----------------------------------------------------------------------

%package -n     heif-pixbuf-loader
Summary:        HEIF image loader for GTK+ applications
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gdk-pixbuf2%{?_isa}

%description -n heif-pixbuf-loader
This package provides a plugin to load HEIF files in GTK+ applications.

%files -n heif-pixbuf-loader
%{_libdir}/gdk-pixbuf-2.0/*/loaders/libpixbufloader-heif.so

# ----------------------------------------------------------------------

%package        tools
Summary:        Tools for manipulating HEIF files
License:        MIT
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       shared-mime-info

%description    tools
This package provides tools for manipulating HEIF files.

%files tools
%{_bindir}/heif-*
%{_mandir}/man1/heif-*
%{_datadir}/thumbnailers/heif.thumbnailer

# ----------------------------------------------------------------------

%if %{with hevc}
%package        hevc
Summary:        HEVC codec support for HEIC files
BuildRequires:  pkgconfig(libde265)
BuildRequires:  pkgconfig(x265)
Supplements:    %{name}

%description    hevc
This package adds support for HEVC-encoded HEIC files to applications
that use %{name} to read HEIF image files.

%files hevc
%{_libdir}/%{name}/%{name}-libde265.so
%{_libdir}/%{name}/%{name}-x265.so
%endif

# ----------------------------------------------------------------------

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files devel
%{_includedir}/%{name}/
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/*.so

# ----------------------------------------------------------------------


%prep
%autosetup -p1
rm -rf third-party/


%build
%cmake \
 -GNinja \
 -DPLUGIN_DIRECTORY=%{_libdir}/%{name} \
 %{?with_hevc:-DWITH_LIBDE265_PLUGIN:BOOL=ON -DWITH_X265_PLUGIN:BOOL=ON} \
 -Wno-dev

%cmake_build


%install
%cmake_install


%check
# Tests are not yet ported to CMake
#ctest


%changelog
* Sun Apr 30 2023 Dominik Mierzejewski <dominik@greysector.net> - 1.15.2-2
- backport fix for issue#590

* Tue Apr 11 2023 Sandro <devel@penguinpee.nl> - 1.15.2-1
- Update to 1.15.2 (RHBZ#2183664)
- Drop patch

* Fri Mar 17 2023 Neal Gompa <ngompa@fedoraproject.org> - 1.15.1-2
- Adapt for Fedora

* Fri Feb 17 2023 Leigh Scott <leigh123linux@gmail.com> - 1.15.1-1
- Update to 1.15.1

* Sat Jan 07 2023 Leigh Scott <leigh123linux@gmail.com> - 1.14.2-1
- Update to 1.14.2
- Switch back to autotools to build due to cmake issues (rfbz#6550}

* Thu Jan 05 2023 Leigh Scott <leigh123linux@gmail.com> - 1.14.1-1
- Update to 1.14.1

* Mon Dec 19 2022 Leigh Scott <leigh123linux@gmail.com> - 1.14.0-4
- Don't build rav1e and SVT-AV1 as plugins (rfbz#6532)

* Mon Dec 05 2022 Nicolas Chauvet <kwizart@gmail.com> - 1.14.0-3
- Fix for SvtAv1Enc in devel - rfbz#6521

* Wed Nov 23 2022 Nicolas Chauvet <kwizart@gmail.com> - 1.14.0-2
- Enable svt-av1 on el9

* Tue Nov 15 2022 Leigh Scott <leigh123linux@gmail.com> - 1.14.0-1
- Update to 1.14.0

* Fri Sep 02 2022 Leigh Scott <leigh123linux@gmail.com> - 1.13.0-1
- Update to 1.13.0

* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.12.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Thu Jun 23 2022 Robert-André Mauchin <zebob.m@gmail.com> - 1.12.0-5
- Rebuilt for new dav1d, rav1e and jpegxl

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Nov 25 2021 Nicolas Chauvet <kwizart@gmail.com> - 1.12.0-3
- Rebuilt

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 14 2021 Leigh Scott <leigh123linux@gmail.com> - 1.12.0-1
- Update to 1.12.0

* Sun Jun 13 2021 Robert-André Mauchin <zebob.m@gmail.com> - 1.11.0-3
- Rebuild for new aom

* Wed Apr 14 2021 Leigh Scott <leigh123linux@gmail.com> - 1.11.0-2
- Rebuild for new x265

* Sat Feb 20 2021 Leigh Scott <leigh123linux@gmail.com> - 1.11.0-1
- Update to 1.11.0

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 19 2020 Leigh Scott <leigh123linux@gmail.com> - 1.10.0-1
- Update to 1.10.0

* Mon Dec 14 2020 Leigh Scott <leigh123linux@gmail.com> - 1.9.1-3
- Actually do the dav1d rebuild

* Mon Dec 14 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.9.1-2
- Rebuild for dav1d SONAME bump

* Tue Oct 27 2020 Leigh Scott <leigh123linux@gmail.com> - 1.9.1-1
- Update to 1.9.1

* Fri Aug 28 2020 Leigh Scott <leigh123linux@gmail.com> - 1.8.0-1
- Update to 1.8.0

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 08 2020 Leigh Scott <leigh123linux@gmail.com> - 1.7.0-2
- Rebuilt

* Thu Jun 04 2020 Leigh Scott <leigh123linux@gmail.com> - 1.7.0-1
- Update to 1.7.0

* Sun May 31 2020 Leigh Scott <leigh123linux@gmail.com> - 1.6.2-3
- Rebuild for new x265 version

* Sun Feb 23 2020 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.6.2-2
- Rebuild for x265

* Mon Feb 10 2020 Leigh Scott <leigh123linux@gmail.com> - 1.6.2-1
- Update to 1.6.2

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 28 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.6.0-1
- Update to 1.6.0
- Rebuilt for x265

* Sun Nov 03 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.5.1-1
- Update to 1.5.1

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 02 2019 Nicolas Chauvet <kwizart@gmail.com> - 1.4.0-3
- Rebuilt for x265

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Feb 28 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.4.0-1
- Update to 1.4.0

* Thu Jan 03 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.3.2-2
- Rebuild for new x265 for el7

* Thu Nov 29 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.3.2-1
- First build
