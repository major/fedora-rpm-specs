%global _hardened_build 1

Name:           hxtools
Version:        20150304
Release:        22%{?dist}
Summary:        A collection of several tools
# fd0ssh: LGPLv2 or LGPLv3
# git-forest: GPLv2+
# ofl: Public Domain, but LGPVv2 or LPGLv3 because of linking with libHX
# peicon: GPLv2+
# Automatically converted from old format: GPLv2+ or LGPLv2 or LGPLv3 - review is highly recommended.
License:        GPL-2.0-or-later OR LicenseRef-Callaway-LGPLv2 OR LGPL-3.0-only
URL:            http://inai.de/projects/hxtools/
# Signature is usually from the key with the fingerpint
# B56B 8B9D 9915 AA87 96ED  C013 DFFF 2CDB 19FC 338D
# Verify it like this:
# xzdec hxtools-%%{version}.tar.xz | gpg --verify hxtools-%%{version}.tar.asc -
Source0:        http://inai.de/files/hxtools/hxtools-%{version}.tar.xz
Source1:        http://inai.de/files/hxtools/hxtools-%{version}.tar.asc
Source2:        gpgkey-B56B8B9D9915AA8796EDC013DFFF2CDB19FC338D.gpg
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libHX-devel
# for sys/capability.h in printcaps.c
BuildRequires:  libcap-devel
# for libmount.h in suser/sysinfo.c
BuildRequires:  libmount-devel
# for pci/pci.h in suser/sysinfo.c
BuildRequires:  pciutils-devel
# for xcb/xcb.h in suser/sysinfo.c
BuildRequires:  libxcb-devel
# For source verification with gpgv
BuildRequires:  gpg perl-generators xz
BuildRequires: make
Provides:       fd0ssh
Provides:       git-forest
Provides:       ofl
Provides:       peicon


%description
hxtools contains several tools for different tasks written by Jan Engelhardt.

Currently only these tools are included in Fedora:

* fd0ssh - Pipe for password-over-stdin support to ssh
* git-forest - A text-based git tree visualizer
* ofl - Open file lister (replaces fuser and lsof -m)
* peicon - PE files icons extractor

%prep
xzcat %{SOURCE0} | gpgv --quiet --keyring %{SOURCE2} %{SOURCE1} -
%setup -q

%build
%configure --disable-silent-rules
%make_build

%install
%make_install

# remove unwanted files
# Using %%exclude in %%files pollutes the debuginfo package :-/
# This seems to be only build if some dependency is present
rm "%{buildroot}%{_bindir}/bin2c"
rm "%{buildroot}%{_bindir}/checkbrack"
rm "%{buildroot}%{_bindir}/clock_info"
rm "%{buildroot}%{_bindir}/clt2bdf"
rm "%{buildroot}%{_bindir}/cwdiff"
rm "%{buildroot}%{_bindir}/declone"
rm "%{buildroot}%{_bindir}/fxterm"
rm "%{buildroot}%{_bindir}/git-author-stat"
rm "%{buildroot}%{_bindir}/git-export-patch"
rm "%{buildroot}%{_bindir}/git-track"
rm "%{buildroot}%{_bindir}/googtts"
rm "%{buildroot}%{_bindir}/gpsh"
rm "%{buildroot}%{_bindir}/hcdplay"
rm "%{buildroot}%{_sysconfdir}/hxloginpref.conf"
rm "%{buildroot}%{_bindir}/man2html"
rm "%{buildroot}%{_bindir}/omixer"
rm "%{buildroot}%{_bindir}/oplay"
rm "%{buildroot}%{_bindir}/orec"
rm "%{buildroot}%{_bindir}/move_moov"
rm "%{buildroot}%{_bindir}/pesubst"
rm "%{buildroot}%{_bindir}/pmap_dirty"
rm "%{buildroot}%{_bindir}/qtar"
rm "%{buildroot}%{_bindir}/rot13"
rm "%{buildroot}%{_bindir}/spec-beautifier"
rm "%{buildroot}%{_bindir}/ssa2srt"
rm "%{buildroot}%{_bindir}/su1"
rm "%{buildroot}%{_bindir}/sysinfo"
rm "%{buildroot}%{_bindir}/tailhex"
rm "%{buildroot}%{_bindir}/wktimer"
rm "%{buildroot}%{_bindir}/xcp"
rm "%{buildroot}%{_libexecdir}/hxtools/bsvplay"
rm "%{buildroot}%{_libexecdir}/hxtools/cctypeinfo"
rm "%{buildroot}%{_libexecdir}/hxtools/clt2pbm"
rm "%{buildroot}%{_libexecdir}/hxtools/diff2php"
rm "%{buildroot}%{_libexecdir}/hxtools/doxygen-kerneldoc-filter"
rm "%{buildroot}%{_libexecdir}/hxtools/extract_d3pkg"
rm "%{buildroot}%{_libexecdir}/hxtools/extract_dxhog"
rm "%{buildroot}%{_libexecdir}/hxtools/extract_f3pod"
rm "%{buildroot}%{_libexecdir}/hxtools/extract_qupak"
rm "%{buildroot}%{_libexecdir}/hxtools/fnt2bdf"
rm "%{buildroot}%{_libexecdir}/hxtools/git-blame-stats"
rm "%{buildroot}%{_libexecdir}/hxtools/git-new-root"
rm "%{buildroot}%{_libexecdir}/hxtools/git-revert-stats"
rm "%{buildroot}%{_libexecdir}/hxtools/logontime"
rm "%{buildroot}%{_libexecdir}/hxtools/mailsplit"
rm "%{buildroot}%{_libexecdir}/hxtools/mod2ogg"
rm "%{buildroot}%{_libexecdir}/hxtools/netload"
rm "%{buildroot}%{_libexecdir}/hxtools/paddrspacesize"
rm "%{buildroot}%{_libexecdir}/hxtools/pcmdiff"
rm "%{buildroot}%{_libexecdir}/hxtools/printcaps"
rm "%{buildroot}%{_libexecdir}/hxtools/proc_iomem_count"
rm "%{buildroot}%{_libexecdir}/hxtools/proc_stat_signal_decode"
rm "%{buildroot}%{_libexecdir}/hxtools/psthreads"
rm "%{buildroot}%{_libexecdir}/hxtools/qplay"
rm "%{buildroot}%{_libexecdir}/hxtools/recursive_lower"
rm "%{buildroot}%{_libexecdir}/hxtools/rezip"
rm "%{buildroot}%{_libexecdir}/hxtools/shared.pm"
rm "%{buildroot}%{_libexecdir}/hxtools/sourcefuncsize"
rm "%{buildroot}%{_libexecdir}/hxtools/stxdb"
rm "%{buildroot}%{_libexecdir}/hxtools/utmp_register"
rm "%{buildroot}%{_libexecdir}/hxtools/vcsaview"
rm "%{buildroot}%{_libexecdir}/hxtools/vfontas"
rm "%{buildroot}%{_libexecdir}/hxtools/proc_stat_parse"
rm "%{buildroot}%{_datadir}/hxtools/gitconfig"
rm "%{buildroot}%{_datadir}/hxtools/hxloginpref.conf"
rm "%{buildroot}%{_datadir}/kbd/consolefonts/ega437_8x14.fnt"
rm "%{buildroot}%{_datadir}/kbd/consolefonts/ega437_8x16.fnt"
rm "%{buildroot}%{_datadir}/kbd/consolefonts/ega437_8x8.fnt"
rm "%{buildroot}%{_datadir}/kbd/consolefonts/gotik-textura.fnt"
rm "%{buildroot}%{_datadir}/kbd/keymaps/i386/qwerty/us_jng.map"
rm "%{buildroot}%{_datadir}/kbd/keymaps/i386/qwerty/us_jng_vaiou3.map"
rm "%{buildroot}%{_datadir}/kbd/keymaps/i386/qwertz/de_jng.map"
rm "%{buildroot}%{_datadir}/kbd/unimaps/cp437AB.uni"
rm "%{buildroot}%{_datadir}/kbd/consolefonts/ital.fnt"
rm "%{buildroot}%{_datadir}/fonts/misc/mux.pcf.gz"
rm "%{buildroot}%{_datadir}/fonts/misc/rhx.pcf.gz"
rm "%{buildroot}%{_datadir}/fonts/misc/tosh.pcf.gz"
rm "%{buildroot}%{_datadir}/kbd/consolefonts/A1.fnt"
rm "%{buildroot}%{_datadir}/kbd/consolefonts/B1.fnt"
rm "%{buildroot}%{_datadir}/kbd/consolefonts/ati.fnt"
rm "%{buildroot}%{_datadir}/kbd/consolefonts/mux.fnt"
rm "%{buildroot}%{_datadir}/kbd/consolefonts/neuropol.fnt"
rm "%{buildroot}%{_datadir}/kbd/consolefonts/nvidia.fnt"
rm "%{buildroot}%{_datadir}/kbd/consolefonts/rhx.fnt"
rm "%{buildroot}%{_datadir}/kbd/consolefonts/tosh.fnt"
rm "%{buildroot}%{_datadir}/hxtools/hxtools_bashrc.bash"
rm "%{buildroot}%{_datadir}/hxtools/hxtools_dircolors"
rm "%{buildroot}%{_datadir}/hxtools/hxtools_profile.bash"
rm "%{buildroot}%{_datadir}/hxtools/rfc2307bis-utf8.schema"
rm "%{buildroot}%{_mandir}/man1/bsvplay.1"*
rm "%{buildroot}%{_mandir}/man1/bin2c.1"*
rm "%{buildroot}%{_mandir}/man1/cctypeinfo.1"*
rm "%{buildroot}%{_mandir}/man1/checkbrack.1"*
rm "%{buildroot}%{_mandir}/man1/clock_info.1"*
rm "%{buildroot}%{_mandir}/man1/clt2bdf.1"*
rm "%{buildroot}%{_mandir}/man1/clt2pbm.1"*
rm "%{buildroot}%{_mandir}/man1/cwdiff.1"*
rm "%{buildroot}%{_mandir}/man1/declone.1"*
rm "%{buildroot}%{_mandir}/man1/diff2php.1"*
rm "%{buildroot}%{_mandir}/man1/extract_d3pkg.1"*
rm "%{buildroot}%{_mandir}/man1/extract_dxhog.1"*
rm "%{buildroot}%{_mandir}/man1/extract_f3pod.1"*
rm "%{buildroot}%{_mandir}/man1/extract_qupak.1"*
rm "%{buildroot}%{_mandir}/man1/fnt2bdf.1"*
rm "%{buildroot}%{_mandir}/man1/fxterm.1"*
rm "%{buildroot}%{_mandir}/man1/git-author-stat.1"*
rm "%{buildroot}%{_mandir}/man1/git-export-patch.1"*
rm "%{buildroot}%{_mandir}/man1/git-revert-stats.1"*
rm "%{buildroot}%{_mandir}/man1/git-track.1"*
rm "%{buildroot}%{_mandir}/man1/hcdplay.1"*
rm "%{buildroot}%{_mandir}/man1/mailsplit.1"*
rm "%{buildroot}%{_mandir}/man1/man2html.1"*
rm "%{buildroot}%{_mandir}/man1/mod2ogg.1"*
rm "%{buildroot}%{_mandir}/man1/omixer.1"*
rm "%{buildroot}%{_mandir}/man1/oplay.1"*
rm "%{buildroot}%{_mandir}/man1/orec.1"*
rm "%{buildroot}%{_mandir}/man1/pcmdiff.1"*
rm "%{buildroot}%{_mandir}/man1/pesubst.1"*
rm "%{buildroot}%{_mandir}/man1/psthreads.1"*
rm "%{buildroot}%{_mandir}/man1/qplay.1"*
rm "%{buildroot}%{_mandir}/man1/qtar.1"*
rm "%{buildroot}%{_mandir}/man1/recursive_lower.1"*
rm "%{buildroot}%{_mandir}/man1/rot13.1"*
rm "%{buildroot}%{_mandir}/man1/sourcefuncsize.1"*
rm "%{buildroot}%{_mandir}/man1/spec-beautifier.1"*
rm "%{buildroot}%{_mandir}/man1/ssa2srt.1"*
rm "%{buildroot}%{_mandir}/man1/stxdb.1"*
rm "%{buildroot}%{_mandir}/man1/sysinfo.1"*
rm "%{buildroot}%{_mandir}/man1/tailhex.1"*
rm "%{buildroot}%{_mandir}/man1/vfontas.1"*
rm "%{buildroot}%{_mandir}/man1/wktimer.1"*
rm "%{buildroot}%{_mandir}/man1/xcp.1"*
rm "%{buildroot}%{_mandir}/man7/hxtools.7"*
rm "%{buildroot}%{_mandir}/man8/logontime.8"*
rm "%{buildroot}%{_mandir}/man8/netload.8"*
rm "%{buildroot}%{_mandir}/man8/printcaps.8"*
rm "%{buildroot}%{_mandir}/man8/utmp_register.8"*
rm "%{buildroot}%{_mandir}/man8/vcsaview.8"*
rm "%{buildroot}%{_mandir}/man8/xfs_irecover.8"*

%files
%license LICENSE.GPL2 LICENSE.GPL3 LICENSE.WTFPL
%doc LICENSES.txt
%{_bindir}/git-forest
%{_bindir}/ofl
%{_libexecdir}/hxtools/fd0ssh
%{_libexecdir}/hxtools/peicon
%{_mandir}/man1/fd0ssh.1*
%{_mandir}/man1/git-forest.1*
%{_mandir}/man1/ofl.1*
%{_mandir}/man1/peicon.1*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20150304-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 20150304-21
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20150304-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20150304-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20150304-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20150304-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20150304-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20150304-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20150304-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20150304-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20150304-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20150304-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20150304-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20150304-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20150304-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20150304-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20150304-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20150304-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20150304-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20150304-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20150304-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jul 25 2015 Christopher Meng <rpm@cicku.me> - 20150304-1
- Update to 20150304

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20150221-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 20150221-1
- Update to new release
- Use %%license
- Update removed tools
- Properly mention peicon

* Sun Nov 09 2014 Till Maas <opensource@till.name> - 20140703-4
- Harden build
- Add automatic GPG key verification

* Mon Aug 18 2014 Till Maas <opensource@till.name> - 20140703-3
- Add missing GPG signature
- Fix man page removal

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20140703-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 21 2014 Christopher Meng <rpm@cicku.me> - 20140703-1
- Update to 20140703

* Thu Jun 19 2014 Christopher Meng <rpm@cicku.me> - 20140325-1
- Update to 20140325
- Add peicon.
- Fix conflicting types include on AArch64.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130605-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130605-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 03 2013 Christopher Meng <rpm@cicku.me> - 20130605-1
- Update to 20130605
- Add git-forest

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120514-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120514-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 06 2012 Till Maas <opensource@till.name> - 20120514-1
- Update to new release
- Update URL and Source0/1
- Update BuildRequires

* Wed Mar 21 2012 Till Maas <opensource@till.name> - 20120107-1
- Update to new release
- Remove upstreamed patch

* Thu Nov 24 2011 Till Maas <opensource@till.name> - 20110721-2
- Update BR: use automake instead of autoconf
- Use %% for rpm macros in comments

* Fri Jul 22 2011 Till Maas <opensource@till.name> - 20110721-1
- Update to new release
- Add patch to make newns build (missing _GNU_SOURCE)

* Thu May 19 2011 Till Maas <opensource@till.name> - 20110509-1
- Update to new release
- cleanup spec
- add BR: autoconf
- add BR: libcaps-devel

* Wed Mar 09 2011 Till Maas <opensource@till.name> - 20110308-2
- Include license files

* Wed Mar 09 2011 Till Maas <opensource@till.name> - 20110308-1
- Update to new release

* Mon Dec 27 2010 Till Maas <opensource@till.name> - 20101227-1
- Initial spec with only the programs needed by pam_mount
