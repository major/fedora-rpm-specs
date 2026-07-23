Name:           perl-Badger
Version:        0.16
Release:        1%{?dist}
Summary:        Perl Application Programming Toolkit
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Badger
Source0:        https://metacpan.org/modules/by-module/Badger/Badger-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# tests
BuildRequires:  perl(FindBin)
BuildRequires:  perl(JSON)
BuildRequires:  perl(YAML)
BuildRequires:  perl(Moose)
# runtime
BuildRequires:  perl(:VERSION) >= 5.8.0
BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(if)
BuildRequires:  perl(IO::Dir)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(lib)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(overload)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
Requires:       perl(Digest::MD5)
Requires:       perl(File::Copy)
Requires:       perl(IO::Dir)
Requires:       perl(IO::File)

%description
The Badger toolkit is a collection of Perl modules designed to simplify the
process of building object-oriented Perl applications. It provides a set of
foundation classes upon which you can quickly build robust and reliable
systems that are simple, sexy and scalable. See Badger::Intro for further
information.

%prep
%setup -q -n Badger-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README TODO
%{perl_vendorlib}/Badger*
%{_mandir}/man3/Badger*3pm*

%changelog
* Thu May 21 2026 Xavier Bachelot <xavier@bachelot.org> 0.16-1
- Initial specfile
