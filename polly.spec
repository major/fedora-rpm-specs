%global toolchain clang
#global rc_ver 3
%global polly_version 15.0.0
%global polly_srcdir polly-%{polly_version}%{?rc_ver:rc%{rc_ver}}.src

Name: polly
Version: %{polly_version}%{?rc_ver:~rc%{rc_ver}}
Release: 3%{?dist}
Summary: LLVM Framework for High-Level Loop and Data-Locality Optimizations

License: NCSA
URL: http://polly.llvm.org
Source0: https://github.com/llvm/llvm-project/releases/download/llvmorg-%{polly_version}%{?rc_ver:-rc%{rc_ver}}/%{polly_srcdir}.tar.xz
Source1: https://github.com/llvm/llvm-project/releases/download/llvmorg-%{polly_version}%{?rc_ver:-rc%{rc_ver}}/%{polly_srcdir}.tar.xz.sig
Source2: release-keys.asc

Patch0: 0001-PATCH-polly-Portability-of-subproject-extension.patch

BuildRequires: cmake
BuildRequires: llvm-devel = %{version}
BuildRequires: llvm-test = %{version}
BuildRequires: clang-devel = %{version}
BuildRequires: ninja-build
BuildRequires: python3-lit
BuildRequires: python3-sphinx

# For origin certification
BuildRequires:	gnupg2

%description
Polly is a high-level loop and data-locality optimizer and optimization
infrastructure for LLVM. It uses an abstract mathematical representation based
on integer polyhedron to analyze and optimize the memory access pattern of a
program.

%package devel
Summary: Polly header files
Requires: %{name} = %{version}-%{release}

%description devel
Polly header files.

%package doc
Summary: Documentation for Polly
BuildArch: noarch
Requires: %{name} = %{version}-%{release}

%description doc
Documentation for the Polly optimizer.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{polly_srcdir} -p2

%build

%cmake 	-GNinja \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DCMAKE_SKIP_RPATH:BOOL=ON \
	-DLLVM_LINK_LLVM_DYLIB:BOOL=ON \
	-DLLVM_EXTERNAL_LIT=%{_bindir}/lit \
	-DCMAKE_PREFIX_PATH=%{_libdir}/cmake/llvm/ \
\
	-DLLVM_ENABLE_SPHINX:BOOL=ON \
	-DSPHINX_WARNINGS_AS_ERRORS=OFF \
	-DSPHINX_EXECUTABLE=%{_bindir}/sphinx-build-3 \
\
%if 0%{?__isa_bits} == 64
	-DLLVM_LIBDIR_SUFFIX=64
%else
	-DLLVM_LIBDIR_SUFFIX=
%endif

%cmake_build
%cmake_build --target docs-polly-html


%install
%cmake_install

install -d %{buildroot}%{_pkgdocdir}/html
cp -r %{_vpath_builddir}/docs/html/* %{buildroot}%{_pkgdocdir}/html/

%check
# Test execution normally relies on RPATH, so set LD_LIBRARY_PATH instead.
export LD_LIBRARY_PATH=%{buildroot}/%{_libdir}
%cmake_build --target check-polly

%files
%license LICENSE.TXT
%{_libdir}/LLVMPolly.so
%{_libdir}/libPolly.so.*
%{_libdir}/libPollyISL.so

%files devel
%{_libdir}/libPolly.so
%{_includedir}/polly
%{_libdir}/cmake/polly

%files doc
%doc %{_pkgdocdir}/html

%changelog
* Tue Sep 13 2022 Nikita Popov <npopov@redhat.com> - 15.0.0-3
- Set CMAKE_SKIP_RPATH

* Thu Sep 08 2022 Nikita Popov <npopov@redhat.com> - 15.0.0-2
- Re-enable LTO

* Tue Sep 06 2022 Nikita Popov <npopov@redhat.com> - 15.0.0-1
- Update to LLVM 15.0.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 14.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 22 2022 Timm Bäder <tbaeder@redhat.com> - 14.0.5-1
- Update to 14.0.5

* Wed Mar 30 2022 Timm Bäder <tbaeder@redhat.com> - 14.0.0-1
- Update to 14.0.0

* Thu Feb 03 2022 Nikita Popov <npopov@redhat.com> - 13.0.1-1
- Update to LLVM 13.0.1 final

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 13.0.1~rc2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan 14 2022 Nikita Popov <npopov@redhat.com> - 13.0.1~rc2-1
- Update to LLVM 13.0.1rc2

* Wed Jan 12 2022 Nikita Popov <npopov@redhat.com> - 13.0.1~rc1-1
- Update to LLVM 13.0.1rc1

* Fri Oct 01 2021 Tom Stellard <tstellar@redhat.com> - 13.0.0-1
- 13.0.0 Release

* Wed Sep 22 2021 Tom Stellard <tstellar@redhat.com> - 13.0.0~rc3-1
- 13.0.0-rc3 Release

* Mon Aug 09 2021 Tom Stellard <tstellar@redhat.com> - 13.0.0~rc1-1
- 13.0.0-rc1 Release

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 12.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 13 2021 Tom Stellard <tstellar@redhat.com> - 12.0.1-1
- 12.0.1 Release

* Thu Jul 01 2021 Tom Stellard <tstellar@redhat.com> - 12.0.0~rc3-1
- 12.0.1-rc3 Release

* Thu Jun 03 2021 Tom Stellard <tstellar@redhat.com> - 12.0.0~rc1-1
- 12.0.1-rc1 Release

* Fri Apr 16 2021 Tom Stellard <tstellar@redhat.com> - 12.0.0-1
- 12.0.0 Release

* Thu Apr 08 2021 sguelton@redhat.com - 12.0.0-0.7.rc5
- New upstream release candidate

* Fri Apr 02 2021 sguelton@redhat.com - 12.0.0-0.6.rc4
- New upstream release candidate

* Wed Mar 31 2021 Jonathan Wakely <jwakely@redhat.com> - 12.0.0-0.5.rc3
- Rebuilt for removed libstdc++ symbols (#1937698)

* Thu Mar 11 2021 sguelton@redhat.com - 12.0.0-0.4.rc3
- LLVM 12.0.0 rc3

* Wed Mar 10 2021 sguelton@redhat.com - 12.0.0-0.3.rc2
- rebuilt

* Thu Feb 25 2021 sguelton@redhat.com - 12.0.0-0.2.rc2
- 12.0.0-rc2 release

* Thu Feb 18 2021 sguelton@redhat.com - 12.0.0-0.1.rc1
- 12.0.0-rc1 release

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 11.1.0-0.2.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 2021 Serge Guelton - 11.1.0-0.1.rc1
- 11.1.0-rc1 release

* Wed Jan 06 2021 Serge Guelton - 11.0.1-3
- LLVM 11.0.1 final

* Tue Dec 22 2020 sguelton@redhat.com - 11.0.1-2.rc2
- llvm 11.0.1-rc2

* Tue Dec 01 2020 sguelton@redhat.com - 11.0.1-1.rc1
- llvm 11.0.1-rc1

* Thu Oct 15 2020 sguelton@redhat.com - 11.0.0-1
- Fix NVR

* Mon Oct 12 2020 sguelton@redhat.com - 11.0.0-0.5
- llvm 11.0.0 - final release

* Thu Oct 08 2020 sguelton@redhat.com - 11.0.0-0.4.rc6
- 11.0.0-rc6

* Fri Oct 02 2020 sguelton@redhat.com - 11.0.0-0.3.rc5
- 11.0.0-rc5 Release

* Sun Sep 27 2020 sguelton@redhat.com - 11.0.0-0.2.rc3
- Fix NVR

* Thu Sep 24 2020 sguelton@redhat.com - 11.0.0-0.1.rc3
- 11.0.0-rc3 Release

* Tue Sep 01 2020 sguelton@redhat.com - 11.0.0-0.1.rc2
- 11.0.0-rc2 Release

* Tue Aug 11 2020 Tom Stellard <tstellar@redhat.com> - 11.0.0-0.1.rc1
- 11.0.0-rc1 Release

* Tue Aug 11 2020 Tom Stellard <tstellar@redhat.com> - 10.0.0-6
- Disable LTO builds

* Mon Aug 10 2020 sguelton@redhat.com - 10.0.0-5
- Make gcc dependency explicit, see https://fedoraproject.org/wiki/Packaging:C_and_C%2B%2B#BuildRequires_and_Requires
- use %%license macro

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.0.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 sguelton@redhat.com - 10.0.0-2
- Modernize cmake macro usage

* Mon Mar 30 2020 sguelton@redhat.com - 10.0.0-1
- llvm-10.0.0 final

* Wed Mar 25 2020 sguelton@redhat.com - 10.0.0-0.2.rc6
- llvm-10.0.0 rc6

* Sat Mar 21 2020 sguelton@redhat.com - 10.0.0-0.1.rc5
- Initial version.

