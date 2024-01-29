Name:           sqlninja
Version:        0.2.999        
Release:        0.22.alpha1%{?dist}
Summary:        A tool for SQL server injection and takeover

License:        GPLv2+
URL:            http://sqlninja.sourceforge.net/index.html
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}-alpha1.tgz
Source1:        README.fedora
Patch0:         sqlninja-binary-upload-mode-fix-0.2.999-alpha1.patch
Patch1:         sqlninja-move-config-file-0.2.999-alpha1.patch
Patch2:         sqlninja-install-path-0.2.999-alpha1.patch
BuildArch:      noarch
BuildRequires:  perl-macros
#BuildRequires:  perl-generators

Requires:       perl-Net-DNS-Nameserver
Requires:       perl-Net-Pcap
Requires:       perl-IO-Socket-SSL
Requires:       perl-NetPacket
Requires:       perl-Net-RawIP
Requires:       perl-DBI
Requires:       perl-DBD-SQLite
Requires:       perl-interpreter

%description
Sqlninja is a tool targeted to exploit SQL Injection vulnerabilities on a web
application that uses Microsoft SQL Server as its back-end. Its main goal is
to provide remote access to vulnerable DB server.

%prep
%autosetup -n %{name}-%{version}-alpha1
cp %{SOURCE1} .

%build
# Patch path to language map in example config
sed -i.bak -E -e 's!lib/langs/!SqlNinja/langs/!' sqlninja.conf

%install
rm -rf %{buildroot}
install -Dp -m 0755 %{name} %{buildroot}%{_sbindir}/%{name}
install -pm 0755 -d %{buildroot}%{perl_vendorlib}/SqlNinja
install -pm 0755 -d %{buildroot}%{perl_vendorlib}/SqlNinja/langs
install -pm 0755 lib/*.pl %{buildroot}%{perl_vendorlib}/SqlNinja/
install -pm 0755 lib/langs/* %{buildroot}%{perl_vendorlib}/SqlNinja/langs/
install -pm 0755 -d %{buildroot}%{_sysconfdir}

%files
%doc LICENSE ChangeLog README sqlninja-howto.html README.fedora %{name}.conf
%{_sbindir}/%{name}
%dir %{perl_vendorlib}/SqlNinja
%{perl_vendorlib}/SqlNinja/

%changelog
* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.999-0.22.alpha1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Nov 06 2023 FeRD (Frank Dana) <ferdnyc@gmail.com> - 0.2.999-0.21.alpha1
- Install to %%perl_vendorlib instead of /usr/share/sqlninja
- Update patched paths for new install location
- Use autosetup to simplify spec file

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.999-0.20.alpha1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.999-0.19.alpha1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.999-0.18.alpha1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.999-0.17.alpha1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.999-0.16.alpha1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.999-0.15.alpha1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.999-0.14.alpha1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.999-0.13.alpha1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.999-0.12.alpha1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.999-0.11.alpha1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.999-0.10.alpha1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.999-0.9.alpha1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.999-0.8.alpha1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 13 2017 Petr Pisar <ppisar@redhat.com> - 0.2.999-0.7.alpha1
- perl dependency renamed to perl-interpreter
  <https://fedoraproject.org/wiki/Changes/perl_Package_to_Install_Core_Modules>

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.999-0.6.alpha1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.999-0.5.alpha1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.999-0.4.alpha1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Sep 26 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.999-0.3.alpha1
- Add additional patches

* Thu Sep 25 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.999-0.2.alpha1
- Update requirements

* Thu Sep 25 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.999-0.1.alpha1
- Update to latest upstream release 0.2.999-alpha1

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.2.6-4
- Perl 5.18 rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 21 2012 Arun SAG <sagarun@gmail.com> - 0.2.6-1
- Update to 0.2.6

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-0.3.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Sep 4 2011 Arun SAG <sagarun [AT] gmail dot com> p 0.2.6-0.2.rc2
- Update to new upstream release

* Sun Jul 3 2011 Arun SAG <sagarun [AT] gmail dot com> - 0.2.6-0.1.rc1
- Remove clean section
- Fix twise listed config file
- Fix license
- Update to 0.2.6-0.1.rc1

* Thu Sep 30 2010 Arun SAG <sagarun [AT] gmail dot com> - 0.2.5-2
- Pre-build binaries are no longer included 

* Sat Sep 25 2010 Arun SAG <sagarun [AT] gmail dot com> - 0.2.5-1
- First release
