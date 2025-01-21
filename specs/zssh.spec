Name:           zssh
Version:        1.5c
Release:        19%{?dist}
Summary:        SSH and Telnet client with ZMODEM file transfer capability
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            http://zssh.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/zssh/zssh/1.5/%{name}-%{version}.tgz
# patches from https://sources.debian.org/patches/zssh/1.5c.debian.1-7/
Patch0:         https://sources.debian.org/data/main/z/zssh/1.5c.debian.1-7/debian/patches/0001-Remove-build-instruction-about-lrzsz.patch
Patch1:         https://sources.debian.org/data/main/z/zssh/1.5c.debian.1-7/debian/patches/0002-Install-files-into-under-DESTDIR.patch
Patch2:         https://sources.debian.org/data/main/z/zssh/1.5c.debian.1-7/debian/patches/0003-Do-not-symlink-zssh-to-ztelnet.patch
Patch3:         https://sources.debian.org/data/main/z/zssh/1.5c.debian.1-7/debian/patches/0004-Use-GNU-openpty-library-for-pty.h.patch
Patch4:         https://sources.debian.org/data/main/z/zssh/1.5c.debian.1-7/debian/patches/0005-Do-not-call-strip-in-build-process.patch
Patch5:         https://sources.debian.org/data/main/z/zssh/1.5c.debian.1-7/debian/patches/0006-replace-CPPFunction-call-with-rl_completion_func_t.patch
Patch6:         https://sources.debian.org/data/main/z/zssh/1.5c.debian.1-7/debian/patches/0007-Fix-typo-in-man-page-zssh.1.patch
Patch7:         https://sources.debian.org/data/main/z/zssh/1.5c.debian.1-7/debian/patches/0008-Strip-build-date-from-version-string-to-enable-repro.patch
Patch8:         zssh-c99.patch
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  readline-devel
BuildRequires:  ncurses-devel
BuildRequires:  autoconf
Requires:       lrzsz

%description
%{summary}.

%prep
%autosetup -p1
# remove bundled lrzsz
rm -fr lrzsz-0.12.20

%build
autoconf
%configure
%make_build

%install
mkdir -p %{buildroot}%{_bindir}/ %{buildroot}%{_mandir}/man1/
%make_install
rm %{buildroot}%{_mandir}/man1/ztelnet.1*

%files
%doc README
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5c-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.5c-18
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5c-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5c-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5c-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5c-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 17 2022 Florian Weimer <fweimer@redhat.com> - 1.5c-13
- Improve C99 compatibility

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5c-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5c-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5c-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5c-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5c-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5c-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 30 2019 Robin Lee <cheeselee@fedoraproject.org> - 1.5c-6
- Fix BR

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5c-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 13 2019 Robin Lee <cheeselee@fedoraproject.org> - 1.5c-4
- Port patches from Debian (BZ#1716106)
- Requires lrzsz

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.5c-3
- Rebuild for readline 8.0

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5c-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec  7 2017 mosquito <sensor.wen@gmail.com> - 1.5c-1
- Initial package build
