Summary:        Compact and feature-rich WordStar-compatible editor
Name:           jupp
Version:        41
Release:        8%{?dist}
# jupp itself is GPL-1.0-only but uses other source codes, breakdown:
# BSD-3-Clause: popen.inc
# ISC: strlfun.inc
# MirOS: {compat,win32}.c and jupprc and strlfun.inc and types.h
# Unicode-DFS-2016: i18n.c
License:        GPL-1.0-only AND BSD-3-Clause AND ISC AND MirOS AND Unicode-DFS-2016
URL:            https://www.mirbsd.org/jupp.htm
Source0:        https://www.mirbsd.org/MirOS/dist/%{name}/joe-3.1%{name}%{version}.tgz
Patch0:         jupp-configure-c99.patch
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  libselinux-devel

%description
Jupp is a compact and feature-rich WordStar-compatible editor and also the
MirOS fork of the JOE 3.x editor which provides easy conversion for former
PC users as well as powerfulness for programmers, while not doing annoying
things like word wrap "automagically". It can double as a hex editor and
comes with a character map plus Unicode support. Additionally it contains
an extension to visibly display tabs and spaces, has a cleaned up, extended
and beautified options menu, more CUA style key-bindings, an improved math
functionality and a bracketed paste mode automatically used with Xterm.

%prep
%autosetup -p1 -n %{name}

%build
chmod +x configure
export CFLAGS="$CFLAGS -std=gnu11"  # http://www.mirbsd.org/jupp.htm#build
%configure --disable-termidx --sysconfdir=%{_sysconfdir}/%{name}
%make_build sysconfjoesubdir=

%install
%make_install sysconfjoesubdir=

# Some cleanups to be done by upstream for future releases
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/{jmacs,joe,jpico,jstar,rjoe}rc
rm -f $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}/{jmacs,jpico,jstar,jupp,rjoe}*
mv -f $RPM_BUILD_ROOT%{_bindir}/{joe,%{name}}
mv -f $RPM_BUILD_ROOT%{_mandir}/man1/{joe,%{name}}.1

%files
%license COPYING
%doc HINTS INFO LIST NEWS README
%dir %{_sysconfdir}/%{name}/
%config(noreplace) %{_sysconfdir}/%{name}/%{name}rc
%dir %{_sysconfdir}/%{name}/charmaps/
%config(noreplace) %{_sysconfdir}/%{name}/charmaps/*
%dir %{_sysconfdir}/%{name}/syntax/
%config(noreplace) %{_sysconfdir}/%{name}/syntax/*
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 41-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 41-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 41-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 41-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 41-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Feb 09 2023 Florian Weimer <fweimer@redhat.com> - 41-3
- Port configure script to C99

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 41-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Oct 01 2022 Robert Scheck <robert@fedoraproject.org> 41-1
- Upgrade to 41 (#2131420)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 40-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 40-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 40-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 29 2020 Robert Scheck <robert@fedoraproject.org> 40-1
- Upgrade to 40

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 38-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 38-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 38-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 11 2018 Robert Scheck <robert@fedoraproject.org> 38-1
- Upgrade to 38

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 32-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 25 2017 Robert Scheck <robert@fedoraproject.org> 32-1
- Upgrade to 32

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 30-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 06 2017 Robert Scheck <robert@fedoraproject.org> 30-1
- Upgrade to 30

* Tue Nov 01 2016 Robert Scheck <robert@fedoraproject.org> 29-1
- Upgrade to 29

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Oct 23 2014 Robert Scheck <robert@fedoraproject.org> 28-1
- Upgrade to 28

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 03 2014 Robert Scheck <robert@fedoraproject.org> 27-1
- Upgrade to 27

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Dec 27 2013 Robert Scheck <robert@fedoraproject.org> 26-1
- Upgrade to 26

* Tue Mar 19 2013 Robert Scheck <robert@fedoraproject.org> 24-1
- Upgrade to 24
- Initial spec file for Fedora and Red Hat Enterprise Linux
