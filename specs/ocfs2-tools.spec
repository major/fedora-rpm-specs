%global with_console %{?_with_console: 1} %{?!_with_console: 0}

Summary: Tools for managing the Oracle Cluster Filesystem 2
Name: ocfs2-tools
Version: 1.8.9
Release: %autorelease
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
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
cp -p vendor/common/51-ocfs2.rules %{buildroot}%{_udevrulesdir}

# for systemd
mkdir -p %{buildroot}%{_sbindir}
cp -p vendor/common/{o2cb,ocfs2}.init %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_unitdir}
cp -p vendor/common/{o2cb,ocfs2}.service %{buildroot}%{_unitdir}
sed -i -e 's/network\.service/network-online.target/' %{buildroot}%{_unitdir}/o2cb.service

chmod 644 %{buildroot}/%{_libdir}/*.a

%if %{with_console}
# rpm autostripper needs to see these as executable
chmod 755 %{buildroot}/%{python2_sitearch}/ocfs2interface/*.so
%endif

# Move files to the correct location
mv %{buildroot}/sbin/*  %{buildroot}%{_sbindir}

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
%{_bindir}/o2info
%{_sbindir}/o2cb
%{_sbindir}/o2cluster
%{_sbindir}/o2hbmonitor
%{_sbindir}/fsck.ocfs2
%{_sbindir}/mkfs.ocfs2
%{_sbindir}/mounted.ocfs2
%{_sbindir}/tunefs.ocfs2
%{_sbindir}/debugfs.ocfs2
%{_sbindir}/defragfs.ocfs2
%{_sbindir}/o2cb_ctl
%{_sbindir}/mount.ocfs2
%{_sbindir}/ocfs2_hb_ctl
%{_sbindir}/o2image
%{_sbindir}/o2cb.init
%{_sbindir}/ocfs2.init
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
%autochangelog
