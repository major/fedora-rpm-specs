Name:           perl-Mail-Box-IMAP4
Version:        3.008
Release:        5%{?dist}
Summary:        Handle IMAP4 folders as client
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Mail-Box-IMAP4
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARKOV/Mail-Box-IMAP4-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(IO::Handle)
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Date::Parse)
BuildRequires:  perl(Digest::HMAC_MD5)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(IO::Socket::IP)
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Mail::Box::Manage::User) >= 3
BuildRequires:  perl(Mail::Box::Net) >= 3
BuildRequires:  perl(Mail::Box::Net::Message)
BuildRequires:  perl(Mail::Box::Parser::Perl)
BuildRequires:  perl(Mail::Box::Search) >= 3
BuildRequires:  perl(Mail::IMAPClient)
BuildRequires:  perl(Mail::Message::Head)
BuildRequires:  perl(Mail::Message::Head::Complete) >= 3
BuildRequires:  perl(Mail::Message::Head::Delayed) >= 3
BuildRequires:  perl(Mail::Transport::Receive) >= 3
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(File::Temp) >= 0.19
BuildRequires:  perl(Mail::Box::Identity)
BuildRequires:  perl(Mail::Box::MH)
BuildRequires:  perl(Mail::Box::Test) >= 3
BuildRequires:  perl(Mail::Message) >= 3.013
BuildRequires:  perl(Mail::Message::Body::Lines) >= 3
BuildRequires:  perl(Test::More)
Requires:       perl(Mail::Box) >= 3.007
Requires:       perl(Mail::Box::Net) >= 3
Requires:       perl(Mail::IMAPClient) >= 3.42
Requires:       perl(Mail::Message::Body::Lines) >= 3
Requires:       perl(Mail::Message::Head::Complete) >= 3
Requires:       perl(Mail::Message::Head::Delayed) >= 3
Requires:       perl(Mail::Transport::Receive) >= 3.004

Conflicts:      perl-Mail-Box < 3

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Mail::Box::Manage::User\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Mail::IMAPClient\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Mail::Box::(Net|Search|Test)\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Mail::Message(::Body::Lines|::Head::Complete|::Head::Delayed|)\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Mail::(Server|Transport::Receive)\\)$

%description
Maintain a folder which has its messages stored on a remote server. The
communication between the client application and the server is implemented
using the IMAP4 protocol.

%package -n perl-Mail-Server-IMAP4
Summary:        IMAP4 server implementation
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Requires:       perl(Mail::Box::Manage::User) >= 3
Requires:       perl(Mail::Box::Search) >= 3
Requires:       perl(Mail::Server) >= 3

%description -n perl-Mail-Server-IMAP4
This module is a place-holder, which can be used to grow code which is
needed to implement a full IMAP4 server.
The server implementation is not completed.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Mail-Server-IMAP4 = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Mail::Box::Test) >= 3
Requires:       perl(Mail::Message) >= 3.013
Requires:       perl(Mail::Message::Body::Lines) >= 3

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%autosetup -p1 -n Mail-Box-IMAP4-%{version}
# Remove tests that are always skipped
for F in t/10client-read.t t/11client-write.t; do
    rm "$F"
    perl -i -ne 'print $_ unless m{\Q'"$F"'\E}' MANIFEST
done
# Correct shebangs
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc ChangeLog README
%dir %{perl_vendorlib}/Mail
%{perl_vendorlib}/Mail/Box
%{perl_vendorlib}/Mail/Transport
%{_mandir}/man3/Mail::Box::*
%{_mandir}/man3/Mail::Transport::*

%files -n perl-Mail-Server-IMAP4
%dir %{perl_vendorlib}/Mail
%dir %{perl_vendorlib}/Mail/Server
%{perl_vendorlib}/Mail/Server/IMAP4*
%{_mandir}/man3/Mail::Server::IMAP4*

%files tests
%{_libexecdir}/%{name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.008-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.008-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.008-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.008-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Aug 21 2023 Jitka Plesnikova <jplesnik@redhat.com> - 3.008-1
- 3.008 bump (bug #2230299)

* Thu Aug 03 2023 Petr Pisar <ppisar@redhat.com> - 3.007-14
- Adapt tests to Mail-Message-3.013 (bug #2225452)
- Specify all dependencies
- Package the tests

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.007-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.007-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.007-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 3.007-10
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.007-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.007-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 3.007-7
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.007-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.007-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 3.007-4
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.007-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.007-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 17 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.007-1
- 3.007 bump

* Thu Jun 13 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.006-1
- 3.006 bump

* Thu Jun 06 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.005-1
- 3.005 bump

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.004-2
- Perl 5.30 rebuild

* Fri May 03 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.004-1
- 3.004 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.003-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.003-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.003-2
- Perl 5.28 rebuild

* Mon Mar 05 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.003-1
- 3.003 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.002-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.002-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 30 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.002-1
- 3.002 bump

* Wed Jun 28 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.001-1
- Initial release
