%global __cmake_in_source_build 1

%global		with_snapshot	0
#%%global		prerelease	beta
#%%global		commit		40b9aca2668f443cae6bfbfa7cc5a354f1087011
#%%global		shortcommit	%%(c=%%{commit}; echo ${c:0:7})
%bcond_without	ispc

Name:		embree
Version:	4.3.1
Release:	%autorelease
Summary:	Collection of high-performance ray tracing kernels

License:	Apache-2.0
URL:		https://embree.github.io
%if %{with_snapshot}
Source:		https://github.com/%{name}/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz#/%{name}-%{version}-%{shortcommit}.tar.gz
%else
Source:		https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
%endif

BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	giflib-devel
%if %{with ispc} 
BuildRequires:	ispc
%endif
BuildRequires:	pkgconfig(glut)
BuildRequires:	pkgconfig(glfw3)
BuildRequires:	pkgconfig(xmu)
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(OpenImageIO)
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

%prep
%if %{with_snapshot}
%autosetup -n %{name}-%{commit}
%else 
%autosetup -p1 -n %{name}-%{version}
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
	-DEMBREE_MAX_ISA=NONE \
%ifarch x86_64
	-DEMBREE_ISA_SSE2=ON \
	-DEMBREE_ISA_SSE4=ON \
	-DEMBREE_ISA_AVX=ON \
	-DEMBREE_ISA_AVX2=ON \
%else
	-DEMBREE_ARM=ON \
	-DEMBREE_ISA_NEON=ON \
%endif
	-DEMBREE_TUTORIALS=ON \
	-DEMBREE_TESTING=ON \
	-DEMBREE_STATIC_LIB=OFF
%cmake_build

%check
%ctest

%install
%cmake_install

# Remove installers
rm %{buildroot}%{_prefix}/%{name}-vars.{csh,sh}

# Relocate doc files
mv %{buildroot}%{_docdir}/%{name}4 %{buildroot}%{_docdir}/%{name}
rm %{buildroot}%{_docdir}/%{name}/LICENSE.txt

# Remove the testing products
rm -r %{buildroot}%{_prefix}/src
rm -r %{buildroot}%{_bindir}/models
rm %{buildroot}%{_bindir}/embree_*

%files
%license LICENSE.txt
%doc README.md CHANGELOG.md readme.pdf third-party-programs{,-TBB,-DPCPP,-OIDN,-oneAPI-DPCPP}.txt
%{_libdir}/lib%{name}4.so.4
%{_mandir}/man3/*

%files devel
%{_libdir}/lib%{name}4.so
%{_includedir}/%{name}4/
%{_libdir}/cmake/%{name}-%{version}/

%changelog
%autochangelog
