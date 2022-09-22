Name:           public-inbox
Version:        1.9.0
Release:        %autorelease
Summary:        An archives-first approach to mailing lists

License:        AGPLv3
URL:            https://public-inbox.org
Source0:        %{url}/public-inbox.git/snapshot/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(Email::Address::XS)
# Fedora's highlight currently built without Perl bindings
# BuildRequires:  perl(highlight)
BuildRequires:  perl(Inline::C)
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(Mail::IMAPClient)
BuildRequires:  perl(Parse::RecDescent)
BuildRequires:  perl(Plack::Middleware::ReverseProxy)
BuildRequires:  perl(Plack::Test)
BuildRequires:  perl(Search::Xapian)
BuildRequires:  pkgconfig(libgit2)
BuildRequires:  curl
BuildRequires:  e2fsprogs
BuildRequires:  git >= 2.6
BuildRequires:  man-db
BuildRequires:  sqlite
BuildRequires:  xapian-core
Requires:       perl-PublicInbox = %{version}-%{release}
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
# not automatically picked up since it's required dynamically
# via `eval` in Search.pm. *shudders*
Requires:       perl(Search::Xapian)

%global __requires_exclude ^perl\\((highlight|IO::KQueue)\\)
%{?perl_default_filter}

%description
public-inbox implements the sharing of an email inbox via git to complement or
replace traditional mailing lists. Readers may read via NNTP, IMAP, Atom feeds
or HTML archives.

%package -n perl-PublicInbox
Summary:        Perl libraries for public-inbox
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
#Requires: git >= 2.6, libgit2, perl-DBD-SQLite, perl-Search-Xapian, xapian-core, perl-URI, perl-TimeDate, perl-Mail-IMAPClient, perl-Linux-Inotify2, perl-Email-Address-XS, perl-sort, perl-Sys-Syslog, perl-Sys-Hostname, perl-Inline-C, sqlite

%description -n perl-PublicInbox
Perl libraries for public-inbox.

%package server
Summary:        public-inbox server-side components
Requires:       %{name} = %{version}-%{release}

%description server
Server-side components and daemons for public-inbox.


%package -n lei
Summary:        Local Email Interface for public-inbox
Requires:       %{name} = %{version}-%{release}

%description -n lei
The client-side component of public-inbox that allows to interact with mail
storage systems, including public-inbox servers.


%prep
%autosetup


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make_build


%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
%{_fixperms} $RPM_BUILD_ROOT/*
for MANS in 1 5 7 8; do
    mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man$MANS
    install -m 0644 *.$MANS $RPM_BUILD_ROOT/%{_mandir}/man$MANS/
done
mkdir -p -m 0755 $RPM_BUILD_ROOT/%{_sysconfdir}/bash_completion.d
install -m 0644 contrib/completion/* $RPM_BUILD_ROOT/%{_sysconfdir}/bash_completion.d/


%check
(cd certs && %{__perl} ./create-certs.perl)
mkdir -p $RPM_BUILD_ROOT/tmp
PERL_INLINE_DIRECTORY=$RPM_BUILD_ROOT/tmp make test
rm -rf $RPM_BUILD_ROOT/tmp


%files
%license COPYING
%doc AUTHORS HACKING NEWS README TODO
%{_bindir}/public-inbox-clone
%{_bindir}/public-inbox-compact
%{_bindir}/public-inbox-convert
%{_bindir}/public-inbox-edit
%{_bindir}/public-inbox-extindex
%{_bindir}/public-inbox-fetch
%{_bindir}/public-inbox-index
%{_bindir}/public-inbox-init
%{_bindir}/public-inbox-learn
%{_bindir}/public-inbox-netd
%{_bindir}/public-inbox-pop3d
%{_bindir}/public-inbox-purge
%{_bindir}/public-inbox-watch
%{_bindir}/public-inbox-xcpdb
%{_mandir}/man1/public-inbox-*.1*
%{_mandir}/man5/public-inbox-*.5*
%{_mandir}/man7/public-inbox-*.7*
%{_mandir}/man8/public-inbox-*.8*
%exclude %{_mandir}/man1/public-inbox.cgi.1*
%exclude %{_mandir}/man1/public-inbox-httpd.1*
%exclude %{_mandir}/man1/public-inbox-imapd.1*
%exclude %{_mandir}/man1/public-inbox-mda.1*
%exclude %{_mandir}/man1/public-inbox-nntpd.1*

%files -n lei
%{_bindir}/lei
%{_mandir}/man1/lei*.1*
%{_mandir}/man5/lei-*.5*
%{_mandir}/man7/lei-*.7*
%{_mandir}/man8/lei-*.8*
%{_sysconfdir}/bash_completion.d/lei-completion.bash

%files -n perl-PublicInbox
%license COPYING
%{perl_vendorlib}/*
%{_mandir}/man3/PublicInbox::*.3*

%files server
%{_bindir}/public-inbox.cgi
%{_bindir}/public-inbox-httpd
%{_bindir}/public-inbox-imapd
%{_bindir}/public-inbox-mda
%{_bindir}/public-inbox-nntpd
%{_mandir}/man1/public-inbox.cgi.1*
%{_mandir}/man1/public-inbox-httpd.1*
%{_mandir}/man1/public-inbox-imapd.1*
%{_mandir}/man1/public-inbox-mda.1*
%{_mandir}/man1/public-inbox-nntpd.1*


%changelog
%autochangelog
