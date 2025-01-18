# https://gcc.gnu.org/gcc-10/porting_to.html#common
# https://github.com/ve7fet/linuxax25/issues/7
%define _legacy_common_support 1

Name:		ax25-tools
Version:	1.0.4
Release:	13%{?dist}
Summary:	Tools used to configure an ax.25 enabled computer

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://www.linux-ax25.org/wiki/LinuxAX25

# Official upstream is not active, moving to supported fork.
# https://github.com/ve7fet/linuxax25
Source0:        https://github.com/ve7fet/linuxax25/archive/ax25tools-%{version}.tar.gz
Source1:	smdiag.desktop
Source2:	xfhdlcchpar.desktop
Source3:	xfhdlcsd.desktop
Source4:	xfsmdiag.desktop
Source5:	xfsmmixer.desktop
#Temporary Icon
Source6:	%{name}.png

BuildRequires:	automake gcc gcc-c++
BuildRequires:	libax25-devel
BuildRequires:	ncurses-devel
BuildRequires:	libXt-devel
BuildRequires:	libXi-devel
BuildRequires:	fltk-devel
BuildRequires:	libX11-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:	desktop-file-utils
BuildRequires: make


%description
ax25-tools is a collection of tools that are used to configure an ax.25 enabled
computer. They will configure interfaces and assign callsigns to ports as well
as Net/ROM and ROSE configuration.  This package only contains the command
line programs; the GUI programs are contained in ax25-tools-x package.

 * m6pack - handle multiple 6pack TNCs on a single interface
 * ax25d - general purpose AX.25, NET/ROM and Rose daemon
 * axctl - configure/Kill running AX.25 connections
 * axparms - configure AX.25 interfaces
 * axspawn - allow automatic login to a Linux system
 * beacon - transmit periodic messages on an AX.25 port
 * bpqparms - configure BPQ ethernet devices
 * mheardd - display AX.25 calls recently heard
 * rxecho - transparently route AX.25 packets between ports
 * mheard - collect information about packet activity
 * dmascc_cfg - configure dmascc devices
 * sethdlc - get/set Linux HDLC packet radio modem driver port information
 * smmixer - get/set Linux soundcard packet radio modem driver mixer
 * kissattach - Attach a KISS or 6PACK interface
 * kissnetd - create a virtual network
 * kissparms - configure KISS TNCs
 * mkiss - attach multiple KISS interfaces
 * net2kiss - convert a network AX.25 driver to a KISS stream on a pty
 * netromd - send and receive NET/ROM routing messages
 * nodesave - saves NET/ROM routing information
 * nrattach - start a NET/ROM interface
 * nrparms - configure a NET/ROM interface
 * nrsdrv - KISS to NET/ROM serial converter
 * rsattach - start a ROSE interface
 * rsdwnlnk - user exit from the ROSE network
 * rsmemsiz - monitor the ROSE subsystem
 * rsusers.sh - monitor AX.25, NET/ROM and ROSE users
 * rsparms - configure a ROSE interface
 * rsuplnk - User entry into the ROSE network
 * rip98d - RIP98 routing daemon
 * ttylinkd - TTYlink daemon for AX.25, NET/ROM, ROSE and IP
 * ax25_call - Make an AX.25 connection
 * netrom_call - Make a NET/ROM connection
 * rose_call - Make a ROSE connection
 * tcp_call - Make a TCP connection
 * yamcfg - configure a YAM interface


%package x
Summary:	X tools used to configure an AX.25 enabled computer
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description x
ax25-tools-x is a collection of tools that are used to configure an ax.25 enabled
computer.  This package contains the GUI programs to configure Baycom modem
and sound modem.

 * smdiag - Linux soundcard packet radio modem driver diagnostics utility
 * xfhdlcchpar - kernel HDLC radio modem driver channel parameter utility
 * xfhdlcst - kernel HDLC radio modem driver status display utility
 * xfsmdiag - kernel soundcard radio modem driver diagnostics utility
 * xfsmmixer - kernel soundcard radio modem driver mixer utility


%package docs
Summary:	Documentation for ax25-tools and ax25-tools-x
BuildArch:      noarch

%description docs
ax25-tools is a collection of tools that are used to configure an ax.25 enabled
computer.  This package contains the GUI programs to configure Baycom modem
and sound modem. This package contains the documentation for ax25-tools and
ax25-tools-x


%prep
%autosetup -p1 -n ax25tools-%{version}


%build
./autogen.sh
%configure --with-xutils
make %{?_smp_mflags} CFLAGS="%{optflags}"


%install
%make_install

# no upstream .desktop or icon yet so we'll use a temporary one
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/pixmaps/
cp %{SOURCE6} ${RPM_BUILD_ROOT}%{_datadir}/pixmaps/%{name}.png
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/applications
desktop-file-install	\
	--dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE1}
desktop-file-install	\
	--dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE2}
desktop-file-install	\
	--dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE3}
desktop-file-install	\
	--dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE4}
desktop-file-install	\
	--dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE5}

#don't include these twice
rm -rf $RPM_BUILD_ROOT%{_docdir}/ax25tools


%files
%doc AUTHORS ChangeLog
%doc doc/README*
%license COPYING
%{_bindir}/*
%{_sbindir}/*
%{_localstatedir}/ax25/mheard/
%config(noreplace) %{_sysconfdir}/ax25/ax25.profile
%config(noreplace) %{_sysconfdir}/ax25/ax25d.conf
%config(noreplace) %{_sysconfdir}/ax25/axports
%config(noreplace) %{_sysconfdir}/ax25/axspawn.conf
%config(noreplace) %{_sysconfdir}/ax25/nrbroadcast
%config(noreplace) %{_sysconfdir}/ax25/nrports
%config(noreplace) %{_sysconfdir}/ax25/rip98d.conf
%config(noreplace) %{_sysconfdir}/ax25/rsports
%config(noreplace) %{_sysconfdir}/ax25/rxecho.conf
%config(noreplace) %{_sysconfdir}/ax25/ttylinkd.conf
%exclude %{_bindir}/smdiag
%exclude %{_sbindir}/xfhdlcchpar
%exclude %{_sbindir}/xfhdlcst
%exclude %{_sbindir}/xfsmdiag
%exclude %{_sbindir}/xfsmmixer

%files x
%{_bindir}/smdiag
%{_sbindir}/xfhdlcchpar
%{_sbindir}/xfhdlcst
%{_sbindir}/xfsmdiag
%{_sbindir}/xfsmmixer
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/*.desktop

%files docs
%doc COPYING
%{_mandir}/man?/*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.4-12
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Feb 16 2020 Richard Shaw <hobbes1069@gmail.com> - 1.0.4-1
- Update to 1.0.4.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 14 2018 Richard Shaw <hobbes1069@gmail.com> - 1.0.3-8
- Add patch for mkiss segfault.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 18 2015 Richard Shaw <hobbes1069@gmail.com> - 0.0.10-0.15.rc4
- Update to latest upstream release.

* Fri Sep 18 2015 Richard Shaw <hobbes1069@gmail.com> - 0.0.10-0.14.rc2
- Prevent duplicate binaries from being packaged, fixes BZ#1058070.
- Add patch to allow more than 4 netrom ports, fixes BZ#1152001.
- Spec file cleanup.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.10-0.13.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr 20 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0.0.10-0.12.rc2
- Fixed crash when processing ROSE packets (by rose-fix patch)
  Resolves: rhbz#1210008

* Tue Apr  7 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0.0.10-0.11.rc2
- Fixed netrom nrattach
  Resolves: rhbz#981833
- Fixed format string build error

* Thu Feb 19 2015 Rex Dieter <rdieter@fedoraproject.org> 0.0.10-0.10.rc2
- rebuild (fltk)

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.10-0.9.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 20 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 0.0.10-0.8.rc2
- Fix FTBFS with automake-1.14 and -Werror=format-security (#1105990)
- Cleanup spec

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.10-0.7.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.10-0.6.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.10-0.5.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.10-0.4.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.10-0.3.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Jul 30 2011 Randall J. Berry, N3LRX <dp67@fedoraproject.org> - 0.0.10-0.2.rc2
- Rebuild for broken deps on Rawhide/F16

* Mon Jun 27 2011 Randall J. Berry, N3LRX <dp67@fedoraproject.org> - 0.0.10-0.1.rc2
- New upstream release

* Sun Jun 26 2011 Randall J. Berry, N3LRX <dp67@fedoraproject.org> - 0.0.9-9
- Add .desktop files for GUI applications in ax25-tools-x
- Upload source to git

* Sun Jun 26 2011 Randall J. Berry, N3LRX <dp67@fedoraproject.org> - 0.0.9-8
- Seperate documentation into sperate package

* Sun Jun 26 2011 Randall J. Berry, N3LRX <dp67@fedoraproject.org> - 0.0.9-7
- Attempt rebuild including upstream recommendations
- Additional BuildRequires libX11-devel

* Tue Jun 21 2011 Randall J. Berry, N3LRX <dp67@fedoraproject.org> - 0.0.9-6
- Rebuild test including new BRs

* Tue Jun 21 2011 Ralf Baechle <ralf@linux-mips.org> - 0.0.9-5
- Added BRs libXi-devel, fltk-devel

* Tue Jun 21 2011 Randall J. Berry, N3LRX <dp67@fedoraproject.org> - 0.0.9-4
- Rebuild per bz #545272

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Mar 12 2009 Randall J. Berry <dp67@fedoraproject.org> 0.0.9-1
- Upstream update to 0.0.9, #488049
- Upstream URL has changed
- Remove patches applied to newer source

* Thu Dec 11 2008 Sindre Pedersen Bjørdal <foolish@guezz.net> 0.0.8-3
- Fix pseudo-terminal issue, #475045

* Sat Feb 16 2008 Robert 'Bob' Jensen <bob@bobjensen.com> 0.0.8-2
- Submit for review

* Thu Dec 06 2007 Sindre Pedersen Bjørdal <foolish@guezz.net> 0.0.8-1
- Initial Build
