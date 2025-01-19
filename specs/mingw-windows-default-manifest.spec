%?mingw_package_header

Name:           mingw-windows-default-manifest
Version:        6.4
Release:        16%{?dist}
Summary:        MinGW Default Windows application manifest

# The source code is FSFAP (see COPYING) except install-sh which is MIT/X11
License:        FSFAP and MIT

# https://cygwin.com/git/?p=cygwin-apps/windows-default-manifest.git;a=summary
URL:            https://cygwin.com/

# How to generate the tarball used in the rpm:
# wget https://cygwin.com/pub/cygwin/x86/release/windows-default-manifest/windows-default-manifest-6.4-1-src.tar.xz
# extract windows-default-manifest-6.4.tar.bz2
# tar -xvf windows-default-manifest-6.4-1-src.tar.xz windows-default-manifest-6.4-1.src/windows-default-manifest-6.4.tar.bz2 --strip=1
Source0:        windows-default-manifest-%{version}.tar.bz2

BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils


%description
The Default Windows application manifest is linked to applications by
default to claim compatibility with the latest Windows versions.
The package version number reflects the latest Windows kernel version
supported by this manifest.

This package contains the MinGW Windows cross compiled default Windows
application manifest.

# Win32
%package -n mingw32-windows-default-manifest
Summary:        MinGW Default Windows application manifest

%description -n mingw32-windows-default-manifest
The Default Windows application manifest is linked to applications by
default to claim compatibility with the latest Windows versions.
The package version number reflects the latest Windows kernel version
supported by this manifest.

This package contains the MinGW Windows cross compiled default Windows
application manifest.

# Win64
%package -n mingw64-windows-default-manifest
Summary:        MinGW Default Windows application manifest

%description -n mingw64-windows-default-manifest
The Default Windows application manifest is linked to applications by
default to claim compatibility with the latest Windows versions.
The package version number reflects the latest Windows kernel version
supported by this manifest.

This package contains the MinGW Windows cross compiled default Windows
application manifest.


%prep
%setup -q -n windows-default-manifest


%build
%mingw_configure
%mingw_make %{?_smp_mflags}


%install
%mingw_make install DESTDIR=$RPM_BUILD_ROOT

# Win32
%files -n mingw32-windows-default-manifest
%doc README
%license COPYING

%{mingw32_libdir}/default-manifest.o

# Win64
%files -n mingw64-windows-default-manifest
%doc README
%license COPYING
%{mingw64_libdir}/default-manifest.o

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 6.4-10
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 27 2018 Wolfgang Stöggl <c72578@yahoo.de> - 6.4-1
- Package has been reviewed
- Use version macro in Source0

* Fri Mar 23 2018 Wolfgang Stöggl <c72578@yahoo.de> - 6.4-0.2
- Add license details for MIT/X11

* Wed Mar 21 2018 Wolfgang Stöggl <c72578@yahoo.de> - 6.4-0.1
- Initial Fedora RPM release
