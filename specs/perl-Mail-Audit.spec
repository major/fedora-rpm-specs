Name:           perl-Mail-Audit
Version:        2.228
Release:        %{autorelease}
Summary:        Library for creating easy mail filters

License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Mail-Audit
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Mail-Audit-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::HomeDir) >= 0.61
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::Tempdir)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(MIME::Entity)
BuildRequires:  perl(MIME::Parser)
BuildRequires:  perl(Mail::Internet)
BuildRequires:  perl(Mail::Mailer)
BuildRequires:  perl(Mail::POP3Client)
BuildRequires:  perl(Mail::Send)
BuildRequires:  perl(Net::SMTP)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Parse::RecDescent)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Test::More) => 0.96
BuildRequires:  perl(blib)
BuildRequires:  perl(constant)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter

%{?perl_default_filter}


%description
Mail::Audit was inspired by Tom Christiansen's audit_mail and deliverlib
programs. It allows a piece of email to be logged, examined, accepted into
a mailbox, filtered, resent elsewhere, rejected, replied to, and so on. It's
designed to allow you to easily create filter programs to stick in a .forward
file or similar.


%prep
%autosetup -n Mail-Audit-%{version}


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
%doc Changes FAQ README
%{_bindir}/popread
%{_bindir}/proc2ma
%{_mandir}/man1/popread.1*
%{_mandir}/man1/proc2ma.1*
%{_mandir}/man3/Mail::Audit.3pm*
%{_mandir}/man3/Mail::Audit::KillDups.3pm*
%{_mandir}/man3/Mail::Audit::MAPS.3pm*
%{_mandir}/man3/Mail::Audit::MailInternet.3pm*
%{_mandir}/man3/Mail::Audit::MimeEntity.3pm*
%{_mandir}/man3/Mail::Audit::Util::Tempdir.3pm*
%{_mandir}/man3/Mail::Audit::Vacation.3pm*
%dir %{perl_vendorlib}/Mail/Audit
%{perl_vendorlib}/Mail/Audit.pm
%{perl_vendorlib}/Mail/Audit/KillDups.pm
%{perl_vendorlib}/Mail/Audit/MAPS.pm
%{perl_vendorlib}/Mail/Audit/MailInternet.pm
%{perl_vendorlib}/Mail/Audit/MimeEntity.pm
%dir %{perl_vendorlib}/Mail/Audit/Util
%{perl_vendorlib}/Mail/Audit/Util/Tempdir.pm
%{perl_vendorlib}/Mail/Audit/Vacation.pm


%changelog
%{autochangelog}
