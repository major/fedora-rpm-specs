
Summary:		Automated Password Generator for random password generation
Name:			apg

Version:		2.3.0b
Release:		48%{?dist}
License:		BSD-3-Clause
URL:			http://www.adel.nursat.kz/%{name}/

# Unpacked tarball, fixed permissions (chmod 755 all dirs) and reuploaded
Source0:		http://www.adel.nursat.kz/%{name}/download/%{name}-%{version}.tar.gz
Source1:		apg.socket
Source2:		apg@.service
Patch0:			apg-2.3.0b-gen_rand_pass.patch
Patch1:                 apg-2.3.0b-null-crypt.patch

BuildRequires: systemd-units
BuildRequires: gcc
BuildRequires: make
Requires(post): grep
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units

%description
APG (Automated Password Generator) is the tool set for random password
generation. This standalone version generates some random words of
required type and prints them to standard output.

%prep
%setup -q

%patch -P 0 -p1 -b .gen_rand_pass
%patch -P 1 -p1

%build
# Build server
make CFLAGS="$RPM_OPT_FLAGS" FLAGS="$RPM_OPT_FLAGS" %{?_smp_mflags} cliserv

# Build standalone files
make CFLAGS="$RPM_OPT_FLAGS" FLAGS="$RPM_OPT_FLAGS" %{?_smp_mflags} standalone

%install
install -D apg %{buildroot}%{_bindir}/apg
install -D apgbfm %{buildroot}%{_bindir}/apgbfm
install -D apgd %{buildroot}%{_sbindir}/apgd
install -D -m 644 doc/man/apg.1 %{buildroot}%{_mandir}/man1/apg.1
install -D -m 644 doc/man/apgbfm.1 %{buildroot}%{_mandir}/man1/apgbfm.1
install -D -m 644 doc/man/apgd.8 %{buildroot}%{_mandir}/man8/apgd.8
install -d -m 755 %{buildroot}%{_unitdir}

install -p -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.socket
install -p -m 644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}@.service

%post
# add a service for apg if it doesn't already exist
/bin/grep ^pwdgen /etc/services >& /dev/null
if [ $? == 1 ]; then
    echo -e 'pwdgen\t\t129/tcp\t\t\t# PWDGEN service' >> /etc/services
fi
%if 0%{?fedora} > 17
	%systemd_post apg@.service
%else
if [ $1 -eq 1 ]; then
    # Initial installation
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi
%endif

%preun
%if 0%{?fedora} > 17
	%systemd_preun apg@.service
%else
if [ $1 -eq 0 ]; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable apg@.service > /dev/null 2>&1 || :
    /bin/systemctl stop apg@.service > /dev/null 2>&1 || :
fi
%endif

%postun
%if 0%{?fedora} > 17
	%systemd_postun apg@.service
%else
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ]; then
    # Package upgrade, not uninstall
    /bin/systemctl try-restart apg@.service >/dev/null 2>&1 || :
fi
%endif

%files
%doc CHANGES COPYING README THANKS TODO doc/rfc*
%{_bindir}/apg
%{_bindir}/apgbfm
%{_sbindir}/apgd
%{_mandir}/man*/*
%{_unitdir}/%{name}@.service
%{_unitdir}/%{name}.socket

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0b-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0b-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0b-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0b-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0b-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 08 2023 Gwyn Ciesla <gwync@protonmail.com> - 2.3.0b-43
- migrated to SPDX license

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0b-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0b-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0b-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0b-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0b-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0b-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0b-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0b-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0b-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 2.3.0b-33
- Rebuilt for libcrypt.so.2 (#1666033)

* Sun Jul 15 2018 Kevin Fenzi <kevin@scrye.com> - 2.3.0b-32
- Add BuildRequires gcc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 06 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0b-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Feb 06 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0b-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 2.3.0b-29
- Rebuilt for switch to libxcrypt

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0b-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0b-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0b-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0b-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0b-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0b-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0b-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0b-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 16 2013 Kevin Fenzi <kevin@scrye.com> 2.3.0b-20
- Fix permissions on systemd files to be 644. Fixes bug #963913

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0b-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Aug 25 2012 Kevin Fenzi <kevin@scrye.com> 2.3.0b-18
- Add systemd preset macros. Fixes bug #850026

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0b-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 03 2012 Kevin Fenzi <kevin@scrye.com> 2.3.0b-16
- Fix odd space characters in scriptlets. Fixes bug #827815

* Wed May 30 2012 Kevin Fenzi <kevin@scrye.com> 2.3.0b-15
- Fix typo in scriptlet. Fixes bug #826638

* Mon Apr 23 2012 Kevin Fenzi <kevin@scrye.com> 2.3.0b-14
- Add patch to handle crypt returning NULL. Fixes bug #815575

* Sat Jan 28 2012 Kevin Fenzi <kevin@scrye.com> 2.3.0b-13
- Convert to use systemd instead of xinetd. Fixes bug #737168

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0b-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Mar 14 2011 Kevin Fenzi <kevin@tummy.com> - 2.3.0b-11
- Add Requires(post) on grep. Fixes bug #684779

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0b-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0b-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0b-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Aug 11 2008 Kevin Fenzi <kevin@tummy.com> - 2.3.0b-7
- Fix permissions. Fixes #453621

* Sun Feb 10 2008 Kevin Fenzi <kevin@tummy.com> - 2.3.0b-6
- Rebuild for gcc43

* Tue Aug 21 2007 Kevin Fenzi <kevin@tummy.com> - 2.3.0b-5
- Fix incorrect license tag
- Fix incorrect sources

* Sun Aug 27 2006 Kevin Fenzi <kevin@tummy.com> - 2.3.0b-4
- Rebuild for fc6

* Thu Feb 16 2006 Kevin Fenzi <kevin@tummy.com> - 2.3.0b-3
- Rebuild for fc5

* Sat Jul 30 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 2.3.0b-2
- Fix -y segfault (#164698).
- Make with CFLAGS and FLAGS to build with RPM optflags to
  repair debuginfo package.

* Fri Apr 22 2005 Oliver Falk <oliver@linux-kernel.at>				- 2.3.0b-1_FC4
- Add FC4 to the release tag, so it's newer than the FC3 package

* Mon Apr 11 2005 Oliver Falk <oliver@linux-kernel.at>				- 2.3.0b-1
- Merge FC devel specfile with lkernAT specfile (=> update)
- Has now support for xinetd

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Wed Nov 10 2004 Matthias Saou <http://freshrpms.net/> 2.2.3-3
- Bump release to provide Extras upgrade path.
- Nicer mode fix for the sources.

* Sun Sep 21 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:2.2.3-0.fdr.2
- Fixed file permission on source tarball.
- Brought spec more in line with current template.

* Mon Sep 15 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:2.2.3-0.fdr.1
- Updated to 2.2.3.

* Mon Sep 01 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:2.2.2-0.fdr.1
- Updated to 2.2.2.

* Tue Aug 05 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:2.2.0-0.fdr.1
- Updated to 2.2.0.

* Wed Jul 30 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:2.1.0-0.fdr.1
- Fedorafication.

* Mon Mar 31 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Rebuilt for Red Hat Linux 9.
- Added _smp_mflags macro.

* Fri Oct  4 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 2.1.0.

* Thu May  2 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 2.0.0final.

* Tue Feb 27 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.2.13.

* Fri Feb 16 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.2.11.

* Thu Feb 15 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.2.1.

* Wed Feb  7 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Initial RPM release.
