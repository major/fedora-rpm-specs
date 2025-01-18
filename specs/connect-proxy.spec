Name:           connect-proxy
Version:        1.105
Release:        4%{?dist}
Summary:        SSH Proxy command helper

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.taiyo.co.jp/~gotoh/ssh/connect.html
Source0:        ssh-connect-%{version}.tar.gz
# Real source listed below, it was renamed for sanity's sake
#Source0:       https://github.com/gotoh/ssh-connect/archive/refs/tags/1.105-tar.gz
Source1:        connect-proxy.1
Patch0:         connect-proxy-1.105-socklen.patch

Requires:       openssh

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  add-determinism
%description
connect-proxy is the simple relaying command to make network connection via
SOCKS and https proxy. It is mainly intended to be used as proxy command
of OpenSSH. You can make SSH session beyond the firewall with this command.

Features of connect-proxy are:

    * Supports SOCKS (version 4/4a/5) and https CONNECT method.
    * Supports NO-AUTH and USERPASS authentication of SOCKS
    * Partially supports telnet proxy (experimental).
    * You can input password from tty, ssh-askpass or environment variable.
    * Simple and general program independent from OpenSSH.
    * You can also relay local socket stream instead of standard I/O.

%prep
%setup -q -n ssh-connect-%{version}
%patch -P 0 -p1

%build
make CFLAGS="$RPM_OPT_FLAGS" %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
cp connect $RPM_BUILD_ROOT/%{_bindir}/connect-proxy
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1/

%files
%doc doc/manual.html
%{_mandir}/man1/*
%{_bindir}/%{name}

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.105-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul  25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.105-3
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.105-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri May 17 2024 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 1.105-1
- Update to upstream 1.105

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.100-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.100-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.100-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.100-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec  6 2022 Florian Weimer <fweimer@redhat.com> - 1.100-27
- Port to C99 (#2151093)

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.100-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.100-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.100-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.100-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.100-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.100-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.100-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.100-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.100-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.100-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.100-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.100-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.100-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.100-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.100-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.100-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.100-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.100-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.100-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.100-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.100-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.100-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.100-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.100-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jul 15 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.100-2
- fix license tag

* Wed Feb 13 2008 Jarod Wilson <jwilson@redhat.com> 1.100-1
- Upgrade to r100.

* Tue Sep 05 2006 Jarod Wilson <jwilson@redhat.com> 1.95-5
- Rebuild for new glibc

* Wed Jul 05 2006 Jarod Wilson <jwilson@redhat.com> 1.95-4
- Minor spec cleanups
- Add copy of html doc page

* Wed Jul 05 2006 Jarod Wilson <jwilson@redhat.com> 1.95-3
- Rename source file with version for sanity's sake

* Wed Jul 05 2006 Jarod Wilson <jwilson@redhat.com> 1.95-2
- Fix BuildRoot and enable CFLAGS

* Wed Jul 05 2006 Jarod Wilson <jwilson@redhat.com> 1.95-1
- Initial build for Fedora Extras

* Wed Dec 12 2005 Jarod Wilson <jarod@wilsonet.com> 1.93-1
- Initial build
