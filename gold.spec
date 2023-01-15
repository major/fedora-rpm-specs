%define goldcgidir	%{_datadir}/%{name}-%{version}
%define golddatadir	%{_localstatedir}/lib/%{name}
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name:		gold
Version:	2.1.12.2
Release:	40%{?dist}
Summary:	Tracks and manages resource usage on High Performance Computers
License:	BSD
URL:		http://www.clusterresources.com/products/%{name}
Source0:	http://www.clusterresources.com/downloads/%{name}/%{name}-%{version}.tar.gz
# These patches are to make it build happily under rpm and mock - they have
# been submitted upstream (see the thread at
# http://www.supercluster.org/pipermail/gold-users/2010-July/000343.html for
# more info).
Patch0:		gold-makefile.patch
Patch1:		gold-configure-ac.patch

BuildArch:	noarch 
Requires(pre):	shadow-utils
Requires:	sqlite

# For some reason, these requires are missed:
Requires:	perl(Data::Properties)
Requires:	perl(Crypt::DES_EDE3)

BuildRequires:  gcc
BuildRequires:	autoconf
BuildRequires:	coreutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter

%description
The Gold Allocation Manager is an open source accounting system developed by
Pacific Northwest National Laboratory (PNNL) as part of the Department of
Energy (DOE) Scalable Systems Software Project (SSS). It tracks resource usage
on High Performance Computers and acts much like a bank, establishing accounts
in order to pre-allocate user and project resource usage over specific nodes and
time-frame. Gold provides balance and usage feedback to users, managers, and
system administrators.  SQLite is used by default, but Gold can be configured
to use either MySQL or PostgreSQL instead.

%package web
Summary:			Gold Allocation Manager Web Frontend
Requires:			%{name} = %{version}-%{release}
Requires:			webserver
BuildRequires:		perl-interpreter

%description web
CGI Perl web front-end for the Gold Allocation Manager.

%package doc
Summary:			Gold Allocation Manager Documentation

%description doc
Documentation for the Gold Allocation Manager.

%prep 
%setup -q
%patch0
%patch1
# Regenerate configure script
autoconf -f -o configure

%build
%configure \
	--with-user=gold --with-db=SQLite \
	--with-doc-dir=%{_pkgdocdir} \
	--with-perl-libs=vendor --with-gold-libs=vendor --with-cgi-bin=%{goldcgidir} \
	--datadir=%{golddatadir}
make %{?_smp_mflags}
make %{?_smp_mflags} gui

# Prevent spurious requirement on Postgres DBD class
cat << \EOF > %{name}-req
#!/bin/sh
%{__perl_requires} $* |\
sed -e '/perl(DBD::Pg)/d'
EOF

%global __perl_requires %{_builddir}/%{name}-%{version}/%{name}-req
chmod +x %{__perl_requires}

%install
## Install documentation
mkdir -p %{buildroot}%{_pkgdocdir}

## Install binaries
mkdir -p %{buildroot}%{golddatadir}
mkdir -p %{buildroot}%{perl_vendorlib}
make install DESTDIR=%{buildroot}

## Install web gui
make install-gui DESTDIR=%{buildroot}

# TODO
#make auth_key DESTDIR=%{buildroot}

# Clean up things that shouldn't have been installed
rm %{buildroot}%{perl_vendorlib}/Gold/*.pm.in

# Fix non UTF-8 files(preserving timestamps)
for i in README LICENSE;
do
	iconv -f iso8859-1 -t utf8 $i >$i.utf8
	touch -r $i $i.utf8
	mv $i.utf8 $i
done

# Install rest of the documentation
install -pm 644 README INSTALL LICENSE DATABASE CHANGES \
	%{buildroot}%{_pkgdocdir}
cp -pR doc/ %{buildroot}%{_pkgdocdir}

# TODO Separate out the gold server and client packages

# TODO Work out why init script isn't installing - in src/etc/gold.d.in
# TODO chkconfig --add gold
# TODO Patch Perl in /usr/sbin/goldd to use the passed in pid file and not the
# hard coded one!!
# TODO Patch Perl in /usr/sbin/goldd to use the correct path for the /etc/
# files!
# TODO Patch Perl in Gold.pm and others too as paths to the config files are
# incorrect.
# TODO Correct init script to use the correct path for the pid file -
# /var/run/gold/gold.pid or /var/run/gold.pid

# TODO Correct goldsh so that the gold_history file isn't in a hard-coded
# location in /usr/log/.gold_history or similar

# TODO Sort out the authkey: ${GOLD_HOME}/etc/auth_key (line 220 of
# /usr/sbin/goldd)

# TODO On the client end, make sure the default logging is to use syslog, and
# that this is honoured in all the places it is currently hard-coded!

# TODO The gold*.conf config files need to have their permissions changed so
# that they belong to the gold user and group and are chmod 600 or similar as
# they will contain database usernames and passwords.

# TODO Change the server name set in the config files
# TODO Change the log location set in the config files
# TODO Change the logging level set in the config files

# The server configuration file is goldd.conf
# The client is 
# The web interface configuration file is 


%check
# This target, although it exists, does nothing at present
make test

%pre
## Add the "gold" group
getent group gold >/dev/null || groupadd -r gold
## Add the "gold" user
getent passwd gold >/dev/null || \
/usr/sbin/useradd -c "Gold Allocation Manager" -g gold \
	-s /sbin/nologin -r -d %{_localstatedir}/lib/%{name} gold 
exit 0

%preun
if [ "$1" = 0 ]
then
	/sbin/service gold stop >/dev/null 2>&1 || :
	/sbin/chkconfig --del gold
fi

%files
%dir %{_pkgdocdir}
%{_pkgdocdir}/LICENSE
%dir %{golddatadir}
%dir %{perl_vendorlib}/Gold
%config(noreplace) %{_sysconfdir}/*
%{_bindir}/*
%{_sbindir}/*
%{perl_vendorlib}/Gold.pm
%{perl_vendorlib}/Gold/*.pm

%files doc
%dir %{_pkgdocdir}
%{_pkgdocdir}/*

%files web
%dir %{goldcgidir}
%{goldcgidir}/*

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.12.2-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.1.12.2-39
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.12.2-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.12.2-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.1.12.2-36
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.12.2-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.12.2-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.1.12.2-33
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.12.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.12.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.1.12.2-30
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.12.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.12.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.1.12.2-27
- Perl 5.28 rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.12.2-26
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.12.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.12.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.1.12.2-23
- Perl 5.26 rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.12.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.1.12.2-21
- Fix build-require of perl

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.1.12.2-20
- Perl 5.24 rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.12.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.12.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.1.12.2-17
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.1.12.2-16
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.12.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Nov 13 2013 Ville Skyttä <ville.skytta@iki.fi> - 2.1.12.2-14
- Install docs to %%{_pkgdocdir} where available (#993797).
- Remove redundant copy of LICENSE from -web.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.12.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.1.12.2-12
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.12.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.12.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 2.1.12.2-9
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.12.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Oct 11 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 2.1.12.2-7
- Rebuild for new perl, cleanup spec file

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.1.12.2-6
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.12.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Aug 12 2010 Jessica Jones <fedora@zaniyah.org> 2.1.12.2-4
- Changed summary to something more comprehensible
- Updated description to include full package name

* Tue Aug  3 2010 Jessica Jones <fedora@zaniyah.org> 2.1.12.2-3
- Attempt to fix Perl dependencies

* Wed Jul 28 2010 Jessica Jones <fedora@zaniyah.org> 2.1.12.2-2
- Convert README and LICENSE to UTF-8
- Change file list to include %%conf directive for config files
- Remove duplicate files from file list
- Remove unnecessary documentation from web and main packages
- Add test step
- Remove unnecessary Perl tests

* Thu Jul 01 2010 Jessica Jones <fedora@zaniyah.org> 2.1.12.2-1
- Initial build for EPEL 5
