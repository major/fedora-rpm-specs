Summary:        Postfix policyd to combine complex restrictions in a ruleset
Name:           postfwd
Version:        2.03
Release:        11%{?dist}
License:        BSD-3-Clause
URL:            https://postfwd.org/
Source0:        https://github.com/postfwd/postfwd/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.service
Source2:        %{name}.sysconfig
Source3:        %{name}.tmpfilesd
Source4:        %{name}.sysusersd
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  systemd-rpm-macros
Requires:       perl(Digest::MD5)
Requires:       perl(Net::CIDR::Lite)
Requires:       perl(NetAddr::IP)
Requires:       perl(Storable)
Requires:       perl(Time::HiRes)
Requires:       %{_bindir}/more
Requires:       %{_bindir}/pod2text
%{?systemd_requires}
%{?sysusers_requires_compat}

%description
Postfwd is written in Perl to combine complex Postfix restrictions in a
ruleset similar to those of the most firewalls. The program uses the
Postfix policy delegation protocol to control access to the mail system
before a message has been accepted. It allows to choose an action (e.g.
reject, dunno) for a combination of several SMTP parameters (like sender
and recipient address, size or the client's TLS fingerprint).

%prep
%setup -q

%build

%install
mkdir -p $RPM_BUILD_ROOT{%{_localstatedir}/lib,%{_rundir}}/%{name}/
install -D -p -m 0755 sbin/%{name}3 $RPM_BUILD_ROOT%{_sbindir}/%{name}3
ln -s %{name}3 $RPM_BUILD_ROOT%{_sbindir}/%{name}
install -D -p -m 0640 etc/%{name}.cf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/%{name}.cf
install -D -p -m 0644 man/man8/%{name}3.8 $RPM_BUILD_ROOT%{_mandir}/man8/%{name}3.8
ln -sf %{name}3.8.gz $RPM_BUILD_ROOT%{_mandir}/man8/%{name}.8.gz
install -D -p -m 0755 tools/%{name}-client.pl $RPM_BUILD_ROOT%{_bindir}/%{name}-client
install -D -p -m 0755 tools/hapolicy/hapolicy $RPM_BUILD_ROOT%{_libexecdir}/%{name}/hapolicy
install -D -p -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/%{name}.service
install -D -p -m 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/%{name}
install -D -p -m 0644 %{SOURCE3} $RPM_BUILD_ROOT%{_tmpfilesdir}/%{name}.conf
install -D -p -m 0644 %{SOURCE4} $RPM_BUILD_ROOT%{_sysusersdir}/%{name}.conf

# Rename changelog for %%doc inclusion
mv -f doc/postfwd3.CHANGELOG CHANGELOG

%pre
%sysusers_create_compat %{SOURCE4}

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license doc/LICENSE
%doc README.md CHANGELOG {etc,plugins}/postfwd.*.sample*
%doc doc/{arch,quick}.html doc/postfwd-ARCH.png doc/postfwd3.{html,txt}
%doc tools/hapolicy/hapolicy.{html,txt} tools/hapolicy/hapolicy0?.png
%dir %attr(0750,root,%{name}) %{_sysconfdir}/%{name}/
%config(noreplace) %attr(0640,root,%{name}) %{_sysconfdir}/%{name}/%{name}.cf
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_unitdir}/%{name}.service
%{_sysusersdir}/%{name}.conf
%{_tmpfilesdir}/%{name}.conf
%{_bindir}/%{name}-client
%{_sbindir}/%{name}
%{_sbindir}/%{name}3
%dir %{_libexecdir}/%{name}/
%{_libexecdir}/%{name}/hapolicy
%{_mandir}/man8/%{name}.8*
%{_mandir}/man8/%{name}3.8*
%dir %attr(0750,%{name},%{name}) %{_rundir}/%{name}/
%dir %attr(0750,%{name},%{name}) %{_localstatedir}/lib/%{name}/

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.03-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.03-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.03-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.03-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.03-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.03-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 29 2022 Robert Scheck <robert@fedoraproject.org> 2.03-5
- Added sysusers.d file to achieve user() and group() provides

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 31 2021 Robert Scheck <robert@fedoraproject.org> 2.03-2
- Change to match with Fedora Packaging Guidelines (#1981585 #c1)

* Mon Jul 12 2021 Robert Scheck <robert@fedoraproject.org> 2.03-1
- Upgrade to 2.03 (#1981585)
- Initial spec file for Fedora and Red Hat Enterprise Linux
