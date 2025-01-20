Name:           perl-WWW-Search
Version:        2.519
Release:        16%{?dist}
Summary:        Virtual base class for WWW searches
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://metacpan.org/release/WWW-Search
Source0:        https://cpan.metacpan.org/authors/id/M/MT/MTHURN/WWW-Search-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Env)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::Scripts)
BuildRequires:  perl(Module::Install::WriteAll)
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Bit::Vector)
BuildRequires:  perl(Carp)
BuildRequires:  perl(CGI)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Date::Manip)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTML::TreeBuilder)
BuildRequires:  perl(HTTP::Cookies)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(HTTP::Status)
# LWP::Debug not used at tests
BuildRequires:  perl(LWP::MemberMixin)
BuildRequires:  perl(LWP::RobotUA)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Tests
BuildRequires:  perl(blib)
BuildRequires:  perl(ExtUtils::testlib)
# Getopt::Long not used
BuildRequires:  perl(IO::Capture::Stderr)
BuildRequires:  perl(Test::File)
# Optional tests
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
Requires:       perl(LWP::Debug)


%description
This class is the parent for all access methods supported by the WWW::Search
library. This library implements a Perl API to web-based search engines. See
README for a list of search engines currently supported, and for a lot of
interesting high-level information about this distribution. Search results can
be limited, and there is a pause between each request to avoid overloading
either the client or the server.


%prep
%setup -q -n WWW-Search-%{version}
# Remove bundled modules
rm -rf inc
sed -i -e '/^inc\//d' MANIFEST


%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}


%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*


%check
make test

%files
# LICENSE is empty
%doc Changes README
%{_bindir}/AutoSearch
%{_bindir}/WebSearch
%{perl_vendorlib}/*
%{_mandir}/man1/*Search.1.gz
%{_mandir}/man3/WWW::Search*3pm.gz


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.519-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 2.519-15
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.519-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.519-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.519-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.519-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.519-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.519-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.519-8
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.519-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.519-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.519-5
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.519-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.519-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.519-2
- Perl 5.32 rebuild

* Tue May 12 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.519-1
- 2.519 bump

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.517-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.517-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.517-8
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.517-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.517-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.517-5
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.517-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.517-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.517-2
- Perl 5.26 rebuild

* Wed May 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.517-1
- 2.517 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.516-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.516-1
- 2.516 bump

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.515-2
- Perl 5.24 rebuild

* Tue Mar 22 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.515-1
- 2.515 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.514-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 23 2015 Petr Pisar <ppisar@redhat.com> - 2.514-1
- 2.514 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.511-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 12 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.511-4
- Perl 5.22 rebuild

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.511-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.511-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 02 2013 Petr Pisar <ppisar@redhat.com> - 2.511-1
- 2.511 bump

* Fri Aug 02 2013 Petr Pisar <ppisar@redhat.com> - 2.508-10
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.508-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.508-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 20 2012 Petr Pisar <ppisar@redhat.com> - 2.508-7
- Perl 5.16 rebuild
- Specify all dependencies

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.508-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 2.508-5
- Perl mass rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 2.508-4
- Perl mass rebuild

* Sat May 14 2011 Iain Arnell <iarnell@gmail.com> 2.508-3
- Add perl(LWP::MemberMixin) and perl(LWP::UserAgent) to BuildRequires

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.508-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan  4 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.508-1
- update

* Thu Dec 23 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.507-7
- 661697 rebuild for fixing problems with vendorach/lib

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.507-6
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 2.507-5
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.507-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Feb 27 2009 Xavier Bachelot <xavier@bachelot.org> - 2.507-3
- More BR: (Bit::Vector, File::Slurp, Test::Pod::Coverage).

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.507-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 22 2009 Xavier Bachelot <xavier@bachelot.org> - 2.507-1
- New upstream version 2.507.

* Sat Aug 02 2008 Xavier Bachelot <xavier@bachelot.org> - 2.504-1
- New upstream version 2.504.

* Fri Jul 18 2008 Xavier Bachelot <xavier@bachelot.org> - 2.503-1
- New upstream version 2.503.

* Thu May 15 2008 Xavier Bachelot <xavier@bachelot.org> - 2.501-1
- New upstream version 2.501.

* Mon Mar  3 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.497-2
- rebuild for new perl (again)

* Fri Feb 15 2008 Xavier Bachelot <xavier@bachelot.org> - 2.497-1
- New upstream version.

* Fri Feb  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.496-4
- rebuild for new perl

* Mon Jan 21 2008 Xavier Bachelot <xavier@bachelot.org> - 2.496-3
- Fix License:.

* Mon Jan 07 2008 Xavier Bachelot <xavier@bachelot.org> - 2.496-2
- Add missing BRs.

* Sat Dec 22 2007 Xavier Bachelot <xavier@bachelot.org> - 2.496-1
- Update to 2.496.
- Clean up spec.

* Wed Jul 26 2006 Xavier Bachelot <xavier@bachelot.org> - 2.488-1
- Initial build.
