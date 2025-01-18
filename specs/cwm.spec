Summary: Calm Window Manager by OpenBSD project
Name: cwm
Version: 7.4
Release: 4%{?dist}
# The entire source code is licensed under ISC license,
# except queue.h which is BSD
# Automatically converted from old format: ISC and BSD - review is highly recommended.
License: ISC AND LicenseRef-Callaway-BSD
Url: https://github.com/chneukirchen/cwm
Source0: http://chneukirchen.org/releases/%{name}-%{version}.tar.gz
Source1: %{name}.desktop
Source2: LICENSE
BuildRequires: gcc
BuildRequires: pkgconf
BuildRequires: byacc
BuildRequires: libX11-devel
BuildRequires: libXrandr-devel
BuildRequires: libXinerama
BuildRequires: libXft-devel
BuildRequires: make

%description
cwm (calm window manager) is a window manager for X11 which contains many
features that concentrate on the efficiency and transparency of window
management, while maintaining the simplest and most pleasant aesthetic.

This package contains a Linux port of the official project, which changes the
source for the port portion but doesn't touches the original functionality
provided by the original OpenBSD's project.

%prep
%setup -q
cp -a %{SOURCE2} .

%build
# The Makefile provides a default CFLAGS but RPM overrides it, without
# the -D_GNU_SOURCE
%{set_build_flags}
CFLAGS="$CFLAGS -D_GNU_SOURCE"
make %{?_smp_mflags}

%install
%{set_build_flags}
CFLAGS="$CFLAGS -D_GNU_SOURCE"
make PREFIX=%{_prefix} DESTDIR=%{buildroot} install
install -d %{buildroot}/%{_datadir}/xsessions
install -m 644 %{SOURCE1} %{buildroot}/%{_datadir}/xsessions

%files
%doc README
%license LICENSE
%{_bindir}/*
%{_datadir}/xsessions/*
%{_mandir}/man1/*
%{_mandir}/man5/*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 7.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 7.4-3
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Feb 26 2024 Bruno Meneguele <bmeneg@heredoc.io> - 7.4-1
- New upstream release (RHBZ#2244513)

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 27 2023 DJ Delorie <dj@redhat.com> - 7.1-4
- Fix C99 compatibility issue

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri May 13 2022 Bruno Meneguele <bmeneguele@gmail.com> - 7.1-1
- New upstream release (RHBZ#2080730)
- Make source files live in the lookaside cache instead of git

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 11 2020 Bruno Meneguele <bmeneg@redhat.com> - 6.7-1
- New upstream release

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Bruno E. O. Meneguele <bmeneguele@gmail.com> - 6.3-4
- Add build requirement for gcc, since it was removed from buildroot and mock
  (BZ#1603731)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 17 2018 Bruno E. O. Meneguele <bmeneguele@gmail.com> - 6.3-2
- New source file

* Thu May 17 2018 Bruno E. O. Meneguele <bmeneguele@gmail.com> - 6.3-1
- New upstream (OpenBSD) package release

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 13 2017 Bruno E. O. Meneguele <bmeneguele@gmail.com> - 6.2-1
- Initial package
