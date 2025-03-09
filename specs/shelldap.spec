Name:		shelldap
Version:	1.5.2
Release:	%autorelease
Summary:	A shell-like interface for browsing LDAP servers

# Automatically converted from old format: BSD - review is highly recommended.
License:	BSD-3-Clause
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
%autochangelog
