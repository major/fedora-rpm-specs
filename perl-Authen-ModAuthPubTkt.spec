Name:           perl-Authen-ModAuthPubTkt
Version:        0.1.1
Release:        %autorelease
Summary:        Generate Tickets (Signed HTTP Cookies) for mod_auth_pubtkt protected websites
# Relicensed as Perl license
# See https://github.com/agordon/Authen-ModAuthPubTkt/issues/1
License:        GPL+ or Artistic
URL:            https://metacpan.org/dist/Authen-ModAuthPubTkt
Source0:        https://cpan.metacpan.org/authors/id/A/AG/AGORDON/Authen-ModAuthPubTkt-%{version}.tar.gz
# Relicensed as Perl license
# See https://github.com/agordon/Authen-ModAuthPubTkt/issues/1
Patch0:         https://github.com/agordon/Authen-ModAuthPubTkt/commit/4bd05a0baefa30f264bff9bc4be7a8ddda9251d6.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  openssl
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IPC::Run3)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
Requires:       openssl

%description
This module generates and verifies a mod_auth_pubtkt-compatible ticket
string, which should be used as a cookie with the rest of the
mod_auth_pubtkt (https://neon1.net/mod_auth_pubtkt/) system.

%prep
%setup -q -n Authen-ModAuthPubTkt-%{version}
%patch0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
# https://rt.cpan.org/Public/Bug/Display.html?id=110752
rm -rfv t/02-generate-dsa.t t/04-verify-dsa.t
make test

%files
%doc Changes ignore.txt META.json README
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* lun. janv. 10 2022 Robert-André Mauchin <zebob.m@gmail.com> 0.1.1-2
- Uncommitted changes

* dim. oct. 10 2021 Robert-André Mauchin <zebob.m@gmail.com> 0.1.1-1
- Initial release
