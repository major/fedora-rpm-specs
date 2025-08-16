# Perform optional tests
%bcond_without perl_Mail_DMARC_enables_optional_test

Name:           perl-Mail-DMARC
Version:        1.20250805
Release:        1%{?dist}
Summary:        Perl implementation of DMARC
# README.md and other files:    GPL-1.0-or-later OR Artistic-1.0-Perl
# share/public_suffix_list:     MPL-2.0
## Not used at build time and not in binary package
# repackage.sh:                 GPL-2.0-or-later
## Stripped from the original upstream archive
# share/html/js:                MIT OR GPL-1.0-or-later
# share/html/plugins/grid.addons.js.gz:         MIT OR GPL-1.0-or-later
# share/html/plugins/grid.postext.js.gz:        MIT OR GPL-1.0-or-later
# share/html/plugins/grid.setcolumns.js.gz:     MIT OR GPL-1.0-or-later
# share/html/plugins/jquery.contextmenu.js.gz:  MIT OR GPL-1.0-or-later
# share/html/plugins/jquery.searchFilter.js.gz: MIT OR GPL-2.0-only
# share/html/plugins/jquery.tablednd.js.gz:     "Licensed like jQuery", i.e. MIT
# share/html/plugins/ui.multiselect.js.gz:      MIT OR GPL-1.0-or-later
# other files under share/html except of share/html/index.html are part of
# jqgrid.
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND MPL-2.0
SourceLicense:  %{license} AND GPL-2.0-or-later
URL:            https://metacpan.org/dist/Mail-DMARC
# Original upstream Source0 URL
# https://cpan.metacpan.org/authors/id/M/MS/MSIMERSON/Mail-DMARC-%%{version}.tar.gz
# contains minified historical jqgrid. Distributing minified code is against
# Fedora packaging guidelines. Current <https://github.com/tonytomov/jqGrid>
# is non-free CC-BY-NC-3.0.
Source0:        Mail-DMARC-%{version}_repackaged.tar.gz
Source1:        repackage.sh
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::ShareDir::Install) >= 0.06
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.10.0
BuildRequires:  perl(Carp)
BuildRequires:  perl(CGI)
BuildRequires:  perl(Config::Tiny)
# CPAN never used, bin/install_deps.pl not used and not installed.
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DBD::SQLite) >= 1.31
BuildRequires:  perl(DBIx::Simple) >= 1.35
BuildRequires:  perl(Email::MIME)
BuildRequires:  perl(Email::Sender)
BuildRequires:  perl(Email::Sender::Simple) >= 1.300032
BuildRequires:  perl(Email::Sender::Transport::SMTP)
BuildRequires:  perl(Email::Sender::Transport::SMTP::Persistent)
BuildRequires:  perl(Email::Sender::Transport::Test)
BuildRequires:  perl(Email::Simple)
BuildRequires:  perl(Encode)
BuildRequires:  perl(English)
BuildRequires:  perl(File::ShareDir) >= 1.00
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Tiny)
BuildRequires:  perl(IO::Compress::Gzip)
BuildRequires:  perl(IO::Compress::Zip)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(IO::Uncompress::Gunzip)
BuildRequires:  perl(IO::Uncompress::Unzip)
BuildRequires:  perl(JSON)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Mail::DKIM::PrivateKey)
BuildRequires:  perl(Mail::DKIM::Signer)
BuildRequires:  perl(Mail::DKIM::TextWrap)
BuildRequires:  perl(Module::Load)
BuildRequires:  perl(Net::DNS::Resolver)
BuildRequires:  perl(Net::IDN::Encode)
BuildRequires:  perl(Net::IMAP::Simple)
BuildRequires:  perl(Net::IP)
BuildRequires:  perl(Net::Server::HTTP)
BuildRequires:  perl(parent)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Regexp::Common) >= 2013031301
BuildRequires:  perl(Socket)
BuildRequires:  perl(Socket6) >= 0.23
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Sys::Syslog)
BuildRequires:  perl(URI)
BuildRequires:  perl(XML::LibXML)
# Optional run-time:
BuildRequires:  perl(Net::HTTP)
# Tests only:
BuildRequires:  perl(Email::Sender::Transport::Failable)
BuildRequires:  perl(lib)
BuildRequires:  perl(Net::DNS::Resolver::Mock)
BuildRequires:  perl(Test::File::ShareDir)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Output)
%if %{with perl_Mail_DMARC_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(XML::SAX::ParserFactory)
BuildRequires:  perl(XML::Validator::Schema)
%endif
Requires:       perl(DBD::SQLite) >= 1.31
Requires:       perl(DBIx::Simple) >= 1.35
Requires:       perl(Email::Sender::Simple) >= 1.300032
Requires:       perl(File::ShareDir) >= 1.00
Requires:       perl(Mail::DKIM::PrivateKey)
Requires:       perl(Mail::DKIM::Signer)
Requires:       perl(Mail::DKIM::TextWrap)
Recommends:     perl(Net::HTTP)
Requires:       perl(Net::IMAP::Simple)
Requires:       perl(Socket6) >= 0.23

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((File::ShareDir|DBIx::Simple|Email::Sender::Simple|Socket6)\\)$

%description
This module is a suite of tools for implementing DMARC. It adheres to the
2013 DMARC draft.

%package HTTP
Summary:        Web server for DMARC validation and report viewing
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(File::ShareDir) >= 1.00

%description HTTP
Mail::DMARC::HTTP Perl module and dmarc_httpd tool for viewing DMARC reports.
This package is has intentionally left out jqgrid JavaScript and CSS files
because of missing their source code.

%package Test
Summary:        Perl modules for testing Mail::DMARC framework
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description Test
Public Perl modules of Mail::DMARC framework which have no other use than
performing internal tests.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-HTTP = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-Test = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness
%if %{with perl_Mail_DMARC_enables_optional_test}
Requires:       perl(XML::SAX::ParserFactory)
Requires:       perl(XML::Validator::Schema)
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%autosetup -p1 -n Mail-DMARC-%{version}
%if %{without perl_Mail_DMARC_enables_optional_test}
rm t/17.Report.Aggregate.Schema.t
perl -i -ne 'print $_ unless m{\Qt/17.Report.Aggregate.Schema.t\E}' MANIFEST
%endif
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
ln -s -r %{buildroot}%{perl_vendorlib}/auto/share/dist/Mail-DMARC \
    %{buildroot}%{_libexecdir}/%{name}/share
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# Tests write into CWD
DIR=$(mktemp -d)
cp -a --dereference %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"
unset HTTP_ACCEPT_ENCODING MAIL_DMARC_CONFIG_FILE
prove -I .
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset HTTP_ACCEPT_ENCODING MAIL_DMARC_CONFIG_FILE
# The tests are not parallel-safe, they write to CWD, and are not indempotent.
export HARNESS_OPTIONS=j1
make test

%files
%license LICENSE
%doc Changes.md DEVELOP.md example FAQ.md README.md TODO.md
%{_bindir}/dmarc_http_client
%{_bindir}/dmarc_lookup
%{_bindir}/dmarc_receive
%{_bindir}/dmarc_send_reports
%{_bindir}/dmarc_update_public_suffix_list
%{_bindir}/dmarc_view_reports
%dir %{perl_vendorlib}/Mail
%{perl_vendorlib}/Mail/DMARC.pm
%dir %{perl_vendorlib}/Mail/DMARC
%{perl_vendorlib}/Mail/DMARC/Base.pm
%{perl_vendorlib}/Mail/DMARC/Policy.pm
%{perl_vendorlib}/Mail/DMARC/PurePerl.pm
%{perl_vendorlib}/Mail/DMARC/Report
%{perl_vendorlib}/Mail/DMARC/Report.pm
%{perl_vendorlib}/Mail/DMARC/Result
%{perl_vendorlib}/Mail/DMARC/Result.pm
%dir %{perl_vendorlib}/auto
%dir %{perl_vendorlib}/auto/share
%{perl_vendorlib}/auto/share/dist/Mail-DMARC
%{_mandir}/man1/dmarc_http_client.*
%{_mandir}/man1/dmarc_lookup.*
%{_mandir}/man1/dmarc_receive.*
%{_mandir}/man1/dmarc_send_reports.*
%{_mandir}/man1/dmarc_update_public_suffix_list.*
%{_mandir}/man1/dmarc_view_reports.*
%{_mandir}/man3/Mail::DMARC.*
%{_mandir}/man3/Mail::DMARC::Base.*
%{_mandir}/man3/Mail::DMARC::Policy.*
%{_mandir}/man3/Mail::DMARC::PurePerl.*
%{_mandir}/man3/Mail::DMARC::Report.*
%{_mandir}/man3/Mail::DMARC::Report::*
%{_mandir}/man3/Mail::DMARC::Result.*
%{_mandir}/man3/Mail::DMARC::Result::*

%files HTTP
%{_bindir}/dmarc_httpd
%{perl_vendorlib}/Mail/DMARC/HTTP.pm
%{_mandir}/man1/dmarc_httpd.*
%{_mandir}/man3/Mail::DMARC::HTTP.*

%files Test
%{perl_vendorlib}/Mail/DMARC/Test

%files tests
%{_libexecdir}/%{name}

%changelog
* Thu Aug 14 2025 Petr Pisar <ppisar@redhat.com> - 1.20250805-1
- 1.20250805 bump

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.20250610-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon Jun 16 2025 Petr Pisar <ppisar@redhat.com> - 1.20250610-1
- 1.20250610 bump

* Tue May 27 2025 Petr Pisar <ppisar@redhat.com> - 1.20250203-2
- Require dependecnies for optional test in perl-Mail-DMARC-tests

* Wed May 21 2025 Petr Pisar <ppisar@redhat.com> 1.20250203-1
- 1.20250203 version packaged
- JavaScript and CSS files for dmarc_httpd removed because of no source code
