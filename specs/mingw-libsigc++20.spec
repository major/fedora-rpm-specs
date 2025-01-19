%?mingw_package_header

Name:           mingw-libsigc++20
Version:        2.10.3
Release:        14%{?dist}
Summary:        MinGW Windows port of the typesafe signal framework for C++

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://libsigc.sourceforge.net/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/libsigc++/2.10/libsigc++-%{version}.tar.xz

BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw32-binutils
BuildRequires:  mingw64-binutils

BuildRequires:  m4

%description
This library implements a full callback system for use in widget
libraries, abstract interfaces, and general programming. Originally
part of the Gtk-- widget set, libsigc++ is now a separate library to
provide for more general use. It is the most complete library of its
kind with the ability to connect an abstract callback to a class
method, function, or function object. It contains adaptor classes for
connection of dissimilar callbacks and has an ease of use unmatched by
other C++ callback libraries.

Package GTK-- (gtkmm), which is a C++ binding to the GTK+ library,
starting with version 1.1.2, uses libsigc++.


# Win32
%package -n mingw32-libsigc++20
Summary:        MinGW Windows port of the typesafe signal framework for C++

%description -n mingw32-libsigc++20
This library implements a full callback system for use in widget
libraries, abstract interfaces, and general programming. Originally
part of the Gtk-- widget set, libsigc++ is now a separate library to
provide for more general use. It is the most complete library of its
kind with the ability to connect an abstract callback to a class
method, function, or function object. It contains adaptor classes for
connection of dissimilar callbacks and has an ease of use unmatched by
other C++ callback libraries.

Package GTK-- (gtkmm), which is a C++ binding to the GTK+ library,
starting with version 1.1.2, uses libsigc++.

%package -n mingw32-libsigc++20-static
Summary:        Static cross compiled version of the libsigc++ library
Requires:       mingw32-libsigc++20 = %{version}-%{release}

%description -n mingw32-libsigc++20-static
Static cross compiled version of the libsigc++ library.

# Win64
%package -n mingw64-libsigc++20
Summary:        MinGW Windows port of the typesafe signal framework for C++

%description -n mingw64-libsigc++20
This library implements a full callback system for use in widget
libraries, abstract interfaces, and general programming. Originally
part of the Gtk-- widget set, libsigc++ is now a separate library to
provide for more general use. It is the most complete library of its
kind with the ability to connect an abstract callback to a class
method, function, or function object. It contains adaptor classes for
connection of dissimilar callbacks and has an ease of use unmatched by
other C++ callback libraries.

Package GTK-- (gtkmm), which is a C++ binding to the GTK+ library,
starting with version 1.1.2, uses libsigc++.

%package -n mingw64-libsigc++20-static
Summary:        Static cross compiled version of the libsigc++ library
Requires:       mingw64-libsigc++20 = %{version}-%{release}

%description -n mingw64-libsigc++20-static
Static cross compiled version of the libsigc++ library.


%?mingw_debug_package


%prep
%setup -q -n libsigc++-%{version}


%build
%mingw_configure --enable-static --disable-documentation
%mingw_make %{?_smp_mflags}


%install
%mingw_make DESTDIR=$RPM_BUILD_ROOT install
chmod a-x $RPM_BUILD_ROOT/%{mingw32_libdir}/libsigc-2.0.dll.a
chmod a-x $RPM_BUILD_ROOT/%{mingw64_libdir}/libsigc-2.0.dll.a
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/libsigc-2.0.la
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/libsigc-2.0.la


# Win32
%files -n mingw32-libsigc++20
%license COPYING
%{mingw32_bindir}/libsigc-2.0-0.dll
%{mingw32_libdir}/libsigc-2.0.dll.a
%{mingw32_libdir}/pkgconfig/sigc++-2.0.pc
%{mingw32_includedir}/sigc++-2.0
%{mingw32_libdir}/sigc++-2.0

%files -n mingw32-libsigc++20-static
%{mingw32_libdir}/libsigc-2.0.a

# Win64
%files -n mingw64-libsigc++20
%license COPYING
%{mingw64_bindir}/libsigc-2.0-0.dll
%{mingw64_libdir}/libsigc-2.0.dll.a
%{mingw64_libdir}/pkgconfig/sigc++-2.0.pc
%{mingw64_includedir}/sigc++-2.0
%{mingw64_libdir}/sigc++-2.0

%files -n mingw64-libsigc++20-static
%{mingw64_libdir}/libsigc-2.0.a


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 2.10.3-13
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 2.10.3-6
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 02 2020 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.10.3-1
- update to 2.10.3

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 2.10.1-3
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.10.1-1
- update to 2.10.1

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Sep 23 2016 Kalev Lember <klember@redhat.com> - 2.10.0-1
- Update to 2.10.0
- Don't set group tags

* Fri Aug 08 2016 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.9.3-1
- Update to 2.9.3

* Fri Apr 01 2016 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.8.0-1
- Update to 2.8.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 18 2015 Kalev Lember <klember@redhat.com> - 2.6.2-1
- Update to 2.6.2

* Sat Sep 26 2015 Kalev Lember <klember@redhat.com> - 2.6.1-1
- Update to 2.6.1

* Fri Sep 25 2015 Kalev Lember <klember@redhat.com> - 2.6.0-1
- Update to 2.6.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Apr 11 2015 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.4.1-2
- Rebuild against latest mingw-gcc

* Wed Mar 25 2015 Kalev Lember <kalevlember@gmail.com> - 2.4.1-1
- Update to 2.4.1
- Use license macro for the COPYING file

* Wed Oct  1 2014 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.4.0-1
- Update to 2.4.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Mar  3 2013 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.3.1-1
- Update to 2.3.1

* Sun Jan 27 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.2.11-2
- Rebuild against mingw-gcc 4.8 (win64 uses SEH exceptions now)

* Wed Nov 28 2012 Kalev Lember <kalevlember@gmail.com> - 2.2.11-1
- Update to 2.2.11

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Apr  8 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.2.10-7
- Added -static subpackage
- Cleaned up unneeded %%global tags

* Thu Mar 15 2012 Kalev Lember <kalevlember@gmail.com> - 2.2.10-6
- Build 64 bit Windows binaries

* Wed Mar 07 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.2.10-5
- Renamed the source package to mingw-libsigc++20 (RHBZ #800921)
- Use mingw macros without leading underscore

* Tue Feb 28 2012 Kalev Lember <kalevlember@gmail.com> - 2.2.10-4
- Remove the .la files

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.2.10-3
- Rebuild against the mingw-w64 toolchain

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Sep 30 2011 Kalev Lember <kalevlember@gmail.com> - 2.2.10-1
- Update to 2.2.10
- Spec cleanup

* Thu Apr 28 2011 Kalev Lember <kalev@smartlink.ee> - 2.2.9-1
- Update to 2.2.9

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Sep 19 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.2.4.2-1
- update to 2.2.4.2 match native package

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 22 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.2.2-8
- add debuginfo packages

* Thu Apr 16 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.2.2-7
- replace %%define with %%global

* Sun Mar 29 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.2.2-6
- remove executable permission from .dll.a and .la file
- remove inappropriate comment

* Fri Feb 20 2009 Richard W.M. Jones <rjones@redhat.com> - 2.2.2-5
- Rebuild for mingw32-gcc 4.4

* Fri Feb  6 2009 Richard W.M. Jones <rjones@redhat.com> - 2.2.2-4
- Include license file.

* Fri Jan 23 2009 Richard W.M. Jones <rjones@redhat.com> - 2.2.2-3
- Use _smp_mflags.

* Tue Jan 13 2009 Richard W.M. Jones <rjones@redhat.com> - 2.2.2-2
- Requires pkgconfig.

* Fri Oct 24 2008 Richard W.M. Jones <rjones@redhat.com> - 2.2.2-1
- Initial RPM release.
