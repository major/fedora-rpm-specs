Name:           perl-Mail-ListDetector
Version:        1.04
Release:        %{autorelease}
Summary:        Perl extension for detecting mailing list messages

License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Mail-ListDetector
Source0:        https://cpan.metacpan.org/modules/by-module/Mail/Mail-ListDetector-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Email::Abstract) >= 3.001
BuildRequires:  perl(Email::Valid) >= 0.182
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(Mail::Internet) >= 2.04
BuildRequires:  perl(Test::More) >= 0.08
BuildRequires:  perl(URI) > 1.10
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter

%{?perl_default_filter}


%description
This module analyzes mail objects in any of the classes handled by
Email::Abstract. It returns a Mail::ListDetector::List object representing
the mailing list.


%prep
%autosetup -n Mail-ListDetector-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build


%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*


%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test


%files
%license LICENSE
%doc AUTHORS README
%{_mandir}/man3/Mail::ListDetector*.3pm*
%{perl_vendorlib}/*


%changelog
%{autochangelog}
