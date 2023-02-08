Name:			Rex
Version:		1.14.0
Release:		0%{?dist}
Summary:		The friendly automation framework on basis of Perl

License:		ASL 2.0
URL:			https://www.rexify.org/
Source0:		https://cpan.metacpan.org/authors/id/F/FE/FERKI/%{name}-%{version}.tar.gz

BuildArch:		noarch


Requires:		perl(Data::Validate::IP)
Requires:		perl(Net::SSH2)
Requires:		perl(Net::OpenSSH)
Requires:		perl(Net::SFTP::Foreign)
Requires:		perl(Parallel::ForkManager)

BuildRequires:  make

BuildRequires:	perl-generators perl-interpreter
BuildRequires:	perl(attributes)
BuildRequires:	perl(autodie)
BuildRequires:	perl(AWS::Signature4)
BuildRequires:	perl(base)
BuildRequires:	perl(Carp)
BuildRequires:	perl(constant)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(Data::Validate::IP)
BuildRequires:	perl(DBI)
Buildrequires:	perl(Devel::Caller)
Buildrequires:	perl(Digest::HMAC_SHA1)
Buildrequires:	perl(Digest::MD5)
Buildrequires:	perl(English)
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:	perl(Exporter)
BuildRequires:	perl(Fcntl)
Buildrequires:	perl(File::Basename)
Buildrequires:	perl(File::Spec)
Buildrequires:	perl(File::Spec::Unix)
Buildrequires:	perl(File::Spec::Win32)
Buildrequires:	perl(File::ShareDir)
Buildrequires:	perl(File::ShareDir::Install)
Buildrequires:	perl(File::Temp)
Buildrequires:	perl(FindBin)
Buildrequires:	perl(Hash::Merge)
Buildrequires:	perl(HTTP::Request::Common)
Buildrequires:	perl(IO::File)
Buildrequires:	perl(IO::Select)
Buildrequires:	perl(IO::Socket)
Buildrequires:	perl(IO::String)
Buildrequires:	perl(IPC::Open3)
BuildRequires:	perl(JSON::MaybeXS)
BuildRequires:	perl(lib)
Buildrequires:	perl(List::MoreUtils)
Buildrequires:	perl(List::Util)
Buildrequires:	perl(LWP::UserAgent)
Buildrequires:	perl(MIME::Base64)
BuildRequires:	perl(Module::Metadata)
Buildrequires:	perl(Net::OpenSSH::ShellQuoter)
BuildRequires:	perl(Net::SFTP::Foreign)
BuildRequires:	perl(overload)
BuildRequires:	perl(Parallel::ForkManager)
BuildRequires:	perl(POSIX)
Buildrequires:	perl(Scalar::Util)
Buildrequires:	perl(Sort::Naturally)
Buildrequires:	perl(Storable)
Buildrequires:	perl(strict)
Buildrequires:	perl(String::Escape)
Buildrequires:	perl(Sub::Override)
Buildrequires:	perl(Symbol)
Buildrequires:	perl(Term::ReadKey)
Buildrequires:	perl(Test::Builder::Module)
BuildRequires:	perl(Test::Deep)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Output)
BuildRequires:	perl(Test::mysqld)
BuildRequires:	perl(Test::UseAllModules)
Buildrequires:	perl(Text::Glob)
Buildrequires:	perl(Text::Wrap)
Buildrequires:	perl(Time::HiRes)
Buildrequires:	perl(UNIVERSAL)
Buildrequires:	perl(vars)
Buildrequires:	perl(version)
Buildrequires:	perl(warnings)
BuildRequires:	perl(XML::LibXML)
Buildrequires:	perl(XML::Simple)
Buildrequires:	perl(YAML)


%description
(R)?ex(ify) is the friendly automation framework on basis of the Perl scripting
language. You can use it in your everyday DevOps life for:

	* Continous Delivery
	* Configuration Management
	* Automation
	* Cloud Deployment
	* Virtualization
	* Software Rollout
	* Server Provisioning

It's friendly to any combinations of local and remote execution, push and pull
style of management, or imperative and declarative approach. Instead of forcing
any specific model on you, it trusts you to be in the best position to decide
what to automate and how, allowing you to build the automation tool your
situation requires.

Rex runs locally, even if managing remotes via SSH. This means it's instantly
usable, without big rollout processes or anyone else to convince, making it
ideal and friendly for incremental automation.


%prep
%setup -q %{name}-%{version}


%build
perl Makefile.PL INSTALLDIRS=vendor NO_PERLLOCAL=1 NO_PACKLIST=1
make %{?_smp_mflags}


%check
make test


%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

chmod 755 $RPM_BUILD_ROOT/%{perl_vendorlib}/%{name}/Commands/templates/append_if_no_such_line.tpl.pl
sed -i "s|/usr/bin/env perl|/usr/bin/perl|" $RPM_BUILD_ROOT/%{_bindir}/rex

%{_fixperms} -c $RPM_BUILD_ROOT


%files
%doc ChangeLog CONTRIBUTORS README
%license LICENSE
%{_mandir}/man1/rex.1*
%{_mandir}/man1/rexify.1*
%{_mandir}/man3/%{name}*
%attr(644, root, root) %{perl_vendorlib}/%{name}.pm
%attr(644, root, root) %{perl_vendorlib}/auto/share/dist/%{name}/
%{perl_vendorlib}/%{name}/
%attr(755, root, root) %{_bindir}/rex
%attr(755, root, root) %{_bindir}/rexify


%changelog
* Mon Feb 06 2023 Dominic Hopf <dmaphy@fedoraproject.org> - 1.14.0-1
- Update to 1.14.0 (#2167207)

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.13.4-4
- Perl 5.36 rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul 08 2021 Dominic Hopf <dmaphy@fedoraproject.org> - 1.13.4-1
- Update to 1.13.4 (#1979408)

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.13.3-2
- Perl 5.34 rebuild

* Sat Mar 06 2021 Dominic Hopf <dmaphy@fedoraproject.org> - 1.13.3-1
- Update to 1.13.3 (#1936026)

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 05 2020 Dominic Hopf <dmaphy@fedoraproject.org> - 1.13.2-1
- Update to 1.13.2 (#1904724)

* Fri Nov 06 2020 Dominic Hopf <dmaphy@fedoraproject.org> - 1.13.1-1
- Upgrade to Rex 1.13.1

* Tue Oct 06 2020 Dominic Hopf <dmaphy@fedoraproject.org> - 1.13.0-1
- Upgrade to Rex 1.13.0

* Sat Sep 05 2020 Dominic Hopf <dmaphy@fedoraproject.org> - 1.12.2-1
- Upgrade to Rex 1.12.2

* Sun Aug 09 2020 Dominic Hopf <dmaphy@fedoraproject.org> - 1.12.1-1
- Upgrade to Rex 1.12.1

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 06 2020 Dominic Hopf <dmaphy@fedoraproject.org> - 1.12.0-1
- Upgrade to Rex 1.12.0

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.11.0-2
- Perl 5.32 rebuild

* Fri Jun 05 2020 Dominic Hopf <dmaphy@fedoraproject.org> - 1.11.0-1
- Upgrade to Rex 1.11.0

* Wed May 06 2020 Dominic Hopf <dmaphy@fedoraproject.org> - 1.10.0-1
- Upgrade to Rex 1.10.0

* Mon Apr 06 2020 Dominic Hopf <dmaphy@fedoraproject.org> - 1.9.0-1
- Upgrade to Rex 1.9.0

* Wed Apr 01 2020 Petr Pisar <ppisar@redhat.com> - 1.8.2-2
- Specify all dependencies

* Sat Mar 07 2020 Dominic Hopf <dmaphy@fedoraproject.org> - 1.8.2-1
- Upgrade to Rex 1.8.2

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.5.0-7
- Perl 5.30 rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.5.0-4
- Perl 5.28 rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 01 2017 Dominic Hopf <dmaphy@fedoraproject.org> - 1.5.0-2
- Upgrade to Rex 1.5.0
- Fix wrong-script-interpreter issue

* Mon Jul 31 2017 Dominic Hopf <dmaphy@fedoraproject.org> - 1.4.1-6
- Remove explicit Requires: perl(AWS::Signature4)
- Change mode for append_if_no_such_line.tpl.pl in %%build section
- Do not explicitly install documentation
- Add Requires for: Net::OpenSSH, Net::SFTP::Foreign, Net::SSH2 and
  Parallel::ForkManager
- Improve legibility of Requires and BuildRequires

* Sun Jul 30 2017 Dominic Hopf <dmaphy@fedoraproject.org> - 1.4.1-5
- Add Requires: perl(AWS::Signature4)

* Sat Jul 29 2017 Dominic Hopf <dmaphy@fedoraproject.org> - 1.4.1-4
- Remove BuildRequires on perl
- Add BuildRequires on Test::Pod
- Do not define LICENSE as %%doc
- Do not explictly define manpages as %%doc
- Replace make install command with make pure_install command
- chmod +x for append_if_no_such_line.tpl.pl

* Thu Jul 27 2017 Dominic Hopf <dmaphy@fedoraproject.org> - 1.4.1-3
- Install Rex into %%{perl_vendorlib}
- Add BuildRequires for perl-generators and perl-interpreter as of Guidelines
- Add Requires for versioned MODULE_COMPAT stuff as of Guidelines
- Use make install instead of %%makeinstall macro in %%install section
- Install documentation files to /usr/share/doc/Rex/ and mark LICENSE as
  %%license

* Mon Jul 24 2017 Dominic Hopf <dmaphy@fedoraproject.org> - 1.4.1-2
- Update to 1.4.1
- Add BuildRequires for: Devel::Caller, IO::String, Test::Deep, Test::mysqld
  and Time::HiRes

* Thu Jun 25 2015 Dominic Hopf <dmaphy@fedoraproject.org> - 1.3.1-1
- Update to 1.3.1

* Tue May 05 2015 Dominic Hopf <dmaphy@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1

* Mon Apr 06 2015 Dominic Hopf <dmaphy@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0

* Thu Nov 13 2014 Dominic Hopf <dmaphy@fedoraproject.org> - 0.55.3-1
- Update to 0.55.3

* Sat Oct 04 2014 Dominic Hopf <dmaphy@fedoraproject.org> - 0.54.3-1
- Update to 0.54.3

* Wed Jul 16 2014 Dominic Hopf <dmaphy@fedoraproject.org> - 0.49.1-1
- initial package
