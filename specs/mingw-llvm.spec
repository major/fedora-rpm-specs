%{?mingw_package_header}

# Disable debuginfo subpackages and debugsource packages for now to use old logic
%undefine _debugsource_packages
%undefine _debuginfo_subpackages

# Override the __debug_install_post argument as this package
# contains both native as well as cross compiled binaries
%global __debug_install_post %%{mingw_debug_install_post}; %{_bindir}/find-debuginfo.sh %{?_missing_build_ids_terminate_build:--strict-build-id} %{?_find_debuginfo_opts} "%{_builddir}/%%{?buildsubdir}" %{nil}


%global pkgname llvm
%global libver 18

Name:          mingw-%{pkgname}
Version:       19.1.7
Release:       1%{?dist}
Summary:       LLVM for MinGW

License:       NCSA
URL:           http://llvm.org
Source0:       https://github.com/llvm/llvm-project/releases/download/llvmorg-%{version}/llvm-%{version}.src.tar.xz
Source1:       https://github.com/llvm/llvm-project/releases/download/llvmorg-%{version}/cmake-%{version}.src.tar.xz
# Set LLVM_INCLUDE_BENCHMARKS=OFF by default
Patch0:        llvm-no-benchmarks.patch
# Export less symbols
# Avoid ld: error: export ordinal too large
# See https://discourse.llvm.org/t/export-ordinal-too-large-when-linking-llvm-dll-with-mingw64/52293/2
Patch1:        llvm-shlib-syms.patch

BuildRequires: chrpath
BuildRequires: make
BuildRequires: cmake
BuildRequires: gcc-c++

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-libffi
BuildRequires: mingw32-zlib

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-libffi
BuildRequires: mingw64-zlib


%description
LLVM for MinGW.


%package -n mingw32-%{pkgname}
Summary:       LLVM for MinGW Windows

%description -n mingw32-%{pkgname}
LLVM for MinGW Windows.


%package -n mingw32-%{pkgname}-static
Summary:       LLVM for MinGW Windows - Static libraries
Requires:      mingw32-%{pkgname} = %{version}-%{release}
BuildArch:     noarch

%description -n mingw32-%{pkgname}-static
LLVM for MinGW Windows - Static libraries.

%package -n mingw32-%{pkgname}-tools
Summary:       LLVM for MinGW Windows - Runtime tools
Requires:      mingw32-%{pkgname} = %{version}-%{release}
BuildArch:     noarch

%description -n mingw32-%{pkgname}-tools
LLVM for MinGW Windows - Runtime tools.


%package -n mingw64-%{pkgname}
Summary:       LLVM for MinGW Windows

%description -n mingw64-%{pkgname}
LLVM for MinGW Windows.


%package -n mingw64-%{pkgname}-static
Summary:       LLVM for MinGW Windows - Static libraries
Requires:      mingw64-%{pkgname} = %{version}-%{release}
BuildArch:     noarch

%description -n mingw64-%{pkgname}-static
LLVM for MinGW Windows - Static libraries


%package -n mingw64-%{pkgname}-tools
Summary:       LLVM for MinGW Windows - Runtime tools
Requires:      mingw64-%{pkgname} = %{version}-%{release}
BuildArch:     noarch

%description -n mingw64-%{pkgname}-tools
LLVM for MinGW Windows - Runtime tools.


%{?mingw_debug_package}


%prep
# Setup cmake support files
%setup -T -q -b 1 -n cmake-%{version}.src
mv ../cmake-%{version}.src ../cmake
# Setup llvm itself
%autosetup -p1 -n %{pkgname}-%{version}.src


%build
# Decrease debuginfo verbosity to reduce memory consumption during final library linking
# Technically only necessary on %%{arm}, but effectively needed everywhere to avoid the build failing due to
#   The following noarch package built differently on different architectures: [...]
mingw32_cflags_="%(echo %mingw32_cflags | sed 's/-g /-g1 /')"
mingw64_cflags_="%(echo %mingw64_cflags | sed 's/-g /-g1 /')"
export MINGW32_CFLAGS="${mingw32_cflags_}"
export MINGW32_CXXFLAGS="${mingw32_cflags_}"
export MINGW64_CFLAGS="${mingw64_cflags_}"
export MINGW64_CXXFLAGS="${mingw64_cflags_}"

# Create toolchain for native build, see cmake/modules/CrossCompile.cmake
# (note that for the native build llvm_create_cross_target_internal is invoked with toolchain = "", hence
# the toolchain file is just .cmake)
cat > cmake/platforms/.cmake <<EOF
SET(CMAKE_SYSTEM_NAME Linux)
SET(CMAKE_CROSSCOMPILING FALSE)

SET(CMAKE_C_COMPILER gcc)
SET(CMAKE_CXX_COMPILER g++)

SET(CMAKE_C_FLAGS "%{optflags}")
SET(CMAKE_CXX_FLAGS "%{optflags}")
SET(CMAKE_EXE_LINKER_FLAGS "%{__global_ldflags}")
EOF

# Build native llvm-tblgen, rather than depending on version-matching native package
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_SKIP_RPATH=ON -DBUILD_SHARED_LIBS=OFF -DLLVM_INCLUDE_TESTS=OFF
%cmake_build --target llvm-tblgen

CMAKE_OPTS="
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_SKIP_RPATH=ON \
    -DBUILD_SHARED_LIBS=OFF \
    -DLLVM_TARGETS_TO_BUILD="X86" \
    -DLLVM_TARGET_ARCH="X86" \
    -DLLVM_INFERRED_HOST_TRIPLE=%{_target} \
    -DLLVM_TABLEGEN=$PWD/%{_vpath_builddir}/bin/llvm-tblgen \
    -DLLVM_ENABLE_LIBCXX=OFF \
    -DLLVM_ENABLE_ZLIB=ON \
    -DLLVM_ENABLE_FFI=ON \
    -DLLVM_ENABLE_RTTI=ON \
    -DLLVM_BUILD_RUNTIME=ON \
    -DLLVM_BUILD_LLVM_DYLIB=ON \
    -DLLVM_LINK_LLVM_DYLIB=ON \
    -DLLVM_BUILD_EXTERNAL_COMPILER_RT=ON \
    -DLLVM_INCLUDE_TESTS=OFF \
    -DLLVM_INCLUDE_DOCS=OFF \
    -DLLVM_INCLUDE_TOOLS=ON \
    -DLLVM_INCLUDE_EXAMPLES=OFF \
    -DLLVM_ENABLE_ASSERTIONS=OFF \
    -DLLVM_INSTALL_TOOLCHAIN_ONLY:BOOL=OFF \
"
mkdir build_win32
pushd build_win32
%mingw32_cmake \
    $CMAKE_OPTS \
    -DLLVM_DEFAULT_TARGET_TRIPLE=%{mingw32_target} \
    -DFFI_INCLUDE_DIR=%{mingw32_libdir}/libffi-%{ffi_ver}/include \
    -DCMAKE_C_FLAGS_RELWITHDEBINFO="${mingw32_cflags_} -DNDEBUG" \
    -DCMAKE_CXX_FLAGS_RELWITHDEBINFO="${mingw32_cflags_} -DNDEBUG"

popd

mkdir build_win64
pushd build_win64
%mingw64_cmake \
    $CMAKE_OPTS \
    -DLLVM_DEFAULT_TARGET_TRIPLE=%{mingw64_target} \
    -DFFI_INCLUDE_DIR=%{mingw64_libdir}/libffi-%{ffi_ver}/include \
    -DCMAKE_C_FLAGS_RELWITHDEBINFO="${mingw64_cflags_} -DNDEBUG" \
    -DCMAKE_CXX_FLAGS_RELWITHDEBINFO="${mingw64_cflags_} -DNDEBUG"
popd

%mingw_make_build


%install
%mingw_make_install

# Install host llmv-config
install -Dpm 0755 build_win32/NATIVE/bin/llvm-config %{buildroot}%{_prefix}/%{mingw32_target}/bin/llvm-config
install -Dpm 0755 build_win64/NATIVE/bin/llvm-config %{buildroot}%{_prefix}/%{mingw64_target}/bin/llvm-config

# Unversioned symlink
ln -s %{mingw32_libdir}/libLLVM-%{libver}.dll.a %{buildroot}%{mingw32_libdir}/libLLVM.dll.a
ln -s %{mingw64_libdir}/libLLVM-%{libver}.dll.a %{buildroot}%{mingw64_libdir}/libLLVM.dll.a

# Remove unused files
rm -rf %{buildroot}%{mingw32_datadir}/opt-viewer
rm -rf %{buildroot}%{mingw64_datadir}/opt-viewer

# Install llvm-tblgen to host tools dir, can be used to cross-compile mingw-clang
install -Dpm 0755 %{_vpath_builddir}/bin/llvm-tblgen %{buildroot}%{_prefix}/%{mingw32_target}/bin/llvm-tblgen
install -Dpm 0755 %{_vpath_builddir}/bin/llvm-tblgen %{buildroot}%{_prefix}/%{mingw64_target}/bin/llvm-tblgen

# Kill rpaths
chrpath --delete %{buildroot}%{_prefix}/%{mingw32_target}/bin/llvm-config
chrpath --delete %{buildroot}%{_prefix}/%{mingw64_target}/bin/llvm-config
chrpath --delete %{buildroot}%{_prefix}/%{mingw32_target}/bin/llvm-tblgen
chrpath --delete %{buildroot}%{_prefix}/%{mingw64_target}/bin/llvm-tblgen


%files -n mingw32-%{pkgname}
%license LICENSE.TXT
%{mingw32_bindir}/llvm-tblgen.exe
%{mingw32_bindir}/libLLVM-%{libver}.dll
%{mingw32_bindir}/libLTO.dll
%{mingw32_bindir}/libRemarks.dll
%{mingw32_includedir}/llvm/
%{mingw32_includedir}/llvm-c/
%{mingw32_libdir}/cmake/llvm/
%{mingw32_libdir}/libLLVM-%{libver}.dll.a
%{mingw32_libdir}/libLLVM.dll.a
%{mingw32_libdir}/libLTO.dll.a
%{mingw32_libdir}/libRemarks.dll.a
%{_prefix}/%{mingw32_target}/bin/llvm-config
%{_prefix}/%{mingw32_target}/bin/llvm-tblgen

%files -n mingw32-%{pkgname}-static
%{mingw32_libdir}/libLLVM*.a
%exclude %{mingw32_libdir}/libLLVM*.dll.a

%files -n mingw32-%{pkgname}-tools
%exclude %{mingw32_bindir}/llvm-tblgen.exe
%{mingw32_bindir}/*.exe

%files -n mingw64-%{pkgname}
%license LICENSE.TXT
%{mingw64_bindir}/llvm-tblgen.exe
%{mingw64_bindir}/libLLVM-%{libver}.dll
%{mingw64_bindir}/libLTO.dll
%{mingw64_bindir}/libRemarks.dll
%{mingw64_includedir}/llvm/
%{mingw64_includedir}/llvm-c/
%{mingw64_libdir}/cmake/llvm/
%{mingw64_libdir}/libLLVM.dll.a
%{mingw64_libdir}/libLLVM-%{libver}.dll.a
%{mingw64_libdir}/libLTO.dll.a
%{mingw64_libdir}/libRemarks.dll.a
%{_prefix}/%{mingw64_target}/bin/llvm-config
%{_prefix}/%{mingw64_target}/bin/llvm-tblgen

%files -n mingw64-%{pkgname}-static
%{mingw64_libdir}/libLLVM*.a
%exclude %{mingw64_libdir}/libLLVM*.dll.a

%files -n mingw64-%{pkgname}-tools
%exclude %{mingw64_bindir}/llvm-tblgen.exe
%{mingw64_bindir}/*.exe


%changelog
* Sat Jan 25 2025 Sandro Mani <manisandro@gmail.com> - 19.1.7-1
- Update to 19.1.7

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 19.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Nov 19 2024 Sandro Mani <manisandro@gmail.com> - 19.1.4-1
- Update to 19.1.4

* Sun Sep 29 2024 Sandro Mani <manisandro@gmail.com> - 19.1.0-1
- Update to 19.1.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 18.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 25 2024 Sandro Mani <manisandro@gmail.com> - 18.1.8-1
- Update to 18.1.8

* Wed May 22 2024 Sandro Mani <manisandro@gmail.com> - 18.1.6-1
- Update to 18.1.6

* Sun Apr 21 2024 Sandro Mani <manisandro@gmail.com> - 18.1.4-1
- Update to 18.1.4

* Wed Mar 27 2024 Sandro Mani <manisandro@gmail.com> - 18.1.2-1
- Update to 18.1.2

* Thu Mar 14 2024 Sandro Mani <manisandro@gmail.com> - 18.1.1-1
- Update to 18.1.1

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 17.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 17.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Dec 03 2023 Sandro Mani <manisandro@gmail.com> - 17.0.6-1
- Update to 17.0.6

* Tue Nov 07 2023 Sandro Mani <manisandro@gmail.com> - 17.0.4-1
- Update to 17.0.4

* Thu Oct 19 2023 Sandro Mani <manisandro@gmail.com> - 17.0.3-1
- Update to 17.0.3

* Sat Oct 07 2023 Sandro Mani <manisandro@gmail.com> - 17.0.2-1
- Update to 17.0.2

* Tue Sep 26 2023 Sandro Mani <manisandro@gmail.com> - 17.0.1-1
- Update to 17.0.1

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 16.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Sandro Mani <manisandro@gmail.com> - 16.0.6-1
- Update to 16.0.6

* Tue May 23 2023 Sandro Mani <manisandro@gmail.com> - 16.0.4-1
- Update to 16.0.4

* Fri May 12 2023 Sandro Mani <manisandro@gmail.com> - 16.0.3-1
- Update to 16.0.3

* Sun Apr 30 2023 Sandro Mani <manisandro@gmail.com> - 16.0.2-1
- Update to 16.0.2

* Sat Apr 15 2023 Sandro Mani <manisandro@gmail.com> - 16.0.1-1
- Update to 16.0.1

* Thu Apr 06 2023 Sandro Mani <manisandro@gmail.com> - 16.0.0-1
- Update to 16.0.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 15.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Jan 15 2023 Sandro Mani <manisandro@gmail.com> - 15.0.7-1
- Update to 15.0.7

* Wed Dec 07 2022 Sandro Mani <manisandro@gmail.com> - 15.0.6-1
- Update to 15.0.6

* Tue Nov 08 2022 Sandro Mani <manisandro@gmail.com> - 15.0.4-1
- Update to 15.0.4

* Thu Sep 15 2022 Sandro Mani <manisandro@gmail.com> - 15.0.0-1
- Update to 15.0.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 14.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jul 03 2022 Sandro Mani <manisandro@gmail.com> - 14.0.6-1
- Update to 14.0.6

* Tue Mar 29 2022 Sandro Mani <manisandro@gmail.com> - 14.0.0-1
- Update to 14.0.0

* Tue Mar 29 2022 Sandro Mani <manisandro@gmail.com> - 13.0.1-3
- Statically link native llvm-tblgen linklibs

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 13.0.1-2
- Rebuild with mingw-gcc-12

* Mon Feb 14 2022 Sandro Mani <manisandro@gmail.com> - 13.0.1-1
- Update to 13.0.1

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 13.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan 14 2022 Sandro Mani <manisandro@gmail.com> - 13.0.0-3
- Build native llvm-tblgen rather than depending on native packge

* Fri Jan 14 2022 Sandro Mani <manisandro@gmail.com> - 13.0.0-2
- Fix *.dll.a included in -static

* Tue Oct 19 2021 Sandro Mani <manisandro@gmail.com> - 13.0.0-1
- Update to 13.0.0

* Fri Jul 30 2021 Sandro Mani <manisandro@gmail.com> - 12.0.1-3
- Rebuild (libffi)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 12.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 16 2021 Sandro Mani <manisandro@gmail.com> - 12.0.1-1
- Update to 12.0.1

* Fri Apr 16 2021 Sandro Mani <manisandro@gmail.com> - 12.0.0-1
- Update to 12.0.0

* Tue Mar 30 2021 Jonathan Wakely <jwakely@redhat.com> - 11.1.0-2
- Rebuilt for removed libstdc++ symbol (#1937698)

* Mon Feb 22 2021 Sandro Mani <manisandro@gmail.com> - 11.1.0-1
- Update to 11.1.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 06 2021 Sandro Mani <manisandro@gmail.com> - 11.0.1-1
- Update to 11.0.1

* Wed Oct 14 2020 Sandro Mani <manisandro@gmail.com> - 11.0.0-1
- Update to 11.0.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Mar 25 2020 Sandro Mani <manisandro@gmail.com> - 10.0.0-1
- Update to 10.0.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 20 2019 Sandro Mani <manisandro@gmail.com> - 9.0.1-1
- Update to 9.0.1

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 9.0.0-2
- Rebuild (Changes/Mingw32GccDwarf2)

* Mon Sep 23 2019 Sandro Mani <manisandro@gmail.com> - 9.0.0-1
- Update to 9.0.0

* Tue Aug 06 2019 Sandro Mani <manisandro@gmail.com> - 8.0.1-1
- Update to 8.0.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 23 2019 Sandro Mani <manisandro@gmail.com> - 8.0.0-1
- Update to 8.0.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 25 2018 Sandro Mani <manisandro@gmail.com> - 7.0.1-1
- Update to 7.0.1

* Tue Sep 25 2018 Sandro Mani <manisandro@gmail.com> - 7.0.0-1
- Update to 7.0.0

* Wed Aug 08 2018 Sandro Mani <manisandro@gmail.com> - 6.0.1-1
- Rework spec
- Update to 6.0.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jul 23 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 3.0-9
- Do not strip during make install (#1106207)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jul 01 2012 Eric Smith <eric@brouhaha.com> - 3.0-4
- Add patch from upstream to fix call to strerror_s() with too few args.

* Thu May 10 2012 Eric Smith <eric@brouhaha.com> - 3.0-3
- Add patch to force llvm-config to always use PREFIX, rather than
  trying to figure out whether it has been installed.

* Mon May 07 2012 Eric Smith <eric@brouhaha.com> - 3.0-2
- Add OPTIMIZE_OPTION and KEEP_SYMBOLS to make command line to prevent
  symbols from being stripped, in order to get usable debuginfo package.

* Sun May 06 2012 Eric Smith <eric@brouhaha.com> - 3.0-1
- Initial version

