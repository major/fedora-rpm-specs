%if 0%{?fedora} <= 14
%define pvendorlib %{perl_privlib}
%endif
%if 0%{?fedora} >= 15
%define pvendorlib %{perl_vendorlib}
%endif
%if 0%{?rhel} >= 5
%define pvendorlib %{perl_vendorlib}
%endif

Name:           perl-Net-SSH-Expect
Version:        1.09
Release:        42%{?dist}
Summary:        Net-SSH-Expect - SSH wrapper to execute remote commands

License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Net-SSH-Expect
Source0:        https://cpan.metacpan.org/authors/id/B/BN/BNEGRAO/Net-SSH-Expect-%{version}.tar.gz
BuildArch:      noarch

BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Expect)
BuildRequires:  perl(fields)
BuildRequires:  perl(Test::More)


%description
This module is a wrapper to the *ssh* executable that is available in
your system's *$PATH*. Use this module to execute commands on the
remote SSH server. It authenticates with the user and password you
passed in the constructor's attributes "user" and "password".

Once an ssh connection was started using the "connect()" method it will
remain open until you call the "close()" method. This allows you execute
as many commands as you want with the "exec()" method using only one
connection. This is a better approach over other ssh wrapper
implementations, i.e: Net::SCP, Net::SSH and Net::SCP::Expect, that
start a new ssh connection each time a remote command is issued or a
file is transfered.

It uses *Expect.pm* module to interact with the SSH server. A
"get_expect()" method is provided so you can obtain the internal
"Expect" object connected to the SSH server. Use this only if you have
some special need that you can't do with the "exec()" method.

This module was inspired by Net::SCP::Expect 
<http://search.cpan.org/~djberg/Net-SCP-Expect-0.12/Expect.pm>
and by Net::Telnet and some of its methods work the same as these two
modules.

%prep
%setup -q -n Net-SSH-Expect-%{version}

%build
PERL5_CPANPLUS_IS_RUNNING=1 %{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} 

%check
%{__make} test

%install
rm -rf %{buildroot}
%{__make} pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} ';' 2>/dev/null

%files
%{_mandir}/man3/Net::SSH::Expect.3pm.gz
%{pvendorlib}/Net
%{pvendorlib}/Net/SSH
%{pvendorlib}/Net/SSH/Expect.pm
%{pvendorlib}/Net/SSH/Expect.pod

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.09-40
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.09-37
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.09-34
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.09-31
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.09-28
- Perl 5.28 rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.09-27
- Escape macros in %%changelog

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.09-24
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.09-22
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.09-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.09-19
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.09-18
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.09-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug 28 2013 Carl Thompson <fedora@red-dragon.com> - 1.09-16
- fixed permissions in %%files section

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.09-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 1.09-14
- Perl 5.18 rebuild

* Tue May 14 2013 Carl Thopmson <fedora@red-dragon.com> - 1.09-13
- added ownership to directories

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.09-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.09-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 1.09-10
- Perl 5.16 rebuild
- Specify all dependencies

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.09-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 24 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.09-8
- Perl mass rebuild

* Fri Jun 24 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.09-7
- Perl mass rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.09-6
- Perl mass rebuild

* Fri Mar 4 2011 Carl Thompson <fedora@red-dragon.com> 1.09-5
- fixed a typo in the spec file

* Thu Mar 3 2011 Carl Thompson <fedora@red-dragon.com> 1.09-4
- updated the spec to remove some legacy components
- added PERL5_CPANPLUS_IS_RUNNING=1 to prevent package from pulling
- from CPAN

* Wed Mar 2 2011 Carl Thompson <fedora@red-dragon.com> 1.09-3
- fixed an error in the if statements testing distro for definition

* Wed Mar 2 2011 Carl Thompson <fedora@red-dragon.com> 1.09-2
- cleaned up the spec file and used more macros

* Tue Mar 1 2011 Carl Thompson <fedora@red-dragon.com> 1.09-1
- Initial build.

