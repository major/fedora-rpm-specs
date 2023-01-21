%?mingw_package_header

Name:           mingw-gstreamer
Version:        0.10.36
Release:        26%{?dist}
Summary:        MinGW Windows Streaming-Media Framework Runtime

License:        LGPLv2+
URL:            http://gstreamer.freedesktop.org/
Source0:        http://gstreamer.freedesktop.org/src/gstreamer/gstreamer-%{version}.tar.bz2

BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-glib2
BuildRequires:  mingw32-libxml2

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-glib2
BuildRequires:  mingw64-libxml2

BuildRequires:  bison flex
# use native glib-genmarshal and glib-mkenums
BuildRequires:  glib2-devel

# Needed for the patches
BuildRequires:  autoconf automake libtool gtk-doc gettext-devel

# Upstream commits which are required to fix the build when winpthreads is available
Patch0:         e2f2ee3582731fd52e5b93a0a82fdf6f4156bce2.patch
Patch1:         e745a2bcf07eb7ecafcb92428b4d2907ff22b124.patch

# Fix compatibility issue with Bison 3
# http://cgit.freedesktop.org/gstreamer/gstreamer/patch/?id=60516f4
Patch2:         gstreamer-0.10.36-bison3.patch


%description
GStreamer is a streaming-media framework, based on graphs of filters
which operate on media data. Applications using this library can do
anything from real-time sound processing to playing videos, and just
about anything else media-related. Its plug-in-based architecture
means that new data types or processing capabilities can be added by
installing new plug-ins.

# Win32
%package  -n mingw32-gstreamer
Summary:        MinGW Windows Streaming-Media Framework Runtime
# Fix upgrade path when upgrading from the testing repository
Obsoletes:      mingw32-gstreamer-tools < 0.10.35-4
Obsoletes:      mingw32-gstreamer-static < 0.10.35-4
Provides:       mingw32-gstreamer-tools = 0.10.35-4
Provides:       mingw32-gstreamer-static = 0.10.35-4

%description -n mingw32-gstreamer
GStreamer is a streaming-media framework, based on graphs of filters
which operate on media data. Applications using this library can do
anything from real-time sound processing to playing videos, and just
about anything else media-related. Its plug-in-based architecture
means that new data types or processing capabilities can be added by
installing new plug-ins.

# Win64
%package  -n mingw64-gstreamer
Summary:        MinGW Windows Streaming-Media Framework Runtime
# Fix upgrade path when upgrading from the testing repository
Obsoletes:      mingw64-gstreamer-tools < 0.10.35-4
Obsoletes:      mingw64-gstreamer-static < 0.10.35-4
Provides:       mingw64-gstreamer-tools = 0.10.35-4
Provides:       mingw64-gstreamer-static = 0.10.35-4

%description -n mingw64-gstreamer
GStreamer is a streaming-media framework, based on graphs of filters
which operate on media data. Applications using this library can do
anything from real-time sound processing to playing videos, and just
about anything else media-related. Its plug-in-based architecture
means that new data types or processing capabilities can be added by
installing new plug-ins.


%?mingw_debug_package


%prep
%setup -q -n gstreamer-%{version}
%patch0 -p1 -b .winpthreads
%patch1 -p1 -b .winpthreads
%patch2 -p1 -b .bison3

NOCONFIGURE=1 ./autogen.sh


%build
%mingw_configure                                                       \
    --with-package-name='Fedora Mingw gstreamer package'               \
    --with-package-origin='http://download.fedora.redhat.com/fedora'   \
    --enable-shared                                                    \
    --disable-static                                                   \
    --disable-gtk-doc                                                  \
    --enable-debug                                                     \
    --disable-tests                                                    \
    --disable-examples

%mingw_make %{?_smp_mflags}


%install
%mingw_make_install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/gstreamer-0.10/*.dll.a
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/gstreamer-0.10/*.la
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/*.la
rm -fr $RPM_BUILD_ROOT%{mingw32_datadir}/gtk-doc
rm -f $RPM_BUILD_ROOT%{mingw32_mandir}/man1/gst*
rm -f $RPM_BUILD_ROOT%{mingw32_datadir}/aclocal/gst-element-check-0.10.m4

rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/gstreamer-0.10/*.dll.a
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/gstreamer-0.10/*.la
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/*.la
rm -fr $RPM_BUILD_ROOT%{mingw64_datadir}/gtk-doc
rm -f $RPM_BUILD_ROOT%{mingw64_mandir}/man1/gst*
rm -f $RPM_BUILD_ROOT%{mingw64_datadir}/aclocal/gst-element-check-0.10.m4

%mingw_find_lang gstreamer-0.10


# Win32
%files -n mingw32-gstreamer -f mingw32-gstreamer-0.10.lang
%doc COPYING
%dir %{mingw32_libdir}/gstreamer-0.10
%{mingw32_libdir}/gstreamer-0.10/libgstcoreelements.dll
%{mingw32_libdir}/gstreamer-0.10/libgstcoreindexers.dll

%dir %{mingw32_includedir}/gstreamer-0.10
%{mingw32_includedir}/gstreamer-0.10/gst

%dir %{mingw32_libexecdir}/gstreamer-0.10
%{mingw32_libexecdir}/gstreamer-0.10/gst-plugin-scanner.exe

%{mingw32_libdir}/libgstbase-0.10.dll.a
%{mingw32_libdir}/libgstcontroller-0.10.dll.a
%{mingw32_libdir}/libgstdataprotocol-0.10.dll.a
%{mingw32_libdir}/libgstnet-0.10.dll.a
%{mingw32_libdir}/libgstreamer-0.10.dll.a

%{mingw32_libdir}/pkgconfig/gstreamer-0.10.pc
%{mingw32_libdir}/pkgconfig/gstreamer-base-0.10.pc
%{mingw32_libdir}/pkgconfig/gstreamer-controller-0.10.pc
%{mingw32_libdir}/pkgconfig/gstreamer-dataprotocol-0.10.pc
%{mingw32_libdir}/pkgconfig/gstreamer-net-0.10.pc

%{mingw32_bindir}/gst-feedback.exe
%{mingw32_bindir}/gst-inspect.exe
%{mingw32_bindir}/gst-launch.exe
%{mingw32_bindir}/gst-xmlinspect.exe
%{mingw32_bindir}/gst-xmllaunch.exe
%{mingw32_bindir}/gst-typefind.exe
%{mingw32_bindir}/gst-feedback-0.10
%{mingw32_bindir}/gst-inspect-0.10.exe
%{mingw32_bindir}/gst-launch-0.10.exe
%{mingw32_bindir}/gst-xmlinspect-0.10.exe
%{mingw32_bindir}/gst-xmllaunch-0.10.exe
%{mingw32_bindir}/gst-typefind-0.10.exe

%{mingw32_bindir}/libgstbase-0.10-0.dll
%{mingw32_bindir}/libgstcontroller-0.10-0.dll
%{mingw32_bindir}/libgstdataprotocol-0.10-0.dll
%{mingw32_bindir}/libgstnet-0.10-0.dll
%{mingw32_bindir}/libgstreamer-0.10-0.dll

# Win64
%files -n mingw64-gstreamer -f mingw64-gstreamer-0.10.lang
%doc COPYING
%dir %{mingw64_libdir}/gstreamer-0.10
%{mingw64_libdir}/gstreamer-0.10/libgstcoreelements.dll
%{mingw64_libdir}/gstreamer-0.10/libgstcoreindexers.dll

%dir %{mingw64_includedir}/gstreamer-0.10
%{mingw64_includedir}/gstreamer-0.10/gst

%dir %{mingw64_libexecdir}/gstreamer-0.10
%{mingw64_libexecdir}/gstreamer-0.10/gst-plugin-scanner.exe

%{mingw64_libdir}/libgstbase-0.10.dll.a
%{mingw64_libdir}/libgstcontroller-0.10.dll.a
%{mingw64_libdir}/libgstdataprotocol-0.10.dll.a
%{mingw64_libdir}/libgstnet-0.10.dll.a
%{mingw64_libdir}/libgstreamer-0.10.dll.a

%{mingw64_libdir}/pkgconfig/gstreamer-0.10.pc
%{mingw64_libdir}/pkgconfig/gstreamer-base-0.10.pc
%{mingw64_libdir}/pkgconfig/gstreamer-controller-0.10.pc
%{mingw64_libdir}/pkgconfig/gstreamer-dataprotocol-0.10.pc
%{mingw64_libdir}/pkgconfig/gstreamer-net-0.10.pc

%{mingw64_bindir}/gst-feedback.exe
%{mingw64_bindir}/gst-inspect.exe
%{mingw64_bindir}/gst-launch.exe
%{mingw64_bindir}/gst-xmlinspect.exe
%{mingw64_bindir}/gst-xmllaunch.exe
%{mingw64_bindir}/gst-typefind.exe
%{mingw64_bindir}/gst-feedback-0.10
%{mingw64_bindir}/gst-inspect-0.10.exe
%{mingw64_bindir}/gst-launch-0.10.exe
%{mingw64_bindir}/gst-xmlinspect-0.10.exe
%{mingw64_bindir}/gst-xmllaunch-0.10.exe
%{mingw64_bindir}/gst-typefind-0.10.exe

%{mingw64_bindir}/libgstbase-0.10-0.dll
%{mingw64_bindir}/libgstcontroller-0.10-0.dll
%{mingw64_bindir}/libgstdataprotocol-0.10-0.dll
%{mingw64_bindir}/libgstnet-0.10-0.dll
%{mingw64_bindir}/libgstreamer-0.10-0.dll


%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.36-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.36-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 0.10.36-24
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.36-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.36-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.36-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 12 13:37:45 GMT 2020 Sandro Mani <manisandro@gmail.com> - 0.10.36-20
- Rebuild (mingw-gettext)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.36-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 20 2020 Sandro Mani <manisandro@gmail.com> - 0.10.36-18
- Rebuild (gettext)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.36-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 0.10.36-16
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.36-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.36-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.36-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.36-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.36-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.36-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.36-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.36-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.36-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Mar 30 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.10.36-6
- Fix FTBFS against Bison 3

* Sat Sep  7 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.10.36-5
- Backported upstream commits which are needed to avoid FTBFS when winpthreads is available

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.36-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.36-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 13 2012 Paweł Forysiuk <tuxator@o2.pl> - 0.10.36-1
- Update to upstream version 0.10.36

* Sun Mar 11 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.10.35-6
- Added win64 support (contributed by Marc-André Lureau)
- Use mingw macros without leading underscore

* Fri Mar 09 2012 Kalev Lember <kalevlember@gmail.com> - 0.10.35-5
- Remove all .la files

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.10.35-4
- Rebuild against the mingw-w64 toolchain

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.35-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Jul 16 2011 Paweł Forysiuk <tuxator@o2.pl> - 0.10.35-2
- Remove no longer needed rpm macros from spec file

* Sat Jul 16 2011 Paweł Forysiuk <tuxator@o2.pl> - 0.10.35-1
- Update to new upstream version 0.10.35

* Fri May 13 2011 Paweł Forysiuk <tuxator@o2.pl> - 0.10.32-1
- Initial packaging, basing on OpenSUSE's mingw32-gstreamer
