%global __cmake_in_source_build 1

%global		with_snapshot	0
%global		with_examples	0
#%%global		prerelease	beta
#%%global		commit		40b9aca2668f443cae6bfbfa7cc5a354f1087011
#%%global		shortcommit	%%(c=%%{commit}; echo ${c:0:7})
%bcond_with	ispc

Name:		embree
Version:	3.13.3
Release:	%autorelease
Summary:	Collection of high-performance ray tracing kernels

License:	ASL 2.0
URL:		https://embree.github.io
%if %{with_snapshot}
Source:		https://github.com/%{name}/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz#/%{name}-%{version}-%{shortcommit}.tar.gz
%else
Source:		https://github.com/%{name}/%{name}/archive/v%{version}%{?prerelease:%{-prerelease}.0}.tar.gz#/%{name}-%{version}%{?prerelease:-%{prerelease}.0}.tar.gz
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
# Optional dependencies needed for examples
%if %{with_examples}
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(libopenjp2)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(OpenImageIO)
%endif
BuildRequires:	pkgconfig(tbb)

# Exclude architectures failing to support SSE2 and up
ExcludeArch:	armv7hl i686 ppc64le s390x

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
%autosetup -n %{name}-%{commit}
%else 
%autosetup -n %{name}-%{version}%{?prerelease:-%{prerelease}.0}
%endif

%build
export CXXFLAGS="%{optflags}"
%cmake \
	-DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_CXX_STANDARD=17 \
	-DCMAKE_INSTALL_LIBDIR=%{_libdir} \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DEMBREE_COMPACT_POLYS=ON \
	-DEMBREE_IGNORE_CMAKE_CXX_FLAGS=OFF \
%if %{with ispc}
        -DEMBREE_ISPC_SUPPORT=ON \
%else
        -DEMBREE_ISPC_SUPPORT=OFF \
%endif
        -DEMBREE_MAX_ISA=DEFAULT \
	-DEMBREE_TUTORIALS=OFF 
%cmake_build

%install
%cmake_install

# Relocate doc files
mv %{buildroot}%{_docdir}/%{name}3 %{buildroot}%{_docdir}/%{name}
rm %{buildroot}%{_docdir}/%{name}/LICENSE.txt

%files
%license LICENSE.txt
%doc README.md CHANGELOG.md readme.pdf third-party-programs-TBB.txt third-party-programs.txt
%{_libdir}/lib%{name}3.so.3
%{_libdir}/lib%{name}3.so.3.*
%{_mandir}/man3/*

%files devel
%{_libdir}/lib%{name}3.so
%{_includedir}/%{name}3/
%{_libdir}/cmake/%{name}-%{version}/

%if %{with_examples}
%files examples
%{_bindir}/%{name}3/*
%endif

%changelog
%autochangelog
