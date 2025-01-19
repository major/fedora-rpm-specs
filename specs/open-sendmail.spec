%global sendmailcf %{_datadir}/sendmail-cf

Summary:        Additional m4 files used to generate sendmail.cf
Name:           open-sendmail
Version:        0
Release:        0.25.20090107cvs%{?dist}
# Automatically converted from old format: Sendmail - review is highly recommended.
License:        Sendmail-8.23
URL:            http://open-sendmail.sourceforge.net/
# cvs -z3 -d:pserver:anonymous@open-sendmail.cvs.sourceforge.net:/cvsroot/open-sendmail co -D "20090107 23:59" open-sendmail
# find open-sendmail -type f -name .cvsignore -exec rm -f {} ';'
# find open-sendmail -type d -name CVS -exec rm -rf {} 2>/dev/null ';'
# mv -f open-sendmail open-sendmail-0
Source0:        %{name}-%{version}.tar.bz2
Requires:       sendmail-cf
BuildArch:      noarch

%description
Open-Sendmail is the open development of additional m4 files
used to generate and enhance sendmail.cf. The project contains
sendmail goodies previously provided at anfi.homeunix.net and
additional items.

%prep
%setup -q

%build

%install
mkdir -p $RPM_BUILD_ROOT{%{sendmailcf}/{feature,mailer}/%{name},%{_datadir}/%{name}}

install -p -m 644 cf/feature/anfi/*.m4 $RPM_BUILD_ROOT%{sendmailcf}/feature/%{name}/
install -p -m 644 cf/mailer/anfi/*.m4 $RPM_BUILD_ROOT%{sendmailcf}/mailer/%{name}/
install -p -m 644 cf/m4/*.patch $RPM_BUILD_ROOT%{_datadir}/%{name}/

ln -sf %{name}/require_rdns.m4 $RPM_BUILD_ROOT%{sendmailcf}/feature/require_rdns2.m4

%files
%doc cf/INSTALL.rtcyrus3 cf/MC.rtcyrus3
%{sendmailcf}/feature/require_rdns2.m4
%{sendmailcf}/feature/%{name}/
%{sendmailcf}/mailer/%{name}/
%{_datadir}/%{name}/

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.25.20090107cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 07 2024 Miroslav Suchý <msuchy@redhat.com> - 0-0.24.20090107cvs
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.23.20090107cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.22.20090107cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.21.20090107cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20.20090107cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.19.20090107cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.18.20090107cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.17.20090107cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16.20090107cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.15.20090107cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.20090107cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.20090107cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.20090107cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.20090107cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.20090107cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.20090107cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.20090107cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.20090107cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.20090107cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.20090107cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.20090107cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.3.20090107cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.2.20090107cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Oct 31 2010 Robert Scheck <robert@fedoraproject.org> 0-0.1.20090107cvs
- Upgrade to CVS 20090107
- Initial spec file for Fedora and Red Hat Enterprise Linux
