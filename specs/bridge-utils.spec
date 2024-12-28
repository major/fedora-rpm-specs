Summary:        Utilities for configuring the linux ethernet bridge
Name:           bridge-utils
Version:        1.7.1
Release:        11%{?dist}
License:        GPL-2.0-or-later
URL:            https://wiki.linuxfoundation.org/networking/bridge

Source0:        https://git.kernel.org/pub/scm/network/bridge/%{name}.git/snapshot/%{name}-%{version}.tar.gz

BuildRequires:  libsysfs-devel
BuildRequires:  autoconf automake libtool
BuildRequires:  gcc
BuildRequires:  kernel-headers >= 2.6.16
BuildRequires:  make

%description
This package contains utilities for configuring the linux ethernet
bridge. The linux ethernet bridge can be used for connecting multiple
ethernet devices together. The connecting is fully transparent: hosts
connected to one ethernet device see hosts connected to the other
ethernet devices directly.

The bridge-utils package is deprecated, the bridge command from the
iproute package should preferably be used for linux ethernet bridges.

%prep
%setup -q

%build
autoconf
%configure
%make_build

%install
%make_install SUBDIRS="brctl doc"

%files
%license COPYING
%doc AUTHORS doc/FAQ doc/HOWTO
%{_sbindir}/brctl
%{_mandir}/man8/brctl.8*

%changelog
* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.7.1-11
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar 15 2021 Robert Scheck <robert@fedoraproject.org> - 1.7.1-2
- Use make macros
- https://fedoraproject.org/wiki/Changes/UseMakeBuildInstallMacro

* Mon Mar 15 2021 David Woodhouse <dwmw2@infradead.org> - 1.7.1-1
- Update to 1.7.1 (#1850243)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 23 2018 Michael Cronenworth <mike@cchtml.com> - 1.6-1
- 1.6 bump

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 21 2015 Peter Robinson <pbrobinson@fedoraproject.org> 1.5-12
- Use system CFLAGS to build libbridge so properly hardened etc (fix FTBFS)
- Use %%license, spec cleanups

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 26 2013 Thomas Woerner <twoerner@redhat.com> - 1.5-7
- fixed build with kernel 3.8.x using upstream fix by Russell Senior

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 19 2012 Nils Philippsen <nils@redhat.com> - 1.5-5
- update sourceforge download URL

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon May 30 2011 Petr Sabata <contyk@redhat.com> - 1.5-2
- Add three latest bugfixes from upstream git on top of 1.5
- Dropping params patch (included upstream variant)

* Mon May 30 2011 Petr Sabata <contyk@redhat.com> - 1.5-1
- 1.5 bump
- BuildRoot and defattr cleanup
- Use macros in Sources
- Drop show-ports and foreach patches -- those have been included upstream

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 20 2010 Bill Nottingham <notting@redhat.com> - 1.2-9
- Fix URL (#248086)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jul 03 2008 David Woodhouse <david.woodhouse@intel.com> 1.2-6
- Fix location of bridge parameters in sysfs

* Wed Mar 05 2008 David Woodhouse <dwmw2@redhat.com> 1.2-5
- Fix handling of bridge named 'bridge' (#436120)

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.2-4
- Autorebuild for GCC 4.3

* Mon Dec 10 2007 Patrick "Jima" Laughton <jima@beer.tclug.org> 1.2-3
- Minor tweaks as recommended in merge review (BZ#225625)

* Wed Aug 22 2007 David Woodhouse <dwmw2@redhat.com> 1.2-2
- Update licence

* Wed Aug 22 2007 David Woodhouse <dwmw2@redhat.com> 1.2-1
- Update to 1.2

* Sat Sep 09 2006 David Woodhouse <dwmw2@redhat.com> 1.1-2
- Fix setportprio command (#205810)
- Other updates from bridge-utils git tree

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.1-1.1
- rebuild

* Wed Jun 07 2006 David Woodhouse <dwmw2@redhat.com> 1.1-1
- Update to 1.1
- BR libsysfs-devel instead of sysfsutils-devel

* Wed Jun 07 2006 David Woodhouse <dwmw2@redhat.com> 1.0.6-2
- Use sane kernel headers, drop -devel package

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.0.6-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.0.6-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Wed Dec 21 2005 David Woodhouse <dwmw2@redhat.com> 1.0.6-1
- Update to 1.0.6
- Cleanups from Matthias Saou (#172774)

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Mar 2 2005 David Woodhouse <dwmw2@redhat.com> 1.0.4-6
- Rebuild with gcc 4

* Tue Feb 15 2005 David Woodhouse <dwmw2@redhat.com> 1.0.4-5
- Rebuild

* Thu Aug 26 2004 David Woodhouse <dwmw2@redhat.com> 1.0.4-4
- BuildRequires: sysfsutils-devel to make the horrid autoconf script magically
  change the entire package's behaviour just because it happens to find
  slightly different header files lying around.
- Include our own kernel-derived headers

* Thu Jul 1 2004 David Woodhouse <dwmw2@redhat.com>
- Update to 1.0.4

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Sat Oct 25 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- support change to call sysconf() to get HZ

* Tue Sep 16 2003 David Woodhouse <dwmw2@redhat.com> 0.9.6-1
- Update to 0.9.6
- Detect lack of kernel bridge support or EPERM and exit with appropriate code.

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Fri Dec 13 2002 Elliot Lee <sopwith@redhat.com> 0.9.3-7
- Rebuild

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Mar 04 2002 Benjamin LaHaise <bcrl@redhat.com>
- manual rebuild

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Nov 07 2001 Matthew Galgoci <mgalgoci@redhat.com>
- initial cleanup of spec file from net release
