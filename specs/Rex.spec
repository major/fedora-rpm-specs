Name:			Rex
Version:		1.15.0
Release:		2%{?dist}
Summary:		The friendly automation framework on basis of Perl

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:		Apache-2.0
URL:			https://www.rexify.org/
Source0:		https://cpan.metacpan.org/authors/id/F/FE/FERKI/%{name}-%{version}.tar.gz

BuildArch:		noarch


Requires:		perl(Data::Validate::IP)
Requires:		perl(Net::SSH2)
Requires:		perl(Net::OpenSSH)
Requires:		perl(Net::SFTP::Foreign)
Requires:		perl(Parallel::ForkManager)

BuildRequires:  git make rsync

BuildRequires:	perl-generators perl-interpreter
BuildRequires:	perl(AWS::Signature4)
BuildRequires:	perl(Carp)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(DBI)
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(Data::Validate::IP)
BuildRequires:	perl(Devel::Caller)
BuildRequires:	perl(Digest::HMAC_SHA1)
BuildRequires:	perl(Digest::MD5)
BuildRequires:	perl(English)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:	perl(Fcntl)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::ShareDir)
BuildRequires:	perl(File::ShareDir::Install)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Spec::Unix)
BuildRequires:	perl(File::Spec::Win32)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(FindBin)
BuildRequires:	perl(HTTP::Request)
BuildRequires:	perl(HTTP::Request::Common)
BuildRequires:	perl(Hash::Merge)
BuildRequires:	perl(IO::File)
BuildRequires:	perl(IO::Select)
BuildRequires:	perl(IO::Socket)
BuildRequires:	perl(IO::String)
BuildRequires:	perl(IPC::Open3)
BuildRequires:	perl(JSON::MaybeXS)
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl(List::Util)
BuildRequires:	perl(MIME::Base64)
BuildRequires:	perl(Module::Load::Conditional)
BuildRequires:	perl(Module::Metadata)
BuildRequires:	perl(Net::OpenSSH::ShellQuoter)
BuildRequires:	perl(Net::SFTP::Foreign)
BuildRequires:	perl(POSIX)
BuildRequires:	perl(Parallel::ForkManager)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Sort::Naturally)
BuildRequires:	perl(Storable)
BuildRequires:	perl(String::Escape)
BuildRequires:	perl(Sub::Override)
BuildRequires:	perl(Symbol)
BuildRequires:	perl(Term::ANSIColor)
BuildRequires:	perl(Term::ReadKey)
BuildRequires:	perl(Test::Builder::Module)
BuildRequires:	perl(Test::Deep)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Output)
BuildRequires:	perl(Test::UseAllModules)
BuildRequires:	perl(Test::Warnings)
BuildRequires:	perl(Test::mysqld)
BuildRequires:	perl(Text::Glob)
BuildRequires:	perl(Text::Wrap)
BuildRequires:	perl(Time::HiRes)
BuildRequires:	perl(UNIVERSAL)
BuildRequires:	perl(URI)
BuildRequires:	perl(URI::QueryParam)
BuildRequires:	perl(XML::LibXML)
BuildRequires:	perl(XML::Simple)
BuildRequires:	perl(YAML)
BuildRequires:	perl(attributes)
BuildRequires:	perl(autodie)
BuildRequires:	perl(base)
BuildRequires:	perl(constant)
BuildRequires:	perl(if)
BuildRequires:	perl(lib)
BuildRequires:	perl(overload)
BuildRequires:	perl(strict)
BuildRequires:	perl(vars)
BuildRequires:	perl(version)
BuildRequires:	perl(warnings)

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
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Nov 06 2024 Dominic Hopf <dmaphy@fedoraproject.org> - 1.15.0-1
- Update to 1.15.0 (#2323989)

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 1.14.3-6
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 29 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Aug 07 2023 Dominic Hopf <dmaphy@fedoraproject.org> - 1.14.3-1
- Update to 1.14.3 (#2229419)

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.2-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue May 30 2023 Dominic Hopf <dmaphy@fedoraproject.org> - 1.14.2-1
- Update to 1.14.2 (#2175551)

* Mon Mar 06 2023 Dominic Hopf <dmaphy@fedoraproject.org> - 1.14.1-1
- Update to 1.14.1 (#2175551)

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
