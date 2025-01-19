%?mingw_package_header

Summary:        MinGW Windows IDL Parsing Library
Name:           mingw-libIDL
Version:        0.8.14
Release:        27%{?dist}
# Automatically converted from old format: LGPLv2 or MPLv1.1 - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2 OR LicenseRef-Callaway-MPLv1.1
URL:            ftp://ftp.gnome.org/pub/GNOME/sources/libIDL
Source:         ftp://ftp.gnome.org/pub/GNOME/sources/libIDL/0.8/libIDL-%{version}.tar.bz2

BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-glib2
BuildRequires:  mingw32-pkg-config
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-binutils

BuildRequires:  mingw64-glib2
BuildRequires:  mingw64-pkg-config
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-binutils

BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  libtool
BuildRequires:  autoconf automake libtool


%description
MinGW Windows IDL Parsing Library.


# Win32
%package -n mingw32-libIDL
Summary:        MinGW Windows IDL Parsing Library

%description -n mingw32-libIDL
MinGW Windows IDL Parsing Library.

%package -n mingw32-libIDL-static
Summary:        Static version of the MinGW Windows IDL Parsing Library
Requires:       mingw32-libIDL = %{version}-%{release}

%description -n mingw32-libIDL-static
Static version of the MinGW Windows IDL Parsing Library

# Win64
%package -n mingw64-libIDL
Summary:        MinGW Windows IDL Parsing Library

%description -n mingw64-libIDL
MinGW Windows IDL Parsing Library.

%package -n mingw64-libIDL-static
Summary:        Static version of the MinGW Windows IDL Parsing Library
Requires:       mingw64-libIDL = %{version}-%{release}

%description -n mingw64-libIDL-static
Static version of the MinGW Windows IDL Parsing Library


%?mingw_debug_package


%prep
%setup -q -n libIDL-%{version}
autoreconf -i -f

%build
%mingw_configure --enable-shared --enable-static libIDL_cv_long_long_format=I64
sed -e '1,1d' -i libIDL.def
cp libIDL.def build_win32
cp libIDL.def build_win64
%mingw_make


%install
%mingw_make_install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{mingw64_datadir}/idl
mkdir -p $RPM_BUILD_ROOT%{mingw32_datadir}/idl

rm -rf $RPM_BUILD_ROOT%{mingw64_infodir}
rm -rf $RPM_BUILD_ROOT%{mingw32_infodir}

find $RPM_BUILD_ROOT -name '*.la' -delete


# Win32
%files -n mingw32-libIDL
%doc COPYING README ChangeLog
%{mingw32_bindir}/libIDL-2-0.dll
%dir %{mingw32_datadir}/idl
%{mingw32_bindir}/libIDL-config-2
%{mingw32_includedir}/libIDL-2.0/
%{mingw32_libdir}/libIDL-2.dll.a
%{mingw32_libdir}/pkgconfig/libIDL-2.0.pc

%files -n mingw32-libIDL-static
%{mingw32_libdir}/libIDL-2.a

# Win64
%files -n mingw64-libIDL
%doc COPYING README ChangeLog
%{mingw64_bindir}/libIDL-2-0.dll
%dir %{mingw64_datadir}/idl
%{mingw64_bindir}/libIDL-config-2
%{mingw64_includedir}/libIDL-2.0/
%{mingw64_libdir}/libIDL-2.dll.a
%{mingw64_libdir}/pkgconfig/libIDL-2.0.pc

%files -n mingw64-libIDL-static
%{mingw64_libdir}/libIDL-2.a


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.14-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 0.8.14-26
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.14-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.14-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.14-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.14-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.14-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.14-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 0.8.14-19
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.14-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.14-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.14-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 12 13:42:49 GMT 2020 Sandro Mani <manisandro@gmail.com> - 0.8.14-15
- Rebuild (mingw-gettext)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.14-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.14-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 0.8.14-12
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.14-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.14-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 16 2015 Greg Hellings <greg.hellings@gmail.com> - 0.8.14-3
- Update spec file name

* Fri Dec 13 2013 Greg Hellings <greg.hellings@gmail.com> - 0.8.14-2
- Review improvements.

* Wed Aug 22 2012 Greg Hellings <greg.hellings@gmail.com> - 0.8.14-1
- Initial import
