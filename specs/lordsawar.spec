Name:           lordsawar
Version:        0.3.2
Release:        15%{?dist}
Summary:        Turn-based strategy game in a fantasy setting

# This is used for prereleases and such
# If not prerelease, set this to the version macro
%global rel_version %{version}

# Some documentation is GFDLv1.1+
# Automatically converted from old format: GPLv3+ and GFDL - review is highly recommended.
License:        GPL-3.0-or-later AND LicenseRef-Callaway-GFDL
URL:            http://savannah.nongnu.org/projects/%{name}
Source0:        http://download.savannah.gnu.org/releases/%{name}/%{name}-%{rel_version}.tar.gz
# Use a local copy of the manual, rather than a remote one, for help
# Except we don't have a copy of the movie demo that doesn't come with
# the source.
# FIXME(hguemar): patch needs to be refreshed, disabled to rebuild against newer gstreamermm
#Patch1:         lordsawar-local-manual.patch
#Patch2:         0001-Migrate-to-Gstreamermm-1.0-API.patch
#Patch3:         0002-Fix-compilation-with-GCC-7-never-compare-pointers-to.patch
# Reserve doesn't actually make vectors bigger, it is used to make resizing 
# more efficient. resize is needed to actually make it bigger.
Patch4:         assert.patch

BuildRequires:  gcc-c++
BuildRequires:  gtkmm30-devel gettext desktop-file-utils gstreamermm-devel
BuildRequires:  libarchive-devel intltool libxslt-devel docbook-utils
BuildRequires:  libxml++-devel libtool
BuildRequires: make

%description
LordsAWar! is a turn-based strategy game set in a fantasy setting.


%prep
%setup -qn %{name}-%{rel_version}
#%patch1
#%patch2 -p1
#%patch3 -p1
%patch -P4
sed -i.orig -e "s/Comment=Play a clone of Warlords II/Comment=Play a turn-based strategy game/" dat/lordsawar.desktop.in.in


%build
./autogen.sh
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
mv $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}-appdata.xml $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml
%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS README COPYING TODO
%{_bindir}/%{name}
%{_bindir}/%{name}-import
%{_bindir}/%{name}-upgrade-file
%{_bindir}/%{name}-game-host-client
%{_bindir}/%{name}-game-host-server
%{_bindir}/%{name}-game-list-client
%{_bindir}/%{name}-game-list-server
#%%{_datadir}/gnome/help/%%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/icons/hicolor/22x22/apps/%{name}.png
%{_datadir}/icons/hicolor/24x24/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/%{name}
%{_mandir}/man6/lordsawar-game-host-client.6*
%{_mandir}/man6/lordsawar-game-host-server.6*
%{_mandir}/man6/lordsawar-game-list-client.6*
%{_mandir}/man6/lordsawar-game-list-server.6*
%{_mandir}/man6/lordsawar-import.6*
%{_mandir}/man6/lordsawar.6*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 0.3.2-14
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 30 2021 Bruno Wolff III - 0.3.2-6
- It looks like the build issue is fixed now

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 12 2020 Bruno Wolff III <bruno@wolff.to> - 0.3.2-2
- Get fix to prevent asserts into a build.

* Fri Apr 24 2020 Bruno Wolff III <bruno@wolff.to> - 0.3.2-1
- New upstream release 0.3.2
- Release notes: http://savannah.nongnu.org/forum/forum.php?forum_id=9714

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb  7 2018 Haïkel Guémar <hguemar@fedoraproject.org> - 0.3.1-1
- Upstream 0.3.1
- Refresh patches
- Disable help installation

* Wed Feb  7 2018 Haïkel Guémar <hguemar@fedoraproject.org> - 0.3.0-9
- Rebuild against newer gstreamermm

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.0-8
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jun 10 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 0.3.0-4
- Migrate to Gstreamermm 1.0 API

* Wed Jun 08 2016 Bruno Wolff III <bruno@wolff.to> - 0.3.0-3
- Rebuild for gstreamermm soname bump
- Manually pull libxml++ in for the build

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jul 05 2015 Bruno Wolff III <bruno@wolff.to> 0.3.0-1
- Upstream 0.3.0
- Release notes: http://savannah.nongnu.org/forum/forum.php?forum_id=8308
- Note lordsawar-upgrade-file can convert 0.2.0 save files to 0.3.0
- Man pages are now included

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.2.0-17
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 0.2.0-16
- Add an AppData file for the software center

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 0.2.0-15
- Rebuild for boost 1.57.0

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 0.2.0-12
- Rebuild for boost 1.55.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 0.2.0-10
- Rebuild for boost 1.54.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-7
- Rebuilt for c++ ABI breakage

* Mon Jan 16 2012 Bruno Wolff III <bruno@wolff.to> 0.2.0-6
- Fix for gcc 4.7

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Nov 05 2011 Bruno Wolff III <bruno@wolff.to> 0.2.0-4
- Rebuild for libpng 1.5
- g_thread_init is no longer needed

* Sat Mar 19 2011 Bruno Wolff III <bruno@wolff.to> 0.2.0-3
- All GDFL license versions share the same tag

* Sat Mar 19 2011 Bruno Wolff III <bruno@wolff.to> 0.2.0-2
- Use a local copy of the manual for help

* Thu Mar 17 2011 Bruno Wolff III <bruno@wolff.to> 0.2.0-1
- 0.2.0 final
- Release notice: http://savannah.nongnu.org/forum/forum.php?forum_id=6751

* Tue Mar 15 2011 Bruno Wolff III <bruno@wolff.to> 0.2.0-0.1.pre4
- Upstream 0.2.0 prerelease

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 Ian Weller <iweller@redhat.com> - 0.1.9-1
- 0.1.9 release

* Wed Mar 10 2010 Ian Weller <ian@ianweller.org> - 0.1.7-1
- Final 0.1.7 release
- lordsawar-0.1.7-pre3-dso.patch applied upstream so removed here

* Tue Mar  2 2010 Ian Weller <ian@ianweller.org> - 0.1.7-0.3.pre3
- Forgot to add the patch in CVS (whoops)

* Mon Mar  1 2010 Ian Weller <ian@ianweller.org> - 0.1.7-0.2.pre3
- Add lordsawar-0.1.7-pre3-dso.patch (patch from upstream)

* Sun Feb 28 2010 Ian Weller <ian@ianweller.org> - 0.1.7-0.1.pre3
- 0.1.7-pre3

* Fri Feb 12 2010 Ian Weller <ian@ianweller.org> - 0.1.6-3
- Remove BuildRequires: e2fsprogs-devel from libuuid-devel switch

* Fri Nov  6 2009 Ian Weller <ian@ianweller.org> - 0.1.6-2
- Remove patch0 command

* Fri Nov  6 2009 Ian Weller <ian@ianweller.org> - 0.1.6-1
- 0.1.6

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Ian Weller <ian@ianweller.org> - 0.1.5-3
- Fix build dependency on uuid.h

* Thu Apr  9 2009 Ian Weller <ianweller@gmail.com> 0.1.5-2
- Include new lang files

* Thu Apr  9 2009 Ian Weller <ianweller@gmail.com> 0.1.5-1
- 0.1.5

* Thu Mar 05 2009 Caolán McNamara <caolanm@redhat.com> - 0.1.4-4
- include stdio.h for printf

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 18 2008 Ian Weller <ianweller@gmail.com> 0.1.4-2
- Bump because I screwed up my CVS checkin

* Sun Dec 07 2008 Ian Weller <ianweller@gmail.com> 0.1.4-1
- 0.1.4
- Add BuildRequires: intltool >= 0.35.0

* Mon Nov 24 2008 Ian Weller <ianweller@gmail.com> 0.1.3-3
- Patch desktop file to not reference a certain patented game

* Mon Nov 24 2008 Ian Weller <ianweller@gmail.com> 0.1.3-2
- Remove commented-out patches
- Remove vendor from desktop-file-install
- Add icon for desktop menu item

* Sat Oct 25 2008 Ian Weller <ianweller@gmail.com> 0.1.3-1
- Updated upstream

* Sun Sep 21 2008 Ian Weller <ianweller@gmail.com> 0.1.1-3
- Add patch lordsawar-0.1.1-bz461454c10.patch:
    This patch fixes a crash in lordsawar when active neutral cities have produced
    a preset maximum number of army units.

* Tue Sep 16 2008 Ian Weller <ianweller@gmail.com> 0.1.1-2
- Summary and description changed

* Sun Sep 07 2008 Ian Weller <ianweller@gmail.com> 0.1.1-1
- Upstream updated

* Sat Aug 09 2008 Ian Weller <ianweller@gmail.com> 0.1.0-1
- Initial package build.
