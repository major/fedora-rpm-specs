
Name:		srcpd
Version:	2.1.7
Release:	4%{?dist}
Summary:	Simple Railroad Command Protocol (SRCP) server

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:	GPL-2.0-only
URL:		http://srcpd.sourceforge.net/
Source0:	http://sourceforge.net/projects/srcpd/files/srcpd/%{version}/srcpd-%{version}.tar.bz2
Source1:	srcpd.service

Patch0:		srcpd-2.1.6-io-conditional.patch

BuildRequires:		make
BuildRequires:		gcc
BuildRequires:		libxml2-devel

Requires(post):		systemd
Requires(preun):	systemd
Requires(postun):	systemd
BuildRequires:		systemd


%description
Simple Railroad Command Protocol (SRCP) is a communication protocol designed
to integrate various models of railroad systems. The srcpd acts a gateway
between any kind of model railway systems and user interface programs that
support SRCP. IANA assigned TCP port 4303 to it.


%prep
%autosetup


%build
%configure
%make_build


%install
%make_install
%find_lang %{name} --with-man --all-name

install -Dpm 0644 %SOURCE1 %{buildroot}/%{_unitdir}/srcpd.service
rm -rf %{buildroot}/%{_sysconfdir}/udev
install -Dpm 0644 10-liusb.rules %{buildroot}/%{_udevrulesdir}/10-liusb.rules


%post
%systemd_post %{name}.service
exit 0


%preun
%systemd_preun %{name}.service
exit 0


%postun
%systemd_postun_with_restart %{name}.service
exit 0


%files -f %{name}.lang
%doc AUTHORS ChangeLog DESIGN NEWS PROGRAMMING-HOWTO TODO
%doc README README.loconet README.selectrix
%license COPYING
%config(noreplace) %{_sysconfdir}/srcpd.conf
%config(noreplace) %{_udevrulesdir}/10-liusb.rules
%{_unitdir}/%{name}.service
%{_sbindir}/srcpd
%{_mandir}/man5/*.5*
%{_mandir}/man8/*.8*


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 2.1.7-3
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri May 03 2024 Denis Fateyev <denis@fateyev.com> - 2.1.7-1
- Update to 2.1.7 release
- Remove obsolete patch

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Apr 06 2023 Denis Fateyev <denis@fateyev.com> - 2.1.6-1
- Update to 2.1.6 release
- Update build patches

* Mon Feb 06 2023 Florian Weimer <fweimer@redhat.com> - 2.1.5-9
- Port configure script to C99

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.1.5-4
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 12 2020 Denis Fateyev <denis@fateyev.com> - 2.1.5-1
- Update to 2.1.5 release
- Removed deprecated build options and patches

* Fri Feb 28 2020 Denis Fateyev <denis@fateyev.com> - 2.1.3-13
- Add "legacy_common_support" build option

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Oct 26 2019 Denis Fateyev <denis@fateyev.com> - 2.1.3-11
- Modernize package spec

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.3-7
- Escape macros in %%changelog

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 09 2015 Denis Fateyev <denis@fateyev.com> - 2.1.3-1
- Update to 2.1.3 release

* Sat Dec 06 2014 Denis Fateyev <denis@fateyev.com> - 2.1.2-6
- Conditional build for ddls88 plugin

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 30 2014 Jakub Čajka <jcajka@redhat.com> - 2.1.2-4
- Changed exclude to exclusive arch %%{ix86} %%{arm} x86_64

* Fri Jun 27 2014 Denis Fateyev <denis@fateyev.com> - 2.1.2-3
- Exclude ppc, ppc64 arch from build

* Thu Jun 26 2014 Denis Fateyev <denis@fateyev.com> - 2.1.2-2
- Package spec cleanup

* Sat Feb 08 2014 Denis Fateyev <denis@fateyev.com> - 2.1.2-1
- Initial Fedora RPM release
