%define		prerelease 493svn
Name:		conmux
Version:	0.0
Release:	54.%{prerelease}%{?dist}
Summary:	ConMux - The Console Multiplexor

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:	GPL-2.0-only
URL:		http://test.kernel.org/autotest/
Source0:	http://people.redhat.com/bpeck/%{name}/%{name}-%{prerelease}.tar.gz
# svn checkout -r493 svn://test.kernel.org/autotest/trunk/conmux conmux
Source1:	%{name}.conf
Source2:	%{name}.logrotate
Source3:	%{name}.init
Patch1:		%{name}.build.patch
BuildRequires:	coreutils
BuildRequires:	make
BuildRequires:	perl-interpreter
BuildRequires:	perl-generators
Requires:	perl-interpreter
Requires:	%{name}-client = %{version}-%{release}
BuildArch:	noarch
Requires:	logrotate
Provides:	perl(Payload)
Provides:	perl(Client)
Requires(post):	/sbin/chkconfig
Requires(preun):	/sbin/chkconfig
Requires(preun):	/sbin/service

%description
Conmux is a console management program designed to support a large
number of console devices and simultaneous users.  It currently supports
IBM's blade and hmc servers.

Its features include:

  - driver interface abstracts how to connect to the console
  - helpers for dealing with autobooting
  - can support additional commands for dealing with power management
  - allows multiple clients to be connected to the same console

%package client
Summary:	Conmux client which will connect to a Conmux server
Obsoletes:	conmux-common < %{version}-%{release}
Provides:	conmux-common = %{version}-%{release}

%description client
Conmux client connects to a conmux server. 

%prep
%setup -q -n conmux
%patch -P1 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d
# put in our own config and logrotate
install -pm 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/%{name}.conf
install -pm 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/%{name}
install -pm 0755 %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/init.d/%{name}
# make log directories
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/log/%{name}
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/log/%{name}.old
# these shouldn't be executable
chmod -x examples/*


%post
/sbin/chkconfig --add conmux

%preun
if [ "$1" = 0 ]; then
  /sbin/service conmux stop >/dev/null 2>&1 || :
  /sbin/chkconfig --del conmux
fi

%postun
if [ "$1" -ge 1 ]; then
  /sbin/service conmux condrestart >/dev/null 2>&1 || :
fi

%files
%doc COPYING README
%doc examples
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%{_sysconfdir}/init.d/%{name}
%dir %{_sysconfdir}/%{name}
%{_localstatedir}/log/%{name}
%{_localstatedir}/log/%{name}.old
%{_localstatedir}/run/%{name}
%{_bindir}/conmux-attach
%{_sbindir}/*
%{_datadir}/conmux/

%files client
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%{_bindir}/conmux
%{perl_vendorlib}/Conmux.pm
%doc COPYING README

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-54.493svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.0-53.493svn
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-52.493svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-51.493svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-50.493svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-49.493svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-48.493svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-47.493svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.0-46.493svn
- Perl 5.36 rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-45.493svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-44.493svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.0-43.493svn
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-42.493svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-41.493svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.0-40.493svn
- Perl 5.32 re-rebuild of bootstrapped packages

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.0-39.493svn
- Perl 5.32 rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-38.493svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-37.493svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.0-36.493svn
- Perl 5.30 rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-35.493svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-34.493svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.0-33.493svn
- Perl 5.28 rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-32.493svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-31.493svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 13 2017 Petr Pisar <ppisar@redhat.com> - 0.0-30.493svn
- perl dependency renamed to perl-interpreter
  <https://fedoraproject.org/wiki/Changes/perl_Package_to_Install_Core_Modules>

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.0-29.493svn
- Perl 5.26 rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-28.493svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Aug 09 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.0-27.493svn
- Add BRs perl, make, coreutils

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.0-26.493svn
- Perl 5.24 rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-25.493svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0-24.493svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.0-23.493svn
- Perl 5.22 rebuild

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.0-22.493svn
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0-21.493svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0-20.493svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.0-19.493svn
- Perl 5.18 rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0-18.493svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0-17.493svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 10 2012 Petr Pisar <ppisar@redhat.com> - 0.0-16.493svn
- Perl 5.16 rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0-15.493svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.0-14.493svn
- Perl mass rebuild

* Fri Jun 10 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.0-13.493svn
- Perl 5.14 mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0-12.493svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 08 2010 Bill Peck <bpeck@redhat.com> - 0.0-11.493svn
- Include COPYING file in -client package.

* Tue Jun 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.0-10.493svn
- Mass rebuild with perl-5.12.0

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0-9.493svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0-8.493svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed May 07 2008 Michal Schmidt <mschmidt@redhat.com> 0.0-7.493svn
- "GPL" is ambiguous, the license is GPLv2 specifically
- conmux-client ships a perl module, so it must require MODULE_COMPAT
  as described in the packaging guidelines. Fixes bug 443273.

* Mon Apr 09 2007 Bill Peck <bpeck@redhat.com> 0.0-6.493svn
- minor spec file changes for directory ownership
* Thu Mar 15 2007 Bill Peck <bpeck@redhat.com> 0.0-5.493svn
- fixed Obsoletes/Provides
- minor update to init.d/conmux
* Wed Mar 14 2007 Bill Peck <bpeck@redhat.com> 0.0-4.493svn
- added jarod's init script.  Thanks!
* Mon Mar 12 2007 Bill Peck <bpeck@redhat.com> 0.0-3.493svn
- release really is 0.0 since there is no upstream release yet.
- merge client and common into one package.
* Mon Mar 05 2007 Bill Peck <bpeck@redhat.com> 0.1-2.493svn
- Removed .svn files from tarball.
- install logrotate and config files with -p
* Mon Mar 05 2007 Bill Peck <bpeck@redhat.com> 0-1.493svn
- changed from perl_sitelib to perl_vendorlib.
* Fri Mar 02 2007 Bill Peck <bpeck@redhat.com> 0-0.493svn
- Update to latest svn. drop upstream patch.
* Mon Feb 26 2007 Bill Peck <bpeck@redhat.com> 0-2.484svn
- Remove erroneous chmod on config file.
- rename conmux to conmuxd and rename console to conmux
* Fri Feb 23 2007 Bill Peck <bpeck@redhat.com> 0-1.484svn
- Initial build for Fedora Extras
