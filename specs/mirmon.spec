Name:           mirmon
Version:        2.11
Release:        20%{?dist}
Summary:        Monitor the status of mirrors
License:        MIT
URL:            http://www.staff.science.uu.nl/~penni101/mirmon/
Source0:        http://www.staff.science.uu.nl/~penni101/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}-httpd.conf
BuildArch:      noarch
BuildRequires:  perl-generators

%description
Many software projects are mirrored worldwide. The mirror sites are required 
to update the mirror archive regularly (daily, weekly) from a root server.

Mirmon helps administrators in keeping an eye on the mirror sites. In a 
concise graphic format, mirmon shows each site's status history of the 
last two weeks. It is easy to spot stale or dead mirrors.

%package        httpd
Summary:        Apache configuration for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       httpd

%description    httpd
This package provides the Apache configuration for
applications using an Alias to %{name}.

%prep
%autosetup

%build
# Nothing to build.

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_mandir}/man1
install -pm644 %{name}.1 %{buildroot}%{_mandir}/man1/
install -pm644 %{name}.pm.1 %{buildroot}%{_mandir}/man1/
install -pDm755 %{name} %{buildroot}%{_bindir}/%{name}
install -pDm755 probe %{buildroot}%{_bindir}/probe
install -pDm0644 %{S:1} %{buildroot}%{_sysconfdir}/httpd/conf.d/%{name}.conf
cp -pa countries.list icons %{buildroot}%{_datadir}/%{name}/

%files
%license LICENSE
%doc RELEASE-NOTES *.{txt,html}
%{_bindir}/%{name}
%{_bindir}/probe
%{_datadir}/%{name}
%{_mandir}/man1/%{name}*.1*

%files httpd
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 07 2023 Robby Callicotte <rcallicotte@fedoraproject.org> - 2.11-15
- Updated license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 30 2016 Sérgio Basto <sergio@serjux.com> - 2.11-1
- New upstream vesion, 2.11

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 22 2014 Christopher Meng <rpm@cicku.me> - 2.10-1
- Update to 2.10

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug 13 2013 Christopher Meng <rpm@cicku.me> - 2.9-1
- Update to 2.9

* Sat Aug 10 2013 Christopher Meng <rpm@cicku.me> - 2.8-2
- Replace macro outside rpm.

* Thu Feb 14 2013 Christopher Meng <rpm@cicku.me> - 2.8-1
- Update to 2.8

* Thu Dec 20 2012 Christopher Meng <rpm@cicku.me> - 2.7-1
- Update to 2.7

* Tue Jun 12 2012 Christopher Meng <rpm@cicku.me> - 2.6-1
- Update to 2.6

* Mon Apr 30 2012 Christopher Meng <rpm@cicku.me> - 2.5-1
- Update to 2.5

* Mon Mar 21 2011 Christopher Meng <cickumqt-NOSPAM@gmail.com> - 2.4-1
- Update to 2.4

* Wed Mar 17 2010 Christopher Meng <cickumqt-NOSPAM@gmail.com> - 2.3-1
- Update to 2.3

* Sun Mar 14 2010 Christopher Meng <cickumqt-NOSPAM@gmail.com> - 2.2-1
- Update to 2.2

* Mon Feb 15 2010 Christopher Meng <cickumqt-NOSPAM@gmail.com> - 2.1-1
- Update to 2.1

* Fri Jan 15 2010 Christopher Meng <cickumqt-NOSPAM@gmail.com> - 2.0-1
- Initial Package.
