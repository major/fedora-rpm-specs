# Url to upstream GitHub repo.
%global git_url https://github.com/scummvm/%{name}


Name:		scummvm-tools
Version:	2.7.0
Release:	7%{?dist}
Summary:	Tools for scummVM / S.C.U.M.M scripting language
# All previous Lua versions are relicensed to MIT (https://www.lua.org/license.html)
# Automatically converted from old format: GPLv3+ and LGPLv2+ and MIT - review is highly recommended.
License:	GPL-3.0-or-later AND LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-MIT
URL:		http://www.scummvm.org

Source0:	http://www.scummvm.org/frs/%{name}/%{version}/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
Patch1:		configure.patch
BuildRequires:	make
BuildRequires:	gcc-c++
BuildRequires:	wxGTK-devel, libvorbis-devel, flac-devel, desktop-file-utils
BuildRequires:	zlib-devel bzip2-devel libmad-devel
BuildRequires:	libpng-devel freetype-devel boost-devel
Requires:	scummvm%{?_isa} >= %{version}
Provides:	bundled(lua) = 3.1

%description
This is a collection of various tools that may be useful to use in
conjunction with ScummVM.
Please note that although a tool may support a feature, certain ScummVM
versions may not. ScummVM 0.6.x does not support FLAC audio, for example.

Many games package together all their game data in a few big archive files.
The following tools can be used to extract these archives, and in some cases
are needed to make certain game versions usable with ScummVM.

The following tools can also be used to analyze the game scripts
(controlling the behavior of certain scenes and actors in a game).
These tools are most useful to developers.

%prep
%autosetup -p 1

%build
# The configure script shall ignore the parameter for the --host option
#passed by %%configure.
export CONFIGURE_NO_HOST=true

%configure --enable-verbose-build
%make_build

%install
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
%make_install
(cd ${RPM_BUILD_ROOT}%{_bindir} ; for i in `ls *|grep -v scummvm` ; do mv $i scummvm-$i ; done)

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications \
	%{SOURCE1}


%files
%license COPYING*
%doc README TODO
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 2.7.0-6
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Jonathan Wakely <jwakely@redhat.com> - 2.7.0-3
- Rebuilt for Boost 1.83

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Apr 16 2023 Christian Krause <chkr@fedoraproject.org> - 2.7.0-1
- Update to latest upstream
- Drop upstreamed patch

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 2.6.0-5
- Rebuilt for Boost 1.81

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Oct 17 2022 Scott Talbert <swt@techie.net> - 2.6.0-3
- Rebuild with wxWidgets 3.2

* Wed Sep 14 2022 Michel Alexandre Salim <salimma@fedoraproject.org> - 2.6.0-2
- Rebuilt for flac 1.4.0

* Sat Aug 13 2022 Christian Krause <chkr@fedoraproject.org> - 2.6.0-1
- Update to latest upstream
- Update License tag

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 2.5.0-3
- Rebuilt for Boost 1.78

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Dec 11 2021 Christian Krause <chkr@fedoraproject.org> - 2.5.0-1
- Update to latest upstream
- Update License tag and add more %%license files
- Drop upstreamed patch
- Update configure patch
- Flag bundled lua

* Sat Aug 07 2021 Jonathan Wakely <jwakely@redhat.com> - 2.2.0-5
- Rebuilt for Boost 1.76

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 2.2.0-2
- Rebuilt for Boost 1.75

* Sun Oct 18 2020 Christian Krause <chkr@fedoraproject.org> - 2.2.0-1
- Update to latest upstream
- Drop upstreamed patch
- Add patch from upstreamed PR to fix an build issue caused
  by the --host option of the %%autosetup macro

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 2020 Jeff Law <law@redhat.com> - 2.1.0-5
Fix broken configure test compromised by LTO

* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 2.1.0-4
- Rebuilt for Boost 1.73

* Sun Feb 23 2020 Björn Esser <besser82@fedoraproject.org> - 2.1.0-3
- Use %%autosetup macro
- Drop unneeded old patch
- Add patch from upstreamed PR to add compatibility for RPM's configure macro

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Oct 19 2019 Christian Krause <chkr@fedoraproject.org> - 2.1.0-1
- update to latest upstream

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 2.0.0-4
- Rebuilt for Boost 1.69

* Tue Oct 30 2018 Scott Talbert <swt@techie.net> - 2.0.0-3
- Fix FTBFS due to missing gcc-c++; Rebuild with wxWidgets 3.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Apr 14 2018 Christian Krause <chkr@fedoraproject.org> - 2.0.0-1
- update to latest upstream

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 1.9.0-9
- Rebuilt for Boost 1.66

* Sun Aug 20 2017 Björn Esser <besser82@fedoraproject.org> - 1.9.0-8
- Properly apply compiler / linker flags
- Add BR: libmad-devel for MP3 support
- Move COPYING to %%license

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 1.9.0-5
- Rebuilt for s390x binutils bug

* Tue Jul 04 2017 Jonathan Wakely <jwakely@redhat.com> - 1.9.0-4
- Rebuilt for Boost 1.64

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 1.9.0-2
- Rebuilt for Boost 1.63

* Sat Nov 12 2016 Christian Krause <chkr@fedoraproject.org> - 1.9.0-1
- update to latest upstream

* Sat Mar 12 2016 Lucian Langa <lucilanga@gnome.eu.org> - 1.8.0-1
- add patch to pass -fPIC to compile flags - fixes wxwidgets
- update url/download links
- update to latest upstream

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 1.7.0-8
- Rebuilt for Boost 1.60

* Mon Sep 07 2015 Jonathan Wakely <jwakely@redhat.com> - 1.7.0-7
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.7.0-5
- rebuild for Boost 1.58

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.7.0-3
- Rebuilt for GCC 5 C++11 ABI change

* Mon Jan 26 2015 Petr Machata <pmachata@redhat.com> - 1.7.0-2
- Rebuild for boost 1.57.0

* Wed Nov 12 2014 Christian Krause <chkr@fedoraproject.org> - 1.7.0-1
- new upstream release

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Peter Robinson <pbrobinson@fedoraproject.org> 1.6.0-5
- Update config.guess/sub during build for new arch (aarch64/ppc64le) support
- Cleanup SPEC

* Thu May 22 2014 Petr Machata <pmachata@redhat.com> - 1.6.0-4
- Rebuild for boost 1.55.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 27 2013 pmachata@redhat.com - 1.6.0-2
- Rebuild for boost 1.54.0

* Mon Jun 03 2013 Christian Krause <chkr@fedoraproject.org> - 1.6.0-1
- new upstream release
- add missing BuildRequires

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Feb 05 2012 Christian Krause <chkr@fedoraproject.org> - 1.4.0-1
- new upstream release

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.2.0-3
- Rebuild for new libpng

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Oct 17 2010 Lucian Langa <cooly@gnome.eu.org> - 1.2.0-1
- new upstream release

* Wed Jul 14 2010 Dan Horák <dan@danny.cz> - 1.1.1-2
- rebuilt against wxGTK-2.8.11-2

* Tue May 04 2010 Lucian Langa <cooly@gnome.eu.org> - 1.1.1-1
- new upstream release

* Thu Nov 26 2009 Lucian Langa <cooly@gnome.eu.org> - 1.0.0-1
- new upstream release

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 10 2009 Lucian Langa <cooly@gnome.eu.org> - 0.13.0-1
- new upstream release
- use SF generic downloads URL
- drop patch0 (fixed upstream)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Oct 30 2008 Lucian Langa <cooly@gnome.eu.org> - 0.12.0-5
- add desktop file

* Thu Oct 30 2008 Lucian Langa <cooly@gnome.eu.org> - 0.12.0-4
- use bz2 source

* Wed Oct 29 2008 Lucian Langa <cooly@gnome.eu.org> - 0.12.0-3
- prevent fedora optflags being overwritten

* Fri Oct 17 2008 Lucian Langa <cooly@gnome.eu.org> - 0.12.0-2
- update license tag
- fix CXXFLAGS
- update description

* Thu Oct 16 2008 Lucian Langa <cooly@gnome.eu.org> - 0.12.0-1
- New upstream release 0.12.0
- Update license
- Add desktop entry
- Prepare for inclusion into Fedora

* Sat Oct 29 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de> - 0:0.8.0-0.lvn.1
- Version upgrade

* Fri Dec 31 2004 Dams <anvil[AT]livna.org> - 0:0.7.0-0.lvn.3
- Missing zlib-devel BuildRequires

* Fri Dec 31 2004 Dams <anvil[AT]livna.org> - 0:0.7.0-0.lvn.2
- Patch for an 'install' target in Makefile
- Smarter way to rename all binaries

* Fri Dec 24 2004 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de> - 0:0.7.0-0.lvn.1
- upgrade to 0.7.0
- all tools have scummvm- prefix now so they can easily be found

* Thu Nov 25 2004 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de> - 0:0.6.1-0.lvn.1
- upgrade to 0.6.1
- adjust spec to new tools naming scheme..

* Thu May 27 2004 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de> - 0:0.6.0-0.lvn.1
- upgrade to 0.6.0

* Thu Oct 02 2003 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de> - 0:0.5.0-0.fdr.5
- removed #--- lines

* Tue Sep 16 2003 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de> - 0:0.5.0-0.fdr.4
- added ${RPM_OPT_FLAGS}

* Tue Sep 02 2003 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de> - 0:0.5.0-0.fdr.3
- changed Requires entry...

* Wed Aug 06 2003 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de> - 0:0.5.0-0.fdr.2
- upgrade to new version

* Fri Aug 01 2003 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de> - 0:0.4.1-0.fdr.1
- Initial RPM release.
