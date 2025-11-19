
%if 0%{?fedora}
%bcond_without mingw
%else
%bcond_with mingw
%endif

%global common_description %{expand:
PhysicsFS is a library to provide abstract access to various archives. It is
intended for use in video games, and the design was somewhat inspired by Quake
3's file subsystem. The programmer defines a "write directory" on the physical
filesystem. No file writing done through the PhysicsFS API can leave that write
directory, for security. For example, an embedded scripting language cannot
write outside of this path if it uses PhysFS for all of its I/O, which means
that untrusted scripts can run more safely. Symbolic links can be disabled as
well, for added safety. For file reading, the programmer lists directories and
archives that form a "search path". Once the search path is defined, it becomes
a single, transparent hierarchical filesystem. This makes for easy access to
ZIP files in the same way as you access a file directly on the disk, and it
makes it easy to ship a new archive that will override a previous archive on a
per-file basis. Finally, PhysicsFS gives you platform-abstracted means to
determine if CD-ROMs are available, the user's home directory, where in the
real filesystem your program is running, etc.}

Name:		physfs
Version:	3.2.0
Release:	%autorelease
License:	Zlib
Summary:	Library to provide abstract access to various archives
URL:		https://www.icculus.org/physfs/
Source0:	https://github.com/icculus/physfs/archive/refs/tags/release-%{version}.tar.gz
Patch0:		https://github.com/icculus/physfs/commit/32858b462a7d8017697a0f20bab160b5a4d8507a.patch
BuildRequires:  gcc-c++
BuildRequires:	doxygen, readline-devel, libtool, cmake
# Only needed to build a test program.
# BuildRequires:	wxGTK-devel
Provides:	bundled(lzma-sdk457)

%if %{with mingw}
BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-binutils
BuildRequires: mingw32-gettext
BuildRequires: mingw32-win-iconv
BuildRequires: mingw32-zlib
BuildRequires: mingw32-readline

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-binutils
BuildRequires: mingw64-gettext
BuildRequires: mingw64-win-iconv
BuildRequires: mingw64-zlib
BuildRequires: mingw64-readline
%endif

%description
%{common_description}

%package devel
Summary:	Development libraries and headers for physfs
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the libraries and headers necessary for developing
packages with physfs functionality.

%if %{with mingw}

# Win32
%package -n mingw32-physfs
Summary:       MinGW compiled physfs library for the Win32 target

%description -n mingw32-physfs
%{common_description}

%package -n mingw32-physfs-static
Summary:       Static version of the MinGW Win32 compiled physfs library
Requires:      mingw32-physfs = %{version}-%{release}

%description -n mingw32-physfs-static
Static version of the MinGW Win32 compiled physfs library.

# Win64
%package -n mingw64-physfs
Summary:       MinGW compiled physfs library for the Win64 target

%description -n mingw64-physfs
%{common_description}

%package -n mingw64-physfs-static
Summary:       Static version of the MinGW Win64 compiled physfs library
Requires:      mingw64-physfs = %{version}-%{release}

%description -n mingw64-physfs-static
Static version of the MinGW Win64 compiled physfs library.

%endif # %%{with mingw}

%{?mingw_debug_package}

%prep
%autosetup -p1 -n %{name}-release-%{version}

%build
%cmake
%cmake_build
doxygen %{_vpath_builddir}/Doxyfile

%if %{with mingw}
%mingw_cmake -DPHYSFS_BUILD_TEST=OFF -DPHYSFS_BUILD_WX_TEST=OFF
%mingw_make_build
%endif # %%{with mingw}

%install
%cmake_install
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.la
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man3
install -m0644 %{_vpath_builddir}/docs/man/man3/* $RPM_BUILD_ROOT%{_mandir}/man3

# Handle man page conflicts (bz #183705)
mv $RPM_BUILD_ROOT%{_mandir}/man3/author.3 $RPM_BUILD_ROOT%{_mandir}/man3/physfs-author.3
mv $RPM_BUILD_ROOT%{_mandir}/man3/deprecated.3 $RPM_BUILD_ROOT%{_mandir}/man3/physfs-deprecated.3
mv $RPM_BUILD_ROOT%{_mandir}/man3/description.3 $RPM_BUILD_ROOT%{_mandir}/man3/physfs-description.3
mv $RPM_BUILD_ROOT%{_mandir}/man3/extension.3 $RPM_BUILD_ROOT%{_mandir}/man3/physfs-extension.3
mv $RPM_BUILD_ROOT%{_mandir}/man3/major.3 $RPM_BUILD_ROOT%{_mandir}/man3/physfs-major.3
mv $RPM_BUILD_ROOT%{_mandir}/man3/minor.3 $RPM_BUILD_ROOT%{_mandir}/man3/physfs-minor.3
mv $RPM_BUILD_ROOT%{_mandir}/man3/patch.3 $RPM_BUILD_ROOT%{_mandir}/man3/physfs-patch.3
mv $RPM_BUILD_ROOT%{_mandir}/man3/url.3 $RPM_BUILD_ROOT%{_mandir}/man3/physfs-url.3
mv $RPM_BUILD_ROOT%{_mandir}/man3/remove.3 $RPM_BUILD_ROOT%{_mandir}/man3/physfs-remove.3

# Rename poorly named manpages
for i in Deinit Free Init Malloc Realloc opaque; do
  mv $RPM_BUILD_ROOT%{_mandir}/man3/$i.3 $RPM_BUILD_ROOT%{_mandir}/man3/physfs-$i.3
done

# Fix multilib conflicts
touch -r LICENSE.txt %{_vpath_builddir}/docs/html/*
touch -r LICENSE.txt %{_vpath_builddir}/docs/latex/*

# Get rid of static library.
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.a

%if %{with mingw}
%mingw_make_install
%endif # %%{with mingw}

%{?mingw_debug_install_post}

%files
%license LICENSE.txt
%doc docs/CHANGELOG.txt docs/CREDITS.txt docs/TODO.txt
%{_libdir}/*.so.*

%files devel
%doc %{_vpath_builddir}/docs/html/
%{_bindir}/test_physfs
%{_includedir}/physfs.h
%{_libdir}/*.so
%{_libdir}/cmake/PhysFS/
%{_libdir}/pkgconfig/physfs.pc
%{_mandir}/man3/*

%if %{with mingw}

# Win32
%files -n mingw32-physfs
%license LICENSE.txt
%{mingw32_bindir}/libphysfs.dll
%{mingw32_includedir}/physfs.h
%{mingw32_libdir}/libphysfs.dll.a
%{mingw32_libdir}/cmake/PhysFS/
%{mingw32_libdir}/pkgconfig/physfs.pc

%files -n mingw32-physfs-static
%{mingw32_libdir}/libphysfs.a

# Win64
%files -n mingw64-physfs
%license LICENSE.txt
%{mingw64_bindir}/libphysfs.dll
%{mingw64_includedir}/physfs.h
%{mingw64_libdir}/libphysfs.dll.a
%{mingw64_libdir}/cmake/PhysFS/
%{mingw64_libdir}/pkgconfig/physfs.pc

%files -n mingw64-physfs-static
%{mingw64_libdir}/libphysfs.a

%endif # %%{with mingw}

%changelog
%autochangelog
