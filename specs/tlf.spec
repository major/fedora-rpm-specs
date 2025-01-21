# LTO breaks unit tests
%global _lto_cflags %nil

Name:		tlf
Version:	1.4.1
Release:	18%{?dist}
Summary:	Ham radio contest logger
# GPLv3+ are some m4 macros
# Automatically converted from old format: GPLv2+ and GPLv3+ - review is highly recommended.
License:	GPL-2.0-or-later AND GPL-3.0-or-later
URL:		https://github.com/Tlf/tlf
Source0:	%{url}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
Source1:	%{url}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz.sig
Source2:	tlf-release-key.asc
ExcludeArch:    i686
BuildRequires:	gnupg2
BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	glib2-devel
BuildRequires:	ncurses-devel
BuildRequires:	hamlib-devel
BuildRequires:	xmlrpc-c-devel
BuildRequires:	libcmocka-devel
# autoconf, automake can be dropped when the FSF patch is dropped
BuildRequires:	autoconf
BuildRequires:	automake
Recommends:	xplanet
Recommends:	sox
Recommends:	cwdaemon
# Backported from upstream
Patch0:		tlf-1.4.1-hamlib-4.2-build-fix.patch
# Fixed FSF address, updated license to the current license text
# https://github.com/Tlf/tlf/pull/270
Patch1:		tlf-1.4.1-fsf-address-fix.patch
# Already fixed upstream, but different way which is not easily backportable,
# no upstream release yet
Patch2:		tlf-1.4.1-format-security-fix.patch
Patch3:		tlf-c99.patch

%description
Tlf is a console (ncurses) mode general purpose CW/VOICE keyer,
logging and contest program for hamradio. It supports the CQWW,
the WPX, the ARRL-DX , the ARRL-FD, the PACC and the EU SPRINT
contests (single operator) as well as a LOT MORE basic contests,
general QSO and DXpedition mode.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
# it can be dropped when the FSF patch is dropped
autoreconf -fi
%configure --enable-fldigi-xmlrpc
%make_build

%install
%make_install

%check
cd test
make check

%files
%doc AUTHORS ChangeLog NEWS README.md
%doc %{_docdir}/%{name}/*
%license COPYING
%{_bindir}/tlf
%{_bindir}/play_vk
%{_bindir}/soundlog
%{_datadir}/%{name}
%{_mandir}/man1/*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Dec 31 2024 Richard Shaw <hobbes1069@gmail.com> - 1.4.1-17
- Rebuild for Hamlib 4.6.

* Wed Aug 07 2024 Miroslav Suchý <msuchy@redhat.com> - 1.4.1-16
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 15 2022 Florian Weimer <fweimer@redhat.com> - 1.4.1-11
- Apply upstream patch to improve C99 compatibility

* Mon Nov 07 2022 Richard Shaw <hobbes1069@gmail.com> - 1.4.1-10
- Rebuild for updated hamlib 4.5.

* Thu Aug  4 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 1.4.1-9
- Fixed FTBFS
  Resolves: rhbz#2113745

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 23 2021 Richard Shaw <hobbes1069@gmail.com> - 1.4.1-6
- Rebuild for hamlib 4.4.

* Thu Dec 23 2021 Richard Shaw <hobbes1069@gmail.com> - 1.4.1-5
- 36-build-side-49086

* Tue Oct 12 2021 Richard Shaw <hobbes1069@gmail.com> - 1.4.1-4
- Rebuild for hamlib 4.3.1.

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jul  7 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 1.4.1-2
- Updated according to the review
  Related: rhbz#1979096

* Sun Jul  4 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 1.4.1-1
- Initial version
