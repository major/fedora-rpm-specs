%define pcscver 1.3.0
%define pcsclib libpcsclite.so.1
%if 0%{?__isa_bits} == 64
%define mark64  ()(64bit)
%endif

%global upstream_name Chipcard-PCSC

Name:           pcsc-perl
Version:        1.4.16
Release:        %autorelease
Summary:        Perl interface to the PC/SC smart card library

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://pcsc-perl.apdu.fr/
Source0:        %{url}%{upstream_name}-v%{version}.tar.gz
Source1:        %{url}%{upstream_name}-v%{version}.tar.gz.asc

BuildRequires:  gcc
BuildRequires:  coreutils
BuildRequires:  glibc-common
BuildRequires:  grep
BuildRequires:  make
BuildRequires:  pcsc-lite-devel >= %{pcscver}
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
Requires:       %{pcsclib}%{?mark64}
Provides:       perl-pcsc = %{version}-%{release}

%description
This library allows to communicate with a smart card using PC/SC
interface (pcsc-lite) from a Perl script.

%prep
%setup -q -n %{upstream_name}-v%{version}
chmod 644 examples/* # avoid dependencies
f=Changelog ; iconv -f iso-8859-1 -t utf-8 $f > $f.utf8 ; mv $f.utf8 $f


%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" DEFINE=-Wall
make %{?_smp_mflags}


%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
# tests need configured readers etc
if ! grep -qF 'dlopen("%{pcsclib}"' PCSCperl.h ; then # sanity check
    echo "ERROR: pcsc lib name mismatch in PCSCperl.h/dependencies" ; exit 1
fi


%files
%license LICENCE
%doc Changelog README examples/
%{perl_vendorarch}/auto/Chipcard/
%{perl_vendorarch}/Chipcard/
%{_mandir}/man3/Chipcard::PCSC*.3*


%changelog
%autochangelog
