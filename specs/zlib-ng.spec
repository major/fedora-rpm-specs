%bcond_without compat
%bcond_without sanitizers

# Be explicit about the soname in order to avoid unintentional changes.
# Before modifying any of the sonames, this must be announced to the Fedora
# community as it may break many other packages.
# A change proposal is needed:
# https://docs.fedoraproject.org/en-US/program_management/changes_policy/
%global soname libz-ng.so.2
%global compat_soname libz.so.1

# Compatible with the following zlib version.
%global zlib_ver 1.3.1
# Obsoletes zlib versions less than.
%global zlib_obsoletes 1.3

# ABI files for ix86 and s390x are not available upstream.
%global supported_abi_test aarch64 ppc64le x86_64

Name:		zlib-ng
Version:	2.2.3
Release:	%autorelease
Summary:	Zlib replacement with optimizations
License:	Zlib
Url:		https://github.com/zlib-ng/zlib-ng
Source0:	https://github.com/zlib-ng/zlib-ng/archive/%{version}/%{name}-%{version}.tar.gz

Patch:		far.diff

BuildRequires:	cmake >= 3.1
BuildRequires:	gcc-c++
BuildRequires:	cmake(GTest)
BuildRequires:	libabigail

%description
zlib-ng is a zlib replacement that provides optimizations for "next generation"
systems.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for developing
application that use %{name}.

%if %{with compat}

%package	compat
Summary:	Zlib implementation provided by %{name}
Provides:	zlib = %{zlib_ver}
Provides:	zlib%{?_isa} = %{zlib_ver}
Conflicts:	zlib%{?_isa}
Obsoletes:	zlib < %{zlib_obsoletes}

%description	compat
zlib-ng is a zlib replacement that provides optimizations for "next generation"
systems.
The %{name}-compat package contains the library that is API and binary
compatible with zlib.

%package	compat-devel
Summary:	Development files for %{name}-compat
Requires:	%{name}-compat%{?_isa} = %{version}-%{release}
Provides:	zlib-devel = %{zlib_ver}
Provides:	zlib-devel%{?_isa} = %{zlib_ver}
Conflicts:	zlib-devel%{?_isa}
Obsoletes:	zlib-devel < %{zlib_obsoletes}

%description	compat-devel
The %{name}-compat-devel package contains libraries and header files for
developing application that use zlib.

%package	compat-static
Summary:	Static libraries for %{name}-compat
Requires:	%{name}-compat-devel%{?_isa} = %{version}-%{release}
Provides:	zlib-static = %{zlib_ver}
Provides:	zlib-static%{?_isa} = %{zlib_ver}
Conflicts:	zlib-static%{?_isa}
Obsoletes:	zlib-static < %{zlib_obsoletes}

%description	compat-static
The %{name}-compat-static package contains static libraries needed for
developing applications that use zlib.

%endif

%prep
%autosetup -p1 -n %{name}-%{version}

%build
cat <<_EOF_
###########################################################################
#
# Build the default zlib-ng library
#
###########################################################################
_EOF_

# zlib-ng uses a different macro for library directory.
%global cmake_param %{?with_sanitizers:-DWITH_SANITIZER=ON} -DWITH_RVV=OFF

# Setting __cmake_builddir is not necessary in this step, but do it anyway for symmetry.
%global __cmake_builddir %{_vpath_builddir}
%cmake %{cmake_param}
%cmake_build

%if %{with compat}
cat <<_EOF_
###########################################################################
#
# Build the compat mode library
#
###########################################################################
_EOF_

%global __cmake_builddir %{_vpath_builddir}-compat
# defining BUILD_SHARED_LIBS disables the static library
%undefine _cmake_shared_libs
# Disable new strategies in order to keep compatibility with zlib.
%cmake %{cmake_param} -DZLIB_COMPAT=ON -DWITH_NEW_STRATEGIES=OFF
%cmake_build
%endif

%check
cat <<_EOF_
###########################################################################
#
# Run the zlib-ng tests
#
###########################################################################
_EOF_

%global __cmake_builddir %{_vpath_builddir}
%ctest

%ifarch ppc64le
# Workaround Copr, that sets _target_cpu to ppc64le.
%global target_cpu powerpc64le
%else
%global target_cpu %{_target_cpu}
%endif

%ifarch x86_64
%global cpu_vendor pc
%else
%global cpu_vendor unknown
%endif

%ifarch %{supported_abi_test}
CHOST=%{target_cpu}-%{cpu_vendor}-linux-gnu sh test/abicheck.sh
%endif

%if %{with compat}
cat <<_EOF_
###########################################################################
#
# Run the compat mode tests
#
###########################################################################
_EOF_

%global __cmake_builddir %{_vpath_builddir}-compat
%ctest
%ifarch %{supported_abi_test}
CHOST=%{target_cpu}-%{cpu_vendor}-linux-gnu sh test/abicheck.sh --zlib-compat
%endif
%endif


%install
%global __cmake_builddir %{_vpath_builddir}
%cmake_install

%if %{with compat}
%global __cmake_builddir %{_vpath_builddir}-compat
%cmake_install
%endif

%files
%license LICENSE.md
%doc README.md
%{_libdir}/libz-ng.so.%{version}
%{_libdir}/%{soname}

%files devel
%{_includedir}/zconf-ng.h
%{_includedir}/zlib-ng.h
%{_includedir}/zlib_name_mangling-ng.h
%{_libdir}/libz-ng.so
%{_libdir}/pkgconfig/%{name}.pc
%dir %{_libdir}/cmake/zlib-ng/
%{_libdir}/cmake/zlib-ng/*

%if %{with compat}

%files compat
%{_libdir}/%{compat_soname}
%{_libdir}/libz.so.%{zlib_ver}.zlib-ng

%files compat-devel
%{_includedir}/zconf.h
%{_includedir}/zlib.h
%{_includedir}/zlib_name_mangling.h
%{_libdir}/libz.so
%{_libdir}/pkgconfig/zlib.pc
%dir %{_libdir}/cmake/ZLIB/
%{_libdir}/cmake/ZLIB/*

%files compat-static
%{_libdir}/libz.a


%endif


%changelog
%autochangelog
