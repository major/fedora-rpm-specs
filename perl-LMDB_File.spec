Name:           perl-LMDB_File
Version:        0.12
Release:        24%{?dist}
Summary:        Perl5 wrapper around the OpenLDAP's LMDB
License:        (GPL+ or Artistic) and Artistic 2.0
URL:            https://metacpan.org/release/LMDB_File
Source0:        https://cpan.metacpan.org/authors/id/S/SO/SORTIZ/LMDB_File-0.12.tar.gz
Patch0:         0001-Fix-tests-on-ppc64-le-architecture.patch
# Fix building with Perl 5.28.0, CPAN RT#125707
Patch1:         LMDB_File-0.12-Fix-passing-mdb_strerror-value-to-croak.patch

# BZ1524377
ExcludeArch:    armv7hl i686

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  libdb-devel
BuildRequires:  lmdb-devel >= 0.9.17
BuildRequires:  perl(:VERSION) >= 5.10.0
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Makefile:
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::Constant)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
# Tests:
BuildRequires:  perl(B)
BuildRequires:  perl(Benchmark)
BuildRequires:  perl(bytes)
BuildRequires:  perl(Devel::Peek)
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(utf8)

Requires:       lmdb-libs
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(AutoLoader)
Requires:       perl(Carp)
Requires:       perl(Exporter)
Requires:       perl(Fcntl)
Requires:       perl(Scalar::Util)
Requires:       perl(XSLoader)
Requires:       perl(strict)
Requires:       perl(warnings)
Requires:       rtld(GNU_HASH)
  
%{?perl_default_filter}

%description
LMDB_File is a Perl wrapper around the OpenLDAP's LMDB (Lightning
Memory-Mapped Database) C library.
LMDB is an ultra-fast, ultra-compact key-value data store developed
by Symas for the OpenLDAP Project. See http://symas.com/mdb/ for details.
LMDB_File provides full access to the complete C API, a thin Perl wrapper
with an Object-Oriented interface and a simple Perl's tie interface
compatible with others DBMs.


%prep
%setup -q -n LMDB_File-%{version}
%patch0 -p1
%patch1 -p1


%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1 NO_PERLLOCAL=1
make %{?_smp_mflags}


%install
%make_install
%{_fixperms} $RPM_BUILD_ROOT/*


%check
make test


%files
%doc Changes README
%license LICENSE
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/LMDB_File*
%{_mandir}/man3/*


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.12-23
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.12-20
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.12-17
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.12-14
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.12-11
- Perl 5.28 rebuild

* Fri Jun 29 2018 Petr Pisar <ppisar@redhat.com> - 0.12-10
- Fix building with Perl 5.28.0 (CPAN RT#125707)

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.12-9
- Perl 5.28 rebuild

* Mon Mar 05 2018 Petr Pisar <ppisar@redhat.com> - 0.12-8
- Adapt to removing GCC from a build root (bug #1547165)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 13 2017 Jakub Janco <jjanco@redhat.com> 0.12-6
- Fix tests on ppc64[le] archs

* Mon Dec 11 2017 Jakub Janco <jjanco@redhat.com> 0.12-5
- Remove s390x from ExcludeArch

* Mon Dec 11 2017 Jakub Janco <jjanco@redhat.com> 0.12-4
- add BZ instead note to ExcludeArch

* Thu Dec 07 2017 Jakub Janco <jjanco@redhat.com> 0.12-3
- require lmdb-libs instead of specific library

* Thu Nov 30 2017 Jakub Janco <jjanco@redhat.com> 0.12-2
- remove libc and liblmdb version dependency

* Tue Oct 24 2017 Jakub Janco <jjanco@redhat.com> 0.12-1
- initial package release
