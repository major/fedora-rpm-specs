Name: trousers
Summary: TCG's Software Stack v1.2
Version: 0.3.15
Release: 13%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
Url: http://trousers.sourceforge.net

Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1: tcsd.service
Patch1:  trousers-0.3.14-noinline.patch
# submitted upstream
Patch2: trousers-0.3.14-unlock-in-err-path.patch
Patch3: trousers-0.3.14-fix-indent-obj_policy.patch
Patch4: trousers-0.3.14-fix-indent-tspi_key.patch

BuildRequires: make
BuildRequires: libtool openssl-devel gettext-devel autoconf automake
BuildRequires: systemd
Requires(pre): shadow-utils
# remove systemd dependency for flatpak builds
%if ! 0%{?flatpak}
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units
%endif
Requires: %{name}-lib%{?_isa} = %{version}-%{release}

%description
TrouSerS is an implementation of the Trusted Computing Group's Software Stack
(TSS) specification. You can use TrouSerS to write applications that make use
of your TPM hardware. TPM hardware can create, store and use RSA keys
securely (without ever being exposed in memory), verify a platform's software
state using cryptographic hashes and more.

%package lib
Summary: TrouSerS libtspi library
# Needed obsoletes due to the -lib subpackage split
Obsoletes: trousers < 0.3.13-4

%description lib
The libtspi library for use in Trusted Computing enabled applications.

%package static
Summary: TrouSerS TCG Device Driver Library
Requires: %{name}-devel%{?_isa} = %{version}-%{release}

%description static
The TCG Device Driver Library (TDDL) used by the TrouSerS tcsd as the
interface to the TPM's device driver. For more information about writing
applications to the TDDL interface, see the latest TSS spec at
https://www.trustedcomputinggroup.org/specs/TSS.

%package devel
Summary: TrouSerS header files and documentation
Requires: %{name}-lib%{?_isa} = %{version}-%{release}

%description devel
Header files and man pages for use in creating Trusted Computing enabled
applications.

%prep
%autosetup -p1
# fix man page paths
sed -i -e 's|/var/tpm|/var/lib/tpm|g' -e 's|/usr/local/var|/var|g' man/man5/tcsd.conf.5.in man/man8/tcsd.8.in

%build
chmod +x ./bootstrap.sh
./bootstrap.sh
%configure --with-gui=openssl
make -k %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_localstatedir}/lib/tpm
%make_install
find %{buildroot} -type f -name '*.la' -print -delete
mkdir -p %{buildroot}%{_unitdir}
install -Dpm0644 %{SOURCE1} %{buildroot}%{_unitdir}/

%pre
getent group tss >/dev/null || groupadd -f -g 59 -r tss
if ! getent passwd tss >/dev/null ; then
    if ! getent passwd 59 >/dev/null ; then
      useradd -r -u 59 -g tss -d /dev/null -s /sbin/nologin -c "Account used for TPM access" tss
    else
      useradd -r -g tss -d /dev/null -s /sbin/nologin -c "Account used for TPM access" tss
    fi
fi
exit 0

%post
%systemd_post tcsd.service

%preun
%systemd_preun tcsd.service

%postun
%systemd_postun_with_restart tcsd.service 

%files
%doc README ChangeLog
%{_sbindir}/tcsd
%config(noreplace) %attr(0640, root, tss) %{_sysconfdir}/tcsd.conf
%{_mandir}/man5/*
%{_mandir}/man8/*
%attr(644,root,root) %{_unitdir}/tcsd.service
%attr(0700, tss, tss) %{_localstatedir}/lib/tpm/

%files lib
%license LICENSE
%{_libdir}/libtspi.so.1*

%files devel
# The files to be used by developers, 'trousers-devel'
%doc doc/LTC-TSS_LLD_08_r2.pdf doc/TSS_programming_SNAFUs.txt
%attr(0755, root, root) %{_libdir}/libtspi.so
%{_includedir}/tss/
%{_includedir}/trousers/
%{_mandir}/man3/Tspi_*

%files static
# The only static library shipped by trousers, the TDDL
%{_libdir}/libtddl.a

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.15-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.3.15-12
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.15-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.15-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.15-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 0.3.15-5
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.3.15-3
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 06 2020 Jerry Snitselaar <jsnitsel@redhat.com> - 0.3.15-1
- Rebase to 0.3.15 release.

* Thu Oct 29 2020 Jerry Snitselaar <jsnitsel@redhat.com> - 0.3.14-4
- Fix for CVE-2020-24330 (RHBZ#1874824)
- Fix for CVE-2020-24331 (RHBZ#1870057)
- Fix for CVE-2020-24332 (RHBZ#1870053)

* Tue Sep 15 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.3.14-3
- Update user creation to latest guidelines

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Mar 18 2020 Jerry Snitselaar <jsnitsel@redhat.com> - 0.3.14-1
- Rebase to 0.3.14 release

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.13-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.13-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.13-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.13-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.13-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.13-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb  7 2017 Peter Robinson <pbrobinson@fedoraproject.org> 0.3.13-7
- Add patch for OpenSSL 1.1

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 26 2015 Tomáš Mráz <tmraz@redhat.com> 0.3.13-4
- Split libtspi to a trousers-lib subpackage (#1225062)
- Fix FTBFS with current gcc (drop inline keyword when bogus)

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 15 2014 Steve Grubb <sgrubb@redhat.com> 0.3.13-1
- New upstream bug fix release

* Tue Mar 18 2014 Steve Grubb <sgrubb@redhat.com> 0.3.11.2-3
- Fix crash when linking libgnutls and libmysqlclient (#1069079)
- Don't order tcsd after syslog.target (#1055198)

* Thu Feb 13 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.3.11.2-2
- Minor spec cleanups

* Mon Aug 19 2013 Steve Grubb <sgrubb@redhat.com> 0.3.11.2-1
- New upstream bug fix and license change release

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 02 2013 Steve Grubb <sgrubb@redhat.com> 0.3.10-3
- Remove +x bit from service file (#963916)

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Sep 25 2012 Steve Grubb <sgrubb@redhat.com> 0.3.10-1
- New upstream bug fix release

* Thu Aug 30 2012 Steve Grubb <sgrubb@redhat.com> 0.3.9-4
- Make daemon full RELRO

* Mon Aug 27 2012 Steve Grubb <sgrubb@redhat.com> 0.3.9-3
- bz #836476 - Provide native systemd service

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 21 2012 Steve Grubb <sgrubb@redhat.com> 0.3.9-1
- New upstream bug fix release

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Apr 08 2011 Steve Grubb <sgrubb@redhat.com> 0.3.6-1
- New upstream bug fix release

* Thu Feb 10 2011 Miloš Jakubíček <xjakub@fi.muni.cz> - 0.3.4-5
- Fix paths in man pages, mark them as %%doc -- fix BZ#676394

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat May 01 2010 Miloš Jakubíček <xjakub@fi.muni.cz> - 0.3.4-3
- Fix init script to conform to Fedora guidelines
- Do not overuse macros

* Mon Feb 08 2010 Steve Grubb <sgrubb@redhat.com> 0.3.4-2
- Fix issue freeing a data structure

* Fri Jan 29 2010 Steve Grubb <sgrubb@redhat.com> 0.3.4-1
- New upstream bug fix release
- Upstream requested the tpm-emulator patch be dropped

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 0.3.1-19
- rebuilt with new openssl

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu May 14 2009 Milos Jakubicek <xjakub@fi.muni.cz> - 0.3.1-17
- Do not overuse macros.
- Removed unnecessary file requirements on chkconfig, ldconfig and service,
  now requiring the initscripts and chkconfig packages.

* Wed May 06 2009 Milos Jakubicek <xjakub@fi.muni.cz> - 0.3.1-16
- Fix a typo in groupadd causing the %%pre scriptlet to fail (resolves BZ#486155).

* Mon Apr 27 2009 Milos Jakubicek <xjakub@fi.muni.cz> - 0.3.1-15
- Fix FTBFS: added trousers-0.3.1-gcc44.patch

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 18 2009 Tomas Mraz <tmraz@redhat.com> - 0.3.1-13
- rebuild with new openssl

* Tue Dec 16 2008 David Woodhouse <David.Woodhouse@intel.com> - 0.3.1-12
- Bump release to avoid wrong tag in rawhide

* Tue Dec 16 2008 David Woodhouse <David.Woodhouse@intel.com> - 0.3.1-11
- Work around SELinux namespace pollution (#464037)
- Use SO_REUSEADDR
- Use TPM emulator if it's available and no hardware is

* Fri Aug 08 2008 Emily Ratliff <ratliff@austin.ibm.com> - 0.3.1-10
- Use the uid/gid pair assigned to trousers from BZ#457593

* Fri Aug 01 2008 Emily Ratliff <ratliff@austin.ibm.com> - 0.3.1-9
- Incorporated changes from the RHEL package which were done by Steve Grubb

* Wed Jun 04 2008 Emily Ratliff <ratliff@austin.ibm.com> - 0.3.1-8
- Fix cast issue preventing successful build on ppc64 and x86_64

* Tue Jun 03 2008 Emily Ratliff <ratliff@austin.ibm.com> - 0.3.1-7
- Fix for BZ #434267 and #440733. Patch authored by Debora Velarde

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.3.1-6
- Autorebuild for GCC 4.3

* Mon Dec 17 2007 Kent Yoder <kyoder@users.sf.net> - 0.3.1-5
- Updated static rpm's comment line (too long)

* Thu Dec 13 2007 Kent Yoder <kyoder@users.sf.net> - 0.3.1-4
- Updated specfile for RHBZ#323441 comment #28

* Wed Dec 12 2007 Kent Yoder <kyoder@users.sf.net> - 0.3.1-3
- Updated specfile for RHBZ#323441 comment #22

* Wed Nov 28 2007 Kent Yoder <kyoder@users.sf.net> - 0.3.1-2
- Updated to include the include dirs in the devel package;
added the no-install-hooks patch

* Wed Nov 28 2007 Kent Yoder <kyoder@users.sf.net> - 0.3.1-1
- Updated specfile for RHBZ#323441 comment #13

* Mon Nov 12 2007 Kent Yoder <kyoder@users.sf.net> - 0.3.1
- Updated specfile for comments in RHBZ#323441

* Wed Jun 07 2006 Kent Yoder <kyoder@users.sf.net> - 0.2.6-1
- Updated build section to use smp_mflags
- Removed .la file from installed dest and files section

* Tue Jun 06 2006 Kent Yoder <kyoder@users.sf.net> - 0.2.6-1
- Initial add of changelog tag for trousers CVS
