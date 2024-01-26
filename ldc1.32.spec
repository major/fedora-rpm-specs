%if 0%{?rhel}
#global llvm_version 15
%else
%global llvm_version 15
%endif
%global soversion 102

%undefine _hardened_build
%undefine _package_note_file

Name:           ldc1.32
Version:        1.32.2
Release:        3%{?dist}
Summary:        LLVM D Compiler

# The DMD frontend in dmd/* GPL version 1 or artistic license
# The files gen/asmstmt.cpp and gen/asm-*.hG PL version 2+ or artistic license
License:        BSD
URL:            https://github.com/ldc-developers/ldc
Source0:        https://github.com/ldc-developers/ldc/releases/download/v%{version_no_tilde}/ldc-%{version_no_tilde}-src.tar.gz

# Make sure /usr/include/d is in the include search path
Patch0:         ldc-include-path.patch
# Don't add rpath to standard libdir
Patch1:         ldc-no-default-rpath.patch
%if 0%{?rhel} && 0%{?rhel} <= 9
# Keep on using ld.gold on RHEL 8 and 9 where using ldc with ld.bfd breaks gtkd
# and leads to crashing tilix.
# https://bugzilla.redhat.com/show_bug.cgi?id=2134875
Patch2:         0001-Revert-Linux-Don-t-default-to-ld.gold-linker.patch
%endif

ExclusiveArch:  %{ldc_arches} ppc64le

BuildRequires:  bash-completion
BuildRequires:  cmake
BuildRequires:  gc
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  ldc
BuildRequires:  libconfig-devel
BuildRequires:  libcurl-devel
BuildRequires:  libedit-devel
BuildRequires:  llvm%{?llvm_version}-devel
BuildRequires:  llvm%{?llvm_version}-static
BuildRequires:  make
BuildRequires:  zlib-devel

%description
LDC is a portable compiler for the D programming language with modern
optimization and code generation capabilities.

It uses the official DMD compiler frontend to support the latest version
of D, and relies on the LLVM Core libraries for code generation.

%package        libs
Summary:        LLVM D Compiler libraries
License:        Boost

%description    libs
LDC is a portable compiler for the D programming language with modern
optimization and code generation capabilities.

This package contains the Phobos D standard library and the D runtime library.

%prep
%autosetup -n ldc-%{version_no_tilde}-src -p1

%build
# This package appears to be failing because links to the LLVM plugins
# are not installed which results in the tools not being able to
# interpret the .o/.a files.  Disable LTO for now
%define _lto_cflags %{nil}

%global optflags %{optflags} -fno-strict-aliasing

tar xf %{SOURCE0}
mkdir build-bootstrap
pushd build-bootstrap
cmake -DLLVM_CONFIG:PATH=llvm-config%{?llvm_version:-%{llvm_version}} \
      ../ldc-%{version_no_tilde}-src
make %{?_smp_mflags}
popd

%cmake -DMULTILIB:BOOL=OFF \
       -DINCLUDE_INSTALL_DIR:PATH=%{_prefix}/lib/ldc/%{_target_platform}/include/d \
       -DBASH_COMPLETION_COMPLETIONSDIR:PATH=%{_datadir}/bash-completion/completions \
       -DLLVM_CONFIG:PATH=llvm-config%{?llvm_version:-%{llvm_version}} \
       -DD_COMPILER:PATH=`pwd`/build-bootstrap/bin/ldmd2 \
       %{nil}

%cmake_build

%install
%cmake_install

# Remove everything except for the shared libraries that are needed for binary
# compatibility
rm -rf $RPM_BUILD_ROOT%{_sysconfdir}
rm -rf $RPM_BUILD_ROOT%{_bindir}
rm -rf $RPM_BUILD_ROOT%{_prefix}/lib/ldc
rm -rf $RPM_BUILD_ROOT%{_libdir}/ldc_rt.dso.o
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.so
rm -rf $RPM_BUILD_ROOT%{_libdir}/*ldc-debug-shared*
rm -rf $RPM_BUILD_ROOT%{_datadir}/bash-completion/completions/ldc2

%files libs
%license runtime/phobos/LICENSE_1_0.txt
%{_libdir}/libdruntime-ldc-shared.so.%{soversion}*
%{_libdir}/libphobos2-ldc-shared.so.%{soversion}*

%changelog
* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.32.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.32.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 26 2023 Kalev Lember <klember@redhat.com> - 1.32.2-1
- Initial Fedora packaging
