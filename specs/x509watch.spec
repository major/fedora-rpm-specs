Summary:          Simple tool to list expiring or expired X.509 certificates
Name:             x509watch
Version:          0.6.1
Release:          18%{?dist}
License:          GPL-2.0-or-later
URL:              https://ftp.robert-scheck.de/linux/%{name}/
Source:           https://ftp.robert-scheck.de/linux/%{name}/%{name}-%{version}.tar.gz
Requires:         %{_bindir}/openssl
Requires:         %{_sbindir}/sendmail
Requires(post):   systemd >= 197
Requires(preun):  systemd >= 197
Requires(postun): systemd >= 197
BuildRequires:    systemd >= 197
BuildRequires:    make
BuildRequires:    perl-generators
BuildArch:        noarch

%description
x509watch is a simple command line application, written in Perl, that can be
used to list soon expiring or already expired X.509 certificates, such as e.g.
SSL certificates. All certificates are searched by default in the standard PKI
directory, but any other directory can be specified as parameter. Only Base64
encoded DER and PEM X.509 certificates are supported.

%prep
%setup -q

%build

%install
%make_install

%post
%systemd_post %{name}.timer

%preun
%systemd_preun %{name}.timer

%postun
%systemd_postun %{name}.timer

%files
%license COPYING
%doc ChangeLog README
%{_bindir}/%{name}
%{_libexecdir}/%{name}
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}.timer
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 03 2019 Robert Scheck <robert@fedoraproject.org> 0.6.1-6
- Corrected systemd scriptlets usage (#1716408)

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Apr 30 2017 Robert Scheck <robert@fedoraproject.org> 0.6.1-1
- Upgrade to 0.6.1 (#1444969)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Nov 29 2013 Robert Scheck <robert@fedoraproject.org> 0.6.0-1
- Upgrade to 0.6.0 (#989128, #1000912, #1035370)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.5.0-5
- Perl 5.18 rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jun 26 2011 Robert Scheck <robert@fedoraproject.org> 0.5.0-1
- Upgrade to 0.5.0 (#698080)

* Thu Jun 02 2011 Robert Scheck <robert@fedoraproject.org> 0.4.0-1
- Upgrade to 0.4.0

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Aug 03 2010 Robert Scheck <robert@fedoraproject.org> 0.3.0-1
- Upgrade to 0.3.0

* Tue Jul 27 2010 Robert Scheck <robert@fedoraproject.org> 0.2.0-1
- Upgrade to 0.2.0 (#618059)

* Mon Jul 26 2010 Robert Scheck <robert@fedoraproject.org> 0.1.0-1
- Upgrade to 0.1.0
- Initial spec file for Fedora and Red Hat Enterprise Linux
