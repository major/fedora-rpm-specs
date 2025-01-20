# Enable Excel file format support
%bcond_without perl_SQL_Translator_enables_excel

Name:           perl-SQL-Translator
Summary:        Manipulate structured data definitions (SQL and more)
Version:        1.66
Release:        2%{?dist}
# script/sqlt*: GPL-2.0-only
# other files:  GPL-1.0-or-later OR Artistic-1.0-Perl
License:        ( GPL-1.0-or-later OR Artistic-1.0-Perl ) AND GPL-2.0-only
Source0:        https://cpan.metacpan.org/authors/id/V/VE/VEESH/SQL-Translator-%{version}.tar.gz
URL:            https://metacpan.org/release/SQL-Translator
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::ShareDir::Install)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Carp::Clan)
BuildRequires:  perl(CGI)
BuildRequires:  perl(CGI::Pretty)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DBI) >= 1.54
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::ShareDir) >= 1.0
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(GD)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Graph::Directed)
BuildRequires:  perl(GraphViz)
BuildRequires:  perl(IO::Dir)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(JSON::MaybeXS) >= 1.003003
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Moo) >= 1.000003
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(overload)
BuildRequires:  perl(Package::Variant) >= 1.001001
BuildRequires:  perl(Parse::RecDescent) >= 1.967009
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Scalar::Util)
%if %{with perl_SQL_Translator_enables_excel}
BuildRequires:  perl(Spreadsheet::ParseExcel) >= 0.41
%endif
BuildRequires:  perl(Storable)
BuildRequires:  perl(Sub::Quote)
BuildRequires:  perl(Template) >= 2.20
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(Text::RecordParser) >= 0.02
BuildRequires:  perl(Try::Tiny) >= 0.04
BuildRequires:  perl(vars)
BuildRequires:  perl(XML::LibXML) >= 1.69
BuildRequires:  perl(XML::LibXML::XPathContext)
BuildRequires:  perl(XML::Writer) >= 0.500
BuildRequires:  perl(YAML) >= 0.66
# Tests:
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(lib)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::Exception) >= 0.42
BuildRequires:  perl(XML::Parser)
# Optional tests:
# DBD::Pg not needed because it requires preconfigures PostgreSQL database
# with DBICTEST_PG_* environemnt variables
# Test::PostgreSQL not yet packaged
# xt/* tests are not run
#BuildRequires:  perl(Test::EOL) >= 1.1
#BuildRequires:  perl(Test::NoTabs) >= 1.1
#BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(Test::PostgreSQL)
Requires:       perl(CGI)
Requires:       perl(CGI::Pretty)
Requires:       perl(DBI) >= 1.54
Requires:       perl(File::ShareDir) >= 1.0
Requires:       perl(Graph::Directed)
Requires:       perl(JSON::MaybeXS) >= 1.003003
Requires:       perl(overload)
Requires:       perl(Package::Variant) >= 1.001001
Requires:       perl(Parse::RecDescent) >= 1.967009
%if %{with perl_SQL_Translator_enables_excel}
Requires:       perl(Spreadsheet::ParseExcel) >= 0.41
%endif
Requires:       perl(Template) >= 2.20
Requires:       perl(Test::More) >= 0.88
Requires:       perl(Text::RecordParser) >= 0.02
Requires:       perl(Try::Tiny) >= 0.04
Requires:       perl(XML::LibXML) >= 1.69
Requires:       perl(XML::Writer) >= 0.500

%{?perl_default_filter}
# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((DBI|File::ShareDir|JSON::MaybeXS|Moo|Package::Variant|Parse::RecDescent|Spreadsheet::ParseExcel|Template|Test::More|Text::RecordParser|Try::Tiny|XML::LibXML)\\)$
# Remove badly detected requires (a grammar in the
# lib/SQL/Translator/Parser/Sybase.pm)
%global __requires_exclude %{__requires_exclude}|^perl\\(:\\)
# Filter modules bundled for tests
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}

%description
SQL::Translator is a group of Perl modules that converts vendor-specific
SQL table definitions into other formats, such as other vendor-specific
SQL, ER diagrams, documentation (POD and HTML), XML, and Class::DBI
classes.  The main focus of SQL::Translator is SQL, but parsers exist
for other structured data formats%{?with_perl_SQL_Translator_enables_excel:, including Excel spreadsheets} and
arbitrarily delimited text files.  Through the separation of the code into
parsers and producers with an object model in between, it’s possible to
combine any parser with any producer, to plug in custom parsers or
producers, or to manipulate the parsed data via the built-in object model.
Presently only the definition parts of SQL are handled (CREATE, ALTER),
not the manipulation of data (INSERT, UPDATE, DELETE).

%package Producer-Diagram
Summary:        ER diagram producer for SQL::Translator

%description Producer-Diagram
ER diagram producer for SQL::Translator.

%package Producer-GraphViz
Summary:        GraphViz diagram producer for SQL::Translator

%description Producer-GraphViz
GraphViz diagram producer for SQL::Translator.

%package -n sqlt-graph
Summary:        sqlt-graph tool to create a graph from a database schema
License:        GPL-2.0-only
Obsoletes:      %{name} < 1.62-4

%description -n sqlt-graph
The sqlt-graph tool from %{name} that can automatically create a graph
from a database schema. Packaged separately to avoid the main package
depending on Graphviz.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-Producer-Diagram = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-Producer-GraphViz = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       sqlt-graph = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(DBD::SQLite)
Requires:       perl(XML::Parser)
Requires:       perl(Test::PostgreSQL)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n SQL-Translator-%{version}
# Fix shell-bangs
perl -MConfig -pi -e 's|^#!.*perl\b|$Config{startperl}|' script/*
# Fix permission, CPAN RT#100532
chmod -x lib/SQL/Translator/Parser/JSON.pm
%if %{without perl_SQL_Translator_enables_excel}
# Remove Excel support
rm lib/SQL/Translator/Parser/Excel.pm
perl -i -ne 'print $_ unless m{^lib/SQL/Translator/Parser/Excel\.pm}' MANIFEST
%endif
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
mkdir -p %{buildroot}%{_libexecdir}/%{name}/script
for F in sqlt sqlt.cgi sqlt-diagram sqlt-diff sqlt-diff-old sqlt-dumper sqlt-graph; do
    ln -s %{_bindir}/$F %{buildroot}%{_libexecdir}/%{name}/script
done
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# Some tests write into temporary files/directories. The easiest solution
# is to copy the tests into a writable directory and execute them from there.
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes README
%{_bindir}/sqlt*
%dir %{perl_vendorlib}/SQL
%{perl_vendorlib}/SQL/Translator*
%dir %{perl_vendorlib}/Test
%{perl_vendorlib}/Test/SQL
%{perl_vendorlib}/auto
%{_mandir}/man1/sqlt*
%{_mandir}/man3/SQL::Translator*
%{_mandir}/man3/Test::SQL::Translator*
%exclude %{perl_vendorlib}/SQL/Translator/Producer/Diagram.pm
%exclude %{perl_vendorlib}/SQL/Translator/Producer/GraphViz.pm
%exclude %{_mandir}/man1/sqlt-graph.*
%exclude %{_mandir}/man3/SQL::Translator::Producer::Diagram.*
%exclude %{_mandir}/man3/SQL::Translator::Producer::GraphViz.*
%exclude %{_bindir}/sqlt-graph

%files Producer-Diagram
%{perl_vendorlib}/SQL/Translator/Producer/Diagram.pm
%{_mandir}/man3/SQL::Translator::Producer::Diagram.*

%files Producer-GraphViz
%{perl_vendorlib}/SQL/Translator/Producer/GraphViz.pm
%{_mandir}/man3/SQL::Translator::Producer::GraphViz.*

%files -n sqlt-graph
%{_bindir}/sqlt-graph
%{_mandir}/man1/sqlt-graph.*

%files tests
%{_libexecdir}/%{name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.66-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Nov 18 2024 Jitka Plesnikova <jplesnik@redhat.com> - 1.66-1
- 1.66 bump (rhbz#2326987)

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.65-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Jitka Plesnikova <jplesnik@redhat.com> - 1.65-1
- 1.65 bump (rhbz#2258649)

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.64-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 02 2024 Jitka Plesnikova <jplesnik@redhat.com> - 1.64-1
- 1.64 bump (rhbz#2255608)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.63-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 27 2023 Jitka Plesnikova <jplesnik@redhat.com> - 1.63-1
- 1.63 bump
- Package tests

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.62-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.62-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.62-7
- Perl 5.36 rebuild

* Tue May 10 2022 Adam Williamson <awilliam@redhat.com> - 1.62-6
- Split GraphViz-dependent components into subpackages

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.62-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.62-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.62-3
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.62-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 14 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.62-1
- 1.62 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.61-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.61-2
- Perl 5.32 rebuild

* Mon Apr 20 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.61-1
- 1.61 bump

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.60-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.60-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.60-2
- Perl 5.30 rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.60-1
- 1.60 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11024-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11024-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.11024-3
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11024-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 10 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.11024-1
- 0.11024 bump

* Mon Dec 11 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.11023-1
- 0.11023 bump

* Tue Dec 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.11022-1
- 0.11022 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11021-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.11021-9
- Perl 5.26 rebuild

* Fri May 26 2017 Petr Pisar <ppisar@redhat.com> - 0.11021-8
- Adapt to changes in JSON-PP-0.92 (bug #1455782)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11021-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.11021-6
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.11021-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11021-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 07 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.11021-3
- Perl 5.22 rebuild

* Mon Mar 02 2015 Petr Šabata <contyk@redhat.com> - 0.11021-2
- Avoid X11 dependency by Subpackaging SQL::Translator::Producer::Diagram

* Tue Feb 03 2015 Petr Šabata <contyk@redhat.com> - 0.11021-1
- 0.11021 bump

* Mon Nov 24 2014 Petr Pisar <ppisar@redhat.com> - 0.11020-1
- 0.11020 bump

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.11016-4
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11016-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11016-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 21 2013 Iain Arnell <iarnell@gmail.com> 0.11016-1
- update to latest upstream version
- license change from GPLv2 to GPL+ or Artistic (aka 'same as Perl')
- drop provides for SQL::Translator::Schema::Graph::*

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11012-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 29 2012 Iain Arnell <iarnell@gmail.com> 0.11012-1
- update to latest upstream version

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11011-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 29 2012 Petr Pisar <ppisar@redhat.com> - 0.11011-3
- Perl 5.16 rebuild

* Tue May 15 2012 Iain Arnell <iarnell@gmail.com> 0.11011-2
- add provides for SQL::Translator::Schema::Graph::*

* Sun May 13 2012 Iain Arnell <iarnell@gmail.com> 0.11011-1
- update to latest upstream version

* Sun Jan 22 2012 Iain Arnell <iarnell@gmail.com> 0.11010-3
- drop tests subpackage; move tests to main package documentation
- drop old-style filtering

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11010-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 12 2011 Iain Arnell <iarnell@gmail.com> 0.11010-1
- update to latest upstream version
- clean up spec for modern rpmbuild
- remove unnecessary explicit requires

* Thu Jul 21 2011 Iain Arnell <iarnell@gmail.com> 0.11006-6
- update filtering for rpm 4.9

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 0.11006-5
- Perl mass rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 0.11006-4
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11006-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.11006-2
- 661697 rebuild for fixing problems with vendorach/lib

* Thu Sep 02 2010 Iain Arnell <iarnell@gmail.com> 0.11006-1
- update to latest upstream version

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.11005-3
- Mass rebuild with perl-5.12.0

* Tue Mar 16 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.11005-2
- fix deps on perl(Parse::RecDescent)... again :\

* Sat Mar 13 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.11005-1
- update by Fedora::App::MaintainerTools 0.006
- updating to latest GA CPAN version (0.11005)
- altered br on perl(Parse::RecDescent) (1.963 => 1.962002)
- added manual BR on perl(Template) (or override to 0)
- added manual BR on perl(Text::RecordParser) (or override to 0)
- added manual BR on perl(XML::XPath) (or override to 0)
- altered req on perl(Parse::RecDescent) (1.963 => 1.962002)

* Wed Feb 10 2010 Paul Howarth <paul@city-fan.org> 0.11003-3
- fix broken deps for perl(Parse::RecDescent)
- altered br on perl(Parse::RecDescent) (1.962002 => 1.963)
- altered req on perl(Parse::RecDescent) (1.962002 => 1.963)

* Fri Feb 05 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.11003-2
- PERL_INSTALL_ROOT => DESTDIR
- add perl_default_subpackage_tests

* Sat Jan 16 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.11003-1
- add br on XML::LibXML
- auto-update to 0.11003 (by cpan-spec-update 0.01)

* Sun Sep 27 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.11002-1
- auto-update to 0.11002 (by cpan-spec-update 0.01)
- altered br on perl(Parse::RecDescent) (1.096 => 1.962002)
- altered req on perl(Parse::RecDescent) (1.096 => 1.962002)

* Mon Aug 24 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.11001-1
- auto-update to 0.11001 (by cpan-spec-update 0.01)
- added a new br on perl(Carp::Clan) (version 0)
- altered br on perl(Digest::SHA1) (2.00 => 2)
- added a new br on perl(ExtUtils::MakeMaker) (version 6.42)
- added a new br on perl(File::ShareDir) (version 1)
- altered br on perl(IO::Scalar) (0 => 2.11)
- altered br on perl(Parse::RecDescent) (1.94 => 1.096)
- altered br on perl(YAML) (0.39 => 0.66)
- added a new br on CPAN (inc::Module::AutoInstall found)
- added a new req on perl(Carp::Clan) (version 0)
- added a new req on perl(Class::Base) (version 0)
- altered req on perl(Class::Data::Inheritable) (0 => 0.02)
- added a new req on perl(Class::MakeMethods) (version 0)
- added a new req on perl(DBI) (version 0)
- added a new req on perl(Digest::SHA1) (version 2)
- added a new req on perl(File::ShareDir) (version 1)
- added a new req on perl(File::Spec) (version 0)
- added a new req on perl(IO::Dir) (version 0)
- added a new req on perl(IO::Scalar) (version 2.11)
- added a new req on perl(Parse::RecDescent) (version 1.096)
- added a new req on perl(Pod::Usage) (version 0)
- added a new req on perl(XML::Writer) (version 0.5)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09004-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed May 27 2009 Iain Arnell <iarnell@gmail.com> 0.09004-2
- add missing requires Class::Accessor::Fast and Class::Data::Inheritable

* Sun Mar 08 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.09004-1
- update to 0.09004

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09002-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 03 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.09002-1
- update to 0.09002

* Sun Sep 07 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.9001-1
- update to 0.9001
- add new BR: perl(Digest::SHA1) >= 2.00

* Wed Mar 19 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.09000-1
- update to 0.09000
- expose more core BR's
- additional br's now required

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.08001-3
- Rebuild for new perl

* Wed Oct 24 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.08001-2
- bump

* Sun Oct 14 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.08001-1
- updated to 0.08001
- update license tag
- nix errant perl(Producer::BaseTest) provides
- make description useful :)
- we now skip Template::Toolkit tests correctly, so stop disabling them

* Mon May 14 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.08-1
- Specfile autogenerated by cpanspec 1.71.
