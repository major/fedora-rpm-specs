%bcond_with toolchain_clang

%if %{with toolchain_clang}
%global toolchain clang
%endif

# requires python3-Cython >= 0.29.17 for libcpp.utility.move
%if 0%{?fedora} || 0%{?rhel} >= 9
%bcond_without python
%else
%bcond_with python
%endif

# tests currently failing
# gmake[2]: *** [thrift/lib/py3/test/CMakeFiles/testing-py3-target.dir/build.make:82: thrift/lib/py3/test/gen-py3/testing_constants.h] Error 1
# [FAILURE:/builddir/build/BUILD/fbthrift-2021.11.15.00/thrift/lib/py3/test/testing.thrift:17] Could not find include file thrift/annotation/cpp.thrift
%bcond_without check

Name:           fbthrift
Version:        2022.07.11.00
Release:        %autorelease
Summary:        Facebook's branch of Apache Thrift, including a new C++ server

License:        ASL 2.0
URL:            https://github.com/facebook/fbthrift
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# causes deleted function error, revert
# traced to https://github.com/facebook/fbthrift/blob/c1be51b727557db4696c9f39fff114dd44eaba4b/thrift/lib/py3/serializer.pyx#L80
Patch:          %{name}-fix_serializer_assignment.patch
# need to properly fix this; temporarily work around by disabling py3 tests
# [FAILURE:/builddir/build/BUILD/fbthrift-2022.07.11.00/thrift/lib/py3/test/testing.thrift:17] Could not find include file thrift/annotation/cpp.thrift
# Patch:          %%{name}-fix_py3_test_includes.patch
Patch:          %{name}-disable_py3_tests.patch
# when compiling with clang but with gcc's libstdc++, this is needed
Source1:        %{name}-fix_contextstack.patch

ExclusiveArch:  x86_64 aarch64 ppc64le

BuildRequires:  cmake
%if %{with toolchain_clang}
BuildRequires:  clang
%else
BuildRequires:  gcc-c++
%endif
# Tool dependencies
BuildRequires:  bison
BuildRequires:  chrpath
BuildRequires:  flex
# Library dependencies
BuildRequires:  fizz-devel = %{version}
BuildRequires:  folly-devel = %{version}
BuildRequires:  wangle-devel = %{version}
# Test dependencies
%if %{with check}
BuildRequires:  gmock-devel
BuildRequires:  gtest-devel
%endif

%global _description %{expand:
Thrift is a serialization and RPC framework for service communication. Thrift
enables these features in all major languages, and there is strong support for
C++, Python, Hack, and Java. Most services at Facebook are written using Thrift
for RPC, and some storage systems use Thrift for serializing records on disk.

Facebook Thrift is not a distribution of Apache Thrift. This is an evolved
internal branch of Thrift that Facebook re-released to open source community in
February 2014. Facebook Thrift was originally released closely tracking Apache
Thrift but is now evolving in new directions. In particular, the compiler was
rewritten from scratch and the new implementation features a fully asynchronous
Thrift server.}

%description %{_description}


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Conflicts:      thrift-devel
Obsoletes:      %{name}-static < 2022.02.28.00-1

%description    devel %{_description}

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%if %{with python}
%package -n python3-%{name}
Summary:        Python bindings for %{name}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-folly-devel
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(wheel)
Requires:       %{name}%{?_isa} = %{version}-%{release}
Conflicts:      python3-thrift

%description -n python3-%{name} %{_description}

The python3-%{name} package contains Python bindings for %{name}.


%package -n python3-%{name}-devel
Summary:        Development files for python3-%{name}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       python3-%{name}%{?_isa} = %{version}-%{release}

%description -n python3-%{name}-devel %{_description}

The python3-%{name}-devel package contains libraries and header files for
developing applications that use python3-%{name}.
%endif


%prep
%autosetup -p1
%if %{with toolchain_clang}
cat %{SOURCE1} | patch -p1
%endif


%build
%cmake \
  -DCMAKE_INSTALL_DIR=%{_libdir}/cmake/%{name} \
  -DCMAKE_SKIP_INSTALL_RPATH=TRUE \
  -DPACKAGE_VERSION=%{version} \
%if %{with python}
  -Dthriftpy3=ON \
%endif
%if %{with check}
  -Denable_tests=ON
%else
  -Denable_tests=OFF
%endif
%cmake_build


%install
%cmake_install

# find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%if %{with python}
# Delete RPATHs
chrpath --delete \
  $RPM_BUILD_ROOT%{python3_sitearch}/thrift/py3/*.so
%endif


%if %{with check}
%check
%ctest
%endif


%files
%license LICENSE
%{_bindir}/thrift1
%{_libdir}/*.so.*

%files devel
%doc CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/%{name}
%exclude %{_includedir}/thrift/lib/py3

%if %{with python}
%files -n python3-%{name}
%{python3_sitearch}/thrift
%{python3_sitearch}/thrift-0.0.1-py%{python3_version}.egg-info
%exclude %{python3_sitearch}/thrift/py3/*.pxd

%files -n python3-%{name}-devel
%{_includedir}/thrift/lib/py3
%{python3_sitearch}/thrift/*.pxd
%{python3_sitearch}/thrift/py3/*.pxd
%endif


%changelog
%autochangelog
