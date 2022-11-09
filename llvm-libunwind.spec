%global toolchain clang
%global maj_ver 15
%global min_ver 0
%global patch_ver 4
#global rc_ver 3
%global libunwind_version %{maj_ver}.%{min_ver}.%{patch_ver}

%global libunwind_srcdir libunwind-%{libunwind_version}%{?rc_ver:rc%{rc_ver}}.src

Name:       llvm-libunwind
Version:    %{libunwind_version}%{?rc_ver:~rc%{rc_ver}}
Release:    1%{?dist}
Summary:    LLVM libunwind

License:    ASL 2.0 or NCSA or MIT
URL:        http://llvm.org
Source0:    https://github.com/llvm/llvm-project/releases/download/llvmorg-%{maj_ver}.%{min_ver}.%{patch_ver}%{?rc_ver:-rc%{rc_ver}}/%{libunwind_srcdir}.tar.xz
Source1:    https://github.com/llvm/llvm-project/releases/download/llvmorg-%{maj_ver}.%{min_ver}.%{patch_ver}%{?rc_ver:-rc%{rc_ver}}/%{libunwind_srcdir}.tar.xz.sig
Source2:    release-keys.asc

# Upstream tighly ties its build to libcxx source, we don't want to use that
# senario, so we need to maintain that patch downstream.
Patch0:     standalone.patch

BuildRequires:  clang
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  llvm-devel

# For documentation
BuildRequires:  python3-sphinx

# For gpg source verification
BuildRequires:  gnupg2

# Explicitly not supported upstream
ExcludeArch:    s390x

%description

LLVM libunwind is an implementation of the interface defined by the HP libunwind
project. It was contributed Apple as a way to enable clang++ to port to
platforms that do not have a system unwinder. It is intended to be a small and
fast implementation of the ABI, leaving off some features of HP's libunwind
that never materialized (e.g. remote unwinding).

%package devel
Summary:    LLVM libunwind development files
Provides:   libunwind(major) = %{maj_ver}
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
Static and unversioned shared libraries for LLVM libunwind

%package doc
Summary:    libunwind documentation
# jquery.js and langage_data.js are used in the HTML doc and under BSD License
License:    BSD and (ASL 2.0 or NCSA or MIT)

%description doc
Documentation for LLVM libunwind

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{libunwind_srcdir} -p2

%build
# Copy CFLAGS into ASMFLAGS, so -fcf-protection is used when compiling assembly files.
export ASMFLAGS=$CFLAGS

%cmake -GNinja \
    -DCMAKE_MODULE_PATH=%{_libdir}/cmake/llvm \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DLLVM_BUILD_DOCS=ON \
    -DLLVM_ENABLE_SPHINX=ON \
    -DLIBUNWIND_ENABLE_STATIC=OFF \
    -DLIBUNWIND_INCLUDE_DOCS=ON \
%if 0%{?__isa_bits} == 64
    -DLIBUNWIND_LIBDIR_SUFFIX=64 \
%else
    -DLIBUNWIND_LIBDIR_SUFFIX= \
%endif
    -DLIBUNWIND_INSTALL_SPHINX_HTML_DIR=%{_pkgdocdir}/html \
    -DSPHINX_WARNINGS_AS_ERRORS=OFF \
    -DSPHINX_EXECUTABLE=%{_bindir}/sphinx-build-3

%cmake_build

%install

%cmake_install

# We can't install the unversionned path on default location because that would conflict with
# https://src.fedoraproject.org/rpms/libunwind
#
# The versionned path has a different soname (libunwind.so.1 compared to
# libunwind.so.8) so they can live together in %{_libdir}
#
# ABI wise, even though llvm-libunwind's library is named libunwind, it doesn't
# have the exact same ABI has gcc's libunwind (it actually provides a subset).
rm %{buildroot}%{_libdir}/libunwind.so
mkdir -p %{buildroot}/%{_libdir}/llvm-unwind/

pushd %{buildroot}/%{_libdir}/llvm-unwind
ln -s ../libunwind.so.1.0 libunwind.so
popd



rm %{buildroot}%{_pkgdocdir}/html/.buildinfo

%check

# upstream has a hard dependency on libcxx source code for test to be configured
# properly. We can't model that, so rely on gating instead.
#cmake_build --target check-unwind

%files
%license LICENSE.TXT
%{_libdir}/libunwind.so.1
%{_libdir}/libunwind.so.1.0

%files devel
%dir %{_libdir}/llvm-unwind
%{_libdir}/llvm-unwind/libunwind.so

%files doc
%license LICENSE.TXT
%doc %{_pkgdocdir}/html

%changelog
* Mon Nov 07 2022 Nikita Popov <npopov@redhat.com> - 15.0.4-1
- Update to LLVM 15.0.4

* Mon Sep 12 2022 Nikita Popov <npopov@redhat.com> - 15.0.0-2
- Make sure asm files are built with -fcf-protection

* Fri Sep 09 2022 Nikita Popov <npopov@redhat.com> - 15.0.0-1
- Update to LLVM 15.0.0

* Thu Sep 8 2022 sguelton@redhat.com - 14.0.5-2
- Install versioned library in standard location

* Mon Aug 29 2022 sguelton@redhat.com - 14.0.5-1
- Update to LLVM 14.0.5

* Mon Aug 29 2022 sguelton@redhat.com - 14.0.0-1
- Update to LLVM 14.0.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 13.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

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

* Wed Nov 17 2021 sguelton@redhat.com - 13.0.0-1
- Initial release

