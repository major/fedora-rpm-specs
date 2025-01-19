%?mingw_package_header

Summary:	MinGW build of GLib bindings for D-Bus
Name:		mingw-dbus-glib
Version:	0.112
Release:	12%{?dist}
# Automatically converted from old format: AFL and GPLv2+ - review is highly recommended.
License:	LicenseRef-Callaway-AFL AND GPL-2.0-or-later
URL:		http://dbus.freedesktop.org/
Source:		http://dbus.freedesktop.org/releases/dbus-glib/dbus-glib-%{version}.tar.gz

BuildArch:	noarch

BuildRequires: make
BuildRequires:	mingw32-dbus
BuildRequires:	mingw32-glib2
BuildRequires:	mingw32-expat
BuildRequires:	mingw32-pkg-config
BuildRequires:	mingw32-filesystem >= 95
BuildRequires:	mingw32-gcc
BuildRequires:	mingw32-gcc-c++
BuildRequires:	mingw32-binutils

BuildRequires:	mingw64-dbus
BuildRequires:	mingw64-glib2
BuildRequires:	mingw64-expat
BuildRequires:	mingw64-pkg-config
BuildRequires:	mingw64-filesystem >= 95
BuildRequires:	mingw64-gcc
BuildRequires:	mingw64-gcc-c++
BuildRequires:	mingw64-binutils

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	dbus-glib-devel
BuildRequires:	gtk-doc


%description
D-Bus is a message bus system, a simple way for applications to talk to
one another. D-Bus supplies both a system daemon and a
per-user-log in-session daemon. Also, the message bus is built on top of
a general one-to-one message passing framework, which can be used by
any two apps to communicate directly (without going through the message
bus daemon).


# Win32
%package -n mingw32-dbus-glib
Summary:	MinGW build of GLib bindings for D-Bus

%description -n mingw32-dbus-glib
D-Bus is a message bus system, a simple way for applications to talk to
one another. D-Bus supplies both a system daemon and a
per-user-log in-session daemon. Also, the message bus is built on top of
a general one-to-one message passing framework, which can be used by
any two apps to communicate directly (without going through the message
bus daemon).

%package -n mingw32-dbus-glib-static
Summary:	MinGW build of GLib bindings for D-Bus static build
Requires:	mingw32-dbus-glib = %{version}-%{release}

%description -n mingw32-dbus-glib-static
Static version of the MinGW Windows D-Bus Message Bus System

# Win64
%package -n mingw64-dbus-glib
Summary:	MinGW build of GLib bindings for D-Bus

%description -n mingw64-dbus-glib
D-Bus is a message bus system, a simple way for applications to talk to
one another. D-Bus supplies both a system daemon and a
per-user-log in-session daemon. Also, the message bus is built on top of
a general one-to-one message passing framework, which can be used by
any two apps to communicate directly (without going through the message
bus daemon).

%package -n mingw64-dbus-glib-static
Summary:	MinGW build of GLib bindings for D-Bus static build
Requires:	mingw64-dbus-glib = %{version}-%{release}

%description -n mingw64-dbus-glib-static
Static version of the MinGW Windows D-Bus Message Bus System


%{?mingw_debug_package}


%prep
%setup -q -n dbus-glib-%{version}

%build
autoreconf --install --force
%mingw_configure --enable-static --enable-shared \
	--with-dbus-binding-tool=`which dbus-binding-tool` \
	--disable-bash-completion \
	--disable-abstract-sockets
%mingw_make %{?_smp_mflags}


%install
%mingw_make_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -name '*.la' -delete

rm -r ${RPM_BUILD_ROOT}%{mingw32_mandir}/man1/	# Duplicates native versions
rm -r ${RPM_BUILD_ROOT}%{mingw64_mandir}/man1/

# Win32
%files -n mingw32-dbus-glib
%doc COPYING README NEWS
%{mingw32_bindir}/libdbus-glib-1-2.dll
%{mingw32_includedir}/dbus-1.0/dbus/*.h
%{mingw32_libdir}/libdbus-glib-1.dll.a
%{mingw32_libdir}/pkgconfig/dbus-glib-1.pc
%{mingw32_bindir}/dbus-binding-tool.exe

%files -n mingw32-dbus-glib-static
%{mingw32_libdir}/libdbus-glib-1.a

# Win64
%files -n mingw64-dbus-glib
%doc COPYING README NEWS
%{mingw64_bindir}/libdbus-glib-1-2.dll
%{mingw64_includedir}/dbus-1.0/dbus/*.h
%{mingw64_libdir}/libdbus-glib-1.dll.a
%{mingw64_libdir}/pkgconfig/dbus-glib-1.pc
%{mingw64_bindir}/dbus-binding-tool.exe

%files -n mingw64-dbus-glib-static
%{mingw64_libdir}/libdbus-glib-1.a


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.112-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 0.112-11
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.112-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.112-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.112-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.112-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.112-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.112-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 0.112-4
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.112-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.112-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Apr 26 2021 Greg Hellings <greg.hellings@gmail.com> - 0.112-1
- Upstream version 0.112

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.110-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 12 13:35:51 GMT 2020 Sandro Mani <manisandro@gmail.com> - 0.110-8
- Rebuild (mingw-gettext)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.110-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.110-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.110-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.110-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.110-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.110-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Greg Hellings <greg.hellings@gmail.com> - 0.110-1
- New upstream version 0.110

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.108-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.108-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 01 2016 Greg Hellings <greg.hellings@gmail.com> - 0.108-1
- New upstream version

* Wed Jun 01 2016 Greg Hellings <greg.hellings@gmail.com> - 0.106-1
- New upstream version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.104-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.104-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 11 2015 Greg Hellings <greg.hellings@gmail.com> - 0.104-1
- New upstream version

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.102-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 15 2014 Greg Hellings <greg.hellings@gmail.com> - 0.102-1
- Updated to new upstream version
- Removed upstreamed patch

* Tue Sep 3 2013 Greg Hellings <greg.hellings@gmail.com> - 0.100.2-1
- Updated to new upstream version

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.100-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jan 26 2013 Greg Hellings <greg.hellings@gmail.com> - 0.100-4
- Added patch comment
- Removed resolved comments about License field
- Added --install --force arguments to autoreconf to satisfy rawhide

* Sat Jan 26 2013 Greg Hellings <greg.hellings@gmail.com> - 0.100-3
- Removed config cache files
- Added patch to replace cache file functionality
- Updated license to match native version
- Updated Summary fields to match MinGW packaging guidelines

* Tue Nov 20 2012 Greg Hellings <greg.hellings@gmail.com> - 0.100-2
- Updated to be more in line with packaging guidelines and practices

* Wed Aug 22 2012 Greg Hellings <greg.hellings@gmail.com> - 0.100-1
- Initial import
