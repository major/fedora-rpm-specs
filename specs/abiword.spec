%define bigversion 3.0
%define docsversion 3.0.1

Name: abiword
Version: 3.0.5
Release: 18%{?dist}
Epoch: 1
Summary: Word processing program
License: GPL-2.0-or-later
URL: http://www.abisource.com/

Source0: http://abisource.com/downloads/abiword/%{version}/source/abiword-%{version}.tar.gz
Source1: http://abisource.com/downloads/abiword/%{version}/source/abiword-docs-%{docsversion}.tar.gz
Source11: abiword.mime
Source12: abiword.keys
Source13: abiword.xml

ExcludeArch:    %{ix86}

Patch0: abiword-2.6.0-windowshelppaths.patch
Patch1: abiword-2.8.3-desktop.patch
Patch2: abiword-2.6.0-boolean.patch
Patch3: abiword-3.0.0-librevenge.patch
Patch4: abiword-3.0.2-explicit-python.patch
Patch5: abiword-3.0.4-pygobject.patch
Patch6: xml-inc.patch

BuildRequires: aiksaurus-devel
BuildRequires: aiksaurus-gtk-devel
BuildRequires: asio-devel
# Needed while explicit-python.patch touches gi-overrides/Makefile.am
BuildRequires: automake
BuildRequires: bison
BuildRequires: boost-devel
BuildRequires: bzip2-devel
BuildRequires: cairo-devel
BuildRequires: dbus-glib-devel
BuildRequires: desktop-file-utils
BuildRequires: enchant-devel
BuildRequires: flex
BuildRequires: fribidi-devel
BuildRequires: gcc-c++
BuildRequires: gobject-introspection-devel
BuildRequires: goffice-devel
BuildRequires: gtk3-devel
# Probably because it's gtk2 based
#BuildRequires: gtkmathview-devel
BuildRequires: libgcrypt-devel
BuildRequires: libgsf-devel
BuildRequires: libpng-devel
BuildRequires: librevenge-devel
BuildRequires: librsvg2-devel
BuildRequires: libsoup-devel
BuildRequires: libwmf-devel
BuildRequires: libwpd-devel
BuildRequires: libwpg-devel
BuildRequires: libxslt-devel
BuildRequires: link-grammar-devel
BuildRequires: loudmouth-devel
BuildRequires: ots-devel
BuildRequires: pkgconf-pkg-config
BuildRequires: pkgconfig(libwps-0.4)
BuildRequires: poppler-devel
BuildRequires: popt-devel
BuildRequires: python3-gobject
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: readline-devel
BuildRequires: t1lib-devel
BuildRequires: telepathy-glib-devel
BuildRequires: wv-devel
BuildRequires: zlib-devel
BuildRequires: make
BuildRequires: libappstream-glib

Requires: libabiword = %{epoch}:%{version}-%{release}
Requires: python3-gobject-base

%description
AbiWord is a cross-platform Open Source word processor. It is full-featured,
while still remaining lean.


%package -n libabiword
Summary: Library for developing applications based on AbiWord's core

%description -n libabiword
Library for developing applications based on AbiWord's core.


%package -n libabiword-devel
Summary: Files for developing with libabiword
Requires: libabiword = %{epoch}:%{version}-%{release}

%description -n libabiword-devel
Includes and definitions for developing with libabiword.


%package -n python3-abiword
%{?python_provide:%python_provide python3-abiword}
Summary: Python bindings for developing with libabiword
Requires: libabiword = %{epoch}:%{version}-%{release}

%description -n python3-abiword
Python bindings for developing with libabiword


%prep
# setup abiword
%setup -q -a 1

# patch abiword
%patch -P 1 -p1 -b .desktop
%patch -P 2 -p1 -b .boolean
%patch -P 3 -p0 -b .librevenge
%patch -P 4 -p1 -b .explicit_python
%patch -P 5 -p1 -b .pygo
%patch -P 6 -p0 -b .xml

# setup abiword documentation
pushd abiword-docs-%{docsversion}
%patch -P 0 -p1 -b .windowshelppaths
# some of the help dirs have bad perms (#109261)
find . -type d -exec chmod -c o+rx {} \;
popd

%build
# Needed while explicit-python.patch touches gi-overrides/Makefile.am
aclocal
automake

export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS -DASIO_ENABLE_BOOST"
%configure \
  --enable-plugins --enable-clipart --enable-templates --enable-introspection \
  --with-gir-dir=%{_datadir}/gir-1.0 --with-typelib-dir=%{_libdir}/girepository-1.0
%{make_build} V=1

# build the documentation
pushd abiword-docs-%{docsversion}
ABI_DOC_PROG=$(pwd)/../%{name}-%{version}/src/abiword ./make-html.sh
popd

%install
%{make_install} overridesdir=%{python3_sitelib}/gi/overrides

# install the documentation
pushd abiword-docs-%{docsversion}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}-%{bigversion}/AbiWord/help
cp -rp help/* $RPM_BUILD_ROOT/%{_datadir}/%{name}-%{bigversion}/AbiWord/help/
popd

install -p -m 0644 -D %{SOURCE11} $RPM_BUILD_ROOT%{_datadir}/mime-info/abiword.mime
install -p -m 0644 -D %{SOURCE12} $RPM_BUILD_ROOT%{_datadir}/mime-info/abiword.keys
install -p -m 0644 -D %{SOURCE13} $RPM_BUILD_ROOT%{_datadir}/mime/packages/abiword.xml

# Remove libtool archives and static libs
find %{buildroot} -name '*.la' -delete
find %{buildroot} -name '*.a' -delete

mv %{buildroot}%{_datadir}/applications/abiword.desktop %{buildroot}%{_datadir}/applications/com.abisource.AbiWord.desktop

mkdir -p %{buildroot}%{_metainfodir}/
mv %{buildroot}%{_datadir}/appdata/abiword.appdata.xml %{buildroot}%{_metainfodir}/
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/abiword.appdata.xml

%ldconfig_scriptlets -n libabiword

%files
%{_bindir}/abiword
%{_metainfodir}/abiword.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/mime-info/abiword.mime
%{_datadir}/mime-info/abiword.keys
%{_datadir}/mime/packages/abiword.xml
%{_datadir}/icons/hicolor/*/apps/abiword.png
%{_datadir}/icons/hicolor/scalable/apps/abiword.svg
# Abiword help
%{_datadir}/%{name}-%{bigversion}/AbiWord
%{_mandir}/man1/abiword.1*

%files -n libabiword
%license COPYING COPYRIGHT.TXT
%{_libdir}/libabiword-%{bigversion}.so
%{_libdir}/libAiksaurusGtk3*
%{_libdir}/%{name}-%{bigversion}
%{_libdir}/girepository-1.0/Abi-3.0.typelib
%{_datadir}/%{name}-%{bigversion}
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.AbiCollab.service
%{_datadir}/telepathy/clients/AbiCollab.client
# Abiword help - included in GUI app
%exclude %{_datadir}/%{name}-%{bigversion}/AbiWord

%files -n libabiword-devel
%{_includedir}/%{name}-%{bigversion}
%{_libdir}/pkgconfig/%{name}-%{bigversion}.pc
%{_datadir}/gir-1.0/Abi-3.0.gir

%files -n python3-abiword
%pycached %{python3_sitelib}/gi/overrides/Abi.py

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Oct 22 2024 Gwyn Ciesla <gwync@protonmail.com> - 1:3.0.5-17
- Fix desktop filename

* Tue Sep 24 2024 Gwyn Ciesla <gwync@protonmail.com> - 1:3.0.5-16
- Fix metainfo

* Sun Sep 08 2024 Alexander Ploumistos <alexpl@fedoraproject.org> - 1:3.0.5-15
- Rebuilt for goffice-0.10.57

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 1:3.0.5-13
- Rebuilt for Python 3.13

* Wed Jan 31 2024 Gwyn Ciesla <gwync@protonmail.com> - 1:3.0.5-12
- Add missing include

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Nov 04 2023 Gwyn Ciesla <gwync@protonmail.com> 1:3.0.5-9
- Drop i386 on f40+

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 1:3.0.5-7
- Rebuilt for Python 3.12

* Wed Mar 08 2023 Gwyn Ciesla <gwync@protonmail.com> - 1:3.0.5-6
- migrated to SPDX license

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1:3.0.5-3
- Rebuilt for Python 3.11

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Oct 23 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 1:3.0.5-1
- Update to 3.0.5

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1:3.0.4-10
- Rebuilt for Python 3.10

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.4-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Jeff Law <law@redhat.com> - 1:3.0.4-7
- Force C++14 as the code is not ready for C++17

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1:3.0.4-5
- Rebuilt for Python 3.9

* Sun Feb  2 2020 Peter Robinson <pbrobinson@fedoraproject.org> 1:3.0.4-4
- More packaging cleanups and fixes

* Wed Jan 29 2020 Peter Robinson <pbrobinson@fedoraproject.org> 1:3.0.4-3
- Packaging cleanups and fixes

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 29 2019 Peter Robinson <pbrobinson@fedoraproject.org> 1:3.0.4-1
- Update to 3.0.4
- Move to python3 gobject introspection bindings
- Disable gtkmathview plugins until requires issue is fixed

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:3.0.2-20
- Rebuild for readline 8.0

* Fri Feb 01 2019 Caolán McNamara <caolanm@redhat.com> - 1:3.0.2-19
- Rebuilt for fixed libwmf soname

* Fri Feb 01 2019 Björn Esser <besser82@fedoraproject.org> - 1:3.0.2-18
- Add patch to explicitly use python2 (#1671692)

* Fri Feb 01 2019 Björn Esser <besser82@fedoraproject.org> - 1:3.0.2-17
- Rebuilt for libwmf soname bump

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 17 2018 Miro Hrončok <mhroncok@redhat.com> - 1:3.0.2-15
- Update Python macros to new packaging standards
  (See https://fedoraproject.org/wiki/Changes/Move_usr_bin_python_into_separate_package)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 28 2018 Caolán McNamara <caolanm@redhat.com> - 1:3.0.2-13
- rebuild for fribidi

* Wed Feb 07 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1:3.0.2-12
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:3.0.2-10
- Remove obsolete scriptlets

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1:3.0.2-9
- Python 2 binary package renamed to python2-abiword
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 1:3.0.2-4
- Rebuild for readline 7.x

* Wed Dec  7 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1:3.0.2-3
- Fix the black drawing regression with Gtk3.22

* Tue Nov 29 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1:3.0.2-2
- Run ldconfig for libabiword

* Tue Nov 29 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1:3.0.2-1
- Update to 3.0.2 stable

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.0.1-12
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun Apr 10 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1:3.0.1-11
- fix parallel build (thanks yselkowi) rhbz 1214395

* Sun Apr 10 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1:3.0.1-10
- Add patches to fix building with newer gnutls and gcc6
- Add patch to fix Wordperfect support

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1:3.0.1-7
- rebuild for Boost 1.58

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 David Tardon <dtardon@redhat.com> - 1:3.0.1-5
- really enable WordPerfect import
- enable MS Works import

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1:3.0.1-4
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 1:3.0.1-3
- Add an AppData file for the software center

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 1:3.0.1-2
- Rebuild for boost 1.57.0

* Wed Dec 24 2014 Peter Robinson <pbrobinson@fedoraproject.org> 1:3.0.1-1
- Update to 3.0.1 stable

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 1:3.0.0-13
- Rebuilt for gobject-introspection 1.41.4

* Tue Jul 08 2014 Rex Dieter <rdieter@fedoraproject.org> 1:3.0.0-12
- update scriptlets (mimeinfo mostly)

* Mon Jun 30 2014 Jon Ciesla <limburgher@gmail.com> - 1:3.0.0-11
- Corrected and second patches from Linas Vepstas.

* Tue Jun 24 2014 Jon Ciesla <limburgher@gmail.com> - 1:3.0.0-10
- Rebuild for new link-grammar, with patch for API change.
- Add librevenge BuildRequires, modified patch for current librevenge header placement.

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 David Tardon <dtardon@redhat.com> - 1:3.0.0-8
- switch to librevenge-based import libs

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 1:3.0.0-7
- Rebuild for boost 1.55.0

* Tue Apr 22 2014 Tomáš Mráz <tmraz@redhat.com> - 1:3.0.0-6
- Rebuild for new libgcrypt

* Sat Feb 22 2014 Peter Robinson <pbrobinson@fedoraproject.org> 1:3.0.0-5
- Add patch to fix redraw issues of ruler

* Mon Nov  4 2013 Peter Robinson <pbrobinson@fedoraproject.org> 1:3.0.0-4
- Add patch to fix libabiword_init annotation

* Fri Oct 25 2013 Peter Robinson <pbrobinson@fedoraproject.org> 1:3.0.0-3
- Update icon cache on install/update/erase

* Wed Oct 16 2013 Peter Robinson <pbrobinson@fedoraproject.org> 1:3.0.0-2
- Enable gobject-introspection and python bindings

* Mon Oct 14 2013 Peter Robinson <pbrobinson@fedoraproject.org> 1:3.0.0-1
- Update to 3.0.0 stable
