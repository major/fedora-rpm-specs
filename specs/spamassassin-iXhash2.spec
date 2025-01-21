%global pkgname iXhash2

Summary:        SpamAssassin plugin to lookup e-mail checksums in blacklists
Name:           spamassassin-%{pkgname}
Version:        4.00
Release:        3%{?dist}
License:        Apache-2.0
URL:            https://mailfud.org/%{pkgname}/
Source0:        https://mailfud.org/%{pkgname}/%{pkgname}-%{version}.tar.gz
Source1:        spamassassin-iXhash2.eml
Patch0:         spamassassin-iXhash2-4.00-conf.patch
Requires:       spamassassin >= 4.0.0
Provides:       spamassassin-iXhash = 1.5.5-2
Obsoletes:      spamassassin-iXhash < 1.5.5-2
BuildRequires:  %{_bindir}/perldoc
BuildRequires:  perl-generators
BuildArch:      noarch

%description
iXhash2 is an unofficial improved version of the iXhash spam filter
plugin for SpamAssassin, adding async DNS lookups for performance and
removing unneeded features but fully compatible with the iXhash 1.5.5
(https://sourceforge.net/projects/ixhash/) implementation. It computes
MD5 checksums of fragments of the body of an e-mail and compares them
to those of known spam using DNS queries to a RBL-like name server. So
it works similar to the standard plugins that use the Pyzor, Razor and
DCC software packages from within SpamAssassin.

%prep
%setup -q -n %{pkgname}-%{version}
%patch -P0 -p1 -b .conf
cp -pf %{SOURCE1} iXhash2.eml

%build

%install
install -D -p -m 644 %{pkgname}.cf $RPM_BUILD_ROOT%{_sysconfdir}/mail/spamassassin/%{pkgname}.cf
touch -c -r %{pkgname}.cf.conf $RPM_BUILD_ROOT%{_sysconfdir}/mail/spamassassin/%{pkgname}.cf
install -D -p -m 644 %{pkgname}.pm $RPM_BUILD_ROOT%{perl_vendorlib}/Mail/SpamAssassin/Plugin/%{pkgname}.pm
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man3/
perldoc %{pkgname}.pm > $RPM_BUILD_ROOT%{_mandir}/man3/Mail::SpamAssassin::Plugin::%{pkgname}.3pm

%files
%license LICENSE
%doc CHANGELOG README iXhash2.eml
%config(noreplace) %{_sysconfdir}/mail/spamassassin/%{pkgname}.cf
%{perl_vendorlib}/Mail/SpamAssassin/Plugin/%{pkgname}.pm
%{_mandir}/man3/*.3pm*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.00-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.00-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Mar 01 2024 Robert Scheck <robert@fedoraproject.org> 4.00-1
- Upgrade to 4.00 (#2222974)

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.05-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.05-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.05-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.05-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.05-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.05-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.05-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.05-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.05-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.05-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.05-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.05-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.05-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 06 2017 Robert Scheck <robert@fedoraproject.org> 2.05-12
- Remove retired iXhash blacklists from default configuration

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.05-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.05-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.05-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.05-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.05-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.05-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 2.05-5
- Perl 5.18 rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.05-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.05-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jul 12 2012 Robert Scheck <robert@fedoraproject.org> 2.05-2
- Added missing perldoc requirement (#838327 #c3)

* Sun Jul 08 2012 Robert Scheck <robert@fedoraproject.org> 2.05-1
- Switched to iXhash2 2.05 (#838327)

* Fri Nov 12 2010 Robert Scheck <robert@fedoraproject.org> 1.5.5-1
- Upgrade to 1.5.5
- Initial spec file for Fedora and Red Hat Enterprise Linux
