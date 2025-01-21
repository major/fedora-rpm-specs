Name:		shelldap
Version:	1.5.1
Release:	13%{?dist}
Summary:	A shell-like interface for browsing LDAP servers

# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
URL:		https://github.com/mahlonsmith/%{name}
Source0:	%{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildArch: noarch
BuildRequires:	coreutils perl-generators perl-interpreter perl(Config) perl-podlators
# perl-generators takes care of the 'Requires' tag.
Recommends:	perl(IO::Socket::SSL) perl(Authen::SASL) perl(Term::ReadLine::Gnu)

%description
A handy shell-like interface for browsing LDAP servers and editing their
content. It keeps command history, has sane auto-completion, credential caching,
site-wide and individual configurations.

%prep
%setup -q
/usr/bin/perl -MConfig -i -pe 's{^#!/usr/bin/env perl}{$Config{startperl}}' %{name}

%build
pod2man shelldap > shelldap.1
/usr/bin/perl -n -e 'if(m/^#/){print if($. > 4)}else{exit 0}' shelldap > LICENSE.txt

%install
/usr/bin/mkdir -p %{buildroot}/%{_bindir}
/usr/bin/mkdir -p %{buildroot}/%{_mandir}/man1
/usr/bin/install -p -m 755 shelldap %{buildroot}%{_bindir}/shelldap
/usr/bin/install -p -m 644 shelldap.1 %{buildroot}%{_mandir}/man1/shelldap.1

%files
%license LICENSE.txt
%{_bindir}/shelldap
%{_mandir}/man1/shelldap.1.*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.5.1-12
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Feb 06 2022 Emmanuel Seyman <emmanuel@seyman.fr> - 1.5.1-6
- Update URL to point to Github (#2050955)

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Apr 26 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 1.5.1-1
- Update to 1.5.1

* Sun Apr 26 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 1.4.0-6
- Add coreutils to BuildRequires (for mkdir and install)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 27 2018 Timothée Floure <fnux@fedoraproject.org> - 1.4.0-1
- Let there be package.
