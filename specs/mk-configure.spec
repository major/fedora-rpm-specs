Name: mk-configure
Version: 0.38.3
Release: 5%{?dist}
Summary: A build system on top of bmake
License: BSD-2-Clause AND BSD-4-Clause AND ISC
# Licenses listed in the doc/LICENSE file
URL: https://github.com/cheusov/mk-configure/


Source0: https://github.com/cheusov/mk-configure/archive/%{version}/%{name}-%{version}.tar.gz
Source1: mkcmake.macros

Patch0: 0001-ignore-incompatible-pointer-types-errors.patch

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: bison
BuildRequires: bmake
BuildRequires: imake
BuildRequires: texinfo
BuildRequires: clang
BuildRequires: fdupes
BuildRequires: flex
BuildRequires: libfl-devel
BuildRequires: gcc-c++
BuildRequires: glib2-devel
BuildRequires: groff
BuildRequires: byacc
BuildRequires: info
BuildRequires: libbsd-devel
BuildRequires: lua-devel
BuildRequires: pkgconfig
BuildRequires: zlib-devel
BuildRequires: glibc-devel
Requires: bmake
Requires: imake
Requires: redhat-rpm-config
BuildArch: noarch

%description
The mk-configure tool is a build system, written in and for bmake
(portable version of NetBSD make) and UNIX tools (shell, awk etc.).

%package doc
Summary: The mk-configure documentation
License: BSD-2-Clause AND ISC AND CC0-1.0
# ISC in the strlcpy and strlcpy2 examples
# CC0-1.0 in the hello_world example
# BSD-2-Clause in the rest as implied by the doc/LICENSE file upstream

Requires: %{name} = %{version}-%{release}

%description doc
The mk-configure package examples

%global env \
        unset MAKEFLAGS \
        export USE_NM=%{_bindir}/nm \
        export USE_INSTALL=%{_bindir}/install \
        export USE_AWK=%{_bindir}/awk \
        export USE_ID=%{_bindir}/id \
        export USE_CC_COMPILERS='gcc clang' \
        export USE_CXX_COMPILERS='g++ clang' \
        export PREFIX=%{_prefix} \
        export SYSCONFDIR=%{_sysconfdir} \
        export MANDIR=%{_mandir}

%prep
%autosetup -p1

%build
%{env}
bmake all

%install
%{env}
bmake install DESTDIR=%{buildroot}
install -m644 %{SOURCE1} -D %{buildroot}%{_rpmmacrodir}/macros.mkcmake
rm -rf %{buildroot}%{_datadir}/doc/%{name}
mkdir -p %{buildroot}%{_docdir}/%{name}
chmod -x examples/*/*.in
chmod -x examples/*/*/*.in
cp -r examples %{buildroot}%{_docdir}/%{name}/

%check
unset MAKEFLAGS
# Disable all compilation warnings so that the test diffs can work
env bmake test-tests

%files
%doc README.md doc/FAQ doc/NEWS doc/TODO
%license doc/LICENSE
%{_bindir}/mkc_check_*
%{_bindir}/mkc_compiler_settings
%{_bindir}/mkc_install
%{_bindir}/mkc_which
%{_bindir}/mkcmake
%{_datadir}/mk-configure/
%{_mandir}/man1/mkc_check_*.1*
%{_mandir}/man1/mkc_compiler_settings.1*
%{_mandir}/man1/mkc_install.1*
%{_mandir}/man1/mkc_which.1*
%{_mandir}/man1/mkcmake.1*
%{_mandir}/man7/mk-configure.7*
%{_rpmmacrodir}/macros.mkcmake
%{_libexecdir}/mk-configure


%files doc
%license %{_docdir}/mk-configure/examples/autoconf/proj/COPYING
%license %{_docdir}/mk-configure/examples/autotools/proj/COPYING
%license %{_docdir}/mk-configure/examples/hello_world/COPYRIGHT
%doc %{_docdir}/mk-configure/examples

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.38.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Sep 29 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 0.38.3-4
- Fix macros for flatpak builds

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.38.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Feb 19 2024 Carlos Rodriguez-Fernandez <carlosrodrifernandez@gmail.com> - 0.38.3-2
- Remove concurrency in macro call because it is not well supported due to output redirects 
* Sat Jan 6 2024 Carlos Rodriguez-Fernandez <carlosrodrifernandez@gmail.com> - 0.38.3-1
- First release
