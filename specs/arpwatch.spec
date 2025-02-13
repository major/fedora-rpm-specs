%bcond autoreconf 1

Name:           arpwatch
Epoch:          14
Version:        3.7
Release:        %autorelease
Summary:        Network monitoring tools for tracking IP addresses on a network

# SPDX matching with BSD-3-Clause confirmed at
# https://gitlab.com/fedora/legal/fedora-license-data/-/issues/49
License:        BSD-3-Clause
# Any files under different licenses are part of the build system and do not
# contribute to the license of the binary RPM:
#   - config.guess and config.sub are GPL-3.0-or-later
#   - configure is FSFUL
#   - install-sh is X11
#   - mkdep is BSD-4.3RENO
SourceLicense:  %{shrink:
                %{license} AND
                BSD-4.3RENO AND
                FSFUL AND
                GPL-3.0-or-later AND
                X11
                }
URL:            https://ee.lbl.gov/


Requires:       /usr/sbin/sendmail
Requires:       python3

BuildRequires:  gcc
BuildRequires:  make
%if %{with autoreconf}
BuildRequires:  autoconf
%endif

BuildRequires:  /usr/sbin/sendmail
BuildRequires:  systemd-rpm-macros
%{?sysuser_requires_compat}
BuildRequires:  python3-devel
BuildRequires:  libpcap-devel

# Note that https://ee.lbl.gov/ may not link to the latest version; the
# directory listing at https://ee.lbl.gov/downloads/arpwatch/ shows all
# available versions.
Source0:        https://ee.lbl.gov/downloads/arpwatch/arpwatch-%{version}.tar.gz
# This file comes from https://standards-oui.ieee.org/oui/oui.csv; it is used
# to generate ethercodes.dat. Because it is unversioned (and frequently
# updated), we store the file directly in the repository with the spec file;
# see the update-oui-csv script.
#
# File oui.csv last fetched 2025-02-01T15:35:35+00:00.
Source1:        oui.csv
Source2:        arpwatch.service
Source3:        arpwatch.sysconfig
Source4:        arp2ethers.8
Source5:        massagevendor.8
Source6:        arpwatch.sysusers

# The latest versions of all “arpwatch-3.1-*” patches were sent upstream by
# email 2021-04-24.

# Fix section numbers in man page cross-references. With minor changes, this
# patch dates all the way back to arpwatch-2.1a4-man.patch, from RHBZ #15442.
Patch:          arpwatch-3.1-man-references.patch
# Add, and document, a -u argument to change to a specified unprivileged user
# after establishing sockets. This combines and improves multiple previous
# patches; see patch header and changelog for notes.
Patch:          arpwatch-3.2-change-user.patch
# Fix nonstandard sort flags in arp2ethers script.
Patch:          arpwatch-3.1-arp2ethers-sort-invocation.patch
# Fix stray rm (of an undefined variable) in example arpfetch script.
Patch:          arpwatch-3.1-arpfetch-stray-rm.patch
# Do not add /usr/local/bin or /usr/local/sbin to the PATH in any scripts
Patch:          arpwatch-3.2-no-usr-local-path.patch
# Do not attempt to search for local libpcap libraries lying around in the
# parent of the build directory, or anywhere else random. This is not expected
# to succeed anyway, but it is better to be sure.
Patch:          arpwatch-3.1-configure-no-local-pcap.patch
# RHBZ #244606: Correctly handle -n 0/32 to allow the user to disable reporting
# bogons from 0.0.0.0.
Patch:          arpwatch-3.1-all-zero-bogon.patch
# When arpwatch is terminated cleanly by a signal (INT/TERM/HUP) handler, the
# exit code should be zero for success instead of nonzero for failure.
Patch:          arpwatch-3.5-exitcode.patch
# When -i is not given, do not just try the first device found, but keep
# checking devices until a usable one is found, if any is available.
# Additionally, handle the case where a device provides both supported and
# unsupported datalink types.
Patch:          arpwatch-3.5-devlookup.patch

# Replace _getshort(), “a glibc function that hasn't been declared in the
# installed headers for many, many years,” with ns_get16(). Fixes C99
# compatibility (https://bugzilla.redhat.com/show_bug.cgi?id=2166336). Sent
# upstream by email 2023-02-01.
Patch:          arpwatch-3.3-c99.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

%global pkgstatedir %{_sharedstatedir}/arpwatch

%description
The arpwatch package contains arpwatch and arpsnmp. Arpwatch and arpsnmp are
both network monitoring tools. Both utilities monitor Ethernet or FDDI network
traffic and build databases of Ethernet/IP address pairs, and can report
certain changes via email.

Install the arpwatch package if you need networking monitoring devices which
will automatically keep track of the IP addresses on your network.


%prep
%autosetup -p1

# Substitute absolute paths to awk scripts in shell scripts
sed -r -i 's|(-f *)([^[:blank:]+]\.awk)|\1%{_datadir}/arpwatch/\2|' arp2ethers

# Fix default directory in man pages to match ARPDIR in build section. This was
# formerly done by arpwatch-dir-man.patch. For thoroughness, do the same
# replacement in update-ethercodes.sh.in and bihourly.sh, even though they are
# not installed.
sed -r -i 's|/usr/local/arpwatch|%{pkgstatedir}|g' *.8.in *.sh.in *.sh

# Fix Python interpreter path (but note that this script is not installed)
sed -r -i 's|/usr/local/bin/python|%{python3}|g' update-ethercodes.sh.in

# Emailed upstream requesting a separate LICENSE/COPYING file 2022-07-30.
# For now, we extract it from the main source file’s “header” comment.
awk '/^ \* / { print substr($0, 4); } /^ \*\// { exit }' arpwatch.c |
  tee LICENSE


%conf
%if %{with autoreconf}
autoreconf --force --install --verbose
%endif

# Prior to version 3.4, this was handled by the configure script. If it is not
# defined, the build fails because time.h is not included in report.c. This
# regregression was reported upstream by email to arpwatch@ee.lbl.gov on
# 2023-09-06.
export CPPFLAGS="${CPPFLAGS-} -DTIME_WITH_SYS_TIME=1"

%configure --with-sendmail=/usr/sbin/sendmail PYTHON=%{python3}


%build
%make_build ARPDIR=%{pkgstatedir}


%install
install -p -D -m 0644 %{SOURCE6} '%{buildroot}%{_sysusersdir}/arpwatch.conf'

# The upstream Makefile does not create the directories it requires, so we must
# do it manually. Additionally, it attempts to comment out the installation of
# the init script on non-FreeBSD platforms, but this does not quite work as
# intended. We just let it install the file, then remove it afterwards.
install -d %{buildroot}%{_mandir}/man8 \
    %{buildroot}%{_sbindir} \
    %{buildroot}%{_datadir}/arpwatch \
    %{buildroot}%{pkgstatedir} \
    %{buildroot}%{_unitdir} \
    %{buildroot}%{_prefix}/etc/rc.d

%make_install

# Make install uses mode 0555, which is unconventional, and which can interfere
# with debuginfo generation since the file is not writable by its owner.
chmod -v 0755 %{buildroot}%{_sbindir}/arpwatch %{buildroot}%{_sbindir}/arpsnmp

install -p -t %{buildroot}%{_datadir}/arpwatch -m 0644 *.awk
install -p -t %{buildroot}%{_sbindir} arp2ethers
install -p massagevendor.py %{buildroot}%{_sbindir}/massagevendor

install -p -t %{buildroot}%{pkgstatedir} -m 0644 *.dat
touch %{buildroot}%{pkgstatedir}/arp.dat- \
    %{buildroot}%{pkgstatedir}/arp.dat.new

install -p -t %{buildroot}%{_unitdir} -m 0644 %{SOURCE2}
%{python3} massagevendor.py < %{SOURCE1} \
    > %{buildroot}%{pkgstatedir}/ethercodes.dat
touch -r %{SOURCE1} ethercodes.dat

# Add an environment/sysconfig file:
install -d %{buildroot}%{_sysconfdir}/sysconfig
install -p -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/sysconfig/arpwatch

# Add extra man pages not provided upstream:
install -p -t %{buildroot}%{_mandir}/man8 -m 0644 %{SOURCE4} %{SOURCE5}

# Remove legacy init scripts:
rm -rvf %{buildroot}%{_prefix}/etc/rc.d


%check
# Verify the sed script in the prep section did not miss fixing the ARPDIR
# anywhere
if grep -FrnI '/usr/local/arpwatch' .
then
  echo 'Missed fixing ARPDIR in at least one file' 1>&2
  exit 1
fi

# Verify we did not miss any PATH alterations in
# arpwatch-no-usr-local-path.patch.
if grep -ErnI --exclude=mkdep --exclude='config.*' '^[^#].*/usr/local/s?bin' .
then
  echo 'Probably missed an uncommented PATH alteration with /usr/local' 1>&2
  exit 1
fi


%post
%systemd_post arpwatch.service




%postun
%systemd_postun_with_restart arpwatch.service


%preun
%systemd_preun arpwatch.service


%files
%license LICENSE
%doc README
%doc CHANGES
%doc arpfetch

%{_sbindir}/arpwatch
%{_sbindir}/arpsnmp
# manually-installed scripts
%{_sbindir}/arp2ethers
%{_sbindir}/massagevendor

%dir %{_datadir}/arpwatch
%{_datadir}/arpwatch/*.awk

# make install uses mode 0444, which is unconventional
%attr(0644,-,-) %{_mandir}/man8/*.8*

%{_unitdir}/arpwatch.service
%{_sysusersdir}/arpwatch.conf
%config(noreplace) %{_sysconfdir}/sysconfig/arpwatch

%attr(1775,-,arpwatch) %dir %{pkgstatedir}
%attr(0644,arpwatch,arpwatch) %verify(not md5 size mtime) %config(noreplace) %{pkgstatedir}/arp.dat
%attr(0644,arpwatch,arpwatch) %verify(not md5 size mtime) %config(noreplace) %{pkgstatedir}/arp.dat-
%attr(0600,arpwatch,arpwatch) %verify(not md5 size mtime) %ghost %{pkgstatedir}/arp.dat.new
%attr(0644,-,arpwatch) %verify(not md5 size mtime) %config(noreplace) %{pkgstatedir}/ethercodes.dat


%changelog
%autochangelog
