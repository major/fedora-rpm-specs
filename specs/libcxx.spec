%global toolchain clang

# Opt out of https://fedoraproject.org/wiki/Changes/fno-omit-frame-pointer
# https://bugzilla.redhat.com/show_bug.cgi?id=2158587
%undefine _include_frame_pointers

%global maj_ver 19
%global libcxx_version %{maj_ver}.1.6
#global rc_ver 4
%global libcxx_srcdir libcxx-%{libcxx_version}%{?rc_ver:-rc%{rc_ver}}.src
%global libcxxabi_srcdir libcxxabi-%{libcxx_version}%{?rc_ver:-rc%{rc_ver}}.src
%global libunwind_srcdir libunwind-%{libcxx_version}%{?rc_ver:-rc%{rc_ver}}.src

Name:		libcxx
Version:	%{libcxx_version}%{?rc_ver:~rc%{rc_ver}}
Release:	2%{?dist}
Summary:	C++ standard library targeting C++11
License:	Apache-2.0 WITH LLVM-exception OR MIT OR NCSA
URL:		http://libcxx.llvm.org/
Source0:	https://github.com/llvm/llvm-project/releases/download/llvmorg-%{libcxx_version}%{?rc_ver:-rc%{rc_ver}}/%{libcxx_srcdir}.tar.xz
Source1:	https://github.com/llvm/llvm-project/releases/download/llvmorg-%{libcxx_version}%{?rc_ver:-rc%{rc_ver}}/%{libcxx_srcdir}.tar.xz.sig
Source2:	https://github.com/llvm/llvm-project/releases/download/llvmorg-%{libcxx_version}%{?rc_ver:-rc%{rc_ver}}/%{libcxxabi_srcdir}.tar.xz
Source3:	https://github.com/llvm/llvm-project/releases/download/llvmorg-%{libcxx_version}%{?rc_ver:-rc%{rc_ver}}/%{libcxxabi_srcdir}.tar.xz.sig
Source4:	https://github.com/llvm/llvm-project/releases/download/llvmorg-%{libcxx_version}%{?rc_ver:-rc%{rc_ver}}/%{libunwind_srcdir}.tar.xz
Source5:	https://github.com/llvm/llvm-project/releases/download/llvmorg-%{libcxx_version}%{?rc_ver:-rc%{rc_ver}}/%{libunwind_srcdir}.tar.xz.sig
Source6:	release-keys.asc
Source7:	CMakeLists.txt
Source8:	https://github.com/llvm/llvm-project/raw/llvmorg-%{libcxx_version}%{?rc_ver:-rc%{rc_ver}}/runtimes/cmake/Modules/HandleFlags.cmake
Source9:	https://github.com/llvm/llvm-project/raw/llvmorg-%{libcxx_version}%{?rc_ver:-rc%{rc_ver}}/runtimes/cmake/Modules/WarningFlags.cmake

Patch0: standalone.patch
# The cmake dependencies for this target are somehow broken upstream.
# However, the libcxx.imp file is only needed for running include-what-you-use.
Patch1: do-not-install-libcxx.imp.patch

BuildRequires:	clang llvm-devel llvm-cmake-utils cmake ninja-build
# We need python3-devel for %%py3_shebang_fix
BuildRequires:	python3-devel

# For documentation
BuildRequires:	python3-sphinx

# For origin certification
BuildRequires:	gnupg2

# PPC64 (on EL7) doesn't like this code.
# /builddir/build/BUILD/libcxx-3.8.0.src/include/thread:431:73: error: '(9.223372036854775807e+18 / 1.0e+9)' is not a constant expression
# _LIBCPP_CONSTEXPR duration<long double> _Max = nanoseconds::max();
%if 0%{?rhel}
ExcludeArch:	ppc64 ppc64le
%endif

Requires: libcxxabi%{?_isa} = %{version}-%{release}

%description
libc++ is a new implementation of the C++ standard library, targeting C++11.

%package devel
Summary:	Headers and libraries for libcxx devel
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	libcxxabi-devel

%description devel
%{summary}.

%package static
Summary:	Static libraries for libcxx

%description static
%{summary}.

%package -n libcxxabi
Summary:	Low level support for a standard C++ library

%description -n libcxxabi
libcxxabi provides low level support for a standard C++ library.

%package -n libcxxabi-devel
Summary:	Headers and libraries for libcxxabi devel
Requires:	libcxxabi%{?_isa} = %{version}-%{release}

%description -n libcxxabi-devel
%{summary}.

%package -n libcxxabi-static
Summary:	Static libraries for libcxxabi

%description -n libcxxabi-static
%{summary}.

%package -n llvm-libunwind
Summary:    LLVM libunwind

%description -n llvm-libunwind

LLVM libunwind is an implementation of the interface defined by the HP libunwind
project. It was contributed Apple as a way to enable clang++ to port to
platforms that do not have a system unwinder. It is intended to be a small and
fast implementation of the ABI, leaving off some features of HP's libunwind
that never materialized (e.g. remote unwinding).

%package -n llvm-libunwind-devel
Summary:    LLVM libunwind development files
Provides:   libunwind(major) = %{maj_ver}
Requires:   llvm-libunwind%{?_isa} = %{version}-%{release}

%description -n llvm-libunwind-devel
Unversioned shared library for LLVM libunwind

%package -n llvm-libunwind-static
Summary: Static library for LLVM libunwind

%description -n llvm-libunwind-static
%{summary}.

%package -n llvm-libunwind-doc
Summary:    libunwind documentation
# doctools.js, searchtools.js and language_data.js are used in the HTML doc
# generated from sphinx-doc under BSD 2-Clause License.
# Source: https://github.com/sphinx-doc/sphinx
License:    BSD-2-Clause AND (Apache-2.0 WITH LLVM-exception OR NCSA OR MIT)

%description -n llvm-libunwind-doc
Documentation for LLVM libunwind

%prep
%{gpgverify} --keyring='%{SOURCE6}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%{gpgverify} --keyring='%{SOURCE6}' --signature='%{SOURCE3}' --data='%{SOURCE2}'
%{gpgverify} --keyring='%{SOURCE6}' --signature='%{SOURCE5}' --data='%{SOURCE4}'

%setup -T -q -b 0 -n %{libcxx_srcdir}
%setup -T -q -b 2 -n %{libcxxabi_srcdir}
%setup -T -q -b 4 -n %{libunwind_srcdir}
%setup -T -c -n build

cp %{SOURCE7} .
mv ../%{libcxx_srcdir} libcxx
mv ../%{libcxxabi_srcdir} libcxxabi
mv ../%{libunwind_srcdir} libunwind
mkdir -p runtimes/cmake/Modules
cp %{SOURCE8} %{SOURCE9} runtimes/cmake/Modules/
%autopatch -p1

%py3_shebang_fix libcxx/utils/

%build

# Copy CFLAGS into ASMFLAGS, so -fcf-protection is used when compiling assembly files.
export ASMFLAGS=$CFLAGS

%cmake -GNinja \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DCMAKE_MODULE_PATH="%{_libdir}/cmake/llvm;%{_datadir}/llvm/cmake/Modules" \
	-DCMAKE_POSITION_INDEPENDENT_CODE=ON \
%if 0%{?__isa_bits} == 64
	-DLIBCXX_LIBDIR_SUFFIX:STRING=64 \
	-DLIBCXXABI_LIBDIR_SUFFIX:STRING=64 \
	-DLIBUNWIND_LIBDIR_SUFFIX:STRING=64 \
%endif
	-DLIBCXX_INCLUDE_BENCHMARKS=OFF \
	-DLIBCXX_STATICALLY_LINK_ABI_IN_STATIC_LIBRARY=ON \
	-DLIBCXX_ENABLE_ABI_LINKER_SCRIPT=ON \
	-DLIBCXXABI_USE_LLVM_UNWINDER=OFF \
	-DLLVM_BUILD_DOCS=ON \
	-DLLVM_ENABLE_SPHINX=ON \
	-DLIBUNWIND_INCLUDE_DOCS=ON \
	-DLIBUNWIND_INSTALL_INCLUDE_DIR=%{_includedir}/llvm-libunwind \
	-DLIBUNWIND_INSTALL_SPHINX_HTML_DIR=%{_pkgdocdir}/html

%cmake_build

%install

%cmake_install

# We can't install the unversionned path on default location because that would conflict with
# https://src.fedoraproject.org/rpms/libunwind
#
# The versionned path has a different soname (libunwind.so.1 compared to
# libunwind.so.8) so they can live together in %%{_libdir}
#
# ABI wise, even though llvm-libunwind's library is named libunwind, it doesn't
# have the exact same ABI as gcc's libunwind (it actually provides a subset).
rm %{buildroot}%{_libdir}/libunwind.so
mkdir -p %{buildroot}/%{_libdir}/llvm-unwind/

pushd %{buildroot}/%{_libdir}/llvm-unwind
ln -s ../libunwind.so.1.0 libunwind.so
popd

rm %{buildroot}%{_pkgdocdir}/html/.buildinfo

%ldconfig_scriptlets

%files
%license libcxx/LICENSE.TXT
%doc libcxx/CREDITS.TXT libcxx/TODO.TXT
%{_libdir}/libc++.so.*

%files devel
%{_includedir}/c++/
%exclude %{_includedir}/c++/v1/cxxabi.h
%exclude %{_includedir}/c++/v1/__cxxabi_config.h
%{_libdir}/libc++.so
%{_libdir}/libc++.modules.json
%{_datadir}/libc++/v1/*

%files static
%license libcxx/LICENSE.TXT
%{_libdir}/libc++.a
%{_libdir}/libc++experimental.a

%files -n libcxxabi
%license libcxxabi/LICENSE.TXT
%doc libcxxabi/CREDITS.TXT
%{_libdir}/libc++abi.so.*

%files -n libcxxabi-devel
%{_includedir}/c++/v1/cxxabi.h
%{_includedir}/c++/v1/__cxxabi_config.h
%{_libdir}/libc++abi.so

%files -n libcxxabi-static
%{_libdir}/libc++abi.a

%files -n llvm-libunwind
%license libunwind/LICENSE.TXT
%{_libdir}/libunwind.so.1
%{_libdir}/libunwind.so.1.0

%files -n llvm-libunwind-devel
%{_includedir}/llvm-libunwind/__libunwind_config.h
%{_includedir}/llvm-libunwind/libunwind.h
%{_includedir}/llvm-libunwind/libunwind.modulemap
%{_includedir}/llvm-libunwind/mach-o/compact_unwind_encoding.h
%{_includedir}/llvm-libunwind/unwind.h
%{_includedir}/llvm-libunwind/unwind_arm_ehabi.h
%{_includedir}/llvm-libunwind/unwind_itanium.h
%dir %{_libdir}/llvm-unwind
%{_libdir}/llvm-unwind/libunwind.so

%files -n llvm-libunwind-static
%{_libdir}/libunwind.a

%files -n llvm-libunwind-doc
%license libunwind/LICENSE.TXT
%doc %{_pkgdocdir}/html

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 19.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jan 02 2025 Timm Bäder <tbaeder@redhat.com> - 19.1.6-1
- Update to 19.1.6

* Thu Dec 05 2024 Timm Bäder <tbaeder@redhat.com> - 19.1.5-1
- Update to 19.1.5

* Mon Nov 25 2024 Timm Bäder <tbaeder@redhat.com> - 19.1.4-1
- Update to 19.1.4

* Thu Nov 07 2024 Timm Bäder <tbaeder@redhat.com> - 19.1.3-1
- Update to 19.1.3

* Thu Sep 19 2024 Timm Bäder <tbaeder@redhat.com> - 19.1.0-1
- Update to 19.1.0

* Fri Sep 13 2024 Timm Bäder <tbaeder@redhat.com> - 19.1.0~rc4-1
- Update to 19.1.0-rc4

* Tue Jul 30 2024 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 18.1.8-3
- Migrate llvm-libunwind-doc to SPDX license

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 18.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jul 11 2024 Jesus Checa Hidalgo <jchecahi@redhat.com> - 18.1.8-1
- 18.1.8 Release

* Thu Jun 13 2024 Tom Stellard <tstellar@redhat.com> - 18.1.7-1
- 18.1.7 Release

* Tue May 21 2024 Tom Stellard <tstellar@redhat.com> - 18.1.6-1
- 18.1.6 Release

* Fri May 03 2024 Tom Stellard <tstellar@redhat.com> - 18.1.4-1
- 18.1.4 Release

* Wed Apr 17 2024 Tom Stellard <tstellar@redhat.com> - 18.1.3-1
- 18.1.3 Release

* Fri Mar 22 2024 Tom Stellard <tstellar@redhat.com> - 18.1.2-1
- 18.1.2 Release

* Wed Mar 13 2024 Tom Stellard <tstellar@redhat.com> - 18.1.1-1
- 18.1.1 Release

* Mon Mar 04 2024 Nikita Popov <npopov@redhat.com> - 18.1.0~rc4-2
- Disable LIBCXXABI_USE_LLVM_UNWINDER (rhbz#2267690)

* Thu Feb 29 2024 Tom Stellard <tstellar@redhat.com> - 18.1.0~rc4-1
- 18.1.0-rc4 Release

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 17.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 17.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 29 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 17.0.6-1
- Update to LLVM 17.0.6

* Wed Nov 01 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 17.0.4-1
- Update to LLVM 17.0.4

* Wed Oct 18 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 17.0.3-1
- Update to LLVM 17.0.3

* Wed Oct 04 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 17.0.2-1
- Update to LLVM 17.0.2

* Mon Sep 25 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 17.0.1-1
- Update to LLVM 17.0.1

* Mon Sep 11 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 17.0.0~rc4-1
- Update to LLVM 17.0.0 RC4

* Fri Aug 25 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 17.0.0~rc3-1
- Update to LLVM 17.0.0 RC3

* Wed Aug 23 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 17.0.0~rc2-1
- Update to LLVM 17.0.0 RC2

* Wed Aug 02 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 17.0.0~rc1-1
- Update to LLVM 17.0.0 RC1

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 16.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 10 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.6-1
- Update to LLVM 16.0.6

* Thu Jun 15 2023 Nikita Popov <npopov@redhat.com> - 16.0.5-2
- Use llvm-cmake-utils package

* Tue Jun 06 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.5-1
- Update to LLVM 16.0.5

* Tue May 30 2023 Nikita Popov <npopov@redhat.com> - 16.0.4-2
- Merge llvm-libunwind srpm into libcxx

* Fri May 19 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.4-1
- Update to LLVM 16.0.4

* Wed May 10 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.3-1
- Update to LLVM 16.0.3

* Wed Apr 26 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.2-1
- Update to LLVM 16.0.2

* Thu Apr 20 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.1-2
- Enable PIC even for static libraries (rhbz#2186531)

* Thu Apr 13 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.1-1
- Update to LLVM 16.0.1

* Mon Mar 20 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.0-1
- Update to LLVM 16.0.0

* Wed Mar 15 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.0~rc4-1
- Update to LLVM 16.0.0 RC4

* Thu Feb 23 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.0~rc3-1
- Update to LLVM 16.0.0 RC3

* Fri Feb 10 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.0~rc1-1
- Update to LLVM 16.0.0 RC1

* Wed Feb 01 2023 Tom Stellard <tstellar@redhat.com> - 15.0.7-4
- Omit frame pointers when building

* Thu Jan 19 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 15.0.7-3
- Include the Apache license adopted in 2019.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 15.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 13 2023 Nikita Popov <npopov@redhat.com> - 15.0.7-1
- Update to LLVM 15.0.7

* Tue Dec 06 2022 Nikita Popov <npopov@redhat.com> - 15.0.6-1
- Update to LLVM 15.0.6

* Mon Nov 07 2022 Nikita Popov <npopov@redhat.com> - 15.0.4-1
- Update to LLVM 15.0.4

* Wed Oct 05 2022 Nikita Popov <npopov@redhat.com> - 15.0.0-5
- Fix libcxxabi dependencies

* Wed Oct 05 2022 Nikita Popov <npopov@redhat.com> - 15.0.0-4
- Combine with libcxxabi build

* Tue Sep 13 2022 Nikita Popov <npopov@redhat.com> - 15.0.0-3
- Rebuild

* Tue Sep 13 2022 Nikita Popov <npopov@redhat.com> - 15.0.0-2
- Link libc++.a against libc++abi.a

* Thu Sep 08 2022 Nikita Popov <npopov@redhat.com> - 15.0.0-1
- Update to LLVM 15.0.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 14.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 20 2022 Timm Bäder <tbaeder@redhat.com> - 14.0.5-1
- Update to 14.0.5

* Fri Apr 29 2022 Timm Bäder <tbaeder@redhat.com> - 14.0.0-2
- Remove llvm-cmake-devel BR

* Thu Mar 24 2022 Timm Bäder <tbaeder@redhat.com> - 14.0.0-1
- Update to 14.0.0

* Thu Feb 03 2022 Nikita Popov <npopov@redhat.com> - 13.0.1-1
- Update to LLVM 13.0.1 final

* Tue Feb 01 2022 Nikita Popov <npopov@redhat.com> - 13.0.1~rc3-1
- Update to LLVM 13.0.1rc3

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

* Tue Jul 13 2021 Tom Stellard <tstellar@redhat.com> - 12.0.1-1
- 12.0.1 Release

* Thu Jul 01 2021 Tom Stellard <tstellar@redhat.com> - 12.0.1~rc3-1
- 12.0.1-rc3 Release

* Thu Jun 03 2021 Tom Stellard <tstellar@redhat.com> - 12.0.1~rc1-1
- 12.0.1-rc1 Release

* Fri Apr 16 2021 Tom Stellard <tstellar@redhat.com> - 12.0.0-1
- 12.0.0 Release

* Thu Apr 08 2021 sguelton@redhat.com - 12.0.0-0.7.rc5
- New upstream release candidate

* Fri Apr 02 2021 sguelton@redhat.com - 12.0.0-0.6.rc4
- New upstream release candidate

* Thu Mar 11 2021 sguelton@redhat.com - 12.0.0-0.5.rc3
- LLVM 12.0.0 rc3

* Tue Mar 09 2021 sguelton@redhat.com - 12.0.0-0.4.rc2
- rebuilt

* Thu Feb 25 2021 Timm Bäder <tbaeder@redhat.com> - 12.0.0-0.3.rc2
- Build shared and static libc++ separately
- Include libc++abi symbols in static libc++.a

* Wed Feb 24 2021 sguelton@redhat.com - 12.0.0-0.2.rc2
- 12.0.0-rc2 release

* Wed Feb 17 2021 Tom Stellard <tstellar@redhat.com> - 12.0.0-0.1.rc1
- 12.0.0-rc1 Release

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 11.1.0-0.3.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Serge Guelton - 11.1.0-0.2.rc2
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

* Tue Aug 11 2020 Tom Stellard <tstellar@redhat.com> - 11.0.0-0.1.rc1
- 11.0.0-rc1 Release

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 sguelton@redhat.com - 10.0.0-2
- Use modern cmake macros
- Finalize source verification

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

* Fri Feb 14 2020 sguelton@redhat.com - 10.0.0-0.1.rc2
- 10.0.0 rc2

* Thu Feb 6 2020 sguelton@redhat.com - 10.0.0-0.2.rc1
- bootstrap off

* Fri Jan 31 2020 sguelton@redhat.com - 10.0.0-0.1.rc1
- 10.0.0 rc1

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Tom Stellard <tstellar@redhat.com> - 9.0.1-1
- 9.0.1 Release

* Thu Jan 16 2020 Tom Stellard <tstellar@redhat.com> - 9.0.0-2
- Build with gcc on all arches

* Mon Sep 23 2019 Tom Stellard <tstellar@redhat.com> - 9.0.0-1
- 9.0.0 Release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 20 2019 sguelton@redhat.com - 8.0.0-1
- 8.0.0 final

* Tue Mar 12 2019 sguelton@redhat.com - 8.0.0-0.4.rc4
- 8.0.0 Release candidate 4

* Mon Mar 4 2019 sguelton@redhat.com - 8.0.0-0.3.rc3
- 8.0.0 Release candidate 3

* Sun Feb 24 2019 sguelton@redhat.com - 8.0.0-0.2.rc2
- 8.0.0 Release candidate 2

* Mon Feb 11 2019 sguelton@redhat.com - 8.0.0-0.1.rc1
- 8.0.0 Release candidate 1

* Wed Feb 06 2019 sguelton@redhat.com - 7.0.1-1
- 7.0.1 Release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.1-0.2.rc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 10 2018 sguelton@redhat.com - 7.0.1-0.1.rc3
- 7.0.1-rc3 Release

* Tue Sep 25 2018 Tom Stellard <tstellar@redhat.com> - 7.0.0-1
- 7.0.0 Release

* Wed Sep 12 2018 Tom Stellard <tstellar@redhat.com> - 7.0.0-0.1.rc3
- 7.0.0-rc3 Release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 26 2018 Tom Callaway <spot@fedoraproject.org> - 6.0.1-1
- update to 6.0.1

* Wed Mar 21 2018 Tom Stellard <tstellar@redhat.com> - 6.0.0-2
- Use default LDFLAGS/CXXFLAGS/CFLAGS and filter out flags not supported by clang

* Wed Mar 14 2018 Tom Callaway <spot@fedoraproject.org> - 6.0.0-1
- 6.0.0 final

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-0.2.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Tom Stellard <tstellar@redhat.com> - 6.0.0-0.1.rc1
- 6.0.0-rc1

* Thu Dec  21 2017 Tom Stellard <tstellar@redhat.com> - 5.0.1-1
- 5.0.1 Release

* Fri Sep  8 2017 Tom Callaway <spot@fedoraproject.org> - 5.0.0-1
- update to 5.0.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 23 2017 Tom Callaway <spot@fedoraproject.org> - 4.0.1-1
- update to 4.0.1

* Sat Apr 22 2017 Tom Callaway <spot@fedoraproject.org> - 4.0.0-1
- update to 4.0.0

* Wed Mar  8 2017 Tom Callaway <spot@fedoraproject.org> - 3.9.1-1
- update to 3.9.1

* Fri Mar  3 2017 Tom Callaway <spot@fedoraproject.org> - 3.9.0-4
- LIBCXX_ENABLE_ABI_LINKER_SCRIPT=ON

* Wed Mar  1 2017 Tom Callaway <spot@fedoraproject.org> - 3.9.0-3
- disable bootstrap

* Tue Feb 21 2017 Dan Horák <dan[at]danny.cz> - 3.9.0-2
- apply s390(x) workaround only in Fedora < 26

* Mon Feb 20 2017 Tom Callaway <spot@fedoraproject.org> - 3.9.0-1
- update to 3.9.0 (match clang)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Aug 26 2016 Tom Callaway <spot@fedoraproject.org> - 3.8.1-1
- update to 3.8.1

* Thu Jun 09 2016 Dan Horák <dan[at]danny.cz> - 3.8.0-4
- exclude Power only in EPEL
- default to z10 on s390(x)

* Thu May 19 2016 Tom Callaway <spot@fedoraproject.org> - 3.8.0-3
- use gcc on el7, fedora < 24. use clang on el6 and f24+
  MAGIC.
- bootstrap on

* Tue May 3 2016 Tom Callaway <spot@fedoraproject.org> - 3.8.0-2
- bootstrap off

* Tue May 3 2016 Tom Callaway <spot@fedoraproject.org> - 3.8.0-1
- initial package
- bootstrap on
