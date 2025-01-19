Name:           perl-App-Nopaste
Version:        1.013
Release:        17%{?dist}
Summary:        Easy access to any pastebin
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/App-Nopaste
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/App-Nopaste-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(CPAN::Meta::Requirements) >= 2.120620
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Class::Load)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long::Descriptive)
BuildRequires:  perl(JSON)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(WWW::Mechanize)
BuildRequires:  perl(namespace::clean)
# Tests only
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(LWP::Protocol)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Trap)
BuildRequires:  perl(version)
# for ssh plugin
Requires:       /usr/bin/scp
Requires:       perl(Clipboard)
Requires:       perl(Browser::Open)
Requires:       perl(WWW::Pastebin::PastebinCom::Create)
Requires:       perl(HTTP::Request::Common)

%description
Pastebins (also known as nopaste sites) let you post text, usually code,
for public viewing. They're used a lot in IRC channels to show code that
would normally be too long to give directly in the channel (hence the
name nopaste).

%package -n nopaste
# needs to beat old nopaste-2835-3
Epoch:          1
Summary:        Access pastebins from the command line
Requires:       %{name} = 0:%{version}-%{release}

%description -n nopaste
This application lets you post text to pastebins from the command line.

Pastebins (also known as nopaste sites) let you post text, usually code, for
public viewing. They're used a lot in IRC channels to show code that would
normally be too long to give directly in the channel (hence the name nopaste).


%prep
%setup -q -n App-Nopaste-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 </dev/null
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes CONTRIBUTING README
%license LICENSE
%dir %{perl_vendorlib}/App
%{perl_vendorlib}/App/Nopaste*
%{_mandir}/man3/App::Nopaste*

%files -n nopaste
%{_bindir}/nopaste
%{_mandir}/man1/nopaste.*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.013-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.013-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.013-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.013-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.013-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.013-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Petr Pisar <ppisar@redhat.com> - 1.013-11
- Convert a License tag to an SPDX format

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.013-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.013-9
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.013-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.013-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.013-6
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.013-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.013-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.013-3
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.013-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jul 28 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 1.013-1
- Update to 1.013

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.012-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.012-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.012-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 15 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 1.012-1
- Update to 1.012

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.011-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.011-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.011-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 27 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 1.011-1
- Update to 1.011

* Sun Aug 06 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 1.010-1
- Update to 1.010

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.009-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.009-2
- Perl 5.26 rebuild

* Sun Apr 23 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 1.009-1
- Update to 1.009

* Sat Mar 04 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 1.008-1
- Update to 1.008

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.007-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Sep 18 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 1.007-1
- Update to 1.007

* Tue May 31 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 1.006-1
- Update to 1.006

* Sat May 21 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 1.005-1
- Update to 1.005

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.004-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.004-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.004-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.004-2
- Perl 5.22 rebuild

* Sun Mar 08 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 1.004-1
- Update to 1.004

* Sun Jan 04 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 1.003-1
- Update to 1.003

* Fri Dec 19 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 1.002-1
- Update to 1.002

* Sun Dec 14 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 1.001-1
- Update to 1.001

* Thu Dec 11 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 0.99-1
- Update to 0.99

* Sat Nov 22 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 0.98-1
- Update to 0.98
- Add the %%license tag
- Tighten file listing

* Fri Nov 07 2014 Petr Šabata <contyk@redhat.com> - 0.96-1
- 0.96 bump

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.90-6
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Petr Pisar <ppisar@redhat.com> - 0.90-4
- Perl 5.18 rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 02 2012 Iain Arnell <iarnell@gmail.com> 1:0.90-1
- update to latest upstream version

* Sat Jul 21 2012 Iain Arnell <iarnell@gmail.com> 1:0.35-1
- update to latest upstream version
- BR inc::Module::Install

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.33-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 23 2012 Petr Pisar <ppisar@redhat.com> - 0.33-2
- Perl 5.16 rebuild

* Thu Jan 05 2012 Iain Arnell <iarnell@gmail.com> 0.33-1
- update to latest upstream version

* Sat Oct 22 2011 Iain Arnell <iarnell@gmail.com> 0.32-1
- update to latest upstream version

* Fri Sep 23 2011 Iain Arnell <iarnell@gmail.com> 1:0.31-1
- update to latest upstream version
- drop defattr in files sections

* Sat Aug 27 2011 Iain Arnell <iarnell@gmail.com> 1:0.30-1
- update to latest upstream version

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 0.28-2
- Perl mass rebuild

* Sat Apr 09 2011 Iain Arnell <iarnell@gmail.com> 1:0.28-1
- update to latest upstream version

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 15 2011 Iain Arnell <iarnell@gmail.com> 0.25-1
- update to latest upstream version

* Sun Jan 02 2011 Iain Arnell <iarnell@gmail.com> 0.24-1
- update to latest upstream version
- clean up spec for modern rpmbuild

* Fri Dec 03 2010 Iain Arnell <iarnell@gmail.com> 0.23-1
- update to latest upstream version

* Tue Jun 15 2010 Iain Arnell <iarnell@gmail.com> 0.22-1
- update to latest upstream

* Sat May 08 2010 Iain Arnell - 0.21-2
- bump for rebuild with perl-5.12.0

* Sat May 01 2010 Iain Arnell <iarnell@gmail.com> 0.21-1
- update to latest upstream

* Thu Apr 29 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.20-2
- Mass rebuild with perl-5.12.0

* Sun Apr 18 2010 Iain Arnell <iarnell@gmail.com> 0.20-1
- update to latest upstream version

* Thu Feb 25 2010 Iain Arnell <iarnell@gmail.com> 0.19-1
- update to latest upstream version

* Mon Jan 04 2010 Iain Arnell <iarnell@gmail.com> 0.18-1
- update to latest upstream version (adds ssh support)

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.17-2
- rebuild against perl 5.10.1

* Sat Nov 07 2009 Iain Arnell <iarnell@gmail.com> 0.17-1
- update to latest upstream version (fixes Gist support better)

* Sun Oct 18 2009 Iain Arnell <iarnell@gmail.com> 0.16-1
- update to latest upstream version (fixes rt#50500 Gist support)

* Fri Jul 31 2009 Iain Arnell <iarnell@gmail.com> 0.15-1
- update to latest upstream version

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jun 21 2009 Iain Arnell <iarnell@gmail.com> 0.11-2
- pretend that CPANPLUS is running

* Sun Jun 21 2009 Iain Arnell <iarnell@gmail.com> 0.11-1
- update to latest upstream version

* Thu Jun 18 2009 Iain Arnell <iarnell@gmail.com> 0.10-4
- don't require Git since Config::INI::Reader is sufficient
- don't require WWW::Pastebin::RafbNet::Create since rafb.net is gone

* Sat Jun 06 2009 Iain Arnell <iarnell@gmail.com> 0.10-3
- nopaste gets its own subpackage (to replace existing nopaste pacakge now that
  rafb.net has gone)

* Sun May 03 2009 Iain Arnell <iarnell@gmail.com> 0.10-2
- rename nopaste command to avoid conflict with existing nopaste rpm

* Sun Apr 19 2009 Iain Arnell <iarnell@gmail.com> 0.10-1
- Specfile autogenerated by cpanspec 1.77.
- add requires for optional modules
- add bindir and man1 to files
