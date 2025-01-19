Name: p0f
Version: 3.09b
Release: 22%{?dist}

Summary: Versatile passive OS fingerprinting tool
License: LGPL-2.0-or-later
URL: http://lcamtuf.coredump.cx/p0f.shtml
Source: http://lcamtuf.coredump.cx/p0f3/releases/p0f-%{version}.tgz
# Fix up build script to use proper flags
Patch1: p0f-3.06b-compiler.patch
Patch2: p0f-configure-c99.patch
BuildRequires: make
BuildRequires: libpcap-devel
BuildRequires: gcc

%description
P0f is a versatile passive OS fingerprinting tool. P0f can identify the
system on machines that talk thru or near your box. p0f will also check
masquerading and firewall presence, the distance to the remote system and its
uptime, other guy's network hookup (DSL, OC3, avian carriers) and his ISP.


%prep
%autosetup

%build
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS -DFP_FILE=\"%{_sysconfdir}/p0f/p0f.fp\""


%install
rm -rf $RPM_BUILD_ROOT
%{__mkdir_p} $RPM_BUILD_ROOT%{_sbindir}
%{__mkdir_p} $RPM_BUILD_ROOT%{_sysconfdir}/p0f
%{__cp} p0f $RPM_BUILD_ROOT%{_sbindir}
%{__cp} p0f.fp $RPM_BUILD_ROOT%{_sysconfdir}/p0f

# Build the tools
cd tools
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS"

%{__cp} p0f-client p0f-sendsyn p0f-sendsyn6 $RPM_BUILD_ROOT%{_sbindir}



%files
%doc docs/*
%doc tools/README-TOOLS
%{_sbindir}/*
%dir %{_sysconfdir}/p0f
%config %{_sysconfdir}/p0f/p0f.fp


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.09b-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.09b-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat May 25 2024 Kevin Fenzi <kevin@scrye.com> - 3.09b-20
- Update spec for patch/rpm changes.
- migrated to SPDX license identifier

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.09b-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.09b-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.09b-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.09b-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 17 2023 Florian Weimer <fweimer@redhat.com> - 3.09b-15
- Fix pre-build probe for C99 compatibility (#2161649)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.09b-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.09b-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.09b-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.09b-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.09b-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.09b-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.09b-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.09b-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.09b-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.09b-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.09b-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.09b-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.09b-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Apr 19 2016 Kevin Fenzi <kevin@scrye.com> - 3.09b-1
- Update to 3.09b

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.08b-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.08b-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Nov 12 2014 Kevin Fenzi <kevin@scrye.com> 3.08b-1
- Update to 3.08b

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.07b-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.07b-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Kevin Fenzi <kevin@scrye.com> 3.07b-1
- Update to 3.07b

* Sun Feb 23 2014 Athmane Madjoudj <athmane@fedoraproject.org> 3.06b-5
- Fix bogus date in the changelog

* Mon Dec 02 2013 Kevin Fenzi <kevin@scrye.com> 3.06b-4
- Patch build.sh to use correct compiler flags. Fixes bug #1037237

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.06b-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.06b-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Dec 08 2012 Athmane Madjoudj <athmane@fedoraproject.org> 3.06b-1
- Update to 3.06b

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.05b-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 20 2012 Athmane Madjoudj <athmane@fedoraproject.org> 3.05b-1
- Update to last upstream release

* Wed Feb 08 2012 Athmane Madjoudj <athmane@fedoraproject.org> - 3.03b-10
- Update to 3.03b
- Fix FP_FILE path (reported by Michal Ambroz)

* Mon Jan 16 2012 Athmane Madjoudj <athmane@fedoraproject.org> - 3.00b-9
- Update to 3.00b
- Clean-up the spec

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 10 2008 Kevin Fenzi <kevin@tummy.com> - 2.0.8-4
- Rebuild for gcc43

* Thu Oct 11 2007 Kevin Fenzi <kevin@tummy.com> - 2.0.8-3
- Rebuild for BuildID
- Update License tag

* Wed Nov 29 2006 Kevin Fenzi <kevin@tummy.com> - 2.0.8-2
- Rebuild for new libpcap

* Sat Nov 11 2006 Kevin Fenzi <kevin@tummy.com> - 2.0.8-1
- Update to 2.0.8

* Sun Aug 27 2006 Kevin Fenzi <kevin@tummy.com> - 2.0.7-2
- Rebuild for fc6

* Wed Aug 23 2006 Kevin Fenzi <kevin@tummy.com> - 2.0.7-1
- Update to 2.0.7

* Thu Jun 29 2006 Kevin Fenzi <kevin@tummy.com> - 2.0.6-2
- libpcap to libpcap-devel in BuildRequires

* Mon May  8 2006 Kevin Fenzi <kevin@tummy.com> - 2.0.6-1
- Upgrade to 2.0.6
- Remove unneeded include patch (fixed upstream)

* Thu Feb 16 2006 Kevin Fenzi <kevin@tummy.com> - 2.0.5-4.fc5
- Rebuild for fc5
- Add dist tag

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 2.0.5-3
- rebuild on all arches

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Tue Oct 26 2004 Adrian Reber <adrian@lisas.de> - 0:2.0.5-1
- updated to 2.0.5
- fixed build on FC2
- bring specfile up to date with current spec templates

* Mon Oct 27 2003 Darryl Luff <darryl@snakegully.nu> - 0:2.0.2-0.fdr.0.1
- Update for version 2.0.2 and Fedora comments.

* Sat Sep 6 2003 Darryl Luff <darryl@snakegully.nu> - 0:2.0.1-0.fdr.0.1
- initial RPM

