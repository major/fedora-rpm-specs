%global toolchain clang

# Opt out of https://fedoraproject.org/wiki/Changes/fno-omit-frame-pointer
# https://bugzilla.redhat.com/show_bug.cgi?id=2158587
%undefine _include_frame_pointers

%global lldb_version 16.0.6
#global rc_ver 4
%global lldb_srcdir %{name}-%{lldb_version}%{?rc_ver:rc%{rc_ver}}.src

Name:		lldb
Version:	%{lldb_version}%{?rc_ver:~rc%{rc_ver}}
Release:	2%{?dist}
Summary:	Next generation high-performance debugger

License:	Apache-2.0 WITH LLVM-exception OR NCSA
URL:		http://lldb.llvm.org/
Source0:	https://github.com/llvm/llvm-project/releases/download/llvmorg-%{lldb_version}%{?rc_ver:-rc%{rc_ver}}/%{lldb_srcdir}.tar.xz
Source1:	https://github.com/llvm/llvm-project/releases/download/llvmorg-%{lldb_version}%{?rc_ver:-rc%{rc_ver}}/%{lldb_srcdir}.tar.xz.sig
Source2:	release-keys.asc

BuildRequires:	clang
BuildRequires:	cmake
BuildRequires:	ninja-build
BuildRequires:	llvm-devel = %{version}
BuildRequires:	llvm-test = %{version}
BuildRequires:	llvm-cmake-utils = %{version}
BuildRequires:	clang-devel = %{version}
BuildRequires:	ncurses-devel
BuildRequires:	swig
BuildRequires:	llvm-static = %{version}
BuildRequires:	libffi-devel
BuildRequires:	zlib-devel
BuildRequires:	libxml2-devel
BuildRequires:	libedit-devel
BuildRequires:	python3-lit
BuildRequires:	multilib-rpm-config
BuildRequires:	doxygen

Requires:	python3-lldb

# For origin certification
BuildRequires:	gnupg2

%description
LLDB is a next generation, high-performance debugger. It is built as a set
of reusable components which highly leverage existing libraries in the
larger LLVM Project, such as the Clang expression parser and LLVM
disassembler.

%package devel
Summary:	Development header files for LLDB
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
The package contains header files for the LLDB debugger.

%package -n python3-lldb
%{?python_provide:%python_provide python3-lldb}
Summary:	Python module for LLDB
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
Requires:	python3-six
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description -n python3-lldb
The package contains the LLDB Python module.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{lldb_srcdir} -p2

%build
%global _lto_cflags -flto=thin

%cmake  -GNinja \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DCMAKE_SKIP_RPATH:BOOL=ON \
	-DLLVM_LINK_LLVM_DYLIB:BOOL=ON \
	-DLLVM_CONFIG:FILEPATH=/usr/bin/llvm-config-%{__isa_bits} \
	-DLLVM_COMMON_CMAKE_UTILS=%{_datadir}/llvm/cmake \
	-DLLDB_DISABLE_CURSES:BOOL=OFF \
	-DLLDB_DISABLE_LIBEDIT:BOOL=OFF \
	-DLLDB_DISABLE_PYTHON:BOOL=OFF \
%if 0%{?__isa_bits} == 64
	-DLLVM_LIBDIR_SUFFIX=64 \
%else
	-DLLVM_LIBDIR_SUFFIX= \
%endif
	\
	-DPYTHON_EXECUTABLE:STRING=%{__python3} \
	-DPYTHON_VERSION_MAJOR:STRING=$(%{__python3} -c "import sys; print(sys.version_info.major)") \
	-DPYTHON_VERSION_MINOR:STRING=$(%{__python3} -c "import sys; print(sys.version_info.minor)") \
	-DLLVM_EXTERNAL_LIT=%{_bindir}/lit \
	-DCLANG_LINK_CLANG_DYLIB=ON \
	-DLLVM_LIT_ARGS="-sv \
	--path %{_libdir}/llvm" \

%cmake_build

%install
%cmake_install

%multilib_fix_c_header --file %{_includedir}/lldb/Host/Config.h

# remove static libraries
rm -fv %{buildroot}%{_libdir}/*.a

# python: fix binary libraries location
liblldb=$(basename $(readlink -e %{buildroot}%{_libdir}/liblldb.so))
ln -vsf "../../../${liblldb}" %{buildroot}%{python3_sitearch}/lldb/_lldb.so
%py_byte_compile %{__python3} %{buildroot}%{python3_sitearch}/lldb

# remove bundled six.py
rm -f %{buildroot}%{python3_sitearch}/six.*

%ldconfig_scriptlets

%check


%files
%license LICENSE.TXT
%{_bindir}/lldb*
%{_libdir}/liblldb.so.*
%{_libdir}/liblldbIntelFeatures.so.*

%files devel
%{_includedir}/lldb
%{_libdir}/*.so

%files -n python3-lldb
%{python3_sitearch}/lldb

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 16.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 10 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.6-1
- Update to LLVM 16.0.6

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 16.0.5-4
- Rebuilt for Python 3.12

* Thu Jun 15 2023 Nikita Popov <npopov@redhat.com> - 16.0.5-3
- Use llvm-cmake-utils package

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 16.0.5-2
- Rebuilt for Python 3.12

* Tue Jun 06 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.5-1
- Update to LLVM 16.0.5

* Fri May 19 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.4-1
- Update to LLVM 16.0.4

* Wed May 10 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.3-1
- Update to LLVM 16.0.3

* Wed Apr 26 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.2-1
- Update to LLVM 16.0.2

* Thu Apr 13 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.1-1
- Update to LLVM 16.0.1

* Tue Mar 21 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.0-1
- Update to LLVM 16.0.0

* Wed Mar 15 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.0~rc4-1
- Update to LLVM 16.0.0 RC4

* Thu Feb 23 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.0~rc3-1
- Update to LLVM 16.0.0 RC3

* Tue Feb 14 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.0~rc1-1
- Update to LLVM 16.0.0 RC1

* Thu Jan 19 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 15.0.7-3
- Include the Apache license adopted in 2019.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 15.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 13 2023 Nikita Popov <npopov@redhat.com> - 15.0.7-1
- Update to LLVM 15.0.7

* Thu Jan 12 2023 Tom Stellard <tstellar@redhat.com> - 15.0.6-2
- Omit frame pointers when building

* Tue Dec 06 2022 Nikita Popov <npopov@redhat.com> - 15.0.6-1
- Update to LLVM 15.0.6

* Mon Nov 07 2022 Nikita Popov <npopov@redhat.com> - 15.0.4-1
- Update to LLVM 15.0.4

* Tue Oct 18 2022 Nikita Popov <npopov@redhat.com> - 15.0.0-3
- Fix crash on ppc64le (fix rhbz#2121369)

* Mon Oct 03 2022 sguelton@redhat.com - 15.0.0-2
- Backport compat patches for swig 4.1.0, see rhbz#2128646

* Tue Sep 06 2022 Nikita Popov <npopov@redhat.com> - 15.0.0-1
- Update to LLVM 15.0.0

* Tue Aug 09 2022 Nikita Popov <npopov@redhat.com> - 14.0.5-3
- Fix s390x build

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 14.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 20 2022 Timm Bäder <tbaeder@redhat.com> - 14.0.5-1
- Update to 14.0.5

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 14.0.0-2
- Rebuilt for Python 3.11

* Wed Mar 23 2022 Timm Bäder <tbaeder@redhat.com> - 14.0.0-1
- Update to 14.0.0

* Thu Feb 03 2022 Nikita Popov <npopov@redhat.com> - 13.0.1-1
- Update to LLVM 13.0.1 final

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 13.0.1~rc2-2
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

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 12.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jul 14 2021 Tom Stellard <tstellar@redhat.com> - 12.0.1-1
- 12.0.1 Release

* Thu Jul 01 2021 Tom Stellard <tstellar@redhat.com> - 12.0.0~rc3-1
- 12.0.0-rc3 Release

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 12.0.1~rc1-2
- Rebuilt for Python 3.10

* Thu Jun 03 2021 Tom Stellard <tstellar@redhat.com> - 12.0.0~rc1-1
- 12.0.0-rc1 Release

* Fri Apr 16 2021 Tom Stellard <tstellar@redhat.com> - 12.0.0-1
- 12.0.0 Release

* Thu Apr 08 2021 sguelton@redhat.com - 12.0.0-11.rc5
- New upstream release candidate

* Fri Apr 02 2021 sguelton@redhat.com - 12.0.0-10.rc4
- New upstream release candidate

* Wed Mar 31 2021 Jonathan Wakely <jwakely@redhat.com> - 12.0.0-9.rc3
- Rebuilt for removed libstdc++ symbols (#1937698)

* Thu Mar 11 2021 sguelton@redhat.com - 12.0.0-8.rc3
- LLVM 12.0.0 rc3

* Thu Mar 11 2021 sguelton@redhat.com - 12.0.0-7.rc2
- rebuilt

* Tue Mar 02 2021 sguelton@redhat.com - 12.0.0-6.rc2
- Update test regexp

* Tue Mar 02 2021 sguelton@redhat.com - 12.0.0-5.rc2
- Improve CI debugging

* Tue Mar 02 2021 sguelton@redhat.com - 12.0.0-4.rc2
- Apply upstream D97721

* Mon Mar 01 2021 sguelton@redhat.com - 12.0.0-3.rc2
- Update CI test

* Thu Feb 25 2021 sguelton@redhat.com - 12.0.0-0.2.rc2
- 12.0.0-rc2 release

* Wed Feb 17 2021 sguelton@redhat.com - 12.0.0-0.1.rc1
- 12.0.0-rc1 release

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 11.1.0-3.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Serge Guelton - 11.1.0-2.rc2
- llvm 11.1.0-rc2 release

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

* Mon Aug 10 2020 Tom Stellard <tstellar@redhat.com> - 11.0.0-0.1.rc1
- 11.0.0-rc1 Release

* Wed Jul 29 2020 sguelton@redhat.com - 10.0.0-8
- Make gcc dependency explicit, see https://fedoraproject.org/wiki/Packaging:C_and_C%2B%2B#BuildRequires_and_Requires
- use %%license macro

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 sguelton@redhat.com - 10.0.0-6
- Use ninja and according macros as build system

* Tue Jun 16 2020 sguelton@redhat.com - 10.0.0-5
- Finer grain specification of python3-lldb deps

* Tue Jun 02 2020 sguelton@redhat.com - 10.0.0-4
- Fix arch-dependent header

* Tue Jun 02 2020 sguelton@redhat.com - 10.0.0-3
- Instruct cmake not to generate RPATH

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 10.0.0-2
- Rebuilt for Python 3.9

* Mon Mar 30 2020 sguelton@redhat.com - 10.0.0-1
- 10.0.0 final

* Wed Mar 25 2020 sguelton@redhat.com - 10.0.0-0.6.rc6
- 10.0.0 rc6

* Fri Mar 20 2020 sguelton@redhat.com - 10.0.0-0.5.rc5
- 10.0.0 rc5

* Sun Mar 15 2020 sguelton@redhat.com - 10.0.0-0.4.rc4
- 10.0.0 rc4

* Thu Mar 05 2020 sguelton@redhat.com - 10.0.0-0.3.rc3
- 10.0.0 rc3

* Fri Feb 14 2020 sguelton@redhat.com - 10.0.0-0.2.rc2
- 10.0.0 rc2

* Fri Jan 31 2020 sguelton@redhat.com - 10.0.0-0.1.rc1
- 10.0.0 rc1

* Wed Jan 29 2020 Tom Stellard <tstellar@redhat.com> - 9.0.1-4
- Link against libclang-cpp.so
- https://fedoraproject.org/wiki/Changes/Stop-Shipping-Individual-Component-Libraries-In-clang-lib-Package

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 21 2019 Tom Stellard <tstellar@redhat.com> - 9.0.1-2
- 9.0.1 Release

* Thu Sep 19 2019 Tom Stellard <tstellar@redhat.com> - 9.0.0-1
- 9.0.0 Release

* Thu Aug 22 2019 Tom Stellard <tstellar@redhat.com> - 9.0.0-0.1.rc3
- 9.0.0-rc3 Release

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 8.0.0-2.2
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 26 2019 sguelton@redhat.com - 8.0.0-2
- Only depend on Python3

* Wed Mar 20 2019 sguelton@redhat.com - 8.0.0-1
- 8.0.0 final

* Tue Mar 12 2019 sguelton@redhat.com - 8.0.0-0.4.rc4
- 8.0.0 Release candidate 4

* Tue Mar 5 2019 sguelton@redhat.com - 8.0.0-0.3.rc3
- 8.0.0 Release candidate 3

* Fri Feb 22 2019 sguelton@redhat.com - 8.0.0-0.2.rc2
- 8.0.0 Release candidate 2

* Mon Feb 11 2019 sguelton@redhat.com - 8.0.0-0.1.rc1
- 8.0.0 Release candidate 1

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.1-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 17 2018 sguelton@redhat.com - 7.0.1-1
- 7.0.1 Release

* Tue Dec 04 2018 sguelton@redhat.com - 7.0.0-2
- Ensure rpmlint passes on specfile

* Tue Sep 25 2018 Tom Stellard <tstellar@redhat.com> - 7.0.0-1
- 7.0.0 Release

* Fri Sep 21 2018 Tom Stellard <tstellar@redhat.com> - 7.0.0-0.5.rc3
- lldb should depend on python2-lldb

* Mon Sep 17 2018 Tom Stellard <tstellar@redhat.com> - 7.0.0-0.4.rc3
- 7.0.0-rc3 Release

* Wed Sep 12 2018 Tom Stellard <tstellar@redhat.com> - 7.0.0-0.3.rc2
- Enable build on s390x

* Fri Aug 31 2018 Tom Stellard <tstellar@redhat.com> - 7.0.0-0.2.rc2
- 7.0.0-rc2 Release

* Tue Aug 14 2018 Tom Stellard <tstellar@redhat.com> - 7.0.0-0.1.rc1
- 7.0.1-rc1 Release

* Tue Aug 07 2018 Tom Stellard <tstellar@redhat.com> - 6.0.1-3
- Enable ppc64le arch

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 21 2018 Tom Stellard <tstellar@redhat.com> - 6.0.1-1
- 6.0.1 Release

* Mon May 21 2018 Tom Stellard <tstellar@redhat.com> - 6.0.1-0.1.rc1
- 6.0.1-rc1 Release

* Sat May 05 2018 Miro Hrončok <mhroncok@redhat.com> - 6.0.0-4
- Update Python macros to new packaging standards
  (See https://fedoraproject.org/wiki/Changes/Avoid_usr_bin_python_in_RPM_Build)

* Tue Mar 20 2018 Tom Stellard <tstellar@redhat.com> - 6.0.0-3
- Rebuild against llvm with the rhbz#1558657 fix

* Wed Mar 14 2018 Tilmann Scheller <tschelle@redhat.com> - 6.0.0-2
- Restore LLDB SB API headers, fixes rhbz#1548758

* Fri Mar 09 2018 Tom Stellard <tstellar@redhat.com> - 6.0.0-1
- 6.0.0 Release

* Tue Feb 13 2018 Tom Stellard <tstellar@redhat.com> - 6.0.0-0.3.rc2
- 6.0.0-rc2 release

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-0.2.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Tom Stellard <tstellar@redhat.com> - 6.0.0-0.1.rc1
- 6.0.1-rc1 Release

* Thu Dec 21 2017 Tom Stellard <tstellar@redhat.com> - 5.0.1-1
- 5.0.1 Release

* Fri Oct 06 2017 Tom Stellard <tstellar@redhat.com> - 5.0.0-1
- 5.0.0 Release

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 4.0.1-4
- Python 2 binary package renamed to python2-lldb
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Mon Jul 31 2017 Jan Kratochvil <jan.kratochvil@redhat.com> - 4.0.1-3
- Backport lldb r303907
  Resolves rhbz #1356140

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 26 2017 Tom Stellard <tstellar@redhat.com> - 4.0.1-1
- 4.0.1 Release

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Mar 24 2017 Tom Stellard <tstellar@redhat.com> - 4.0.0-1
- lldb 4.0.0

* Tue Mar 21 2017 Tom Stellard <tstellar@redhat.com> - 3.9.1-4
- Add explicit Requires for llvm-libs and clang-libs

* Fri Mar 17 2017 Tom Stellard <tstellar@redhat.org> - 3.9.1-3
- Adjust python sys.path so lldb can find readline.so

* Tue Mar 14 2017 Tom Stellard <tstellar@redhat.com> - 3.9.1-2
- Fix build with gcc 7

* Thu Mar 02 2017 Dave Airlie <airlied@redhat.com - 3.9.1-1
- lldb 3.9.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 14 2016 Nathaniel McCallum <npmccallum@redhat.com> - 3.9.0-3
- Disable libedit support until upstream fixes it (#1356140)

* Wed Nov  2 2016 Peter Robinson <pbrobinson@fedoraproject.org> 3.9.0-2
- Set upstream supported architectures in an ExclusiveArch

* Wed Oct 26 2016 Dave Airlie <airlied@redhat.com> - 3.9.0-1
- lldb 3.9.0
- fixup some issues with MIUtilParse by removing it
- build with -fno-rtti

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Mar 10 2016 Dave Airlie <airlied@redhat.com> 3.8.0-1
- lldb 3.8.0

* Thu Mar 03 2016 Dave Airlie <airlied@redhat.com> 3.8.0-0.3
- lldb 3.8.0 rc3

* Wed Feb 24 2016 Dave Airlie <airlied@redhat.com> - 3.8.0-0.2
- dynamically link to llvm

* Thu Feb 18 2016 Dave Airlie <airlied@redhat.com> - 3.8.0-0.1
- lldb 3.8.0 rc2

* Sun Feb 14 2016 Dave Airlie <airlied@redhat.com> 3.7.1-3
- rebuild lldb against latest llvm

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Oct 06 2015 Jan Vcelak <jvcelak@fedoraproject.org> 3.7.0-100
- initial version using cmake build system
