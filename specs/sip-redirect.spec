Summary:           Tiny IPv4 and IPv6 SIP redirect server written in Perl
Summary(de):       Ein winziger, in Perl geschriebener, SIP Redirekt-Server
Name:              sip-redirect
Version:           0.2.0
Release:           23%{?dist}
License:           GPL-2.0-or-later
URL:               https://ftp.robert-scheck.de/linux/%{name}/
Source0:           https://ftp.robert-scheck.de/linux/%{name}/%{name}-%{version}.tar.gz
Source1:           sip-redirect.sysusersd
BuildArch:         noarch
BuildRequires:     make
BuildRequires:     perl-generators
BuildRequires:     systemd
BuildRequires:     systemd-rpm-macros
Requires:          logrotate
Requires:          perl(Socket) >= 1.95
%{?systemd_requires}
%{?sysusers_requires_compat}

%description
sip-redirect is a tiny SIP redirect server written in Perl. It is IPv4 and
IPv6 capable, but the IPv6 support is optional. The RFC 3261 was the base for
this simple and very configurable implementation. There is neither TCP nor
multicast support programmed in.

%description -l de
sip-redirect ist ein winziger, in Perl geschriebener, SIP Redirekt-Server. Er
unterstützt IPv4 und IPv6, aber der IPv6-Support ist optional. Als Grundlage
für diese einfache und sehr konfigurierbare Implementation wurde die RFC 3261
verwendet. Es wurde keine Unterstützung für TCP und für Multicast eingebaut.

%prep
%setup -q

%build

%install
%make_install

# Declarative allocation of system users and groups
install -D -p -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysusersdir}/%{name}.conf

%pre
%sysusers_create_compat %{SOURCE1}

%post
touch %{_localstatedir}/log/%{name} > /dev/null 2>&1 || :
chown sip:sip %{_localstatedir}/log/%{name} > /dev/null 2>&1 || :
chmod 0640 %{_localstatedir}/log/%{name} > /dev/null 2>&1 || :
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license COPYING
%doc ChangeLog README
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%{_sysusersdir}/%{name}.conf
%config(noreplace) %{_sysconfdir}/%{name}.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%ghost %attr(0640,sip,sip) %{_localstatedir}/log/%{name}

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Jul 31 2022 Robert Scheck <robert@fedoraproject.org> 0.2.0-18
- Added sysusers.d file to achieve user() and group() provides

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.2.0-14
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 03 2019 Robert Scheck <robert@fedoraproject.org> 0.2.0-9
- Corrected systemd scriptlets usage (#1716388)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Nov 29 2014 Robert Scheck <robert@fedoraproject.org> 0.2.0-1
- Upgrade to 0.2.0

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.1.2-9
- Perl 5.18 rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Robert Scheck <robert@fedoraproject.org> 0.1.2-3
- Rebuild against rpm 4.6

* Thu Nov 06 2008 Robert Scheck <robert@fedoraproject.org> 0.1.2-2
- Changes to match with Fedora Packaging Guidelines (#443675)

* Tue Apr 22 2008 Robert Scheck <robert@fedoraproject.org> 0.1.2-1
- Upgrade to 0.1.2

* Wed Oct 25 2006 Robert Scheck <robert@fedoraproject.org> 0.1.1-1
- Upgrade to 0.1.1

* Sat Jul 08 2006 Robert Scheck <robert@fedoraproject.org> 0.1.0-1
- Upgrade to 0.1.0
- Initial spec file for Fedora Core and Red Hat Enterprise Linux
