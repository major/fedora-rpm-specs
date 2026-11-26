%global upstream_name Chipcard-PCSC
%define pcsc_soname libpcsclite.so.1
%if 0%{?__isa_bits} == 64
%define mark64  ()(64bit)
%endif

Name:           pcsc-perl
Version:        1.4.16
Release:        %autorelease
Summary:        Perl interface to the PC/SC smart card library
License:        GPL-2.0-or-later
URL:            https://pcsc-perl.apdu.fr/
Source0:        %{url}%{upstream_name}-v%{version}.tar.gz
Source1:        %{url}%{upstream_name}-v%{version}.tar.gz.asc
# <https://ludovic-rousseau.pages-perso.free.fr/gpg_key_E8F9C57E.txt> contains
# SHA-1 signatures.
# A resigned F5E11B9FFE911146F41D953D78A1B4DFE8F9C57E key from a keyserver is
# rejected by Sequoia with "No binding signature at time
# 2023-11-21T20:36:51Z".
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  glibc-common
BuildRequires:  grep
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  pkgconf-pkg-config
BuildRequires:  pkgconfig(libpcsclite) >= 1.3.0
# No tests are performed
Requires:       pcsc-lite-libs%{?_isa} >= 1.3.0
Requires:       %{pcsc_soname}%{?mark64}
Provides:       perl-pcsc = %{version}-%{release}

%description
This library allows to communicate with a smart card using PC/SC
interface (pcsc-lite) from a Perl script.

%prep
%setup -q -n %{upstream_name}-v%{version}
chmod 644 examples/* # avoid dependencies
f=Changelog ; iconv -f iso-8859-1 -t utf-8 $f > $f.utf8 ; mv $f.utf8 $f

%build
if ! grep -qF 'dlopen("%{pcsc_soname}"' PCSCperl.h ; then # sanity check
    echo "ERROR: pcsc lib name mismatch in PCSCperl.h/dependencies" ; exit 1
fi
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS" DEFINE=-Wall
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -delete
chmod -R u+w $RPM_BUILD_ROOT/*

%check
# tests need configured readers etc

%files
%license LICENCE
%doc Changelog README examples/
%dir %{perl_vendorarch}/auto/Chipcard
%{perl_vendorarch}/auto/Chipcard/PCSC
%dir %{perl_vendorarch}/Chipcard/
%{perl_vendorarch}/Chipcard/PCSC
%{perl_vendorarch}/Chipcard/PCSC.pod
%{perl_vendorarch}/Chipcard/PCSC.pm
%{_mandir}/man3/Chipcard::PCSC.3*
%{_mandir}/man3/Chipcard::PCSC::*.3*

%changelog
%autochangelog
