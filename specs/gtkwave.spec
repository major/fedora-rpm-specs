Summary:	Waveform Viewer
Name:		gtkwave
Version:	3.3.121
Release:	2%{?dist}
License:	GPL-2.0-or-later
URL:		http://gtkwave.sourceforge.net/
Source0:	http://gtkwave.sourceforge.net/gtkwave-gtk3-%{version}.tar.gz
Patch0:		gtkwave-3.3.121-appdata.patch
Patch1:		gtkwave-3.3.121-gcc15.patch
BuildRequires:	bzip2-devel
BuildRequires:	coreutils
BuildRequires:	desktop-file-utils
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	flex
BuildRequires:	gedit
BuildRequires:	gperf
BuildRequires:	hardlink
BuildRequires:	pkgconfig(gio-unix-2.0) >= 2.0
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.0.0
BuildRequires:	pkgconfig(gtk+-unix-print-3.0)
BuildRequires:	pkgconfig(libtirpc)
BuildRequires:	hicolor-icon-theme
BuildRequires:	Judy-devel
BuildRequires:	libappstream-glib
BuildRequires:	make
BuildRequires:	shared-mime-info
BuildRequires:	tcl-devel >= 8.4
BuildRequires:	tk-devel
BuildRequires:	xz-devel
BuildRequires:	zlib-devel
# Dependencies
Recommends:	gedit
Requires:	hicolor-icon-theme
Requires:	shared-mime-info

# Judy-devel missing on EL-8 s390x
# https://lists.fedoraproject.org/archives/list/epel-devel@lists.fedoraproject.org/thread/O4JISZYIVXXPIB6OZIE2TNKR2EIQZWBL/
%if 0%{?el8}
ExcludeArch:	s390x
%endif

%description
GTKWave is a waveform viewer that can view VCD files produced by most Verilog
simulation tools, as well as LXT files produced by certain Verilog simulation
tools.

%prep
%setup -q -n gtkwave-gtk3-%{version}

# Fix broken appdata file
# https://github.com/gtkwave/gtkwave/pull/387
%patch -P 0

# Port to gcc 15
# https://github.com/gtkwave/gtkwave/pull/406
%patch -P 1

%build
%configure \
	--disable-dependency-tracking \
	--disable-mime-update \
	--enable-gtk3 \
	--enable-judy \
	--with-gsettings \
	--with-tirpc
make %{?_smp_mflags}

%install
make install \
	DESTDIR=%{buildroot} \
	pkgdatadir=%{_pkgdocdir} \
	INSTALL="install -p"

# Icons and desktop entry
desktop-file-install --vendor "" --dir %{buildroot}%{_datadir}/applications \
	share/applications/gtkwave.desktop
install -D -m 644 -p share/icons/gnome/16x16/mimetypes/gtkwave.png \
	%{buildroot}%{_datadir}/icons/hicolor/16x16/apps/gtkwave.png
install -D -m 644 -p share/icons/gnome/32x32/mimetypes/gtkwave.png \
	%{buildroot}%{_datadir}/icons/hicolor/32x32/apps/gtkwave.png
install -D -m 644 -p share/icons/gnome/48x48/mimetypes/gtkwave.png \
	%{buildroot}%{_datadir}/icons/hicolor/48x48/apps/gtkwave.png
install -D -m 644 -p share/icons/gtkwave_256x256x32.png \
	%{buildroot}%{_datadir}/icons/hicolor/256x256/apps/gtkwave.png

# Appdata
install -D -m 644 -p share/appdata/io.github.gtkwave.GTKWave.metainfo.xml \
	%{buildroot}%{_datadir}/appdata/io.github.gtkwave.GTKWave.metainfo.xml

# Include extra docs
install -p -m 644 AUTHORS %{buildroot}%{_pkgdocdir}/
install -p -m 644 ChangeLog %{buildroot}%{_pkgdocdir}/

# hardlink identical icons together
hardlink -cv %{buildroot}%{_datadir}/icons/

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/io.github.gtkwave.GTKWave.metainfo.xml

%files
%license COPYING LICENSE.TXT
%doc %{_pkgdocdir}/
%{_bindir}/evcd2vcd
%{_bindir}/fst2vcd
%{_bindir}/fstminer
%{_bindir}/gtkwave
%{_bindir}/lxt2miner
%{_bindir}/lxt2vcd
%{_bindir}/rtlbrowse
%{_bindir}/shmidcat
%{_bindir}/twinwave
%{_bindir}/vcd2fst
%{_bindir}/vcd2lxt
%{_bindir}/vcd2lxt2
%{_bindir}/vcd2vzt
%{_bindir}/vzt2vcd
%{_bindir}/vztminer
%{_bindir}/xml2stems
%{_datadir}/appdata/io.github.gtkwave.GTKWave.metainfo.xml
%{_datadir}/applications/gtkwave.desktop
%{_datadir}/glib-2.0/schemas/com.geda.gtkwave.gschema.xml
%dir %{_datadir}/icons/gnome/
%dir %{_datadir}/icons/gnome/16x16/
%dir %{_datadir}/icons/gnome/16x16/mimetypes/
%{_datadir}/icons/gnome/16x16/mimetypes/gnome-mime-application-vnd.gtkwave-ae2.png
%{_datadir}/icons/gnome/16x16/mimetypes/gnome-mime-application-vnd.gtkwave-aet.png
%{_datadir}/icons/gnome/16x16/mimetypes/gnome-mime-application-vnd.gtkwave-evcd.png
%{_datadir}/icons/gnome/16x16/mimetypes/gnome-mime-application-vnd.gtkwave-fst.png
%{_datadir}/icons/gnome/16x16/mimetypes/gnome-mime-application-vnd.gtkwave-ghw.png
%{_datadir}/icons/gnome/16x16/mimetypes/gnome-mime-application-vnd.gtkwave-gtkw.png
%{_datadir}/icons/gnome/16x16/mimetypes/gnome-mime-application-vnd.gtkwave-lx2.png
%{_datadir}/icons/gnome/16x16/mimetypes/gnome-mime-application-vnd.gtkwave-lxt.png
%{_datadir}/icons/gnome/16x16/mimetypes/gnome-mime-application-vnd.gtkwave-lxt2.png
%{_datadir}/icons/gnome/16x16/mimetypes/gnome-mime-application-vnd.gtkwave-vcd.png
%{_datadir}/icons/gnome/16x16/mimetypes/gnome-mime-application-vnd.gtkwave-vzt.png
%{_datadir}/icons/gnome/16x16/mimetypes/gtkwave.png
%dir %{_datadir}/icons/gnome/32x32/
%dir %{_datadir}/icons/gnome/32x32/mimetypes/
%{_datadir}/icons/gnome/32x32/mimetypes/gnome-mime-application-vnd.gtkwave-ae2.png
%{_datadir}/icons/gnome/32x32/mimetypes/gnome-mime-application-vnd.gtkwave-aet.png
%{_datadir}/icons/gnome/32x32/mimetypes/gnome-mime-application-vnd.gtkwave-evcd.png
%{_datadir}/icons/gnome/32x32/mimetypes/gnome-mime-application-vnd.gtkwave-fst.png
%{_datadir}/icons/gnome/32x32/mimetypes/gnome-mime-application-vnd.gtkwave-ghw.png
%{_datadir}/icons/gnome/32x32/mimetypes/gnome-mime-application-vnd.gtkwave-gtkw.png
%{_datadir}/icons/gnome/32x32/mimetypes/gnome-mime-application-vnd.gtkwave-lx2.png
%{_datadir}/icons/gnome/32x32/mimetypes/gnome-mime-application-vnd.gtkwave-lxt.png
%{_datadir}/icons/gnome/32x32/mimetypes/gnome-mime-application-vnd.gtkwave-lxt2.png
%{_datadir}/icons/gnome/32x32/mimetypes/gnome-mime-application-vnd.gtkwave-vcd.png
%{_datadir}/icons/gnome/32x32/mimetypes/gnome-mime-application-vnd.gtkwave-vzt.png
%{_datadir}/icons/gnome/32x32/mimetypes/gtkwave.png
%dir %{_datadir}/icons/gnome/48x48/
%dir %{_datadir}/icons/gnome/48x48/mimetypes/
%{_datadir}/icons/gnome/48x48/mimetypes/gnome-mime-application-vnd.gtkwave-ae2.png
%{_datadir}/icons/gnome/48x48/mimetypes/gnome-mime-application-vnd.gtkwave-aet.png
%{_datadir}/icons/gnome/48x48/mimetypes/gnome-mime-application-vnd.gtkwave-evcd.png
%{_datadir}/icons/gnome/48x48/mimetypes/gnome-mime-application-vnd.gtkwave-fst.png
%{_datadir}/icons/gnome/48x48/mimetypes/gnome-mime-application-vnd.gtkwave-ghw.png
%{_datadir}/icons/gnome/48x48/mimetypes/gnome-mime-application-vnd.gtkwave-gtkw.png
%{_datadir}/icons/gnome/48x48/mimetypes/gnome-mime-application-vnd.gtkwave-lx2.png
%{_datadir}/icons/gnome/48x48/mimetypes/gnome-mime-application-vnd.gtkwave-lxt.png
%{_datadir}/icons/gnome/48x48/mimetypes/gnome-mime-application-vnd.gtkwave-lxt2.png
%{_datadir}/icons/gnome/48x48/mimetypes/gnome-mime-application-vnd.gtkwave-vcd.png
%{_datadir}/icons/gnome/48x48/mimetypes/gnome-mime-application-vnd.gtkwave-vzt.png
%{_datadir}/icons/gnome/48x48/mimetypes/gtkwave.png
%{_datadir}/icons/gtkwave_256x256x32.png
%{_datadir}/icons/gtkwave_files_256x256x32.png
%{_datadir}/icons/gtkwave_savefiles_256x256x32.png
%{_datadir}/icons/hicolor/16x16/apps/gtkwave.png
%{_datadir}/icons/hicolor/32x32/apps/gtkwave.png
%{_datadir}/icons/hicolor/48x48/apps/gtkwave.png
%{_datadir}/icons/hicolor/256x256/apps/gtkwave.png
%{_datadir}/icons/hicolor/scalable/apps/gtkwave.svg
%{_datadir}/mime/packages/x-gtkwave-extension-ae2.xml
%{_datadir}/mime/packages/x-gtkwave-extension-aet.xml
%{_datadir}/mime/packages/x-gtkwave-extension-evcd.xml
%{_datadir}/mime/packages/x-gtkwave-extension-fst.xml
%{_datadir}/mime/packages/x-gtkwave-extension-ghw.xml
%{_datadir}/mime/packages/x-gtkwave-extension-gtkw.xml
%{_datadir}/mime/packages/x-gtkwave-extension-lx2.xml
%{_datadir}/mime/packages/x-gtkwave-extension-lxt.xml
%{_datadir}/mime/packages/x-gtkwave-extension-lxt2.xml
%{_datadir}/mime/packages/x-gtkwave-extension-vcd.xml
%{_datadir}/mime/packages/x-gtkwave-extension-vzt.xml
%{_mandir}/man1/evcd2vcd.1*
%{_mandir}/man1/fst2vcd.1*
%{_mandir}/man1/fstminer.1*
%{_mandir}/man1/gtkwave.1*
%{_mandir}/man1/lxt2miner.1*
%{_mandir}/man1/lxt2vcd.1*
%{_mandir}/man1/rtlbrowse.1*
%{_mandir}/man1/shmidcat.1*
%{_mandir}/man1/twinwave.1*
%{_mandir}/man1/vcd2fst.1*
%{_mandir}/man1/vcd2lxt.1*
%{_mandir}/man1/vcd2lxt2.1*
%{_mandir}/man1/vcd2vzt.1*
%{_mandir}/man1/vzt2vcd.1*
%{_mandir}/man1/vztminer.1*
%{_mandir}/man1/xml2stems.1*
%{_mandir}/man5/gtkwaverc.5*

%changelog
* Wed Jan 15 2025 Paul Howarth <paul@city-fan.org> - 3.3.121-2
- Port to gcc 15 (GH#406)

* Wed Oct  9 2024 Paul Howarth <paul@city-fan.org> - 3.3.121-1
- Update to 3.3.121
  - Add launchable tag in io.github.gtkwave.GTKWave.metainfo.xml
  - Fix memory leak on name in build_hierarchy_array()
  - Fix memory leak in ptranslate/ttranslate
  - Fix case of missing newline at EOF for VCD loaders
  - Add escape handling state machine for vars in FST loader
  - Remove escape check on coalesce in FST loader
  - CreateFileMapping() warning fix for Win32 compiles
  - Integrate gtkwave/pull/376 and gtkwave/pull/377 updates to the FST loader
    for Windows and warnings fixes
  - Clang warning fixes in fstapi.c on dynamic arrays

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.119-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Mar 25 2024 Paul Howarth <paul@city-fan.org> - 3.3.119-1
- Update to 3.3.119
  - Remove FST_DO_MISALIGNED_OPS
  - Update lz4 to current version from GitHub
  - Change LZ4_compress to LZ4_compress_default
  - Update libghw.c/.h to latest upstream version
  - Fix for -Wsign-compare in fstapi.c
  - Security fixes for GHW
  - Fix left shift of a negative number warning in fstapi.c
  - Fix ctrl-A behavior for SST filter entry
  - Fix for bad shmat return value in main.c
- Hardlink identical icons together to save space

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.118-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.118-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan  9 2024 Paul Howarth <paul@city-fan.org> - 3.3.118-1
- Update to 3.3.118
  - Update xml2stems to handle newer "loc" vs. "fl" xml tags
  - Change preg_regex_c_1 decl to use regex_t* as datatype
  - Move gtkwave.appdata.xml to io.github.gtkwave.GTKWave.metainfo.xml
  - Fixed popen security advisories:
    - TALOS-2023-1786 (CVE-2023-35963, CVE-2023-35960, CVE-2023-35964,
		       CVE-2023-35959, CVE-2023-35961, CVE-2023-35962)
  - Fixed FST security advisories:
    - TALOS-2023-1777 (CVE-2023-32650)
    - TALOS-2023-1783 (CVE-2023-35704, CVE-2023-35703, CVE-2023-35702)
    - TALOS-2023-1785 (CVE-2023-35956, CVE-2023-35957, CVE-2023-35958,
		       CVE-2023-35955)
    - TALOS-2023-1789 (CVE-2023-35969, CVE-2023-35970)
    - TALOS-2023-1790 (CVE-2023-35992)
    - TALOS-2023-1791 (CVE-2023-35994, CVE-2023-35996, CVE-2023-35997,
		       CVE-2023-35995)
    - TALOS-2023-1792 (CVE-2023-35128)
    - TALOS-2023-1793 (CVE-2023-36747, CVE-2023-36746)
    - TALOS-2023-1797 (CVE-2023-36864)
    - TALOS-2023-1798 (CVE-2023-36915, CVE-2023-36916)
  - Fixed evcd2vcd security advisories:
    - TALOS-2023-1803 (CVE-2023-34087)
  - Fixed VCD security advisories:
    - TALOS-2023-1804 (CVE-2023-37416, CVE-2023-37419, CVE-2023-37420,
		       CVE-2023-37418, CVE-2023-37417)
    - TALOS-2023-1805 (CVE-2023-37447, CVE-2023-37446, CVE-2023-37445,
		       CVE-2023-37444, CVE-2023-37442, CVE-2023-37443)
    - TALOS-2023-1806 (CVE-2023-37576, CVE-2023-37577, CVE-2023-37573,
		       CVE-2023-37578, CVE-2023-37575, CVE-2023-37574)
    - TALOS-2023-1807 (CVE-2023-37921, CVE-2023-37923, CVE-2023-37922)
  - Fixed VZT security advisories:
    - TALOS-2023-1810 (CVE-2023-37282)
    - TALOS-2023-1811 (CVE-2023-36861)
    - TALOS-2023-1812 (CVE-2023-38618, CVE-2023-38621, CVE-2023-38620,
		       CVE-2023-38619, CVE-2023-38623, CVE-2023-38622)
    - TALOS-2023-1813 (CVE-2023-38649, CVE-2023-38648)
    - TALOS-2023-1814 (CVE-2023-38651, CVE-2023-38650)
    - TALOS-2023-1815 (CVE-2023-38653, CVE-2023-38652)
    - TALOS-2023-1816 (CVE-2023-35004)
    - TALOS-2023-1817 (CVE-2023-39235, CVE-2023-39234)
  - Fixed LXT2 security advisories:
    - TALOS-2023-1818 (CVE-2023-39273, CVE-2023-39271, CVE-2023-39274,
		       CVE-2023-39275, CVE-2023-39272, CVE-2023-39270)
    - TALOS-2023-1819 (CVE-2023-34436)
    - TALOS-2023-1820 (CVE-2023-39316, CVE-2023-39317)
    - TALOS-2023-1821 (CVE-2023-35057)
    - TALOS-2023-1822 (CVE-2023-35989)
    - TALOS-2023-1823 (CVE-2023-38657)
    - TALOS-2023-1824 (CVE-2023-39413, CVE-2023-39414)
    - TALOS-2023-1826 (CVE-2023-39443, CVE-2023-39444)
    - TALOS-2023-1827 (CVE-2023-38583)

* Mon Aug 14 2023 Paul Howarth <paul@city-fan.org> - 3.3.117-1
- Update to 3.3.117
  - Fix stems reader processing code broken in 3.3.114

* Sun Jul 23 2023 Paul Howarth <paul@city-fan.org> - 3.3.116-1
- Update to 3.3.116
  - Fix manpage/odt for vcd2fst command switch documentation for zlibpack
  - Add GDK_WINDOWING_WAYLAND check for gdkwayland.h header usage
  - Change sprintf to snprintf in fstapi.c
  - Fix init crash on show_base_symbols enabled

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.115-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Apr  3 2023 Paul Howarth <paul@city-fan.org> - 3.3.115-1
- Update to 3.3.115
  - Fix VZT reader with -fstrict-aliasing
  - Fix use_multi_state condition in vzt_write.c
  - Fix for UNDEF vs strings at start of a vzt file
  - Fix sleep() time scaling redefine for mingw
  - Use MapViewOfFileEx for mmap on Windows (fstapi)
  - Define FST_DO_MISALIGNED_OPS on AArch64 (fstapi)
  - Fixed attrbegin short length problem

* Sun Feb 19 2023 Paul Howarth <paul@city-fan.org> - 3.3.114-1
- Update to 3.3.114
  - Buffer overflow fixes in FST reader

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.113-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Oct  5 2022 Paul Howarth <paul@city-fan.org> - 3.3.113-1
- Update to 3.3.113
  - Fix high CPU utilization when nothing is happening (GH#117)

* Tue Oct  4 2022 Paul Howarth <paul@city-fan.org> - 3.3.112-1
- Update to 3.3.112
  - VCD reader fixes for unnamed Icarus begin blocks
  - String data type crash fix in fst.c
- Use SPDX-format license tag

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.111-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Feb  9 2022 Paul Howarth <paul@city-fan.org> - 3.3.111-3
- Address excessive CPU usage under Wayland (#2052437)
  https://github.com/gtkwave/gtkwave/issues/117

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.111-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep  7 2021 Paul Howarth <paul@city-fan.org> - 3.3.111-1
- Update to 3.3.111
  - Rendering fix for filled rectangles and line caps in Cairo
  - Fix in fstapi for read start limit time
  - Use GtkSearchEntry in SST
  - Convert entrybox to use dialog box
  - Entrybox: use default response instead of signal handler
  - Updated show-change widget
  - Fix xml2stems when begin blocks are in functions
  - Skip over decimal point in timescale in viewer

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.110-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jun 20 2021 Paul Howarth <paul@city-fan.org> - 3.3.110-1
- Update to 3.3.110
  - gtk_ctree_node_moveto bugfix in SST
  - MSVC compiler fix for fstapi
  - Update xml2stems and rtlbrowse to support generate
  - Removed ghwdump from the distribution (now provided with GHDL)
  - Fix for when WAVE_GTK3_GESTURE_ZOOM_USES_GTK_PHASE_CAPTURE is disabled
  - Integrated blank window fixes from Fedora
  - Minor scan-build fixes

* Wed May 19 2021 Paul Howarth <paul@city-fan.org> - 3.3.108-3
- Silence some compiler warnings, fixes broken GUI with -O2
  https://bugzilla.redhat.com/show_bug.cgi?id=1956191
  https://github.com/gtkwave/gtkwave/issues/62

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.108-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 30 2020 Paul Howarth <paul@city-fan.org> - 3.3.108-1
- Update to 3.3.108
  - Added View/Leading Zero Removal toggle item also controlled by lz_removal
    rc var
  - User submitted patch using gtk_widget_get_scale_factor()
  - Add include of X11/X.h for Arch Linux
  - Fix VZT writer crash when dumpoff is invoked before first timestep
  - Fix convert_ffo(), which scanned in wrong direction
  - Fix use after free in fstapi.c

* Mon Oct  5 2020 Paul Howarth <paul@city-fan.org> - 3.3.107-1
- Update to 3.3.107
  - Fix left shift overflow in cvt_fpsudec for fixed point
  - Added Find First One trace type options
  - Fixed bug in Show-Change All Highlighted

* Sat Aug  8 2020 Paul Howarth <paul@city-fan.org> - 3.3.106-1
- Update to 3.3.106
  - Fix Shift-Up/Down highlight to traverse inside groups
  - Resync ghwlib to handle unbounded array

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.105-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul  6 2020 Paul Howarth <paul@city-fan.org> - 3.3.105-1
- Update to 3.3.105
  - Fix bad (void) of is_closing in fstDestroyMmaps when using Cygwin or MinGW
  - Fix left shift overflow in cvt_fpsdec()
  - Add in missing file/translate/process filter for reals
  - Fix for bitvec merging in GHW so integers arrays can be viewed
  - Added Shift-Up/Down highlight with scroll in order to assist with
    left/right arrow based transition movement
  - Fix Show Wave Highlight so it is not dependent on Show Grid
  - Fix negative MSBs on VCD loaders for vectors
  - Fix getpwuid() null pointer exception
  - Add missing recursion case to treenamefix()
  - Fix lock/unlock misuse of pthread mutexes across threads
  - Examine env var $HOME for home dir on geteuid failure
  - Fix blurring on use_fat_lines rc variable usage

* Sun May 17 2020 Paul Howarth <paul@city-fan.org> - 3.3.104-2
- Use gtk3 toolkit rather than gtk2 (#1836549)
- Own directories under and including %%{_datadir}/icons/gnome/ to avoid
  dependency on gnome-icon-theme, which is not available on EL-8

* Fri Feb 14 2020 Paul Howarth <paul@city-fan.org> - 3.3.104-1
- Update to 3.3.104
  - Added support for loading .vf files (provided FSDB reader libraries are
    enabled)
  - Added support for dumping variable types in vcd saver, not just using
    "wire" for non-reals/strings
  - Fix for uninitialized values at time 0 for FST, FSDB loaders

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.103-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 22 2020 Paul Howarth <paul@city-fan.org> - 3.3.103-2
- Fix FTBFS with GCC 10

* Mon Nov 11 2019 Paul Howarth <paul@city-fan.org> - 3.3.103-1
- Update to 3.3.103
  - Fix MAP_FAILED missing for MinGW
  - Fix to make the coloration red on 'u' traces (bug from Dinotrace-like
    rendering in 3.3.96)
  - Typo fix on missing group start on vectors

* Wed Oct  2 2019 Paul Howarth <paul@city-fan.org> - 3.3.102-1
- Update to 3.3.102
  - Remove redundant TREE_VHDL_ST_PACKAGE from SST exclude
  - Added addCommentTracesFromList tcl command from user patch
  - Harden savefile loader for missing group start on vectors
  - Preliminary VHDL support for wlf2vcd
  - Add missing return value checks on mmap() in FST writer

* Mon Aug 19 2019 Paul Howarth <paul@city-fan.org> - 3.3.101-3
- Weaken dependency on gedit where possible (#1743019)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.101-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 23 2019 Paul Howarth <paul@city-fan.org> - 3.3.101-1
- Update to 3.3.101
  - Added gtkwave::getFacDir, gtkwave::getFacVtype and gtkwave::getFacDtype
    Tcl accessor functions, which operate similarly to gtkwave::getFacName
  - Pair $end with $dumpvars in VCD writers
  - Make %%.16g printing in baseconvert.c more resistant to power of 10
    roundoff errors
  - Remove register keyword where applicable as it is deprecated
  - Added --saveonexit gtkwave command line option

* Fri Mar 22 2019 Paul Howarth <paul@city-fan.org> - 3.3.100-1
- Update to 3.3.100
  - FSDB fix for variable declarations of array of reals
  - Added Real, Time, Enum, and Popcnt flags to Edit/Show-Change
  - Ensure Show-Change regenerates analog traces
  - Added braces inside Tcl source command to allow spaces in filenames for
    Tcl scripts

* Sun Feb 10 2019 Paul Howarth <paul@city-fan.org> - 3.3.99-1
- Update to 3.3.99
  - Added visible single bit glitches as a yellow dot (if enabled with
    --rcvar 'vcd_preserve_glitches on')
  - Fixed print routine broken by bsearch_trunc() optimization in version 3.3.96

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.98-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan  2 2019 Paul Howarth <paul@city-fan.org> - 3.3.98-1
- Update to 3.3.98
  - Removed pccts and vermin; use xml2stems instead

* Mon Nov 26 2018 Paul Howarth <paul@city-fan.org> - 3.3.97-1
- Update to 3.3.97
  - Need to set menu_wlist entry NULL on gtk_widget_destroy()
  - Fix on vtype()/vtype2() to detect 'x' and make the coloration red on
    newly-displayed traces (bug new from Dinotrace-like rendering in 3.3.96)

* Mon Nov 19 2018 Paul Howarth <paul@city-fan.org> - 3.3.96-1
- Update to 3.3.96
  - Changed to standardized zoom in/out/full hotkeys
  - Added time backtracking warning (for partial mode) to lxt2vcd
  - VCD time backtracking fix (not for interactive mode)
  - Added drag_failed handling (can press ESC) to DnD operations
  - Prevent missing file in savefile from causing savefile to be read as VCD by
    mistake
  - Changed to Dinotrace-like 0s/1s rendering for bit vectors so values can be
    discerned without seeing the full value text
  - Removed unneeded pango_layout_get_extents() inside call for
    font_engine_draw_string()
  - Changed bsearch_trunc() to run in constant time when monospace fonts are in
    use
  - Added missing GDK_SCROLL_MASK to signal area (need for gtk3, but not for
    other versions for some reason)
- Add patch to fix build with GTK 2.20 on Fedora 13 (missing GDK_KEY_equal)

* Thu Oct 11 2018 Paul Howarth <paul@city-fan.org> - 3.3.95-1
- Update to 3.3.95
  - Added fflush on stdout for help text as fix for possible stdout problem
    with mingw/msys shells
  - Added preliminary support for Time datatype
  - Warnings fixes for Verilator integration
  - Fixed install_proc_filter usage for Tcl invocation
  - Change integer type to "integer" in SST to differentiate it from sv ints
  - Premiminary support for enum tables embedded in FST files

* Fri Sep  7 2018 Paul Howarth <paul@city-fan.org> - 3.3.94-1
- Update to 3.3.94
  - Applied ghwlib.c patch for dealing with null ranges
  - Added second chance algorithm for find_dumpfile() in case it fails

* Wed Aug 15 2018 Paul Howarth <paul@city-fan.org> - 3.3.93-1
- Update to 3.3.93
  - Added sst_dbl_action_type rc variable which controls side-effect of
    double-clicking in SST signals pane
  - Added xml2stems Verilator XML to rtlbrowse stems converter to
    distribution; eventually vermin will be removed
  - Added missing realpath() in udp emission in vermin

* Mon Jul 16 2018 Paul Howarth <paul@city-fan.org> - 3.3.92-1
- Update to 3.3.92
  - Harden FST loader for missing .hier files (if applicable)
  - Fixed broken GTK+-1.2 compile of twinwave
  - Fix scrolling on help window by adding scroll to end mark
  - Fix scrolling on status window when use_toolbutton_interface rc var is set
    to FALSE by adding scroll to end mark
  - Updated BUILT_SOURCES for vermin
  - extern yy_size_t yyleng fix in rtlbrowse

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.91-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun  4 2018 Paul Howarth <paul@city-fan.org> - 3.3.91-1
- Update to 3.3.91
  - Added support for GSettings for when GConf is removed from distributions
    such as Debian and Ubuntu
  - Performance fix for large number of groups (remove useless recursion
    required for transaction traces)
- Use gsettings rather than gconf from Fedora 29 onwards

* Tue May 15 2018 Paul Howarth <paul@city-fan.org> - 3.3.90-1
- Update to 3.3.90
  - For Cut Traces, fix up scroll position if there are traces above the
    current row being cut
  - Bits to real crash fix for very large floats
  - Fixed gray code conversions that were incomplete for right justified
    vectors such that the vector length is not a multiple of the radix size
    (4 for hex, 3 for oct)
  - Warray-bounds warning fix for 32-bit conversions in BitsToReal

* Fri Mar 23 2018 Paul Howarth <paul@city-fan.org> - 3.3.89-1
- Update to 3.3.89
  - Added support for 32-bit conversions in BitsToReal
  - Crash fix for pattern search with reals using LXT, LXT2, VZT

* Tue Mar  6 2018 Paul Howarth <paul@city-fan.org> - 3.3.88-1
- Update to 3.3.88
  - Added --sstexclude command line option to prune unwanted clutter from the
    SST window
  - Updated "/View/Mouseover Copies To Clipboard" menu option for copying
    signal names into the clipboard so they can be pasted into text editors,
    etc.
  - Fixed Write Save File to handle getting confused by initial cancel then
    retry
  - Updated v2k input/output declarations to handle unpacked arrays
  - Fix for pattern marks that could overshoot the left marker

* Tue Feb 20 2018 Paul Howarth <paul@city-fan.org> - 3.3.87-4
- BR: gcc-c++ as upstream prefers c++ for some of the code

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.87-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Paul Howarth <paul@city-fan.org> - 3.3.87-2
- Use libtirpc for RPC rather than SunRPC

* Tue Jan  9 2018 Paul Howarth <paul@city-fan.org> - 3.3.87-1
- Update to 3.3.87
  - Added missing prototype for ghw_read_sm_hdr in ghwlib.h
  - Made intptr_t changes vs. long during casting for win64
  - Warnings fixes
  - Re-enable twinwave for Win32/64
  - Added missing gtkwave_bin_launcher.sh in contrib/bundle_for_osx Makefile.am
- Scriptlets replaced by File Triggers from Fedora 26 onwards

* Mon Oct  9 2017 Paul Howarth <paul@city-fan.org> - 3.3.86-1
- Update to 3.3.86
  - Added recurse import function (found before only in the hier search) into
    the SST
  - Removed obsolete bundle functionality from SST as recurse import more
    accurately imports recursively
  - Made entrybox taller (using -1) as recent versions of gnome have taller
    window titlebars and the widget was not tall enough

* Mon Sep 25 2017 Paul Howarth <paul@city-fan.org> - 3.3.85-1
- Update to 3.3.85
  - Fix integer type in GHW loader so integer value changes are not stored as
    a string; this then allows bitwise manipulations of integers

* Thu Sep 21 2017 Paul Howarth <paul@city-fan.org> - 3.3.84-2
- Some spec clean-ups based on PR#1
  (https://src.fedoraproject.org/rpms/gtkwave/pull-request/1)
  - Drop support for pre-release builds
  - One build requirement per line
  - Sort build requirements
  - Add dependencies on gnome and hicolor icon themes, plus
    shared-mime-info (for directory ownership)
  - Don't use so many tabs

* Wed Sep  6 2017 Paul Howarth <paul@city-fan.org> - 3.3.84-1
- Update to 3.3.84
  - Updated FSDB reader with experimental FST tree build routines for faster
    initialization
  - Removed warnings found when compiling with -Wshadow
  - Automatically enable --comphier for FST/FSDB/AE2 if facility count reaches
    500000; this is to reduce memory consumption for traces with very many
    signals (added disable_auto_comphier to override this behavior)
  - Fix null pointer sent to gtk_clipboard_set_text() for mouseover to
    clipboard cut ops
- Use upstream desktop file and icons

* Mon Aug  7 2017 Paul Howarth <paul@city-fan.org> - 3.3.83-1
- Update to 3.3.83
  - Preserve search type for regex search across reloads or close/reopens of
    regex search widget
  - Update local libz to current version

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.82-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.82-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul  3 2017 Paul Howarth <paul@city-fan.org> - 3.3.82-1
- Update to 3.3.82
  - Get sys_fst working with VCS VPI
  - Added string concatenations for vectors
  - Added asserts to ghwlib.c to make scan-view clean

* Tue Jun 13 2017 Paul Howarth <paul@city-fan.org> - 3.3.81-1
- Update to 3.3.81
  - Added max_fsdb_trees environment variable
  - Fixed -C option so it is persistent across new tabs
  - Integrated updated GHW reader code
- Drop EL-5 support
  - Drop transitive build requirement on dbus-devel
  - Drop legacy BuildRoot: and Group: tags
  - Drop explicit buildroot cleaning in %%install section
  - Drop explicit %%clean section

* Thu Mar 30 2017 Paul Howarth <paul@city-fan.org> - 3.3.80-1
- Update to 3.3.80
  - Added "/View/Mouseover Copies To Clipboard" menu option to allow copying
    values into the clipboard so they can be pasted into text editors, etc.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.79-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 31 2016 Paul Howarth <paul@city-fan.org> - 3.3.79-1
- Update to 3.3.79
  - Disable accelerator keys in twinwave single window mode to avoid focus
    conflicts
  - Fixes for -fstrict-aliasing and other recent warnings
  - Added fill_waveform rc variable and corresponding menu option
    (/View/Show Filled High Values) to allow filling in the lower portion of
    high values for increased visibility

* Thu Oct 27 2016 Paul Howarth <paul@city-fan.org> - 3.3.78-1
- Update to 3.3.78
  - Fixed crash when using multiple pattern searches

* Wed Oct 19 2016 Paul Howarth <paul@city-fan.org> - 3.3.77-2
- Rebuild with new upstream tarball containing correct version numbering

* Mon Oct 17 2016 Paul Howarth <paul@city-fan.org> - 3.3.77-1
- Update to 3.3.77
  - Updated documentation to include an appendix on FST implementation details
  - Removed '!A || (A && B)' is equivalent to '!A || B' redundant condition
    checks where found in source
  - Added hier_ignore_escapes rc variable
  - Dynamic resizing tweaks for when it is turned off
  - Added HUWL-? value types to signal_change_list() to keep GHW files from
    crashing Tcl scripts

* Tue Aug 16 2016 Paul Howarth <paul@city-fan.org> - 3.3.76-1
- Update to 3.3.76
  - Fix for --disable-tcl in ./configure caused by 3.3.75 fix
  - Crash fix in fstapi.c on read value at time accessing of FST files that
    use new dynamic aliases, FastLZ, or LZ4; this primarily affects rtlbrowse

* Tue Aug  9 2016 Paul Howarth <paul@city-fan.org> - 3.3.75-1
- Update to 3.3.75
  - Fix crash when -S and -W are used in tandem

* Sun Jul 31 2016 Paul Howarth <paul@city-fan.org> - 3.3.74-1
- Update to 3.3.74
  - Fix for when a signal name is used as a hierarchy name at the same level of
    scope (affects fsdb)
  - Added --rcvar command line option to insert rc variable changes
    individually without needing to point to a configuration file
  - Change to combine traces down/up routines to handle 2D vector name
    generation
  - Allow FSDB files to contain ".gz" and ".bz2" suffixes as the libnffr loader
    can handle those
  - If a variable is declared in the dumpfile as an integer, then it is
    imported to the waveform display as an integer instead of a hex value; this
    works for dump file formats that show the datatype in the SST window
  - Added code that should prevent the primary marker from disappearing
    unexpectedly as well as dynamic resizing being stuck in the unset marker
    width

* Wed Jun 15 2016 Paul Howarth <paul@city-fan.org> - 3.3.73-1
- Update to 3.3.73
  - Added dragzoom_threshold rc variable to accommodate input devices that
    have a noisy 3rd mouse button
  - Fix emission of all filter names so they are emitted in canonical fashion,
    avoiding growing strings of ../ in savefiles

* Thu Apr 14 2016 Paul Howarth <paul@city-fan.org> - 3.3.72-1
- Update to 3.3.72
  - Revert to old gtkwave.appdata.xml as the new one is causing problems with
    appstream-util validation

* Wed Apr 13 2016 Paul Howarth <paul@city-fan.org> - 3.3.71-1
- Update to 3.3.71
  - printf format warnings fixes in lxt2_write.c
  - Added SVG gtkwave icon share/icons/hicolor/scalable/apps/gtkwave.svg
  - Make gtkwave interpret values as double precision FP for plotting when
    BitsToReal is enabled; also keeps analog mode enabled when selecting
    numerical formats (which allows enabling/disabling BitsToReal without
    going out of analog mode) - disabling analog mode can be done using the
    existing Analog->Off menu option
  - Fix broken non-canonical bit ordering (IBM) single bit extraction in
    process_tcl_list()
  - Fixed gtkwave::gtkwave::addSignalsFromList so it can handle subset and
    forward/reverse extractions on signals
  - Remove FST_WRITER_PARALLEL from MinGW CFLAGS as some recent versions of
    MinGW have issues with struct timespec when pthread.h is included
  - Added /Edit/Delete to destroy traces without affecting the existing cut
    buffer
- Patch out icon details from upstream appdata so as to pass validation

* Tue Feb 23 2016 Paul Howarth <paul@city-fan.org> - 3.3.70-1
- Update to 3.3.70
  - Various warnings fixes from new version of scan-build
  - Crash fix in Windows for transaction traces (broken since VCD/TIM export
    in 3.3.61)

* Sun Feb  7 2016 Paul Howarth <paul@city-fan.org> - 3.3.69-1
- Update to 3.3.69
  - Added missing EXTLOAD_CFLAGS declarations in configure.ac for FSDB
    detection when only .a files are present (necessary for Ubuntu)
  - Fixed valgrind warning in fst.c for dead memory allocation
  - Fixed signed fixed point binary number shift for negative numbers
  - Added ghw patch for missing enum crash in ghw files

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.68-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 24 2015 Paul Howarth <paul@city-fan.org> - 3.3.68-1
- Update to 3.3.68
  - Update copyright date
  - Added named markers capability to From: and To: time value input boxes
  - Added support for fixed point binary numbers for both signed and unsigned
    decimal display types

* Wed Sep 30 2015 Paul Howarth <paul@city-fan.org> - 3.3.67-1
- Update to 3.3.67
  - Updated LZ4 for version r131
  - Fixed right justify ascii datatype display

* Mon Jul  6 2015 Paul Howarth <paul@city-fan.org> - 3.3.66-1
- Update to 3.3.66
  - Faster fsdb initialization
  - Fix vcd recoder loader crash for malformed vcd if signal is declared as
    bits and a real valued change is encountered for the value change
  - Fixed crash in vcd2vzt for vcd files with no value changes (likely a
    malformed vcd)
  - Added fsdbReaderResetSignalList() to prevent signals from loading over and
    over when unnecessary
  - Compile fixes for renamed functions and defines in gtk osx

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.65-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 23 2015 Paul Howarth <paul@city-fan.org> - 3.3.65-1
- Update to 3.3.65
  - Added --, -I-, etc. option to port filtering in SST; using -- for example
    filters all non-ports from search results
  - Updated LZ4 for version r126
  - Minor warnings fixes
  - Moved TCL_LDADD/TK_LDADD before FSDB_LDADD to avoid stale Tcl library
    version conflicts
  - Removed appending [31:0] to vcd loaded integer names
  - Reduced recursion depth in GHW signal loader to prevent stack overflow
    crashes
  - Added support for synthetic clocks in FST file
  - Update timetrace marking so it runs quicker for large traces

* Wed Nov 26 2014 Paul Howarth <paul@city-fan.org> 3.3.64-1
- update to 3.3.64
  - fix to FileChooser to prevent requester from blocking on asking for a
    directory if a dumpfile is loaded without some amount of
    absolute/relative pathname
  - updated LZ4 for version r124
  - fix for x-windows OSX compiles

* Tue Nov 11 2014 Paul Howarth <paul@city-fan.org> 3.3.63-1
- update to 3.3.63
  - updated LZ4 for version r123
  - added fine horiz scrolling in wave window (when using the wheel on a mouse)
    if shift pressed
  - timescale fix for Verilator where it emits 0ps as a timescale
  - added sample gtkwave.appdata.xml file in share/appdata
- install and validate appdata from F-20 onwards

* Fri Oct  3 2014 Paul Howarth <paul@city-fan.org> 3.3.62-3
- fix scriptlet compatibility for older Fedora releases

* Thu Oct 02 2014 Rex Dieter <rdieter@fedoraproject.org> 3.3.62-2
- update mime scriptlet

* Fri Sep 26 2014 Paul Howarth <paul@city-fan.org> 3.3.62-1
- update to 3.3.62
  - added zoom_full, zoom_size and move_to_time to the dbus interface (dbus
    enabled by --with-gconf)
  - updated LZ4 to version r120 (r121 files are the same)
  - compiler warnings fixes for gtk+-1.2 (-Wall -Wshadow -Wextra)
- enable GConf support
- put a 256x256 icon where gnome-software can find it

* Mon Aug 18 2014 Paul Howarth <paul@city-fan.org> 3.3.61-2
- use %%license where possible

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 3.3.61-1.1
- rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 18 2014 Paul Howarth <paul@city-fan.org> 3.3.61-1
- update to 3.3.61
  - parameterized number of named markers, so that --enable-manymarkers at
    configure time allows up to 702 named markers instead of 26 (disabled by
    default)
  - updated LZ4 for version r118
  - fixed broken VCD/TIM export in Windows (broken by new file requester)

* Mon Jun  9 2014 Paul Howarth <paul@city-fan.org> 3.3.60-1
- update to 3.3.60
  - fix MinGW tmpfile_open() patch from previous release as it was using the
    wrong filename
  - harden fsdb reader against xtags that move backward in time

* Sat Jun  7 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 3.3.59-4
- rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Paul Howarth <paul@city-fan.org> 3.3.59-3
- rebuild for tcl 8.6 in Rawhide
  (https://fedoraproject.org/wiki/Changes/f21tcl86)

* Tue Apr 29 2014 Paul Howarth <paul@city-fan.org> 3.3.59-1
- update to 3.3.59
  - use Duff's Device for 8 byte -> 1 byte binary value compression algorithm
    in FST writer
  - warnings fixes from cppcheck
  - moved MinGW for FST to using different windows tempfile generation instead
    of tmpfile()
  - removed fflush() in FST for MinGW in places that can cause crashes with
    read-only files
  - updated man page for gtkwave.1 indicating that XID is in hex
  - allow decimal conversions on popcnt filtered vectors that are greater than
    64 bits (they will never overflow)

* Mon Mar 24 2014 Paul Howarth <paul@city-fan.org> 3.3.58-1
- update to 3.3.58
  - added /Data Format/Popcnt function for ones counting
  - warnings fixes from new Clang 3.4 scan-build
  - updated VCD ID generation in various helpers to use a faster, equivalent
    algorithm
  - change [1] at end of struct to C99 [] notation with appropriate allocation
    size modification
  - system_profiler speed fix for OSX
- drop EL-4 support

* Mon Feb 17 2014 Paul Howarth <paul@city-fan.org> 3.3.57-1
- update to 3.3.57
  - fix for Electric Fence crash in vlist_freeze()
  - updated LZ4 for version r113

* Thu Feb 13 2014 Paul Howarth <paul@city-fan.org> 3.3.56-1
- update to 3.3.56
  - added another crash fix patch for GTK-OSX
  - fix to regex search to remove duplicate signal names because of faulty
    dumpers
  - fix to configure.ac for MSYS not adding -lcomdlg32 when Tcl is disabled
  - valgrind fix on deallocated context: old GLOBALS pointer could be examined
    in set_GLOBALS_x()
  - minor cleanup in treesearch_gtk2.c: removed redundant show widget
    invocation
  - added missing compressBound() for compress2() dest mallocs

* Mon Feb 10 2014 Paul Howarth <paul@city-fan.org> 3.3.55-1
- update to 3.3.55
  - fixed problem with FST_DYNAMIC_ALIAS_DISABLE enabled when Judy arrays are
    not present
  - FST writer performance tweaks for traces with millions of signal
    declarations
  - keep FSDB_VT_STREAM (FSDB transaction type) traces from attempting to be
    read (for now) as they aren't yet processed
  - added more space-efficient FST dynamic alias encoding
  - tempfile creation fix for Windows; using tmpnam() is not enough and fails
    depending on user permissions
  - make vcd2fst use FastLZ instead of LZ4 as a default compression type if an
    EVCD file is being processed as it (re-)compresses much better; using
    -4/-F/-Z still gives expected results
  - changed double printf formatting for FSDB to "%%.16g" to match VCD
    formatting
  - added very fast I/O write capability to fst2vcd
  - added support for FSDB_BYTES_PER_BIT_2B (EVCD) in FSDB loader
  - added experimental fsdb2vcd in contrib; it is not currently compiled or
    used
  - fix to treesearch to remove duplicate signal names because of faulty
    dumpers
  - repscript fix for if -R starts without a dumpfile name

* Fri Jan  3 2014 Paul Howarth <paul@city-fan.org> 3.3.54-1
- update to 3.3.54
  - added LZ4 double compression on hierarchy tree for FST when hierarchy size
    exceeds 4MB
  - fix to regular expression filtering when +I+ form expressions are
    encountered in the SST; previously, the wrong value of regex match was used
    on 32-bit architectures due to the stack layout
  - removed --disable-inline-asm ./configure flag as inline assembly has been
    removed because it is generating incorrectly in some cases on x86_64

* Tue Dec 17 2013 Paul Howarth <paul@city-fan.org> 3.3.53-1
- update to 3.3.53
  - made LZ4 the default compression routine selected for vcd2fst
  - fixes to EVCD parsing in vcd2fst and evcd2vcd
  - automatically invoke --optimize if VPD or WLF is detected; invoke on FSDB
    if FsdbReader is missing
  - standardized export feature to write vcd using lower case for non 0/1 values
  - added perror() on errno-related exits in vcd loaders
  - added experimental wlf2vcd in contrib; it is not currently compiled or used
  - corrected non-functional typos in documentation

* Tue Nov 12 2013 Paul Howarth <paul@city-fan.org> 3.3.52-1
- update to 3.3.52
  - added LZ4 as compression type for FST; when enabled with --fourpack in
    vcd2fst, this compresses both signal data and the hierarchy using LZ4
  - added WLF support via wlf2vcd; to use, specify -o at the command line
    (e.g., gtkwave -o test.wlf)
  - changed left/right arrow function in signal/wave windows to find next
    transition of selected signal(s)
  - re-enabled DnD scroll beyond top/bottom of Signals pane
  - added debounce for baseline (middle) mouse button
  - another partial VCD loader fix
  - now use libcomdlg32 file requesters on MinGW
  - added --extensions flag to fstvcd to enable emission of FST extensions/
    attributes to VCD files; this is to keep FST attributes from making VCD
    files unparseable with other tools
  - fix in FsdbReader interface for version 1.x files
  - many warnings fixes found from gcc -Wextra flag
  - fixed thread-unsafe static allocations in fstapi.c

* Mon Oct 28 2013 Paul Howarth <paul@city-fan.org> 3.3.51-1
- update to 3.3.51
  - add gedit to the list of dependencies for gtkwave in order to enable new
    function that Icarus Verilog dumps into FST files
  - fix "/File/Grab To File" on OSX with an OSX patch as the
    _gdk_quartz_image_copy_to_image() function in the GTK toolkit for Quartz is
    broken
  - updated examples/gtkwaverc accel options to reflect the current state of
    the gtkwave main window main menu
  - added "Open Source Definition" and "Open Source Instantiation" options that
    invoke .gtkwaverc variable "editor" (or $GTKWAVE_EDITOR or gedit or open -t
    [OSX]) on sourcecode when source stems are present in the dumpfile
    (currently FST only)
  - fixed timezero in vcd2fst as it was only parsing unsigned numbers
  - fixed Open Hierarchy crash on blank signals
- BR:/R: gedit as per upstream recommendation

* Wed Oct 16 2013 Paul Howarth <paul@city-fan.org> 3.3.50-1
- update to 3.3.50
  - limit number of rows that can be displayed in mouseover in order to
    prevent potential X11 crashes on extremely wide signals
  - added "/File/Grab To File" PNG image grab menu option
  - added missing $dumpvars emission in fst2vcd
  - added missing atto and zepto time prefix parsing in vcd2fst
  - added VHDL package type to FST
  - added red box around 'U' vector values for VHDL similar to 'X' for Verilog
  - used FST "attribute name" for variable types if specified
  - CRLF fix for save file reading on LF-only systems
  - fix Valgrind hit in fst.c that was causing crashes on OSX
  - added fstWriterSetFiletype() and fstReaderGetFiletype() to provide sim
    language hint to gtkwave for language-appropriate formatting of various
    data
  - added fstWriterSetSourceStem() so writers can embed source stems in the FST
    file (specify before the appropriate hierarchy or variable declaration)
  - added gtkwave_bin_launcher.sh script to set up environment variables on OSX
    for running the bin/ directory files from a terminal rather than as an app
    invocation

* Thu Sep 12 2013 Paul Howarth <paul@city-fan.org> 3.3.49-1
- update to 3.3.49
  - fix crashes caused by X11 protocol limitation for pixmap size
  - potential buffer overflow fix in vcd2fst
  - added ability to store environment variable information in FST files
    (FST_MT_ENVVAR)
  - fixed bad enum for FST_PT_MAX
  - added contrib/fst_jni directory to distribution
  - fixed broken "make dist" variants
  - added buffer and linkage data directions (future expansion for VHDL) in
    FST and gtkwave
  - removed requirement for fsdbdebug in path when FsdbReader is present
  - fixed ordering of static FSDB libraries for when dynamic ones are not
    present
  - added direction filters to SST name filter search, i.e. adding +I+, +O+,
    +IO+, +B+, or +L+ before the regular expression adds additional filtering
    criteria (direction filters are case-insensitive)
  - relax FSDB loader to allow VHDL and mixed-language files
  - added VHDL hierarchy types to FST, internal VCD loaders and also
    vcdfst/fst2vcd
  - added in VHDL to FST (which will also allow other languages): gtkwave can
    process these types (e.g., signal + std_ulogic), but there are currently no
    simulators supporting them

* Tue Aug  6 2013 Paul Howarth <paul@city-fan.org> 3.3.48-1
- update to 3.3.48
  - fixed infinite loop hang on various helper executables when extra arguments
    are specified
  - delete changed marker name if it exists when marker is removed
  - added "Open Hierarchy" option that will expand the SST and select the
    hierarchy for a given signal selected in the Signals window
  - added preliminary support for FsdbReader
  - FSDB fix for generate created hierarchies
  - FSDB fix for new debug info output style to be parsed
  - added generate as scope type to VCD/FST/FSDB
  - preliminary add for module port direction for FSDB and FST
  - display signal direction column in SST if not all signals are declared as
    FST_VD_IMPLICIT
  - fixed GTK warning when hide_sst is enabled and SST is opened then closed
  - added extraction of in/out/inout from FSDB into FST with vcd2fst helper
    executable (it also converts FSDB to FST)
  - added support for SV structures, unions, classes, packages, programs and
    interfaces
  - updated signal parsing in FST/FSDB to handle NC declarations for arrays in
    VCD (i.e. bit-ranges are missing); use vcd2fst or the -o option to read NC
    VCD files with arrays properly
  - preliminary support for SV datatypes of bit, logic, int, shortint, longint,
    byte, enum, and shortreal in VCD and FST
  - added sparse array datatype to FST (currently unused by gtkwave)
  - added support for attribute begin/end in FST (currently unused by gtkwave);
    this allows embedding of various data inside the structure tree
  - added autoraise on entry window on keystrokes or periodically when it exists
  - added ability to store $comment in FST files via the attribute mechanism
    (FST_AT_MISC/FST_MT_COMMENT)

* Sun Jul 28 2013 Paul Howarth <paul@city-fan.org> 3.3.47-2
- install docs to %%{_pkgdocdir} where available

* Wed Jun 12 2013 Paul Howarth <paul@city-fan.org> 3.3.47-1
- update to 3.3.47
  - deprecated loader
  - partial VCD loader fix for small files
  - added preliminary do-nothing generate support in vermin
  - fixed minmax_valid for partial VCD loader: affects scaling on
    floating-point traces

* Mon Apr 29 2013 Paul Howarth <paul@city-fan.org> 3.3.46-1
- update to 3.3.46
  - fixed as of yet undetected hdr_incomplete bug when running off end of FST
    file (e.g., while file is being written)
  - fixed problem with is_gtkw_save_file getting wiped out on reload

* Sun Mar 24 2013 Paul Howarth <paul@city-fan.org> 3.3.45-1
- update to 3.3.45
  - fix for VCDNAM_ESCAPE character in treesearch window; this sometimes
    occurs for structure identifiers

* Thu Feb 28 2013 Paul Howarth <paul@city-fan.org> 3.3.44-1
- update to 3.3.44
  - fix for gdk_draw_layout assertion `GDK_IS_DRAWABLE (drawable)'

* Tue Feb  5 2013 Paul Howarth <paul@city-fan.org> 3.3.43-1
- update to 3.3.43
  - fix for rtlbrowse for gtk_adjustment_get_page_increment and
    gtk_adjustment_get_step_increment introduced in 2.14
  - added VPD support via vpd2vcd (to use, specify -o at the command line, e.g.
    gtkwave -o test.vpd)
  - added autodetect for LXT, LXT2, VZT, FST regardless of the filename suffix
  - crash fix for gtkwave::getDisplayedSignals, specifically removing the extra
    free_2() in WAVE_OE_ME
  - added conditional compile for stat() being available
- drop upstreamed old-gtk2 patch

* Wed Jan  2 2013 Paul Howarth <paul@city-fan.org> 3.3.42-1
- update to 3.3.42
  - fix to prevent missing group openings from keeping other signals in the
    viewer that follow from displaying
  - added more support for newer constructs in Vermin
  - added scrollwheel support to rtlbrowse code windows
  - added fseeko() return checking in fstapi.c to prevent errors with
    dynamically updated files
- add patch to fix build with gtk2 < 2.14

* Fri Nov  2 2012 Paul Howarth <paul@city-fan.org> 3.3.41-1
- update to 3.3.41
  - fix for gtkwave::addSignalsFromList when encountering signals of form
    a.b.MyBus[7:0] and a.b.MyBus[15:8] such that brackets aren't stripped
  - added experimental highlight_wavewindow rc variable, which allows signals
    also to be highlighted in the wave window using the value for color_grid
  - added use_standard_trace_select rc variable and related menu option

* Wed Sep 12 2012 Paul Howarth <paul@city-fan.org> 3.3.40-1
- update to 3.3.40
  - fixed y-size of splash screen on MinGW with newest version of GTK2 (as it
    could be verified on that version)
  - fixed off-by-one buffer string allocation write overflow in calloc_2()
    call in maketraces()

* Fri Aug 10 2012 Paul Howarth <paul@city-fan.org> 3.3.39-1
- update to 3.3.39
  - fixed relative pathnames when generated in MinGW and used back on Linux
  - added --output filename option to fst2vcd, vzt2vcd, and lxt2vcd
  - fixed crash on OSX if gtk_widget_set_sensitive is called on a separator
  - fixed OSX version so it looks for .gtkwaverc in the home directory and if
    not found, probes the resource bundle for
    Contents/Resources/examples/gtkwaverc (no dot in the name)
  - added GTKWave User's Guide option to help menu on OSX
  - added + vs ++ separators for twinwave
  - dynamic resize fixes

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.38-2
- rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 11 2012 Paul Howarth <paul@city-fan.org> 3.3.38-1
- update to 3.3.38
  - upgraded vermin parser to handle some > 1995 constructs
  - propagated -o option into "Open New Window" menu option
  - changed invert function so it does not incorrectly expand into the whole
    nybble when it is < 4 bits, i.e. inverting the two bit quantity 10 now
    displays as 0x1, not 0xD
  - added fstminer
  - various MinGW fixes

* Mon Jun 11 2012 Paul Howarth <paul@city-fan.org> 3.3.37-1
- update to 3.3.37
  - correct an issue in which the parser for process filter lines assumed the
    associated id number was always a single digit
  - catch one more case when locating bitblasted signals in vcd files created
    by modelsim
  - kill stray pipeio_create() processes on pipeio_destroy()
  - additions to extload to handle hier types, component types and signal types
  - added support for extload files as input filetype in vcd2fst
  - added -o for extload files to convert to FST

* Wed May  9 2012 Paul Howarth <paul@city-fan.org> 3.3.36-1
- update to 3.3.36
  - fixed destructive string convert in fstUtilityBinToEsc()
  - added support for 01xzhuwl-
  - added adaptive buffer resizing in FST writer for Linux and Mac OSX
  - fix for realpath() 2nd argument NULL on Leopard
  - fix for doubles stored in HistEnt fields in ghw introduced in 3.3.19

* Fri Apr 13 2012 Paul Howarth <paul@city-fan.org> 3.3.35-1
- update to 3.3.35
  - polarity fix for vcd_preserve_glitches in rcfile; default is no/off, use
    yes in the rcfile to enable (e.g., for viewing interpolated analog
    waveforms)
  - added vcd_preserve_glitches support to FST as --optimize uses FST
  - added vcd_preserve_glitches_real (for VCD/FST) rcfile variable that turns
    off deglitching only for real signals
  - fix for do_initial_zoom_fit when file requester used
  - changed contact address for bug reports to bybell at rocketmail.com
  - added fstWriterSetParallelMode()

* Tue Mar 13 2012 Paul Howarth <paul@city-fan.org> 3.3.34-1
- update to 3.3.34
  - fix for marker time deltas when $timezero is used
  - reduced size of alert requester icons to 64x64 pixels

* Sun Mar  4 2012 Paul Howarth <paul@city-fan.org> 3.3.33-1
- update to 3.3.33
  - scan-build fix in vcd_recoder.c
  - added $timezero tag to VCD files, which allows offsetting all the values
    in a trace to provide ability for negative time values (currently only VCD,
    LXT, LXT2, VZT, and FST support this)
  - fix for timescale 10s and 100s
- drop patch for builing with gtk2 2.10.0 to 2.14.0, no longer needed
- drop support for distributions prior to FC-3:
  - unconditionally build with tcl support

* Sat Feb 18 2012 Paul Howarth <paul@city-fan.org> 3.3.32-1
- update to 3.3.32
  - turn off loader messages when Tcl is executing a command
  - added gtk_print_unix_dialog support for printing to real printers by using
    the "UNIX" type
  - automatically kill splash screen on reload/new tab
  - added transaction_args savefile tag and support for passing args to
    transaction filters via the args $comment
  - added string value of \000, which renders as high-Z
  - integrated alt_wheel_mode code provided by Tom Browne
  - fixes for some rc file variables to keep them from getting clobbered on
    2nd tab opening
  - warning fixes when compiled on Ubuntu
- drop upstreamed patch for gtk2 < 2.4.0
- add patch to fix builds with gtk2 2.10.0 to 2.14.0

* Fri Feb  3 2012 Paul Howarth <paul@city-fan.org> 3.3.31-1
- update to 3.3.31
  - added support for native file requesters in OSX Quartz
  - added support for native alert dialogs in OSX Quartz
  - clang warning fixes
  - added missing config.guess and config.sub
  - allow drag of .gtkw (when viewer still does not have a file loaded) to
    load the corresponding dump file
  - fix MinGW compiles broken by recent changes
  - documentation updates
  - fixed broken ifdef in signalwindow.c that caused issues with loading and
    saving files
- add patch to fix build with gtk2 < 2.4.0

* Wed Jan 18 2012 Paul Howarth <paul@city-fan.org> 3.3.30-1
- update to 3.3.30
  - updated ./configure to add --disable-mime-update flag
  - fixed --optimize for --restore
  - added [optimize_vcd] savefile tag
  - disabled analog during mutually incompatible mode selection (binary,
    filters, etc.)
  - added F/P/T flags to mouseover for the filters
  - fixed problem where ungrab doesn't occur if button pressed and simultaneous
    reload accelerator key occurs
  - fixed combine direction in transaction filter to down
  - fixed vector analog render/print routine to use skipcnt
  - fixed transaction filter to cache hptr node if converted (i.e., do not
    place bitblasted in save file if avoidable)
  - fixed min/max of cached autoscaling sizing when number of extension traces
    changes

* Fri Dec 16 2011 Paul Howarth <paul@city-fan.org> 3.3.29-1
- update to 3.3.29
  - added OSX integration when compiled against gtk-osx
  - added mime types and icons for file types and desktop menus
  - changed .sav (deprecated but not removed) to .gtkw, with .gtkw itself being
    able to bring up the original dumpfile
  - numerous bug fixes
  - preliminary GConf support supporting session ID-based restore
  - preliminary GConf support to emulate OSX "open" functionality such that
    dumpfiles/savefiles can be targeted to an open gtkwave viewer/session ID
- drop upstreamed array size patch
- add scriptlet snippets for new desktop functionality

* Mon Nov 14 2011 Paul Howarth <paul@city-fan.org> 3.3.28-1
- update to 3.3.28
  - use larger, more readable Apple fonts for Quartz
  - added support for colorful traces using the /Edit/Color Format/... menu
    options
  - fixed rendertimes bug where times did not always display when grid is
    turned off
  - added keep_xz_colors gtkwaverc variable
- drop upstreamed patch for glib2 header file inclusion
- add patch to fix array size declared too small

* Tue Oct 25 2011 Paul Howarth <paul@city-fan.org> 3.3.27-1
- update to 3.3.27
  - fixes of suspicious NULL pointer warnings from scan-build
  - fixed inline function linker errors when using Clang
  - optimization of more [1] cases found in analyzer.h when
    -DWAVE_USE_STRUCT_PACKING is active
  - in process_url_list(), use g_malloc/g_free as context can or will change
    when files are loaded
  - added fix for DnD crash when Quartz is the GDK back-end on Mac OSX
  - fixed fstWriterFlushContext() such that invocations outside the fstapi are
    synced with time changes
  - modify main window size for twinwave on Quartz: GtkPlug window does not
    fit into GtkSocket as with X11
- add patch to fix up glib2 header file inclusion

* Wed Sep 28 2011 Paul Howarth <paul@city-fan.org> 3.3.26-1
- update to 3.3.26
  - Mac OSX fixes: removed restrictions for twinwave, compile fixes for Tcl
    detection, printf warning fixes (xcode gcc uses stricter warnings)
  - more generic warning fixes from recent feature adds

* Fri Sep 16 2011 Paul Howarth <paul@city-fan.org> 3.3.25-1
- update to 3.3.25
  - replace calloc_2 with histent_calloc in loaders where applicable
  - update tcl.m4 so /usr/lib64 can be automatically used
  - fix TR_ANALOG_STEP line clipping problem
  - fix for modelsim single-bit nets that are defined as [0] as some tools emit
    signals without the [0] and it causes savefile compatibility problems
  - add visible filter pattern in fileselbox() as well as selectable "*"
    pattern overrides
  - add custom filters to GtkFileChooser dialogue
  - fix in lxt2_read.c/.h for negative msb/lsb indices
  - fix in vzt_read.c/.h for negative msb/lsb indices

* Mon Aug  8 2011 Paul Howarth <paul@city-fan.org> 3.3.24-1
- update to 3.3.24
  - improve the searching for the TCL libraries (when using stubs)
  - fixed bug where Tcl_GetString was substituted with brace removal
    preprocessing when unnecessary (would break addSignalsFromList, etc.)

* Mon Jul  4 2011 Paul Howarth <paul@city-fan.org> 3.3.23-1
- update to 3.3.23
  - fixed ItemFactory callbacks as their argument lists did not reflect the
    correct callback argument type/order for callback_type=1; this is a
    long-standing hidden bug that would prevent pattern search from working on
    64-bit big-endian architectures
  - fixed broken "replace" signal option

* Sat Jun  4 2011 Paul Howarth <paul@city-fan.org> 3.3.22-1
- update to 3.3.22
  - optimized tree build so it can handle large amounts of component
    instantiations (netlists) without undue slowdown
  - added gcc -Wformat and -Wformat-security related fixes
  - updated hier_decompress_flagged so it can also decompress into its own
    static buffer in order to speed up temporary usage cases
  - fixed FST reader iterator to work better with --begin flag
  - fixed missing facname decompression for FST files on single trace import
    (backup case that should never happen)
  - added support for user-specified timescale ruler using the ruler_origin and
    ruler_step rc variables
  - added "/View/Define Time Ruler Marks" menu option
  - removed indirect file support as is unneeded for 64-bit
  - removed obsolete CVS modification log comments
  - handle vcd saver case of dot at end of signal name

* Sat Apr 30 2011 Paul Howarth <paul@city-fan.org> 3.3.21-1
- update to 3.3.21
  - fixed crash in LXT2 reader on malformed files (#690920)
  - fixed reload crash when -o flag used on non-VCD files (#695444)
- drop patch now included in upstream release

* Tue Mar 29 2011 Paul Howarth <paul@city-fan.org> 3.3.20-2
- tentative upstream fix for crash when reading malformed LXT file (#690920)
- nobody else likes macros for commands

* Fri Feb 25 2011 Paul Howarth <paul@city-fan.org> 3.3.20-1
- update to 3.3.20
  - fixed uninitialized mat variable in compress_facility()
  - added --slider-zoom option to gtkwave to enable experimental horizontal
    slider zoom feature with GTK2
  - fix vcd2fst so it can handle zero-length VCD event variables in their
    declarations

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.19-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb  7 2011 Paul Howarth <paul@city-fan.org> 3.3.19-1
- update to 3.3.19
  - more sanity checking in vcd2fst to prevent crashes on malformed files
  - rewrote support for compressed signal handling (FST only)
  - shmidcat now exits on EOF
  - added sys_fst.c VPI source for NC Verilog and XL
  - added component typename dumping into sys_fst.c so that NC can dump
    component names
  - added component type names in gtk2 tree (only used by FST so far)
  - memory usage improvements on 64-bit architectures
  - fixed top/bottom pane resizing bug after reload in SST window
  - fixed crashes in hierarchy search widget for GHW where standard, textio,
    std_logic_1164, etc. were selectable
  - fixed reload scroll position for bottom TreeView in SST window

* Wed Dec 29 2010 Paul Howarth <paul@city-fan.org> 3.3.18-1
- update to 3.3.18
  - minor bug fixes for corner cases
  - assembler fixes for x86_64
  - preliminary support for variable length records in FST files
  - added fstUtilityBinToEsc and fstUtilityEscToBin for conversion of binary
    data to C-style strings
  - allow escaped strings in VCD files to encode a richer set of data for
    non-standard "s" VCD records
  - to comply with fst2vcd, vcd readers now handle "string" variable type
    keyword
  - add detection for Verilog XL-style VCD identifiers in all VCD loaders in
    gtkwave in order to aid in indexing
  - more warnings fixes
  - fix mif_draw_string so it does not emit escaped character codes

* Mon Nov 29 2010 Paul Howarth <paul@city-fan.org> 3.3.17-1
- update to 3.3.17
  - added sanity check in dynamic alias reconstruct routine in FST reader and
    also fixed bug where alias reconstruction in current blocks doesn't
    overwrite previous, old block data

* Thu Nov 25 2010 Paul Howarth <paul@city-fan.org> 3.3.16-1
- update to 3.3.16
  - remove unused JError variables and replace with PJE0 macro
  - added experimental dynamic alias detection in fst writer when building
    with Judy support
  - added Jenkins hash routine to enable dynamic alias detection when Judy
    support is not available

* Thu Nov 11 2010 Paul Howarth <paul@city-fan.org> 3.3.15-1
- update to 3.3.15
  - fixes for fstapi file reading and writing
  - add detection in vcd2fst for Verilog XL-style VCD identifiers
  - the --optimize flag now uses fst instead of lxt2 as its default file format

* Wed Oct 27 2010 Paul Howarth <paul@city-fan.org> 3.3.14-1
- update to 3.3.14
  - fixes for experimental dynamic SST building code and compiler warnings
  - allow VCD files with start time = end time
  - add preliminary RPC mechanism
  - add configure --disable-inline-asm build option
  - add initial_signal_window_width rc variable

* Tue Oct 26 2010 Paul Howarth <paul@city-fan.org> 3.3.13-3
- rebuild for liblzma.so.5

* Fri Oct  1 2010 Paul Howarth <paul@city-fan.org> 3.3.13-2
- rebuild for gcc bug (#634757)

* Mon Sep 27 2010 Paul Howarth <paul@city-fan.org> 3.3.13-1
- update to 3.3.13
  - improve memory utilization on 32-bit architectures
  - add warnings for options that are non-functional for some configurations
  - reduce memory usage during file init for lxt2, vzt, and fst files
  - sparse versus non-sparse array crash fix for ae2 loader
  - fix tree build for fst when compressed facs are being used
  - make printed waves the same as viewed waves
  - add experimental dynamic SST building code (speedup for large trees)

* Mon Sep  6 2010 Paul Howarth <paul@city-fan.org> 3.3.12-1
- update to 3.3.12
  - fix for --disable-tcl or systems that do not have Tcl installed
  - add support for process and transaction filters in MinGW
  - add support for Open New Window to MinGW
- drop non-Tcl build patch, no longer needed

* Wed Aug 18 2010 Paul Howarth <paul@city-fan.org> 3.3.11-1
- update to 3.3.11
  - new tcl function: gtkwave::installFileFilter
  - new tcl function: gtkwave::installProcFilter
  - new tcl function: gtkwave::installTransFilter
  - new tcl function: gtkwave::setCurrentTranslateFile
  - new tcl function: gtkwave::setCurrentTranslateProc
  - new tcl function: gtkwave::setCurrentTranslateTransProc
  - new tcl function: gtkwave::setCurrentTranslateEnums
  - nested `ifdef fix for Vermin
  - fix for free to non-malloc'd address problem in repscripts
  - start to build a framework to support Tcl variable change callbacks
  - fix for 0 millisecond Tcl timer causing 100% CPU usage
  - add CVS versus ModelSim compatibility fixes for Bluespec savefiles
  - fix atoi_64 in presence of some garbage non-numerics
- add patch to fix building without Tcl
- explicitly disable Tcl where it won't build

* Sun Jul 18 2010 Paul Howarth <paul@city-fan.org> 3.3.10-1
- update to 3.3.10
  - parallel build fix
  - fix free of non-malloc'd address due to context changing in Tcl scripts
  - updated vcd2fst so it is compatible with VerilatedVcd writer
  - read hierarchy reconstruction hardening in fstapi.c
  - check return code for hierarchy generation in fst2vcd.c
  - updated example to reflect Quit name change
  - updated repscript_timer so it prints stack trace

* Wed Jul  7 2010 Paul Howarth <paul@city-fan.org> 3.3.9-1
- update to 3.3.9
  - changed accelerator for Quit to conform to Gnome guidelines
  - fix crash that can occur in RemoveTrace
- disable parallel build for now

* Sat Jun 26 2010 Paul Howarth <paul@city-fan.org> 3.3.8-1
- update to 3.3.8
  - add failure check on tempfile creation in fstReaderInit()
  - add strace_repeat_count and an appropriate menu option
  - add drag-and-drop of signals from gtkwave into rtlbrowse
  - remove the "/File/Quit/Don't Quit" menu item if "fast exit" is enabled
  - more warnings cleanups

* Sun Jun  6 2010 Paul Howarth <paul@city-fan.org> 3.3.7-1
- update to 3.3.7 (general bug and compiler warning fixes)
- -n option not needed in desktop file

* Tue May  4 2010 Paul Howarth <paul@city-fan.org> 3.3.6-1
- update to 3.3.6 (see CHANGELOG.TXT for details)
- add desktop file and icons based on Mandriva package
- BR: desktop-file-utils
- add scriptlets to update icon cache
- no longer need to fix permissions of lzma wrapper code

* Sat Mar 20 2010 Paul Howarth <paul@city-fan.org> 3.3.5-1
- update to 3.3.5 (see CHANGELOG.TXT for details)
- add Judy-devel buildreq for improved memory usage efficiency

* Mon Mar  8 2010 Paul Howarth <paul@city-fan.org> 3.3.4-1
- update to 3.3.4 (see CHANGELOG.TXT for details)

* Fri Feb 19 2010 Paul Howarth <paul@city-fan.org> 3.3.3-1
- update to 3.3.3
- drop upstreamed dlopen linking patch
- drop obsolete helper apps mvl2lxt, mvl2vcd, tex2vcd and tla2vcd

* Mon Feb 15 2010 Paul Howarth <paul@city-fan.org> 3.3.2-2
- fix FTBFS due to missing -ldl linking for dlopen function (#565173)

* Tue Jan  5 2010 Paul Howarth <paul@city-fan.org> 3.3.2-1
- update to 3.3.2 (speed up operation on networked filesystems)

* Sat Dec 26 2009 Paul Howarth <paul@city-fan.org> 3.3.0-1
- update to 3.3.0
- added tk support
- bundled old liblzma replaced by system xz (add BR: xz-devel)
- tcl/tk support require Fedora >= 2 or RHEL >= 4 (tcl 8.4)

* Fri Sep  4 2009 Paul Howarth <paul@city-fan.org> 3.2.3-1
- update to 3.2.3
- fix permissions in bundled liblzma for debuginfo

* Thu Aug  6 2009 Paul Howarth <paul@city-fan.org> 3.2.2-3
- drop patch for #515672, not needed with gcc 4.4.1-4

* Thu Aug  6 2009 Paul Howarth <paul@city-fan.org> 3.2.2-2
- add patch to work around #515672 (internal compiler error on PPC)

* Wed Aug  5 2009 Paul Howarth <paul@city-fan.org> 3.2.2-1
- update to 3.2.2 (new tools evcd2vcd/fst2vcd/vcd2fst)
- drop print-to-file patch, no longer needed

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-2.1
- rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Paul Howarth <paul@city-fan.org> 3.2.1-2
- add upstream patch for crash on print to file (#511858)

* Tue Apr 14 2009 Paul Howarth <paul@city-fan.org> 3.2.1-1
- update to 3.2.1

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 3.2.0-1.1
- rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 17 2009 Paul Howarth <paul@city-fan.org> 3.2.0-1
- update to 3.2.0

* Mon Feb  2 2009 Paul Howarth <paul@city-fan.org> 3.2.0-0.2.RC5
- update to 3.2.0RC5

* Fri Jan 23 2009 Paul Howarth <paul@city-fan.org> 3.2.0-0.1.RC4
- update to 3.2.0RC4 (#481264)
- new upstream URLs
- buildreq /usr/include/tcl.h for embedded tcl support

* Thu Aug 21 2008 Paul Howarth <paul@city-fan.org> 3.1.13-1
- update to 3.1.13

* Mon Jul 14 2008 Paul Howarth <paul@city-fan.org> 3.1.12-1
- update to 3.1.12

* Thu Jun 19 2008 Paul Howarth <paul@city-fan.org> 3.1.11-1
- update to 3.1.11

* Thu May 15 2008 Paul Howarth <paul@city-fan.org> 3.1.10-1
- update to 3.1.10

* Tue Apr 22 2008 Paul Howarth <paul@city-fan.org> 3.1.9-1
- update to 3.1.9

* Mon Apr  7 2008 Paul Howarth <paul@city-fan.org> 3.1.8-1
- update to 3.1.8

* Tue Mar 25 2008 Paul Howarth <paul@city-fan.org> 3.1.7-1
- update to 3.1.7

* Wed Feb 27 2008 Paul Howarth <paul@city-fan.org> 3.1.6-1
- update to 3.1.6

* Fri Feb  1 2008 Paul Howarth <paul@city-fan.org> 3.1.4-1
- update to 3.1.4

* Tue Jan 15 2008 Paul Howarth <paul@city-fan.org> 3.1.3-1
- update to 3.1.3

* Wed Jan  2 2008 Paul Howarth <paul@city-fan.org> 3.1.2-1
- update to 3.1.2

* Fri Sep 28 2007 Paul Howarth <paul@city-fan.org> 3.1.1-1
- update to 3.1.1

* Tue Sep  4 2007 Paul Howarth <paul@city-fan.org> 3.1.0-1
- update to 3.1.0

* Fri Aug 24 2007 Paul Howarth <paul@city-fan.org> 3.0.30-3
- clarify license as GPL, version 2 or later

* Fri Jul 27 2007 Paul Howarth <paul@city-fan.org> 3.0.30-1
- update to 3.0.30

* Fri Jun  8 2007 Paul Howarth <paul@city-fan.org> 3.0.29-1
- update to 3.0.29
- spec file much-simplified as gtkwave is now fully autotooled
- try to retain upstream timestamps as far as possible
- use parallel make

* Tue May  1 2007 Paul Howarth <paul@city-fan.org> 3.0.28-1
- update to 3.0.28
- update source URL to master source

* Mon Apr 30 2007 Paul Howarth <paul@city-fan.org> 3.0.27-1
- update to 3.0.27
- rename "vertex" to "vermin" to avoid conflict with Vertex 3D Model Assembler
  (http://wolfpack.twu.net/Vertex/index.html)

* Fri Apr 20 2007 Paul Howarth <paul@city-fan.org> 3.0.26-1
- update to 3.0.26

* Wed Apr 11 2007 Paul Howarth <paul@city-fan.org> 3.0.25-1
- update to 3.0.25

* Thu Apr  5 2007 Paul Howarth <paul@city-fan.org> 3.0.24-1
- update to 3.0.24

* Tue Mar 20 2007 Paul Howarth <paul@city-fan.org> 3.0.23-1
- update to 3.0.23

* Mon Feb 26 2007 Paul Howarth <paul@city-fan.org> 3.0.22-1
- update to 3.0.22

* Mon Feb  5 2007 Paul Howarth <paul@city-fan.org> 3.0.21-1
- update to 3.0.21

* Wed Jan 24 2007 Paul Howarth <paul@city-fan.org> 3.0.20-1
- update to 3.0.20

* Tue Jan  2 2007 Paul Howarth <paul@city-fan.org> 3.0.19-1
- update to 3.0.19

* Tue Dec  5 2006 Paul Howarth <paul@city-fan.org> 3.0.18-1
- update to 3.0.18

* Tue Nov 28 2006 Paul Howarth <paul@city-fan.org> 3.0.17-1
- update to 3.0.17

* Tue Nov 14 2006 Paul Howarth <paul@city-fan.org> 3.0.16-1
- update to 3.0.16

* Mon Oct 30 2006 Paul Howarth <paul@city-fan.org> 3.0.15-1
- update to 3.0.15

* Wed Oct 18 2006 Paul Howarth <paul@city-fan.org> 3.0.14-1
- update to 3.0.14

* Mon Oct  9 2006 Paul Howarth <paul@city-fan.org> 3.0.13-1
- update to 3.0.13

* Tue Oct  3 2006 Paul Howarth <paul@city-fan.org> 3.0.12-2
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Fri Sep 22 2006 Paul Howarth <paul@city-fan.org> 3.0.12-1
- update to 3.0.12
- create dummy libz/libbz2 Makefile.in files to ensure that config.h gets
  generated

* Thu Sep 14 2006 Paul Howarth <paul@city-fan.org> 3.0.11-1
- update to 3.0.11

* Mon Aug 21 2006 Paul Howarth <paul@city-fan.org> 3.0.10-1
- update to 3.0.10

* Fri Aug 11 2006 Paul Howarth <paul@city-fan.org> 3.0.9-1
- update to 3.0.9
- tarball is now .tar.gz rather than .tgz

* Mon Aug  7 2006 Paul Howarth <paul@city-fan.org> 3.0.8-1
- update to 3.0.8
- new program and manpage: shmidcat

* Fri Jul 21 2006 Paul Howarth <paul@city-fan.org> 3.0.7-1
- update to 3.0.7
- new program and manpage: twinwave

* Mon Jul 17 2006 Paul Howarth <paul@city-fan.org> 3.0.6-1
- update to 3.0.6

* Wed Jun 28 2006 Paul Howarth <paul@city-fan.org> 3.0.5-1
- update to 3.0.5
- new program and manpage: ghwdump

* Fri Jun  2 2006 Paul Howarth <paul@city-fan.org> 3.0.4-1
- update to 3.0.4

* Tue May 30 2006 Paul Howarth <paul@city-fan.org> 3.0.3-1
- update to 3.0.3

* Sun May 28 2006 Paul Howarth <paul@city-fan.org> 3.0.2-2
- adding missing buildreq flex

* Wed May 10 2006 Paul Howarth <paul@city-fan.org> 3.0.2-1
- update to 3.0.2

* Tue May  9 2006 Paul Howarth <paul@city-fan.org> 3.0.1-1
- update to 3.0.1

* Tue May  2 2006 Paul Howarth <paul@city-fan.org> 3.0.0-1
- update to 3.0.0
- add examples directory as %%doc
- add new buildreq gperf
- tweak Makefile.in edits to handle Makefiles under contrib/
- add new binaries rtlbrowse and vertex
- add new manpages for rtlbrowse, vertex, and gtkwaverc
- %%{_mandir} no longer needs to be created manually
- configure script now accepts --libdir

* Tue Mar  7 2006 Paul Howarth <paul@city-fan.org> 1.3.86-1
- update to 1.3.86

* Mon Feb 27 2006 Paul Howarth <paul@city-fan.org> 1.3.85-1
- update to 1.3.85

* Tue Feb 21 2006 Paul Howarth <paul@city-fan.org> 1.3.84-1
- update to 1.3.84
- INSTALL now called INSTALL.TXT

* Thu Feb 16 2006 Paul Howarth <paul@city-fan.org> 1.3.83-2
- rebuild

* Tue Jan 31 2006 Paul Howarth <paul@city-fan.org> 1.3.83-1
- update to 1.3.83

* Thu Jan 19 2006 Paul Howarth <paul@city-fan.org> 1.3.82-1
- update to 1.3.82

* Tue Dec 13 2005 Paul Howarth <paul@city-fan.org> 1.3.81-1
- update to 1.3.81

* Sun Nov 27 2005 Paul Howarth <paul@city-fan.org> 1.3.80-1
- update to 1.3.80

* Wed Nov 23 2005 Paul Howarth <paul@city-fan.org> 1.3.79-2
- fix file permissions in debuginfo package

* Mon Nov 21 2005 Paul Howarth <paul@city-fan.org> 1.3.79-1
- update to 1.3.79

* Wed Nov  9 2005 Paul Howarth <paul@city-fan.org> 1.3.78-1
- update to 1.3.78

* Tue Nov  8 2005 Paul Howarth <paul@city-fan.org> 1.3.77-1
- update to 1.3.77
- GHDL ghw support now included upstream, so remove patches

* Mon Nov  7 2005 Paul Howarth <paul@city-fan.org> 1.3.76-3
- clean up for Fedora Extras:
  - don't support GTK1 builds
  - unconditionally remove buildroot in %%clean and %%install
  - remove redundant glib2-devel buildreq
  - add dist tag

* Mon Nov  7 2005 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.3.76-2
- add GHDL ghw support

* Thu Oct 27 2005 Paul Howarth <paul@city-fan.org> 1.3.76-1
- update to 1.3.76

* Thu Oct 13 2005 Paul Howarth <paul@city-fan.org> 1.3.73-1
- update to 1.3.73

* Mon Oct 10 2005 Paul Howarth <paul@city-fan.org> 1.3.72-1
- update to 1.3.72

* Fri Oct  7 2005 Paul Howarth <paul@city-fan.org> 1.3.71-1
- update to 1.3.71

* Thu Sep 15 2005 Paul Howarth <paul@city-fan.org> 1.3.70-1
- update to 1.3.70
- new program tla2vcd (with manpage)

* Mon Sep  5 2005 Paul Howarth <paul@city-fan.org> 1.3.69-1
- update to 1.3.69
- honour %%{optflags}
- use system bzip and zlib libraries

* Fri Sep  2 2005 Paul Howarth <paul@city-fan.org> 1.3.68-1
- update to 1.3.68

* Thu Aug 25 2005 Paul Howarth <paul@city-fan.org> 1.3.67-1
- update to 1.3.67

* Wed Aug 10 2005 Paul Howarth <paul@city-fan.org> 1.3.64-1
- update to 1.3.64
- new programs lxt2miner & vztminer (with manpages)

* Tue Jul 26 2005 Paul Howarth <paul@city-fan.org> 1.3.63-1
- update to 1.3.63

* Mon Jul 11 2005 Paul Howarth <paul@city-fan.org> 1.3.62-1
- update to 1.3.62

* Thu Apr 21 2005 Paul Howarth <paul@city-fan.org> 1.3.58-1
- update to 1.3.58
- include sample .gtkwaverc in doc area
- update URL to point to new project home page

* Wed Apr 13 2005 Paul Howarth <paul@city-fan.org> 1.3.57-1
- update to 1.3.57
- add support for building with gtk version 1 (build using: --without gtk2)

* Tue Apr 12 2005 Paul Howarth <paul@city-fan.org> 1.3.56-1
- initial RPM build
