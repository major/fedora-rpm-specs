Name:           perl-Mail-Box-POP3
Version:        3.005
Release:        12%{?dist}
Summary:        Handle POP3 folders as client
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Mail-Box-POP3
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARKOV/Mail-Box-POP3-%{version}.tar.gz
Patch0:         Mail-Box-POP3-3.001-Use-IO-Socket-IP-to-support-IPv6.patch
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(:VERSION) >= 5.10
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(IO::Handle)
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(IO::Socket::IP)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Mail::Box::FastScalar) >= 3
BuildRequires:  perl(Mail::Box::Net) >= 3
BuildRequires:  perl(Mail::Box::Net::Message)
BuildRequires:  perl(Mail::Box::Parser::Perl) >= 3
BuildRequires:  perl(Mail::Transport::Receive) >= 3
BuildRequires:  perl(Socket)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Mail::Box::Test) >= 3
BuildRequires:  perl(Test::More)
Requires:       perl(IO::Socket::IP)
Requires:       perl(IO::Socket::SSL)
Requires:       perl(Mail::Box::FastScalar) >= 3
Requires:       perl(Mail::Box::Net) >= 3
Requires:       perl(Mail::Box::Parser::Perl) >= 3
Requires:       perl(Mail::Transport::Receive) >= 3


%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Mail::Box::FastScalar\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Mail::Box::(Net|Parser::Perl)\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Mail::Transport::Receive\\)$

%description
Maintain a folder which has its messages stored on a remote server. The
communication between the client application and the server is implemented
using the POP3 protocol. This class uses Mail::Transport::POP3 to hide the
transport of information, and focuses solely on the correct handling of
messages within a POP3 folder.

%prep
%setup -q -n Mail-Box-POP3-%{version}
%patch0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
MARKOV_DEVEL=1 make test

%files
%doc ChangeLog README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.005-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 3.005-11
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.005-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.005-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 3.005-8
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.005-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.005-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 3.005-5
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.005-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.005-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.005-2
- Perl 5.30 rebuild

* Fri May 03 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.005-1
- 3.005 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.004-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.004-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.004-2
- Perl 5.28 rebuild

* Mon Mar 05 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.004-1
- 3.004 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.003-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.003-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 17 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.003-1
- 3.003 bump

* Mon Jul 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.002-2
- Update the list of dependencies

* Fri Jun 30 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.002-1
- 3.002 bump

* Wed Jun 28 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.001-1
- Initial release
