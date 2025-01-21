Name:		xtrlock
URL:		https://salsa.debian.org/debian/xtrlock
Version:	2.16
Release:	2%{?dist}
License:	GPL-3.0-or-later
Summary:	Minimal X display lock program
Source0:	%{url}/-/archive/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	libX11-devel
BuildRequires:	libxcrypt-devel
BuildRequires:	libcap-devel

%description
Xtrlock is a very minimal X display lock program. It doesn't
obscure the screen, it is completely idle while the display is locked
and you don't type at it, and it doesn't do funny things to the X
access control lists.

%prep
%autosetup -p1

%build
%make_build -f Makefile.noimake CFLAGS="-DSHADOW_PWD=1 -DLIBCAP=1 %{build_cflags}" \
  LDLIBS="-lcap -lX11 -lcrypt"

%install
%make_install install.man -f Makefile.noimake BINDIR=%{_bindir}

%files
%license GPL-3.txt
%doc xtrlock.service
# it requires CAP_DAC_READ_SEARCH for password hash read
%caps(cap_dac_read_search=pe) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1x*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jan  6 2025 Jaroslav Škarvada <jskarvad@redhat.com> - 2.16-1
- New version
  Resolves: rhbz#2335525

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Mar  6 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 2.15-1
- Initial version
