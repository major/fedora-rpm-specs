# Run optional test
%if ! 0%{?rhel}
%bcond_without perl_BerkeleyDB_enables_optional_test
%else
%bcond_with perl_BerkeleyDB_enables_optional_test
%endif

# We need to know the exact DB version we're built against
%global db_ver %(sed '/DB_VERSION_STRING/!d;s/.*Berkeley DB[[:space:]]*\\([^:]*\\):.*/\\1/' /usr/include/db.h 2>/dev/null || echo 4.0.0)

Name:           perl-BerkeleyDB
Version:        0.66
Release:        2%{?dist}
Summary:        Interface to Berkeley DB
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/BerkeleyDB
Source0:        https://cpan.metacpan.org/authors/id/P/PM/PMQS/BerkeleyDB-%{version}.tar.gz
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  libdb-devel
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  sed
# Module Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(strict)
BuildRequires:  perl(UNIVERSAL)
BuildRequires:  perl(vars)
BuildRequires:  perl(XSLoader)
# Test Suite
BuildRequires:  perl(charnames)
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)
%if %{with perl_BerkeleyDB_enables_optional_test}
# Optional Tests
BuildRequires:  perl(Data::Dumper) >= 2.08
BuildRequires:  perl(Encode)
BuildRequires:  perl(MLDBM)
BuildRequires:  perl(Test::CPAN::Meta)
BuildRequires:  perl(Test::CPAN::Meta::JSON)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Pod) >= 1.00
%endif
# Runtime
# Hard-code Berkeley DB requirement to avoid problems like #592209
Requires:       libdb = %{db_ver}
Requires:       perl(XSLoader)

# Don't "provide" private Perl libs
%{?perl_default_filter}

%description
BerkeleyDB is a module that allows Perl programs to make use of the
facilities provided by Berkeley DB version 2 or greater (note: if
you want to use version 1 of Berkeley DB with Perl you need the DB_File
module).

Berkeley DB is a C library that provides a consistent interface to a
number of database formats. BerkeleyDB provides an interface to all
four of the database types (hash, btree, queue and recno) currently
supported by Berkeley DB.

%prep
%setup -q -n BerkeleyDB-%{version}

chmod -c -x Changes README

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}
install -D -m755 dbinfo %{buildroot}%{_bindir}/dbinfo

# Remove files we don't want packaged
rm %{buildroot}%{perl_vendorarch}/{mkconsts,scan}.pl

%check
make test

%files
%doc README Changes Todo
%{_bindir}/dbinfo
%{perl_vendorarch}/BerkeleyDB/
%{perl_vendorarch}/BerkeleyDB.pm
%doc %{perl_vendorarch}/BerkeleyDB.pod
%{perl_vendorarch}/auto/BerkeleyDB/
%{_mandir}/man3/BerkeleyDB.3*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.66-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Oct 15 2024 Jitka Plesnikova <jplesnik@redhat.com> - 0.66-1
- 0.66 bump (rhbz#2318577)
  - Remove bundled Test::More
  - Possible precedence problem between ! and string eq
  - Silence clang warnings

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.65-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 10 2024 Jitka Plesnikova <jplesnik@redhat.com> - 0.65-9
- Perl 5.40 rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.65-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.65-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.65-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.65-5
- Perl 5.38 rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.65-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.65-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.65-2
- Perl 5.36 rebuild

* Fri May 13 2022 Paul Howarth <paul@city-fan.org> - 0.65-1
- 0.65 bump

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.64-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.64-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.64-3
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.64-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Sep 17 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.64-1
- 0.64 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.63-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.63-4
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.63-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.63-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 22 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.63-1
- 0.63 bump

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.61-2
- Perl 5.30 rebuild

* Sun Mar 31 2019 Paul Howarth <paul@city-fan.org> - 0.61-1
- Update to 0.61
  - Fix a couple of typos (GH#1)

* Sat Mar 30 2019 Paul Howarth <paul@city-fan.org> - 0.60-1
- Update to 0.60
  - Updates for BDB 6.2 and BDB 6.3
  - Expose set_lg_filemode (CPAN RT#124979)
  - Added meta-json.t and meta-yaml.t
  - Moved source to github: https://github.com/pmqs/BerkeleyDB
  - Add META_MERGE to Makefile.PL
- Add patch to fix a couple of typos
  https://github.com/pmqs/BerkeleyDB/pull/1

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.55-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.55-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.55-12
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.55-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.55-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.55-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.55-8
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.55-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.55-6
- Perl 5.24 rebuild

* Thu Apr 21 2016 Paul Howarth <paul@city-fan.org> - 0.55-5
- Fix FTBFS due to missing buildreq perl-devel
- Simplify find commands using -empty and -delete

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.55-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.55-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.55-2
- Perl 5.22 rebuild

* Sun Feb 22 2015 Paul Howarth <paul@city-fan.org> - 0.55-1
- Update to 0.55
  - Error opening ErrFile with PerlIO_findFILE (CPAN RT#101883)
  - Minor updates for BDB 6.1
- Classify buildreqs by usage

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.54-4
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.54-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.54-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Nov 10 2013 Paul Howarth <paul@city-fan.org> - 0.54-1
- Update to 0.54
  - Fix memory leak in CDS locking routines (CPAN RT#90134)

* Wed Oct 09 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.53-2
- Rebuild against libdb 5.3.28

* Fri Aug 16 2013 Paul Howarth <paul@city-fan.org> 0.53-1
- Update to 0.53
  - BerkeleyDB 0.52 failed to build on 5.18.1RC3 (CPAN RT#87771)
  - Typo fixes (CPAN RT#86705)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.52-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 0.52-2
- Perl 5.18 rebuild

* Tue Jun 11 2013 Paul Howarth <paul@city-fan.org> 0.52-1
- Update to 0.52
  - Updates for BDB 6.0 - added Blob support
    - Added BerkeleyDB::DbStream class to interface to Blobs
    - Added BlobThreshold and BlobDir options to BerkeleyDB::Env constructor
    - Added BlobThreshold and BlobDir options to Hash, Btree and Heap
      constructors
    - Added get_blob_threshold method to BerkeleyDB::Env
    - Added get_blob_dir method to BerkeleyDB::Env
    - Added get_blob_threshold method to Hash, Btree and Heap
    - Added get_blob_dir method to Hash, Btree and Heap
  - Added method $cursor->set_partial
  - Added method $cursor->partial_clear
  - Fixed $env->lock_detect dies due to incorrect version check (CPAN RT#84179)
  - Fixed memory leak in db_verify() method with libdb < 4.2 (CPAN RT##84409)
  - Fixed a few croaks
- Drop %%defattr, redundant since rpm 4.4

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.51-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.51-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 09 2012 Petr Pisar <ppisar@redhat.com> - 0.51-2
- Perl 5.16 rebuild

* Thu Jul  5 2012 Paul Howarth <paul@city-fan.org> - 0.51-1
- Update to 0.51
  - Documentation updated courtesy of Mike Caron
  - Croak if attempt to freeze BerkeleyDB object (CPAN RT#69985)
  - Rework FETCHSIZE (CPAN RT#75691)
- BR: perl(AutoLoader), perl(Carp), perl(Exporter) and perl(IO::File)
- Anticipate RHEL 7 having libdb
- Mention in %%description that this module doesn't support db1
- Don't need to remove empty directories from buildroot
- Don't use macros for commands
- Don't need to BR: bundled perl(Test::More)

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 0.49-5
- Perl 5.16 rebuild

* Thu Apr 05 2012 Jindrich Novy <jnovy@redhat.com> - 0.49-4
- Rebuild against libdb 5.3.15

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.49-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Sep 21 2011 Paul Howarth <paul@city-fan.org> - 0.49-2
- Rebuild for libdb 5.2.36 in Rawhide

* Sun Sep 18 2011 Steven Pritchard <steve@kspei.com> 0.49-1
- Update to 0.49.
- BR Cwd (not in core now).

* Sun Jun 19 2011 Paul Howarth <paul@city-fan.org> - 0.48-2
- Perl mass rebuild

* Sun Jun 19 2011 Paul Howarth <paul@city-fan.org> - 0.48-1
- Update to 0.48
  - Added support for db_exists and lock_detect
  - Fixed bug with c_pget when the DB_GET_BOTH flag is used
  - Fixed bug with db_pget when the DB_GET_BOTH flag is used
  - Changes to build with BDB 5.2
  - Add support for new Heap database format
  - Fixed test harness issue with Heap.t (CPAN RT#68818)
- Don't package build tools mkconsts.pl and scan.pl

* Sun Jun 19 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.43-6
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.43-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Feb  4 2011 Paul Howarth <paul@city-fan.org> - 0.43-4
- Rebuild for libdb 5.1.25 in Rawhide

* Wed Sep 29 2010 jkeating - 0.43-3
- Rebuilt for gcc bug 634757

* Sun Sep 12 2010 Paul Howarth <paul@city-fan.org> - 0.43-2
- Rebuild for libdb 5.1.19 in Rawhide

* Tue Aug  3 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.43-1
- Update to 0.43
  - Changes to build with BDB 5.1
  - Dropped support for Server option when creating an environment
  - Documentation updates (CPAN RT#59202)
  - Fixed compilation error with MS Visual Studio 2005 (CPAN RT#59924)

* Wed Jul  7 2010 Paul Howarth <paul@city-fan.org> - 0.42-1
- Update to 0.42
  - added $db->Env method to retrieve environment object from a database object
  - get the tied interface to use truncate in the CLEAR method if available
- Build with libdb (Berkeley DB 5.x) from Fedora 14 onwards (#612139)
- Tag BerkeleyDB.pod as %%doc
- Use DESTDIR rather than PERL_INSTALL_ROOT

* Tue May 25 2010 Paul Howarth <paul@city-fan.org> - 0.41-3
- Rebuild for Berkeley DB 4.8.30 in F-13 and Rawhide (#592209)
- Hard-code Berkeley DB requirement to avoid problems like #592209
- Add %%{?perl_default_filter}

* Thu Apr 29 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.41-2
- Mass rebuild with perl-5.12.0

* Sat Feb 13 2010 Steven Pritchard <steve@kspei.com> 0.41-1
- Update to 0.41.

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.39-2
- rebuild against perl 5.10.1

* Sat Aug 29 2009 Steven Pritchard <steve@kspei.com> 0.39-1
- Update to 0.39.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jun 04 2009 Steven Pritchard <steve@kspei.com> 0.38-1
- Update to 0.38.

* Thu Jun 04 2009 Steven Pritchard <steve@kspei.com> 0.36-1
- Update to 0.36.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu May 15 2008 Steven Pritchard <steve@kspei.com> 0.34-1
- Update to 0.34.

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.33-3
Rebuild for new perl

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.33-2
- Autorebuild for GCC 4.3

* Mon Jan 28 2008 Steven Pritchard <steve@kspei.com> 0.33-1
- Update to 0.33.
- Update License tag.
- BR Test::More.

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 0.32-2
- Rebuild for selinux ppc32 issue.

* Fri Jul 13 2007 Steven Pritchard <steve@kspei.com> 0.32-1
- Update to 0.32.

* Tue Apr 17 2007 Steven Pritchard <steve@kspei.com> 0.31-3
- BR ExtUtils::MakeMaker.

* Mon Oct 16 2006 Steven Pritchard <steve@kspei.com> 0.31-2
- Rebuild.

* Mon Oct 16 2006 Steven Pritchard <steve@kspei.com> 0.31-1
- Update to 0.31.
- Use fixperms macro instead of our own chmod incantation.

* Wed Sep 13 2006 Steven Pritchard <steve@kspei.com> 0.30-1
- Update to 0.30.

* Mon Aug 28 2006 Steven Pritchard <steve@kspei.com> 0.29-2
- Minor spec cleanup.

* Fri Jul 07 2006 Steven Pritchard <steve@kspei.com> 0.29-1
- Update to 0.29.

* Fri Jun 30 2006 Steven Pritchard <steve@kspei.com> 0.28-1
- Update to 0.28

* Sat Feb 18 2006 Steven Pritchard <steve@kspei.com> 0.27-2
- Rebuild

* Tue Jan 10 2006 Steven Pritchard <steve@kspei.com> 0.27-1
- Update to 0.27

* Wed Oct 12 2005 Steven Pritchard <steve@kspei.com> 0.26-6
- Another rebuild

* Sat Sep 24 2005 Steven Pritchard <steve@kspei.com> 0.26-5
- Rebuild for new db4 in rawhide

* Mon Sep 05 2005 Steven Pritchard <steve@kspei.com> 0.26-4
- Spec cleanup
- Include COPYING and Artistic

* Wed Aug 03 2005 Steven Pritchard <steve@kspei.com> 0.26-3
- Move OPTIMIZE to Makefile.PL instead of make

* Mon Aug 01 2005 Steven Pritchard <steve@kspei.com> 0.26-2
- Various fixes from Paul Howarth:
  - Add description
  - Fix permissions on docs (also Paul Howarth)
  - Add OPTIMIZE to make
  - Don't own perl_vendorarch/auto/
  - BuildRequire Test::Pod and MLDBM

* Wed Jul 06 2005 Steven Pritchard <steve@kspei.com> 0.26-1
- Specfile autogenerated.
- Add BuildRequires db4-devel.
- Install dbinfo script.
