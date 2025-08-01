Summary:        SAX parser access API for Perl
Name:           perl-XML-SAX
Version:        1.02
Release:        19%{?dist}

License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/XML-SAX
# Original source
# http://www.cpan.org/authors/id/G/GR/GRANTM/XML-SAX-%%{version}.tar.gz
Source0:        XML-SAX-%{version}-nopatents.tar.gz
# XML-SAX contains patented code that we cannot ship. Therefore we use
# this script to remove the patented code before shipping it.
# Download the upstream tarball and invoke this script while in the
# tarball's directory:
# ./generate-tarball.sh %%{version}
Source1: generate-tarball.sh

# Fix rt#20126
Patch0:         perl-XML-SAX-0.99-rt20126.patch

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XML::NamespaceSupport) >= 0.03
# XML::SAX::Base became independent package, BR just for test
BuildRequires:  perl(XML::SAX::Base)
BuildRequires:  perl(XML::SAX::Exception)
# Test
BuildRequires:  perl(base)
BuildRequires:  perl(Fatal)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(Test)

Requires:       perl(LWP::UserAgent)

# Remove bogus XML::SAX::PurePerl* dependencies and unversioned provides
%global __requires_exclude ^perl\\(XML::SAX::PurePerl
%global __provides_exclude ^perl\\(XML::SAX::PurePerl\\)$

%description
XML::SAX consists of several framework classes for using and building
Perl SAX2 XML parsers, filters, and drivers. It is designed around the
need to be able to "plug in" different SAX parsers to an application
without requiring programmer intervention. Those of you familiar with
the DBI will be right at home. Some of the designs come from the Java
JAXP specification (SAX part), only without the javaness.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n XML-SAX-%{version}
%patch -P0 -p1
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
echo N | perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}
touch %{buildroot}%{perl_vendorlib}/XML/SAX/ParserDetails.ini

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t testfiles %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/99cleanup.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# Some tests write into temporary files/directories.
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./

# Non-root user is not possible to work with system
# %{perl_vendorlib}/XML/SAX/ParserDetails.ini
if [ `id -u` -ne 0 ]; then
    rm t/01known.t t/20factory.t t/21saxini.t
    prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
else
    cp -p "%{perl_vendorlib}/XML/SAX/ParserDetails.ini" "%{perl_vendorlib}/XML/SAX/ParserDetails.ini.backup"
    prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
    mv "%{perl_vendorlib}/XML/SAX/ParserDetails.ini.backup" "%{perl_vendorlib}/XML/SAX/ParserDetails.ini"
fi

popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

# See http://rhn.redhat.com/errata/RHBA-2010-0008.html regarding these scriptlets
# perl-XML-LibXML-1.58-6 is in EL 5.8 and possibly later EL-5 releases
%post
if [ ! -f "%{perl_vendorlib}/XML/SAX/ParserDetails.ini" ] ; then
  perl -MXML::SAX -e \
    'XML::SAX->add_parser(q(XML::SAX::PurePerl))->save_parsers()' 2>/dev/null || :
else
  cp -p "%{perl_vendorlib}/XML/SAX/ParserDetails.ini" "%{perl_vendorlib}/XML/SAX/ParserDetails.ini.backup"
fi

%triggerun -- perl-XML-LibXML < 1.58-8
if [ -f "%{perl_vendorlib}/XML/SAX/ParserDetails.ini.backup" ] ; then
  mv "%{perl_vendorlib}/XML/SAX/ParserDetails.ini.backup" "%{perl_vendorlib}/XML/SAX/ParserDetails.ini"
fi

%preun
# create backup of ParserDetails.ini, therefore user's configuration is used
if [ $1 -eq 0 ] ; then
  perl -MXML::SAX -e \
    'XML::SAX->remove_parser(q(XML::SAX::PurePerl))->save_parsers()' || :
fi
[ -f "%{perl_vendorlib}/XML/SAX/ParserDetails.ini.backup" ] && \
rm -rf "%{perl_vendorlib}/XML/SAX/ParserDetails.ini.backup" || :

%files
%license LICENSE
%doc Changes README
%dir %{perl_vendorlib}/XML/
%{perl_vendorlib}/XML/SAX.pm
%dir %{perl_vendorlib}/XML/SAX/
%{perl_vendorlib}/XML/SAX/*.pm
%doc %{perl_vendorlib}/XML/SAX/*.pod
%{perl_vendorlib}/XML/SAX/PurePerl/
%{_mandir}/man3/XML::*.3pm*
%ghost %{perl_vendorlib}/XML/SAX/ParserDetails.ini

%files tests
%{_libexecdir}/%{name}

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 31 2024 Jitka Plesnikova <jplesnik@redhat.com> - 1.02-16
- Package tests

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.02-10
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.02-7
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.02-4
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 17 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.02-1
- 1.02 bump

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.00-5
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.00-2
- Perl 5.28 rebuild

* Thu Feb 15 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.00-1
- 1.00 bump

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.99-19
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.99-17
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.99-14
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.99-13
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 0.99-10
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 22 2012 Jitka Plesnikova <jplesnik@redhat.com> - 0.99-8
- Create script generate-tarball.sh which remove xmltest.xml from source
  tarball

* Thu Nov 22 2012 Jitka Plesnikova <jplesnik@redhat.com> - 0.99-7
- Update dependencies and summary
- Remove xmltest.xml due to copyright
- Replace PERL_INSTALL_ROOT with DESTDIR

* Wed Aug 15 2012 Jitka Plesnikova <jplesnik@redhat.com> - 0.99-6
- Fixed incorrect parsing of comments (RT#20126).
- Specify all dependencies.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 0.99-4
- Perl 5.16 rebuild

* Sat Mar 17 2012 Paul Howarth <paul@city-fan.org> - 0.99-3
- Drop redundant runtime dependencies on perl(XML::LibXML) and
  perl(XML::LibXML::Common), which cause circular build dependencies (#720974)
- Simplify provides and requires filters
- Don't need to remove empty directories from buildroot
- Mark POD files as %%doc

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Oct 07 2011 Marcela Mašláňová <mmaslano@redhat.com> 0.99-1
- update to 0.99

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 0.96-15
- Perl mass rebuild

* Fri Jun 24 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.96-14
- fix macros to work with new macros
- clean spec

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 24 2011 Adrian Reber <adrian@lisas.de> - 0.96-12
- rebuild for ppc

* Thu Dec 23 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.96-11
- 661697 rebuild for fixing problems with vendorach/lib

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.96-10
- Mass rebuild with perl-5.12.0

* Fri Feb  5 2010 Stepan Kasal <skasal@redhat.com> - 0.96-9
- anchor the filtering regexps

* Fri Feb  5 2010 Marcela Mašláňová <mmaslano@redhat.com> - 0.96-8
- XML-LibXML use triggers for XML::SAX update. Deleting of settings in
 ParserDetails.ini is solved by post and preun part, which create backup.

* Thu Nov 12 2009 Marcela Mašláňová <mmaslano@redhat.com> - 0.96-7
- instead of path into post used perl_vendorlib macro
- rebuilt will be needed for perl-5.10.1

* Thu Nov 12 2009 Marcela Mašláňová <mmaslano@redhat.com> - 0.96-6
- post scriptlet needs to check whether the file is installed. When it isn't,
 then it's needed call for adding PurePerl parser
 http://perl-xml.sourceforge.net/faq/#parserdetails.ini

* Mon Oct 19 2009 Stepan Kasal <skasal@redhat.com> - 0.96-5
- use the filtering macros

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 28 2009 Marcela Mašláňová <mmaslano@redhat.com> - 0.96-3
- 478905 fix scriptlets

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 11 2008 Marcela Mašláňová <mmaslano@redhat.com> - 0.96-1
- update to 0.96, big leap in versioning

* Sun Mar  2 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.16-5
- Re-enable XML::LibXML BuildRequires

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.16-4
- Rebuild for perl 5.10 (again)

* Mon Jan 28 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.16-3.1
- temporarily disable BR against perl-XML-LibXML

* Thu Jan 24 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.16-3
- rebuild for new perl

* Sat Jul 07 2007 Robin Norwood <rnorwood@redhat.com> - 0.16-2
- Resolves: rhbz#247213
- Fix provides and requires scripts.

* Mon Jul 02 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.16-1
- Update to 0.16.
- Brings specfile closer to Fedora Perl template.
- Corrects Source0 URL (upstream maintainer has changed).
- Move Requires filter into spec, and add Provides filter.

* Tue Feb 13 2007 Robin Norwood <rnorwood@redhat.com> - 0.15-1
- New version: 0.15

* Fri Jun 09 2006 Jason Vas Dias <jvdias@redhat.com> - 0.14-2
- fix bug 194706: fails to build under (new!) mock

* Mon Jun 05 2006 Jason Vas Dias <jvdias@redhat.com> - 0.14-1
- upgrade to 0.14

* Fri Feb 03 2006 Jason Vas Dias <jvdias@redhat.com> - 0.13-1.1
- rebuild for new perl-5.8.8

* Mon Dec 19 2005 Jason Vas Dias <jvdias@redhat.com> - 0.13-1
- upgrade to 0.13

* Fri Dec 16 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt for new gcc

* Fri Dec 16 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt for new gcj

* Sun Apr 18 2004 Ville Skyttä <ville.skytta at iki.fi> - 0.12-7
- #121167
- Handle ParserDetails.ini parser registration.
- Require perl(:MODULE_COMPAT_*).
- Own installed directories.

* Wed Oct 22 2003 Chip Turner <cturner@redhat.com> - 0.12-1
- Specfile autogenerated.

