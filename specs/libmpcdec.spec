%bcond cuefile 0

# FTBFS with GCC 14 -Werror=incompatible-pointer-types
# https://bugzilla.redhat.com/show_bug.cgi?id=2261331
%global build_type_safety_c 2

%global svn_release 475
# code does not compile with -fno-common
%global _legacy_common_support 1

Summary: Musepack audio decoding library
Name:	 libmpcdec
Version: 1.3.0^20110810svn%{svn_release}
Release: %autorelease

License: BSD-3-Clause
URL: 	 https://www.musepack.net/
Source:  https://files.musepack.net/source/musepack_src_r%{svn_release}.tar.gz

## upstream patches
Patch:   0001-changes-a-seeking-behavior-that-confused-some-people.patch
Patch:   0002-removed-some-gcc-warnings-and-compilation-issues.patch
Patch:   0003-prevent-endless-loops.patch
Patch:   0004-add-extern-keyword-to-global-variable-declaration-do.patch
Patch:   0005-add-raw-output-to-mpcdec-not-really-tested.patch
Patch:   0008-FSF-address-change.patch
Patch:   0011-removed-some-new-gcc-warnings.patch
Patch:   0012-mpcenc-remove-compilation-error-and-a-warning.patch
Patch:   0013-mpc2sv8-fix-a-segfault-caused-by-commit-r476.patch

## upstreamable patches

## downstream patches
Patch:  r475-cmake.patch

BuildRequires: gcc
BuildRequires: sed
BuildRequires: cmake
%if %{with cuefile}
BuildRequires: libcuefile-devel
%endif
BuildRequires: libreplaygain-devel

%description
Musepack is an audio compression format with a strong emphasis on high quality.
It's not lossless, but it is designed for transparency, so that you won't be
able to hear differences between the original wave file and the much smaller
MPC file.
It is based on the MPEG-1 Layer-2 / MP2 algorithms, but has rapidly developed
and vastly improved and is now at an advanced stage in which it contains
heavily optimized and patentless code.

%package devel
Summary: Development files for the Musepack audio decoding library
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%package -n musepack-tools
Summary: Musepack audio decoding and encoding tools
License: BSD-3-Clause AND LGPL-2.1-or-later
Requires: %{name}%{?_isa} = %{version}-%{release}
%description -n musepack-tools
%{summary}.


%prep
%autosetup -p1 -n musepack_src_r%{svn_release}

%if %{without cuefile}
sed -i -e '/add_subdirectory.*mpcchap/d' CMakeLists.txt
%endif

# Correct permissions and end of line
find -type f -exec chmod 0644 '{}' +
sed -ibackup 's/\r$//' libwavformat/*


%build
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake -Wno-dev .
%cmake_build


%install
%cmake_install


%files
%doc libmpcdec/AUTHORS libmpcdec/ChangeLog libmpcdec/README
%license libmpcdec/COPYING
%{_libdir}/libmpcdec.so.6{,.*}

%files devel
%{_includedir}/mpc/
%{_libdir}/libmpcdec.so

%files -n musepack-tools
%license libmpcdec/COPYING
%{_bindir}/mpc*
%{_bindir}/wavcmp


%changelog
%autochangelog
