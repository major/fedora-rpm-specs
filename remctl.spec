Name: remctl
Version: 3.18
Release: 4%{?dist}
Summary: Client/server for Kerberos-authenticated command execution

License: MIT
URL: https://www.eyrie.org/~eagle/software/remctl
Source0: https://archives.eyrie.org/software/kerberos/remctl-%{version}.tar.xz

%if "%{php_version}" < "5.6"
%global ini_name     %{name}.ini
%else
%global ini_name     40-%{name}.ini
%endif

Requires(preun):  systemd
Requires(postun): systemd
Requires(post):   systemd

BuildRequires: make
BuildRequires: gcc
BuildRequires: libevent-devel
BuildRequires: krb5-devel
BuildRequires: pcre-devel
BuildRequires: perl-devel
BuildRequires: perl-generators
BuildRequires: perl(ExtUtils::CBuilder)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Test::Pod)
BuildRequires: perl(Test::Spelling)
BuildRequires: php-devel
BuildRequires: ruby(release)
BuildRequires: ruby-devel
BuildRequires: rubygem(minitest)
BuildRequires: systemd
BuildRequires: systemd-devel
BuildRequires: python3-devel
BuildRequires: python3dist(setuptools)
BuildRequires: python3dist(pytest)

%description

remctl (the client) and remctld (the server) implement a client/server
protocol for running single commands on a remote host using Kerberos
v5 authentication and returning the output. They use a very simple
GSS-API-authenticated network protocol, combined with server-side ACL
support and a server configuration file that maps remctl commands to
programs that should be run when that command is called by an
authorised user.

%package devel
Summary: Development files needed to compile C programs against remctl
Requires: %{name} = %{version}-%{release}

%description devel

remctl implements a client/server protocol for running single commands
on a remote host using Kerberos v5 authentication. If you want to develop
programs which use remctl's libraries, you need to install this package.

%package perl
Summary: Perl interface to remctl
Requires: %{name} = %{version}-%{release}

%description perl
remctl implements a client/server protocol for running single commands 
on a remote host using Kerberos v5 authentication. If you want to use
remctl's Perl bindings, you need to install this package.

%package php
Summary: PHP interface to remctl
Requires: %{name} = %{version}-%{release}
Requires:     php(zend-abi) = %{php_zend_api}
Requires:     php(api) = %{php_core_api}

%description php
remctl implements a client/server protocol for running single commands
on a remote host using Kerberos v5 authentication. If you want to use
remctl's PHP bindings, you need to install this package.

%package -n python3-remctl
Summary: Python 3 interface to remctl
Requires: %{name} = %{version}-%{release}

%description -n python3-remctl
remctl implements a client/server protocol for running single commands
on a remote host using Kerberos v5 authentication. If you want to use
remctl's Python bindings, you need to install this package.

%package ruby
Summary: Ruby interface to remctl
Requires: %{name} = %{version}-%{release}
Requires: ruby(release)
Provides: ruby(remctl) = %{version}-%{release}

%description ruby
remctl implements a client/server protocol for running single commands
on a remote host using Kerberos v5 authentication. If you want to use
remctl's Ruby bindings, you need to install this package.

%prep
%autosetup -p1

%build
export REMCTL_PERL_FLAGS="installdirs=vendor"
%configure \
	--with-pcre \
	--enable-perl \
	--enable-php \
	--enable-python \
	--enable-ruby \
	--disable-static
make %{?_smp_mflags}

%check
make check

%install
make install \
	DESTDIR=%{buildroot} \
	INSTALL="install -p" \
	RUBYARCHDIR="%{buildroot}%{ruby_vendorarchdir}" \

chmod 0755 %{buildroot}%{perl_vendorarch}/auto/Net/Remctl/Remctl.so
chmod 0644 %{buildroot}%{perl_vendorarch}/Net/Remctl.pm
chmod 0644 %{buildroot}%{_mandir}/man3/Net::Remctl.3pm*

# Tidy up the perl installation ...
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type f -name perllocal.pod -exec rm -f {} ';'
find %{buildroot} -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'

# And the libraries
find %{buildroot} -type f -name '*.la' -exec rm -f {} ';'

# PHP configuration
mkdir -p %{buildroot}%{php_inidir}
cp -p php/remctl.ini %{buildroot}%{php_inidir}/%{ini_name}

%post
/sbin/ldconfig
%systemd_post remctld.service

%preun
%systemd_preun remctld.service

%postun
/sbin/ldconfig
%systemd_postun remctld.service

%files 
%doc README NEWS TODO
%{_libdir}/*.so.*
%{_bindir}/remctl
%{_sbindir}/remctld
%{_sbindir}/remctl-shell
%{_mandir}/man1/remctl*
%{_mandir}/man8/remctl*
%{_unitdir}/remctld.service
%{_unitdir}/remctld.socket

%files devel
%{_includedir}/remctl.h
%{_mandir}/man3/remctl*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libremctl.pc

%files perl
%{perl_vendorarch}/Net
%{perl_vendorarch}/auto/Net
%{_mandir}/man3/Net::Remctl*

%files php
%doc README
%{php_extdir}/remctl.so
%config(noreplace) %{php_inidir}/%{ini_name}

%files -n python3-remctl
%doc python/README
%{python3_sitearch}/_remctl.*.so
%{python3_sitearch}/pyremctl-*.egg-info/
%{python3_sitearch}/remctl.py*
%{python3_sitearch}/__pycache__/remctl.*

%files ruby
%doc README
%{ruby_vendorarchdir}/remctl.so


%changelog
* Wed Jan 04 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.18-4
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.2

* Wed Oct 05 2022 Remi Collet <remi@remirepo.net> - 3.18-3
- rebuild for https://fedoraproject.org/wiki/Changes/php82

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Ken Dreyer <ktdreyer@ktdreyer.com> - 3.18-1
- Update to 3.18

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.17-8
- Rebuilt for Python 3.11

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 3.17-7
- Perl 5.36 rebuild

* Thu Jan 27 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.17-6
- F-36: rebuild against ruby31

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 10 2021 Ken Dreyer <ktdreyer@ktdreyer.com> - 3.17-4
- Add python3-remctl subpackage
- Patch and enable tests

* Thu Oct 28 2021 Remi Collet <remi@remirepo.net> - 3.17-3
- rebuild for https://fedoraproject.org/wiki/Changes/php81

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jul 14 2021 Ken Dreyer <ktdreyer@ktdreyer.com> - 3.17-1
- Update to 3.17

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 3.15-16
- Perl 5.34 rebuild

* Thu Mar  4 2021 Remi Collet <remi@remirepo.net> - 3.15-15
- Rebuild for https://fedoraproject.org/wiki/Changes/php80
- add patch for PHP 8

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 06 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.15-13
- F-34: rebuild against ruby 3.0

* Tue Sep 29 2020 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.15-12
- Rebuilt for libevent 2.1.12

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 3.15-10
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 18 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.15-8
- F-32: rebuild against ruby27

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.15-6
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 Miro Hrončok <mhroncok@redhat.com> - 3.15-4
- Subpackage python2-remctl has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Jan 21 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.15-3
- F-30: rebuild against ruby26

* Fri Oct 12 2018 Remi Collet <remi@remirepo.net> - 3.15-2
- Rebuild for https://fedoraproject.org/wiki/Changes/php73

* Fri Sep 21 2018 Ken Dreyer <ktdreyer@ktdreyer.com> - 3.15-1
- Update to 3.15
- Use HTTPS URLs
- Remove Group tag
- Enable parallel make with smpflags
- Switch to %%autosetup
- cherry-pick "Fix passing CFLAGS to PHP configure" from upstream
- set REMCTL_PYTHON_VERSIONS=python2 (rhbz#1606109)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.14-2
- Perl 5.28 rebuild

* Fri Apr 06 2018 Ken Dreyer <ktdreyer@ktdreyer.com> - 3.14-1
- Update to 3.14 (CVE-2018-0493)

* Fri Mar 02 2018 Petr Pisar <ppisar@redhat.com> - 3.13-14
- Adapt to removing GCC from a build root (bug #1547165)

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.13-13
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.13-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 3.13-11
- Rebuilt for switch to libxcrypt

* Fri Jan 05 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.13-10
- F-28: rebuild for ruby25

* Tue Oct 03 2017 Remi Collet <remi@fedoraproject.org> - 3.13-9
- rebuild for https://fedoraproject.org/wiki/Changes/php72

* Sun Aug 20 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.13-8
- Add Provides for the old name without %%_isa

* Thu Aug 10 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.13-7
- Python 2 binary package renamed to python2-remctl
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.13-4
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 13 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.13-2
- F-26: rebuild for ruby24

* Sun Jan 08 2017 Ken Dreyer <ktdreyer@ktdreyer.com> - 3.13-1
- Update to 3.13
- Drop EL5 compatibility

* Thu Nov 24 2016 Remi Collet <remi@fedoraproject.org> - 3.11-4
- rebuild for https://fedoraproject.org/wiki/Changes/php71

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.11-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu May 19 2016 Jitka Plesnikova <jplesnik@redhat.com> - 3.11-2
- Perl 5.24 re-rebuild of bootstrapped packages

* Thu May 19 2016 Ken Dreyer <ktdreyer@ktdreyer.com> - 3.11-1
- Update to remctl 3.11

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 3.9-12
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 12 2016 Vít Ondruch <vondruch@redhat.com> - 3.9-10
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.3

* Wed Jul 01 2015 Ken Dreyer <ktdreyer@ktdreyer.com> - 3.9-9
- Remove Fedora 19 workarounds, since that is EOL

* Wed Jul 01 2015 Ken Dreyer <ktdreyer@ktdreyer.com> - 3.9-8
- BR: systemd in order to fix FTBFS (rhbz#1238103)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 3.9-6
- Perl 5.22 rebuild

* Sat Jan 17 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.9-5
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_2.2

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 3.9-4
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 03 2014 Ken Dreyer <ktdreyer@ktdreyer.com> - 3.9-1
- Update to remctl 3.9
- Adjust Makefile for GCC on EL5

* Thu Jun 19 2014 Remi Collet <rcollet@redhat.com> - 3.8-5
- rebuild for https://fedoraproject.org/wiki/Changes/Php56
- add numerical prefix to extension configuration file

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 22 2014 Ken Dreyer <ktdreyer@ktdreyer.com> - 3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.1

* Sat Feb 08 2014 Ken Dreyer <ktdreyer@ktdreyer.com> - 3.8-2
- Add tarball for 3.8

* Sat Feb 08 2014 Ken Dreyer <ktdreyer@ktdreyer.com> - 3.8-1
- Update to 3.8
- Alphabetize BRs
- Optimize python file list (#1062765, thanks Remi Ferrand)
- Enable pcre support (#1062765, thanks Remi Ferrand)

* Fri Jan 24 2014 Ken Dreyer <ktdreyer@ktdreyer.com> - 3.7-2
- Adjust UnversionedDocdirs conditional to support Fedora 19

* Thu Jan 23 2014 Ken Dreyer <ktdreyer@ktdreyer.com> - 3.7-1
- Update to 3.7
- Drop upstreamed EL5 perl patch
- Drop RPM conditionals for Fedoras earlier than 19
- Add systemd support
- Use upstream's php.ini instead of our own
- Ship upstream's READMEs for PHP, Python, and Ruby

* Wed Aug 21 2013 Ken Dreyer <ktdreyer@ktdreyer.com> - 3.6-1
- Upgrade to 3.6
- Drop upstreamed EL5 gcc patch

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 3.5-2
- Perl 5.18 rebuild

* Tue Jul 16 2013 Ken Dreyer <ktdreyer@ktdreyer.com> - 3.5-1
- Upgrade to 3.5
- Switch to using upstream's xz tarballs
- Patch for EL5's gcc and Module::Build
- Add BR for tests
- Correct old changelog dates

* Fri Mar 22 2013 Remi Collet <rcollet@redhat.com> - 3.3-4
- rebuild for http://fedoraproject.org/wiki/Features/Php55

* Wed Mar 13 2013 Ken Dreyer <ktdreyer@ktdreyer.com> - 3.3-3
- Adjust RPM conditionals for new Ruby guidelines on Fedora 19
- Add workaround for Ruby 2.0 "make install" bug (#921650)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Sep 26 2012 Ken Dreyer <ktdreyer@ktdreyer.com> - 3.3-1
- Upgrade to 3.3

* Mon Sep 03 2012 Ken Dreyer <ktdreyer@ktdreyer.com> - 3.2-5
- Fix PHP build for EL5
- Add remctl.ini PHP file

* Mon Sep 03 2012 Ken Dreyer <ktdreyer@ktdreyer.com> - 3.2-4
- Add PHP, Python, and Ruby bindings
- Drop separate Perl "vendor" patch in favor of using REMCTL_PERL_FLAGS

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 28 2012 Petr Pisar <ppisar@redhat.com> - 3.2-2
- Perl 5.16 rebuild

* Wed Jun 20 2012 Ken Dreyer <ktdreyer@ktdreyer.com> - 3.2-1
- Upgrade to 3.2

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 3.1-2
- Perl 5.16 rebuild

* Wed Feb 29 2012 Ken Dreyer <ktdreyer@ktdreyer.com> - 3.1-1
- Upgrade to 3.1

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 23 2011 Ken Dreyer <ktdreyer@ktdreyer.com> - 3.0-1
- Upgrade to 3.0

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.11-13
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jun 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.11-11
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 2.11-10
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jul 03 2008 Simon Wilkinson <simon@sxw.org.uk> 2.11-7
- Update to catch new perl version, and fix perl dependencies (#453579)

* Thu Feb 28 2008 Simon Wilkinson <simon@sxw.org.uk> 2.11-6
- The build process isn't -j safe, so remove smpflags until this can be fixed.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.11-5
- Autorebuild for GCC 4.3

* Sun Jan 27 2008 Simon Wilkinson <simon@sxw.org.uk> 2.11-4
- More changes to address review comments

* Wed Jan 23 2008 Simon Wilkinson <simon@sxw.org.uk> 2.11-3
- Modifications for second round of review comments

* Tue Jan 22 2008 Simon Wilkinson <simon@sxw.org.uk> 2.11-2
- Modifications for first round of review comments
- Put perl modules in vendor_lib

* Mon Jan 14 2008 Simon Wilkinson <simon@sxw.org.uk> 2.11-1
- Upgrade to remctl 2.11

* Mon Oct  1 2007 Simon Wilkinson <simon@sxw.org.uk> 2.10-1
- Upgrade to remctl 2.10

* Sun Sep  2 2007 Simon Wilkinson <simon@sxw.org.uk> 2.9-1
- Initial specfile

