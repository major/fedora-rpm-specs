Summary: A program for X11 protocol tracing
Name: x11trace
Version: 1.3.1
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL: http://xtrace.alioth.debian.org/

# Please set buildid below when building a private version of this rpm to
# differentiate it from the stock rpm.
#
# % global buildid .local

Release: 29%{?buildid}%{?dist}
Obsoletes: xtrace < 1.3.1-7

Source0: ftp://ftp.debian.org/debian/pool/main/x/xtrace/xtrace_%{version}.orig.tar.gz

# Bring the sources up to the head of the git master branch.
Patch1: x11trace-1.3.1-git-HEAD.patch

# AM_CONFIG_HEADER() is obsolete - use AC_CONFIG_HEADERS instead.
Patch2: x11trace-1.3.1-use-AC_CONFIG_HEADERS.patch

# Rename xtrace to x11trace
Patch3: x11trace-1.3.1-rename-to-x11trace.patch
Patch4: x11trace-1.3.1-rename-manpage.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires: automake autoconf
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: xorg-x11-proto-devel

%description
What strace is for system calls, x11trace is for X11 connections:
you hook it between one or more X11 clients and an X server and
it prints the requests going from client to server and the replies,
events and errors going the other way.

%prep
%setup -q -n xtrace-1.3.1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1

%build
autoreconf -i
%configure

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} INSTALL="install -p"

%files
%doc AUTHORS COPYING NEWS README
%{_bindir}/*
%{_datadir}/x11trace
%{_mandir}/man1/*


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.3.1-28
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 26 2014 David Howells <dhowells@redhat.com> - 1.3.1-7
- Fixed up review comments on the specfile.

* Thu Jun 26 2014 David Howells <dhowells@redhat.com> - 1.3.1-6
- Rename xtrace to x11trace.

* Fri Mar 28 2014 David Howells <dhowells@redhat.com> - 1.3.1-5
- Use % global rather than % define.

* Wed Mar 26 2014 David Howells <dhowells@redhat.com> - 1.3.1-4
- AM_CONFIG_HEADER is obsolete - use AC_CONFIG_HEADERS instead.

* Wed Feb 26 2014 David Howells <dhowells@redhat.com> - 1.3.1-3
- Rename the patch that brings the source up to date with git.
- Include derivation information in the patch.
- Fixed up review comments on the specfile.

* Fri Feb 21 2014 David Howells <dhowells@redhat.com> - 1.3.1-2
- Fixed up review comments on the specfile.

* Thu Feb 20 2014 David Howells <dhowells@redhat.com> - 1.3.1-1
- Initial packaging.
- Apply new changes from git as a patch.
