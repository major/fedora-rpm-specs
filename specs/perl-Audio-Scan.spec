Name:           perl-Audio-Scan
Version:        1.13
Release:        %{autorelease}
Summary:        Fast C metadata and tag reader for all common audio file formats
URL:            https://metacpan.org/dist/Audio-Scan
Source0:        https://cpan.metacpan.org/authors/id/E/EL/ELBRUS/Audio-Scan-%{version}.tar.gz

# https://github.com/LMS-Community/Audio-Scan/pull/18
Patch:          0001-Detail-licences.patch
License:        GPL-2.0-or-later AND BSD-2-Clause AND BSD-3-Clause AND MIT AND SSH-OpenSSH AND Zlib

# Contains code derived from libmpcdec/streaminfo.c
Provides:       bundled(libmpcdec)

BuildRequires:  /usr/bin/chmod
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  zlib-devel

%{?perl_default_filter}

%description
This module implements several image resizing algorithms for Perl, with a
focus on low overhead, speed and minimal features.


%prep
%autosetup -p1 -n Audio-Scan-%{version}


%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}


%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*


%check
make test


%files
%license COPYING
%license COPYING.ape
%license COPYING.buffer
%license COPYING.mpc
%license COPYING.pinttypes
%license COPYING.pstdint
%doc Changes
%doc README
%dir %{perl_vendorarch}/Audio
%{perl_vendorarch}/Audio/Scan.pm
%dir %{perl_vendorarch}/auto/Audio
%{perl_vendorarch}/auto/Audio/Scan/Scan.so
%{_mandir}/man3/Audio::Scan.3pm*


%changelog
%{autochangelog}
