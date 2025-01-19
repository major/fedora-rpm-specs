Name:           perl-DBIx-Class-Schema-Loader
Summary:        Dynamic definition of a DBIx::Class::Schema
Version:        0.07052
Release:        5%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/V/VE/VEESH/DBIx-Class-Schema-Loader-%{version}.tar.gz
URL:            https://metacpan.org/release/DBIx-Class-Schema-Loader
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Carp::Clan)
BuildRequires:  perl(Class::Accessor::Grouped)
BuildRequires:  perl(Class::C3::Componentised)
BuildRequires:  perl(Class::Inspector)
BuildRequires:  perl(Class::Unload)
BuildRequires:  perl(curry)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dump)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DBIx::Class)
BuildRequires:  perl(DBIx::Class::Schema)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Hash::Merge)
BuildRequires:  perl(Lingua::EN::Inflect::Number)
BuildRequires:  perl(Lingua::EN::Inflect::Phrase)
BuildRequires:  perl(Lingua::EN::Tagger)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(mro)
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(overload)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(String::CamelCase)
BuildRequires:  perl(String::ToIdentifier::EN)
BuildRequires:  perl(String::ToIdentifier::EN::Unicode)
BuildRequires:  perl(Sub::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Try::Tiny)
# Tests only
BuildRequires:  perl(Config)
# Unused BuildRequires:  perl(DBD::Interbase)
# Unused BuildRequires:  perl(DBD::Interbase::GetInfo)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBI)
BuildRequires:  perl(DBIx::Class::Core)
BuildRequires:  perl(DBIx::Class::Optional::Dependencies)
BuildRequires:  perl(DBIx::Class::Storage)
# Unused BuildRequires:  perl(DBIx::Class::Storage::DBI)
BuildRequires:  perl(English)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(lib)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Scope::Guard)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(utf8)
# hidden from PAUSE
Provides:       perl(DBIx::Class::Schema::Loader::Utils)
Requires:       perl(Hash::Merge)
Requires:       perl(Test::More)

%{?perl_default_filter}
# Filter modules bundled for tests
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(dbixcsl_.*\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(make_dbictest_db.*\\)

%description
DBIx::Class::Schema::Loader automates the definition of a
DBIx::Class::Schema by scanning database table definitions
and setting up the columns, primary keys, and relationships.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(DBD::SQLite)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n DBIx-Class-Schema-Loader-%{version}
# Help generators to recognize Perl scripts
for F in `find t -name *.t -o -name *.pl` t/bin/simple_filter; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
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
mkdir -p %{buildroot}%{_libexecdir}/%{name}/script
ln -s %{_bindir}/dbicdump %{buildroot}%{_libexecdir}/%{name}/script
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
export SCHEMA_LOADER_TESTS_BACKCOMPAT=1
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes
%{perl_vendorlib}/DBIx*
%{_mandir}/man1/dbicdump*
%{_mandir}/man3/DBIx::Class::Schema::Loader*
%{_bindir}/dbicdump*

%files tests
%{_libexecdir}/%{name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.07052-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.07052-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.07052-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.07052-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 08 2024 Jitka Plesnikova <jplesnik@redhat.com> - 0.07052-1
- 0.07052 bump (rhbz#2257119)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.07051-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.07051-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 28 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.07051-1
- 0.07051 bump

* Mon Nov 21 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.07050-1
- 0.07050 bump
- Package tests

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.07049-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.07049-14
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.07049-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.07049-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.07049-11
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.07049-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.07049-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.07049-8
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.07049-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.07049-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.07049-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.07049-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.07049-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.07049-2
- Perl 5.28 rebuild

* Mon Mar 26 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.07049-1
- 0.07049 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.07048-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.07048-1
- 0.07048 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.07047-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.07047-2
- Perl 5.26 rebuild

* Mon May 29 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.07047-1
- 0.07047 bump

* Fri May 26 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.07046-3
- Fix building on Perl without '.' in @INC

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.07046-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Sep 06 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.07046-1
- 0.07046 bump

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.07045-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.07045-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 25 2016 Petr Šabata <contyk@redhat.com> - 0.07045-1
- 0.07045 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07043-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 15 2015 Petr Šabata <contyk@redhat.com> - 0.07043-1
- 0.07043 bump

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.07042-2
- Perl 5.22 rebuild

* Tue Dec 09 2014 Petr Šabata <contyk@redhat.com> - 0.07042-1
- 0.07042 bump
- META.* files list lots of modules with specific versions this
  distribution doesn't even touch and the few that match what we really
  use require dubious versions; I'm not going to list any unless it proves
  to be necessary

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.07033-5
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07033-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07033-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07033-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Sep 09 2012 Iain Arnell <iarnell@gmail.com> 0.07033-1
- update to latest upstream version

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07025-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 02 2012 Petr Pisar <ppisar@redhat.com> - 0.07025-2
- Perl 5.16 rebuild

* Sat Jun 09 2012 Iain Arnell <iarnell@gmail.com> 0.07025-1
- update to latest upstream version
- BR inc::Module::Install instead of EU::MM

* Sat May 12 2012 Iain Arnell <iarnell@gmail.com> 0.07024-1
- update to latest upstream version

* Mon May 07 2012 Iain Arnell <iarnell@gmail.com> 0.07023-1
- update to latest upstream version

* Mon Apr 09 2012 Iain Arnell <iarnell@gmail.com> 0.07022-1
- update to latest upstream version

* Sun Apr 01 2012 Iain Arnell <iarnell@gmail.com> 0.07020-1
- update to latest upstream version

* Fri Mar 30 2012 Iain Arnell <iarnell@gmail.com> 0.07019-1
- update to latest upstream version

* Wed Feb 08 2012 Iain Arnell <iarnell@gmail.com> 0.07017-1
- update to latest upstream version

* Fri Feb 03 2012 Iain Arnell <iarnell@gmail.com> 0.07015-1
- update to latest upstream version
- silence rpmlint wrong-script-interpreter warning

* Sun Jan 22 2012 Iain Arnell <iarnell@gmail.com> 0.07010-5
- drop tests subpackage; move tests to main package documentation
- clean up spec for modern rpmbuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07010-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 0.07010-3
- Perl mass rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.07010-2
- Perl mass rebuild

* Sat Apr 23 2011 Iain Arnell <iarnell@gmail.com> 0.07010-1
- update to latest upstream version

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07002-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Nov 05 2010 Iain Arnell <iarnell@gmail.com> 0.07002-2
- provides perl(DBIx::Class::Schema::Loader::Utils)

* Tue Oct 05 2010 Iain Arnell <iarnell@gmail.com> 0.07002-1
- update to 0.07002
- disable auto_install
- remove unnecessary explicit requires

* Mon Aug 16 2010 Iain Arnell <iarnell@gmail.com> 0.07001-1
- update by Fedora::App::MaintainerTools 0.006
- updating to latest GA CPAN version (0.07001)
- altered br on perl(DBD::SQLite) (1.12 => 1.29)
- added a new br on perl(Exporter) (version 5.63)
- added a new br on perl(Lingua::EN::Inflect::Phrase) (version 0.02)
- added a new br on perl(Moose) (version 0)
- added a new br on perl(MooseX::NonMoose) (version 0)
- added a new br on perl(Scope::Guard) (version 0)
- altered br on perl(Test::More) (0.92 => 0.94)
- added a new br on perl(Try::Tiny) (version 0)
- added a new br on perl(namespace::clean) (version 0)
- added a new req on perl(Exporter) (version 5.63)
- added a new req on perl(Lingua::EN::Inflect::Phrase) (version 0.02)
- added a new req on perl(Scope::Guard) (version 0)
- added a new req on perl(Try::Tiny) (version 0)
- added a new req on perl(namespace::clean) (version 0)
- dropped old requires on perl(namespace::autoclean)

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.05003-2
- Mass rebuild with perl-5.12.0

* Tue Feb 23 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.05003-1
- switch filtering systems
- add files in bin && man1
- enable back-compat testing
- update by Fedora::App::MaintainerTools 0.003
- PERL_INSTALL_ROOT => DESTDIR
- added a new br on perl(Class::Accessor::Grouped) (version 0.09002)
- added a new br on perl(Class::C3::Componentised) (version 1.0005)
- added a new br on perl(Class::Unload) (version 0)
- altered br on perl(DBIx::Class) (0.07006 => 0.08114)
- added a new br on perl(File::Copy) (version 0)
- altered br on perl(File::Path) (0 => 2.07)
- added a new br on perl(File::Slurp) (version 9999.13)
- added a new br on perl(File::Temp) (version 0.16)
- added a new br on perl(IPC::Open3) (version 0)
- added a new br on perl(List::MoreUtils) (version 0)
- added a new br on perl(Test::Exception) (version 0)
- altered br on perl(Test::More) (0.47 => 0.92)
- added a new br on perl(namespace::autoclean) (version 0)
- dropped old BR on perl(Class::Accessor::Fast)
- dropped old BR on perl(Class::Data::Accessor)
- dropped old BR on perl(Test::Pod)
- dropped old BR on perl(Test::Pod::Coverage)
- dropped old BR on perl(UNIVERSAL::require)
- dropped old BR on perl(YAML::Tiny)
- added a new br on CPAN (inc::Module::AutoInstall found)
- added a new req on perl(Carp::Clan) (version 0)
- added a new req on perl(Class::Accessor::Grouped) (version 0.09002)
- added a new req on perl(Class::C3) (version 0.18)
- added a new req on perl(Class::C3::Componentised) (version 1.0005)
- added a new req on perl(Class::Inspector) (version 0)
- added a new req on perl(Class::Unload) (version 0)
- added a new req on perl(DBIx::Class) (version 0.08114)
- added a new req on perl(Data::Dump) (version 1.06)
- added a new req on perl(Digest::MD5) (version 2.36)
- added a new req on perl(File::Slurp) (version 9999.13)
- added a new req on perl(File::Spec) (version 0)
- added a new req on perl(Lingua::EN::Inflect::Number) (version 1.1)
- added a new req on perl(List::MoreUtils) (version 0)
- added a new req on perl(Scalar::Util) (version 0)
- added a new req on perl(Text::Balanced) (version 0)
- added a new req on perl(namespace::autoclean) (version 0)
- dropped old requires on perl(Class::Accessor::Fast)
- dropped old requires on perl(Class::Data::Accessor)

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.04006-6
- rebuild against perl 5.10.1

* Wed Aug 05 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.04006-5
- Remove R: DBIX::Class.

* Wed Aug 05 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.04006-4
- Fix mass rebuild breakdown:
  Replace bundled Module-Install with Module-Install-0.91.
  Add --skipdeps.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04006-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 26 2009 Tom "spot" Callaway <tcallawa@redhat.com> 0.04006-2
- fix duplicate directory ownership (perl-DBIx-Class owns %%{perl_vendorlib}/DBIx/Class/)

* Wed Jun 03 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.04006-1
- auto-update to 0.04006 (by cpan-spec-update 0.01)
- altered br on perl(ExtUtils::MakeMaker) (0 => 6.42)
- altered br on perl(Test::More) (0 => 0.47)

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04005-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul 23 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.04005-2
- bump

* Mon Jun 02 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.04005-1
- update to 0.4005
- filter _docdir requires/provides

* Mon Mar 17 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.04004-1
- brush-up for review submission

* Wed Oct 17 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.04003-1
- Specfile autogenerated by cpanspec 1.71.
