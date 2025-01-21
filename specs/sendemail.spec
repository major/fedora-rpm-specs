Summary:        Lightweight command line SMTP e-mail client
Name:           sendemail
Version:        1.56
Release:        16%{?dist}
License:        GPL-2.0-or-later
URL:            http://caspian.dotconf.net/menu/Software/SendEmail/
Source0:        http://caspian.dotconf.net/menu/Software/SendEmail/sendEmail-v%{version}.tar.gz
Source1:        sendemail.1
Patch0:         sendemail-1.56-fix_ssl_version.patch
Patch1:         sendemail-1.56-add-ipv6-support.patch
Patch2:         sendemail-1.56-local-sendmail.patch
BuildArch:      noarch
BuildRequires:  perl-generators
Requires:       perl(IO::Socket::SSL)
Provides:       sendEmail = %{version}-%{release}

%description
SendEmail is a lightweight, completely command line based, SMTP e-mail
client. It was designed to be used in bash scripts, batch files, Perl
programs and web sites, but is also quite useful in many other contexts.

SendEmail is written in Perl and is unique in that it requires no special
modules. It has a straight forward interface, making it very easy to use.

%prep
%setup -q -n sendEmail-v%{version}
%patch -P0 -p1 -b .fix_ssl_version
%patch -P1 -p1 -b .add-ipv6-support
%patch -P2 -p1 -b .local-sendmail

%build
# Empty build section, most likely nothing required.

%install
install -D -p -m 0755 sendEmail $RPM_BUILD_ROOT%{_bindir}/%{name}
install -D -p -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1
ln -s %{name} $RPM_BUILD_ROOT%{_bindir}/sendEmail
ln -s %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/sendEmail.1

%files
%doc CHANGELOG README
%{_bindir}/%{name}
%{_bindir}/sendEmail
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/sendEmail.1*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.56-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.56-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.56-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.56-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.56-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.56-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.56-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.56-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.56-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.56-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.56-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.56-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.56-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.56-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.56-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 06 2017 Robert Scheck <robert@fedoraproject.org> 1.56-1
- Upgrade to 1.56
- Initial spec file for Fedora and Red Hat Enterprise Linux
