# this is purely a shell script, so no debug packages
%global debug_package %{nil}

Name: rear
Version: 2.6
Release: 9%{?dist}
Summary: Relax-and-Recover is a Linux disaster recovery and system migration tool
URL: http://relax-and-recover.org/
License: GPLv3

# as GitHub stopped with download section we need to go back to Sourceforge for downloads
Source0: https://sourceforge.net/projects/rear/files/rear/%{version}/rear-%{version}.tar.gz
# Add cronjob and systemd timer as documentation
Source1: rear.cron
Source2: rear.service
Source3: rear.timer
# Skip buildin modules, RHBZ#1831311
Patch0: 0001-skip-kernel-buildin-modules.patch

# rear contains only bash scripts plus documentation so that on first glance it could be "BuildArch: noarch"
# but actually it is not "noarch" because it only works on those architectures that are explicitly supported.
# Of course the rear bash scripts can be installed on any architecture just as any binaries can be installed on any architecture.
# But the meaning of architecture dependent packages should be on what architectures they will work.
# Therefore only those architectures that are actually supported are explicitly listed.
# This avoids that rear can be "just installed" on architectures that are actually not supported (e.g. ARM or IBM z Systems):
ExclusiveArch: %ix86 x86_64 ppc ppc64 ppc64le ia64
# Furthermore for some architectures it requires architecture dependent packages (like syslinux for x86 and x86_64)
# so that rear must be architecture dependent because ifarch conditions never match in case of "BuildArch: noarch"
# see the GitHub issue https://github.com/rear/rear/issues/629
%ifarch %ix86 x86_64
Requires: syslinux
%endif
# In the end this should tell the user that rear is known to work only on ix86 x86_64 ppc ppc64 ppc64le ia64
# and on ix86 x86_64 syslinux is explicitly required to make the bootable ISO image
# (in addition to the default installed bootloader grub2) while on ppc ppc64 the
# default installed bootloader yaboot is also useed to make the bootable ISO image.

# Required for HTML user guide
BuildRequires: make
BuildRequires: asciidoctor

### Mandatory dependencies:
Requires: binutils
Requires: ethtool
Requires: gzip
Requires: iputils
Requires: parted
Requires: tar
Requires: openssl
Requires: gawk
Requires: attr
Requires: bc
Requires: iproute
Requires: genisoimage
%if 0%{?rhel}
Requires: util-linux
%endif

%description
Relax-and-Recover is the leading Open Source disaster recovery and system
migration solution. It comprises of a modular
frame-work and ready-to-go workflows for many common situations to produce
a bootable image and restore from backup using this image. As a benefit,
it allows to restore to different hardware and can therefore be used as
a migration tool as well.

Currently Relax-and-Recover supports various boot media (incl. ISO, PXE,
OBDR tape, USB or eSATA storage), a variety of network protocols (incl.
sftp, ftp, http, nfs, cifs) as well as a multitude of backup strategies
(incl.  IBM TSM, MircroFocus Data Protector, Symantec NetBackup, EMC NetWorker,
Bacula, Bareos, BORG, Duplicity, rsync).

Relax-and-Recover was designed to be easy to set up, requires no maintenance
and is there to assist when disaster strikes. Its setup-and-forget nature
removes any excuse for not having a disaster recovery solution implemented.

Professional services and support are available.

#-- PREP, BUILD & INSTALL -----------------------------------------------------#
%prep
%autosetup -p1

# Change /lib to /usr/lib for COPY_AS_IS
sed -E -e "s:([\"' ])/lib:\1/usr/lib:g" \
    -i usr/share/rear/prep/GNU/Linux/*include*.sh

# Same for Linux.conf
sed -e 's:/lib/:/usr/lib/:g' \
    -e 's:/lib\*/:/usr/lib\*/:g' \
    -e 's:/usr/usr/lib:/usr/lib:g' \
    -i 'usr/share/rear/conf/GNU/Linux.conf'

%build
# build HTML user guide
make doc

%install
%{make_install}
install -p -d %{buildroot}%{_docdir}/%{name}/
install -m 0644 %{SOURCE1} %{buildroot}%{_docdir}/%{name}/
install -m 0644 %{SOURCE2} %{buildroot}%{_docdir}/%{name}/
install -m 0644 %{SOURCE3} %{buildroot}%{_docdir}/%{name}/

#-- FILES ---------------------------------------------------------------------#
%files
%doc MAINTAINERS COPYING README.adoc doc/*.txt doc/user-guide/*.html
%doc %{_mandir}/man8/rear.8*
%doc %{_docdir}/%{name}/rear.*
%config(noreplace) %{_sysconfdir}/rear/
%{_datadir}/rear/
%{_sharedstatedir}/rear/
%{_sbindir}/rear

#-- CHANGELOG -----------------------------------------------------------------#
%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Feb 26 2021 Christopher Engelhard <ce@lcts.de> - 2.6-5
- Change /lib to /usr/lib in scripts to fix RHBZ #1931112

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 23 2020 Christopher Engelhard <ce@lcts.de> - 2.6-3
- Stop auto-creating a cronjob, but ship example cronjob/
  systemd timer units in docdir instead (upstream issue #1829)
- Build & ship HTML user guide
- Remove %pre scriptlet, as it was introduced only to fix a
  specific upgrade issue with v1.15 in 2014

* Tue Sep 22 2020 Christopher Engelhard <ce@lcts.de> - 2.6-2
- Backport upstream PR#2469 to fix RHBZ #1831311

* Tue Sep 22 2020 Christopher Engelhard <ce@lcts.de> - 2.6-1
- Update to 2.6
- Streamline & clean up spec file

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul 30 2015 Johannes Meixner <jsmeix@suse.de>
- For a changelog see the rear-release-notes.txt file.

