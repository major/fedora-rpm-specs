%global commit6 e23b9d3726b010c9e747786ffe72e38debc8cfef
%global shortcommit %(c=%{commit6}; echo ${c:0:7})
%global repo https://github.com/iguanaworks/iguanair-lirc/archive
%global __python %{__python3}

Name:           iguanaIR
Version:        1.1.0
Release:        42%{?dist}
Epoch:          2
Summary:        Driver for Iguanaworks USB IR transceiver

# Automatically converted from old format: GPLv2 and LGPLv2 - review is highly recommended.
License:        GPL-2.0-only AND LicenseRef-Callaway-LGPLv2
URL:            http://iguanaworks.net/ir
Source0:        http://iguanaworks.net/downloads/%{name}-%{version}.tar.bz2
Source1:        iguanaIR.service
Source2:        iguanaIR-rescan
Source3:        README.fedora
Source4:        patch-soname
Source5:        iguanaIR.logrotate
Source6:        %{repo}/%{commit6}/iguanair-lirc-%{shortcommit}.tar.gz
# https://iguanaworks.net/projects/IguanaIR/ticket/317
Patch1:         changeset_2710.patch
Patch2:         rpath.patch
Patch3:         cmake-args.patch

# https://github.com/iguanaworks/iguanair-lirc/pull/1 (Patch10..Patch13)
Source10:       0010-Change-iguanaIR.-iguanair.-to-match-other-plugins.patch
Source11:       0011-Rename-link-README-files-to-match-modified-install-r.patch
Source12:       0012-Makefile-Add-DESTDIR-support.patch
Source13:       0013-Convert-all-files-to-LF-line-endings-like-main-drive.patch

Source20:       0020-build-Fix-DESTDIR-dont-update-docs.patch
Source21:       0016-reflasher-Move-to-python3.patch

Requires:       udev

BuildRequires:  cmake gcc
BuildRequires:  dos2unix
BuildRequires:  git
BuildRequires:  libusb1-devel
%if 0%{?fedora} < 37
libusb-devel
%endif
BuildRequires:  popt-devel
BuildRequires:  systemd

%{?systemd_requires}
Requires(post): systemd-sysv

# some features can be disabled during the rpm build
%{?_without_clock_gettime: %define _disable_clock_gettime --disable-clock_gettime}

# Filter away versioned plugin deps (they only depend on ABI):
%global __provides_exclude_from ^%{_libdir}/lirc/plugins/.*$


%description
This package provides igdaemon and igclient, the programs necessary to
control the Iguanaworks USB IR transceiver.


%package devel
Summary: Library and header files for iguanaIR
Requires: %{name} = %{epoch}:%{version}-%{release}

%description devel
The development files needed to interact with the iguanaIR igdaemon are
included in this package.


%package reflasher
Summary: Reflasher for Iguanaworks USB IR transceiver
BuildArch: noarch

%description reflasher
This package provides the reflasher/testing script and assorted firmware
versions for the Iguanaworks USB IR transceiver.  If you have no idea
what this means, you don't need it.


%if 0%{fedora} > 23
%package -n lirc-drv-iguanair
Summary: lirc plugin for iguanair user-space driver
Requires: lirc >= 0.9.4
BuildRequires: lirc-devel >= 0.9.4
BuildRequires: make

%description -n lirc-drv-iguanair
lirc plugin providing full support for the iguanaIR userspace driver,
the same as was built in into the lirc releases up to 0.9.3.
%endif


%prep
%setup -q -n %{name}-%{version}
%setup -q -T -D -a 6
%patch -P1 -p3
%patch -P2 -p1
%patch -P3 -p1
cp %{SOURCE3} README.fedora
cd iguanair-lirc-%{commit6}
patch -p1 < %{SOURCE10}
patch -p1 < %{SOURCE11}
patch -p1 < %{SOURCE12}
git apply --whitespace=fix %{SOURCE13}
dos2unix Makefile
patch -l -p2 --fuzz 2 < %{SOURCE20}
cd ..
patch  -p1 --fuzz 2 < %{SOURCE21}



%build
./runCmake -DLIBDIR="%{_libdir}"
cd build
make CFLAGS="%{optflags} -fpic -DFEDORA=1 -DHAVE_KERNEL_LIRC_H=1 -I.." %{?_smp_mflags}
cp %{SOURCE4} .


%install
%if 0%{fedora} > 23
cd iguanair-lirc-%{commit6}
PLUGINDOCS=$(pkg-config --variable=plugindocs lirc-driver)
make LDFLAGS="-liguanaIR -L../build" CFLAGS="%{optflags} \
    -fpic -I.. -DHAVE_KERNEL_LIRC_H=1 -DPLUGINDOCS=\\\"$PLUGINDOCS\\\"" \
    DESTDIR=$RPM_BUILD_ROOT install
cd ..
%endif


mkdir -p $RPM_BUILD_ROOT/%{_datadir} || :
cp -ar files/python/usr/share/iguanaIR-reflasher $RPM_BUILD_ROOT/%{_datadir}
mkdir -p $RPM_BUILD_ROOT/%{_bindir} || :
cp -ar files/python/usr/bin/* $RPM_BUILD_ROOT/%{_bindir}

cd build
make install PREFIX=$RPM_BUILD_ROOT/usr DESTDIR=$RPM_BUILD_ROOT \
    INLIBDIR=$RPM_BUILD_ROOT%{_libdir}
rm -rf $RPM_BUILD_ROOT/%{_libdir}/python%{python_version}/site-packages

install -m755 -d $RPM_BUILD_ROOT%{_localstatedir}/run/%{name}

%if 0%{fedora} > 30
rm -rf $RPM_BUILD_ROOT/%{_libdir}/python2.7/site-packages
%endif

# fix missing links
pushd  $RPM_BUILD_ROOT%{_libdir}
rm libiguanaIR.so.0.3
mv libiguanaIR.so.0 libiguanaIR.so.0.3
ln -sf libiguanaIR.so.0.3 libiguanaIR.so.0

# Use /etc/sysconfig instead of /etc/default
mkdir $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig || :
mv  $RPM_BUILD_ROOT/etc/default/iguanaIR \
    $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig

# Fix up some stray file permissions issues
         chmod a-x $RPM_BUILD_ROOT%{_includedir}/%{name}.h \
         $RPM_BUILD_ROOT%{_datadir}/%{name}-reflasher/hex/*

# Remove the installed initfile and install the systemd support instead.
rm -rf $RPM_BUILD_ROOT%{_sysconfdir}/init.d/
install -m644 -D %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/%{name}.service
install -m755 -D %{SOURCE2} $RPM_BUILD_ROOT%{_libexecdir}/iguanaIR/rescan

# Install private log dir, tmpfiles.d setup.
install -m755 -d $RPM_BUILD_ROOT%{_localstatedir}/log/iguanaIR

install -m755 -d $RPM_BUILD_ROOT/%{_tmpfilesdir}
cat > $RPM_BUILD_ROOT/%{_tmpfilesdir}/%{name}.conf <<EOF
d   /run/%{name}    0755    iguanair   iguanair
EOF
install -m 755 -d $RPM_BUILD_ROOT/run/%{name}
install -m 644 -D %{SOURCE5} $RPM_BUILD_ROOT/etc/logrotate.d/%{name}


%pre
getent group iguanair >/dev/null || groupadd -r iguanair
getent passwd iguanair >/dev/null || \
    useradd -r -g iguanair -d %{_localstatedir}/run/%{name} -s /sbin/nologin \
    -c "Iguanaworks IR Daemon" iguanair
exit 0

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service


%files
%license LICENSE LICENSE-LGPL
%doc README.txt WHY ChangeLog AUTHORS
%doc README.fedora
%{_bindir}/igdaemon
%{_bindir}/igclient
%{_bindir}/iguanaIR-rescan
%{_libdir}/lib%{name}.so.*
%{_libdir}/%{name}/*.so
%{_libexecdir}/%{name}/
%{_unitdir}/%{name}.service
%config(noreplace) /etc/logrotate.d/%{name}
/lib/udev/rules.d/80-%{name}.rules
%config(noreplace) /etc/sysconfig/%{name}
%{_tmpfilesdir}/%{name}.conf
%ghost %attr(755, iguanair, iguanair) /run/%{name}
%attr(775, iguanair, iguanair) %{_localstatedir}/log/%{name}

%if 0%{fedora} < 30
%{_libdir}/python2.7/*
%endif

%files devel
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so

%files reflasher
%{_datadir}/%{name}-reflasher/
%{_bindir}/%{name}-reflasher

%if 0%{fedora} > 23
%files -n lirc-drv-iguanair
%config /etc/modprobe.d/60-blacklist-kernel-iguanair.conf
%{_libdir}/lirc/plugins/iguanair.so
%{_docdir}/lirc/plugindocs/iguanair.html
%{_datadir}/lirc/configs/iguanair.conf
%endif


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.1.0-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 2:1.1.0-41
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.1.0-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.1.0-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.1.0-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.1.0-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.1.0-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.1.0-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.1.0-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.1.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2:1.1.0-32
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.1.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.1.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.1.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 22 2019 Alec Leamas <leamas.alec@gmail.com> - 2:1.1.0-28
- Move to python3 (Closes: #1737981).
- Drop the SWIG-generated python bindings.
- Update ancient systemd scriptlets.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.1.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.1.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.1.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.1.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.1.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.1.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.1.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Alec Leamas <leamas.alec@gmail.com> - 2:1.1.0-20
- Fix bad linkage for dynamic lirc-drv-iguanair module.

* Wed Jan 25 2017 Alec Leamas <leamas.alec@gmail.com> - 2:1.1.0-19
- -18 was a COPR release only.
- Drop the python package which does not compile cleanly any more.
- Add lirc plugin generation.
- Fix %%license usage for license files - #1413263.
- Use %%tmpfilesdir as required - #1413263.
- Remove horrible hacks from -10 to break circular dep lirc <=> iguanaIR.
- Filter away plugin deps - they only depend on ABI.
- Fix so-file links - #1409065

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:1.1.0-17
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:1.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Dec 22 2014  Alec Leamas <leamas.alec@gmail.com> - 2:1.1.0-14
- Fixing #1176627: Update logrotate conf.

* Thu Dec 11 2014 Alec Leamas <leamas.alec@gmail.com> - 2:1.1.0-13
- Filter away bogus, patched so-name from Requires:

* Wed Dec 10 2014 Alec Leamas <leamas.alec@gmail.com> - 2:1.1.0-12
- Fixes #1159618.
- Re-install logrotate file, mysteriously dropped sometime.

* Wed Sep 10 2014  Alec Leamas <leamas.alec@nowhere.net> - 2:1.1.0-11
- Fixed 64-bit provides tweak.

* Tue Sep 09 2014  Alec Leamas <leamas.alec@nowhere.net> - 2:1.1.0-10
- Added 64-bit provides tweak.

* Wed Sep 03 2014 Alec Leamas <leamas.alec@nowhere.net> - 2:1.1.0-9
- Remove needless and circular dependency on lirc.

* Wed Sep 03 2014 Alec Leamas <leamas.alec@nowhere.net> - 2:1.1.0-8
- patch soname + add virtual compatibility Provides:

* Wed Sep 3 2014 Alec Leamas <leamas.alec@nowhere.net - 2:1.1.0-7
- Patch soname on rawhide to avoid unintended bump.

* Tue Sep 2 2014 Alec Leamas <leamas.alec@nowhere.net - 2:1.1.0-6
- Make a new try to sort out deps for 1.1.0

* Wed Aug 27 2014 Alec Leamas <leamas.alec@nowhere.net - 2:1.0.5-7
- Have to re-add sources as well.

* Wed Aug 27 2014 Alec Leamas <leamas.alec@nowhere.net - 2:1.0.5-6
- Backing out 1.1.0 again, broken dependencies problem

* Thu Aug 21 2014 Alec Leamas <leamas.alec@nowhere.net - 1:1.1.0-5
- Fixing typo, bad %%{epoch} requires:

* Thu Aug 21 2014 Alec Leamas <leamas.alec@nowhere.net> - 1:1.1.0-4
- New attempt to introduce 1.1.0 (ABI bump)

* Wed Aug 20 2014 Alec Leamas <leamas.alec@nowhere.net> - 1:1.0.5-5
- Updating dependencies with epoch (sigh...).

* Tue Aug 19 2014 Alec Leamas <leamas.alec@nowhere.net> - 1:1.0.5-4
- Backing out 1.1.0 due to ABI problems.
- Purged old changelog dating to 2006, partly outside Fedora.

* Mon Aug 18 2014 Alec Leamas <leamas.alec@gmail.com> - 1.1.0-3
- Add missing patch (how did this ever build?).

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Aug 11 2014 Alec Leamas <leamas.alec@gmail.com> - 1.1.0-1
- Updating to latest version
- Old patches now upstreamed, new patches for cmake required. LIBDIR handling
  needs cleanup (not required part in rpath.patch).

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Apr 21 2013 Alec Leamas <leamas.alec@gmail.com> - 1.0.5-1
- Update to latest upstream 1.0.5
- Most patches merged upstream.

* Tue Dec 25 2012 Alec Leamas <leamas.alec@gmail.com> - 1.0.3-1
- Updated to 1.0.3
- Moved most of fixes.patch to spec file, split rest to smaller ones.
- Support sysconfig configuration file.
- Include documentation files
- Install udev rule in /lib/udev, not /etc/udev.
- Fixed udev issue invoking '/etc/init.d/iguanaIR rescan'.

* Wed Apr 18 2012 Jason L Tibbitts III <tibbs@math.uh.edu> - 1.0.1-3
- Some systemd and dependency filtering suggestions.

* Fri Jan 28 2011 Jarod Wilson <jarod@redhat.com> 1.0.1-2
- Address Fedora package review concerns (#642773)

* Thu Jan 20 2011 Jarod Wilson <jarod@redhat.com> 1.0.1-1
- Update to 1.0.1 release

* Wed Oct 13 2010 Jarod Wilson <jarod@redhat.com> 1.0-0.2.pre2.svn1419
- Update to 1.0pre2 snapshot plus svn rev 1419 additions
- Patch in additional changes to use more suitable locations for
  plugins, socket directory and reflasher files

* Wed Jul 21 2010 Jarod Wilson <jarod@redhat.com> 1.0-0.1.pre2
- Update to 1.0pre2 snapshot
- Revamp spec to be more compliant with Fedora packaging guidelines
