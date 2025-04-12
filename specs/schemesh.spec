%global forgeurl https://github.com/cosmos72/schemesh

Name:    schemesh
Version: 0.8.3
Release: 1%{?dist}
Summary: Fusion between a Unix shell and a Lisp REPL

%forgemeta
License: GPL-2.0-or-later
URL:     %{forgeurl}
Source0: %{forgesource}

BuildRequires: gcc
BuildRequires: make
BuildRequires: chez-scheme-devel
BuildRequires: lz4-devel
BuildRequires: ncurses-devel
BuildRequires: libuuid-devel
BuildRequires: zlib-devel

%description
Schemesh is an interactive shell scriptable in Lisp.

It is primarily intended as a user-friendly Unix login shell,
replacing bash, zsh, pdksh etc.

%prep
%forgesetup

%build
%make_build \
    prefix=%{_prefix} \
    libdir=%{_libdir} \
    bindir=%{_bindir} \
    CFLAGS="$CFLAGS" \
    LDFLAGS="$LDFLAGS"

%install
%make_install prefix=%{_prefix} libdir=%{_libdir} bindir=%{_bindir}

%check
./schemesh_test

%files
%license COPYING
%doc README.md
%doc doc/*
%{_bindir}/schemesh
%{_bindir}/countdown
%{_libdir}/schemesh/

%changelog
* Mon Apr 07 2025 Jonny Heggheim <hegjon@gmail.com> - 0.8.3-1
- Updated to version 0.8.3

* Sat Apr 05 2025 Jonny Heggheim <hegjon@gmail.com> - 0.8.2-1
- Updated to version 0.8.2

* Tue Mar 18 2025 Jonny Heggheim <hegjon@gmail.com> - 0.8.1-1
- Updated to version 0.8.1

* Mon Feb 17 2025 Jonny Heggheim <hegjon@gmail.com> - 0.7.5-1
- Initial package
