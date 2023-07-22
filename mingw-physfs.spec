%{?mingw_package_header}

Name:           mingw-physfs
Version:        3.0.2
Release:        2%{?dist}
Summary:        MinGW compiled physfs library to provide abstract access to various archives

License:        zlib
URL:            http://www.icculus.org/physfs/
Source0:        http://www.icculus.org/physfs/downloads/physfs-%{version}.tar.bz2

BuildArch:      noarch

BuildRequires: make
BuildRequires:  cmake
BuildRequires:  libtool


BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-gettext
BuildRequires:  mingw32-win-iconv
BuildRequires:  mingw32-zlib
BuildRequires:  mingw32-readline


BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-gettext
BuildRequires:  mingw64-win-iconv
BuildRequires:  mingw64-zlib
BuildRequires:  mingw64-readline


%description
MinGW compiled PhysicsFS, a library to provide abstract access 
to various archives. It is intended for use in video games, and the 
design was somewhat inspired by Quake 3's file subsystem. 
The programmer defines a "write directory" on the physical filesystem. 
No file writing done through the PhysicsFS API can leave that 
write directory, for security. 
For example, an embedded scripting language cannot write outside of 
this path if it uses PhysFS for all of its I/O, which means that 
untrusted scripts can run more safely. Symbolic links can be disabled 
as well, for added safety. For file reading, the programmer lists 
directories and archives that form a "search path". 
Once the search path is defined, it becomes a single, 
transparent hierarchical filesystem. 
This makes for easy access to ZIP files in the same way as you access 
a file directly on the disk, and it makes it easy to ship a new archive 
that will override a previous archive on a per-file basis. 
Finally, PhysicsFS gives you platform-abstracted means to determine 
if CD-ROMs are available, the user's home directory, where in the 
real filesystem your program is running, etc.

# Win32
%package -n mingw32-physfs
Summary:       MinGW compiled physfs library for the Win32 target

%description -n mingw32-physfs
MinGW compiled PhysicsFS, a library to provide abstract access 
to various archives. It is intended for use in video games, and the 
design was somewhat inspired by Quake 3's file subsystem. 
The programmer defines a "write directory" on the physical filesystem. 
No file writing done through the PhysicsFS API can leave that 
write directory, for security. 
For example, an embedded scripting language cannot write outside of 
this path if it uses PhysFS for all of its I/O, which means that 
untrusted scripts can run more safely. Symbolic links can be disabled 
as well, for added safety. For file reading, the programmer lists 
directories and archives that form a "search path". 
Once the search path is defined, it becomes a single, 
transparent hierarchical filesystem. 
This makes for easy access to ZIP files in the same way as you access 
a file directly on the disk, and it makes it easy to ship a new archive 
that will override a previous archive on a per-file basis. 
Finally, PhysicsFS gives you platform-abstracted means to determine 
if CD-ROMs are available, the user's home directory, where in the 
real filesystem your program is running, etc.
Compiled for the Win32 target.

%package -n mingw32-physfs-static
Summary:       Static version of the MinGW Win32 compiled physfs library
Requires:      mingw32-physfs = %{version}-%{release}

%description -n mingw32-physfs-static
Static version of the MinGW Win32 compiled physfs library.

# Win64
%package -n mingw64-physfs
Summary:       MinGW compiled physfs library for the Win64 target

%description -n mingw64-physfs
MinGW compiled PhysicsFS, a library to provide abstract access 
to various archives. It is intended for use in video games, and the 
design was somewhat inspired by Quake 3's file subsystem. 
The programmer defines a "write directory" on the physical filesystem. 
No file writing done through the PhysicsFS API can leave that 
write directory, for security. 
For example, an embedded scripting language cannot write outside of 
this path if it uses PhysFS for all of its I/O, which means that 
untrusted scripts can run more safely. Symbolic links can be disabled 
as well, for added safety. For file reading, the programmer lists 
directories and archives that form a "search path". 
Once the search path is defined, it becomes a single, 
transparent hierarchical filesystem. 
This makes for easy access to ZIP files in the same way as you access 
a file directly on the disk, and it makes it easy to ship a new archive 
that will override a previous archive on a per-file basis. 
Finally, PhysicsFS gives you platform-abstracted means to determine 
if CD-ROMs are available, the user's home directory, where in the 
real filesystem your program is running, etc.
Compiled for the Win64 target.

%package -n mingw64-physfs-static
Summary:       Static version of the MinGW Win64 compiled physfs library
Requires:      mingw64-physfs = %{version}-%{release}

%description -n mingw64-physfs-static
Static version of the MinGW Win64 compiled physfs library.


%{?mingw_debug_package}

%prep
%setup -q -n physfs-%{version}

# Ensure we use system zlib
# don't use bundled lzma
rm -rf zlib123
rm -rf lzma


%build
%mingw_cmake . -DPHYSFS_BUILD_TEST=OFF -DPHYSFS_BUILD_WX_TEST=OFF -DPHYSFS_ARCHIVE_7Z=OFF

%install
%mingw_make_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -name "*.la" -delete


# Win32
%files -n mingw32-physfs
%license LICENSE.txt
%{mingw32_bindir}/libphysfs.dll
%{mingw32_includedir}/physfs.h
%{mingw32_libdir}/libphysfs.dll.a
%{mingw32_libdir}/pkgconfig/physfs.pc

%files -n mingw32-physfs-static
%{mingw32_libdir}/libphysfs.a

# Win64
%files -n mingw64-physfs
%license LICENSE.txt
%{mingw64_bindir}/libphysfs.dll
%{mingw64_includedir}/physfs.h
%{mingw64_libdir}/libphysfs.dll.a
%{mingw64_libdir}/pkgconfig/physfs.pc

%files -n mingw64-physfs-static
%{mingw64_libdir}/libphysfs.a


%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Apr 25 2023 Pete Walter <pwalter@fedoraproject.org> - 3.0.2-1
- Update to 3.0.2

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 2.0.3-20
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 2.0.3-14
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Oct 14 2013 maci <maci@satgnu.net> - 2.0.3-4
- remove patch
- build without 7zip support, its unlikely mingw-lzma-sdk457 will ever
  work. Can be re-enabled when xz-devel support is implemented 
  http://icculus.org/pipermail/physfs/2010-December/000971.html


* Thu Jun 06 2013 Marcel Wysocki <maci@satgnu.net> - 2.0.3-3
- rebuilt for mingw-lzma-sdk457 package

* Tue May 14 2013 Marcel Wysocki <maci@satgnu.net> - 2.0.3-2
- spec cleanups

* Sat Apr 27 2013 Marcel Wysocki <maci@satgnu.net> - 2.0.3-1
- Initial release
