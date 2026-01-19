%global chez_version %(%{_bindir}/scheme --version 2>/dev/null || echo unknown)
%global forgeurl https://github.com/cosmos72/schemesh

Name:    schemesh
Version: 0.9.1
Release: 6%{?dist}
Summary: Fusion between a Unix shell and a Lisp REPL

%forgemeta
License: GPL-2.0-or-later
URL:     %{forgeurl}
Source0: %{forgesource}

BuildRequires: gcc
BuildRequires: make
# chez-scheme < 10.2 outputs --version to stderr
BuildRequires: chez-scheme-devel >= 10.2
BuildRequires: lz4-devel
BuildRequires: ncurses-devel
BuildRequires: libuuid-devel
BuildRequires: zlib-devel

Requires: chez-scheme%{?_isa} = %{chez_version}

%description
Schemesh is an interactive shell scriptable in Lisp.

It is primarily intended as a user-friendly Unix login shell,
replacing bash, zsh, pdksh etc.

%prep
%forgesetup

%build
%ifarch ppc64le s390x
EXTRA_LDFLAGS="-lffi"
%endif
%make_build \
    prefix=%{_prefix} \
    libdir=%{_libdir} \
    bindir=%{_bindir} \
    CFLAGS="$CFLAGS" \
    LDFLAGS="$LDFLAGS $EXTRA_LDFLAGS"

%install
%make_install prefix=%{_prefix} libdir=%{_libdir} bindir=%{_bindir}

%check
time ./schemesh_test

%files
%license COPYING
%doc README.md
%doc doc/*
%{_bindir}/schemesh
%{_bindir}/countdown
%{_libdir}/schemesh/

%changelog
* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Thu Nov 06 2025 Jens Petersen <petersen@redhat.com> - 0.9.1-5
- fix build on ppc64le and s390x

* Tue Nov 04 2025 Jens Petersen <petersen@redhat.com> - 0.9.1-4
- rebuild against newer chez-scheme

* Tue Nov 04 2025 Jens Petersen <petersen@redhat.com> - 0.9.1-3
- exclude ppc64le and s390x which are failing (#2385621)

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat May 10 2025 Jonny Heggheim <hegjon@gmail.com> - 0.9.1-1
- Updated to version 0.9.1

* Sat May 03 2025 Jonny Heggheim <hegjon@gmail.com> - 0.9.0-1
- Updated to version 0.9.0

* Tue Apr 22 2025 Jonny Heggheim <hegjon@gmail.com> - 0.8.3-3
- Require the version of chez-scheme that it is built against

* Fri Apr 18 2025 Jonny Heggheim <hegjon@gmail.com> - 0.8.3-2
- Added missing runtime requires on chez-scheme

* Mon Apr 07 2025 Jonny Heggheim <hegjon@gmail.com> - 0.8.3-1
- Updated to version 0.8.3

* Sat Apr 05 2025 Jonny Heggheim <hegjon@gmail.com> - 0.8.2-1
- Updated to version 0.8.2

* Tue Mar 18 2025 Jonny Heggheim <hegjon@gmail.com> - 0.8.1-1
- Updated to version 0.8.1

* Mon Feb 17 2025 Jonny Heggheim <hegjon@gmail.com> - 0.7.5-1
- Initial package
