%{?mingw_package_header}

Name:           mingw-colord
Version:        1.2.9
Release:        26%{?dist}
Summary:        Color libraries and data files for MinGW

# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:            http://www.freedesktop.org/software/colord/
Source0:        http://www.freedesktop.org/software/colord/releases/colord-%{version}.tar.xz

BuildArch:      noarch
BuildRequires: make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-glib2
BuildRequires:  mingw64-glib2
BuildRequires:  mingw32-lcms2
BuildRequires:  mingw64-lcms2
BuildRequires:  mingw32-sqlite
BuildRequires:  mingw64-sqlite
BuildRequires:  mingw32-libgusb
BuildRequires:  mingw64-libgusb
BuildRequires:  intltool

# These seem odd BRs, but we actually compile .exe's that are noramlly used to
# generate other binary files. For instance cd-create-profile.exe would be
# linked against the built libcolord.dll and then used to create the shipped
# spectral IT8 files and .icc profiles.
#
# Normally we'd use wine for this, but we can't install wine64 on a i386 builder
# and can't install wine32 on a x64 builder. The build system is clever enough
# to use the host tools if they are installed, which is fine for these kind of
# noarch data files.
BuildRequires:  /usr/bin/cd-it8
BuildRequires:  /usr/bin/cd-create-profile

%description
colord is a low level system activated daemon that maps color devices
to color profiles. This package is designed for MinGW where the color libraries
are being installed without the daemon.

%package -n mingw32-colord
Summary:        Color libraries and data files for MinGW
Requires:       pkgconfig

%description -n mingw32-colord
This package contains the header files and libraries needed to develop
applications that use libcolord.

%package -n mingw32-colord-static
Summary:        Static color libraries and data files for MinGW
Requires:       mingw32-colord = %{version}-%{release}

%description -n mingw32-colord-static
This package contains the static libraries needed to develop
applications that use libcolord.

%package -n mingw64-colord
Summary:        Color libraries and data files for MinGW
Requires:       pkgconfig

%description -n mingw64-colord
This package contains the header files and libraries needed to develop
applications that use libcolord.

%package -n mingw64-colord-static
Summary:        Static color libraries and data files for MinGW
Requires:       mingw64-colord = %{version}-%{release}

%description -n mingw64-colord-static
This package contains the static libraries needed to develop
applications that use libcolord.

%{?mingw_debug_package}


%prep
%setup -q -n colord-%{version}


%build
%mingw_configure \
        --disable-argyllcms-sensor              \
        --disable-bash-completion               \
        --disable-examples                      \
        --disable-polkit                        \
        --disable-print-profiles                \
        --disable-sane                          \
        --disable-session-example               \
        --disable-systemd-login                 \
        --disable-udev                          \
        --without-pic                           \
        --with-systemdsystemunitdir=/tmp        \
        --with-udevrulesdir=/tmp
%mingw_make %{?_smp_mflags} V=1


%install
%mingw_make_install "DESTDIR=$RPM_BUILD_ROOT"

# no idea why libtool is installing locale files into
# /usr/i686-w64-mingw32/sys-root/mingw/lib/locale rather than
# /usr/i686-w64-mingw32/sys-root/mingw/share/locale
mv $RPM_BUILD_ROOT%{mingw32_libdir}/locale $RPM_BUILD_ROOT%{mingw32_datadir}
mv $RPM_BUILD_ROOT%{mingw64_libdir}/locale $RPM_BUILD_ROOT%{mingw64_datadir}

%mingw_find_lang colord

# Libtool files don't need to be bundled
find $RPM_BUILD_ROOT -name "*.la" -delete

# delete 32 bit things we don't want/need
rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}/colord/cmf
rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}/colord/illuminant
rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}/colord/ref
rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}/colord/ti1
rm -rf $RPM_BUILD_ROOT%{mingw32_libdir}/colord-sensors
rm $RPM_BUILD_ROOT%{mingw32_libdir}/bin/*-private.dll

# delete 64 bit things we don't want/need
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}/colord/cmf
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}/colord/illuminant
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}/colord/ref
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}/colord/ti1
rm -rf $RPM_BUILD_ROOT%{mingw64_libdir}/colord-sensors
rm $RPM_BUILD_ROOT%{mingw64_libdir}/bin/*-private.dll


%files -n mingw32-colord -f mingw32-colord.lang
%doc AUTHORS COPYING README.md NEWS
%{mingw32_bindir}/cd-create-profile.exe
%{mingw32_bindir}/cd-fix-profile.exe
%{mingw32_bindir}/cd-iccdump.exe
%{mingw32_bindir}/cd-it8.exe
%{mingw32_bindir}/libcolord-2.dll
%{mingw32_bindir}/libcolordprivate-2.dll
%{mingw32_bindir}/libcolorhug-2.dll
%{mingw32_datadir}/colord
%{mingw32_datadir}/color/icc/colord
%{mingw32_includedir}/colord-1
%{mingw32_libdir}/libcolord.dll.a
%{mingw32_libdir}/libcolordprivate.dll.a
%{mingw32_libdir}/libcolorhug.dll.a
%{mingw32_libdir}/pkgconfig/*.pc

%files -n mingw32-colord-static
%{mingw32_libdir}/libcolord.a
%{mingw32_libdir}/libcolordprivate.a
%{mingw32_libdir}/libcolorhug.a

%files -n mingw64-colord -f mingw64-colord.lang
%doc AUTHORS COPYING README.md NEWS
%{mingw64_bindir}/cd-create-profile.exe
%{mingw64_bindir}/cd-fix-profile.exe
%{mingw64_bindir}/cd-iccdump.exe
%{mingw64_bindir}/cd-it8.exe
%{mingw64_bindir}/libcolord-2.dll
%{mingw64_bindir}/libcolordprivate-2.dll
%{mingw64_bindir}/libcolorhug-2.dll
%{mingw64_datadir}/colord
%{mingw64_datadir}/color/icc/colord
%{mingw64_includedir}/colord-1
%{mingw64_libdir}/libcolord.dll.a
%{mingw64_libdir}/libcolordprivate.dll.a
%{mingw64_libdir}/libcolorhug.dll.a
%{mingw64_libdir}/pkgconfig/*.pc

%files -n mingw64-colord-static
%{mingw64_libdir}/libcolord.a
%{mingw64_libdir}/libcolordprivate.a
%{mingw64_libdir}/libcolorhug.a

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.9-25
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 1.2.9-18
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 12 13:35:14 GMT 2020 Sandro Mani <manisandro@gmail.com> - 1.2.9-14
- Rebuild (mingw-gettext)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 20 2020 Sandro Mani <manisandro@gmail.com> - 1.2.9-12
- Rebuild (gettext)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 1.2.9-10
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 10 2015 Richard Hughes <richard@hughsie.com> - 1.2.9-1
- Update to latest upstream version

* Mon Jan 26 2015 Richard Hughes <richard@hughsie.com> - 1.2.8-1
- Update to latest upstream version

* Wed Nov 19 2014 Richard Hughes <richard@hughsie.com> - 1.2.7-1
- Initial packaging attempt
