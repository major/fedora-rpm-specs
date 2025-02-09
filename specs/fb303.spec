%bcond_with toolchain_clang

%if %{with toolchain_clang}
%global toolchain clang
%endif

%global forgeurl https://github.com/facebook/fb303/

# need to figure out how to get the Python bindings to build later
%bcond_with python

# No tests were found!!!
%bcond_without check

Name:           fb303
Version:        2025.02.03.00
Release:        %autorelease
Summary:        Base Thrift service and a common set of functionality

License:        Apache-2.0
URL:            %{forgeurl}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

ExclusiveArch:  x86_64 aarch64 ppc64le riscv64

BuildRequires:  cmake
%if %{with toolchain_clang}
BuildRequires:  clang
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  fbthrift-devel = %{version}
BuildRequires:  fizz-devel = %{version}
BuildRequires:  folly-devel = %{version}
BuildRequires:  mvfst-devel = %{version}
BuildRequires:  gflags-devel
BuildRequires:  glog-devel
%if %{with python}
BuildRequires:  python3-devel
BuildRequires:  python3-fbthrift-devel
%endif
BuildRequires:  wangle-devel

%global _description %{expand:
fb303 is a base Thrift service and a common set of functionality for querying
stats, options, and other information from a service.}

%description %{_description}


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake-filesystem
Obsoletes:      %{name}-static < 0^20220221gitfd133d9-1

%description    devel %{_description}

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1


%build
%cmake \
  -DBUILD_SHARED_LIBS=ON \
  -DCMAKE_INSTALL_DIR=%{_libdir}/cmake/%{name} \
  -DPACKAGE_VERSION=%{version} \
%if %{with python}
  -DPYTHON_EXTENSIONS=ON
%else
  -DPYTHON_EXTENSIONS=OFF
%endif
%cmake_build


%install
%cmake_install


%if %{with check}
%check
%ctest
%endif


%files
%license LICENSE
%doc README.md
%{_libdir}/*.so.%{version}

%files devel
%doc CODE_OF_CONDUCT.md CONTRIBUTING.md
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/%{name}/


%changelog
%autochangelog
