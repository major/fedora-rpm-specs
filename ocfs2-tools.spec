%global with_console %{?_with_console: 1} %{?!_with_console: 0}

Summary: Tools for managing the Oracle Cluster Filesystem 2
Name: ocfs2-tools
Version: 1.8.7
Release: 5%{?dist}
License: GPLv2
Source0: https://github.com/markfasheh/%{name}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz
# https://github.com/markfasheh/ocfs2-tools/issues/18#issuecomment-360449375
Patch1:  ocfs2-tools-1.8.5-format-fortify.patch
URL: https://github.com/markfasheh/ocfs2-tools
Requires: bash
Requires: coreutils
Requires: net-tools
Requires: util-linux
Requires: e2fsprogs
Requires: glib2 >= 2.2.3
Provides: ocfs2-tools-pcmk = %{version}
Obsoletes: ocfs2-tools-pcmk < 1.6.3-1

BuildRequires: make
BuildRequires: gcc
BuildRequires: autoconf, automake
%{?systemd_requires}
BuildRequires: systemd
BuildRequires: libuuid-devel
BuildRequires: libcom_err-devel
BuildRequires: libblkid-devel
BuildRequires: glib2-devel >= 2.2.3
BuildRequires: readline-devel
BuildRequires: pacemaker-libs-devel
BuildRequires: dlm-devel
BuildRequires: libaio-devel
BuildRequires: corosynclib-devel
%if %{with_console}
BuildRequires: pygtk2 >= 1.99.16
BuildRequires: python2-devel >= 2.5
%endif

%description
Programs to manage the OCFS2 cluster file system, including mkfs.ocfs2,
tunefs.ocfs2 and fsck.ocfs2.

OCFS2 is a general purpose extent based shared disk cluster file
system. It supports 64 bit inode numbers, and has automatically
extending metadata groups which may also make it attractive for
non-clustered use. OCFS2 leverages some well tested kernel
technologies, such as JBD - the same journaling subsystem in use by
ext3.

%if %{with_console}
%package -n ocfs2console
Summary: GUI frontend for OCFS2 management
Requires: e2fsprogs
Requires: glib2 >= 2.2.3
Requires: vte >= 0.11.10
Requires: pygtk2 >= 1.99.16
Requires: python2 >= 2.5
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n ocfs2console
ocfs2console can make it easier to manage an OCFS2 cluster by
providing a gui front-end to common tasks, including initial cluster
setup.  In addition to cluster setup, ocfs2console can format and
mount OCFS2 volumes.
%endif

%package devel
Summary: Headers and static archives for ocfs2-tools
Requires: e2fsprogs-devel
Requires: glib2-devel >= 2.2.3
Requires: pkgconfig
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: %{name}-static%{?_isa} = %{version}-%{release}

%description devel
ocfs2-tools-devel contains the libraries and header files needed to
develop OCFS2 filesystem-specific programs.

%prep
%autosetup -p1 -n %{name}-%{name}-%{version}
# remove -Wno-format to prevent conflict with rpm optflags
sed -i -e 's/-Wno-format//g' {o2info,o2image,o2monitor}/Makefile

%build
# update config.guess config.sub to support aarch64 and ppc64le
cp -fv /usr/lib/rpm/redhat/config.guess ./config.guess
cp -fv /usr/lib/rpm/redhat/config.sub ./config.sub
./autogen.sh
%{configure} \
%if %{with_console}
    --enable-ocfs2console=yes \
%endif
    --enable-dynamic-fsck=yes

# parallel build currently fails, so no %%{_smp_mflags}
CFLAGS="$(echo '%{optflags}')" make

%install
%make_install

mkdir -p %{buildroot}%{_sysconfdir}/ocfs2
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
cp -p vendor/common/o2cb.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/o2cb
mkdir -p %{buildroot}%{_udevrulesdir}
cp -p vendor/common/51-ocfs2.rules \
  %{buildroot}%{_udevrulesdir}

# for systemd
mkdir -p %{buildroot}/sbin
cp -p vendor/common/{o2cb,ocfs2}.init %{buildroot}/sbin
mkdir -p %{buildroot}%{_unitdir}
cp -p vendor/common/{o2cb,ocfs2}.service %{buildroot}%{_unitdir}
sed -i -e 's/network\.service/network-online.target/' %{buildroot}%{_unitdir}/o2cb.service

chmod 644 %{buildroot}/%{_libdir}/*.a

%if %{with_console}
# rpm autostripper needs to see these as executable
chmod 755 %{buildroot}/%{python2_sitearch}/ocfs2interface/*.so
%endif


%post
%systemd_post {o2cb,ocfs2}.service

%preun
%systemd_preun {o2cb,ocfs2}.service

%postun
%systemd_postun {o2cb,ocfs2}.service


%files
%doc README.O2CB CREDITS MAINTAINERS
%doc documentation/users_guide.txt
%license COPYING
/sbin/o2cb
/sbin/o2cluster
%{_sbindir}/o2hbmonitor
%{_bindir}/o2info
/sbin/fsck.ocfs2
/sbin/mkfs.ocfs2
/sbin/mounted.ocfs2
/sbin/tunefs.ocfs2
/sbin/debugfs.ocfs2
/sbin/defragfs.ocfs2
/sbin/o2cb_ctl
/sbin/mount.ocfs2
/sbin/ocfs2_hb_ctl
/sbin/o2image
/sbin/o2cb.init
/sbin/ocfs2.init
%{_unitdir}/o2cb.service
%{_unitdir}/ocfs2.service
%{_sysconfdir}/ocfs2
%{_udevrulesdir}/51-ocfs2.rules
%config(noreplace) %{_sysconfdir}/sysconfig/o2cb
%{_mandir}/man*/*

%if %{with_console}
%files -n ocfs2console
%dir %{python2_sitearch}/ocfs2interface
%{python2_sitearch}/ocfs2interface/*
%{_sbindir}/ocfs2console
%{_mandir}/man8/ocfs2console.8.gz
%endif

%files devel
%{_libdir}/*.a
%{_libdir}/pkgconfig/*.pc
%dir %{_includedir}/ocfs2-kernel
%dir %{_includedir}/o2cb
%dir %{_includedir}/o2dlm
%dir %{_includedir}/ocfs2
%{_includedir}/ocfs2-kernel/*
%{_includedir}/o2cb/*
%{_includedir}/o2dlm/*
%{_includedir}/ocfs2/*

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul  9 2021 Robin Lee <cheeselee@fedoraproject.org> - 1.8.7-1
- Release 1.8.7

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug  9 2019 Robin Lee <cheeselee@fedoraproject.org> - 1.8.6-1
- Release 1.8.6
- Drop ocfs2console, which requires Python 2 (RHBZ#1738064)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.8.5-10
- Rebuild for readline 8.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 23 2018 Robin Lee <cheeselee@fedoraproject.org> - 1.8.5-8
- Apply patch to change python-config to python2-config
- Apply patch to load dlm_lt by soname

* Sun Jul 15 2018 Robin Lee <cheeselee@fedoraproject.org> - 1.8.5-7
- Fix python2_sitearch macro

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun May 27 2018 Robin Lee <cheeselee@fedoraproject.org> - 1.8.5-6
- Fix build with glibc 2.28

* Sat Mar 10 2018 Robin Lee <cheeselee@fedoraproject.org> - 1.8.5-5
- BR gcc for http://fedoraproject.org/wiki/Changes/Remove_GCC_from_BuildRoot

* Thu Mar 01 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.8.5-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Tue Feb  6 2018 Robin Lee <cheeselee@fedoraproject.org> - 1.8.5-3
- Remove Group tags
- Fix FSF address in files
- Move udev rule to %%{_udevrulesdir}
- Add needed %%{?_isa}
- BR python2-devel

* Mon Jan 29 2018 Robin Lee <cheeselee@fedoraproject.org> - 1.8.5-2
- Fix build for f28
- Move COPYING to %%license
- Use %%make_install
- one BR or R per line

* Tue Mar 28 2017 Robin Lee <cheeselee@fedoraproject.org> - 1.8.5-1
- Update to 1.8.5

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec  3 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 1.6.3-1
- new upstream release
- drop ocfs2-tools-gcc45.patch (now upstream)
- clean up comment sections in spec file
- drop ocfs2-tools-pcmk package/build. -pcmk variants of other packages are gone
- ship o2cb pcmk ras from main package
- clear BuildRequires
- fix linking with readline5 (rhbz: #511308)
- update BuildRoot and usage of RPM_BUILD_ROOT

* Mon Aug 2 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 1.4.3-8
- make the patch use a character string instead of a sequence of characters
  string.  gcc didn't complain but it seems like a better idea.

* Mon Aug 2 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 1.4.3-7
- Patch for gcc45 compilation failures

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 1.4.3-6
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Mon Feb 15 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 1.4.3-5
- Update to use crmcommon and drop linking with stonithd

* Sun Feb 14 2010 Caolán McNamara <caolanm@redhat.com> - 1.4.3-4
- Resolves: rhbz#564744 fix FTBFS

* Fri Oct  9 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 1.4.3-3
- Explicitly BuildRequires: corosynclib-devel

* Wed Sep 30 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 1.4.3-2
- Fix -pcmk Requires.

* Wed Sep 30 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 1.4.3-1
- New upstream release.

* Mon Sep 21 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 1.4.2-5
- Fix pcmk resource agent.

* Tue Sep 15 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 1.4.2-4
- Add pcmk resource agent.

* Thu Sep  3 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 1.4.2-3
- Fix pcmk and cman Requires.

* Wed Sep  2 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 1.4.2-2
- Fix udev rule packaging

* Mon Aug 31 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 1.4.2-1
- New upstream release
- Undefine alpha tag
- Add patch to fix 2 minor build glitches
- Add Requires: redhat-lsb for init scripts
- Update BuildRequires to enable all features
- Add ocfs2-tools-{cman,pcmk} packages with respective control daemons
- Install udev rule
- Update file lists

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.9-11.20080221git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.9-10.20080221git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.3.9-9.20080221git
- Rebuild for Python 2.6

* Thu Jun 19 2008 Fabio M. Di Nitto <fdinitto@redhat.com> - 1.3.9-8.20080221git
- Make alpha tag optional
- Use package names rather than files for Requires
- Clean up changelog in spec file
- Respect fedora build default CFLAGS

* Fri Apr 18 2008 Mark Fasheh <mark@fasheh.com> - 1.3.9-7.20080221git
- Use 'Fedora' as vendor for desktop-file-install

* Thu Feb 21 2008 Mark Fasheh <mark@fasheh.com> - 1.3.9-6.20080221git
- Move to git revision 22fb58d0318a2946479833bb5e2fd58864499c78

* Mon Feb  4 2008 Mark Fasheh <mark@fasheh.com> - 1.3.9-5.20080131git
- Incorporate feedback via bugzilla during review process.

* Thu Jan 31 2008 Mark Fasheh <mark@fasheh.com> - 1.3.9-4.20080131git
- Initial Fedora spec, heavily modified from ocfs2-tools distribution. Thanks
  to Eric Sandeen for helping with this.
