%global		srcname embree
%global		with_snapshot	0
%global		with_examples	0
%bcond_without	ispc

Name:		%{srcname}3
Version:	3.13.5
Release:	%autorelease
Summary:	Collection of high-performance ray tracing kernels

License:	Apache-2.0
URL:		https://embree.github.io
%if %{with_snapshot}
Source:		https://github.com/%{srcname}/%{srcname}/archive/%{commit}/%{srcname}-%{commit}.tar.gz#/%{srcname}-%{version}-%{shortcommit}.tar.gz
%else
Source:		https://github.com/%{srcname}/%{srcname}/archive/v%{version}%{?prerelease:%{-prerelease}.0}.tar.gz#/%{srcname}-%{version}%{?prerelease:-%{prerelease}.0}.tar.gz
%endif

#[PATCH] Fix Linux aarch64 support on GCC with lax vector conversions
# https://github.com/embree/embree/pull/408/commits/ace05ce4e3bcee8ff4d6204f4dac835f86f17d4a
Patch:		ace05ce4e3bcee8ff4d6204f4dac835f86f17d4a.patch

BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	giflib-devel
%if %{with ispc} 
BuildRequires:	ispc
%endif
BuildRequires:	pkgconfig(glut)
BuildRequires:	pkgconfig(glfw3)
BuildRequires:	pkgconfig(xmu)
# Optional dependencies needed for examples
%if %{with_examples}
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(libopenjp2)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(OpenImageIO)
%endif
BuildRequires:	pkgconfig(tbb)

# Embree only supports these architectures with SSE2 and up enabled
ExclusiveArch:	aarch64 x86_64

%description
A collection of high-performance ray tracing kernels intended to graphics 
application engineers that want to improve the performance of their application.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
 applications that use %{name}.

%if %{with_examples}
%package	examples
Summary:	Example of application using %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	examples
The %{name}-examples package contains sample binaries using %{name}.
%endif

%prep
%if %{with_snapshot}
%autosetup -n %{srcname}-%{commit}
%else 
%autosetup -p1 -n %{srcname}-%{version}%{?prerelease:-%{prerelease}.0}
%endif

%build
%cmake \
	-DCMAKE_BUILD_TYPE=Release \
	-DCMAKE_CXX_FLAGS="%{optflags} -Wl,--as-needed" \
	-DCMAKE_INSTALL_LIBDIR=%{_libdir} \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DEMBREE_COMPACT_POLYS=ON \
	-DEMBREE_IGNORE_CMAKE_CXX_FLAGS=OFF \
%if %{with ispc}
        -DEMBREE_ISPC_SUPPORT=ON \
%endif
%ifarch x86_64
	-DEMBREE_ISA_SSE2=ON \
	-DEMBREE_ISA_SSE4=ON \
	-DEMBREE_ISA_AVX=ON \
	-DEMBREE_ISA_AVX2=ON \
%else
	-DEMBREE_ISA_NEON=ON \
%endif
	-DEMBREE_TUTORIALS=OFF 
%cmake_build

%install
%cmake_install

# Remove duplicated license
rm %{buildroot}%{_docdir}/%{name}/LICENSE.txt

%files
%license LICENSE.txt
%doc README.md CHANGELOG.md readme.pdf third-party-programs-TBB.txt third-party-programs.txt
%{_libdir}/lib%{name}.so.3
%{_libdir}/lib%{name}.so.3.*
%{_mandir}/man3/*

%files devel
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}/
%{_libdir}/cmake/%{srcname}-%{version}/

%if %{with_examples}
%files examples
%{_bindir}/%{name}/*
%endif

%changelog
%autochangelog
