%global _hardened_build 1
%bcond_with python2

#TODO: split nut-client so it does not require python
%global nut_uid 57
%global nut_gid 57

%global cgidir  /var/www/nut-cgi-bin
%global piddir  /run/nut
%global modeldir %{_sbindir}
# powerman is retired on Fedora, therefore disable it by default
%bcond_with powerman

Summary: Network UPS Tools
Name: nut
Version: 2.8.2.1
Release: 4%{?dist}
License: GPL-2.0-or-later AND GPL-3.0-or-later
Url: https://www.networkupstools.org/
Source: https://www.networkupstools.org/source/2.8/%{name}-%{version}.tar.gz
Source4: libs.sh
Patch2: nut-2.8.0-piddir-owner.patch

#quick fix. TODO: fix it properly
Patch9: nut-2.6.5-rmpidf.patch
Patch15: nut-c99-strdup.patch

Requires(pre): shadow-utils
Requires(post): coreutils systemd
Requires(preun): systemd
Requires(postun): coreutils systemd
Recommends: nut-xml

BuildRequires: make
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: augeas-libs
BuildRequires: avahi-devel
BuildRequires: cppunit-devel
BuildRequires: dbus-glib-devel
BuildRequires: desktop-file-utils
BuildRequires: elfutils-devel
BuildRequires: fontconfig-devel
BuildRequires: freeipmi-devel
BuildRequires: freetype-devel
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: gd-devel
%if 0%{?fedora} < 39
BuildRequires: libgpiod-devel
%endif
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libtool
BuildRequires: libtool-ltdl-devel
BuildRequires: libX11-devel
BuildRequires: libXpm-devel
BuildRequires: libmodbus-devel
BuildRequires: libi2c-devel
BuildRequires: neon-devel
BuildRequires: net-snmp-devel
BuildRequires: netpbm-devel
BuildRequires: nss-devel
BuildRequires: openssl-devel
BuildRequires: pkgconfig
%if %{with powerman}
BuildRequires: powerman-devel
%endif
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: systemd-devel
BuildRequires: systemd-rpm-macros

%ifnarch s390 s390x
BuildRequires: libusb1-devel
%endif

ExcludeArch: s390 s390x

%global restart_flag %{piddir}/%{name}-restart-after-rpm-install

%description
These programs are part of a developing project to monitor the assortment
of UPSes that are found out there in the field. Many models have serial
ports of some kind that allow some form of state checking. This
capability has been harnessed where possible to allow for safe shutdowns,
live status tracking on web pages, and more.

%package client
Summary: Network UPS Tools client monitoring utilities
Requires(post): systemd
Requires(preun): systemd
Requires(pre): shadow-utils
%if %{with python2}
Requires: pygtk2, pygtk2-libglade
#only for python and gui part
%endif
#Requires:

%description client
This package includes the client utilities that are required to monitor a
ups that the client host has access to, but where the UPS is physically
attached to a different computer on the network.

%package cgi
Summary: CGI utilities for the Network UPS Tools
Requires: %{name}-client = %{version}-%{release} webserver
Requires(pre): shadow-utils

%description cgi
This package includes CGI programs for accessing UPS status via a web
browser.

%package xml
Summary: XML UPS driver for the Network UPS Tools
Requires: %{name}-client = %{version}-%{release}

%description xml
This package adds the netxml-ups driver, that allows NUT to monitor a XML
capable UPS.

%package devel
Summary: Development files for NUT Client
Requires: %{name}-client = %{version}-%{release} webserver openssl-devel

%description devel
This package contains the development header files and libraries
necessary to develop NUT client applications.

%prep
%setup -q
%patch -P 2 -p1 -b .piddir-owner
%patch -P 9 -p1 -b .rmpidf
%patch -P 15 -p1

sed -i 's|=NUT-Monitor|=nut-monitor|'  scripts/python/app/nut-monitor-py3qt5.desktop
sed -i "s|sys.argv\[0\]|'%{_datadir}/%{name}/nut-monitor/nut-monitor'|" scripts/python/app/NUT-Monitor-py3qt5.in
sed -i 's|LIBSSL_LDFLAGS|LIBSSL_LIBS|' lib/libupsclient-config.in
sed -i 's|LIBSSL_LDFLAGS|LIBSSL_LIBS|' lib/libupsclient.pc.in

# workaround for multilib conflicts - caused by patch changing modification time of scripts
find . -mtime -1 -print0 | xargs -0 touch --reference %{SOURCE0}

# fix python site packages check
sed -i 's|\(PYTHON3\?_SITE_PACKAGES=\)".*"|\1"%{python3_sitelib}"|' m4/nut_check_python.m4

%build
%if 0%{?fedora} > 38
#--without-gpio is not enough to stop it complaining about missing library
sed -i 's|with_gpio="[^"]*"|with_gpio="no"|g' configure.ac
%endif
autoreconf -i
export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
# prevent assignment of default value, it would break configure's tests
export LDFLAGS="-Wl,-z,now"
%configure \
    --with-all \
%if %{without powerman}
    --without-powerman \
%endif
    --with-libltdl \
%if (0%{?fedora} && 0%{?fedora} < 33) || 0%{?el8}
    --with-nss \
%endif
    --without-wrap \
    --with-cgi \
    --with-python=%{python3} \
    --with-python3=%{python3} \
    --without-python2 \
    --datadir=%{_datadir}/%{name} \
    --with-user=%{name} \
    --with-group=dialout \
    --with-statepath=%{piddir} \
    --with-pidpath=%{piddir} \
    --with-altpidpath=%{piddir} \
    --sysconfdir=%{_sysconfdir}/ups \
    --with-cgipath=%{cgidir} \
    --with-drvpath=%{modeldir} \
%if 0%{?fedora} > 38
    --without-gpio \
%endif
    --with-systemdsystemunitdir=%{_unitdir} \
    --with-systemdshutdowndir=/lib/systemd/system-shutdown \
    --with-pkgconfig-dir=%{_libdir}/pkgconfig \
    --disable-static \
    --with-udev-dir=%{_usr}/lib/udev \
    --libdir=%{_libdir}
#    --with-doc # does not work in 2.7.1

# for rhbz#838139 check if still needed?
sh %{SOURCE4} >>include/config.h

#remove rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build LDFLAGS="%{__global_ldflags}"

%install
mkdir -p %{buildroot}%{modeldir} \
         %{buildroot}%{_sysconfdir}/udev/rules.d \
         %{buildroot}%{_sysconfdir}/ups \
         %{buildroot}%{piddir} \
         %{buildroot}%{_localstatedir}/lib/ups \
         %{buildroot}%{_libexecdir}

%make_install

#mv %{buildroot}%{_tmpfilesdir}/nut-common.tmpfiles %{buildroot}%{_tmpfilesdir}/nut-common.conf

rm -rf %{buildroot}%{_prefix}/html
rm -f %{buildroot}%{_libdir}/*.la
rm -rf docs/man
rm -rf %{buildroot}%{_datadir}/nut/solaris-init
find docs/ -name 'Makefile*' -delete

pushd conf;
%make_install
for file in %{buildroot}%{_sysconfdir}/ups/*.sample
do
   mv $file %{buildroot}%{_sysconfdir}/ups/`basename $file .sample`
done
popd

#fix collision with virtualbox
#mv %{buildroot}/%{_usr}/lib/udev/rules.d/52-nut-usbups.rules %{buildroot}/%{_usr}/lib/udev/rules.d/62-nut-usbups.rules
mv %{buildroot}/%{_usr}/lib/udev/rules.d/52-nut-ipmipsu.rules %{buildroot}/%{_usr}/lib/udev/rules.d/62-nut-ipmipsu.rules

# fix encoding
for fe in ./docs/cables/powerware.txt
do
  iconv -f iso-8859-1 -t utf-8 <$fe >$fe.new
  touch -r $fe $fe.new
  mv -f $fe.new $fe
done

# install PyNUT
install -p -D -m 644 scripts/python/module/PyNUT.py %{buildroot}%{python3_sitelib}/PyNUT.py
# install nut-monitor
%if %{with python2}
mkdir -p %{buildroot}%{_datadir}/nut/nut-monitor/pixmaps
install -p -m 755 scripts/python/app/NUT-Monitor %{buildroot}%{_datadir}/nut/nut-monitor/nut-monitor
install -p -m 644 scripts/python/app/gui-1.3.glade %{buildroot}%{_datadir}/nut/nut-monitor
install -p -m 644 scripts/python/app/pixmaps/* %{buildroot}%{_datadir}/nut/nut-monitor/pixmaps/
install -p -D scripts/python/app/nut-monitor.png %{buildroot}%{_datadir}/pixmaps/nut-monitor.png
desktop-file-install --dir=%{buildroot}%{_datadir}/applications scripts/python/app/nut-monitor.desktop
ln -s %{_datadir}/nut/nut-monitor/nut-monitor %{buildroot}%{_bindir}/nut-monitor
%endif

# Setup permissions for pid file
touch %{buildroot}/%{piddir}/upsmon.pid
chmod 0644 %{buildroot}/%{piddir}/upsmon.pid

%pre
/usr/sbin/useradd -c "Network UPS Tools" -u %{nut_uid}  \
        -s /bin/false -r -d %{_localstatedir}/lib/ups %{name} 2> /dev/null || :
/usr/sbin/usermod -G dialout,tty %{name}

# do not let upsmon run during upgrade rhbz#916472
# phase 1: stop upsmon before upsd changes
if [ "$1" = "2" ]; then
  rm -f %restart_flag
  /bin/systemctl is-active nut-monitor.service >/dev/null 2>&1 && touch %restart_flag ||:
  /bin/systemctl stop nut-monitor.service >/dev/null 2>&1
fi


%post
%systemd_post nut-driver-enumerator.path nut-driver-enumerator.service nut-driver.target nut-server.service nut.target

%preun
%systemd_preun nut-driver-enumerator.path nut-driver-enumerator.service nut-driver.target nut-server.service nut.target

%postun
%systemd_postun_with_restart nut-driver.target nut-server.service

%pre client
/usr/sbin/useradd -c "Network UPS Tools" -u %{nut_uid} \
        -s /bin/false -r -d %{_localstatedir}/lib/ups %{name} 2> /dev/null || :
/usr/sbin/usermod -G dialout,tty %{name}

%pre cgi
/usr/sbin/useradd -c "Network UPS Tools" -u %{nut_uid} \
        -s /bin/false -r -d %{_localstatedir}/lib/ups %{name} 2> /dev/null || :
/usr/sbin/usermod -G dialout,tty %{name}

%post client
%systemd_post nut-monitor.service nut.target

%preun client
%systemd_preun nut-monitor.service nut.target

%postun client
%systemd_postun_with_restart nut-monitor.service

%posttrans
# phase 2: start upsmon again
if [ -e %restart_flag ]; then
  /bin/systemctl restart nut-monitor.service >/dev/null 2>&1 || :
  rm -f %restart_flag
else
  # maybe we did not stop it - if we reinstalled just nut-client
  /bin/systemctl try-restart nut-monitor.service >/dev/null 2>&1 || :
fi

%files
%license COPYING LICENSE-GPL2 LICENSE-GPL3
%doc ChangeLog AUTHORS MAINTAINERS README docs INSTALL NEWS
%config(noreplace) %attr(640,root,nut) %{_sysconfdir}/ups/ups.conf
%config(noreplace) %attr(640,root,nut) %{_sysconfdir}/ups/upsd.conf
%config(noreplace) %attr(640,root,nut) %{_sysconfdir}/ups/upsd.users
%attr(644,root,root) %{_usr}/lib/udev/rules.d/62-nut-usbups.rules
%attr(644,root,root) %{_usr}/lib/udev/rules.d/62-nut-ipmipsu.rules
%{modeldir}/*
%exclude %{modeldir}/netxml-ups
%{_unitdir}/nut-driver-enumerator.path
%{_unitdir}/nut-driver-enumerator.service
%{_unitdir}/nut-driver-enumerator-daemon-activator.path
%{_unitdir}/nut-driver-enumerator-daemon-activator.service
%{_unitdir}/nut-driver-enumerator-daemon.service
%{_unitdir}/nut-driver@.service
%{_unitdir}/nut-driver.target
%{_unitdir}/nut-server.service
%{_unitdir}/nut.target
%{_sbindir}/upsd
%{_bindir}/nutconf
%{_bindir}/nut-scanner
%{_libdir}/libnutscan.so.*
%{_libexecdir}/nut-driver-enumerator.sh
%{_libexecdir}/sockdebug
%{_datadir}/augeas/lenses/dist/nut*
%{_datadir}/augeas/lenses/dist/tests/test_nut.aug
%{_datadir}/%{name}/cmdvartab
%{_datadir}/%{name}/driver.list
%{_mandir}/man5/ups.conf.5.gz
%{_mandir}/man5/upsd.conf.5.gz
%{_mandir}/man5/upsd.users.5.gz

%{_mandir}/man8/nutconf.8.gz

%{_mandir}/man8/adelsystem_cbi.8.gz
%{_mandir}/man8/apc_modbus.8.gz

%{_mandir}/man8/al175.8.gz
%{_mandir}/man8/apcsmart.8.gz
%{_mandir}/man8/apcsmart-old.8.gz
%{_mandir}/man8/apcupsd-ups.8.gz
%{_mandir}/man8/asem.8.gz
%{_mandir}/man8/bcmxcp.8*
%{_mandir}/man8/bcmxcp_usb.8.gz
%{_mandir}/man8/belkin.8.gz
%{_mandir}/man8/bestfcom.8.gz
%{_mandir}/man8/belkinunv.8.gz
%{_mandir}/man8/bestfortress.8.gz
%{_mandir}/man8/bestups.8.gz
%{_mandir}/man8/bestuferrups.8.gz
%{_mandir}/man8/bicker_ser.8.gz
%{_mandir}/man8/blazer_ser.8.gz
%{_mandir}/man8/blazer_usb.8.gz
%{_mandir}/man8/clone.8.gz
%{_mandir}/man8/dummy-ups.8.gz
%{_mandir}/man8/everups.8.gz
%{_mandir}/man8/etapro.8.gz
%{_mandir}/man8/gamatronic.8.gz
%{_mandir}/man8/generic_modbus.8.gz
%{_mandir}/man8/genericups.8.gz
%if 0%{?fedora} < 39
%{_mandir}/man8/generic_gpio.8.gz
%endif
%{_mandir}/man8/hwmon_ina219.8.gz
%{_mandir}/man8/huawei-ups2000.8.gz
%{_mandir}/man8/isbmex.8.gz
%{_mandir}/man8/ivtscd.8.gz
%{_mandir}/man8/liebert.8.gz
%{_mandir}/man8/liebert-esp2.8.gz
%{_mandir}/man8/masterguard.8.gz
%{_mandir}/man8/metasys.8.gz
%{_mandir}/man8/microdowell.8.gz
%{_mandir}/man8/microsol-apc.8.gz
%{_mandir}/man8/mge-utalk.8.gz
%{_mandir}/man8/mge-shut.8.gz
%{_mandir}/man8/nutupsdrv.8.gz
%{_mandir}/man8/nutdrv_atcl_usb.8.gz
%{_mandir}/man8/nutdrv_siemens_sitop.8.gz
%{_mandir}/man8/nut-driver-enumerator.8.gz
%{_mandir}/man8/nut-ipmipsu.8.gz
%{_mandir}/man8/nut-recorder.8.gz
%{_mandir}/man8/nut-scanner.8.gz
%{_mandir}/man8/nutdrv_qx.8.gz
%{_mandir}/man8/oneac.8.gz
%{_mandir}/man8/optiups.8.gz
%{_mandir}/man8/phoenixcontact_modbus.8.gz
%{_mandir}/man8/pijuice.8.gz
%{_mandir}/man8/powercom.8.gz
%if %{with powerman}
%{_mandir}/man8/powerman-pdu.8.gz
%endif
%{_mandir}/man8/powerpanel.8.gz
%{_mandir}/man8/rhino.8.gz
%{_mandir}/man8/richcomm_usb.8.gz
%{_mandir}/man8/riello_ser.8.gz
%{_mandir}/man8/riello_usb.8.gz
%{_mandir}/man8/safenet.8.gz
%{_mandir}/man8/sms_ser.8.gz
%{_mandir}/man8/snmp-ups.8.gz
%{_mandir}/man8/solis.8*
%{_mandir}/man8/sockdebug.8.gz
%{_mandir}/man8/socomec_jbus.8.gz
%{_mandir}/man8/tripplite.8.gz
%{_mandir}/man8/tripplite_usb.8.gz
%{_mandir}/man8/tripplitesu.8.gz
%{_mandir}/man8/victronups.8.gz
%{_mandir}/man8/upscode2.8*
%{_mandir}/man8/upsd.8.gz
%{_mandir}/man8/upsdrvctl.8.gz
%{_mandir}/man8/upsdrvsvcctl.8.gz
%{_mandir}/man8/usbhid-ups.8.gz

%files client
%license COPYING LICENSE-GPL2 LICENSE-GPL3
%dir %{_sysconfdir}/ups
%config(noreplace) %attr(640,root,nut) %{_sysconfdir}/ups/nut.conf
%config(noreplace) %attr(640,root,nut) %{_sysconfdir}/ups/upsmon.conf
%config(noreplace) %attr(640,root,nut) %{_sysconfdir}/ups/upssched.conf
%{_tmpfilesdir}/nut-common-tmpfiles.conf
%dir %attr(750,nut,nut) %{_localstatedir}/lib/ups
# upsmon.pid is written as root, so root needs access for now
%dir %attr(770,root,dialout) %{piddir}
%attr(644,nut,nut) %verify(not size mtime md5) /run/%{name}/upsmon.pid
%{_bindir}/upsc
%{_bindir}/upscmd
%{_bindir}/upslog
%{_bindir}/upsrw
%{_sbindir}/upsmon
%{_sbindir}/upssched
%{_bindir}/upssched-cmd
%{_unitdir}/nut-monitor.service
# nut-monitor.service also needs nut.target
%{_unitdir}/nut.target
/lib/systemd/system-shutdown/nutshutdown
%{_libdir}/libupsclient.so.*
%{_libdir}/libnutclient.so.*
%{_libdir}/libnutclientstub.so.*
%{_mandir}/man5/nut.conf.5.gz
%{_mandir}/man5/upsmon.conf.5.gz
%{_mandir}/man5/upssched.conf.5.gz
%{_mandir}/man8/upsc.8.gz
%{_mandir}/man8/upscmd.8.gz
%{_mandir}/man8/upslog.8.gz
%{_mandir}/man8/upsrw.8.gz
%{_mandir}/man8/upsmon.8.gz
%{_mandir}/man8/upssched.8.gz
%pycached %{python3_sitelib}/PyNUT.py
%pycached %{python3_sitelib}/test_nutclient.py
%{_datadir}/nut
%if %{with python2}
%{_bindir}/nut-monitor
%{_datadir}/pixmaps/nut-monitor.png
%{_datadir}/applications/nut-monitor.desktop
%endif

%files cgi
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/ups/hosts.conf
%config(noreplace) %attr(600,nut,root) %{_sysconfdir}/ups/upsset.conf
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/ups/upsstats.html
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/ups/upsstats-single.html
%{cgidir}/
%{_mandir}/man5/hosts.conf.5.gz
%{_mandir}/man5/upsstats.html.5.gz
%{_mandir}/man5/upsset.conf.5.gz
%{_mandir}/man8/upsimage.cgi.8.gz
%{_mandir}/man8/upsstats.cgi.8.gz
%{_mandir}/man8/upsset.cgi.8.gz

%files xml
%{modeldir}/netxml-ups
%doc %{_mandir}/man8/netxml-ups.8.gz

%files devel
%{_includedir}/*
%{_mandir}/man3/upscli*
%{_mandir}/man3/nutscan*
%{_mandir}/man3/nutclient*
%{_mandir}/man3/libnutclient*
%{_libdir}/libupsclient.so
%{_libdir}/libnutclient.so
%{_libdir}/libnutclientstub.so
%{_libdir}/libnutscan.so
%{_libdir}/pkgconfig/libupsclient.pc
%{_libdir}/pkgconfig/libnutclient.pc
%{_libdir}/pkgconfig/libnutclientstub.pc
%{_libdir}/pkgconfig/libnutscan.pc

%changelog
* Wed Jan 29 2025 Michal Hlavinka <mhlavink@redhat.com> - 2.8.2.1-4
- fix ftbfs, make it build with unified bin/sbin

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2.1-3.1.git20240703pr2505
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Nov 15 2024 Orion Poplawski <orion@nwra.com> - 2.8.2.1-2.1.git20240703pr2505
- Add BR systemd-devel to enable systemd notification support

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2.1-1.1.git20240703pr2505
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 03 2024 Michal Hlavinka <mhlavink@redhat.com> - 2.8.2.1-0.1.git20240703pr2505
- fix python FTBFS, uses git snapshot as of 20240703 with PR 2505

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.8.2-2
- Rebuilt for Python 3.13

* Wed Apr 03 2024 Michal Hlavinka <mhlavink@redhat.com> - 2.8.2-1
- updated to 2.8.2(2272586)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Nov 30 2023 Orion Poplawski <orion@nwra.com> - 2.8.1-2
- Re-add nut.target to nut-client (bz#2156504)

* Wed Nov 01 2023 Michal Hlavinka <mhlavink@redhat.com> - 2.8.1-1
- updated to 2.8.1 (#2247337)

* Tue Oct 10 2023 Michal Hlavinka <mhlavink@redhat.com> - 2.8.0-14
- spec cleanup, based on PR#14 by Orion Poplawski

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.8.0-12
- Rebuilt for Python 3.12

* Wed Apr 26 2023 Michal Hlavinka <mhlavink@redhat.com> - 2.8.0-11
- update license tag format (SPDX migration) for https://fedoraproject.org/wiki/Changes/SPDX_Licenses_Phase_1

* Tue Feb 14 2023 Michal Hlavinka <mhlavink@redhat.com> - 2.8.0-10
- add nut-xml to nut recommends (#2151810)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Michal Hlavinka <mhlavink@redhat.com> - 2.8.0-8
- move upslog to nut-client, some small spec file changes (#2156504)

* Wed Nov 30 2022 Charles R. Anderson <cra@alum.wpi.edu> - 2.8.0-7
- use piddir for specifying restart_flag location
- use piddir for specifying configure --with-statepath/pidpath/altpidpath
- add nut-2.8.0-piddir-owner.patch for upstream tmpfiles config creation to not append /nut and always use owner root
- update nut-2.6.3-tmpfiles.patch to use correct tmpfiles config file name
- remove unused downstream tmpfiles source and code

* Sun Nov 27 2022 Florian Weimer <fweimer@redhat.com> - 2.8.0-6
- Port configure script to C99

* Wed Aug 31 2022 Michal Hlavinka <mhlavink@redhat.com> - 2.8.0-5
- update pid path

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.8.0-3
- Rebuilt for Python 3.11

* Tue Jun 07 2022 Michal Hlavinka <mhlavink@redhat.com> - 2.8.0-2
- drop unused solaris init script pulling unnecessary dependency

* Mon May 09 2022 Michal Hlavinka <mhlavink@redhat.com> - 2.8.0-1
- updated to 2.8.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.4-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Sep 23 2021 Miro Hrončok <mhroncok@redhat.com> - 2.7.4-43
- Don't own /usr/lib/python3.X/site-packages

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 2.7.4-42
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.4-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 08 2021 Michal Hlavinka <mhlavink@redhat.com> - 2.7.4-40
- drop snmp-ups support for DES, as required net-snmp no longer supports it

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.7.4-39
- Rebuilt for Python 3.10

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.7.4-38
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.4-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 15 2020 Jeff Law <law@redhat.com> - 2.7.4-36
- Force C++14 as this code is not C++17 ready

* Wed Sep 02 2020 Josef Ridky <jridky@redhat.com> - 2.7.4-35
- Resolves: #1865077 - FTBFS in Fedora 33
- Rebuilt for new release of net-snmp

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.4-34
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.4-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 02 2020 Michal Hlavinka <mhlavink@redhat.com> - 2.7.4-32
- nut user needs tty group for wall (#1774591)

* Tue Jun 02 2020 Michal Hlavinka <mhlavink@redhat.com> - 2.7.4-31
- update tmpfiles nut run directory

* Tue May 26 2020 Orion Poplawski <orion@nwra.com> - 2.7.4-30
- Drop old udev requires/scriptlet

* Tue May 26 2020 Orion Poplawski <orion@nwra.com> - 2.7.4-29
- Add upstream patch for OpenSSL 1.1.0 support, enable for Fedora >= 33

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.7.4-28
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.4-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 04 2019 Michal Hlavinka <mhlavink@redhat.com> - 2.7.4-26
- drop pygtk2 requirements

* Thu Oct 03 2019 Michal Hlavinka <mhlavink@redhat.com> - 2.7.4-25
- drop python 2 requirements including nut-monitor app

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 25 2019 Michal Hlavinka <mhlavink@redhat.com> - 2.7.4-23
- add missing requirements for nut monitor
- fix file descriptor leak for notifycmd

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 16 2018 Orion Poplawski <orion@nwra.com> - 2.7.4-21
- Cleanup and modernize spec
- Fix ownership/permissions of /var/run/nut (bug #1584330, #1580082)
- Fix python shbangs

* Sun Oct 14 2018 Peter Robinson <pbrobinson@fedoraproject.org> 2.7.4-20
- Updates dependencies, modernise spec, use %%license
- Python build fixes

* Tue Jul 24 2018 Adam Williamson <awilliam@redhat.com> - 2.7.4-19
- Rebuild for new net-snmp

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 17 2018 Xavier Bachelot <xavier@bachelot.org> - 2.7.4-17
- Remove unrecognized configure option --without-hal
- Explicitely disable tcpwrapper support
- Remove unneeded CRLF EOL fix
- Add BR: cppunit-devel

* Wed Mar 07 2018 Michal Hlavinka <mhlavink@redhat.com> - 2.7.4-16
- add gcc buildrequire

* Wed Feb 14 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.7.4-15
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 07 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.7.4-13
- Remove old crufty coreutils requires

* Wed Aug 30 2017 Michal Hlavinka <mhlavink@redhat.com> - 2.7.4-12
- rebuild for freeipmi update

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 22 2017 Michal Hlavinka <mhlavink@redhat.com> - 2.7.4-9
- enable nss crypto (#1463071)

* Wed May 24 2017 Michal Hlavinka <mhlavink@redhat.com> - 2.7.4-8
- fix location of tmpfiles.d in service files (#1399602)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 01 2017 Sandro Mani <manisandro@gmail.com> - 2.7.4-6
- Rebuild (libwebp)

* Fri Nov 11 2016 Michal Hlavinka <mhlavink@redhat.com> - 2.7.4-5
- use %%_tmpfilesdir macro (#1394009)

* Thu Sep 15 2016 Till Maas <opensource@till.name> - 2.7.4-4
- Disable powerman support, powerman was retired on Fedora

* Thu Aug 11 2016 Michal Hlavinka <mhlavink@redhat.com> - 2.7.4-3
- make sure tmpfiles creation is executped before ups driver (#1365904,#1349362)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.4-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sat Mar 12 2016 Michal Hlavinka <mhlavink@redhat.com> - 2.7.4-1
- nut updated to 2.7.4

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Dec 05 2015 Kalev Lember <klember@redhat.com> - 2.7.3-6
- Rebuilt for libfreeipmi soname bump

* Tue Dec  1 2015 Tom Callaway <spot@fedoraproject.org> - 2.7.3-5
- rebuild for libvpx 1.5.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.7.3-3
- Rebuilt for GCC 5 C++11 ABI change

* Tue Apr 28 2015 Michal Hlavinka <mhlavink@redhat.com> - 2.7.3-2
- start nut driver before the daemon

* Thu Apr 23 2015 Michal Hlavinka <mhlavink@redhat.com> - 2.7.3-1
- nut updated to 2.7.3

* Mon Apr  6 2015 Tom Callaway <spot@fedoraproject.org> - 2.7.2-4
- rebuild against libvpx 1.4.0

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 22 2014 Michal Hlavinka <mhlavink@redhat.com> - 2.7.2-1
- nut updated to 2.7.2

* Thu Apr 17 2014 Michal Hlavinka <mhlavink@redhat.com> - 2.7.1-4
- fix multilib issue (#831429)

* Thu Mar 06 2014 Michal Hlavinka <mhlavink@redhat.com> - 2.7.1-3
- fix path of nut-driver executable (#1072076)
- fix location of udev rules

* Thu Mar 06 2014 Michal Hlavinka <mhlavink@redhat.com> - 2.7.1-2
- fix undefined references in libupsclient (#1071919)

* Thu Feb 27 2014 Michal Hlavinka <mhlavink@redhat.com> - 2.7.1-1
- nut updated to 2.7.1

* Tue Sep 24 2013 Michal Hlavinka <mhlavink@redhat.com> - 2.6.5-16
- rebuilt with updated freeipmi (1.3.2)

* Tue Sep 03 2013 Michal Hlavinka <mhlavink@redhat.com> - 2.6.5-15
- rebuilt with updated freeipmi

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 11 2013 Remi Collet <rcollet@redhat.com> - 2.6.5-13
- rebuild for new GD 2.1.0

* Mon Apr 22 2013 Michal Hlavinka <mhlavink@redhat.com> - 2.6.5-12
- do not let upsmon run during update (#916472)
- make binaries hardened (#955157)

* Thu Feb 28 2013 Michal Hlavinka <mhlavink@redhat.com> - 2.6.5-11
- clean pid file on exit (#916468)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 2.6.5-9
- rebuild due to "jpeg8-ABI" feature drop

* Mon Jan 07 2013 Michal Hlavinka <mhlavink@redhat.com> - 2.6.5-8
- do not traceback when ups is not reachable

