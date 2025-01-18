%global baseversion 2.2

Name:           c++-gtk-utils
Version:        2.2.20
Release:        10%{?dist}
Summary:        A library for GTK+ programming with C++

# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2
URL:            http://cxx-gtk-utils.sourceforge.net/
Source0:        http://downloads.sourceforge.net/cxx-gtk-utils/%{name}-%{version}.tar.gz
Patch0:         %{name}-gcc11.patch

BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  make

%description
c++-gtk-utils is a lightweight library containing a number of classes and
functions for programming GTK+ programs using C++ in POSIX (Unix-like)
environments, where the user does not want to use a full-on wrapper such as
gtkmm or wxWidgets, or is concerned about exception safety or thread safety of
the wrapper and their documentation.

%package gtk2
Summary:        A library for GTK+ programming with C++ - GTK2 version
BuildRequires:  gtk2-devel

%description gtk2
c++-gtk-utils is a lightweight library containing a number of classes and
functions for programming GTK+ programs using C++ in POSIX (Unix-like)
environments, where the user does not want to use a full-on wrapper such as
gtkmm or wxWidgets, or is concerned about exception safety or thread safety of
the wrapper and their documentation.

This version is built against GTK2.

%package gtk3
Summary:        A library for GTK+ programming with C++ - GTK3 version
BuildRequires:  gtk3-devel

%description gtk3
c++-gtk-utils is a lightweight library containing a number of classes and
functions for programming GTK+ programs using C++ in POSIX (Unix-like)
environments, where the user does not want to use a full-on wrapper such as
gtkmm or wxWidgets, or is concerned about exception safety or thread safety of
the wrapper and their documentation.

This version is built against GTK3.

%package gtk4
Summary:        A library for GTK+ programming with C++ - GTK4 version
BuildRequires:  gtk4-devel

%description gtk4
c++-gtk-utils is a lightweight library containing a number of classes and
functions for programming GTK+ programs using C++ in POSIX (Unix-like)
environments, where the user does not want to use a full-on wrapper such as
gtkmm or wxWidgets, or is concerned about exception safety or thread safety of
the wrapper and their documentation.

This version is built against GTK4.

%package gtk2-devel
Summary:        Development files for the c++-gtk-utils library - GTK2 version
Requires:       %{name}-gtk2%{?_isa} = %{version}-%{release}

%description gtk2-devel
This package contains libraries and header files needed for development of
applications or toolkits which use c++-gtk-utils.

This version is built against GTK2.

%package gtk3-devel
Summary:        Development files for the c++-gtk-utils library - GTK3 version
Requires:       %{name}-gtk3%{?_isa} = %{version}-%{release}

%description gtk3-devel
This package contains libraries and header files needed for development of
applications or toolkits which use c++-gtk-utils.

This version is built against GTK3.

%package gtk4-devel
Summary:        Development files for the c++-gtk-utils library - GTK4 version
Requires:       %{name}-gtk4%{?_isa} = %{version}-%{release}

%description gtk4-devel
This package contains libraries and header files needed for development of
applications or toolkits which use c++-gtk-utils.

This version is built against GTK4.

%package devel-doc
Summary:        Development documentation for the c++-gtk-utils library
BuildArch:      noarch

%description devel-doc
This package contains documentation files for development of applications or
toolkits which use c++-gtk-utils.

%prep
%setup -q -n %{name}-%{version} -c
pushd %{name}-%{version}
%patch -P0 -p1
popd
mv %{name}-{,gtk2-}%{version}
cp -a %{name}-gtk{2,3}-%{version}
cp -a %{name}-gtk{2,4}-%{version}

%build
pushd %{name}-gtk2-%{version}
mv -f configure-gtk2 configure
%configure --disable-static
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
%make_build V=1
popd

pushd %{name}-gtk3-%{version}
%configure --disable-static
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
%make_build V=1
popd

pushd %{name}-gtk4-%{version}
mv -f configure-gtk4 configure
%configure --disable-static
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
%make_build V=1
popd

%install
pushd %{name}-gtk2-%{version}
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/*.la
popd

pushd %{name}-gtk3-%{version}
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/*.la
popd

pushd %{name}-gtk4-%{version}
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/*.la
popd


%files gtk2
%{_libdir}/libcxx-gtk-utils-2-%{baseversion}.so.0*
%dir %{_defaultdocdir}/%{name}
%dir %{_defaultdocdir}/%{name}/%{baseversion}
%{_defaultdocdir}/%{name}/%{baseversion}/BUGS
%{_defaultdocdir}/%{name}/%{baseversion}/COPYING
%{_defaultdocdir}/%{name}/%{baseversion}/NEWS
%{_defaultdocdir}/%{name}/%{baseversion}/README

%files gtk3
%{_libdir}/libcxx-gtk-utils-3-%{baseversion}.so.0*
%dir %{_defaultdocdir}/%{name}
%dir %{_defaultdocdir}/%{name}/%{baseversion}
%{_defaultdocdir}/%{name}/%{baseversion}/BUGS
%{_defaultdocdir}/%{name}/%{baseversion}/COPYING
%{_defaultdocdir}/%{name}/%{baseversion}/NEWS
%{_defaultdocdir}/%{name}/%{baseversion}/README

%files gtk4
%{_libdir}/libcxx-gtk-utils-4-%{baseversion}.so.0*
%dir %{_defaultdocdir}/%{name}
%dir %{_defaultdocdir}/%{name}/%{baseversion}
%{_defaultdocdir}/%{name}/%{baseversion}/BUGS
%{_defaultdocdir}/%{name}/%{baseversion}/COPYING
%{_defaultdocdir}/%{name}/%{baseversion}/NEWS
%{_defaultdocdir}/%{name}/%{baseversion}/README

%files gtk2-devel
%{_libdir}/pkgconfig/%{name}-2-%{baseversion}.pc
%{_libdir}/libcxx-gtk-utils-2-%{baseversion}.so
%{_includedir}/%{name}-2-%{baseversion}

%files gtk3-devel
%{_libdir}/pkgconfig/%{name}-3-%{baseversion}.pc
%{_libdir}/libcxx-gtk-utils-3-%{baseversion}.so
%{_includedir}/%{name}-3-%{baseversion}

%files gtk4-devel
%{_libdir}/pkgconfig/%{name}-4-%{baseversion}.pc
%{_libdir}/libcxx-gtk-utils-4-%{baseversion}.so
%{_includedir}/%{name}-4-%{baseversion}

%files devel-doc
%dir %{_defaultdocdir}/%{name}
%dir %{_defaultdocdir}/%{name}/%{baseversion}
%{_defaultdocdir}/%{name}/%{baseversion}/COPYING
%{_defaultdocdir}/%{name}/%{baseversion}/PORTING-TO-%{baseversion}
%{_defaultdocdir}/%{name}/%{baseversion}/html

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.20-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 2.2.20-9
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.20-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.20-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.20-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.20-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar 08 2021 Frederik Holden <frh+fedora@frh.no> - 2.2.20-1
- Upgrade to newest version (2.2 branch)
- Add GTK4 subpackages
- Spec file cleanups

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.16-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 09 2020 Jeff Law <law@redhat.com> - 2.0.16-20
- Fix bogus volatile caught by gcc-11

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.16-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.16-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.16-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.16-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 19 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.0.16-15
- Use C.UTF-8 locale
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 2.0.16-14
- Rebuild with fixed binutils

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.16-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.16-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.16-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.16-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.16-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.16-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 2.0.16-7
- Fix FTBFS with current libtool

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 28 2013 Frederik Holden <frh+fedora@frh.no> - 2.0.16-2
- Temporary fix for bz 925145 (aarch64 support) until new upstream release.
- Changed the build step so it doesn't unnecessarily ./configure twice.

* Wed Mar 13 2013 Frederik Holden <frh+fedora@frh.no> - 2.0.16-1
- Updated to newest upstream release.

* Thu Feb 28 2013 Frederik Holden <frh+fedora@frh.no> - 2.0.15-2
- Fixed an error in the package summary.

* Thu Feb 14 2013 Frederik Holden <frh+fedora@frh.no> - 2.0.15-1
- Updated to newest upstream release.

* Tue Feb 12 2013 Frederik Holden <frh+fedora@frh.no> - 2.0.14-3
- Built for both GTK2 and GTK3, with separate versions for each one.

* Tue Feb 12 2013 Frederik Holden <frh+fedora@frh.no> - 2.0.14-2
- Made the build more verbose.

* Fri Feb 08 2013 Frederik Holden <frh+fedora@frh.no> - 2.0.14-1
- Initial version of the package.
