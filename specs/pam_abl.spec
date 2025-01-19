Name:           pam_abl
Summary:        A Pluggable Authentication Module (PAM) for auto blacklisting
Version:        0.6.0
Release:        28%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://pam-abl.sourceforge.net/
Source0:        http://downloads.sourceforge.net/pam-abl/pam-abl-%{version}.tar.gz
Patch0:         pam_abl-0.6.0-whitelistroot.patch
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libdb-devel pam-devel cmake asciidoc

%description
Provides auto blacklisting of hosts and users responsible for repeated
failed authentication attempts. Generally configured so that
blacklisted users still see normal login prompts but are guaranteed to
fail to authenticate. A command line tool allows to query or purge the
databases used by the pam_abl module.

%prep
%setup -q -c
%patch -P0 -p 1 -b .whitelistroot

%build
%cmake
%cmake_build
cd doc
sh generate.sh

%install
%cmake_install
install -d -m 755 ${RPM_BUILD_ROOT}/%{_libdir}/security

# The build process puts the shared library in /usr/lib even if it should be
# in a different directory (e.g., /usr/lib64).  Fix with mv.
# NOTE: the mv command will cause a spurious hardcoded-libary-path error from
# rpmlint. The mv command is acutally *correcting* that problem.
%if %(test "%{_libdir}" != "/usr/lib" && echo 1 || echo 0)
  mv ${RPM_BUILD_ROOT}/usr/lib/security/pam_abl.so  ${RPM_BUILD_ROOT}/%{_libdir}/security/pam_abl.so 
%endif

install -D -m 644 conf/pam_abl.conf %{buildroot}%{_sysconfdir}/security/pam_abl.conf
install -d -m 755 %{buildroot}%{_localstatedir}/lib/abl

install -D -m 644 doc/pam_abl.1      %{buildroot}%{_mandir}/man1/pam_abl.1
install -D -m 644 doc/pam_abl.conf.5 %{buildroot}%{_mandir}/man5/pam_abl.conf.5
install -D -m 644 doc/pam_abl.8      %{buildroot}%{_mandir}/man8/pam_abl.8

%files
%doc README
%config(noreplace) %{_sysconfdir}/security/pam_abl.conf
%{_libdir}/security/pam_abl.so
%{_bindir}/pam_abl
%{_localstatedir}/lib/abl/
%{_mandir}/man?/*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.6.0-27
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 15 2020 Petr Pisar <ppisar@redhat.com> - 0.6.0-17
- Adapt to new CMake packaging macros (bug #1865194)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-16
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Sep 06 2013 Eric Smith <brouhaha@fedordaproject.org> - 0.6.0-2
- Change user whitelist to root, and remove host whitelist (bug #985371).

* Fri Sep 06 2013 Eric Smith <brouhaha@fedordaproject.org> - 0.6.0-1
- Update to latest upstream.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 05 2013 Eric Smith <brouhaha@fedordaproject.org> - 0.5.0-2
- Change name of command line utility to pam_abl (with underscore) for
  consistency with man page and examples therein.

* Wed Jun 05 2013 Eric Smith <brouhaha@fedordaproject.org> - 0.5.0-1
- Update to latest upstream.

* Tue Feb 19 2013 Mat Booth <fedora@matbooth.co.uk> - 0.2.3-15
- Build against libdb instead of libdb4.

* Tue Feb 19 2013 Mat Booth <fedora@matbooth.co.uk> - 0.2.3-14
- Fix FTBFS following mass rebuild.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 05 2012 Petr Pisar <ppisar@redhat.com> - 0.2.3-11
- Rebase pam_abl-0.2.3-fixes.patch

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul  9 2008 Tomas Mraz <tmraz@redhat.com> - 0.2.3-6
- fix build (#449429)

* Wed May 21 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.2.3-5
- fix license tag

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.2.3-4
- Autorebuild for GCC 4.3

* Sun May 13 2007 Alexander Dalloz <alex {%} dalloz {*} de> - 0.2.3-3
- Rebuild to fix #219947.

* Tue Aug 29 2006 Alexander Dalloz <alex {%} dalloz {*} de> - 0.2.3-2
- Rebuild for FC6.

* Sun Jul 16 2006 Alexander Dalloz <alex {%} dalloz {*} de> - 0.2.3-1
- Upgrade to 0.2.3
  - fixes #165817, #174932, #185866, #192614
- Added manpage, improved documentation
  (big thanks to Robert Scheck)

* Fri Jul 15 2005 Alexander Dalloz <alex {%} dalloz {*} de> - 0.2.2-2
- Defined %%{reldate} and made macro usage consistent
- pam_abl moved to /usr/sbin.

* Wed Jul 13 2005 Alexander Dalloz <alex {%} dalloz {*} de> - 0.2.2-1
- Changes following review:
  - added %%{?dist} tag
  - set Group to System Environment/Base
  - set Source0 to be an absolute URL
  - changed BuildPrereq to be BuildRequires
  - moved instructions into README.Fedora
- dropped release date in tarball name as release number flag
- removed outdated instruction in example system-auth doc file.

* Mon Jul 11 2005 Alexander Dalloz <alex {%} dalloz {*} de> - 0.2.2-20050110
- Initial build.
