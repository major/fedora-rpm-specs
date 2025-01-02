%{?mingw_package_header}

Name:           mingw-gtk2
Version:        2.24.33
Release:        14%{?dist}
Summary:        MinGW Windows Gtk2 library

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://www.gtk.org
Source0:        http://download.gnome.org/sources/gtk+/2.24/gtk+-%{version}.tar.xz
BuildArch:      noarch

# wine %{mingw32_bindir}/gtk-query-immodules-2.0.exe > gtk.immodules
Source1:        gtk.immodules

Patch1:         system-python.patch
# https://bugzilla.gnome.org/show_bug.cgi?id=583273
Patch2:         icon-padding.patch
# https://bugzilla.gnome.org/show_bug.cgi?id=599618
Patch3:         tooltip-positioning.patch
# https://bugzilla.gnome.org/show_bug.cgi?id=611313
Patch4:         window-dragging.patch
# Fix use of extended buttons in gtkstatusicon.
Patch5:         mingw32-gtk2-2.15.0-xbuttons.patch
# Enable building a static library of GTK
Patch6:         mingw32-gtk2-enable_static_build.patch
# Fix incompatible pointer types
Patch7:         gtk-incompat-pointer-type.patch
# Avoid implicit function declaration
Patch8:         gtk-implicit-decl.patch
# Assorted build fixes
Patch10:        gtk2-c99.patch
Patch11:        gtk2-c89.patch
Patch12:        gtk2-c89-2.patch
Patch13:        gtk2-c89-3.patch
Patch14:        gtk2-c89-4.patch
Patch15:        gtk2-c89-5.patch
Patch16:        gtk2-c89-6.patch


BuildRequires: make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-atk
BuildRequires:  mingw32-cairo
BuildRequires:  mingw32-gettext
BuildRequires:  mingw32-glib2
BuildRequires:  mingw32-win-iconv
BuildRequires:  mingw32-pango
BuildRequires:  mingw32-gdk-pixbuf
BuildRequires:  mingw32-pixman
BuildRequires:  mingw32-zlib

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-atk
BuildRequires:  mingw64-cairo
BuildRequires:  mingw64-gettext
BuildRequires:  mingw64-glib2
BuildRequires:  mingw64-win-iconv
BuildRequires:  mingw64-pango
BuildRequires:  mingw64-gdk-pixbuf
BuildRequires:  mingw64-pixman
BuildRequires:  mingw64-zlib

BuildRequires:  pkgconfig

# Native one for msgfmt
BuildRequires:  gettext
# Native one for glib-genmarsjal
BuildRequires:  glib2-devel
# Native one for gtk-update-icon-cache
BuildRequires:  gtk-update-icon-cache
# Native one for gdk-pixbuf-csource
BuildRequires:  gtk2-devel
# Packages needed for regenerating configure
BuildRequires:  gtk-doc
BuildRequires:  gobject-introspection-devel

# Needed for the patch
BuildRequires:  autoconf automake libtool


%description
MinGW Windows Gtk2 library.


# Win32
%package -n mingw32-gtk2
Summary:        MinGW Windows Gtk2 library
# built as a subpackage of mingw-gtk3
Requires:       mingw32-gtk-update-icon-cache

%description -n mingw32-gtk2
MinGW Windows Gtk2 library.

%package -n mingw32-gtk2-static
Summary:        Static version of the MinGW Windows Gtk2 library
Requires:       mingw32-gtk2 = %{version}-%{release}

%description -n mingw32-gtk2-static
Static version of the MinGW Windows Gtk2 library.

# Win64
%package -n mingw64-gtk2
Summary:        MinGW Windows Gtk2 library
# built as a subpackage of mingw-gtk3
Requires:       mingw64-gtk-update-icon-cache

%description -n mingw64-gtk2
MinGW Windows Gtk2 library.

%package -n mingw64-gtk2-static
Summary:        Static version of the MinGW Windows Gtk2 library
Requires:       mingw64-gtk2 = %{version}-%{release}

%description -n mingw64-gtk2-static
Static version of the MinGW Windows Gtk2 library.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n gtk+-%{version}


%build
%mingw_configure --disable-cups --enable-static

# The pre-generated gtk.def file can't be used for MinGW-W64
# Force a regeneration of this file by removing the bundled copy
rm -f gtk/gtk.def

%mingw_make_build


%install
%mingw_make_install

rm -f %{buildroot}/%{mingw32_libdir}/charset.alias
rm -f %{buildroot}/%{mingw64_libdir}/charset.alias

# Remove manpages which duplicate those in Fedora native.
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}

# Remove documentation too.
rm -rf %{buildroot}%{mingw32_datadir}/gtk-doc
rm -rf %{buildroot}%{mingw64_datadir}/gtk-doc

# The .def files are only used while compiling the libraries themselves
# (they contain a list of functions which need to be exported by the linker)
# so they serve no purpose for other libraries and applications
rm -f %{buildroot}%{mingw32_libdir}/*.def
rm -f %{buildroot}%{mingw64_libdir}/*.def

# Install the gtk.immodules file
mkdir -p %{buildroot}%{mingw32_sysconfdir}/gtk-2.0/
mkdir -p %{buildroot}%{mingw64_sysconfdir}/gtk-2.0/
install -m 0644 %{SOURCE1} %{buildroot}%{mingw32_sysconfdir}/gtk-2.0/
install -m 0644 %{SOURCE1} %{buildroot}%{mingw64_sysconfdir}/gtk-2.0/

# Drop all .la files
find %{buildroot} -name "*.la" -delete

# Drop the .dll.a files for all modules as nothing is supposed
# to link directly to these modules
rm -f %{buildroot}%{mingw32_libdir}/gtk-2.0/2.10.0/*/*.dll.a
rm -f %{buildroot}%{mingw64_libdir}/gtk-2.0/2.10.0/*/*.dll.a
rm -f %{buildroot}%{mingw32_libdir}/gtk-2.0/modules/*.dll.a
rm -f %{buildroot}%{mingw64_libdir}/gtk-2.0/modules/*.dll.a

# gtk-update-icon-cache.exe is now shipped in mingw-gtk3
rm -f %{buildroot}%{mingw32_bindir}/gtk-update-icon-cache.exe
rm -f %{buildroot}%{mingw64_bindir}/gtk-update-icon-cache.exe

%mingw_find_lang gtk2 --all-name


# Win32
%files -n mingw32-gtk2 -f mingw32-gtk2.lang
%license COPYING
%{mingw32_datadir}/themes/*
%{mingw32_bindir}/gtk-builder-convert
%{mingw32_bindir}/gtk-demo.exe
%{mingw32_bindir}/gtk-query-immodules-2.0.exe
%{mingw32_bindir}/libgailutil-18.dll
%{mingw32_bindir}/libgdk-win32-2.0-0.dll
%{mingw32_bindir}/libgtk-win32-2.0-0.dll
%dir %{mingw32_libdir}/gtk-2.0
%dir %{mingw32_libdir}/gtk-2.0/2.10.0
%dir %{mingw32_libdir}/gtk-2.0/2.10.0/engines
%{mingw32_libdir}/gtk-2.0/2.10.0/engines/libpixmap.dll
%{mingw32_libdir}/gtk-2.0/2.10.0/engines/libwimp.dll
%dir %{mingw32_libdir}/gtk-2.0/2.10.0/immodules
%{mingw32_libdir}/gtk-2.0/2.10.0/immodules/im-am-et.dll
%{mingw32_libdir}/gtk-2.0/2.10.0/immodules/im-cedilla.dll
%{mingw32_libdir}/gtk-2.0/2.10.0/immodules/im-cyrillic-translit.dll
%{mingw32_libdir}/gtk-2.0/2.10.0/immodules/im-ime.dll
%{mingw32_libdir}/gtk-2.0/2.10.0/immodules/im-inuktitut.dll
%{mingw32_libdir}/gtk-2.0/2.10.0/immodules/im-ipa.dll
%{mingw32_libdir}/gtk-2.0/2.10.0/immodules/im-multipress.dll
%{mingw32_libdir}/gtk-2.0/2.10.0/immodules/im-thai.dll
%{mingw32_libdir}/gtk-2.0/2.10.0/immodules/im-ti-er.dll
%{mingw32_libdir}/gtk-2.0/2.10.0/immodules/im-ti-et.dll
%{mingw32_libdir}/gtk-2.0/2.10.0/immodules/im-viqr.dll
%{mingw32_libdir}/gtk-2.0/include/
%dir %{mingw32_libdir}/gtk-2.0/modules
%{mingw32_libdir}/gtk-2.0/modules/libgail.dll
%{mingw32_libdir}/libgailutil.dll.a
%{mingw32_libdir}/libgdk-win32-2.0.dll.a
%{mingw32_libdir}/libgtk-win32-2.0.dll.a
%{mingw32_libdir}/pkgconfig/gail.pc
%{mingw32_libdir}/pkgconfig/gdk-2.0.pc
%{mingw32_libdir}/pkgconfig/gdk-win32-2.0.pc
%{mingw32_libdir}/pkgconfig/gtk+-2.0.pc
%{mingw32_libdir}/pkgconfig/gtk+-win32-2.0.pc
%{mingw32_includedir}/gtk-2.0/
%{mingw32_includedir}/gail-1.0/
%{mingw32_sysconfdir}/gtk-2.0/
%{mingw32_datadir}/aclocal/gtk-2.0.m4
%{mingw32_datadir}/gtk-2.0/

%files -n mingw32-gtk2-static
%{mingw32_libdir}/libgailutil.a
%{mingw32_libdir}/libgdk-win32-2.0.a
%{mingw32_libdir}/libgtk-win32-2.0.a
%{mingw32_libdir}/gtk-2.0/2.10.0/engines/libpixmap.a
%{mingw32_libdir}/gtk-2.0/2.10.0/engines/libwimp.a
%{mingw32_libdir}/gtk-2.0/2.10.0/immodules/im-am-et.a
%{mingw32_libdir}/gtk-2.0/2.10.0/immodules/im-cedilla.a
%{mingw32_libdir}/gtk-2.0/2.10.0/immodules/im-cyrillic-translit.a
%{mingw32_libdir}/gtk-2.0/2.10.0/immodules/im-ime.a
%{mingw32_libdir}/gtk-2.0/2.10.0/immodules/im-inuktitut.a
%{mingw32_libdir}/gtk-2.0/2.10.0/immodules/im-ipa.a
%{mingw32_libdir}/gtk-2.0/2.10.0/immodules/im-multipress.a
%{mingw32_libdir}/gtk-2.0/2.10.0/immodules/im-thai.a
%{mingw32_libdir}/gtk-2.0/2.10.0/immodules/im-ti-er.a
%{mingw32_libdir}/gtk-2.0/2.10.0/immodules/im-ti-et.a
%{mingw32_libdir}/gtk-2.0/2.10.0/immodules/im-viqr.a
%{mingw32_libdir}/gtk-2.0/modules/libgail.a

# Win64
%files -n mingw64-gtk2 -f mingw64-gtk2.lang
%license COPYING
%{mingw64_datadir}/themes/*
%{mingw64_bindir}/gtk-builder-convert
%{mingw64_bindir}/gtk-demo.exe
%{mingw64_bindir}/gtk-query-immodules-2.0.exe
%{mingw64_bindir}/libgailutil-18.dll
%{mingw64_bindir}/libgdk-win32-2.0-0.dll
%{mingw64_bindir}/libgtk-win32-2.0-0.dll
%dir %{mingw64_libdir}/gtk-2.0
%dir %{mingw64_libdir}/gtk-2.0/2.10.0
%dir %{mingw64_libdir}/gtk-2.0/2.10.0/engines
%{mingw64_libdir}/gtk-2.0/2.10.0/engines/libpixmap.dll
%{mingw64_libdir}/gtk-2.0/2.10.0/engines/libwimp.dll
%dir %{mingw64_libdir}/gtk-2.0/2.10.0/immodules
%{mingw64_libdir}/gtk-2.0/2.10.0/immodules/im-am-et.dll
%{mingw64_libdir}/gtk-2.0/2.10.0/immodules/im-cedilla.dll
%{mingw64_libdir}/gtk-2.0/2.10.0/immodules/im-cyrillic-translit.dll
%{mingw64_libdir}/gtk-2.0/2.10.0/immodules/im-ime.dll
%{mingw64_libdir}/gtk-2.0/2.10.0/immodules/im-inuktitut.dll
%{mingw64_libdir}/gtk-2.0/2.10.0/immodules/im-ipa.dll
%{mingw64_libdir}/gtk-2.0/2.10.0/immodules/im-multipress.dll
%{mingw64_libdir}/gtk-2.0/2.10.0/immodules/im-thai.dll
%{mingw64_libdir}/gtk-2.0/2.10.0/immodules/im-ti-er.dll
%{mingw64_libdir}/gtk-2.0/2.10.0/immodules/im-ti-et.dll
%{mingw64_libdir}/gtk-2.0/2.10.0/immodules/im-viqr.dll
%{mingw64_libdir}/gtk-2.0/include/
%dir %{mingw64_libdir}/gtk-2.0/modules
%{mingw64_libdir}/gtk-2.0/modules/libgail.dll
%{mingw64_libdir}/libgailutil.dll.a
%{mingw64_libdir}/libgdk-win32-2.0.dll.a
%{mingw64_libdir}/libgtk-win32-2.0.dll.a
%{mingw64_libdir}/pkgconfig/gail.pc
%{mingw64_libdir}/pkgconfig/gdk-2.0.pc
%{mingw64_libdir}/pkgconfig/gdk-win32-2.0.pc
%{mingw64_libdir}/pkgconfig/gtk+-2.0.pc
%{mingw64_libdir}/pkgconfig/gtk+-win32-2.0.pc
%{mingw64_includedir}/gtk-2.0/
%{mingw64_includedir}/gail-1.0/
%{mingw64_sysconfdir}/gtk-2.0/
%{mingw64_datadir}/aclocal/gtk-2.0.m4
%{mingw64_datadir}/gtk-2.0/

%files -n mingw64-gtk2-static
%{mingw64_libdir}/libgailutil.a
%{mingw64_libdir}/libgdk-win32-2.0.a
%{mingw64_libdir}/libgtk-win32-2.0.a
%{mingw64_libdir}/gtk-2.0/2.10.0/engines/libpixmap.a
%{mingw64_libdir}/gtk-2.0/2.10.0/engines/libwimp.a
%{mingw64_libdir}/gtk-2.0/2.10.0/immodules/im-am-et.a
%{mingw64_libdir}/gtk-2.0/2.10.0/immodules/im-cedilla.a
%{mingw64_libdir}/gtk-2.0/2.10.0/immodules/im-cyrillic-translit.a
%{mingw64_libdir}/gtk-2.0/2.10.0/immodules/im-ime.a
%{mingw64_libdir}/gtk-2.0/2.10.0/immodules/im-inuktitut.a
%{mingw64_libdir}/gtk-2.0/2.10.0/immodules/im-ipa.a
%{mingw64_libdir}/gtk-2.0/2.10.0/immodules/im-multipress.a
%{mingw64_libdir}/gtk-2.0/2.10.0/immodules/im-thai.a
%{mingw64_libdir}/gtk-2.0/2.10.0/immodules/im-ti-er.a
%{mingw64_libdir}/gtk-2.0/2.10.0/immodules/im-ti-et.a
%{mingw64_libdir}/gtk-2.0/2.10.0/immodules/im-viqr.a
%{mingw64_libdir}/gtk-2.0/modules/libgail.a


%changelog
* Tue Dec 31 2024 Sandro Mani <manisandro@gmail.com> - 2.24.33-14
- Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 2.24.33-13
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.33-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.33-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.33-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.33-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.33-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.33-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 2.24.33-6
- Rebuild with mingw-gcc-12

* Tue Feb 01 2022 Sandro Mani <manisandro@gmail.com> - 2.24.33-5
- Use python3

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.33-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.33-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 05 2021 Sandro Mani <manisandro@gmail.com> - 2.24.33-1
- Update to 2.24.33

* Wed Aug 12 13:39:01 GMT 2020 Sandro Mani <manisandro@gmail.com> - 2.24.32-7
- Rebuild (mingw-gettext)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.32-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 20 2020 Sandro Mani <manisandro@gmail.com> - 2.24.32-5
- Rebuild (gettext)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.32-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 2.24.32-3
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 05 2019 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.24.32-1
- Update to 2.24.32

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.31-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.31-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.31-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.31-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.31-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 24 2016 Kalev Lember <klember@redhat.com> - 2.24.31-2
- Depend on gtk-update-icon-cache that is now split out in a subpackage

* Fri Oct 07 2016 Kalev Lember <klember@redhat.com> - 2.24.31-1
- Update to 2.24.31
- Don't set group tags

* Mon May 09 2016 Kalev Lember <klember@redhat.com> - 2.24.30-1
- Update to 2.24.30

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Dec 12 2015 Kalev Lember <klember@redhat.com> - 2.24.29-1
- Update to 2.24.29

* Sat Aug 15 2015 Kalev Lember <klember@redhat.com> - 2.24.28-1
- Update to 2.24.28

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 25 2015 Kalev Lember <kalevlember@gmail.com> - 2.24.27-2
- Drop gtk-update-icon-cache.exe which is now shipped in mingw-gtk3

* Tue Mar 24 2015 Kalev Lember <kalevlember@gmail.com> - 2.24.27-1
- Update to 2.24.27
- Use license macro for the COPYING file

* Tue Oct 14 2014 Kalev Lember <kalevlember@gmail.com> - 2.24.25-1
- Update to 2.24.25

* Wed Jul 30 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.24.24-2
- Fix build failure on environments with older gtk-doc

* Tue Jul 22 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.24.24-1
- Update to 2.24.24

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Kalev Lember <kalevlember@gmail.com> - 2.24.23-1
- Update to 2.24.23

* Tue Feb 11 2014 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.24.22-2
- Patch for Gdk 16bpp memory leak (RHBZ #1063709, GNOME BZ #671538)

* Sun Oct 13 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.24.22-1
- Update to 2.24.22

* Tue Sep 24 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.24.21-1
- Update to 2.24.21

* Sun Aug  4 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.24.20-3
- Prevent segfault in GtkFileChooserButton caused by the use
  of an invalidated iter in GtkComboBox (RHBZ #985559, GNOME BZ #704508)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul  7 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.24.20-1
- Update to 2.24.20

* Sun Jun 16 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.24.19-1
- Update to 2.24.19

* Sun Jun 16 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.24.18-2
- Rebuild to resolve InterlockedCompareExchange regression in mingw32 libraries

* Tue May 14 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.24.18-1
- Update to 2.24.18

* Thu Apr  4 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.24.17-2
- Workaround knownfolders.h linker issue when using a recent mingw-w64 snapshot

* Sun Mar 24 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.24.17-1
- Update to 2.24.17

* Sun Mar  3 2013 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.24.16-1
- Update to 2.24.16

* Sun Feb 10 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.24.15-1
- Update to 2.24.15

* Wed Jan 16 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.24.14-2
- Workaround broken automake 1.13.1

* Thu Dec 06 2012 Kalev Lember <kalevlember@gmail.com> - 2.24.14-1
- Update to 2.24.14

* Fri Oct  5 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.24.13-1
- Update to 2.24.13

* Sat Sep 22 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.24.12-1
- Update to 2.24.12

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012 Kalev Lember <kalevlember@gmail.com> - 2.24.11-1
- Update to 2.24.11

* Sun Mar 18 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.24.10-5
- Added win64 support

* Fri Mar 09 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.24.10-4
- Fix linking against modern glib2

* Tue Mar 06 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.24.10-3
- Renamed the source package to mingw-gtk2 (RHBZ #800392)
- Use mingw macros without leading underscore

* Tue Feb 28 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.24.10-2
- Rebuild against the mingw-w64 toolchain

* Thu Feb 09 2012 Kalev Lember <kalevlember@gmail.com> - 2.24.10-1
- Update to 2.24.10
- Drop an upstreamed patch

* Wed Feb  1 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.24.9-1
- Update to 2.24.9
- Dropped the .la files
- Dropped the .dll.a files for all modules
- Fix gmodule linker failure when using the latest pango

* Tue Jan 31 2012 Kalev Lember <kalevlember@gmail.com> - 2.24.8-3
- Rebuilt for libpng 1.5

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 10 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.24.8-1
- Update to 2.24.8
- Make sure the autotools don't get triggered

* Tue Oct 18 2011 Kalev Lember <kalevlember@gmail.com> - 2.24.7-1
- Update to 2.24.7
- Switch to .xz tarballs

* Sun Jul 10 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.24.5-1
- Update to 2.24.5

* Wed Jul 06 2011 Kalev Lember <kalevlember@gmail.com> - 2.24.4-2
- Rebuilt against win-iconv

* Wed Apr 27 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.24.4-1
- Update to 2.24.4
- Dropped the proxy-libintl pieces

* Sun Feb 13 2011 Thomas Sailer <sailer@fedoraproject.org> - 2.24.0-1
- update to 2.24.0

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.22.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Nov  7 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.22.0-2
- Rebuild in order to have soft dependency on libintl

* Thu Sep 23 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.22.0-1
- Update to 2.22.0

* Fri Sep 17 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.21.8-1
- Update to 2.21.8
- Fixed a small rpmlint warning

* Sun Sep 12 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.21.7-1
- Update to 2.21.7
- Dropped upstreamed WIMP theme patch
- Moved all gdk-pixbuf bits to a seperate package as upstream has separated it
- Added BR: mingw32-gdk-pixbuf

* Sun Jul  4 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.20.1-2
- Re-enable the WIMP theme now that upstream has provided a fix for it (RHBZ #608911, GNOME BZ #598299)
- Rebuild against libpng 1.4.3

* Fri Jun 11 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.20.1-1
- Update to 2.20.1

* Wed Feb 24 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.19.6-1
- Update to 2.19.6

* Tue Feb  2 2010 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.19.4-1
- Update to 2.19.4

* Wed Dec  2 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.19.1-1
- Update to 2.19.1
- Dropped the autoreconf call

* Sun Nov 29 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.19.0-1
- Update to 2.19.0
- Added BR: gtk-doc

* Sat Oct 17 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.18.3-1
- Update to 2.18.3
- Drop upstreamed patch (GNOME BZ #597535)
- Re-enable GDI+ support as it's fixed upstream (GNOME BZ #552678)
- This release contains a workaround for a rendering bug which got
  introduced during the CSW merge (GNOME BZ #598299)

* Tue Oct  6 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.18.2-1
- Update to 2.18.2

* Thu Oct  1 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.18.1-1
- Update to 2.18.1

* Wed Sep 23 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.18.0-1
- Update to 2.18.0
- Drop upstreamed patch

* Sun Sep 20 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.17.11-3
- Use relative paths instead of absolute paths in the gdk-pixbuf.loaders file
- Added the gtk.immodules file (BZ #522957)

* Fri Sep 18 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.17.11-2
- Rebuild because of broken mingw32-gcc/mingw32-binutils

* Sat Sep  5 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.17.11-1
- Update to 2.17.11

* Tue Sep  1 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.17.10-1
- Update to 2.17.10

* Thu Aug 27 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.17.9-1
- Update to 2.17.9
- Rebuild against mingw32-libjpeg 7

* Tue Aug 18 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.17.8-1
- Update to 2.17.8

* Thu Aug 13 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.17.7-1
- Update to 2.17.7
- Automatically generate debuginfo subpackage
- Add --with-libjasper to the ./configure command

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 10 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.17.1-1
- Update to 2.17.1
- Use %%global instead of %%define
- The -static subpackage was missing a Group: declaration
- Drop upstreamed patch
- Add BR: mingw32-libtiff
- Updated the gdk-pixbuf.loaders file for libtiff support

* Fri May 22 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.16.1-2
- don't open double browser windows from about dialogs
  (patch is from the native gtk2 package)

* Sat Apr 18 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.16.1-1
- Update to 2.16.1

* Fri Mar 13 2009 Richard W.M. Jones <rjones@redhat.com> - 2.15.5-2
- Force build against latest mingw32-filesystem.

* Sun Mar 8 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.15.5-1
- Update to 2.15.5
- Disable gdiplus support for now because of GNOME BZ#552678
- Use the ./configure flag --without-libtiff until mingw32-libtiff is packaged
- Fixed the %%defattr line
- Dropped the .def files as they aren't used anymore after compilation
- Added -static subpackage

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.15.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb  6 2009 Richard W.M. Jones <rjones@redhat.com> - 2.15.0-3
- Remove documentation.
- Add license file.
- Added extra BRs suggested by auto-buildrequires.

* Fri Jan 30 2009 Richard W.M. Jones <rjones@redhat.com> - 2.15.0-2
- Requires pkgconfig.

* Fri Jan 23 2009 Richard W.M. Jones <rjones@redhat.com> - 2.15.0-1
- Rebase to Fedora native version 2.15.0.
- Disable static libraries.
- Use _smp_mflags.
- Use find_lang macro.

* Mon Oct 27 2008 Richard W.M. Jones <rjones@redhat.com> - 2.14.4-3
- Remove preun script, no longer used.

* Fri Oct 24 2008 Richard W.M. Jones <rjones@redhat.com> - 2.14.4-1
- New upstream version 2.14.4.
- Require cairo >= 1.8.0 because of important fixes.
- Remove a couple of patches which are now upstream.

* Fri Oct 10 2008 Richard W.M. Jones <rjones@redhat.com> - 2.14.2-3
- Remove the requirement for Wine at build or install time.
- Conflicts with (native) cups-devel.

* Wed Sep 24 2008 Richard W.M. Jones <rjones@redhat.com> - 2.14.2-2
- Rename mingw -> mingw32.

* Mon Sep 22 2008 Daniel P. Berrange <berrange@redhat.com> - 2.14.2-1
- Update to 2.14.2 release

* Sun Sep 21 2008 Richard W.M. Jones <rjones@redhat.com> - 2.14.0-5
- Remove manpages duplicating those in Fedora native packages.

* Thu Sep 11 2008 Daniel P. Berrange <berrange@redhat.com> - 2.14.0-4
- Added dep on pkgconfig, gettext and glib2 (native)

* Thu Sep 11 2008 Richard W.M. Jones <rjones@redhat.com> - 2.14.0-3
- post/preun scripts to update the gdk-pixbuf.loaders list.

* Wed Sep 10 2008 Richard W.M. Jones <rjones@redhat.com> - 2.14.0-2
- Jasper DLLs now fixed.
- Fix source URL.
- Run the correct glib-mkenums.

* Tue Sep  9 2008 Daniel P. Berrange <berrange@redhat.com> - 2.14.0-1
- Initial RPM release
