%global _cups_serverbin %{_prefix}/lib/cups

%global upstream_version 2.0rc2

%if 0%{?fedora}
%bcond_without mdns
%else
%bcond_with mdns
%endif


Name: cups-browsed
Epoch: 1
Version: 2.0~rc2
Release: 3%{?dist}
Summary: Daemon for local auto-installation of remote printers
# the CUPS exception text is the same as LLVM exception, so using that name with
# agreement from legal team
# https://lists.fedoraproject.org/archives/list/legal@lists.fedoraproject.org/message/A7GFSD6M3GYGSI32L2FC5KB22DUAEQI3/
License: Apache-2.0 WITH LLVM-exception
URL: https://github.com/OpenPrinting/cups-browsed
Source0: %{URL}/releases/download/%{upstream_version}/%{name}-%{upstream_version}.tar.gz


# Patches
Patch001: 0001-cups-browsed.c-Ensure-we-always-send-a-valid-name-to.patch


# remove once CentOS Stream 10 is released, cups-browsed
# was shipped in cups-filters before 2.0
Conflicts: cups-filters < 2.0

# for generating configure and Makefile scripts in autogen.h
BuildRequires: autoconf
# for generating configure and Makefile scripts in autogen.h
BuildRequires: automake
# most filter functions written in C
BuildRequires: gcc
# for generating configure and Makefile scripts in autogen.h
BuildRequires: gettext-devel
# for autosetup
BuildRequires: git-core
# for generating configure and Makefile scripts in autogen.h
BuildRequires: libtool
# uses Makefiles
BuildRequires: make
# for pkg-config in configure and in SPEC file
BuildRequires: pkgconf-pkg-config
# for looking for devices on mDNS and their sharing on mDNS
BuildRequires: pkgconfig(avahi-client)
# for polling avahi
BuildRequires: pkgconfig(avahi-glib)
# uses CUPS and IPP API
BuildRequires: pkgconfig(cups) >= 2.2.2
# uses cupsfilters API
BuildRequires: pkgconfig(libcupsfilters) >= 2.0b3
# implicitclass uses libppd
BuildRequires: pkgconfig(libppd) >= 2.0b3
# for dBUS proxy from GLib
BuildRequires: pkgconfig(glib-2.0)
# needed for systemd rpm macros in scriptlets
BuildRequires: systemd-rpm-macros

%if %{with mdns}
# Avahi has to run for mDNS support
Recommends: avahi
# if set to browse or share mDNS, we need a resolver
Recommends: nss-mdns
%endif
# only recommends cups RPM in case someone wants to use CUPS container/SNAP
# - cups-browsed has to have a cupsd daemon to send requests to
# using a weak dep will work for bootstraping as well in case the old cups-filters
# 1.x, which is CUPS dependency, will be in repos when cups-browsed
Recommends: cups

# requires cups directories
Requires: cups-filesystem

Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd


%description
cups-browsed is a helper daemon, which automatically installs printers
locally, provides load balancing and clustering of print queues.
The daemon installs the printers based on found mDNS records and CUPS
broadcast, or by polling a remote print server.


%prep
%autosetup -n %{name}-%{upstream_version} -S git


%build
# generate configuration/compilation files
./autogen.sh

# --enable-auto-setup-driverless-only - enable autoinstalling of driverless IPP
# destinations
# --disable-saving-created-queues - don't save the queues during shutdown
# --disable-frequent-netif-update - don't update network interfaces after
# every found printer, update only on NM dBUS event
# --with-browseremoteprotocols - which protocols to use for looking for printers, default DNSSD and CUPS
# --with-remote-cups-local-queue-naming - use the name from remote server
# if polling the server for printers via BrowsePoll
%configure --enable-auto-setup-driverless-only\
  --disable-rpath\
  --disable-saving-created-queues\
  --disable-frequent-netif-update\
%if %{without mdns}
  --with-browseremoteprotocols=none\
%endif
  --with-remote-cups-local-queue-naming=RemoteName\
  --without-rcdir

%make_build


%install
%make_install

# systemd unit file
mkdir -p %{buildroot}%{_unitdir}
install -p -m 644 daemon/cups-browsed.service %{buildroot}%{_unitdir}

# remove INSTALL file
rm -f %{buildroot}%{_pkgdocdir}/INSTALL

# provided by cups-browsed dependency
rm -f %{buildroot}%{_pkgdocdir}/CHANGES-1.x.md

# license related files are already under /usr/share/licenses
rm -f %{buildroot}%{_pkgdocdir}/{LICENSE,COPYING,NOTICE}


%post
%systemd_post cups-browsed.service

# put UpdateCUPSQueuesMaxPerCall and PauseBetweenCUPSQueueUpdates into cups-browsed.conf
# for making cups-browsed work more stable for environments with many print queues
# remove this after 1-2 releases
for directive in "UpdateCUPSQueuesMaxPerCall" "PauseBetweenCUPSQueueUpdates"
do
    found=`%{_bindir}/grep "^[[:blank:]]*$directive" %{_sysconfdir}/cups/cups-browsed.conf`
    if [ -z "$found" ]
    then
        if [ "x$directive" == "xUpdateCUPSQueuesMaxPerCall" ]
        then
            %{_bindir}/echo "UpdateCUPSQueuesMaxPerCall 20" >> %{_sysconfdir}/cups/cups-browsed.conf
        else
            %{_bindir}/echo "PauseBetweenCUPSQueueUpdates 5" >> %{_sysconfdir}/cups/cups-browsed.conf
        fi
    fi
done

%preun
%systemd_preun cups-browsed.service

%postun
%systemd_postun_with_restart cups-browsed.service


%files
%license COPYING LICENSE NOTICE
%doc ABOUT-NLS AUTHORS CHANGES.md CONTRIBUTING.md DEVELOPING.md README.md
# implicitclass backend must be run as root
# https://github.com/OpenPrinting/cups-filters/issues/183#issuecomment-570196216
%attr(0744,root,root) %{_cups_serverbin}/backend/implicitclass
# 2123809 - rpm -Va reports changes due %%post scriptlet (remove the verify part once we remove
# cups-browsed.conf update from %%post scriptlet)
%config(noreplace) %verify(not size filedigest mtime) %{_sysconfdir}/cups/cups-browsed.conf
%{_mandir}/man5/cups-browsed.conf.5.gz
%{_mandir}/man8/cups-browsed.8.gz
%{_sbindir}/cups-browsed
%{_unitdir}/cups-browsed.service


%changelog
* Tue Aug 29 2023 Zdenek Dohnal <zdohnal@redhat.com> - 1:2.0~rc2-3
- 2150035 - [abrt] cups-filters: __strlen_avx2(): cups-browsed killed by SIGSEGV

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0~rc2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 28 2023 Zdenek Dohnal <zdohnal@redhat.com> - 1:2.0~rc2-1
- 2.0rc2

* Thu Apr 27 2023 Zdenek Dohnal <zdohnal@redhat.com> - 1:2.0~rc1-1
- 2.0rc1

* Mon Apr 03 2023 Zdenek Dohnal <zdohnal@redhat.com> - 1:2.0~b4-1
- 2179346 - cups-browsed-2.0b4 is available

* Wed Mar 01 2023 Zdenek Dohnal <zdohnal@redhat.com> - 1:2.0~b3-2
- use Epoch to ensure upgrade path because I didn't read FPG carefully

* Thu Feb 02 2023 Zdenek Dohnal <zdohnal@redhat.com> - 2.0b3-1
- Initial import (fedora#2170547)
