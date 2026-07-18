# The tests don't work in mock, they can be run on local machine
%bcond_with testsuite

Name:           perl-Filesys-Fuse3
Version:        0.021
Release:        2%{?dist}
Summary:        Write filesystems in Perl using Fuse3
License:        LGPL-2.1-only
URL:            https://metacpan.org/dist/Filesys-Fuse3
Source0:        https://cpan.metacpan.org/authors/id/D/DD/DDUMONT/Filesys-Fuse3-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(POSIX)
BuildRequires:  pkgconf-pkg-config
BuildRequires:  pkgconfig(fuse3) >= 2.6
%if %{with testsuite}
# Run-time
BuildRequires:  fuse3
BuildRequires:  perl(:VERSION) >= 5.20
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(English)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(Filesys::Statvfs)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Unix::Mknod)
%endif
Requires:       fuse3

%description
This module lets you implement filesystems in Perl, through the FUSE
(Filesystem in USErspace) kernel/lib interface.

%prep
%setup -q -n Filesys-Fuse3-%{version}
chmod -x examples/*

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} %{buildroot}/*

%check
%if %{with testsuite}
unset FAKEROOTKEY LOGNAME
make test
%endif

%files
%doc AUTHORS Changes examples README.md
%{perl_vendorarch}/auto/Filesys/
%{perl_vendorarch}/Filesys/
%{_mandir}/man3/Filesys::Fuse3*

%changelog
* Thu Jul 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.021-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Wed Jun 10 2026 Jitka Plesnikova <jplesnik@redhat.com> - 0.021-1
- Initial package
