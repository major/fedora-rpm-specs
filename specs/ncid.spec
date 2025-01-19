Name:       ncid
Version:    1.17
Release:    6%{?dist}
Summary:    Network Caller ID server, client and gateways
Requires:   logrotate
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:    GPL-3.0-or-later
Url:        http://ncid.sourceforge.net
Source0:    https://sourceforge.net/projects/ncid/files/%{name}/%{version}/%{name}-%{version}-src.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
%if !%{defined fc40} && !%{defined fc41}
ExcludeArch:   %{ix86}
%endif

BuildRequires: make, gcc, gcc-c++
BuildRequires: libpcap-devel, pcre2-devel, libappstream-glib
BuildRequires: libphonenumber-devel, libicu-devel, protobuf-devel hidapi-devel
BuildRequires: perl-generators, perl-podlators
%{?systemd_requires}
BuildRequires: systemd

# Disable debuginfo, a stripped upstream binary is packaged.
%global debug_package %{nil}

%description
NCID is Caller ID (CID) distributed over a network to a variety of
devices and computers.  NCID includes a server, gateways, a client,
client output modules and command line tools.

The NCID server obtains the Caller ID information from a modem,
a serial or USB device and from gateways: NCID, OBI, SIP, WC, YAC and XDMF.

This package contains the server and command line tools.
The gateways are in the ncid-gateways package.
The client and default modules are in the ncid-client package.

%package gateways
Summary:    NCID (Network Caller ID) gateways
Requires:   libpcap%{?_isa} >= 1.5.0, nc, hidapi

%description gateways
NCID is Caller ID (CID) distributed over a network to a variety of
devices and computers.  NCID includes a server, gateways, a client,
client output modules and command line tools.

This package contains the NCID gateways.

%package client
Summary:    NCID (Network Caller ID) client
BuildArch:  noarch
Requires:   tcl, tk >= 8.6.8, mailx, nmap-ncat, bwidget, python3, python3-phonenumbers

%description client
The NCID client obtains the Caller ID from the NCID server and normally
displays it in a GUI window.  It can also display the Called ID in a
terminal window or, using an output module, format the output and send it
to another program.

This package contains the NCID client and output modules that are not
separate packages.

%package kpopup
Summary:    NCID kpopup module displays Caller ID info in a KDE window
BuildArch:  noarch
Requires:   %{name}-client = %{version}-%{release}
Requires:   %{name}-speak = %{version}-%{release}
Requires:   kde-baseapps, kmix

%description kpopup
The NCID kpopup module displays Caller ID information in a KDE pop-up window
and optionally speaks the number via voice synthesis.  The KDE or Gnome
desktop must be running.

%package mysql
Summary:    NCID mysql module inputs Caller ID information into a SQL database
BuildArch:  noarch
Requires:   %{name}-client = %{version}-%{release}, mysql

%description mysql
The NCID mysql module inputs NCID Caller information into a SQL database
using either MariaDB or a MySQL database.

%package mythtv
Summary:    NCID mythtv module sends Caller ID information to MythTV
BuildArch:  noarch
Requires:   %{name}-client = %{version}-%{release}
Recommends: mythtv-frontend

%description mythtv
The NCID MythTV module displays Caller ID information using mythutil

%package samba
Summary:    NCID samba module sends Caller ID information to windows machines
BuildArch:  noarch
Requires:   %{name}-client = %{version}-%{release}, samba-client

%description samba
The NCID samba module sends Caller ID information to a windows machine
as a pop-up.  This will not work if the messenger service is disabled.

%package speak
Summary:    NCID speak module speaks Caller ID information via voice synthesis
BuildArch:  noarch
Requires:   %{name}-client = %{version}-%{release}, festival

%description speak
The NCID speak module announces Caller Id information verbally, using
the Festival text-to-speech voice synthesis system.

%prep

%autosetup -n %{name}

%build
make %{?_smp_mflags} EXTRA_CFLAGS="$RPM_OPT_FLAGS" libdir libcdir
make %{?_smp_mflags} EXTRA_CFLAGS="$RPM_OPT_FLAGS" \
     LOCKFILE=/var/lock/lockdev/LCK.. \
     TTYPORT=/dev/ttyACM0 \
     STRIP= prefix=%{_prefix} prefix2= prefix3= package systemddir

%install
make install-fedora prefix=%{buildroot}/%{_prefix} \
                            prefix2=%{buildroot} \
                            prefix3=%{buildroot}
# uncomment if building a debuginfo package
# rm -f %{buildroot}/etc/ncid/*.conf.new

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/ncid.metainfo.xml

%files
%defattr(-,root,root)
%doc README VERSION doc/README-docdir
%doc doc/NCID-UserManual.md doc/NCID-API.md doc/ReleaseNotes.md doc/images
%doc man/README-mandir Fedora/README-Fedora server/README-server
%doc attic/README-attic extensions/README-extensions logrotate/README-logrotate
%doc tools/README-tools lib/README-lib udev/README-udev
%license doc/GPL.md
%{_docdir}/ncid/recordings/README-recordings
%{_docdir}/ncid/recordings/*.pvf
%{_bindir}/cidcall
%{_bindir}/cidalias
%{_bindir}/cidupdate
%{_bindir}/ncid-setup
%{_bindir}/ncidutil
%{_bindir}/ncidnumberinfo
%{_bindir}/update-cidcall
%{_sbindir}/ncidd
%dir %{_libdir}/ncid
%dir %{_datadir}/ncid
%dir %{_datadir}/ncid/sys
%dir %{_datadir}/ncid/recordings
%dir %{_datadir}/ncid/extensions
%dir %{_datadir}/ncid/plugins
%{_libdir}/ncid/libcarrier.so.8.12
%{_libdir}/ncid/libcarrier.so.8
%{_libdir}/ncid/libcarrier.so
%{_datadir}/ncid/sys/ncidrotate
%{_datadir}/ncid/sys/get-areacodes-list
%{_datadir}/ncid/sys/get-fcc-list
%{_datadir}/ncid/sys/ncid-yearlog
%{_datadir}/ncid/sys/udev-action
%{_datadir}/ncid/sys/udev-name
%{_datadir}/ncid/recordings/Callback.rmd
%{_datadir}/ncid/recordings/CallingDeposit.rmd
%{_datadir}/ncid/recordings/CannotBeCompleted.rmd
%{_datadir}/ncid/recordings/DidNotGoThrough.rmd
%{_datadir}/ncid/recordings/DisconnectedNotInService.rmd
%{_datadir}/ncid/recordings/NotInService.rmd
%{_datadir}/ncid/extensions/hangup-calls
%{_datadir}/ncid/extensions/hangup-closed-skel
%{_datadir}/ncid/extensions/hangup-combo
%{_datadir}/ncid/extensions/hangup-fakenum
%{_datadir}/ncid/extensions/hangup-fcc
%{_datadir}/ncid/extensions/hangup-greylist
%{_datadir}/ncid/extensions/hangup-message-skel
%{_datadir}/ncid/extensions/hangup-nohangup
%{_datadir}/ncid/extensions/hangup-skel
%{_datadir}/ncid/extensions/hangup-postal-code
%{_datadir}/ncid/plugins/message_dialog
%{_datadir}/ncid/plugins/us_number_info
%{_datadir}/ncid/plugins/display_ncid_variables
%dir %{_sysconfdir}/ncid
%config(noreplace) %{_sysconfdir}/ncid/hangup-combo.conf
%config(noreplace) %{_sysconfdir}/ncid/postal-codes
%config(noreplace) %{_sysconfdir}/ncid/ncidd.blacklist
%config(noreplace) %{_sysconfdir}/ncid/ncidd.whitelist
%config(noreplace) %{_sysconfdir}/ncid/modem2.conf
%config(noreplace) %{_sysconfdir}/ncid/modem3.conf
%config(noreplace) %{_sysconfdir}/ncid/modem4.conf
%config(noreplace) %{_sysconfdir}/ncid/modem5.conf
%config(noreplace) %{_sysconfdir}/ncid/ncidd.conf
%config(noreplace) %{_sysconfdir}/ncid/ncidd.alias
%config(noreplace) %{_sysconfdir}/ncid/ncidrotate.conf
%config(noreplace) %{_sysconfdir}/ncid/rotatebysize.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/ncid
%{_unitdir}/ncidd.service
%{_usr}/lib/udev/rules.d/*.rules
%{_mandir}/man1/cidalias.1*
%{_mandir}/man1/cidcall.1*
%{_mandir}/man1/cidupdate.1*
%{_mandir}/man1/ncidnumberinfo.1*
%{_mandir}/man1/update-cidcall.1*
%{_mandir}/man1/get-areacodes-list.1*
%{_mandir}/man1/get-fcc-list.1*
%{_mandir}/man1/hangup-calls.1*
%{_mandir}/man1/hangup-closed-skel.1*
%{_mandir}/man1/hangup-combo.1*
%{_mandir}/man1/hangup-fakenum.1*
%{_mandir}/man1/hangup-fcc.1*
%{_mandir}/man1/hangup-greylist.1*
%{_mandir}/man1/hangup-message-skel.1*
%{_mandir}/man1/hangup-nohangup.1*
%{_mandir}/man1/hangup-postal-code.1*
%{_mandir}/man1/hangup-skel.1*
%{_mandir}/man1/ncid-setup.1*
%{_mandir}/man1/ncid-yearlog.1*
%{_mandir}/man1/ncidutil.1*
%{_mandir}/man1/ncidrotate.1*
%{_mandir}/man5/ncidd.alias.5*
%{_mandir}/man5/ncidd.conf.5*
%{_mandir}/man5/ncidd.greylist.5*
%{_mandir}/man5/ncidd.blacklist.5*
%{_mandir}/man5/ncidd.whitelist.5*
%{_mandir}/man5/ncidrotate.conf.5*
%{_mandir}/man5/rotatebysize.conf.5*
%{_mandir}/man7/ncid_extensions.7*
%{_mandir}/man7/ncid_modems.7*
%{_mandir}/man7/ncid_plugins.7*
%{_mandir}/man7/ncid_recordings.7*
%{_mandir}/man7/ncid_tools.7*
%{_mandir}/man8/ncidd.8*

%files gateways
%defattr(-,root,root)
%doc README VERSION doc/GPL.md gateway/README-gateways
%{_sbindir}/artech2ncid
%{_sbindir}/cideasy2ncid
%{_bindir}/email2ncid
%{_bindir}/ncid2ncid
%{_bindir}/obi2ncid
%{_bindir}/rn2ncid
%{_bindir}/wc2ncid
%{_bindir}/wct
%{_bindir}/xdmf2ncid
%{_bindir}/yac2ncid
%{_sbindir}/sip2ncid
%dir %{_datadir}/ncid/setup
%{_datadir}/ncid/setup/ncid-email2ncid-setup
%config(noreplace) %{_sysconfdir}/ncid/artech2ncid.conf
%config(noreplace) %{_sysconfdir}/ncid/cideasy2ncid.conf
%config(noreplace) %{_sysconfdir}/ncid/email2ncid.conf
%config(noreplace) %{_sysconfdir}/ncid/ncid2ncid.conf
%config(noreplace) %{_sysconfdir}/ncid/obi2ncid.conf
%config(noreplace) %{_sysconfdir}/ncid/rn2ncid.conf
%config(noreplace) %{_sysconfdir}/ncid/sip2ncid.conf
%config(noreplace) %{_sysconfdir}/ncid/wc2ncid.conf
%config(noreplace) %{_sysconfdir}/ncid/xdmf2ncid.conf
%config(noreplace) %{_sysconfdir}/ncid/yac2ncid.conf
%{_unitdir}/artech2ncid.service
%{_unitdir}/cideasy2ncid.service
%{_unitdir}/ncid2ncid.service
%{_unitdir}/obi2ncid.service
%{_unitdir}/rn2ncid.service
%{_unitdir}/sip2ncid.service
%{_unitdir}/wc2ncid.service
%{_unitdir}/xdmf2ncid.service
%{_unitdir}/yac2ncid.service
%{_mandir}/man1/artech2ncid.1*
%{_mandir}/man1/cideasy2ncid.1*
%{_mandir}/man1/email2ncid.1*
%{_mandir}/man1/ncid2ncid.1*
%{_mandir}/man1/obi2ncid.1*
%{_mandir}/man1/rn2ncid.1*
%{_mandir}/man1/wc2ncid.1*
%{_mandir}/man1/wct.1*
%{_mandir}/man1/xdmf2ncid.1*
%{_mandir}/man1/yac2ncid.1*
%{_mandir}/man1/ncid-email2ncid-setup.1*
%{_mandir}/man5/artech2ncid.conf.5*
%{_mandir}/man5/cideasy2ncid.conf.5*
%{_mandir}/man5/email2ncid.conf.5*
%{_mandir}/man5/ncid2ncid.conf.5*
%{_mandir}/man5/obi2ncid.conf.5*
%{_mandir}/man5/rn2ncid.conf.5*
%{_mandir}/man5/sip2ncid.conf.5*
%{_mandir}/man5/wc2ncid.conf.5*
%{_mandir}/man5/xdmf2ncid.conf.5*
%{_mandir}/man5/yac2ncid.conf.5*
%{_mandir}/man7/ncid_gateways.7*
%{_mandir}/man8/sip2ncid.8*

%files client
%defattr(-,root,root)
%doc README VERSION client/README-client modules/README-modules
%doc icons/README-icons locales/README-locales
%doc doc/GPL.md doc/README-docdir desktop/README-desktop
%{_bindir}/ncid
%{_bindir}/phonetz
%dir %{_datadir}/ncid
%dir %{_datadir}/ncid/modules
%dir %{_datadir}/ncid/images
%dir %{_datadir}/ncid/msgs
%{_datadir}/ncid/lib
%{_datadir}/ncid/icons/flags
%{_datadir}/ncid/icons/phones
%{_datadir}/ncid/modules/ncid-alert
%{_datadir}/ncid/modules/ncid-initmodem
%{_datadir}/ncid/modules/ncid-notify
%{_datadir}/ncid/modules/ncid-page
%{_datadir}/ncid/modules/ncid-skel
%{_datadir}/ncid/modules/ncid-wakeup
%{_datadir}/ncid/modules/ncid-yac
%{_datadir}/ncid/images/logo.png
%{_datadir}/ncid/msgs/de_de.msg
%{_datadir}/ncid/msgs/fr_fr.msg
%{_datadir}/ncid/msgs/ja_jp.msg
%{_datadir}/applications/ncid.desktop
%{_metainfodir}/ncid.metainfo.xml
%{_datadir}/icons/hicolor/128x128/apps/ncid.png
%{_datadir}/icons/hicolor/96x96/apps/ncid.png
%{_datadir}/icons/hicolor/72x72/apps/ncid.png
%{_datadir}/icons/hicolor/64x64/apps/ncid.png
%{_datadir}/icons/hicolor/48x48/apps/ncid.png
%{_datadir}/icons/hicolor/32x32/apps/ncid.png
%{_datadir}/icons/hicolor/24x24/apps/ncid.png
%{_datadir}/icons/hicolor/22x22/apps/ncid.png
%{_datadir}/icons/hicolor/16x16/apps/ncid.png
%dir %{_sysconfdir}/ncid
%dir %{_sysconfdir}/ncid/conf.d
%config(noreplace) %{_sysconfdir}/ncid/ncid.conf
%config(noreplace) %{_sysconfdir}/ncid/conf.d/ncid-alert.conf
%config(noreplace) %{_sysconfdir}/ncid/conf.d/ncid-notify.conf
%config(noreplace) %{_sysconfdir}/ncid/conf.d/ncid-page.conf
%config(noreplace) %{_sysconfdir}/ncid/conf.d/ncid-skel.conf
%config(noreplace) %{_sysconfdir}/ncid/conf.d/ncid-yac.conf
%{_unitdir}/ncid-initmodem.service
%{_unitdir}/ncid-notify.service
%{_unitdir}/ncid-page.service
%{_unitdir}/ncid-yac.service
%{_mandir}/man1/phonetz.1*
%{_mandir}/man1/ncid.1*
%{_mandir}/man1/ncid-alert.1*
%{_mandir}/man1/ncid-initmodem.1*
%{_mandir}/man1/ncid-notify.1*
%{_mandir}/man1/ncid-page.1*
%{_mandir}/man1/ncid-skel.1*
%{_mandir}/man1/ncid-wakeup.1*
%{_mandir}/man1/ncid-yac.1*
%{_mandir}/man5/ncid.conf.5*
%{_mandir}/man7/ncid_modules.7*

%files kpopup
%defattr(-,root,root)
%doc VERSION modules/README-modules
%{_datadir}/ncid/modules/ncid-kpopup
%config(noreplace) %{_sysconfdir}/ncid/conf.d/ncid-kpopup.conf
%{_mandir}/man1/ncid-kpopup.1*

%files mysql
%defattr(-,root,root)
%doc VERSION modules/README-modules setup/README-setup
%{_datadir}/ncid/modules/ncid-mysql
%{_datadir}/ncid/setup/ncid-mysql-setup
%config(noreplace) %{_sysconfdir}/ncid/conf.d/ncid-mysql.conf
%{_unitdir}/ncid-mysql.service
%{_mandir}/man1/ncid-mysql.1*
%{_mandir}/man8/ncid-mysql-setup.8*

%files mythtv
%defattr(-,root,root)
%doc VERSION modules/README-modules
%{_datadir}/ncid/modules/ncid-mythtv
%config(noreplace) %{_sysconfdir}/ncid/conf.d/ncid-mythtv.conf
%{_unitdir}/ncid-mythtv.service
%{_mandir}/man1/ncid-mythtv.1*

%files samba
%defattr(-,root,root)
%doc VERSION modules/README-modules
%{_datadir}/ncid/modules/ncid-samba
%config(noreplace) %{_sysconfdir}/ncid/conf.d/ncid-samba.conf
%{_unitdir}/ncid-samba.service
%{_mandir}/man1/ncid-samba.1*

%files speak
%defattr(-,root,root)
%doc VERSION modules/README-modules
%{_datadir}/ncid/modules/ncid-speak
%config(noreplace) %{_sysconfdir}/ncid/conf.d/ncid-speak.conf
%{_unitdir}/ncid-speak.service
%{_mandir}/man1/ncid-speak.1*

%post
%systemd_post ncidd.service

%post gateways
%systemd_post artech2ncid.service cideasy2ncid ncid2ncid.service obi2ncid.service rn2ncid.service sip2ncid.service wc2ncid.service xdmf2ncid.service yac2ncid.service

%post client
%systemd_post ncid-initmodem.service ncid-notify.service ncid-page.service ncid-yac.service

%post mythtv
%systemd_post ncid-mythtv.service

%post mysql
%systemd_post ncid-mysql.service

%post samba
%systemd_post ncid-samba.service

%post speak
%systemd_post ncid-speak.service

%preun
%systemd_preun ncidd.service ncid2ncid.service sip2ncid.service yac2ncid.service obi2ncid.service rn2ncid.service wc2ncid.service

%preun client
# stop all modules even from other packages
%systemd_preun ncid-alert ncid-initmodem.service ncid-mysql.service ncid-mythtv.service ncid-notify.service ncid-page.service ncid-samba.service ncid-speak.service ncid-yac.service
# stop ncid GUI client and any user started modules
if [ $1 -eq 0 ] ; then
    pkill -f 'wish.*ncid ' || true
    pkill -f 'tclsh.*ncid-' || true
fi

%preun mysql
%systemd_preun ncid-mysql.service

%preun mythtv
%systemd_preun ncid-mythtv.service

%preun samba
%systemd_preun ncid-samba.service

%preun speak
%systemd_preun ncid-speak.service

%postun
if [ $1 -ne 0 ]; then
    ### upgrade package ###
    # move any user recordings to recordings directory
    for RECORDING in %{_datadir}/ncid/*.rmd
    do
        test -f $RECORDING && mv $RECORDING %{_datadir}/ncid/recordings || :
    done

    gtk-update-icon-cache /usr/share/icons/hicolor &>/dev/null || :
fi
%systemd_postun_with_restart ncidd.service

%postun gateways
%systemd_postun_with_restart ncid2ncid.service obi2ncid.service rn2ncid.service sip2ncid.service wc2ncid.service xdmf2ncid.service yac2ncid.service

%postun client
if [ $1 -ge 1 ]; then ### upgrade package ###
    # move any modules found to the modules directory
    for MODULE in %{_datadir}/ncid/ncid-*
    do
        test -f $MODULE && mv $MODULE %{_datadir}/ncid/modules
    done
fi
# a module service could have been installed by another package
%systemd_postun_with_restart %{_datadir}/ncid/modules/ncid-*

%postun mysql
%systemd_postun_with_restart ncid-mysql.service

%postun mythtv
%systemd_postun_with_restart ncid-mythtv.service

%postun samba
%systemd_postun_with_restart ncid-samba.service

%postun speak
%systemd_postun_with_restart ncid-speak.service

%posttrans client
# Icon Cache
touch --no-create %{_datadir}/icons/hicolor &>/dev/null
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Dec 16 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 1.17-5
- Drop i686 support beginning with Fedora 42 (leaf package)

* Sat Dec 14 2024 Adam Williamson <awilliam@redhat.com> - 1.17-4
- Rebuild for new libphonenumber

* Tue Dec 3 2024 <jlc@users.sourceforge.net> 1.17-1
- updated for new upstream release

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.16-3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Apr 12 2024 <jlc@users.sourceforge.net> 1.16-1
- updated for new upstream release

* Thu Feb 01 2024 Pete Walter <pwalter@fedoraproject.org> - 1.15-5
- Rebuild for ICU 74

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Oct 3 2023 John Chmielewski <jlc@users.sourceforge.net> 1.15-1
- updated for new upstream release

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 František Zatloukal <fzatlouk@redhat.com> - 1.14-3
- Rebuilt for ICU 73.2

* Wed May 31 2023 John Chmielewski <jlc@users.sourceforge.net> 1.14-2
- updated for upstream release
- New upstream release

* Wed May 17 2023 Sérgio Basto <sergio@serjux.com> - 1.13-9
- Rebuild for libphonenumber-8.13.x

* Thu Apr 13 2023 Jitka Plesnikova <jplesnik@redhat.com> - 1.13-8
- Remove redundant perl dependencies

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 31 2022 Pete Walter <pwalter@fedoraproject.org> - 1.13-6
- Rebuild for ICU 72

* Mon Aug 01 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.13-5
- Rebuilt for ICU 71.1

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 3 2022 John Chmielewski <jlc@users.sourceforge.net> 1.13-3
- updated for upstream release
- New upstream release

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Aug 19 2021 John Chmielewski <jlc@users.sourceforge.net> 1.12-1
- changed net.sourceforge.ncid.desktop back to ncid.desktop
- updated for upstream release
- new upstream release

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.11-7
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 3 2020 John Chmielewski <jlc@users.sourceforge.net> 1.11-4
- added ncid-usrlocal-manpage-fixes.patch
- added logrotate dependency

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 John Chmielewski <jlc@users.sourceforge.net> 1.11-1
- added new gateway requirement: perl-Net-Pcap
- changed ncid.desktop to net.sourceforge.ncid.desktop
- changed README. files to README- files
- changed local to package in build
- removed ncid-mysql.service and ncid-mythtv.service from client systemctl_post
- new upstream release

* Fri Feb 08 2019 John Chmielewski <jlcjohn@fedoraproject.org> - 1.10.1-7
- removed ncid-mythtv.patch

* Tue Feb 05 2019 John Chmielewski <jlcjohn@fedoraproject.org> - 1.10.1-6
- added more makefiles changes in ncid-makefiles.patch
- changed README.desktop to README-desktop

* Sat Feb 02 2019 John Chmielewski <jlcjohn@fedoraproject.org> - 1.10.1-5
- added ncid-mythtv.patch

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 31 2019 John Chmielewski <jlcjohn@fedoraproject.org> - 1.10.1-3
- added ncid-makefiles.patch

* Mon Jan 28 2019 John Chmielewski <jlcjohn@fedoraproject.org> - 1.10.1-2
- Removed obsolete Group tags
- created default server modem port and lockfile
- created the ncid-gateway package
- creates the ncid-mythtv package again
- changed mythtvosd to mythutil in ncid-mythtv
- updated Source0 URL
- New upstream release.

* Fri Dec 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-2
- New upstream release.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 24 2018 Filipe Rosset <rosset.filipe@gmail.com> - 1.6-8
- spec cleanup + attempt to fix FTBFS on rawhide

* Mon Feb 26 2018 Eric Sandeen <sandeen@redhat.com> - 1.6-7
- BuildRequires: gcc

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 13 2017 Petr Pisar <ppisar@redhat.com> - 1.6-3
- perl dependency renamed to perl-interpreter
  <https://fedoraproject.org/wiki/Changes/perl_Package_to_Install_Core_Modules>

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov 25 2016 Eric Sandeen <sandeen@redhat.com> 1.6-1
- New upstream release

* Thu Apr 14 2016 Eric Sandeen <sandeen@redhat.com> 1.3-3
- Fix up systemd service files

* Thu Apr 14 2016 Eric Sandeen <sandeen@redhat.com> 1.3-2
- Tidy up specfile; match uptream more closely.

* Mon Apr 11 2016 Eric Sandeen <sandeen@redhat.com> 1.3-1
- New upstream version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.83-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.83-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.83-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.83-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.83-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.83-5
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.83-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.83-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.83-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 10 2011 Eric Sandeen <sandeen@redhat.com> 0.83-1
- New upstream version

* Tue Mar 01 2011 Eric Sandeen <sandeen@redhat.com> 0.81-1
- New upstream version

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.80-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Eric Sandeen <sandeen@redhat.com> 0.80-1
- New upstream version

* Wed Sep 29 2010 jkeating - 0.79-2
- Rebuilt for gcc bug 634757

* Wed Sep 22 2010 Eric Sandeen <sandeen@redhat.com> 0.79-1
- New upstream version

* Mon Jul 12 2010 Eric Sandeen <sandeen@redhat.com> 0.78-2
- Add doc/LICENSE to -client subpackage docs

* Mon May 17 2010 Eric Sandeen <sandeen@redhat.com> 0.78-1
- New upstream version

* Sat Apr 17 2010 Eric Sandeen <sandeen@redhat.com> 0.77-1
- New upstream version

* Tue Feb 16 2010 Eric Sandeen <sandeen@redhat.com> 0.76-1
- New upstream version

* Sat Nov 07 2009 Eric Sandeen <sandeen@redhat.com> 0.75-1
- New upstream version
- Make client subpackage noarch

* Fri Oct 09 2009 Eric Sandeen <sandeen@redhat.com> 0.74-3
- Address new review items

* Fri Sep 04 2009 Eric Sandeen <sandeen@redhat.com> 0.74-2
- Address new review items

* Wed Jul 29 2009 Eric Sandeen <sandeen@redhat.com> 0.74-1
- New upstream release.

* Sun Mar 29 2009 Eric Sandeen <sandeen@redhat.com> 0.73-2
- First Fedora build.

* Thu Mar 12 2009 John Chmielewski <jlc@users.sourceforge.net> 0.73-1
- Initial build.
