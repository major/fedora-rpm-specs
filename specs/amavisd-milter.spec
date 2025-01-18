Summary:        Sendmail milter for amavisd-new using the AM.PDP protocol
Name:           amavisd-milter
Version:        1.7.2
Release:        9%{?dist}
# ISC (compat/strlcpy.c) and BSD-3-Clause (the rest)
License:        BSD-3-Clause AND ISC
URL:            https://github.com/prehor/amavisd-milter
Source0:        https://github.com/prehor/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        amavisd-milter.service
Source2:        amavisd-milter.sysconfig
BuildRequires:  gcc
BuildRequires:  make
%if 0%{?fedora} || 0%{?rhel} > 7
BuildRequires:  sendmail-milter-devel >= 8.12.0
BuildRequires:  systemd-rpm-macros
%else
BuildRequires:  sendmail-devel >= 8.12.0
BuildRequires:  systemd
%endif
%{?systemd_requires}
Requires:       amavisd-new

%description
The amavisd-milter is a sendmail milter (mail filter) for amavisd-new
2.4.3 (and above) and sendmail 8.13 (and above) which use the new AM.PDP
protocol.

Run 'usermod -a -G amavis postfix' when using Postfix and amavisd-milter
via the unix socket.

%prep
%setup -q

%build
%configure \
  --localstatedir=/run/amavisd \
  --with-working-dir=%{_localstatedir}/spool/amavisd/tmp
%make_build

%install
%make_install

# Install systemd unit file
install -D -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/%{name}
install -D -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/%{name}.service

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license LICENSE
%doc CHANGES
%{_sbindir}/%{name}
%{_unitdir}/%{name}.service
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_mandir}/man8/%{name}.8*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 04 2022 Robert Scheck <robert@fedoraproject.org> 1.7.2-1
- Upgrade to 1.7.2 (#2036828)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.7.1-3
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 14 2020 Robert Scheck <robert@fedoraproject.org> 1.7.1-1
- Upgrade to 1.7.1 (#1878910)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 22 2020 Robert Scheck <robert@fedoraproject.org> 1.7.0-1
- Upgrade to 1.7.0 (#1824332)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 15 2017 Robert Scheck <robert@fedoraproject.org> 1.6.1-1
- Upgrade to 1.6.1
- Initial spec file for Fedora and Red Hat Enterprise Linux
