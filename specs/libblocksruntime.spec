%global debug_package %{nil}
%global shlibver 1


Name:       libblocksruntime
Version:    7.0.0
Release:    14%{?dist}
Summary:    LLVM's compiler-rt/BlocksRuntime development files 
License:    NCSA and MIT
URL:        http://compiler-rt.llvm.org
Source0:    http://releases.llvm.org/7.0.0/compiler-rt-7.0.0.src.tar.xz
Source1:    buildlib
Source2:    config.h

BuildRequires: gcc


%description
This package contains development headers for building 
software that uses blocks, a proposed extension to the 
C, Objective C, and C++ languages developed by Apple 
to support the Grand Central Dispatch concurrency engine.


%package devel
Summary:    Development files for blocks
Requires:   %{name} = %{version}-%{release}


%description devel
Development files for compiling and statically linking
blocks in a program that uses the Apple blocks
proposed extension.


%package static
Summary:    Static development file for libblocksruntime
Requires:   %{name}-devel = %{version}-%{release}


%description static
This package contains the static library to develop
applications that use libblocksruntime


%prep
%setup -n compiler-rt-%{version}.src
cp -p %SOURCE1 lib
cp -p %SOURCE2 lib


%build
cd lib
./buildlib -shared %{shlibver}


%install
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}
install -m 644 lib/BlocksRuntime/Block.h %{buildroot}%{_includedir}
install -m 644 lib/libBlocksRuntime.a %{buildroot}%{_libdir}
install -m 755 lib/libBlocksRuntime.so.0.%{shlibver} %{buildroot}/%{_libdir}
ln -fs libBlocksRuntime.so.0.%{shlibver} %{buildroot}%{_libdir}/libBlocksRuntime.so.0
ln -fs libBlocksRuntime.so.0 %{buildroot}%{_libdir}/libBlocksRuntime.so


%files
%license LICENSE.TXT
%{_libdir}/*.so.*


%files devel
%{_includedir}/Block.h
%{_libdir}/*.so


%files static
%{_libdir}/*.a

%ldconfig_scriptlets


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 10 2019 Ron Olson <tachoknight@gmail.com> 7.0.0-2
- Updated to Clang 7.0.0
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild
* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild
* Fri Jul 05 2018 Ron Olson <tachoknight@gmail.com> 5.0.2-1
- Updated to compiler-rt-5.0.2
* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild
* Sun Jan 14 2018 Ron Olson <tachoknight@gmail.com> 5.0.1-1
- Initial package for Fedora
