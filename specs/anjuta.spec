# The Python templates in /usr/share/anjuta/project can not be byte-compiled.
%global _python_bytecompile_errors_terminate_build 0

%if 0%{?fedora}
%global with_python3 1
%else
%global with_python3 0
%endif

Name:           anjuta
Epoch:          1
Version:        3.34.0
Release:        27%{?dist}
Summary:        GNOME IDE for various programming languages (including C/C++, Python, Vala and JavaScript)

License:        GPL-2.0-or-later
URL:            http://www.anjuta.org/
Source0:        http://download.gnome.org/sources/anjuta/3.34/%{name}-%{version}.tar.xz
Patch0:         cpp-java.patch
Patch1:         webkit-4.1.patch
Patch2:         autoconf-2.72.patch
Patch3:         pointer-types.patch

BuildRequires:  autogen
BuildRequires:  chrpath
BuildRequires:  desktop-file-utils
BuildRequires:  devhelp-devel >= 3.0.0
BuildRequires:  gettext
BuildRequires:  glade-devel
BuildRequires:  graphviz-devel
BuildRequires:  gtksourceview3-devel >= 2.91.8
BuildRequires:  intltool
BuildRequires:  libgda5-devel >= 5.1.0
BuildRequires:  libgdl-devel >= 2.91.4
BuildRequires:  libuuid-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  neon-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Locale::gettext)
BuildRequires:  perl(XML::Parser)
%if 0%{?with_python3}
BuildRequires:  python3-devel
%else
BuildRequires:  python-devel
%endif
BuildRequires:  sqlite-devel
BuildRequires:  subversion-devel
BuildRequires:  vala-devel
BuildRequires:  vte291-devel
BuildRequires:  libxml2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  itstool
BuildRequires:  libappstream-glib
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  gnome-common
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  gtk-doc

Requires:       autogen
Requires:       gdb >= 7.0
Requires:       git
Requires:       hicolor-icon-theme
Requires:       libgda5-sqlite >= 5.1.0
Requires:       automake
Requires:       autoconf
Requires:       %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description
Anjuta DevStudio is a versatile software development studio featuring
a number of advanced programming facilities including project
management, application wizard, interactive debugger, source editor,
version control, GUI designer, profiler and many more tools. It
focuses on providing simple and usable user interface, yet powerful
for efficient development.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
This package contains development files for %{name}.

%package libs
Summary:        Libraries for %{name}

%description libs
This package contains library files for %{name}.

%prep
%setup -q

%patch -P 0 -p0 -b .cpp-java
%patch -P 1 -p1 -b .webkit
%patch -P 2 -p1 -b .autoconf
%patch -P 3 -p0 -b .pointer

%build
autoreconf -fi
%if 0%{?with_python3}
export PYTHON=%{__python3}
%endif
%configure \
  --disable-compile-warnings \
  --disable-schemas-compile \
  --disable-silent-rules \
  --disable-static \
  --enable-introspection \
  --enable-plugin-devhelp \
  --enable-plugin-glade \
  --enable-plugin-subversion

# Omit unused direct shared library dependencies.
sed --in-place --expression 's! -shared ! -Wl,--as-needed\0!g' libtool

make %{?_smp_mflags}


%install
%make_install
find $RPM_BUILD_ROOT -type f -name "*.la" -delete

# Update the screenshot shown in the software center
#
# NOTE: It would be *awesome* if this file was pushed upstream.
#
# See http://people.freedesktop.org/~hughsient/appdata/#screenshots for more details.
#
appstream-util replace-screenshots $RPM_BUILD_ROOT%{_datadir}/metainfo/anjuta.appdata.xml \
  https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/anjuta/a.png \
  https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/anjuta/b.png 

# Remove lib64 rpaths
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/anjuta
for f in $RPM_BUILD_ROOT%{_libdir}/anjuta/*.so ; do
    chrpath --delete $f
done

# Use %%doc instead.
rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}

%find_lang %{name} --all-name --with-gnome


%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/anjuta.desktop


%files -f %{name}.lang
%doc AUTHORS
%doc MAINTAINERS
%doc NEWS
%doc ROADMAP
%{_bindir}/%{name}
%{_bindir}/%{name}-launcher
%{_bindir}/%{name}-tags
%{_datadir}/applications/anjuta.desktop
%{_datadir}/icons/hicolor/*/apps/anjuta.png
%{_datadir}/icons/hicolor/*/mimetypes/application-x-anjuta.png
%{_datadir}/icons/hicolor/scalable/apps/anjuta.svg
%{_datadir}/icons/hicolor/scalable/mimetypes/application-x-anjuta.svg
%{_datadir}/icons/hicolor/symbolic/apps/anjuta-symbolic.svg
%{_datadir}/metainfo/anjuta.appdata.xml
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/anjuta/
%{_datadir}/glib-2.0/schemas/org.gnome.anjuta*.gschema.xml
%{_datadir}/pixmaps/anjuta/
%{_mandir}/man1/anjuta.1*
%{_mandir}/man1/anjuta-launcher.1*

%files devel
%doc doc/ScintillaDoc.html
%{_libdir}/libanjuta-3.so
%{_libdir}/pkgconfig/libanjuta-3.0.pc
%{_datadir}/gir-1.0/Anjuta-3.0.gir
%{_datadir}/gir-1.0/IAnjuta-3.0.gir

%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%dir %{_datadir}/gtk-doc/html/libanjuta
%doc %{_datadir}/gtk-doc/html/libanjuta/*

%dir %{_includedir}/libanjuta-3.0
%{_includedir}/libanjuta-3.0/libanjuta

%files libs
%license COPYING
%{_libdir}/anjuta/
%{_libdir}/girepository-1.0/Anjuta-3.0.typelib
%{_libdir}/girepository-1.0/IAnjuta-3.0.typelib
%{_libdir}/libanjuta-3.so.*

%changelog
* Sat Feb 01 2025 Björn Esser <besser82@fedoraproject.org> - 1:3.34.0-27
- Add explicit BR: libxcrypt-devel

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.34.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jan 08 2025 Gwyn Ciesla <gwync@protonmail.com> - 1:3.34.0-25
- Fix FTBFS

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.34.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 31 2024 Gwyn Ciesla <gwync@protonmail.com> - 1:3.34.0-23
- Patch for modern C.

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.34.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.34.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.34.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 08 2023 Gwyn Ciesla <gwync@protonmail.com> - 1:3.34.0-19
- migrated to SPDX license

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.34.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov 18 2022 Gwyn Ciesla <gwync@protonmail.com> - 1:3.34.0-17
- Patch for autoconf 2.72

* Fri Sep 23 2022 Gwyn Ciesla <gwync@protonmail.com> - 1:3.34.0-16
- Fix libgda requires.

* Thu Sep 01 2022 Gwyn Ciesla <gwync@protonmail.com> - 1:3.34.0-15
- Update webkit patch.

* Thu Aug 04 2022 Gwyn Ciesla <gwync@protonmail.com> - 1:3.34.0-14
- libgda rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.34.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.34.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 15 2021 Gwyn Ciesla <gwync@protonmail.com> - 1:3.34.0-11
- Patch for source file hang.

* Sun Nov 14 2021 Gwyn Ciesla <gwync@protonmail.com> - 1:3.34.0-10
- Split out libs package to reduce gtkpod footprint.

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.34.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.34.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Sep 13 2020 Kalev Lember <klember@redhat.com> - 1:3.34.0-7
- Rebuilt for libgladeui soname bump

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.34.0-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.34.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 01 2020 Gwyn Ciesla <gwync@protonmail.com> - 1:3.34.0-4
- Autogen rebuild

* Fri May 22 2020 Kalev Lember <klember@redhat.com> - 1:3.34.0-3
- Rebuilt for libgladeui soname bump

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.34.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 08 2019 Gwyn Ciesla <gwync@protonmail.com> - 1:3.34.0-1
- 3.34

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1:3.28.0-10
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.28.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.28.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Sep 07 2018 Kalev Lember <klember@redhat.com> - 1:3.28.0-7
- Rebuilt against fixed atk (#1626575)

* Fri Sep 07 2018 Kalev Lember <klember@redhat.com> - 1:3.28.0-6
- Rebuilt for libdevhelp soname bump

* Mon Aug 06 2018 Kalev Lember <klember@redhat.com> - 1:3.28.0-5
- Rebuilt for vala 0.42

* Fri Jul 20 2018 Gwyn Ciesla <limburgher@gmail.com> - 1:3.28.0-4
- BR fix.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.28.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1:3.28.0-2
- Rebuilt for Python 3.7

* Sun Mar 11 2018 Kalev Lember <klember@redhat.com> - 1:3.28.0-1
- Update to 3.28.0
- Remove ldconfig scriptlets

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:3.26.0-5
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.26.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:3.26.0-3
- Remove obsolete scriptlets

* Wed Dec 20 2017 Kalev Lember <klember@redhat.com> - 1:3.26.0-2
- Rebuilt for vala 0.40

* Sun Sep 10 2017 Kalev Lember <klember@redhat.com> - 1:3.26.0-1
- Update to 3.26.0

* Fri Aug 25 2017 Kalev Lember <klember@redhat.com> - 1:3.22.0-9
- Rebuilt for libdevhelp soname bump

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.22.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.22.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 21 2017 Kalev Lember <klember@redhat.com> - 1:3.22.0-6
- Rebuilt for libdevhelp soname bump

* Mon Feb 13 2017 Kalev Lember <klember@redhat.com> - 1:3.22.0-5
- Rebuilt for vala 0.36

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.22.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1:3.22.0-3
- Rebuild for Python 3.6

* Thu Sep 22 2016 Kalev Lember <klember@redhat.com> - 1:3.22.0-2
- Rebuilt for vala 0.34

* Mon Sep 19 2016 Kalev Lember <klember@redhat.com> - 1:3.22.0-1
- Update to 3.22.0
- Don't set group tags
- Move desktop-file-validate to the check section

* Mon Apr 11 2016 Jon Ciesla <limburgher@gmail.com> - 1:3.20.0-2
- Add Requires for autoconf, automake, BZ 1269674.

* Sun Mar 20 2016 Kalev Lember <klember@redhat.com> - 1:3.20.0-1
- Update to 3.20.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.18.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 15 2015 Mohammed El-Afifi <Mohammed_ElAfifi@yahoo.com> - 1:3.18.2-2
- Build with Python 3

* Tue Nov 10 2015 Kalev Lember <klember@redhat.com> - 1:3.18.2-1
- Update to 3.18.2

* Sun Sep 20 2015 Kalev Lember <klember@redhat.com> - 1:3.18.0-1
- Update to 3.18.0
- Include new symbolic icon
- Use make_install macro

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.16.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 27 2015 Kalev Lember <kalevlember@gmail.com> - 1:3.16.0-4
- Rebuilt for vala 0.30

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1:3.16.0-3
- Rebuilt for GCC 5 C++11 ABI change

* Mon Mar 30 2015 Richard Hughes <rhughes@redhat.com> - 1:3.16.0-2
- Use better AppData screenshots

* Sun Mar 22 2015 Kalev Lember <kalevlember@gmail.com> - 1:3.16.0-1
- Update to 3.16.0
- Use license macro for the COPYING file

* Sat Feb 21 2015 Kalev Lember <kalevlember@gmail.com> - 1:3.15.90-2
- Rebuilt for libvala soname bump

* Mon Jan 26 2015 Michael Catanzaro <mcatanzaro@gnome.org> - 1:3.15.90-1
- Update to 3.15.90

* Sun Sep 21 2014 Kalev Lember <kalevlember@gmail.com> - 1:3.14.0-1
- Update to 3.14.0

* Sun Sep 14 2014 Kalev Lember <kalevlember@gmail.com> - 1:3.13.92-1
- Update to 3.13.92
- Tighten -devel subpackage deps with the _isa macro

* Fri Aug 22 2014 Kalev Lember <kalevlember@gmail.com> - 1:3.13.90-2
- Switch to webkitgtk4

* Tue Aug 19 2014 Kalev Lember <kalevlember@gmail.com> - 1:3.13.90-1
- Update to 3.13.90
- Drop the gnome-icon-theme dep now that anjuta no longer installs icons there
- Switch to vte291

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.13.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 23 2014 Kalev Lember <kalevlember@gmail.com> - 1:3.13.1-5
- Rebuilt for vala 0.26

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 1:3.13.1-4
- Rebuilt for gobject-introspection 1.41.4

* Tue Jul 08 2014 Rex Dieter <rdieter@fedoraproject.org> 1:3.13.1-3
- optimize/update scriptlets

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 29 2014 Richard Hughes <rhughes@redhat.com> - 1:3.13.1-1
- Update to 3.13.1

* Tue Mar 25 2014 Richard Hughes <rhughes@redhat.com> - 1:3.12.0-1
- Update to 3.12.0

* Fri Mar 21 2014 Richard Hughes <rhughes@redhat.com> - 1:3.11.92-1
- Update to 3.11.92

* Sun Feb 23 2014 Richard Hughes <rhughes@redhat.com> - 1:3.11.90-1
- Update to 3.11.90

* Wed Jan 29 2014 Richard Hughes <rhughes@redhat.com> - 1:3.11.4-1
- Update to 3.11.4

* Mon Nov 18 2013 Richard Hughes <rhughes@redhat.com> - 1:3.10.2-1
- Update to 3.10.2

* Wed Sep 25 2013 Kalev Lember <kalevlember@gmail.com> - 1:3.10.0-1
- Update to 3.10.0

* Wed Sep 18 2013 Kalev Lember <kalevlember@gmail.com> - 1:3.9.92-1
- Update to 3.9.92

* Wed Sep 04 2013 Kalev Lember <kalevlember@gmail.com> - 1:3.9.91-2
- Rebuilt for libgladeui soname bump

* Tue Sep 03 2013 Kalev Lember <kalevlember@gmail.com> - 1:3.9.91-1
- Update to 3.9.91
- Remove lib64 rpaths

* Thu Aug 22 2013 Kalev Lember <kalevlember@gmail.com> - 1:3.9.90-1
- Update to 3.9.90
- Include the HighContrast icons

* Mon Aug 19 2013 Kalev Lember <kalevlember@gmail.com> - 1:3.9.5-2
- Rebuilt for libvala soname bump

* Sat Aug 10 2013 Kalev Lember <kalevlember@gmail.com> - 1:3.9.5-1
- Update to 3.9.5

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Petr Pisar <ppisar@redhat.com> - 1:3.9.4-2
- Perl 5.18 rebuild

* Tue Jul 16 2013 Richard Hughes <rhughes@redhat.com> - 1:3.9.4-1
- Update to 3.9.4

* Fri Jun 21 2013 Kalev Lember <kalevlember@gmail.com> - 1:3.9.3-1
- Update to 3.9.3

* Sun Jun 02 2013 Kalev Lember <kalevlember@gmail.com> - 1:3.9.2-1
- Update to 3.9.2

* Sat May 04 2013 Kalev Lember <kalevlember@gmail.com> - 1:3.9.1-1
- Update to 3.9.1

* Tue Apr 16 2013 Richard Hughes <rhughes@redhat.com> - 1:3.8.1-1
- Update to 3.8.1

* Wed Mar 27 2013 Kalev Lember <kalevlember@gmail.com> - 1:3.8.0-2
- Rebuilt for libwebkit2gtk soname bump

* Tue Mar 26 2013 Kalev Lember <kalevlember@gmail.com> - 1:3.8.0-1
- Update to 3.8.0

* Wed Mar 20 2013 Kalev Lember <kalevlember@gmail.com> - 1:3.7.92-1
- Update to 3.7.92

* Sat Mar 09 2013 Cosimo Cecchi <cosimoc@redhat.com> - 1:3.7.90-4
- Rebuilt for devhelp soname bump

* Fri Feb 22 2013 Kalev Lember <kalevlember@gmail.com> - 1:3.7.90-3
- Rebuilt for libwebkit2gtk soname bump

* Fri Feb 22 2013 Kalev Lember <kalevlember@gmail.com> - 1:3.7.90-2
- Rebuilt for libvala soname bump

* Tue Feb 19 2013 Richard Hughes <rhughes@redhat.com> - 1:3.7.90-1
- Update to 3.7.90

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 16 2013 Richard Hughes <hughsient@gmail.com> - 1:3.7.4-1
- Update to 3.7.4

* Wed Jan 09 2013 Richard Hughes <hughsient@gmail.com> - 1:3.7.3-1
- Update to 3.7.3

* Tue Nov 20 2012 Richard Hughes <hughsient@gmail.com> - 1:3.7.2-1
- Update to 3.7.2

* Tue Nov 13 2012 Kalev Lember <kalevlember@gmail.com> - 1:3.6.2-1
- Update to 3.6.2

* Mon Oct 22 2012 Kalev Lember <kalevlember@gmail.com> - 1:3.6.1-2
- Rebuilt for libgda 5.1

* Sat Oct 20 2012 Kalev Lember <kalevlember@gmail.com> - 1:3.6.1-1
- Update to 3.6.1

* Fri Sep 28 2012 Kalev Lember <kalevlember@gmail.com> - 1:3.6.0-2
- Rebuild with new libgdl once more, 3.6.0-1 used the old one

* Thu Sep 27 2012 Richard Hughes <hughsient@gmail.com> - 1:3.6.0-1
- Update to 3.6.0

* Wed Sep 26 2012 Kalev Lember <kalevlember@gmail.com> - 1:3.5.91-3
- Rebuilt for libgdl soname bump

* Thu Sep 20 2012 Cosimo Cecchi <cosimoc@redhat.com> - 1:3.5.91-2
- Rebuild for libglade soname bump

* Tue Sep 04 2012 Richard Hughes <hughsient@gmail.com> - 1:3.5.91-1
- Update to 3.5.91

* Tue Aug 07 2012 Richard Hughes <hughsient@gmail.com> - 1:3.5.5-1
- Update to 3.5.5

* Mon Jul 23 2012 Kalev Lember <kalevlember@gmail.com> - 1:3.5.4-3
- Rebuilt for libgdl 3.5.4 soname bump

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 17 2012 Richard Hughes <hughsient@gmail.com> - 1:3.5.4-1
- Update to 3.5.4

* Tue Jun 26 2012 Richard Hughes <hughsient@gmail.com> - 1:3.5.3-1
- Update to 3.5.3

* Sat May 05 2012 Kalev Lember <kalevlember@gmail.com> - 1:3.5.1-1
- Update to 3.5.1

* Sun Apr 29 2012 Kalev Lember <kalevlember@gmail.com> - 1:3.4.1-1
- Update to 3.4.1

* Sun Apr 22 2012 Kalev Lember <kalevlember@gmail.com> - 1:3.4.0-3
- Rebuilt with libgdl 3.4.1 (#815108)
- Added missing gdk-doc buildrequires

* Fri Apr 13 2012 Kalev Lember <kalevlember@gmail.com> - 1:3.4.0-2
- Update BuildRequires for glade3 -> glade rename

* Tue Mar 27 2012 Richard Hughes <hughsient@gmail.com> - 1:3.4.0-1
- Update to 3.4.0

* Wed Mar 21 2012 Kalev Lember <kalevlember@gmail.com> - 1:3.3.92-1
- Update to 3.3.92
- Spec file cleanup
- Install user manual in main anjuta package and obsolete anjuta-doc

* Sat Mar 17 2012 Kalev Lember <kalevlember@gmail.com> - 1:3.3.91-1
- Update to 3.3.91
- Re-enable vala support
- Remove perl Provides/Requires filtering

* Tue Jan 17 2012 Cosimo Cecchi <cosimoc@redhat.com> - 1:3.3.4-1
- Update to 3.3.4

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jan 10 2012 Cosimo Cecchi <cosimoc@redhat.com> - 1:3.3.3-2
- Disable vala support, until Anjuta supports Vala 0.15

* Thu Dec 29 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 1:3.3.3-1
- Update to 3.3.3
- http://ftp.acc.umu.se/pub/GNOME/sources/anjuta/3.3/anjuta-3.3.2.news
- http://ftp.acc.umu.se/pub/GNOME/sources/anjuta/3.3/anjuta-3.3.3.news

* Tue Nov 22 2011 Tomas Bzatek <tbzatek@redhat.com> - 1:3.3.1-1
- Update to 3.3.1

* Tue Sep 27 2011 Cosimo Cecchi <cosimoc@redhat.com> - 3.2.0-1
- Update to 3.2.0

* Mon Sep 19 2011 Cosimo Cecchi <cosimoc@redhat.com> - 3.1.92-1
- Update to 3.1.92

* Wed Sep 07 2011 Kalev Lember <kalevlember@gmail.com> - 3.1.91-1
- Update to 3.1.91

* Wed Aug 31 2011 Kalev Lember <kalevlember@gmail.com> - 3.1.90-1
- Update to 3.1.90

* Mon Jul 25 2011 Kalev Lember <kalevlember@gmail.com> - 3.1.4-1
- Update to 3.1.4

* Wed Jul 13 2011 Cosimo Cecchi <cosimoc@redhat.com> - 3.1.3-1
- Update to 3.1.3

* Wed Jul 13 2011 Kalev Lember <kalevlember@gmail.com> - 3.1.2-2
- Build with vala 0.13
- Avoid dependency on gtk-doc (#604338)

* Thu Jun 16 2011 Tomas Bzatek <tbzatek@redhat.com> - 3.1.2-1
- Update to 3.1.2

* Thu Apr 28 2011 Cosimo Cecchi <cosimoc@redhat.com> - 3.0.1.0-1
- Update to 3.0.1.0

* Tue Apr 12 2011 Cosimo Cecchi <cosimoc@redhat.com> - 3.0.0.0-2
- Don't require ctags

* Thu Apr 07 2011 Cosimo Cecchi <cosimoc@redhat.com> - 3.0.0.0-1
- Update to 3.0.0

* Fri Mar 04 2011 Rakesh Pandit <rakesh@fedoraproject.org> 2.91.90.0-2
- Added sqlite-devel as a require (hack)
  This seems to be an issue with libgda-sqlite (Needs a fix)

* Thu Feb 24 2011 Rakesh Pandit <rakesh@fedoraproject.org> 2.91.90.0-1
- Updated to 2.91.90.0
  New:
   - Signal dragging support for python
   - Glade usuability fixes
   - New inline search/replace from Eugenia (Women Outreach program)

  Bugs fixed:
   - 530060 Have a "replace all" option in search and replace
   - 553772 Unable to move or resize widget placed inside a layout widget
   - 568047 Glade plugin does not allow adding notebook containers with less
     than 3 tabs.
   - 631260 Composer window broken after defining ActionGroup
   - 633786 plugin.c:59: warning: implicit declaration of function
     'PyString_FromString' when compiling anjuta
   - 642647 Crash if anjuta is launched with a project that needs the glade
     plugin.
   - 642719 Prototype generator for C header files
   - 638787 wrong set on gtk_source_view_set_smart_home_end
   - 642763 Fix memory in message-view plugin
   - 516685 New artwork for splash screen
   - 549440 LIBADD is added at the wrong position in Makefile.am if it doesn't
     exist
   - 565358 documentation files appear in "other files" target
   - 566248 ianjuta_project_manager_get_elements returns weird data
   - 569992 support makefiles named GNUmakefile.am
   - 637981 Port Makefile backend to the new API
   - 640969 Allow importing projects with 3rd party project backends
   - 641181 error building out-of-tree plugins that only include
     libanjuta/libanjuta.h
   - 642640 NULL pointer dereference and memory leak in parameter.c
   - 642750 [PATCH] NULL pointer dereference in anjuta-tabber.c
   - 570912 Cannot remove module/package
   - 642723 Small in C header template

* Tue Feb 22 2011 Rakesh Pandit <rakesh@fedoraproject.org> 2.91.6.0-4
- Added missing files for glade plugin
- Updated summary

* Tue Feb 22 2011 Rakesh Pandit <rakesh@fedoraproject.org> 2.91.6.0-3
- Rebuild with new glade

* Tue Feb 22 2011 Rakesh Pandit <rakesh@fedoraproject.org> 2.91.6.0-2
- Updated description (Thanks Johannes Schmid <jhs AT jsschmid DOT de>)

* Mon Feb 21 2011 Rakesh Pandit <rakesh@fedoraproject.org> 2.91.6.0-1
 - Removed libxml and glade-plugin patch (included in this version)
 - New:
    * Support for dragging signals from glade into the code (C only)
    * Improvements in project-manager
    * More features in git-plugin
 - Bugs fixed:
    638506 Homepage: FAQ Mailinglist link is wrong
    639786 quick bookmark deletion
    640277 editor position history doesn’t work with shortcut
    618142 Anjuta Snippets Plug-in
    627131 Autocompletion duplicates characters
    639795 Editing variabile after inserting snippet bug
    638980 Crash when closing project
    608578 Anjuta is unable to import Gnumeric source tree
    611206 doesn’t recognize newer AC_INIT
    615990 path is missing when add a source to the target
    616041 Add Source -> Cannot add source files -> Core Dump
    618617 Project view doesn’t make sense
    638368 test-suite fails
    639342 Anjuta crash when loading libgee
    640348 minor mistake in UI string
    640726 anjuta stops updating session information
    581613 Unable to import a tarball into Anjuta 2.4.2
    639093 I can’t start a new project properly

* Fri Feb 11 2011 Matthias Clasen <mclasen@redhat.com> 2.91.5.0-4
- Rebuild against newer gtk

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.91.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb  2 2011 Matthias Clasen <mclasen@redhat.com> 2.91.5.0-2
- Rebuild against newer gtk

* Tue Jan 11 2011 Rakesh Pandit <rakesh@fedoraproject.org> 2.91.5.0-1
- Replaced vte-devel with vte3-devel as dep 
- Updated to 2.91.5.0
 * Updates:
  - Glade integration is working again and far more stable
  - Devhelp plugin is here gain
  - New class generation for Vala, Python and Javascript (Kenny)
  - New artwork (Samuel)
  - Comment/Uncomment feature for C/C++
  - Various improvements in vala support
 * Bugs (Gnome BZ) fixed:
  - 638228 language-support-vala: interrupt parsing if user switches to another file
  - 638252 language-support-vala: use the new markers to show error tooltips
  - 511000 Icons needed
  - 638532 crash in plugin list when pressing cursor-down
  - 637699 JavaScript wizard
  - 637774 Add Vala class wizard to class-gen
  - 638534 Criticals with local-only repositories
  - 616426 model wants symbols before db creation.
  - 625399 Attempt to make a query when database is not connected
  - 633018 crash in Anjuta IDE: I closed a project, wich...
  - 637695 allow comment/uncomment with gtksourceview editor
  - 638097 Remove deprecated gdk_spawn_command_line_on_screen gdk_spawn_on_screen
  - 638347 Incorrect makefile
  - 638830 Fortan typo?
  - 638878 $(BUILT_SOURCES): No such file or directory
  - 638034 Unable to create new project
  - 638524 Syntax error on valid configure.ac files
- Added libxml patch
- Added glade plugin patch
- Disabled stripping unneeded translation for time being
- Disabled /usr/lib64/libglade/2.0/libanjuta symlink

* Tue Dec 07 2010 Bastien Nocera <bnocera@redhat.com> 2.91.3.0-1
- Update to 2.91.3.0

* Fri Nov 26 2010 Johannes Schmid <jhs@jsschmid.de> - 1:2.32.1.0-1
- Version bump to 2.32.1.0

  * language-support-cpp-java: bgo#621916 - check for brace
  * libanjuta: bgo#633042 New: Sensitivity off 'ok' button on the project import dialog
  * language-support-cpp: Don't show duplicated results in autocompletion
  * build: bgo#633661 - vala support is automagic
  * language-support-cpp-java: bgo#633112 - Smart Brace Completion Quotation Mark Crash
  * python-support: Fix bgo#631223 autointention causes anjuta to hang

  * bgo#630460 PackageKit integration is not working on all distros
  * project-wizard: Update default ui file to use gtk+-2.16

* Thu Nov  4 2010 Michel Salim <salimma@fedoraproject.org> - 1:2.31.90.0-4
- Rebuild for vala-0.11.x

* Wed Sep 29 2010 jkeating - 1:2.31.90.0-3
- Rebuilt for gcc bug 634757

* Tue Sep 21 2010 Rakesh Pandit <rakesh@fedoraproject.org> - 1:2.31.90.0-2
- build against latest Vala

* Sun Aug 22 2010 Debarshi Ray <rishi@fedoraproject.org> - 1:2.31.90.0-1
- Version bump to 2.31.90.0.
  * Initial support for Python plugins.
  * Language support for Vala got a major update.
  * Python is now fully supported.
  * Snippets plugin from Google Summer of Code.
  * Increase launcher buffer size. (GNOME Bugzilla #624700)
  * Class generator plugin:
    + Add missing include. (GNOME Bugzilla #626265)
  * Language support (Vala) plugin:
    + Symbol completion does not work with 'this'. (GNOME Bugzilla #626306)
  * Project wizard plugin:
    + Add PyGTK project template. (GNOME Bugzilla #608304)
    + Remove cvsignore from templates. (GNOME Bugzilla #625434)
  * Symbol-db plugin:
    + Display names containing special characters correctly. (GNOME Bugzilla
      #616560)
    + Create temporary symbol database if project directory is read-only.
      (GNOME Bugzilla #622529)
  * http://download.gnome.org/sources/anjuta/2.31/anjuta-2.31.90.0.news
- configure fixes accepted by upstream.

* Sun Aug 22 2010 Debarshi Ray <rishi@fedoraproject.org> - 1:2.31.6.1-2
- Fixed configure to look for vala-0.10.pc and not vala-1.0.pc.
- Restored 'BuildRequires: graphviz-devel' as the class inheritence plugin
  was copied over from anjuta-extras.
- Added 'BuildRequires: sqlite-devel' for the symbol-db benchmarks.

* Fri Aug 06 2010 Debarshi Ray <rishi@fedoraproject.org> - 1:2.31.6.1-1
- Version bump to 2.31.6.1.
  * Debugger is now much more polished.
  * Debugger supports pretty printing now.
  * Drag and drop of multiple source files. (GNOME Bugzilla #620664)
  * Project wizard shows better package chooser.
  * Support for Vala.
  * Symbol-db is super fast now.
  * GNOME Goal: removed deprecated GTK+ symbols. (GNOME Bugzilla #572754)
  * Debug manager plugin:
    + Mouse cursor is a clock in debug mode. (GNOME Bugzilla #515395)
    + Do not create too many variable objects. (GNOME Bugzilla #516112)
    + Documentation for debug interfaces is incomplete. (GNOME Bugzilla
      #558954)
    + Locals column is now configurable. (GNOME Bugzilla #598187)
    + Allow saving the debugger stack trace. (GNOME Bugzilla #617323)
  * Document manager plugin:
    + Paths with symlinks do not get 'real' absolute paths. (GNOME Bugzilla
      #586428)
  * File wizard plugin:
    + Create the corresponding header for a C source file. (GNOME Bugzilla
      #616810)
  * GDB plugin:
    + New 'set next statement' command. (GNOME Bugzilla #494292)
  * Language support (C, C++, Java) plugin:
    + Race condition leading to crash while editing. (GNOME Bugzilla #618314)
    + Smart brace completion is no longer smart. (GNOME Bugzilla #618955)
  * Terminal plugin:
    + Do not become unresponsive when child execution fails. (GNOME Bugzilla
      #619253)
  * http://download.gnome.org/sources/anjuta/2.31/anjuta-2.31.6.1.news
  * http://download.gnome.org/sources/anjuta/2.31/anjuta-2.31.6.0.news
  * http://download.gnome.org/sources/anjuta/2.31/anjuta-2.31.5.0.news
  * http://download.gnome.org/sources/anjuta/2.31/anjuta-2.31.3.0.news
  * http://download.gnome.org/sources/anjuta/2.31/anjuta-2.31.2.0.news

* Wed Aug 04 2010 Debarshi Ray <rishi@fedoraproject.org> - 1:2.30.2.1-1
- Version bump to 2.30.2.1.
  * Document manager plugin:
    + Open .ui files. (GNOME Bugzilla #616739)
  * Language support (C, C++, Java) plugin:
    + Support more Vim modelines.
  * Language support (Javascript) plugin:
    + Do not abort when working on a project with Javascript files. (GNOME
      Project #617734)
  * Symbol-db plugin:
    + Wrong return type recognition. (GNOME Bugzilla #616780)
  * http://download.gnome.org/sources/anjuta/2.30/anjuta-2.30.2.1.news
  * http://download.gnome.org/sources/anjuta/2.30/anjuta-2.30.2.0.news

* Thu May 27 2010 Debarshi Ray <rishi@fedoraproject.org> - 1:2.30.1.0-1
- Version bump to 2.30.1.0.
  * Do not free the same string twice. (GNOME Bugzilla #615718)
  * Duplicated shortcut nodes. (GNOME Bugzilla #616740)
  * Document manager plugin:
    + Close documents by middle click. (GNOME Bugzilla #600083)
  * GTodo plugin:
    + Deselecting "Hide completed items" does not show completed items. (GNOME
      Bugzilla #614751)
  * Language support (C, C++, Java) plugin:
    + Javascript plugins use incorrect LDFLAGS and end up having versioned
      shared object files, links, etc.. (GNOME Bugzilla #615341)
    + Completion for . and -> does not work with prefixed &, %%, etc.. (GNOME
      Bugzilla #615596)
  * Project manager plugin:
    + Consider Vala files as sources. (GNOME Bugzilla #616503)
  * Symbol-db plugin:
    + Improved symbol icons for members. (GNOME Bugzilla #611834)
  * http://download.gnome.org/sources/anjuta/2.30/anjuta-2.30.1.0.news
- Updated the GConf scriptlet snippets according to Fedora packaging
  guidelines.

* Thu May 20 2010 Rakesh Pandit <rakesh@fedoraproject.org> - 1:2.30.0.0-4
- Bump (to fix a nuisance I created)

* Thu May 20 2010 Rakesh Pandit <rakesh@fedoraproject.org> - 1:2.30.0.0-3
- Bump to consume latest libgladeui-1.so.9

* Thu Apr 29 2010 Debarshi Ray <rishi@fedoraproject.org> - 1:2.30.0.0-2
- The Python templates in /usr/share/anjuta/project/python can not be
  byte-compiled. Try not to abort the build on byte-compilation errors.
- Updated the icon cache and scrollkeeper scriptlet snippets according to
  Fedora packaging guidelines.

* Thu Apr 29 2010 Debarshi Ray <rishi@fedoraproject.org> - 1:2.30.0.0-1
- Version bump to 2.30.0.0.
  * Completion for ., -> and :: in C/C++.
  * PackageKit integration.
  * Support for a simple 'Directory' project.
  * Support for Javascript.
  * Support for Vala symbols in the symbol-db.
  * Fixed shortcut grabbing. (GNOME Bugzilla #567689)
  * Loading file from command line should not put starter page in front of
    file. (GNOME Bugzilla #582726)
  * Send special keys to the terminal. (GNOME Bugzilla #559925)
  * Smaller icons in plugin list. (GNOME Bugzilla #550715)
  * Build (basic Autotools) plugin:
    + Underline warnings/errors using user-selected message colors. (GNOME
      Bugzilla #567029)
    + Missing call to fclose. (GNOME Bugzilla #599532)
    + Allow project path to contain space. (GNOME Bugzilla #604954)
    + Do not crash when trying to compile a file without an open project.
      (GNOME Bugzilla #612959)
  * Debug manager plugin:
    + Easier addition of watches. (GNOME Bugzilla #596009)
    + Single-step highlighting works only for the first opened project. (GNOME
      Bugzilla #605060)
  * File manager:
    + Saving a file duplicates its entry. (GNOME Bugzilla #605050)
  * GDB plugin:
    + Can not attach to a process to debug it. (GNOME Bugzilla #606069)
  * GtkSourceView editor plugin:
    + Parenthesis in strings confuse auto-indentation. (GNOME Bugzilla #586457)
    + Tooltip evaluation does not respect mouse position. (GNOME Bugzilla
      #601750)
  * Language support (C, C++, Java) plugin:
    + Do not auto-complete inside string or comment. (GNOME Bugzilla #566982)
    + Better expression parsing. (GNOME Bugzilla #608499)
  * Message view plugin:
    + Do not print garbage for messages in bold font. (GNOME Bugzilla #566194)
  * Project manager plugin:
    + Allow Python source to be added to a project. (GNOME Bugzilla #559876)
    + Fixed 'add project target'. (GNOME Bugzilla #565191)
    + Do not create random directories when importing. (GNOME Bugzilla #607415)
  * http://download.gnome.org/sources/anjuta/2.29/anjuta-2.29.92.0.news
  * http://download.gnome.org/sources/anjuta/2.29/anjuta-2.29.90.0.news
  * http://download.gnome.org/sources/anjuta/2.29/anjuta-2.29.6.0.news
  * http://download.gnome.org/sources/anjuta/2.29/anjuta-2.29.5.0.news
- Added 'BuildRequires: dbus-glib-devel vala-devel'.
- Dropped patch to fix build failures due to missing libxml cflags/libs.
  (GNOME Bugzilla #567029)
- Force verbose build output with '--disable-silent-rules'.

* Tue Feb 16 2010 Debarshi Ray <rishi@fedoraproject.org> - 1:2.28.2.0-1
- Version bump to 2.28.2.0.
  * Class generator plugin:
    + C++ keywords should not be translated. (GNOME Bugzilla #606801)
  * Git plugin:
    + Fixed failure while importing. (GNOME Bugzilla #601567)
  * Symbol-db plugin:
    + Editing some text while searching should not lead to an inconsistent
      state. (GNOME Bugzilla #566209)
  * http://download.gnome.org/sources/anjuta/2.28/anjuta-2.28.2.0.news

* Thu Nov 05 2009 Debarshi Ray <rishi@fedoraproject.org> - 1:2.28.1.0-2
- Bumped to consume new libgdl soname.

* Thu Oct 29 2009 Debarshi Ray <rishi@fedoraproject.org> - 1:2.28.1.0-1
- Version bump to 2.28.1.0.
  * Debug manager plugin:
    + Report error when location is < 0 for markers. (GNOME Bugzilla #593954)
  * File loader plugin:
    + Improved drag-and-drop behaviour. (GNOME Bugzilla #567363)
  * GtkSourceView editor plugin:
    + Improved drag-and-drop behaviour. (GNOME Bugzilla #355151)
  * Subversion plugin:
    + Removed duplicate IDs from the Glade file. (GNOME Bugzilla #596001)
  * Symbol-db plugin:
    + Fixed crash when loading a project. (GNOME Bugzilla #597113)
  * Terminal plugin:
    + Prevented it from crashing and freezing X. (GNOME Bugzilla #597318)
  * http://download.gnome.org/sources/anjuta/2.28/anjuta-2.28.1.0.news
- Added 'BuildRequires: GConf2-devel ORBit2-devel' and removed
  'BuildRequires: binutils-devel graphviz-devel libgnomeui-devel pcre-devel'.

* Sat Sep 12 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1:2.27.92.0-1
- Version bump to 2.27.92.0, rebuild for broken deps.
  * A better Git plugin and working C++ auto-completion.
  * http://download.gnome.org/sources/anjuta/2.27/anjuta-2.27.92.0.news
  * http://download.gnome.org/sources/anjuta/2.27/anjuta-2.27.91.0.news
  * http://download.gnome.org/sources/anjuta/2.27/anjuta-2.27.5.0.news
- Fixed build failures due to missing libxml cflags/libs. (GNOME
  Bugzilla #600407)

* Mon Aug 10 2009 Ville Skyttä <ville.skytta@iki.fi> - 1:2.27.3.0-3
- Use bzipped upstream tarball.

* Fri Jul 24 2009 Release Engineering <rel-eng@fedoraproject.org> - 1:2.27.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 14 2009 Debarshi Ray <rishi@fedoraproject.org> - 1:2.27.3.0-1
- Version bump to 2.27.3.0.
  * The Graphviz, profiler, Scintilla, ScratchBox and Valgrind plugins
    are now part of Anjuta Extras. They are no longer shipped with
    this package.
  * Improvements in auto-completion speed.
  * Improvements in Git and Subversion plugins.
  * Ported to GtkBuilder. (GNOME Bugzilla #530740)
  * Git plugin:
    + Commit dialog should have the "amend" option. (GNOME Bugzilla #580340)
  * GTodo plugin:
    + Use g_timeout_add_seconds to reduce wakeups. (GNOME Bugzilla #582710)
  * Language support (C, C++, Java) plugin:
    + Fixed crash when dismissing auto-completion popup and deleting some
      characters. (GNOME Bugzilla #582464)
  * Project wizard plugin:
    + Infer project name from project path. (GNOME Bugzilla #568779)
    + wxWidget projects should not depend on libglade and Gtk+. (GNOME
      Bugzilla #581074)
  * Scintilla editor plugin:
    + Fixed position of tooltips. (GNOME Bugzilla #577721)
  * Search plugin:
    + Point to correct line number. (GNOME Bugzilla #576959)
  * http://ftp.gnome.org/pub/GNOME/sources/anjuta/2.26/anjuta-2.27.3.0.news
  * http://ftp.gnome.org/pub/GNOME/sources/anjuta/2.26/anjuta-2.27.2.0.news
- Do not drop schemas translations from po files.
- Replaced 'BuildRequires: e2fsprogs-devel' with
  'BuildRequires: libuuid-devel'.
- Removed 'Requires: libglade2 >= 2.6.3-2'.

* Tue Jul 14 2009 Debarshi Ray <rishi@fedoraproject.org> - 1:2.26.2.2-3
- Added patch against class generator plugin to fix wrong copyright and
  license notices. (GNOME Bugzilla #575147)

* Tue Jul 14 2009 Debarshi Ray <rishi@fedoraproject.org> - 1:2.26.2.2-2
- Fixed the value of PACKAGE_DOC_DIR. (GNOME Bugzilla #588506)

* Tue Jul 14 2009 Debarshi Ray <rishi@fedoraproject.org> - 1:2.26.2.2-1
- Version bump to 2.26.2.2.
  * Git plugin:
    + Fixed a crash. (GNOME Bugzilla #584347)
  * Project manager plugin:
    + Fixed segmentation fault when adding a file to a project. (GNOME
      Bugzilla #579118)
    + Make gbf-am-parse work with subdirectory targets. (GNOME Bugzilla
      #580247)
  * Subversion plugin:
    + Do not show a commit number in the info pane if no files are given.
    + Do not crash if no paths are selected for committing.
  * Symbol-db plugin:
    + Fixed viewing of local symbols.
    + Plugged a memory leak that broke completion. (GNOME Bugzilla #585498)
  * Tools plugin:
    + Handle patch files with whitespaces in their names. (GNOME Bugzilla
      #580013)
  * http://ftp.gnome.org/pub/GNOME/sources/anjuta/2.26/anjuta-2.26.2.2.news
  * http://ftp.gnome.org/pub/GNOME/sources/anjuta/2.26/anjuta-2.26.2.1.news
  * http://ftp.gnome.org/pub/GNOME/sources/anjuta/2.26/anjuta-2.26.2.0.news
- Explicitly set docdir to /usr/share/doc/anjuta-2.26.2.2.

* Wed Apr 15 2009 Debarshi Ray <rishi@fedoraproject.org> - 1:2.26.1.0-1
- Version bump to 2.26.1.0.
  * New animation to identify running builds.
  * File manager plugin:
    + Show tooltips in the Files view only when full name does not fit. (GNOME
      Bugzilla #564002)
  * http://ftp.gnome.org/pub/GNOME/sources/anjuta/2.26/anjuta-2.26.1.0.news
  * http://ftp.gnome.org/pub/GNOME/sources/anjuta/2.26/anjuta-2.26.1.0.changes

* Mon Apr 13 2009 Debarshi Ray <rishi@fedoraproject.org> - 1:2.26.0.1-3
- Added 'Requires: ctags libgda-sqlite >= 3.99.7'. (Red Hat Bugzilla #494423)
- Removed 'Requires: libglade2-devel >= 2.6.3-2 libgnomeui-devel pkgconfig'
  from anjuta-devel.

* Sat Apr 11 2009 Debarshi Ray <rishi@fedoraproject.org> - 1:2.26.0.1-2
- Replaced 'Obsoletes: gnome-build <= 2.24.1-1' with
  'Obsoletes: gnome-build <= 2.24.1-1.fc10'. (Red Hat Bugzilla #485452).
- Explicitly passed '--enable-scrollkeeper' to configure.

* Tue Apr 07 2009 Debarshi Ray <rishi@fedoraproject.org> - 1:2.26.0.1-1
- Version bump to 2.26.0.1.
  * Get rid of libgnomecanvas. (GNOME Bugzilla #571740)
  * Huge improvements in the tooltip area.
  * Prevent hang when pressing backspace in the editor.
  * Git plugin:
    + Fixed crash.
  * GtkSourceView editor plugin:
    + Actually save modified files on exit. (GNOME Bugzilla #574376)
  * Language support (C, C++, Java) plugin:
    + Showing calltips should not hinder editing. (GNOME Bugzilla #574802)
  * Scintilla editor plugin:
    + Use line endings correctly. (GNOME Bugzilla #574607)
  * Search plugin:
    + Should point to correct line number. (GNOME Bugzilla #576959)
  * Translation updates: pt_BR, en_GB, da, fi, fr, gl, el, it, ca, pt, sv, es,
    tr, hu, vi, de, sl, ru, ja, mr, ar, th and pl.
  * http://ftp.gnome.org/pub/GNOME/sources/anjuta/2.26/anjuta-2.26.0.1.news
  * http://ftp.gnome.org/pub/GNOME/sources/anjuta/2.26/anjuta-2.26.0.1.changes
- configure fixes accepted by upstream.
- Stripped redundant translations from .mo files. (GNOME Bugzilla #474987)

* Tue Mar 10 2009 Debarshi Ray <rishi@fedoraproject.org> - 1:2.25.903.0-1
- Version bump to 2.25.903.0.
  * Fixed Glade and version control integration.
  * Updated documentation.
  * Automatically select program to run if the project has only one
    executable. (GNOME Bugzilla #564306)
  * Build (basic Autotools) plugin:
    + Save configuration options for build configuration. (GNOME Bugzilla
      #555895)
    + Fixed Valgrind violations. (GNOME Bugzilla #565170)
  * GtkSourceView editor plugin:
    + Make swapping of .h and .c work for C header files. (GNOME Bugzilla
      #556970)
    + Should not crash when closing unsaved file. (GNOME Bugzilla #559806)
    + Fixed crash when closing a read-only file that threw an exception while
      running a program in the debugger. (GNOME Bugzilla #564891)
  * Scintilla editor plugin:
    + Make auto-complete box vanish on backspace. (GNOME Bugzilla #567068)
  * Search plugin:
    + Repaired Find & Replace. (GNOME Bugzilla #571760)
    + Fixed crash when clicking on the results of 'Find in files ...'. (GNOME
      Bugzilla #572608)
  * Symbol-db plugin:
    + Fixed Valgrind violations. (GNOME Bugzilla #572637)
  * http://ftp.gnome.org/pub/GNOME/sources/anjuta/2.25/anjuta-2.25.903.0.news
  * http://ftp.gnome.org/pub/GNOME/sources/anjuta/2.25/anjuta-2.25.903.0.changes
- Fixed configure to correctly handle --enable-plugin-scintilla.
- Upstream no longer installs /usr/bin/benchmark.

* Sun Mar 08 2009 Rakesh Pandit <rakesh@fedoraproject.org> - 1:2.25.902-6
- Bumped to consume new WebKit soname.

* Fri Feb 27 2009 Debarshi Ray <rishi@fedoraproject.org> - 1:2.25.902-5
- Added 'Provides: perl(GBF::Make)'. Imported from gnome-build. (Red Hat
  Bugzilla #486530)

* Wed Feb 25 2009 Debarshi Ray <rishi@fedoraproject.org> - 1:2.25.902-4
- Removed 'BuildRequires: libgnomeprintui22-devel'.
- Enabled Glade3 plugin, and added 'Requires: glade3-libglade3ui >= 3.5.7' and
  'BuildRequires: glade3-libgladeui-devel >= 3.5.7'.
- Added 'BuildArch: noarch' to anjuta-doc for
  http://fedoraproject.org/wiki/Features/NoarchSubpackages
- Excluded /usr/bin/benchmark.

* Wed Feb 25 2009 Alex Lancaster <alexlan[AT]fedoraproject.org> - 1:2.25.902-3
- Added 'BuildRequires: libgnomeui-devel unique-devel'.

* Mon Feb 23 2009 Release Engineering <rel-eng@fedoraproject.org> - 1:2.25.902-2
- Autorebuild for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb 21 2009 Debarshi Ray <rishi@fedoraproject.org> - 1:2.25.902-1
- Version bump to 2.25.902.
  * Updated code completion, searching and project management.
  * Fixed crash on enabling or disabling a plugin. (GNOME Bugzilla #566785)
  * Fixed plugin description parser. (GNOME Bugzilla #571233)
  * Git plugin:
    + Initialize widgets before adding watches. (GNOME Bugzilla #570929)
  * GtkSourceView editor plugin:
    + Fixed multiple crashes. (GNOME Bugzilla #570492)
    + Fixed crash after clicking Edit/Preferences with an open file. (GNOME
      Bugzilla #571114)
  * Language support (C, C++, Java) plugin:
    + Code completion of symbols. (GNOME Bugzilla #566693)
    + Correctly tab indent function parameters automatically. (GNOME Bugzilla
      #567606)
    + Indent multi-line function declarations correctly. (GNOME Bugzilla
      #571215)
  * Project manager plugin:
    + Enable removal of project variables. (GNOME Bugzilla #556148)
  * Search plugin:
    + Trailing backslashes missing from the find pane. (GNOME Bugzilla #539580)
    + Fixed duplicate matches in search results. (GNOME Bugzilla #565015)
    + Handle find and replace in files containing multi-byte UTF-8 sequences.
      (GNOME Bugzilla #566531)
  * Symbol-db plugin:
    + Display tooltip with prototype when calling a function in the same
      project. (GNOME Bugzilla #566987).
    + Scan user-added packages. (GNOME Bugzilla #570877)
  * Terminal plugin:
    + Fixed multiple crashes. (GNOME Bugzilla #570492)
  * Tools plugin:
    + Fixed crash due to a double free. (GNOME Bugzilla #571143)
  * http://ftp.gnome.org/pub/GNOME/sources/anjuta/2.25/anjuta-2.25.902.news
  * http://ftp.gnome.org/pub/GNOME/sources/anjuta/2.25/anjuta-2.25.902.changes
- Removed unwanted Perl Provides and Requires. Imported from gnome-build.

* Thu Feb 12 2009 Rakesh Pandit <rakesh@fedoraproject.org> - 1:2.25.901-2
- Added 'BuildRequires: perl(Locale::gettext)'.

* Thu Feb 12 2009 Rakesh Pandit <rakesh@fedoraproject.org> - 1:2.25.901-1
- Version bump to 2.25.901.
  * Absorbed gnome-build code. Added 'Obsoletes: gnome-build <= 2.24.1-1'.
  * New starter plugin for fast access to common actions.
  * Improved searching and HIG fixes.
  * Scintilla updated to 1.77.
  * Ported to GLib VFS. (GNOME Bugzilla #511589)
  * Get rid of libgnome(ui) partially. (GNOME Bugzilla #513156)
  * GNOME Goal: removed deprecated GLib symbols. (GNOME Bugzilla #560857)
  * Added Scratchbox2 support. (GNOME Bugzilla #565320)
  * Improved auto-completion and symbol-db.
  * Improved file status display.
  * Ported to GtkPrint. (GNOME Bugzilla #564659)
  * Fixed crash when replacing all in open buffers. (GNOME Bugzilla #570223)
  * Build (basic Autotools) plugin:
    + Build does not start with unsaved files. (GNOME Bugzilla #567206)
  * File loader plugin:
    + Support opening PHP, Ruby, etc. scripts. (GNOME Bugzilla #309664)
  * File manager plugin:
    + Added option to hide unversioned files. (GNOME Bugzilla #570136)
    + Detect modified files. (GNOME Bugzilla #570264)
  * File wizard plugin:
    + Support creation of corresponding header file. (GNOME Bugzilla #562754)
  * GDB plugin:
    + Support remote debugging using GDBServer. (GNOME Bugzilla #503764)
  * Glade plugin:
    + Google Summer of Code 2008: merged integration work. (GNOME Bugzilla
      #542412)
  * GtkSourceView editor plugin:
    + Added go to matching brace, and start/end of block commands. (GNOME
      Bugzilla #563499)
    + Go to tag definition should support symbols ending in a digit. (GNOME
      Bugzilla #567049)
    + Autocomplete box should vanish on backspace. (GNOME Bugzilla #567068)
  * Project wizard plugin:
    + Expand tilde to $HOME. (GNOME Bugzilla #562623)
    + Autogenerated Gtk/GNOME program should exit. (GNOME Bugzilla #564308)
  * Scintilla editor plugin:
    + Spurious reload messages. (GNOME Bugzilla #491491)
  * Subversion plugin:
    + Differentiate between versioned and non-versioned files. (GNOME Bugzilla
      #561370)
    + Added revert command. (GNOME Bugzilla #564988)
    + Diffs should be done from the project root directory. (GNOME Bugzilla
      #566924)
  * Symbol-db plugin:
    + This is now the default. The old CTags and symbol-browser plugins have
      been removed.
    + Go to declaration/definition should support macros. (GNOME Bugzilla
      #566691)
    + Do not hang if project is closed while scanning symbols. (GNOME Bugzilla
      #567067)
    + Allow jumping to declarations in external package header. (GNOME Bugzilla
      #567361)
    + Go to tag definition should support an enum, a global variable, a struct
      or a typedef. (GNOME Bugzilla #567058)
    + Go to declaration/implementation should prefer the current file. (GNOME
      Bugzilla #568028)
    + Scan system packages. (GNOME Bugzilla #568119)
    + Do not freeze when moving around large portions of code. (GNOME Bugzilla
      #568493)
  * Translation updates: es, fr, sv, fi, he, ru, pt_BR and pl.
  * http://ftp.gnome.org/pub/GNOME/sources/anjuta/2.25/anjuta-2.25.901.news
  * http://ftp.gnome.org/pub/GNOME/sources/anjuta/2.25/anjuta-2.25.90.news
  * http://ftp.gnome.org/pub/GNOME/sources/anjuta/2.25/anjuta-2.25.5.news
  * http://ftp.gnome.org/pub/GNOME/sources/anjuta/2.25/anjuta-2.25.901.changes
  * http://ftp.gnome.org/pub/GNOME/sources/anjuta/2.25/anjuta-2.25.90.changes
  * http://ftp.gnome.org/pub/GNOME/sources/anjuta/2.25/anjuta-2.25.5.changes
- Patch against Devhelp plugin is now upstream.
- Disabled Glade3 plugin because glade3-3.5.7 is not yet available.

* Sun Jan 04 2009 Debarshi Ray <rishi@fedoraproject.org> - 1:2.24.2-1
- Version bump to 2.24.2. (Red Hat Bugzilla #478684)
  * Debug manager plugin:
    + Missing debugger menu. (GNOME Bugzilla #559800)
  * Translation updates: pt_BR and si.
  * http://ftp.gnome.org/pub/GNOME/sources/anjuta/2.24/anjuta-2.24.2.news
  * http://ftp.gnome.org/pub/GNOME/sources/anjuta/2.24/anjuta-2.24.2.changes

* Sat Jan 03 2009 Debarshi Ray <rishi@fedoraproject.org> - 1:2.24.1-3
- Added patch against the Devhelp plugin from GNOME to make it work with the
  new WebKit-based Devhelp >= 0.22. (GNOME Bugzilla #560311, and Red Hat
  Bugzilla #478578)

* Sun Nov 09 2008 Debarshi Ray <rishi@fedoraproject.org> - 1:2.24.1-2
- Added 'Requires: libglade2 >= 2.6.3-2' and a symlink to libanjuta.so.0 for
  some plugins to work. (Red Hat Bugzilla #467894)

* Tue Oct 28 2008 Debarshi Ray <rishi@fedoraproject.org> - 1:2.24.1-1
- Version bump to 2.24.1.
  * Build (basic Autotools) plugin:
    + Could not find the .glade file while executing a binary. (GNOME Bugzilla
      #554337)
  * Document manager plugin:
    + Do not disable save when closing file tabs. (GNOME Bugzilla #556053)
  * Translation updates: ar, de, ru, bg, fi, pl, he and da.
  * http://ftp.gnome.org/pub/GNOME/sources/anjuta/2.24/anjuta-2.24.1.news
  * http://ftp.gnome.org/pub/GNOME/sources/anjuta/2.5/anjuta-2.5.90.news
  * http://ftp.gnome.org/pub/GNOME/sources/anjuta/2.24/anjuta-2.24.1.changes
  * http://ftp.gnome.org/pub/GNOME/sources/anjuta/2.24/anjuta-2.24.0.1.changes
  * http://ftp.gnome.org/pub/GNOME/sources/anjuta/2.5/anjuta-2.5.90.changes
- Makefile problems fixed by upstream.
- Added 'Requires: git' and 'BuildRequires: e2fsprogs-devel intltool'.
- libanjuta-egg.so has been dropped.

* Sat Sep 20 2008 Debarshi Ray <rishi@fedoraproject.org> - 1:2.4.2-1
- Version bump to 2.4.2.
  * http://ftp.gnome.org/pub/GNOME/sources/anjuta/2.4/anjuta-2.4.2.news
  * http://ftp.gnome.org/pub/GNOME/sources/anjuta/2.4/anjuta-2.4.2.changes
- Enabled Valgrind plugin and added 'BuildRequires: binutils-devel'.

* Sat May 24 2008 Debarshi Ray <rishi@fedoraproject.org> - 1:2.4.1-1
- Version bump to 2.4.1. (Red Hat Bugzilla #446242)
  * http://ftp.gnome.org/pub/GNOME/sources/anjuta/2.4/anjuta-2.4.1.news
  * http://ftp.gnome.org/pub/GNOME/sources/anjuta/2.3/anjuta-2.3.5.news
  * http://ftp.gnome.org/pub/GNOME/sources/anjuta/2.3/anjuta-2.3.4.news
  * http://ftp.gnome.org/pub/GNOME/sources/anjuta/2.3/anjuta-2.3.3.news
  * http://ftp.gnome.org/pub/GNOME/sources/anjuta/2.3/anjuta-2.3.2.news
  * http://ftp.gnome.org/pub/GNOME/sources/anjuta/2.3/anjuta-2.3.1.news
  * http://ftp.gnome.org/pub/GNOME/sources/anjuta/2.4/anjuta-2.4.1.changes
  * http://ftp.gnome.org/pub/GNOME/sources/anjuta/2.3/anjuta-2.3.5.changes
  * http://ftp.gnome.org/pub/GNOME/sources/anjuta/2.3/anjuta-2.3.4.changes
  * http://ftp.gnome.org/pub/GNOME/sources/anjuta/2.3/anjuta-2.3.3.changes
  * http://ftp.gnome.org/pub/GNOME/sources/anjuta/2.3/anjuta-2.3.2.changes
  * http://ftp.gnome.org/pub/GNOME/sources/anjuta/2.3/anjuta-2.3.1.changes
- Spurious file modification messages from Scintilla fixed by upstream. (Red
  Hat Bugzilla #447090)

* Tue May 13 2008 Debarshi Ray <rishi@fedoraproject.org> - 1:2.2.3-8
- Added missing header to fix build failure on ia64. (Red Hat Bugzilla #446020)

* Fri Apr 11 2008 Debarshi Ray <rishi@fedoraproject.org> - 1:2.2.3-7
- Restored empty files. (Red Hat Bugzilla #440087)

* Sun Apr 06 2008 Debarshi Ray <rishi@fedoraproject.org> - 1:2.2.3-6
- Added 'Requires: autogen'. (Red Hat Bugzilla #441036)

* Thu Mar 27 2008 Debarshi Ray <rishi@fedoraproject.org> - 1:2.2.3-5
- Fixed Source0 URL according to Fedora packaging guidelines.
- Removed 'BuildRequires: chrpath' and use better ways of removing rpaths.
- Added Scintilla documentation to anjuta-devel.

* Fri Feb 29 2008 Debarshi Ray <rishi@fedoraproject.org> - 1:2.2.3-4
- Restored 'BuildRequires: chrpath' for removing rpaths.
- Added 'Requires: gtk-doc' for anjuta-devel.

* Fri Feb 29 2008 Debarshi Ray <rishi@fedoraproject.org> - 1:2.2.3-3
- Fixed create_global_tags.sh.in. (Red Hat Bugzilla #228351)
- Enabled Devhelp plugin on Fedora 7.
- Removed 'BuildRequires: chrpath' and use better ways of removing rpaths.
- Removed 'ExcludeArch: ppc64'.
- Fixed post scriplet for the doc subpackage.

* Mon Feb 18 2008 Debarshi Ray <rishi@fedoraproject.org> - 1:2.2.3-2
- Added 'BuildRequires: libgnomeui-devel' to prevent failure on Fedora 7.
- Disabled Devhelp plugin to prevent failure on Fedora 7.

* Sun Jan 27 2008 Debarshi Ray <rishi@fedoraproject.org> - 1:2.2.3-1
- Initial build. Imported SPEC from Rawhide and renamed as anjuta-doc from
  anjuta-docs according to Fedora naming guidelines.
  * http://ftp.gnome.org/pub/GNOME/sources/anjuta/2.2/anjuta-2.2.3.news
  * http://ftp.gnome.org/pub/GNOME/sources/anjuta/2.2/anjuta-2.2.3.changes
