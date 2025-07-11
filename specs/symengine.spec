%global common_description %{expand:
SymEngine is a standalone fast C++ symbolic manipulation library. Optional thin
wrappers allow usage of the library from other languages.}

Name:           symengine
Version:        0.14.0
Release:        %autorelease
Summary:        Fast symbolic manipulation library
License:        MIT
URL:            https://symengine.org/
ExcludeArch:    %{ix86}

Source0:        https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         https://github.com/symengine/symengine/commit/d8234815beee37447bd85d51c70f4a855509c20f.patch
Patch1:         https://github.com/symengine/symengine/commit/00085a24acbffd95dafb94331fa4a07a0da44ffa.patch

BuildRequires:  cereal-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  flint-devel
BuildRequires:  llvm-devel
BuildRequires:  zlib-devel

%description    %{common_description}

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake-filesystem

%description    devel %{common_description}

The %{name}-devel package contains libraries and header files for developing
applications that use SymEngine.

%prep
%autosetup -p1
sed -i -e 's|DEF_INSTALL_CMAKE_DIR lib/cmake|DEF_INSTALL_CMAKE_DIR %{_lib}/cmake|g' CMakeLists.txt

%build
# https://github.com/symengine/symengine?tab=readme-ov-file#recommended-options-to-build
%cmake \
    -DINTEGER_CLASS=flint \
%ifarch s390x
    -DHAVE_SYMENGINE_RTTI=no \
%endif
    -DWITH_GMP=on \
    -DWITH_LLVM=on \
    -DWITH_LLVM=on \
    -DWITH_MPFR=on \
    -DWITH_SYSTEM_CEREAL=on \
    -DWITH_SYMENGINE_THREAD_SAFE=on
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%doc AUTHORS README.md
%{_libdir}/libsymengine.so.0.14
%{_libdir}/libsymengine.so.%{version}

%files devel
%{_includedir}/%{name}/
%dir %{_libdir}/cmake/%{name}
%{_libdir}/cmake/%{name}/SymEngineConfig.cmake
%{_libdir}/cmake/%{name}/SymEngineConfigVersion.cmake
%{_libdir}/cmake/%{name}/SymEngineTargets-release.cmake
%{_libdir}/cmake/%{name}/SymEngineTargets.cmake
%{_libdir}/lib%{name}.so

%changelog
%autochangelog
