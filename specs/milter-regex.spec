# Use sysusers from Fedora 43 onwards
%if (0%{?rhel} && 0%{?rhel} <= 10) || (0%{?fedora} && 0%{?fedora} <= 42)
%global use_sysusers 0
%else
%global use_sysusers 1
%endif

Name:		milter-regex
Version:	2.7
Release:	17%{?dist}
Summary:	Milter plug-in for regular expression filtering
License:	BSD-2-Clause
URL:		http://www.benzedrine.ch/milter-regex.html
Source0:	http://www.benzedrine.ch/milter-regex-%{version}.tar.gz
# Note: signature made with ancient PGP key, needs gpg1 to verify
Source10:	http://www.benzedrine.ch/milter-regex-%{version}.tar.gz.asc
Source1:	milter-regex.service
Source2:	milter-regex-options
Source3:	milter-regex.conf
BuildRequires:	byacc
BuildRequires:	coreutils
BuildRequires:	gcc
BuildRequires:	groff
BuildRequires:	make
BuildRequires:	sed
BuildRequires:	sendmail-milter-devel >= 8.13
BuildRequires:	systemd
%if !%{use_sysusers}
Requires(pre):	shadow-utils
%endif
%{?systemd_requires}

%description
Milter-regex is a milter based filter that makes it possible to filter
emails using regular expressions.

%prep
%setup -q

# Customize config file location and dæmon user
sed -i -e	's|/etc/milter-regex\.conf|%{_sysconfdir}/mail/milter-regex.conf|;
		 s|_milter-regex|mregex|' milter-regex.[8c]

# Copy out the license text from the source code
head -n +31 milter-regex.c > LICENSE

# Create a sysusers.d config file
cat >milter-regex.sysusers.conf <<EOF
u mregex - 'Regex Milter' %{_localstatedir}/spool/milter-regex -
EOF

%build
make %{?_smp_mflags} -f Makefile.linux \
	CFLAGS="%{optflags} -Wextra -Wwrite-strings -DYYMAXDEPTH=8192 -std=gnu17" \
	LDFLAGS="-Wl,-z,now -Wl,-z,relro %{?__global_ldflags} -Wl,--as-needed -L/usr/lib/libmilter -lmilter -lpthread"

%install
mkdir -p \
	%{buildroot}%{_unitdir} \
	%{buildroot}%{_localstatedir}/spool/milter-regex \
	%{buildroot}%{_mandir}/man8 \
	%{buildroot}%{_sbindir} \
	%{buildroot}%{_sysconfdir}/{mail,sysconfig}
install -p -m 755 milter-regex %{buildroot}%{_sbindir}/
install -p -m 644 milter-regex.8 %{buildroot}%{_mandir}/man8/
install -p -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/milter-regex.service
install -p -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/milter-regex
install -p -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/mail/milter-regex.conf

%if %{use_sysusers}
install -m0644 -D milter-regex.sysusers.conf %{buildroot}%{_sysusersdir}/milter-regex.conf
%endif

# Create a ghost sock file so we can remove it on package deletion
: > %{buildroot}%{_localstatedir}/spool/milter-regex/sock

%if !%{use_sysusers}
%pre
getent group mregex >/dev/null || groupadd -r mregex
getent passwd mregex >/dev/null || \
	useradd -r -g mregex -d %{_localstatedir}/spool/milter-regex \
		-s /sbin/nologin -c "Regex Milter" mregex
exit 0
%endif

%post
%systemd_post milter-regex.service

%preun
%systemd_preun milter-regex.service

%postun
%systemd_postun_with_restart milter-regex.service

%files
%license LICENSE
%{_sbindir}/milter-regex
%{_unitdir}/milter-regex.service
%config(noreplace) %{_sysconfdir}/sysconfig/milter-regex
%config(noreplace) %{_sysconfdir}/mail/milter-regex.conf
%dir %attr(755,root,mregex) %{_localstatedir}/spool/milter-regex/
%ghost %{_localstatedir}/spool/milter-regex/sock
%{_mandir}/man8/milter-regex.8*
%if %{use_sysusers}
%{_sysusersdir}/milter-regex.conf
%endif

%changelog
* Wed Feb 12 2025 Paul Howarth <paul@city-fan.org> - 2.7-17
- Drop EL-7 support
- Add sysusers.d config file to allow rpm to create users/groups automatically
  (from F-43 onwards)

* Fri Jan 17 2025 Paul Howarth <paul@city-fan.org> - 2.7-16
- Build with -std=gnu17 due to issues with milter API (#2336394)

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Mar  6 2023 Paul Howarth <paul@city-fan.org> - 2.7-10
- Use distribution linker flags

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.7-5
- Rebuilt for updated systemd-rpm-macros (https://pagure.io/fesco/issue/2583)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 13 2019 Paul Howarth <paul@city-fan.org> - 2.7-1
- Update to 2.7
  - Add -t option to test the configuration file and exit with a status

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 29 2019 Paul Howarth <paul@city-fan.org> - 2.6-1
- Update to 2.6
  - Treat socket file name without prefix like local file
  - Make pid file writeable only by root

* Tue Apr 23 2019 Paul Howarth <paul@city-fan.org> - 2.5-1
- Update to 2.5
  - Add -r option to write pid file, based on FreeBSD port patches

* Wed Apr  3 2019 Paul Howarth <paul@city-fan.org> - 2.4-1
- Update to 2.4
  - Bug fix: for actions followed by multiple expressions (not just one
    arbitrarily complex expression), when multiple expressions become defined
    during the same sequence point, but with different values (e.g. one true,
    another false), depending on the expression order, the action might not be
    taken, when it should be
  - Add -f option to set syslog facility

* Sun Mar 24 2019 Paul Howarth <paul@city-fan.org> - 2.2-3
- Fix ownership of /var/spool/milter-regex so that dac_override isn't needed
  (#1678040)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 24 2018 Paul Howarth <paul@city-fan.org> - 2.2-1
- Update to 2.2
  - Add -U, -G, and -P options to set pipe user, group, and permissions

* Fri Aug 24 2018 Paul Howarth <paul@city-fan.org> - 2.1-1
- Update to 2.1
  - Default maximum log level to 6 (LOG_INFO), i.e. exclude LOG_DEBUG
- Upstream switched from benezedrine.cx to bezendrine.ch

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Paul Howarth <paul@city-fan.org> - 2.0-11
- Drop dependencies on systemd-units and use %%{?systemd_requires} instead
- Use forward-looking conditionals
- List build requirements one per line
- Don't use full paths for commands in scriptlets, to improve readability
- Drop legacy Group: tag

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Aug  5 2016 Paul Howarth <paul@city-fan.org> - 2.0-7
- sendmail-devel renamed to sendmail-milter-devel from Fedora 26
- Specify all build requirements

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar  2 2015 Paul Howarth <paul@city-fan.org> - 2.0-4
- Use %%license

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Nov 25 2013 Paul Howarth <paul@city-fan.org> - 2.0-1
- Update to 2.0
  - Add -l option to specify maximum log level
- Drop upstreamed cleanup and starttls patches

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Sep  7 2012 Paul Howarth <paul@city-fan.org> - 1.9-5
- Drop SysV-to-systemd migration support from F-18 onwards
- Use systemd scriptlet macros for preset support (#850207)

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 17 2012 Paul Howarth <paul@city-fan.org> - 1.9-3
- Add support for STARTTLS macro checking (#840665)
- Defer dæmon startup until network is available

* Fri Jan  6 2012 Paul Howarth <paul@city-fan.org> - 1.9-2
- Rebuilt for gcc 4.7

* Tue Nov 22 2011 Paul Howarth <paul@city-fan.org> - 1.9-1
- Update to 1.9
  - Add -j option to chroot
  - Improve building on various platforms
  - Fix some typos in documentation and example config
- Drop upstreamed strlcat patch
- Drop gcc patch, no longer needed
- Build with additional warnings enabled, and add patch to fix warnings where
  possible (libmilter API is missing some 'const' attributes, so it's not
  possible to get rid of all of them)

* Mon Jul 25 2011 Paul Howarth <paul@city-fan.org> - 1.8-4
- Requires(post): systemd-sysv for sysv-to-systemd migration

* Sat Jul 16 2011 Paul Howarth <paul@city-fan.org> - 1.8-3
- Switch from SysV initscript to systemd unit file
- Clean up for modern rpmbuild
- Drop Sendmail references as the milter should work with Postfix too
- Nobody else likes macros for commands

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Aug 13 2010 Paul Howarth <paul@city-fan.org> - 1.8-1
- Update to 1.8 (log symbolic host name together with numeric IP address)
- Add missing function strlcat from openbsd libc
- Fix %%postun to restart the milter properly on package upgrades
- Use %%{_initddir} rather than the deprecated %%{_initrddir} where possible

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 13 2009 Paul Howarth <paul@city-fan.org> - 1.7-4
- Rebuild for shared libmilter in Fedora 11 development

* Mon Feb 18 2008 Paul Howarth <paul@city-fan.org> - 1.7-3
- Support config files with more than 507 rules (#304071)

* Wed Aug 22 2007 Paul Howarth <paul@city-fan.org> - 1.7-2
- Rebuild for BuildID inclusion
  (http://fedoraproject.org/wiki/Releases/FeatureBuildId)

* Mon Aug  6 2007 Paul Howarth <paul@city-fan.org> - 1.7-1
- Update to 1.7 (sendmail macro filtering support added)
- Tarball now includes a versioned directory name
- Split milter-regex.conf out from being a here document in the spec and have
  it as a separate source file instead
- Unexpand tabs
- Use the standard scriptlet for user/group creation in %%pre
- Use %%{_initrddir} rather than %%{_sysconfdir}/rc.d/init.d for initscript
- Use %%{__install} rather than %%{__cp} in %%install
- Drop scriptlet dependencies on /sbin/service by calling initscript directly
- LSB-ize initscript (#246983)

* Wed Apr 18 2007 Paul Howarth <paul@city-fan.org> - 1.6-7
- Add patch for compile errors on Fedora 7
- Use sed rather than perl for quick scripted edits

* Tue Aug 29 2006 Paul Howarth <paul@city-fan.org> - 1.6-6
- Rebuild for dynamic linking speedups (FE6)

* Thu May 25 2006 Paul Howarth <paul@city-fan.org> - 1.6-5
- Address issues raised in review (#189611)
  - Add sendmail dependency
  - Honor %%{optflags}

* Fri Apr 21 2006 Paul Howarth <paul@city-fan.org> - 1.6-4
- Minor cosmetic changes for resubmission for Fedora Extras

* Fri Nov 18 2005 Paul Howarth <paul@city-fan.org> - 1.6-3
- Remove redundant ver_ and rel_ macros
- Don't include package name in the summary
- Use macros consistently
- Generate LICENSE file in %%prep rather than %%install
- Don't strip binary, so debuginfo package is useful
- Combine groupadd+useradd into a single useradd command
- Use /sbin/nologin for mregex shell instead of non-existent /bin/nologin
- Don't delete user+group on package removal (see
  http://www.redhat.com/archives/fedora-extras-commits/2005-June/msg00271.html)
- Install initscript in %%{_sysconfdir} rather than /etc/init.d
- Don't enable service by default on installation
- Add scriptlet dependencies
- Add buildreq groff
- Use full URL for source
- Edit username in man page as well as in code
- Use install rather than cp to install %%{SOURCE1} and %%{SOURCE2} so
  that permissions don't need to be set in SRPM
- Ghost the socket for clean package removal
- Buildreq sendmail-devel ≥ 8.13.0 because of the use of SMFIF_QUARANTINE
- Use dist tag

* Tue Jan 25 2005 Victor Ramirez <vramirez@gmail.com> - 1.6-2 
- Initial rpm release
- Modified user and configuration file location.

