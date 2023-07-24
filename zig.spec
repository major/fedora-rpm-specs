# https://ziglang.org/download/%{version}/release-notes.html#Support-Table
# 32 bit builds currently run out of memory https://github.com/ziglang/zig/issues/6485
%global         zig_arches x86_64 aarch64 riscv64 %{mips64}

%global         llvm_version 13.0.0
%define         llvm_compat 13

%if 0%{?fedora} >= 38
# documentation and tests do not build due to an unsupported glibc version
%bcond_with     test
%bcond_with     docs
%else
%bcond_without  test
%bcond_without  docs
%endif

%bcond_without  macro


Name:           zig
Version:        0.9.1
Release:        4%{?dist}
Summary:        Programming language for maintaining robust, optimal, and reusable software

License:        MIT and NCSA and LGPLv2+ and LGPLv2+ with exceptions and GPLv2+ and GPLv2+ with exceptions and BSD and Inner-Net and ISC and Public Domain and GFDL and ZPLv2.1
URL:            https://ziglang.org
Source0:        https://github.com/ziglang/zig/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        macros.%{name}
# prevent native directories from polluting the rpath
# https://github.com/ziglang/zig/pull/10621
Patch0:         0001-ignore-target-lib-dirs-when-invoked-with-feach-lib-r.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  llvm%{?llvm_compat}-devel
BuildRequires:  clang%{?llvm_compat}-devel
BuildRequires:  lld%{?llvm_compat}-devel
# for man page generation
BuildRequires:  help2man

%if %{with macro} || 0%{?llvm_compat}
BuildRequires:  sed
%endif

%if %{with test}
# for testing
BuildRequires:  elfutils-libelf-devel
BuildRequires:  libstdc++-static
%endif

Requires:       %{name}-libs = %{version}

# These packages are bundled as source

# NCSA
Provides: bundled(compiler-rt) = %{llvm_version}
# LGPLv2+, LGPLv2+ with exceptions, GPLv2+, GPLv2+ with exceptions, BSD, Inner-Net, ISC, Public Domain and GFDL
Provides: bundled(glibc) = 2.34
# NCSA
Provides: bundled(libcxx) = %{llvm_version}
# NCSA
Provides: bundled(libcxxabi) = %{llvm_version}
# NCSA
Provides: bundled(libunwind) = %{llvm_version}
# BSD, LGPG, ZPL
Provides: bundled(mingw) = 9.0.0
# MIT
Provides: bundled(musl) = 1.2.2
# CC0, BSD, MIT, Apache2, Apache2 with exceptions
Provides: bundled(wasi-libc) = 82fc2c4f449e56319112f6f2583195c7f4e714b1

ExclusiveArch: %{zig_arches}

%description
Zig is an open-source programming language designed for robustness, optimality,
and clarity. This package provides the zig compiler and the associated runtime.

# the standard library contains only plain text
%package libs
Summary:        %{name} Standard Library
BuildArch:      noarch

%description libs
%{name} Standard Library

%if %{with docs}
%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}

%description doc
Documentation for %{name}. For more information, visit %{url}
%endif

%if %{with macro}
%package        rpm-macros
Summary:        Common RPM macros for %{name}
Requires:       rpm
BuildArch:      noarch

%description    rpm-macros
This package contains common RPM macros for %{name}.
%endif

%prep
%autosetup -p1

%if 0%{?llvm_compat}
    sed -i "s|/usr/lib/llvm-13|%{_libdir}/llvm%{llvm_compat}|g" cmake/Find{clang,lld,llvm}.cmake
%endif

%build

%cmake \
    -DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
    -DZIG_PREFER_CLANG_CPP_DYLIB=true \
    -DZIG_VERSION:STRING="%{version}"
%cmake_build

# Zig has no official manpage
# https://github.com/ziglang/zig/issues/715
help2man --no-discard-stderr "%{__cmake_builddir}/zig" --version-option=version --output=%{name}.1

ln -s lib "%{__cmake_builddir}/"

%if %{with docs}
%{__cmake_builddir}/zig build docs -Dversion-string="%{version}"
%endif
mkdir -p zig-cache
touch zig-cache/langref.html

%install
%cmake_install

mkdir -p %{buildroot}/%{_mandir}/man1
install -m 0644 %{name}.1 %{buildroot}%{_mandir}/man1/

mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d/

install -p -m644 %{SOURCE1} %{buildroot}%{_rpmconfigdir}/macros.d/
sed -i -e "s|@@ZIG_VERSION@@|%{version}|"  %{buildroot}%{_rpmconfigdir}/macros.d/macros.%{name}

%check

%if %{with test}
# Issues with tests stop them from completing successfully
# https://github.com/ziglang/zig/issues/9738
#%%{__cmake_builddir}/zig build test
%endif

%files
%license LICENSE
%{_bindir}/zig
%{_mandir}/man1/%{name}.1.*

%files libs
%{_prefix}/lib/%{name}

%if %{with docs}
%files doc
%doc README.md
%doc zig-cache/langref.html
%endif

%if %{with macro}
%files rpm-macros
%{_rpmconfigdir}/macros.d/macros.%{name}
%endif

%changelog
* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Feb 18 2022 Jan Drögehoff <sentrycraft123@gmail.com> - 0.9.1-1
- Update to 0.9.1

* Thu Jan 27 2022 Jan Drögehoff <sentrycraft123@gmail.com> - 0.9.0-3
- Jan: add rpath patch
- Aleksei Bavshin: rpm macros: set default build flags

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild


* Mon Dec 20 2021 Jan Drögehoff <sentrycraft123@gmail.com> - 0.9.0-1
- Update to 0.9.0

* Wed Nov 17 2021 Jan Drögehoff <sentrycraft123@gmail.com> - 0.8.1-5
- Enable documentation on Fedora 35

* Tue Nov 09 2021 Tom Stellard <tstellar@redhat.com> - 0.8.1-4
- Rebuild for llvm-13.0.0

* Sat Oct 30 2021 Jan Drögehoff <sentrycraft123@gmail.com> - 0.8.1-3
- Update LLVM13 Patch

* Thu Oct 07 2021 Tom Stellard <tstellar@redhat.com> - 0.8.1-2
- Rebuild for llvm-13.0.0

* Sun Sep 12 2021 Jan Drögehoff <sentrycraft123@gmail.com> - 0.8.1-1
- Update to Zig 0.8.1, add LLVM 13 patch

* Wed Aug 18 2021 Jan Drögehoff <sentrycraft123@gmail.com> - 0.8.0-8
- Rebuilt for lld soname bump

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 19 2021 Jan Drögehoff <sentrycraft123@gmail.com> - 0.8.0-6
- add native libc detection patch

* Sun Jul 04 2021 Jan Drögehoff <sentrycraft123@gmail.com> - 0.8.0-5
- correct newline in macro that caused DESTDIR to be ignored

* Mon Jun 28 2021 Jan Drögehoff <sentrycraft123@gmail.com> - 0.8.0-4
- correct macro once again to allow for proper packaging

* Thu Jun 24 2021 Jan Drögehoff <sentrycraft123@gmail.com> - 0.8.0-3
- improve macro for using the zig binary

* Thu Jun 24 2021 Jan Drögehoff <sentrycraft123@gmail.com> - 0.8.0-2
- Update patches, correct rpm macro

* Sat Jun 05 2021 Jan Drögehoff <sentrycraft123@gmail.com> - 0.8.0-1
- Update to Zig 0.8.0

* Sun Dec 13 23:18:24 CET 2020 Jan Drögehoff <sentrycraft123@gmail.com> - 0.7.1-1
- Update to Zig 0.7.1

* Wed Nov 11 17:18:27 CET 2020 Jan Drögehoff <sentrycraft123@gmail.com> - 0.7.0-1
- Update to Zig 0.7.0

* Tue Aug 18 2020 Jan Drögehoff <sentrycraft123@gmail.com> - 0.6.0-1
- Initial zig spec
