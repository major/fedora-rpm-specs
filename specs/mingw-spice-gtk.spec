%{?mingw_package_header}

Name:           mingw-spice-gtk
Version:        0.42
Release:        8%{?dist}
Summary:        A GTK+ widget for SPICE clients

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://spice-space.org/page/Spice-Gtk
Source0:        http://www.spice-space.org/download/gtk/spice-gtk-%{version}%{?_version_suffix}.tar.xz
#Source1:        http://www.spice-space.org/download/gtk/spice-gtk-%{version}%{?_version_suffix}.tar.xz.sig
#Source2:        victortoso-E37A484F.keyring

Patch0001:     0001-usb-backend-Fix-compiling-with-i686-clang-in-mingw.patch

BuildArch: noarch

BuildRequires: mingw32-filesystem >= 104
BuildRequires: mingw64-filesystem >= 104
BuildRequires: mingw32-gcc
BuildRequires: mingw64-gcc
BuildRequires: mingw32-binutils
BuildRequires: mingw64-binutils
BuildRequires: glib2-devel

BuildRequires: mingw32-gtk3 >= 3.22
BuildRequires: mingw64-gtk3 >= 3.22
BuildRequires: mingw32-pixman
BuildRequires: mingw64-pixman
BuildRequires: mingw32-openssl
BuildRequires: mingw64-openssl
BuildRequires: mingw32-libjpeg-turbo
BuildRequires: mingw64-libjpeg-turbo
BuildRequires: mingw32-zlib
BuildRequires: mingw64-zlib
BuildRequires: mingw32-gstreamer1
BuildRequires: mingw64-gstreamer1
BuildRequires: mingw32-gstreamer1-plugins-base
BuildRequires: mingw64-gstreamer1-plugins-base
BuildRequires: mingw32-opus
BuildRequires: mingw64-opus
BuildRequires: mingw32-spice-protocol >= 0.12.15
BuildRequires: mingw64-spice-protocol >= 0.12.15
BuildRequires: mingw32-libusbx >= 1.0.21
BuildRequires: mingw64-libusbx >= 1.0.21
BuildRequires: mingw32-usbredir >= 0.5
BuildRequires: mingw64-usbredir >= 0.5
BuildRequires: mingw32-json-glib
BuildRequires: mingw64-json-glib

BuildRequires: meson
BuildRequires: gcc
BuildRequires: git
BuildRequires: gettext
BuildRequires: python3-six
BuildRequires: python3-pyparsing
BuildRequires: gnupg2
# FIXME: shouldn't be necessary
BuildRequires: gobject-introspection-devel

%description
Client libraries for SPICE desktop servers.


# Mingw32
%package -n mingw32-spice-gtk3
Summary: %{summary}
Requires: mingw32-spice-glib = %{version}-%{release}
Requires: mingw32-gtk3
Requires: pkgconfig
Obsoletes: mingw32-spice-gtk < 0.32
Obsoletes: mingw32-spice-gtk-static < 0.32-2

%description -n mingw32-spice-gtk3
Gtk+3 client libraries for SPICE desktop servers.

%package -n mingw32-spice-glib
Summary: GLib-based library to connect to SPICE servers
Requires: pkgconfig
Requires: mingw32-glib2
Requires: mingw32-spice-protocol

%description -n mingw32-spice-glib
A SPICE client library using GLib2.

# Mingw64
%package -n mingw64-spice-gtk3
Summary: %{summary}
Requires: mingw64-spice-glib = %{version}-%{release}
Requires: mingw64-gtk3
Requires: pkgconfig
Obsoletes: mingw64-spice-gtk < 0.32
Obsoletes: mingw64-spice-gtk-static < 0.32-2

%description -n mingw64-spice-gtk3
Gtk+3 client libraries for SPICE desktop servers.

%package -n mingw64-spice-glib
Summary: GLib-based library to connect to SPICE servers
Requires: pkgconfig
Requires: mingw64-glib2
Requires: mingw64-spice-protocol

%description -n mingw64-spice-glib
A SPICE client library using GLib2.

%{?mingw_debug_package}


%prep
#gpgv2 --quiet --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}
%autosetup -S git_am -n spice-gtk-%{version}%{?_version_suffix}

%build

# meson macro has --auto-features=enabled
# gstreamer should be enough, may be deprecated in the future
%global mjpegflag -Dbuiltin-mjpeg=false

%mingw_meson \
  %{mjpegflag} \
  -Dgtk_doc=disabled \
  -Dintrospection=disabled

%mingw_ninja

%install
export DESTDIR=%{buildroot}
%mingw_ninja install

# man pages don't need to be bundled
find $RPM_BUILD_ROOT -name "*.1" -delete

%mingw_find_lang spice-gtk --all-name

# Mingw32
%files -n mingw32-spice-glib -f mingw32-spice-gtk.lang
%doc AUTHORS
%doc COPYING
%doc README.md
%doc CHANGELOG.md
%{mingw32_bindir}/libspice-client-glib-2.0-8.dll
%{mingw32_bindir}/spicy-screenshot.exe
%{mingw32_bindir}/spicy-stats.exe
%{mingw32_libdir}/libspice-client-glib-2.0.dll.a
%{mingw32_libdir}/pkgconfig/spice-client-glib-2.0.pc
%{mingw32_includedir}/spice-client-glib-2.0

%files -n mingw32-spice-gtk3
%{mingw32_bindir}/libspice-client-gtk-3.0-5.dll
%{mingw32_bindir}/spicy.exe
%{mingw32_libdir}/libspice-client-gtk-3.0.dll.a
%{mingw32_libdir}/pkgconfig/spice-client-gtk-3.0.pc
%{mingw32_includedir}/spice-client-gtk-3.0

# Mingw64
%files -n mingw64-spice-glib -f mingw64-spice-gtk.lang
%doc AUTHORS
%doc COPYING
%doc README.md
%doc CHANGELOG.md
%{mingw64_bindir}/libspice-client-glib-2.0-8.dll
%{mingw64_bindir}/spicy-screenshot.exe
%{mingw64_bindir}/spicy-stats.exe
%{mingw64_libdir}/libspice-client-glib-2.0.dll.a
%{mingw64_libdir}/pkgconfig/spice-client-glib-2.0.pc
%{mingw64_includedir}/spice-client-glib-2.0

%files -n mingw64-spice-gtk3
%{mingw64_bindir}/libspice-client-gtk-3.0-5.dll
%{mingw64_bindir}/spicy.exe
%{mingw64_libdir}/libspice-client-gtk-3.0.dll.a
%{mingw64_libdir}/pkgconfig/spice-client-gtk-3.0.pc
%{mingw64_includedir}/spice-client-gtk-3.0

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 0.42-7
- convert license to SPDX

* Tue Jul 30 2024 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.42-6
- Fix FTBFS rhbz#2300965

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jan 23 2023 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.42-1
- new version

* Thu Jan 19 2023 Richard W.M. Jones <rjones@redhat.com> - 0.41-1
- New upstream version 0.41

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 0.40-3
- Rebuild with mingw-gcc-12

* Thu Feb 17 2022 Sandro Mani <manisandro@gmail.com> - 0.40-2
- Rebuild (openssl)

* Thu Feb 10 2022 Victor Toso <victortoso@redhat.com> - 0.40-1
- Update to 0.40

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 12 13:45:50 GMT 2020 Sandro Mani <manisandro@gmail.com> - 0.37-5
- Rebuild (mingw-gettext)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 10 2020 Eduardo Lima (Etrunko) <etrunko@redhat.com> - 0.37-3
- Fix spec issue with more than one package installing the same files

* Mon Apr 20 2020 Sandro Mani <manisandro@gmail.com> - 0.37-2
- Rebuild (gettext)

* Wed Feb 05 2020 Eduardo Lima (Etrunko) <etrunko@redhat.com> - 0.37-1
- Sync with native spice-gtk version 0.37

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 0.36-4
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 16 2019 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.36-1
- new version

* Fri Aug 24 2018 Richard W.M. Jones <rjones@redhat.com> - 0.35-2
- Rebuild for new mingw-openssl.

* Fri Aug 24 2018 Christophe Fergeau <cfergeau@redhat.com> - 0.35-1
- Update to spice-gtk 0.35

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.34-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.34-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jul 31 2017 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.34-1
- new version

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.33-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.33-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 15 2016 Victor Toso <victortoso@redhat.com> - 0.33-4
- Do not send unnecessary 0 bytes messages
  Resolves: https://bugs.freedesktop.org/show_bug.cgi?id=97227
- Fix hang over UsbDk failure and better error handling
  Resolves: https://bugs.freedesktop.org/show_bug.cgi?id=98686

* Tue Nov  8 2016 Victor Toso <victortoso@redhat.com> - 0.33-3
- Avoid crash on clipboard

* Mon Oct 31 2016 Victor Toso <victortoso@redhat.com> - 0.33-2
- Enable usbredir now with UsbDk integration in libusb

* Fri Oct 07 2016 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.33-1
- new version

* Tue Jun 28 2016 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.32-3
- Add missing Obsoletes for gtk2 and static packages

* Wed Jun 22 2016 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.32-2
- Remove static libraries

* Tue Jun 21 2016 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.32-1
- Update to spice-gtk 0.32 release

* Fri Mar 11 2016 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.31-1
- Update to spice-gtk 0.31 release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 07 2015 Christophe Fergeau <cfergeau@redhat.com> 0.30-1
- Update to spice-gtk 0.30

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 15 2015 Marc-André Lureau <marcandre.lureau@redhat.com> 0.29-1
- Update to spice-gtk 0.29

* Wed Mar  4 2015 Marc-André Lureau <marcandre.lureau@redhat.com> 0.28-1
- Update to spice-gtk 0.28

* Tue Jan  6 2015 Fabiano Fidêncio <fidencio@redhat.com> 0.27.4
- Drop gstreamer-0.10 in favour to gstreamer-1.0

* Mon Dec 22 2014 Marc-André Lureau <marcandre.lureau@redhat.com> 0.27-3
- Fix usbredir crash on disconnection.

* Tue Dec 16 2014 Marc-André Lureau <marcandre.lureau@redhat.com> 0.27-2
- Fix authentication error handling regression.

* Thu Dec 11 2014 Marc-André Lureau <marcandre.lureau@redhat.com> 0.27-1
- Update to spice-gtk 0.27

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 10 2014 Marc-André Lureau <marcandre.lureau@redhat.com> 0.23-1
- Update to spice-gtk 0.23

* Wed Dec 18 2013 Marc-André Lureau <marcandre.lureau@redhat.com> 0.22-1
- Update to spice-gtk 0.22

* Wed Sep 18 2013 Marc-André Lureau <marcandre.lureau@redhat.com> 0.21-1
- Update to spice-gtk 0.21

* Thu Aug 01 2013 Christophe Fergeau <cfergeau@redhat.com> 0.20-1
- Update to spice-gtk 0.20

* Sun Jun 16 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.19-3
- Rebuild to resolve InterlockedCompareExchange regression in mingw32 libraries

* Sat Jun 15 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.19-2
- Rebuild to resolve InterlockedCompareExchange regression in mingw32 libraries

* Thu Apr 11 2013 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.19-1
- Update to spice-gtk 0.19

* Wed Feb 13 2013 Christophe Fergeau <cfergeau@redhat.com> - 0.18-1
- Update to spice-gtk 0.18

* Wed Feb  6 2013 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.17-1
- Update to spice-gtk 0.17

* Thu Jan 24 2013 Christophe Fergeau <cfergeau@redhat.com> - 0.16-2
- Add missing Requires (spice-protocol is required by
  spice-client-glib-2.0.pc)

* Tue Jan 22 2013 Christophe Fergeau <cfergeau@redhat.com> - 0.16-1
- Update to spice-gtk 0.16

* Fri Dec 21 2012 Christophe Fergeau <cfergeau@redhat.com> - 0.15-2
- Update to the 0.15 release

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May 11 2012 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.12-2
- Remove spice-protocol dependency

* Wed May  2 2012 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.12-1
- Initial mingw64 packaging
