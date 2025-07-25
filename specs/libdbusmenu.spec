# Todo: build docs
# BuildRequires:  gtk-doc >= 1.14
# configure --enable-gtk-doc --enable-gtk-doc-html --enable-gtk-doc-pdf

%global ubuntu_release 16.04

# Set to 1 to run testsuite
%global with_tests 0

# No gtk2 in RHEL 10
%if 0%{?rhel} > 9
%bcond_with    gtk2
%else
%bcond_without gtk2
%endif

Name:       libdbusmenu
Version:    %{ubuntu_release}.0
Release:    30%{?dist}
Summary:    Library for passing menus over DBus

# All files installed in final rpms use C sources with dual licensing headers.
# Tests compiled in the build process are licensed GPLv3

License:    (LGPL-3.0-only OR LGPL-2.1-only) AND GPL-3.0-only
URL:        https://launchpad.net/libdbusmenu
Source0:    https://launchpad.net/libdbusmenu/%{ubuntu_release}/%{version}/+download/%{name}-%{version}.tar.gz

# patch to remove -Werror flag - fixes build despite usage of deprecated things
Patch0:     00-no-werror.patch

BuildRequires: make
BuildRequires:  atk-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext
BuildRequires:  glibc-devel
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  libxslt
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(gio-2.0) >= 2.35.4
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.24
BuildRequires:  pkgconfig(glib-2.0) >= 2.35.4
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 0.10
%if %{with gtk2}
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.16
%endif
BuildRequires:  pkgconfig(gtk+-3.0) >= 2.91
BuildRequires:  pkgconfig(json-glib-1.0) >= 0.13.4
BuildRequires:  pkgconfig(x11) >= 1.3
BuildRequires:  vala

# pkgconfig file is checked for valgrind, but is actually only used for tests
# https://bugzilla.redhat.com/show_bug.cgi?id=1262274
# BuildRequires:  pkgconfig(valgrind)
%if 0%{?with_tests}
BuildRequires:  dbus-test-runner
BuildRequires:  python2
BuildRequires:  valgrind
%endif

%description
This is a small library designed to make sharing and displaying of menu
structures over DBus simple and easy to use. It works for both QT and GTK+ and
makes building menus simple.

%package devel
Summary:    %{summary} - Development files
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%if %{with gtk2}
%package gtk2
Summary:    %{summary} - GTK+2 version
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description gtk2
Shared libraries for the %{name}-gtk2 library.
%endif

%package gtk3
Summary:    %{summary} - GTK+3 version
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description gtk3
Shared libraries for the %{name}-gtk3 library.

%if %{with gtk2}
%package gtk2-devel
Summary:    Development files for %{name}-gtk2
Requires:   %{name}-gtk2%{?_isa} = %{version}-%{release}
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   gtk2-devel

%description gtk2-devel
The %{name}-gtk2-devel package contains libraries and header files for
developing applications that use %{name}-gtk2.
%endif

%package gtk3-devel
Summary:    Development files for %{name}-gtk3
Requires:   %{name}-gtk3%{?_isa} = %{version}-%{release}
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   gtk3-devel

%description gtk3-devel
The %{name}-gtk3-devel package contains libraries and header files for
developing applications that use %{name}-gtk3.

%package jsonloader
Summary:    Test lib development files
Requires:   %{name}-devel%{?_isa} = %{version}-%{release}
Requires:   libdbusmenu = %{version}-%{release}

%description jsonloader
Test library for %{name}.

%package jsonloader-devel
Summary:    Test lib development files for %{name}
Requires:   %{name}-jsonloader%{?_isa} = %{version}-%{release}
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description jsonloader-devel
The %{name}-jsonloader-devel package contains libraries and header files for
developing applications that use %{name}-jsonloader.

%package    doc
Summary:    Document files for %{name}
BuildArch:  noarch

%description doc
The %{name}-doc package contains documents for developing applications that
use %{name}.

%package    tools
Summary:    Development tools for the dbusmenu libraries
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description tools
The %{name}-tools package contains helper tools for developing applications
that use %{name}.


%prep
%setup -q -n %{name}-%{version} -c

export ACLOCAL_PATH=/usr/share/gettext/m4/
pushd %{name}-%{version}
%patch 0 -p1
autoreconf -fiv
popd

cp -a %{name}-%{version}/{README,COPYING,COPYING.2.1,COPYING-GPL3,AUTHORS,ChangeLog} .
cp -a %{name}-%{version} %{name}-gtk3-%{version}


%build
build(){
%configure --disable-static --disable-dumper --enable-introspection $*
%make_build
}

pushd %{name}-gtk3-%{version}
sed -i -e 's@^#!.*python$@#!/usr/bin/python2@' tools/dbusmenu-bench
build --with-gtk=3
popd

%if %{with gtk2}
pushd %{name}-%{version}
sed -i -e 's@^#!.*python$@#!/usr/bin/python2@' tools/dbusmenu-bench
build --with-gtk=2
popd
%endif


%install
pushd %{name}-gtk3-%{version}
%make_install
find %{buildroot} -name '*.la' -delete
popd

%if %{with gtk2}
pushd %{name}-%{version}
%make_install
find %{buildroot} -name '*.la' -delete
popd
%endif

# Let rpmbuild pick the documents in the files section
rm -fr %{buildroot}%{_docdir}/%{name}

# Remove benchmarking tool written in python2
rm %{buildroot}/%{_libexecdir}/dbusmenu-bench


%if 0%{?with_tests}
%check
for variant in %{name}-gtk3-%{version} %{name}-%{version}; do
    pushd $variant
        make check V=1
    popd
done
%endif

%ldconfig_scriptlets
%if %{with gtk2}
%ldconfig_scriptlets gtk2
%endif
%ldconfig_scriptlets gtk3
%ldconfig_scriptlets jsonloader

%files
%license COPYING COPYING.2.1 COPYING-GPL3
%doc README AUTHORS ChangeLog
%{_libdir}/libdbusmenu-glib.so.*
%{_libdir}/girepository-1.0/Dbusmenu-0.4.typelib

%files devel
%doc %{name}-%{version}/tests/glib-server-nomenu.c
%dir %{_includedir}/libdbusmenu-glib-0.4/
%dir %{_includedir}/libdbusmenu-glib-0.4/libdbusmenu-glib/
%{_includedir}/libdbusmenu-glib-0.4/libdbusmenu-glib/*.h
%{_libdir}/libdbusmenu-glib.so
%{_libdir}/pkgconfig/dbusmenu-glib-0.4.pc
%{_datadir}/gir-1.0/Dbusmenu-0.4.gir
%{_datadir}/vala/vapi/Dbusmenu-0.4.vapi

%files jsonloader
%{_libdir}/libdbusmenu-jsonloader.so.*

%files jsonloader-devel
%dir %{_includedir}/libdbusmenu-glib-0.4/
%dir %{_includedir}/libdbusmenu-glib-0.4/libdbusmenu-jsonloader/
%{_includedir}/libdbusmenu-glib-0.4/libdbusmenu-jsonloader/*.h
%{_libdir}/libdbusmenu-jsonloader.so
%{_libdir}/pkgconfig/dbusmenu-jsonloader-0.4.pc

%files gtk3
%{_libdir}/libdbusmenu-gtk3.so.*
%{_libdir}/girepository-1.0/DbusmenuGtk3-0.4.typelib

%if %{with gtk2}
%files gtk2
%{_libdir}/libdbusmenu-gtk.so.*
%{_libdir}/girepository-1.0/DbusmenuGtk-0.4.typelib
%endif

%files gtk3-devel
%dir %{_includedir}/libdbusmenu-gtk3-0.4
%dir %{_includedir}/libdbusmenu-gtk3-0.4/libdbusmenu-gtk
%{_includedir}/libdbusmenu-gtk3-0.4/libdbusmenu-gtk/*.h
%{_libdir}/libdbusmenu-gtk3.so
%{_libdir}/pkgconfig/dbusmenu-gtk3-0.4.pc
%{_datadir}/gir-1.0/DbusmenuGtk3-0.4.gir
%{_datadir}/vala/vapi/DbusmenuGtk3-0.4.vapi

%if %{with gtk2}
%files gtk2-devel
%dir %{_includedir}/libdbusmenu-gtk-0.4
%dir %{_includedir}/libdbusmenu-gtk-0.4/libdbusmenu-gtk
%{_includedir}/libdbusmenu-gtk-0.4/libdbusmenu-gtk/*.h
%{_libdir}/libdbusmenu-gtk.so
%{_libdir}/pkgconfig/dbusmenu-gtk-0.4.pc
%{_datadir}/gir-1.0/DbusmenuGtk-0.4.gir
%{_datadir}/vala/vapi/DbusmenuGtk-0.4.vapi
%endif

%files doc
%dir %{_datadir}/gtk-doc/
%{_datadir}/gtk-doc/*

%files tools
%{_libexecdir}/dbusmenu-testapp
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/json/
%{_datadir}/%{name}/json/test-gtk-label.json

%changelog
* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 16.04.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 16.04.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 16.04.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 16.04.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 16.04.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Nov 06 2023 Tomas Popela <tpopela@redhat.com> - 16.04.0-25
- Drop the requirements on dbus-glib as the project was migrated to GDBus

* Thu Nov 02 2023 Tomas Popela <tpopela@redhat.com> - 16.04.0-24
- Build require GTK+ 2 conditionally (follow up fix for previous change)

* Tue Oct 10 2023 Takao Fujiwara <fujiwara@redhat.com> - 16.04.0-23
- Delete GTK2 sub packages for RHEL

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 16.04.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 16.04.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 16.04.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 16.04.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 16.04.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 16.04.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 16.04.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 16.04.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 09 2019 Fabio Valentini <decathorpe@gmail.com> - 16.04.0-14
- Remove benchmarking tool, drop python2 dependency.

* Mon Sep 09 2019 Fabio Valentini <decathorpe@gmail.com> - 16.04.0-13
- Remove -Werror flag to fix build despite usage of deprecated things.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 16.04.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 26 2019 Kalev Lember <klember@redhat.com> - 16.04.0-11
- Explicitly enable gobject-introspection support

* Mon Feb 04 2019 Kalev Lember <klember@redhat.com> - 16.04.0-10
- Update BRs for vala packaging changes

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 16.04.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 16.04.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Charalampos Stratakis <cstratak@redhat.com> - 16.04.0-7
- Remove gnome-doc-utils build dependency

* Wed Feb 07 2018 Iryna Shcherbina <ishcherb@redhat.com> - 16.04.0-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 16.04.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16.04.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16.04.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Apr 17 2017 Simone Caronni <negativo17@gmail.com> - 16.04.0-2
- Add tests, remove valgrind-devel build requirements (#1262274).
- Disable tests until dbus-test-runner is available.

* Sun Apr 16 2017 Simone Caronni <negativo17@gmail.com> - 16.04.0-1
- Update to 16.04.0.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 12.10.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 12.10.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.10.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.10.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 12.10.2-7
- Rebuilt for gobject-introspection 1.41.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.10.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 26 2013 Eduardo Echeverria <echevemaster@gmail.com> - 12.10.2-5
- switch to unversioned documentation directory

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.10.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 02 2013 Dan Horák <dan[at]danny.cz> - 12.10.2-3
- valgrind exists only on selected arches

* Mon May 27 2013 Eduardo Echeverria <echevemaster@gmail.com> - 12.10.2-2
- Fix issues with macros-in-comment
- Fix cosmetics errors
- Workaround for the docs files
- Fix a issue with the ownership of the some directories

* Sun Feb 17 2013 Eduardo Echeverria <echevemaster@gmail.com> - 12.10.2-1
- initial packaging
