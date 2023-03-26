# Tests require network access

Name:           perl-MusicBrainz-DiscID
Version:        0.06
Release:        %autorelease
Summary:        Perl interface for the MusicBrainz libdiscid library
License:        MIT
URL:            https://metacpan.org/release/MusicBrainz-DiscID
Source0:        https://cpan.metacpan.org/authors/id/N/NJ/NJH/MusicBrainz-DiscID-%{version}.tar.gz
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  libdiscid-devel
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::Depends), perl(ExtUtils::PkgConfig)
BuildRequires:  perl(ExtUtils::MakeMaker)

%{?perl_default_filter}

%description
MusicBrainz::DiscID is a class to calculate a MusicBrainz DiscID from an
audio CD in the drive. The coding style is slightly different to the C
interface to libdiscid, because it makes use of perl's Object Oriented
functionality.

%prep
%setup -q -n MusicBrainz-DiscID-%{version}
chmod -c a-x examples/*.pl

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -empty -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
%{?_with_testsuite:make test}

%files
%doc Changes README*
%{perl_vendorarch}/MusicBrainz*
%{perl_vendorarch}/auto/MusicBrainz/
%{_mandir}/man3/*.3pm*

%changelog
%autochangelog
