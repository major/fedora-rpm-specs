%{?mingw_package_header}

%global         api_version      1.0

Name:           mingw-gstreamer1-plugins-base
Version:        1.25.1
Release:        2%{?dist}
Summary:        Cross compiled GStreamer1 media framework base plug-ins

License:        LGPL-2.0-or-later
URL:            http://gstreamer.freedesktop.org/
Source:         http://gstreamer.freedesktop.org/src/gst-plugins-base/gst-plugins-base-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  gettext
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  orc-compiler

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-gettext
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-gstreamer1 >= %{version}
BuildRequires:  mingw32-libogg >= 1.0
BuildRequires:  mingw32-libvorbis >= 1.0
BuildRequires:  mingw32-libtheora
BuildRequires:  mingw32-orc
BuildRequires:  mingw32-gtk3
BuildRequires:  mingw32-pango
BuildRequires:  mingw32-libxml2

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-gettext
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-gstreamer1 >= %{version}
BuildRequires:  mingw64-libogg >= 1.0
BuildRequires:  mingw64-libvorbis >= 1.0
BuildRequires:  mingw64-libtheora
BuildRequires:  mingw64-orc
BuildRequires:  mingw64-gtk3
BuildRequires:  mingw64-pango
BuildRequires:  mingw64-libxml2

BuildRequires:  perl-interpreter
# We need glib-mkenums
BuildRequires:  glib2-devel


%description
GStreamer is a streaming media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plug-ins.

This package contains a set of well-maintained base plug-ins.


# Win32
%package -n mingw32-gstreamer1-plugins-base
Summary:        Cross compiled GStreamer media framework base plug-ins
Requires:       mingw32-gstreamer1 >= %{version}

%description  -n mingw32-gstreamer1-plugins-base
GStreamer is a streaming media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plug-ins.

This package contains a set of well-maintained base plug-ins.

# Win64
%package -n mingw64-gstreamer1-plugins-base
Summary:        Cross compiled GStreamer media framework base plug-ins
Requires:       mingw64-gstreamer1 >= %{version}

%description  -n mingw64-gstreamer1-plugins-base
GStreamer is a streaming media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plug-ins.

This package contains a set of well-maintained base plug-ins.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n gst-plugins-base-%{version}


%build
%mingw_meson                                                            \
    -Dpackage-name='Fedora MinGW GStreamer-plugins-base package'        \
    -Dpackage-origin='http://download.fedoraproject.org'                \
    -D doc=disabled \
    -D orc=enabled \
    -D tremor=disabled \
    -D tests=disabled \
    -D examples=disabled

%mingw_ninja


%install
%mingw_ninja_install

# Drop man pages
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}

# Drop import libs for plugins
rm -rf %{buildroot}%{mingw32_libdir}/gstreamer-%{api_version}/*.dll.a
rm -rf %{buildroot}%{mingw64_libdir}/gstreamer-%{api_version}/*.dll.a

%mingw_find_lang gst-plugins-base-%{api_version}


# Win32
%files -n mingw32-gstreamer1-plugins-base -f mingw32-gst-plugins-base-%{api_version}.lang
%license COPYING
%doc AUTHORS README.md REQUIREMENTS

%{mingw32_bindir}/gst-device-monitor-%{api_version}.exe
%{mingw32_bindir}/gst-play-%{api_version}.exe
%{mingw32_bindir}/gst-discoverer-%{api_version}.exe
%{mingw32_bindir}/libgstallocators-%{api_version}-0.dll
%{mingw32_bindir}/libgstapp-%{api_version}-0.dll
%{mingw32_bindir}/libgstaudio-%{api_version}-0.dll
%{mingw32_bindir}/libgstfft-%{api_version}-0.dll
%{mingw32_bindir}/libgstgl-%{api_version}-0.dll
%{mingw32_bindir}/libgstpbutils-%{api_version}-0.dll
%{mingw32_bindir}/libgstriff-%{api_version}-0.dll
%{mingw32_bindir}/libgstrtp-%{api_version}-0.dll
%{mingw32_bindir}/libgstrtsp-%{api_version}-0.dll
%{mingw32_bindir}/libgstsdp-%{api_version}-0.dll
%{mingw32_bindir}/libgsttag-%{api_version}-0.dll
%{mingw32_bindir}/libgstvideo-%{api_version}-0.dll

%{mingw32_includedir}/gstreamer-%{api_version}/

%{mingw32_libdir}/gstreamer-%{api_version}/*.dll
%{mingw32_libdir}/gstreamer-%{api_version}/include
%{mingw32_libdir}/libgstallocators-%{api_version}.dll.a
%{mingw32_libdir}/libgstapp-%{api_version}.dll.a
%{mingw32_libdir}/libgstaudio-%{api_version}.dll.a
%{mingw32_libdir}/libgstfft-%{api_version}.dll.a
%{mingw32_libdir}/libgstgl-%{api_version}.dll.a
%{mingw32_libdir}/libgstpbutils-%{api_version}.dll.a
%{mingw32_libdir}/libgstriff-%{api_version}.dll.a
%{mingw32_libdir}/libgstrtp-%{api_version}.dll.a
%{mingw32_libdir}/libgstrtsp-%{api_version}.dll.a
%{mingw32_libdir}/libgstsdp-%{api_version}.dll.a
%{mingw32_libdir}/libgsttag-%{api_version}.dll.a
%{mingw32_libdir}/libgstvideo-%{api_version}.dll.a

%{mingw32_libdir}/pkgconfig/*.pc

%{mingw32_datadir}/gst-plugins-base

# Win64
%files -n mingw64-gstreamer1-plugins-base -f mingw64-gst-plugins-base-%{api_version}.lang
%license COPYING
%doc AUTHORS README.md REQUIREMENTS

%{mingw64_bindir}/gst-device-monitor-%{api_version}.exe
%{mingw64_bindir}/gst-play-%{api_version}.exe
%{mingw64_bindir}/gst-discoverer-%{api_version}.exe
%{mingw64_bindir}/libgstallocators-%{api_version}-0.dll
%{mingw64_bindir}/libgstapp-%{api_version}-0.dll
%{mingw64_bindir}/libgstaudio-%{api_version}-0.dll
%{mingw64_bindir}/libgstfft-%{api_version}-0.dll
%{mingw64_bindir}/libgstgl-%{api_version}-0.dll
%{mingw64_bindir}/libgstpbutils-%{api_version}-0.dll
%{mingw64_bindir}/libgstriff-%{api_version}-0.dll
%{mingw64_bindir}/libgstrtp-%{api_version}-0.dll
%{mingw64_bindir}/libgstrtsp-%{api_version}-0.dll
%{mingw64_bindir}/libgstsdp-%{api_version}-0.dll
%{mingw64_bindir}/libgsttag-%{api_version}-0.dll
%{mingw64_bindir}/libgstvideo-%{api_version}-0.dll

%{mingw64_includedir}/gstreamer-%{api_version}/

%{mingw64_libdir}/gstreamer-%{api_version}/*.dll
%{mingw64_libdir}/gstreamer-%{api_version}/include
%{mingw64_libdir}/libgstallocators-%{api_version}.dll.a
%{mingw64_libdir}/libgstapp-%{api_version}.dll.a
%{mingw64_libdir}/libgstaudio-%{api_version}.dll.a
%{mingw64_libdir}/libgstfft-%{api_version}.dll.a
%{mingw64_libdir}/libgstgl-%{api_version}.dll.a
%{mingw64_libdir}/libgstpbutils-%{api_version}.dll.a
%{mingw64_libdir}/libgstriff-%{api_version}.dll.a
%{mingw64_libdir}/libgstrtp-%{api_version}.dll.a
%{mingw64_libdir}/libgstrtsp-%{api_version}.dll.a
%{mingw64_libdir}/libgstsdp-%{api_version}.dll.a
%{mingw64_libdir}/libgsttag-%{api_version}.dll.a
%{mingw64_libdir}/libgstvideo-%{api_version}.dll.a

%{mingw64_libdir}/pkgconfig/*.pc

%{mingw64_datadir}/gst-plugins-base

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.25.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jan 15 2025 Sandro Mani <manisandro@gmail.com> - 1.25.1-1
- Update to 1.25.1

* Sun Jan 12 2025 Sandro Mani <manisandro@gmail.com> - 1.24.11-1
- Update to 1.24.11

* Fri Dec 06 2024 Sandro Mani <manisandro@gmail.com> - 1.24.10-1
- Update to 1.24.10

* Tue Nov 05 2024 Sandro Mani <manisandro@gmail.com> - 1.24.9-1
- Update to 1.24.9

* Mon Sep 23 2024 Sandro Mani <manisandro@gmail.com> - 1.24.8-1
- Update to 1.24.8

* Fri Aug 23 2024 Sandro Mani <manisandro@gmail.com> - 1.24.7-1
- Update to 1.24.7

* Tue Jul 30 2024 Sandro Mani <manisandro@gmail.com> - 1.24.6-1
- Update to 1.24.6

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 23 2024 Sandro Mani <manisandro@gmail.com> - 1.24.5-1
- Update to 1.24.5

* Thu Jun 06 2024 Sandro Mani <manisandro@gmail.com> - 1.24.4-1
- Update to 1.24.4

* Wed May 01 2024 Sandro Mani <manisandro@gmail.com> - 1.24.3-1
- Update to 1.24.3

* Thu Mar 07 2024 Sandro Mani <manisandro@gmail.com> - 1.24.0-1
- Update to 1.24.0

* Sat Jan 27 2024 Sandro Mani <manisandro@gmail.com> - 1.22.9-1
- Update to 1.22.9

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Dec 20 2023 Sandro Mani <manisandro@gmail.com> - 1.22.8-1
- Update to 1.22.8

* Wed Nov 15 2023 Sandro Mani <manisandro@gmail.com> - 1.22.7-1
- Update to 1.22.7

* Thu Sep 21 2023 Sandro Mani <manisandro@gmail.com> - 1.22.6-1
- Update to 1.22.6

* Sat Jul 29 2023 Sandro Mani <manisandro@gmail.com> - 1.22.5-1
- Update to 1.22.5

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 04 2023 Sandro Mani <manisandro@gmail.com> - 1.22.4-1
- Update to 1.22.4

* Thu May 25 2023 Sandro Mani <manisandro@gmail.com> - 1.22.3-1
- Update to 1.22.3

* Sat Apr 15 2023 Sandro Mani <manisandro@gmail.com> - 1.22.2-1
- Update to 1.22.2

* Sun Mar 19 2023 Sandro Mani <manisandro@gmail.com> - 1.22.1-1
- Update to 1.22.1

* Sat Jan 28 2023 Sandro Mani <manisandro@gmail.com> - 1.22.0-1
- Update to 1.22.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Nov 13 2022 Sandro Mani <manisandro@gmail.com> - 1.20.4-1
- Update to 1.20.4

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Sandro Mani <manisandro@gmail.com> - 1.20.3-1
- Update to 1.20.3

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 1.20.0-2
- Rebuild with mingw-gcc-12

* Sat Feb 05 2022 Sandro Mani <manisandro@gmail.com> - 1.20.0-1
- Update to 1.20.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Nov 13 2021 Sandro Mani <mansiandro@gmail.com> - 1.19.3-1
- Update to 1.19.3

* Sat Oct 02 2021 Sandro Mani <manisandro@gmail.com> - 1.19.2-1
- Update to 1.19.2

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 07 2021 Sandro Mani <manisandro@gmail.com> - 1.19.1-1
- Update to 1.19.1

* Wed Mar 24 2021 Sandro Mani <manisandro@gmail.com> - 1.18.4-1
- Update to 1.18.4

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 10 2020 Sandro Mani <manisandro@gmail.com> - 1.18.2-1
- Update to 1.18.2

* Sun Nov 01 2020 Sandro Mani <manisandro@gmail.com> - 1.18.1-1
- Update to 1.18.1

* Mon Sep 14 2020 Sandro Mani <manisandro@gmail.com> - 1.18.0-3
- Use same meson options as native package

* Mon Sep 14 2020 Sandro Mani <manisandro@gmail.com> - 1.18.0-2
- Drop import libs for plugins

* Sun Sep 13 2020 Sandro Mani <manisandro@gmail.com> - 1.18.0-1
- Update to 1.18.0

* Wed Aug 12 13:38:23 GMT 2020 Sandro Mani <manisandro@gmail.com> - 1.16.2-3
- Rebuild (mingw-gettext)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 20 2020 Sandro Mani <manisandro@gmail.com> - 1.16.2-1
- Update to 1.16.2

* Mon Apr 20 2020 Sandro Mani <manisandro@gmail.com> - 1.14.2-6
- Rebuild (gettext)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 1.14.2-4
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 24 2018 Christophe Fergeau <cfergeau@redhat.com> - 1.14.2-1
- Update to 1.14.2

* Mon Jul 16 2018 Victor Toso <victortoso@redhat.com> - 1.14.1-1
- Update to 1.14.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 15 2017 Kalev Lember <klember@redhat.com> - 1.12.3-1
- Update to 1.12.3

* Sat Sep 09 2017 Sandro Mani <manisandro@gmail.com> - 1.12.1-3
- Fix debug files in main package
- Fix FTBFS

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 20 2017 Kalev Lember <klember@redhat.com> - 1.12.1-1
- Update to 1.12.1
- Enable libtheora and orc support

* Tue Feb  7 2017 Victor Toso <victortoso@redhat.com> - 1.11.1-1
- Update to 1.11.1
- Fix CVE-2017-5837
- Fix CVE-2017-5839
- Fix CVE-2017-5842
- Fix CVE-2017-5844

* Fri Nov  4 2016 Victor Toso <victortoso@redhat.com> - 1.10.0-1
- Update to 1.10.0

* Thu May 12 2016 Kalev Lember <klember@redhat.com> - 1.8.1-1
- Update to 1.8.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 26 2015 Kalev Lember <klember@redhat.com> - 1.6.0-1
- Update to 1.6.0
- Use license macro for COPYING

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 16 2015 Paweł Forysiuk <tuxator@o2.pl> - 1.4.5-1
- Update to 1.4.5

* Sat Nov 15 2014 Kalev Lember <kalevlember@gmail.com> - 1.4.4-1
- Update to 1.4.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 29 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.3.2-1
- Update to 1.3.2

* Thu May 29 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.2.4-1
- Update to 1.2.4
- Fix FTBFS against mingw-gcc 4.9

* Wed Dec  4 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 02 2013 Paweł Forysiuk <tuxator@o2.pl> - 1.0.6-1
- Initial packaging
