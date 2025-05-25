Name:           imapfilter
Version:        2.8.3
Release:        %autorelease
Summary:        A flexible client side mail filtering utility for IMAP servers

%global forgeurl https://github.com/lefcha/imapfilter/
%forgemeta

# SPDX
License:        MIT
URL:            %forgeurl
Source:         %forgesource
# Fix paths for MANDIR, SSLCAFILE and keep existing CFLAGS
Patch0:         imapfilter-makefile-fix.patch

BuildRequires:  gcc, make
BuildRequires:  openssl-devel
BuildRequires:  lua-devel
BuildRequires:  pcre2-devel


%description
IMAPFilter is a mail filtering utility. It connects to remote mail servers
using the Internet Message Access Protocol (IMAP), sends searching queries
to the server and processes mailboxes based on the results. It can be used
to delete, copy, move, flag, etc. messages residing in mailboxes at the
same or different mail servers. The 4rev1 and 4 versions of the IMAP
protocol are supported.


%prep
%forgeautosetup -p1


%build
# imapfilter does not have any autotools based ./configure - just a plain Makefile
CFLAGS=$RPM_OPT_FLAGS make PREFIX=%{_prefix} %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install PREFIX=%{_prefix} DESTDIR=$RPM_BUILD_ROOT


%files
%doc README AUTHORS NEWS
%license LICENSE
%{_bindir}/imapfilter
%{_datadir}/imapfilter/
%{_mandir}/man1/imapfilter.1.gz
%{_mandir}/man5/imapfilter_config.5.gz


%changelog
%autochangelog
