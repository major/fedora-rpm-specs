## This SPEC file compiles NativeJIT library including specific modifications for
# COPASI project (see COPASI package).
## NativeJIT code (fork) repository from COPASI team: https://github.com/copasi/copasi-dependencies/tree/master/src/NativeJIT
## Original NativeJIT repository: https://github.com/BitFunnel/NativeJIT

# This library works specifically on x86_64 systems with SSE4 (Streaming SIMD Extensions 4) 
# See https://pagure.io/packaging-committee/issue/1044
ExclusiveArch: x86_64

Name:    nativejit
Version: 0.1
Release: 11%{?dist}
Summary: Library for high-performance just-in-time compilation
License: MIT
URL:     https://github.com/copasi/copasi-dependencies/tree/master/src/NativeJIT
Source0: https://gitlab.com/anto.trande/nativejit/-/archive/v%{version}/nativejit-v%{version}.tar.bz2

BuildRequires: cmake3, gcc, gcc-c++, make
BuildRequires: gtest-devel

Provides: NativeJIT = 0:%{version}-%{release}

%description
NativeJIT is an open-source cross-platform library for high-performance
just-in-time compilation of expressions involving C data structures.
The compiler is light weight and fast and it takes no dependencies
beyond the standard C++ runtime. It runs on Linux, OSX, and Windows.
The generated code is optimized with particular attention paid to
register allocation.
It requires CPUs with SSE4 (Streaming SIMD Extensions 4).

%package devel
Summary: NativeJIT headers and development-related files
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: cmake%{?_isa}
%description devel
NativeJIT headers and development-related files, CMake config files.

%prep
%autosetup -n %{name}-v%{version}

%build
%cmake \
 -DCMAKE_BUILD_TYPE:STRING=Release \
 -DCMAKE_CXX_FLAGS_RELEASE:STRING="%{build_cxxflags} -DNDEBUG" \
 -DCMAKE_C_FLAGS_RELEASE:STRING="%{build_cflags} -DNDEBUG" \
 -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES \
 -DNATIVEJIT_VERSION_MAJOR=0 -DNATIVEJIT_VERSION=0
%cmake_build

%install
%cmake_install

%check
if grep -E '\bsse4_2\b' /proc/cpuinfo >/dev/null
then
  %ctest -- -VV
else
  echo 'No SSE4.2 support on build host; skipping tests' 1>&2
fi


%files
%license LICENSE.txt
%doc README.md
%{_libdir}/libCodeGen.so.0
%{_libdir}/libNativeJIT.so.0

%files devel
%{_libdir}/libCodeGen.so
%{_libdir}/libNativeJIT.so
%{_includedir}/NativeJIT/
%{_includedir}/Temporary/
%{_libdir}/cmake/nativejit*.cmake

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jan 30 2022 Antonio Trande <sagitter@fedoraproject.org> - 0.1-4
- Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Mar 05 2021 Antonio Trande <sagitter@fedoraproject.org> - 0.1-1
- Fix links to CodeGen library

* Thu Mar 04 2021 Antonio Trande <sagitter@fedoraproject.org> - 0.0-2
- Conditional test when SSE4 in available
- Add explicit comments about SSE4

* Tue Mar 02 2021 Antonio Trande <sagitter@fedoraproject.org> - 0.0-1
- Initial package
