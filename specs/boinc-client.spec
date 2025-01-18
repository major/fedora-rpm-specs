# ========== README ==========
#
# BOINC client is not released with Github releases, it is released using
# Github tags.
# When a new BOINC client Github tag is released, replace
# 1) Version
# 2) Release (obviously)
# 3) commit, you can take it from the URL you get on Github when you pass the
# mousepointer on shortcommit (7 chars string)
# 
# BOINC release URLs are troublesome, to download the tar.gz use the following command
# spectool -g -s 0 boinc-client.spec
#
# Do not move the %%global foo block of code in the upper part of the spec
# file, otherwise it will not work because it will try to read macros not
# yet defined like %%{version}

Summary:       The BOINC client
Name:          boinc-client
Version:       8.0.2
Release:       2%{?dist}
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:       LicenseRef-Callaway-LGPLv2+
URL:           http://boinc.berkeley.edu/

%global major_version %(v=%{version}; echo ${v:0:3})
%global commit c0b8b6fd37687aa1b93102129a054837b84cc032
%global gittag client_release/%{major_version}/%{version}
# gittag_custom is needed in %%setup process because tar.gz unpacks a folder
# named for example boinc-client_release-7.14-7.14.2
%global gittag_custom client_release-%{major_version}-%{version}
%global shortcommit %(c=%{commit}; echo ${c:0:7})


Source0:       https://github.com/BOINC/boinc/archive/%{gittag}/%{name}-%{version}.tar.gz
SOURCE1:       boinc-client-logrotate-d
SOURCE3:       36x11-common_xhost-boinc
SOURCE4:       config.properties
SOURCE5:       edu.berkeley.BOINC.metainfo.xml
%if 0%{?fedora} > 35
#Patch0:        openssl3.patch
%endif
Patch1:        disable_idle_time_detection.patch
# On Linux distributions, BOINC runs as a service. Users must not be able to
# try stopping the service from exit menu entry.
# This leads to unexpected behaviour, like:
# - service being killed;
# - service still running.
# Moreover, the Manager will no longer be able to connect to the client, unless
# the user connects to 127.0.0.1. Then if the Manager is connected to the client
# by using 127.0.0.1 address, the "Exit from BOINC Manager" entry will not
# show any frame asking the user if he wants to stop the service.
# upstream pull request https://github.com/BOINC/boinc/pull/3094 has ben merged
# and unmerged later
#Patch4:        manager_exit_menu_entry_removal.patch


Requires:         logrotate
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd
Requires(pre):    shadow-utils

BuildRequires: curl-devel
%if 0%{?el7}
BuildRequires: devtoolset-7-toolchain
BuildRequires: devtoolset-7-libatomic-devel
%endif
BuildRequires: freeglut-devel
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: gtk3-devel
BuildRequires: docbook2X
BuildRequires: libXmu-devel
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(libnotify)
BuildRequires: libtool
BuildRequires: libXScrnSaver-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: pkgconfig(openssl)
%if 0%{?fedora} > 40
# https://fedoraproject.org/wiki/Changes/OpensslDeprecateEngine
#
# We have raised the possibility of removing OpenSSL engine support upstream:
#   Remove OpenSSL engine support
#   https://github.com/BOINC/boinc/pull/5991
# However, it’s difficult to test this thoroughly, so it makes sense to wait
# for upstream feedback and/or for the next major-version update before
# patching this downstream. For now, we just add the necessary BuildRequires to
# keep supporting engines.
BuildRequires: openssl-devel-engine
%endif
%if 0%{?fedora}
BuildRequires: pkgconfig(sqlite)
%else
BuildRequires: sqlite-devel
%endif
BuildRequires: systemd-rpm-macros
BuildRequires: wxGTK-devel
BuildRequires: pkgconfig(xcb-util)
BuildRequires: pkgconfig(libunwind)
BuildRequires: make


# EPEL8 webkit2gtk3 is missing for s390x, aarch64
%if 0%{?el8}
ExcludeArch: s390x
%endif
%description 
The Berkeley Open Infrastructure for Network Computing (BOINC) is an open-
source software platform which supports distributed computing, primarily in
the form of "volunteer" computing and "desktop Grid" computing.  It is well
suited for problems which are often described as "trivially parallel".  BOINC
is the underlying software used by projects such as SETI@home, Einstein@Home,
ClimatePrediciton.net, the World Community Grid, and many other distributed
computing projects.

This package installs the BOINC client software, which will allow your
computer to participate in one or more BOINC projects, using your spare
computer time to search for cures for diseases, model protein folding, study
global warming, discover sources of gravitational waves, and many other types
of scientific and mathematical research.

%package -n boinc-manager
Summary:    GUI to control and monitor %{name}
Requires:   hicolor-icon-theme
Requires:   %{name} = %{version}-%{release}

%description -n boinc-manager
The BOINC Manager is a graphical monitor and control utility for the BOINC
core client. It gives a detailed overview of the state of the client it is
monitoring. The BOINC Manager has two modes of operation, the "Simple View" in
which it only displays the most important information and the "Advanced View"
in which all information and all control elements are available.

%package devel
Summary:    Development files for %{name}
Requires:   %{name} = %{version}-%{release}
Requires:   openssl-devel
%if 0%{?el7}
Requires:   mysql-devel
%else
Requires:   mariadb-connector-c-devel
%endif

%description devel
This package contains development files for %{name}.

%package static
Summary:    Static libraries for %{name}
Requires:   %{name}-devel = %{version}-%{release}

%description static
This package contains static libraries for %{name}.

%package doc
Summary:    Documentation files for %{name}
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}

%description doc
This package contains documentation files for %{name}.

%prep
%autosetup -p1 -n boinc-%{gittag_custom}

# Fix encoding
for file in $(ls | grep checkin_notes_20); do
    iconv -f ISO-8859-1 -t UTF-8 -o ${file}.utf8 ${file}
    mv ${file}.utf8 ${file}
done

# Fix file permissions
for file in $(ls clientgui | grep .cpp$ ) $(ls clientgui | grep .h$ ); do 
    chmod 644 clientgui/${file}
done

%build
%if 0%{?el7}
. /opt/rh/devtoolset-7/enable
%endif

%ifarch %{ix86}
%global boinc_platform i686-pc-linux-gnu
%endif
%ifarch powerpc ppc
%global boinc_platform powerpc-linux-gnu
%endif
%ifarch powerpc64 ppc64
%global boinc_platform ppc64-linux-gnu
%endif
%ifarch aarch64
%global boinc_platform aarch64-unknown-linux-gnu
%endif

%if %{defined boinc_platform}
%global confflags --with-boinc-platform=%{boinc_platform}
%endif

./_autosetup

%configure %{?confflags} \
  --disable-silent-rules \
  --enable-dynamic-client-linkage \
  --disable-server \
  --disable-fcgi \
  --enable-unicode \
  --with-wx-config=/usr/bin/wx-config-3.2 \
  --with-ssl \
  --with-x \
  STRIP=: \
  DOCBOOK2X_MAN=/usr/bin/db2x_docbook2man \
  "CXXFLAGS=$(pkg-config gtk+-x11-3.0 --cflags --libs) ${RPM_OPT_FLAGS} -DNDEBUG"

# Disable rpaths
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
mkdir -p $RPM_BUILD_ROOT%{_metainfodir}
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/boinc
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/X11/Xsession.d
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/boinc-client

make install INSTALL="%{__install} -p" DESTDIR=$RPM_BUILD_ROOT

# Set up links to correct log locations
#ln -s /var/log/boinc/ %%{_localstatedir}/log/boinc.log 
#ln -s /var/log/boinc/ %%{_localstatedir}/log/boincerr.log 

# Remove libtool archives
rm $RPM_BUILD_ROOT%{_libdir}/*.la

# Use custom systemd script and logrotate configuration file
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/init.d/%{name} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/%{name}

install -p -m644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/%{name}
install -p -m644 %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/X11/Xsession.d/36x11-common_xhost-boinc
install -p -m644 %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/boinc-client/config.properties

# Install Icons
install -p -m644 packages/generic/sea/boincmgr.16x16.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/boincmgr.png
install -p -m644 packages/generic/sea/boincmgr.32x32.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/boincmgr.png
install -p -m644 packages/generic/sea/boincmgr.48x48.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/boincmgr.png

# Install AppStream metainfo file
install -p -m644 %{SOURCE5} $RPM_BUILD_ROOT%{_metainfodir}/edu.berkeley.BOINC.metainfo.xml

%find_lang BOINC-Manager
%find_lang BOINC-Client

# bash-completion
install -p -m644 client/scripts/boinc.bash $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/boinc-client

%pre

# Create BOINC user and group
getent group boinc >/dev/null || groupadd -r boinc
getent passwd boinc >/dev/null || \
useradd -r -g boinc -d %{_localstatedir}/lib/boinc -s /sbin/nologin \
    -c "BOINC client account." boinc
exit 0

%post
%{?ldconfig}
%systemd_post boinc-client.service

%preun
%systemd_preun boinc-client.service

%postun
%{?ldconfig}
%systemd_postun_with_restart boinc-client.service  

%if 0%{?rhel} && 0%{?rhel} <= 7
%post -nboinc-manager
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun -n boinc-manager
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans -n boinc-manager
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
%endif

%files -f BOINC-Client.lang
%doc COPYING COPYRIGHT
%{_bindir}/boinc
%{_bindir}/boinc_client
%{_bindir}/boinccmd
#%{_bindir}/switcher
%{_unitdir}/%{name}.service
%{_mandir}/man1/boinccmd.1.gz
%{_mandir}/man1/boinc.1.gz
%{_libdir}/*.so.*
%config(noreplace) %{_sysconfdir}/logrotate.d/boinc-client
%config(noreplace) %{_sysconfdir}/bash_completion.d/boinc-client
%attr(-,boinc,boinc) %{_localstatedir}/lib/boinc/
%{_sysconfdir}/X11/Xsession.d/36x11-common_xhost-boinc
%{_sysconfdir}/boinc-client/config.properties


%files doc
%doc checkin_notes checkin_notes_*

%files -n boinc-manager -f BOINC-Manager.lang
%{_bindir}/boincmgr
%{_bindir}/boincscr
%{_datadir}/applications/boinc.desktop
%{_metainfodir}/edu.berkeley.BOINC.metainfo.xml
%{_datadir}/boinc-manager/skins/*
%{_datadir}/icons/hicolor/16x16/apps/boincmgr.png
%{_datadir}/icons/hicolor/32x32/apps/boincmgr.png
%{_datadir}/icons/hicolor/48x48/apps/boincmgr.png
%{_datadir}/icons/hicolor/64x64/apps/boinc.png
%{_datadir}/icons/hicolor/scalable/apps/boinc.svg
%{_mandir}/man1/boincmgr.1.gz

%files static
%{_libdir}/libboinc.a
%{_libdir}/libboinc_api.a
%{_libdir}/libboinc_crypt.a
%{_libdir}/libboinc_graphics2.a
%{_libdir}/libboinc_opencl.a

%files devel
%{_libdir}/*.so
%{_includedir}/boinc
%{_libdir}/pkgconfig/libboinc.pc
%{_libdir}/pkgconfig/libboinc_api.pc
%{_libdir}/pkgconfig/libboinc_crypt.pc
%{_libdir}/pkgconfig/libboinc_graphics2.pc
%{_libdir}/pkgconfig/libboinc_opencl.pc

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jan 10 2025 Germano Massullo <germano.massullo@gmail.com> - 8.0.2-1
- 8.0.2 release
- Erased obsolete patches

* Sun Jan 05 2025 Benjamin A. Beasley <code@musicinmybrain.net> - 7.20.2-12
- Fix FTBFS in F41+ due to OpenSSL ENGINE API deprecation; fixes RHBZ#2300580.

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 7.20.2-11
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.20.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.20.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.20.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.20.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 28 2023 Daniel Rusek <mail@asciiwolf.com> - 7.20.2-6
- Added an AppStream metainfo file

* Wed Apr 05 2023 K. de Jong <keesdejong@fedoraproject.org> - 7.20.2-5
- Removed custom boincmgr.desktop file

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.20.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Florian Weimer <fweimer@redhat.com> - 7.20.2-3
- Suppress spurious diagnostics related to C99 porting

* Thu Aug 04 2022 Scott Talbert <swt@techie.net> - 7.20.2-2
- Rebuild with wxWidgets 3.2

* Wed Jul 20 2022 Germano Massullo <germano.massullo@gmail.com> - 7.20.2-1
- 7.20.2 release

* Thu Jun 09 2022 Germano Massullo <germano.massullo@gmail.com> - 7.18.1-3
- re-enabled patches disabled in 7.18.1-1
- removed 4071.patch
- enabled devtoolset-7 for EPEL7

* Sun Apr 10 2022 Germano Massullo <germano.massullo@gmail.com> - 7.18.1-2
- added boinc-client-7.18-AC_CHECK_DECLS-change.patch

* Sat Apr 09 2022 Germano Massullo <germano.massullo@gmail.com> - 7.18.1-1
- 7.18.1 release
- added openssl3.patch for Fedora > 35
- added some pkgconfig
- added BuildRequires: systemd-rpm-macros
- temporarily disabled all patches except openssl3.patch
- added openssl3.patch

* Thu Feb 17 2022 Germano Massullo <germano.massullo@gmail.com> - 7.16.11-9
- resume aarch64 CPU architecture on EL8

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.16.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 7.16.11-7
- Rebuilt with OpenSSL 3.0.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.16.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 7.16.11-5
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.16.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 11 2020 Germano Massullo <germano.massullo@gmail.com> - 7.16.11-3
- updated 4071 patch file

* Fri Oct 30 2020 Germano Massullo <germano.massullo@gmail.com> - 7.16.11-2
- Added SOURCE4: config.properties

* Fri Oct 30 2020 Germano Massullo <germano.massullo@gmail.com> - 7.16.11-1
- 7.16.11 release
- Added 4071.patch Read https://github.com/BOINC/boinc/pull/4071
- 

* Tue Oct 06 2020 Germano Massullo <germano.massullo@gmail.com> - 7.16.6-7
-  Re-enabled ppc64 architecture on EPEL7. Read https://bugzilla.redhat.com/show_bug.cgi?id=1648290

* Fri Sep 18 2020 Germano Massullo <germano.massullo@gmail.com> - 7.16.6-6
- Renamed boinc-manager.desktop to boincmgr.desktop This fixes https://bugzilla.redhat.com/show_bug.cgi?id=1880553

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.16.6-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.16.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr 23 2020 Germano Massullo <germano.massullo@gmail.com> - 7.16.6-3
- Updated disable_idle_time_detection.patch

* Sat Apr 11 2020 Germano Massullo <germano.massullo@gmail.com> - 7.16.6-2
- Added disable_idle_time_detection.patch

* Thu Apr 09 2020 Germano Massullo <germano.massullo@gmail.com> - 7.16.1-7
- 7.16.6 release
- Removed cc_config_cpp_3249.patch
- Disabled disabled_idle_detection.patch. Read https://bugzilla.redhat.com/show_bug.cgi?id=1822723

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.16.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Germano Massullo <germano.massullo@cern.ch> - 7.16.1-5
- Added ExcludeArch: s390x, aarch64 for EPEL8

* Fri Aug 16 2019 Germano Massullo <germano.massullo@cern.ch> - 7.16.1-4
- Added cc_config_cpp_3249.patch

* Mon Aug 12 2019 Germano Massullo <germano.massullo@cern.ch> - 7.16.1-3
- Added remove_etc_boinc-client_from_systemd_unit_file.patch

* Tue Aug 06 2019 Germano Massullo <germano.massullo@cern.ch>
- replaced %%setup -q -n boinc-%%{gittag_custom} with %%autosetup -n boinc-%%{gittag_custom}

* Tue Aug 06 2019 Germano Massullo <germano.massullo@cern.ch> - 7.16.1-1
- 7.16.1 release
- Removed scheduler.patch tray_icon_removal.patch window_close.patch because they have been merged into 7.16.1

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.14.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 04 2019 Germano Massullo <germano.massullo@cern.ch> - 7.14.2-17
- Added prevent_manager_from_starting_client.patch

* Wed Mar 06 2019 Germano Massullo <germano.massullo@cern.ch> - 7.14.2-16
- Added manager_shut_down_connected_client.patch

* Wed Mar 06 2019 Germano Massullo <germano.massullo@cern.ch> - 7.14.2-15
- Added tray_icon_removal.patch

* Fri Feb 22 2019 Germano Massullo <germano.massullo@cern.ch> - 7.14.2-14
- Added manager_exit_menu_entry_removal.patch

* Wed Feb 20 2019 Germano Massullo <germano.massullo@cern.ch> - 7.14.2-13
- Added manager_close_no_service_stop.patch that prevents manager close action from stopping client service

* Tue Feb 19 2019 Kalev Lember <klember@redhat.com> - 7.14.2-12
- Rebuilt against fixed atk (#1626575)

* Tue Feb 19 2019 Germano Massullo <germano.massullo@cern.ch> - 7.14.2-11
- Added window_close.patch

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.14.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 11 2019 Germano Massullo <germano.massullo@cern.ch> - 7.14.2-9
- removed systemd_nice_removal.patch because scheduling policies and nice level in systemd unit file only affects boinc process, that should have nice=10 and a slightly more higher priority than working units. Since controller processes do not run often, the system should not be affected by them

* Thu Jan 10 2019 Germano Massullo <germano.massullo@cern.ch> - 7.14.2-8
- added systemd_nice_removal.patch

* Tue Jan 08 2019 Germano Massullo <germano.massullo@cern.ch> - 7.14.2-7
- removed added systemd_scheduler.patch since scheduler.patch is already enough to achieve boinc running in idle
- disabled systemd_hardening.patch because its tests are still in early stage on upstream development process

* Fri Dec 14 2018 Germano Massullo <germano.massullo@cern.ch> - 7.14.2-6
- added systemd_hardening.patch

* Fri Dec 14 2018 Germano Massullo <germano.massullo@cern.ch> - 7.14.2-5
- added systemd_scheduler.patch

* Wed Dec 12 2018 Germano Massullo <germano.massullo@cern.ch> - 7.14.2-4
- added scheduler.patch

* Mon Nov 12 2018 Germano Massullo <germano.massullo@cern.ch> - 7.14.2-3
- replaced hardcoded Source0
- replaced hardcoded %%setup
- adjusted macro tags for git
- added README section

* Mon Nov 12 2018 Germano Massullo <germano.massullo@cern.ch> - 7.14.2-2
- EPEL7 only: added ExcludeArch: ppc64, read https://bugzilla.redhat.com/show_bug.cgi?id=1648290

* Thu Nov 08 2018 Germano Massullo <germano.massullo@gmail.com> - 7.14.2-1
- 7.14.2 release
- Hardcoded Source0 URL, read https://bugzilla.redhat.com/show_bug.cgi?id=1647945

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.10.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Germano Massullo <germano.massullo@gmail.com> - 7.10.2-2
- Added BuildRequires: gcc-c++

* Wed May 02 2018 Laurence Field <laurence.field@cern.ch> - 7.10.2-1
- New BONC client version 7.10.2

* Wed Apr 25 2018 Laurence Field <laurence.field@cern.ch> - 7.10.1-1
- New BONC client version 7.10.1

* Fri Mar 09 2018 Laurence Field <laurence.field@cern.ch> - 7.9.3-1
- New BONC client version 7.9.3

* Fri Feb 23 2018 Germano Massullo <germano.massullo@gmail.com> - 7.9.2-3
- added macros to use mariadb-connector-c instead of mysql-* only for Fedora > 26

* Mon Feb 19 2018 Germano Massullo <germano.massullo@gmail.com> - 7.9.2-2
- Use mariadb-connector-c instead of mysql-libs or mariadb-libs. See bugreport #1494241

* Mon Feb 19 2018 Laurence Field <laurence.field@cern.ch> - 7.9.2-1
- New BONC client version 7.9.2

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.8.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb 02 2018 Germano Massullo <germano.massullo@gmail.com> - 7.8.4-4
- systemd unit file: changed from Type=forking to Type=simple and removed --daemon --start_delay 1 from ExecStart

* Mon Jan 15 2018 Germano Massullo  <germano.massullo@gmail.com> - 7.8.4-3
- Removed obsolete %%defattr(-,root,root)

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 7.8.4-2
- Remove obsolete scriptlets

* Mon Nov 13 2017 Laurence Field <laurence.field@cern.ch> - 7.8.4-1
- New BONC client version 7.8.4

* Fri Oct 13 2017 Laurence Field <laurence.field@cern.ch> - 7.8.3-1
- New BONC client version 7.8.3

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.6.33-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.6.33-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 09 2017 Germano Massullo <germano.massullo@gmail.com> - 7.6.33-3
- forced nice=19 in systemd boinc-client unit file

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.6.33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 28 2016 Germano Massullo <germano.massullo@gmail.com> - 7.6.33-1
- 7.6.33 release

* Thu Jul 21 2016 Germano Massullo <germano.massullo@gmail.com> - 7.6.22-7
- Disabled idle detection. See RedHat Bugzilla #1337607 for further infos. Thanks to Claudio Pisa for his hint on editing BOINC source code

* Sat Jun 25 2016 Germano Massullo <germano.massullo@gmail.com> - 7.6.22-6
- Improved solution to RH bugreport #1347423. Used -DNDEBUG flag instead of patching source code

* Sat Jun 25 2016 Germano Massullo <germano.massullo@gmail.com> - 7.6.22-5
- disabled wxWidgets trace. See RH bugreport #1347423

* Mon May 16 2016 Germano Massullo <germano.massullo@gmail.com> - 7.6.22-4
- Changed gtk+-x11-2.0 to gtk+-x11-3.0

* Mon May 16 2016 Germano Massullo <germano.massullo@gmail.com> - 7.6.22-3
- Edited systemd script to fix bugreport #1329332

* Mon May 16 2016 Germano Massullo <germano.massullo@gmail.com> - 7.6.22-2
- Rebuild to enforce GTK2 stuff removal and do tests to fix bugreport #1323492

* Thu Feb 18 2016 Laurence Field <laurence.field@cern.ch> - 7.6.22-1
- Upstream release of version 7.6.22

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.42-9.gitdd0d630
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 31 2016 Germano Massullo <germano.massullo@gmail.com> - 7.2.42-8.gitdd0d630
- Fixed %%{_sysconfdir}/bash_completion.d/ See https://bugzilla.redhat.com/show_bug.cgi?id=1192799

* Mon Nov 09 2015 Germano Massullo <germano.massullo@gmail.com> - 7.2.42-7.gitdd0d630
- fixed %%{_localstatedir}/lib/boinc/ ownership.

* Mon Aug 03 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 7.2.42-6.gitdd0d630
- Rework CXXFLAGS handling (Fix F23FTBS, RHBZ#1239389).
- Fix bogus permissions on %%{_localstatedir}/lib/boinc.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.2.42-5.gitdd0d630
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Nov 20 2014 Mattia Verga <mattia.verga@tiscali.it> - 7.2.42-4.gitdd0d630
- Clean up build requires and delete not official script.

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.2.42-3.gitdd0d630
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.2.42-2.gitdd0d630
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 19 2014 Mattia Verga <mattia.verga@tiscali.it> - 7.2.42-1.gitdd0d630
- Upgrade to 7.2.42

* Wed Feb 19 2014 Mattia Verga <mattia.verga@tiscali.it> - 7.2.39-1.gitdc95e3f
- Upgrade to 7.2.39 #1065275
- Remove ControlGroup setting from systemd unit file. #1065648
- Backport patch from 7.3 branch to (hopefully) fix idle time detection. #1047044

* Fri Feb 07 2014 Mattia Verga <mattia.verga@tiscali.it> - 7.2.33-3.git1994cc8
- Remove CPUShares limitation to systemd unit. #1038283

* Tue Dec 17 2013 Mattia Verga <mattia.verga@tiscali.it> - 7.2.33-2.git1994cc8
- Change default attribute of /var/lib/boinc to give write permission to boinc group
- Fix systemd requires as described in guidelines

* Tue Dec 17 2013 Mattia Verga <mattia.verga@tiscali.it> - 7.2.33-1.git1994cc8
- Update to 7.2.33
- Removed no more needed X11 patch
- Removed boinc manager notification patch see bug #990693
- Add patch to fix Italian locale dir
- Enabled parallel make
- Removed boincmgr wrap
- Fix checkin_notes
- Added boinc_gpu wrapper to fix GPU detection (see instruction on how to use it)
- Build now requires mariadb-devel instead of mysql-devel as actual default for Fedora
- Fix trim script for new directory and not remove html dir for build error
- Remove scripts for update from sysV to systemd

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.0.65-2.git79b00ef
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Apr 28 2013 Miloš Jakubíček <xjakub@fi.muni.cz> - 7.0.65-1.git79b00ef
- Update to 7.0.65
- Fix /var/lib/boinc user and group (typo caused by the previous commit)

* Wed Feb 13 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 7.0.44-3.git443c49949
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247
- clean up spec to follow current guidelines
- use systemd macros. resolves rhbz#850049

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.0.44-2.git443c49949
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 15 2013 Miloš Jakubíček <xjakub@fi.muni.cz> - 7.0.44-1.git443c49949
- Svn to Git switch of upstream sources
- Rebase the 7.0a branch to 7.0.44 (pulled from git)
- Removed BR: automake
- Dropped boinc-xcb-compat.patch (merged upstream)

* Tue Jan 15 2013 Miloš Jakubíček <xjakub@fi.muni.cz> - 7.0.36-2.r26158svn
- Added BR: automake

* Sat Jan 12 2013 Miloš Jakubíček <xjakub@fi.muni.cz> - 7.0.36-1.r26158svn
- Rebase the 7.0a branch to 7.0.36
- Removed non-free code as per BZ#894290
- Dropped boinc-client-menu.patch (merged upstream)

* Mon Aug 20 2012 Adam Jackson <ajax@redhat.com> 7.0.29-3.r25790svn
- Rebuild for new xcb-util soname

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.0.29-2.r25790svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 09 2012 Miloš Jakubíček <xjakub@fi.muni.cz> - 7.0.29-1.r25790svn
- Update to 7.0a branch
- Added boinc-client-X11.patch to workaround a --no-as-needed build issue
- Added boinc-manager-client-notification.patch to be tell users about how
  to setup Boinc on Fedora
- Added backported boinc-client-menu.patch to fix menu display
- Don't use Boinc rotating log files (never deletes them)
- Fix automatic startup of the service
- Fix leaving lockfile after service stop
- Resolve BZ#731669, BZ#814060, BZ#825032, BZ#827912, BZ#829564, BZ#834900,
  BZ#838507.

* Fri Jun 22 2012 Miloš Jakubíček <xjakub@fi.muni.cz> - 6.12.43-2.r25218svn
- Fixed naming systemd service file
- Fixed logging to /var/log/boinc.log and /var/log/boincerr.log

* Wed Feb 08 2012 Miloš Jakubíček <xjakub@fi.muni.cz> - 6.12.43-1.r25218svn
- Rebase the 6.12 branch to 6.12.43
- Switch from SysVInit to systemd
- drop boinc-libnotify.patch (merged upstream)

* Thu Jan 12 2012 Adam Jackson <ajax@redhat.com> 6.12.35-4.rsvn
- boinc-xcb-compat.patch: Also fix the atom enums to be compatible with
  new XCB.

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 6.12.35-3.r24014svn
- Rebuild for new libpng

* Thu Dec 01 2011 Adam Jackson <ajax@redhat.com> 6.12.35-2.rsvn
- Rebuild for new xcb-util
- boinc-glib-compat.patch: Build compat with new glib
- boinc-xcb-compat.patch: Build compat with new xcb-util

* Fri Aug 19 2011 Miloš Jakubíček <xjakub@fi.muni.cz> - 6.12.35-1.r24014svn
- Update to 6.12 branch (fix BZ#719875, BZ#690333)
- Dropped boinc-gui-rpc-port.patch (merged upstream)
- Added BR: libnotify-devel, xcb-util-devel
- Added boinc-libnotify.patch to build with libnotify >= 0.7
- Added boinc-manager-Makefile.patch to fix Makefile indentation error
- Now shipping also BOINC screensaver
- Added BOINC Client translation files
- Fixed scheduling problems related to cgroups (BZ#705444)

* Wed Feb 09 2011 Miloš Jakubíček <xjakub@fi.muni.cz> - 6.10.58-3.r22930svn
- Add boinc-gui-rpc-port.patch, fixing BZ#620585

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.10.58-2.r22930svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 20 2011 Miloš Jakubíček <xjakub@fi.muni.cz> - 6.10.58-1.r22930svn
- Rebase the 6.10 branch to 6.10.58
- Fix rpmlint complaining:
- E: executable-marked-as-config-file /etc/sysconfig/boinc-client
- E: script-without-shebang /etc/sysconfig/boinc-client
