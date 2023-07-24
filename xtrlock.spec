Name:		xtrlock
URL:		https://salsa.debian.org/debian/xtrlock
Version:	2.15
Release:	2%{?dist}
License:	GPL-3.0-or-later
Summary:	Minimal X display lock program
Source0:	%{url}/-/archive/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	libX11-devel
BuildRequires:	libxcrypt-devel
BuildRequires:	libcap-devel
# https://salsa.debian.org/debian/xtrlock/-/merge_requests/3
Patch0:		xtrlock-2.15-distro-fix.patch
# https://salsa.debian.org/debian/xtrlock/-/merge_requests/2
Patch1:		xtrlock-2.15-capabilities-drop.patch

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
* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Mar  6 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 2.15-1
- Initial version
