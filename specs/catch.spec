Name:           catch
Version:        3.13.0
Release:        %autorelease
Summary:        Modern, C++-native, header-only, framework for unit-tests, TDD and BDD

License:        BSL-1.0
URL:            https://github.com/catchorg/Catch2
Source:         https://github.com/catchorg/Catch2/archive/v%{version}/Catch2-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  python3

%description
Catch2 is mainly a unit testing framework for C++, but it also provides basic
micro-benchmarking features, and simple BDD macros.

Catch2’s main advantage is that using it is both simple and natural. Test names
do not have to be valid identifiers, assertions look like normal C++ boolean
expressions, and sections provide a nice and local way to share set-up and
tear-down code in tests.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p 1 -n Catch2-%{version}


%conf
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCATCH_BUILD_EXTRA_TESTS=ON \
    -DCATCH_ENABLE_WERROR=OFF \
    -DCATCH_INSTALL_DOCS=OFF \
    -DBUILD_SHARED_LIBS=ON


%build
%cmake_build


%install
%cmake_install


%check
%ctest


%files
%license LICENSE.txt
%{_libdir}/libCatch2.so.%{version}
%{_libdir}/libCatch2Main.so.%{version}


%files devel
%doc README.md
%doc docs/
%{_includedir}/catch2/
%{_libdir}/libCatch2.so
%{_libdir}/libCatch2Main.so
%{_libdir}/cmake/Catch2/
%{_datadir}/Catch2/
%{_datadir}/pkgconfig/catch2.pc
%{_datadir}/pkgconfig/catch2-with-main.pc


%changelog
%autochangelog
