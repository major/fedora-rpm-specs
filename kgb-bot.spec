Name:		kgb-bot
Summary:	IRC Collaboration Bot
Version:	1.51
Release:	20%{dist}
License:	GPLv2+
URL:	    https://salsa.debian.org/kgb-team/kgb
Buildarch:	noarch
Source:		%{name}-%{version}.tar.gz
Source1:	%{name}.service
Source2:	%{name}.init
Source3:	%{name}.logrotate
# Adjust tests to changes in git-2.28.0, bug #1859842, upstream bug #965350,
# fixed in upstream release 1.57.
Patch0:		%{name}-1.51-Update-tests-to-changed-output-in-merge-messages.patch
# Adjusts tests to changes in git-2.29.0, bug #1898263, upstream bug #973118,
# fixed in upstream release 1.58
Patch1:		%{name}-1.51-detect-merge-message-text.patch
AutoReq:	0
BuildRequires:  coreutils
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Config)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Pod::Man)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl(Monkey::Patch)
# Run-time:
BuildRequires:  perl(autodie)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
# Data::Dumper not needed if Devel::PartialDump is available
# Devel::PartialDump not needed at tests
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(DirHandle)
BuildRequires:  perl(Encode)
BuildRequires:  perl(encoding)
BuildRequires:  perl(Error)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(feature)
BuildRequires:  perl(File::Basename)
# File::Touch not used at tests
# File::Which not used at tests
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Git)
BuildRequires:  perl(IPC::Run)
# JSON::RPC::Client not needed if JSON::RPC::Legacy::Client is available
BuildRequires:  perl(JSON::RPC::Legacy::Client)
BuildRequires:  perl(JSON::XS)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(open)
BuildRequires:  perl(overload)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(POE)
BuildRequires:  perl(POE::Component::IRC)
BuildRequires:  perl(POE::Component::IRC::Plugin::AutoJoin)
BuildRequires:  perl(POE::Component::IRC::Plugin::BotAddressed)
BuildRequires:  perl(POE::Component::IRC::Plugin::Connector)
BuildRequires:  perl(POE::Component::IRC::Plugin::CTCP)
BuildRequires:  perl(POE::Component::IRC::Plugin::NickReclaim)
BuildRequires:  perl(POE::Component::IRC::Plugin::NickServID)
BuildRequires:  perl(POE::Component::IRC::State)
BuildRequires:  perl(POE::Component::Server::SOAP)
BuildRequires:  perl(Proc::PID::File)
BuildRequires:  perl(Safe)
BuildRequires:  perl(Schedule::RateLimiter)
BuildRequires:  perl(SOAP::Lite)
BuildRequires:  perl(Storable)
BuildRequires:  perl(SVN::Core)
BuildRequires:  perl(SVN::Fs)
BuildRequires:  perl(SVN::Repos)
BuildRequires:  perl(Time::Piece)
BuildRequires:  perl(User::pwent)
BuildRequires:  perl(version)
BuildRequires:  perl(WWW::Shorten::generic)
BuildRequires:  perl(YAML)
BuildRequires:  perl(Net::IP)
%if 0%{?fedora}
BuildRequires:  perl(Test::CPAN::Changes)
%endif
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(File::Remove)
BuildRequires:  perl(DBD::Pg)
BuildRequires:  perl(File::Touch)
BuildRequires:  perl(Dpkg::Version)
# Optional run-time:
BuildRequires:  perl(WWW::Shorten)
# Tests:
# IPC::System::Simple is needed for autodie ':all'
BuildRequires:  perl(IPC::System::Simple)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Test::Compile::Internal)
# Test::Differences not used
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Perl::Critic)
BuildRequires:  %{_bindir}/svnadmin
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.22
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
BuildRequires:  %{_sbindir}/useradd
BuildRequires:  %{_sbindir}/groupadd
Requires:	%{name}-client = %{version}-%{release}
Requires:	perl(Proc::PID::File)
Requires:	perl(Time::Piece)
Requires:	perl(YAML)
Requires:	perl(Digest::SHA)
Requires:	perl(Schedule::RateLimiter)
Requires:	perl(File::Touch)
Requires:	perl(JSON)
Requires:	perl(JSON::XS)
Requires:   perl(JSON::RPC::Legacy::Client)
Requires:	perl(SOAP::Lite)
Requires:	perl(POE::Component::Server::SOAP)
Requires:	perl(POE::Component::Syndicator)
Requires:	perl(POE::Component::IRC)
Requires:	perl(POE)
Requires:	perl(Error)
Requires:   perl(Monkey::Patch)
Requires:   perl(Net::IP)
Requires:   perl(IPC::Run)
%if 0%{?fedora} >= 15 || 0%{?rhel} >= 7
BuildRequires:	systemd-units
BuildRequires: make
Requires(post):	systemd-units
Requires(preun):	systemd-units
Requires(postun):	systemd-units
%else
Requires(post):	chkconfig
Requires(preun):	chkconfig
Requires(preun):	initscripts
%endif

%description
KGB is an IRC bot, helping people work together by notifying an IRC channel
when a commit occurs. It supports multiple repositories/IRC channels and is
fully configurable.

%package client
Summary:	The kgb-bot's client
AutoReq:	0
Requires:	perl(Class::Accessor)
Requires:	perl(SOAP::Lite)
Requires:	subversion-perl
Requires:	perl(YAML)
Requires:	perl(WWW::Shorten)
Requires:	perl(JSON::XS)

%description client
This package contains the client-side program, kgb-client, which is supposed
to be used as an hook in your version control system and sends the
notifications to the KGB daemon. Currently supported version control
systems are: Subversion, Git (via kgb-client-git package), CVS.

%package client-git
Summary:	The kgb-bot's client
AutoReq:	0
Requires:	git-core
Requires:	%{name}-client = %{version}-%{release}
Requires:	perl(IPC::Run)
Requires:	perl(JSON::XS)

%description client-git
This package adds support of Git version control system to kgb-client.

%prep
%setup -q -n App-KGB-%{version}
%patch0 -p1
%patch1 -p1

%pre
getent group Fedora-kgb >/dev/null || groupadd -r Fedora-kgb
getent passwd Fedora-kgb >/dev/null || useradd -r -g Fedora-kgb -M -s /sbin/nologin Fedora-kgb
exit 0

%preun
%if 0%{?fedora} >= 15 || 0%{?rhel} >= 7
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable %{name}.service > /dev/null 2>&1 || :
    /bin/systemctl stop %{name}.service > /dev/null 2>&1 || :
fi
%else
if [ $1 -eq 0 ] ; then
   /sbin/service %{name} stop > /dev/null 2>&1 ||:
   /sbin/chkconfig --del %{name}
fi
%endif

%post
%if 0%{?fedora} >= 15 || 0%{?rhel} >= 7
if [ $1 -eq 1 ] ; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi
%else
/sbin/chkconfig --add %{name}
%endif

%postun
%if 0%{?fedora} >= 15 || 0%{?rhel} >= 7
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /bin/systemctl try-restart %{name}.service >/dev/null 2>&1 || :
fi
%else
if [ $1 -ge 1 ] ; then
   /sbin/service %{name} condrestart >/dev/null 2>&1 ||:
fi
%endif

%build
perl Build.PL --destdir .
./Build --installdirs vendor
make %{?_smp_mflags}

%install
./Build install --installdirs vendor --destdir $RPM_BUILD_ROOT

# Create a /var/run/kgb-bot directory.
mkdir -p $RPM_BUILD_ROOT/%{_localstatedir}/run/%{name}

# Create an /etc/kgb-bot/kgb.conf.d directory, it's included on the default
# kgb.conf configuration file.
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}/kgb.conf.d

# Create a /var/log/kgb-bot.log file, it'll be %%ghosted later.
mkdir -p $RPM_BUILD_ROOT/%{_localstatedir}/log
touch $RPM_BUILD_ROOT/%{_localstatedir}/log/%{name}.log

# Install a logrotate configuration file for /var/log/kgb-bot.log
mkdir -p $RPM_BUILD_ROOT/{_sysconfdir}/logrotate.d
%{__install} -Dp -m0644 %{SOURCE3} $RPM_BUILD_ROOT/%{_sysconfdir}/logrotate.d/%{name}

%if 0%{?fedora} >= 15 || 0%{?rhel} >= 7
%{__install} -Dp -m0644 %{SOURCE1} $RPM_BUILD_ROOT/%{_unitdir}/%{name}.service
%else
mkdir -p $RPM_BUILD_ROOT/%{_initrddir}/
%{__install} -Dp -m0644 %{SOURCE2} $RPM_BUILD_ROOT/%{_sysconfdir}/init.d/%{name}
%endif

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
# Export an UTF8 locale since the tests demand them.
LANG=C.UTF-8 LC_ALL=C.utf8
./Build test

%files
%doc Changes LICENSE
%config(noreplace) %{_sysconfdir}/%{name}/kgb.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%attr(640, Fedora-kgb, Fedora-kgb) %{_sysconfdir}/%{name}/kgb.conf
%attr(755, Fedora-kgb, Fedora-kgb) %dir %{_localstatedir}/run/%{name}
%attr(755, Fedora-kgb, Fedora-kgb) %dir %{_sysconfdir}/%{name}/kgb.conf.d
%ghost %{_localstatedir}/log/kgb-bot.log
%{_sbindir}/kgb-split-config
%{_sbindir}/%{name}
%{_sbindir}/kgb-add-project
%{_mandir}/man1/%{name}.*
%{_mandir}/man1/kgb-split-config.*
%{_mandir}/man1/kgb-add-project.*
%{_mandir}/man5/kgb.conf.*
%{_mandir}/man7/kgb-protocol.7*
%if 0%{?fedora} >= 15 || 0%{?rhel} >= 7
%{_unitdir}/%{name}.service
%else
%{_sysconfdir}/init.d/%{name}
%endif

%files client
%doc Changes eg/kgb-client.conf.sample eg/post-commit LICENSE
%{_bindir}/kgb-client
%{_bindir}/kgb-ci-report
%{_mandir}/man1/kgb-client.*
%{_mandir}/man1/kgb-ci-report.*
%{_mandir}/man3/App::KGB*
%{_mandir}/man3/WWW::Shorten*
%{_mandir}/man3/JSON::RPC::Client::Any*
%{_mandir}/man5/kgb-client.conf.*
%{perl_vendorlib}/*

%files client-git
%doc Changes LICENSE
%{_mandir}/man3/App::KGB::Client::Git.3pm*
%{perl_vendorlib}/App/KGB/Client/Git.pm

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.51-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.51-19
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.51-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.51-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.51-16
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.51-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 16 2020 Petr Pisar <ppisar@redhat.com> - 1.51-14
- Adjusts tests to changes in git-2.29.0 (bug #1898263)

* Thu Oct 01 2020 Petr Pisar <ppisar@redhat.com> - 1.51-13
- Adjust tests to changes in git-2.28.0 (bug #1859842)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.51-12
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.51-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.51-10
- Perl 5.32 rebuild

* Thu Jun 18 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.51-9
- Add missing test BR svnadmin

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.51-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.51-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.51-6
- Perl 5.30 rebuild

* Mon May 27 2019 Andrea Veri <averi@fedoraproject.org> - 1.51-5
- Add the `-p` flag to mkdir to avoid it failing whenever the directory
  exists already

* Mon May 06 2019 Andrea Veri <averi@fedoraproject.org> - 1.51-4
- Make sure /var/run/kgb-bot gets created and assigned correct permissions

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.51-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 19 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.51-2
- Use C.UTF-8 locale
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Wed Aug 01 2018 Andrea Veri <averi@fedoraproject.org> - 1.51-1
- New upstream release.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.31-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.31-16
- Perl 5.28 rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.31-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.31-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 08 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.31-13
- Perl 5.26 rebuild

* Thu May 25 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.31-12
- Remove deprecated pragma encoding

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.31-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Sep 06 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.31-10
- Update the patch to compare versions properly

* Tue Aug 30 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.31-9
- Fix t/52-client-git.t to work with newer git versions

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.31-8
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.31-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.31-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.31-5
- Perl 5.22 rebuild

* Fri Nov 28 2014 Petr Pisar <ppisar@redhat.com> - 1.31-4
- Specify all build-time dependencies (bug #1168856)

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.31-3
- Perl 5.20 rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Oct 02 2013 Andrea Veri <averi@fedoraproject.org> - 1.31-1
- New upstream release.
- Drop the kgb-bot-1.26-Adjust-to-Safe-2.35 patch, it has been
  included upstream.
- Drop the JSON-RPC-to-JSON-Legacy-Client patch, a fix has been
  applied upstream.

* Fri Sep 27 2013 Andrea Veri <averi@fedoraproject.org> - 1.26-20130927svn880
- Minor adjustements: fixed typo on the spec file and added two missing
  runtime dependencies.

* Tue Aug 06 2013 Petr Pisar <ppisar@redhat.com> - 1.26-20130525svn880
- Perl 5.18 rebuild
- Adjust to Safe-2.35

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.26-20130524svn880
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 23 2013 Andrea Veri <averi@fedoraproject.org> - 1.26-20130523svn880
- Add the missing /var/run/kgb-bot and /etc/kgb-bot/kgb.conf.d directories,
  the initial configuration file has them enabled by default.
- Touch and chown the /var/log/kgb-bot.log file to Fedora-kgb:Fedora-kgb.
- Add a logrotate config file for kgb-bot.

* Sat May 11 2013 Andrea Veri <averi@fedoraproject.org> - 1.26-20130516svn880
- Fix the path for /etc/init.d.
- Add the missing runtime dependencies.
- Fix the initscript.

* Sat May 11 2013 Andrea Veri <averi@fedoraproject.org> - 1.26-20130512svn880
- First package release.
