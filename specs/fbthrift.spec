%bcond_with toolchain_clang

%if %{with toolchain_clang}
%global toolchain clang
%endif

# requires python3-Cython >= 0.29.17 for libcpp.utility.move
%if 0%{?fedora} || 0%{?rhel} >= 9
# disable as folly's Python bindings can't currently be built
%bcond_with python
%else
%bcond_with python
%endif

%bcond_without check

# use this to re-test running all tests
%ifarch ppc64le
%bcond_with all_tests
%else
%bcond_without all_tests
%endif

Name:           fbthrift
Version:        2025.02.03.00
Release:        %autorelease
Summary:        Facebook's branch of Apache Thrift, including a new C++ server

License:        Apache-2.0
URL:            https://github.com/facebook/fbthrift
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# revert the fix for https://github.com/facebook/fbthrift/issues/276
# we don't want a mix of dynamic and static libraries
Patch:          %{name}-fix-static-libs.diff

ExclusiveArch:  x86_64 aarch64 ppc64le riscv64

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
BuildRequires:  mvfst-devel = %{version}
BuildRequires:  wangle-devel = %{version}
BuildRequires:  xxhash-devel
# Test dependencies
%if %{with check}
BuildRequires:  gmock-devel
BuildRequires:  gtest-devel
%endif
%if %{without python}
Obsoletes:      python3-%{name} < 2023.04.24.00-1
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
Requires:       xxhash-devel
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

# [ 90%] Generating protocolconformance files. Output: /builddir/build/BUILD/fbthrift-2025.02.03.00-build/fbthrift-2025.02.03.00/redhat-linux-build/thrift/lib/cpp2/test/../../../conformance/if
# cd /builddir/build/BUILD/fbthrift-2025.02.03.00-build/fbthrift-2025.02.03.00/redhat-linux-build/thrift/lib/cpp2/test && ../../../../bin/thrift1 --gen mstch_cpp2:frozen2,include_prefix=thrift/conformance/if -o /builddir/build/BUILD/fbthrift-2025.02.03.00-build/fbthrift-2025.02.03.00/redhat-linux-build/thrift/lib/cpp2/test/../../../conformance/if -I /builddir/build/BUILD/fbthrift-2025.02.03.00-build/fbthrift-2025.02.03.00 /builddir/build/BUILD/fbthrift-2025.02.03.00-build/fbthrift-2025.02.03.00/thrift/lib/cpp2/test/../../../conformance/if/protocol.thrift
# Output path /builddir/build/BUILD/fbthrift-2025.02.03.00-build/fbthrift-2025.02.03.00/redhat-linux-build/thrift/lib/cpp2/test/../../../conformance/if is unusable or not a directory
# make[2]: *** [thrift/lib/cpp2/test/CMakeFiles/protocolconformance-cpp2-target.dir/build.make:80: thrift/conformance/if/gen-cpp2/protocol_constants.h] Error 1
mkdir -p %{__cmake_builddir}/thrift/conformance/if

%cmake_build


%install
%cmake_install

# TODO - need to disable these properly
rm -rf %{buildroot}%{_prefix}/lib/fb-py-libs

%if %{with python}
# Delete RPATHs
chrpath --delete \
  %{buildroot}%{python3_sitearch}/thrift/py3/*.so
%endif


%if %{with check}
%check
%if %{with all_tests}
%ctest
%else

EXCLUDED_TESTS='--exclude-regex '

%ifarch ppc64le
EXCLUDED_TESTS+='F14RoundTripTest\.RoundTrip'
%endif

%ctest -- ${EXCLUDED_TESTS}
%endif

%endif


%files
%license LICENSE
%{_bindir}/thrift1
%{_libdir}/*.so.*

%files devel
%doc CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%{_bindir}/ProtocolBench
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
