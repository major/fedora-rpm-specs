%global appname include-what-you-use
%global toolchain clang

%if 0%{?fedora} && 0%{?fedora} >= 43
%global llvm_legacy 1
%else
%global llvm_legacy 0
%endif
%global llvm_ver 20

# Opt out of https://fedoraproject.org/wiki/Changes/fno-omit-frame-pointer
# https://bugzilla.redhat.com/show_bug.cgi?id=2215937
# https://github.com/include-what-you-use/include-what-you-use/issues/1264
%undefine _include_frame_pointers

Name: iwyu
Version: 0.24
Release: %autorelease

License: NCSA
Summary: C/C++ source files #include analyzer based on clang
URL: https://github.com/%{appname}/%{appname}
Source0: %{url}/archive/%{version}/%{appname}-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
%if 0%{?fedora} && 0%{?fedora} >= 42
ExcludeArch: %{ix86}
%endif

%if %{llvm_legacy}
BuildRequires: clang%{llvm_ver}
BuildRequires: clang%{llvm_ver}-devel
BuildRequires: compiler-rt%{llvm_ver}
BuildRequires: llvm%{llvm_ver}-devel
BuildRequires: llvm%{llvm_ver}-static
%else
BuildRequires: clang >= %{llvm_ver}
BuildRequires: clang-devel >= %{llvm_ver}
BuildRequires: compiler-rt >= %{llvm_ver}
BuildRequires: llvm-devel >= %{llvm_ver}
BuildRequires: llvm-static >= %{llvm_ver}
%endif

BuildRequires: libcxx-devel
BuildRequires: ncurses-devel
BuildRequires: python3-devel
BuildRequires: zlib-devel

BuildRequires: cmake
BuildRequires: ninja-build

Provides: %{appname} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: %{appname}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description
"Include what you use" means this: for every symbol (type, function, variable,
or macro) that you use in foo.cc (or foo.cpp), either foo.cc or foo.h should
include a .h file that exports the declaration of that symbol. (Similarly, for
foo_test.cc, either foo_test.cc or foo.h should do the including.) Obviously
symbols defined in foo.cc itself are excluded from this requirement.

This puts us in a state where every file includes the headers it needs to
declare the symbols that it uses. When every file includes what it uses,
then it is possible to edit any file and remove unused headers, without fear
of accidentally breaking the upwards dependencies of that file. It also
becomes easy to automatically track and update dependencies in the source
code.

%prep
%autosetup -n %{appname}-%{version} -p1
%py3_shebang_fix *.py

%build
%if %{llvm_legacy}
export CC="clang-%{llvm_ver}"
export CXX="clang++-%{llvm_ver}"
%endif
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
%if %{llvm_legacy}
    -DCMAKE_PREFIX_PATH='%{_libdir}/llvm%{llvm_ver}/%{_lib}/cmake/clang;%{_libdir}/llvm%{llvm_ver}/%{_lib}/cmake/llvm' \
%endif
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON
%cmake_build

%install
%cmake_install

%check
%ctest --exclude-regex "(cxx.test_(badinc|ms_inline_asm|precomputed_tpl_args)|driver.test_offload_openmp)"

%files
%doc docs/* README.md
%license LICENSE.TXT
%{_bindir}/%{appname}
%{_bindir}/fix_includes.py
%{_bindir}/iwyu_tool.py
%{_datadir}/%{appname}/
%{_mandir}/man1/%{appname}.1*

%changelog
%autochangelog
