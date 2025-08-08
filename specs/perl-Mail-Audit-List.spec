Name:           perl-Mail-Audit-List
Version:        1.853
Release:        %{autorelease}
Summary:        Mail::Audit plugin for automatic list delivery

License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Mail-Audit-List
Source0:        https://cpan.metacpan.org/modules/by-module/Mail/Mail-Audit-List-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Mail::Audit) >= 2.217
BuildRequires:  perl(Mail::ListDetector)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(blib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter

%{?perl_default_filter}


%description
This is a Mail::Audit plugin which provides a method for automatically
delivering mailing lists to a suitable mainbox. It requires the CPAN
Mail::ListDetector module.


%prep
%autosetup -n Mail-Audit-List-%{version}


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
%doc Changes README
%{_mandir}/man3/Mail::Audit::List.3pm*
%{perl_vendorlib}/Mail/Audit/List.pm


%changelog
%{autochangelog}
