%if %{defined flatpak_runtime}
%global _prefix /app/extensions/Plugins/Calf
%global __brp_check_rpaths %{nil}
%endif

Name:		calf
Version:	0.90.4
Release:	2%{?dist}
Summary:	Audio plugins pack
# The jackhost code is GPLv2+ 
# The GUI code is LGPLv2+
# ladspa plugin is LGPLv2+
# lv2 plugin is GPLv2+ and LGPLv2+ and Public Domain
# dssi plugin is LGPLv2+
License:	GPL-2.0-or-later AND LGPL-2.0-or-later
URL:		http://calf-studio-gear.org/
Source0:	http://github.com/calf-studio-gear/calf/archive/%{version}/calf-%{version}.tar.gz
Source1:	%{name}-dssi.desktop

BuildRequires:	desktop-file-utils
BuildRequires:	dssi-devel
BuildRequires:	expat-devel
BuildRequires:	gcc-c++
BuildRequires:	glib2-devel
BuildRequires:	gtk2-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	lash-devel
BuildRequires:	libglade2-devel
BuildRequires:	lv2-devel
BuildRequires:  fluidsynth-devel
BuildRequires:  cairo-devel
BuildRequires:  libtool
BuildRequires:  fftw3-devel
BuildRequires:  make

Provides: ladspa-%{name}-plugins = %{version}-%{release}
Obsoletes: ladspa-%{name}-plugins < 0.90.3-13

%global common_desc \
The Calf project aims at providing a set of high quality open source audio\
plugins for musicians. All the included plugins are designed to be used with\
multitrack software, as software replacement for instruments and guitar stomp\
boxes.

%description
%common_desc

The plugins are available in LV2, DSSI, Standalone JACK and LADSPA formats.
This package contains the common files and the Standalone JACK plugin.

%package -n lv2-%{name}-plugins
Summary:	Calf plugins in LV2 format
License:	GPL-2.0-or-later AND LGPL-2.0-or-later AND LicenseRef-Fedora-Public-Domain
Requires:	%{name} = %{version}-%{release}
Requires:	lv2

%description -n lv2-%{name}-plugins
%common_desc

This package contains LV2 synthesizers and effects, MIDI I/O extension.

%package -n lv2-%{name}-plugins-gui
Summary:	Calf plugins in LV2 format
License:	GPL-2.0-or-later AND LGPL-2.0-or-later AND LicenseRef-Fedora-Public-Domain
Requires:	%{name} = %{version}-%{release}
Requires:	lv2-%{name}-plugins
Requires:	lv2

%description -n lv2-%{name}-plugins-gui
%common_desc

This package contains LV2 plugins GUI extension.

%package -n dssi-%{name}-plugins
Summary:	Calf plugins in DSSI format
License:	LGPL-2.0-or-later
Requires:	%{name} = %{version}-%{release}
Requires:	dssi

%description -n dssi-%{name}-plugins
%common_desc

This package contains DSSI synthesizers and effects, also GUI extensions.

%prep
%setup -q

%build
# Add GenericName to the .desktop file
echo "GenericName= Audio Effects" >> %{name}.desktop.in
./autogen.sh
# Make sure that optflags are not overriden.
sed -i 's|-O3||' configure

%configure \
	--with-dssi-dir=%{_libdir}/dssi/ \
	--with-lv2-dir=%{_libdir}/lv2 \
	--enable-experimental=yes \
%ifarch x86_64 %ix86
	--enable-sse \
%endif

make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

# The Jack host
desktop-file-install \
	--remove-category="Application" \
	--remove-key="Version" \
	--add-category="X-Synthesis" \
	--dir=$RPM_BUILD_ROOT%{_datadir}/applications \
	$RPM_BUILD_ROOT/%{_datadir}/applications/%{name}.desktop

# The DSSI host
ln -s jack-dssi-host $RPM_BUILD_ROOT%{_bindir}/%{name}
desktop-file-install \
	--dir=$RPM_BUILD_ROOT%{_datadir}/applications \
	%{SOURCE1}

# We don't need this file:
rm -f $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/icon-theme.cache

rm $RPM_BUILD_ROOT/%{_libdir}/%{name}/*.a*

#symlinks for dssi and ladspa
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/dssi
ln -s %{_libdir}/calf/calf.so $RPM_BUILD_ROOT/%{_libdir}/dssi/calf.so

%files
%doc AUTHORS ChangeLog README TODO
%license COPYING*
%{_bindir}/%{name}*
%{_libdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/*
%{_mandir}/man1/%{name}*
%{_mandir}/man7/%{name}*
%{_docdir}/%{name}
%{_datadir}/bash-completion/

%files -n lv2-%{name}-plugins
%license COPYING*
%{_libdir}/lv2/%{name}.lv2
%exclude %{_libdir}/lv2/%{name}.lv2/calflv2gui.so

%files -n lv2-%{name}-plugins-gui
%{_libdir}/lv2/%{name}.lv2/calflv2gui.so

%files -n dssi-%{name}-plugins
%{_bindir}/%{name}
%{_datadir}/applications/%{name}-dssi.desktop
%{_libdir}/dssi/%{name}.so

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Nov 04 2024 Gwyn Ciesla <gwync@protonmail.com> - 0.90.4-1
- 0.90.4

* Mon Sep 23 2024 Gwyn Ciesla <gwync@protonmail.com> - 0.90.3-20
- Fix lv2 requires.

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Mar 03 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.90.3-15
- migrated to SPDX license

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Oct 20 2022 Gwyn Ciesla <gwync@protonmail.com> - 0.90.3-13
- Drop ladspa, BZ 2064061

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 15 2021 Gwyn Ciesla <gwync@protonmail.com> - 0.90.3-9
- Fluidsynth rebuild.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 29 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.90.3-6
- Make lv2-calf-plugins require the main package.

* Wed Apr 01 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.90.3-5
- Move gui to subpackage (vascom)

* Mon Feb 17 2020 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.90.3-4
- Rebuild against fluidsynth2

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 16 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.90.3-1
- 0.90.3.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 07 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.90.1-1
- 0.90.1.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat May 26 2018 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.90.0-2
- Fix crashes due to accessing an index of a vector beyond its size RHBZ#1581433

* Wed Mar 07 2018 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.90.0-1
- Latest upstream
- Added BR: gcc-c++
- moved COPYING into %%license

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.60-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.0.60-8
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.60-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.60-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.60-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.60-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Apr 25 2016 Jon Ciesla <limburgher@gmail.com> - 0.0.60-3
- Correct upstream tarball.
- Enable experimental, BZ 1206761.

* Mon Apr 25 2016 Jon Ciesla <limburgher@gmail.com> - 0.0.60-2
- Fix symlinks.

* Sun Apr 24 2016 Jon Ciesla <limburgher@gmail.com> - 0.0.60-1
- Latest upstream, BZ 1229579.

* Thu Feb 25 2016 Jon Ciesla <limburgher@gmail.com> - 0.0.19-10
- Fix FTBFS.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.19-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.19-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.0.19-7
- Rebuilt for GCC 5 C++11 ABI change

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.19-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat May 04 2013 Brendan Jones <brendan.jones.it@gmail.com> 0.0.19-3
- Another missing BR fftw3-devel

* Fri May 03 2013 Brendan Jones <brendan.jones.it@gmail.com> 0.0.19-2
- Add libtool

* Fri Dec 14 2012 Brendan Jones <brendan.jones.it@gmail.com> 0.0.19.0-1
- New upstream release

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.18.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.18.6-6
- Rebuilt for c++ ABI breakage

* Mon Jan 09 2012 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.0.18.6-5
- gcc-4.7 compile fix
- remove parts of the spec file that are no longer required by the guidelines

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.0.18.6-4
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.18.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 29 2010 jkeating - 0.0.18.6-2
- Rebuilt for gcc bug 634757

* Sat Sep 11 2010 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.0.18.6-1
- Update to 0.0.18.6
- Drop upstreamed patch

* Wed Jul 14 2010 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.0.18.5-4
- Fix ladspa_wrapper crash RHBZ#600713

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.18.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 13 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.0.18.5-2
- Add a .desktop file for the DSSI plugin
- Add X-Synthesis category to the existing .desktop file of the JACK plugin
- Backport the LADSPA URI fix from trunk

* Thu Jun 11 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.0.18.5-1
- Update to 0.0.18.5
- Drop upstreamed gcc44 patch

* Mon Mar 30 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.0.18.3-1
- Initial build
