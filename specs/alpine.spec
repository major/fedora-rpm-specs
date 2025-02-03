# Fedora review: http://bugzilla.redhat.com/249365

# crasher workaround, http://bugzilla.redhat.com/1282092
%undefine _hardened_build

Summary: powerful, easy to use console email client
Name: alpine
Version: 2.26
Release: %autorelease

License: Apache-2.0
URL:     https://alpineapp.email/

# alpine-2.26_new_patched.tar.xz was generated from the new upstream location
# wget https://alpineapp.email/alpine/patches/alpine-2.26/alpine-2.26.tar.xz
# mv alpine-2.26.tar.xz alpine_patched-2.26.tar.xz
# alpine-2.26.tar.xz is slightly different between what Fedora has cached and
# what is at the new upstream. The old location no longer exists
# Clearly this shuffle should be removed as soon as a new release appears.
# Source0: https://alpineapp.email/alpine/patches/alpine-2.26/alpine-2.26.tar.xz
Source0: alpine-2.26_patched.tar.xz
Source1: README.fedora

Patch1: alpine-2.24-useragent.patch
Patch2: alpine-2.23-gcc10.patch
Patch3: alpine-configure-c99.patch

# Using "Conflicts" instead of Obsoletes because while alpine is substantially
# compatible with pine the change to Unicode breaks important user
# functionality such as non-ASCII encoded saved passwords. Additionally, there
# are also many patches to pine floating around that for political/technical
# reasons will not be integrated into alpine. (I'd like to stay out of it...
# just search "Mark Crispin maildir" for the gory details.) Since licensing
# prevents a Fedora pine package, I cannot predict what patches users might
# have and so want to warn them instead of automatically replacing their pine
# install with an alpine that could break their configuration. 
# I understand this to be a special case of the "Optional Functionality"
# description at http://fedoraproject.org/wiki/Packaging/Conflicts
Conflicts: pine

Provides: re-alpine = %{version}-%{release}

#BuildRequires: automake libtool
BuildRequires: gettext
BuildRequires: hunspell
## passing --with-npa=/usr/bin/inews
#BuildRequires: inews
BuildRequires: krb5-devel
BuildRequires: ncurses-devel 
BuildRequires: openldap-devel
BuildRequires: openssl-devel
BuildRequires: pam-devel
BuildRequires: passwd
# passing --with-smtp-msa=/usr/sbin/sendmail instead
#BuildRequires: /usr/sbin/sendmail 

Requires: hunspell
Requires: mailcap
Requires: /usr/sbin/sendmail

BuildRequires: gcc
BuildRequires: make
BuildRequires: libxcrypt-devel

%description
Alpine -- an Alternatively Licensed Program for Internet
News & Email -- is a tool for reading, sending, and managing
electronic messages.  Alpine is the successor to Pine and was
developed by Computing & Communications at the University of
Washington.  
  Though originally designed for inexperienced email users,
Alpine supports many advanced features, and an ever-growing number of
configuration and personal-preference options.
Changes and enhancements over pine:
  * Released under the Apache Software License, Version 2.0.
  * Internationalization built around new internal Unicode support.
  * Ground-up reorganization of source code around new "pith/" core 
routine library.
  * Ground-up reorganization of build and install procedure based on 
GNU Build System's autotools.


%prep
%setup -q -n alpine-%{version}
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

install -m644 -p %{SOURCE1} .


%build
touch imap/ip6
# --without-tcl disables the TCL-based CGI "Web Alpine"
%configure \
  --enable-debug=no \
  --without-tcl \
  --with-c-client-target=lfd \
  --with-date-stamp="$(date --utc ${SOURCE_DATE_EPOCH:+--date=@${SOURCE_DATE_EPOCH}})" \
  --with-smtp-msa=/usr/sbin/sendmail \
  --with-npa=/usr/bin/inews \
  --with-passfile=.alpine.passfile \
  --with-simple-spellcheck=hunspell \
  --with-interactive-spellcheck=hunspell \
  --with-system-pinerc=%{_sysconfdir}/pine.conf \
  --with-system-fixed-pinerc=%{_sysconfdir}/pine.conf.fixed


# Build single threaded, make is not creating directories in time.
export RPM_BUILD_NCPUS=1
%make_build EXTRACFLAGS="$RPM_OPT_FLAGS"


%install
%make_install

# create/touch %ghost'd files
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
touch $RPM_BUILD_ROOT%{_sysconfdir}/pine.conf
touch $RPM_BUILD_ROOT%{_sysconfdir}/pine.conf.fixed


%files
%doc README
%doc README.fedora
%license LICENSE
%ghost %config(noreplace) %{_sysconfdir}/pine.conf
%ghost %config(noreplace) %{_sysconfdir}/pine.conf.fixed
%{_bindir}/alpine
%{_bindir}/pico
%{_bindir}/pilot
%{_bindir}/rpload
%{_bindir}/rpdump
%{_mandir}/man1/alpine.1*
%{_mandir}/man1/pico.1*
%{_mandir}/man1/pilot.1*
%{_mandir}/man1/rpload.1*
%{_mandir}/man1/rpdump.1*


%changelog
%autochangelog
