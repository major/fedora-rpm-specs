Name:           openarena
Version:        0.8.8
Release:        34%{?dist}
Summary:        Open source first person shooter
License:        GPL-2.0-only AND CC0-1.0
URL:            http://openarena.ws/
Source0:        http://download.tuxfamily.org/openarena/rel/081/oa081.zip
Source10:       http://download.tuxfamily.org/openarena/rel/085/oa085p.zip
Source11:       http://download.tuxfamily.org/openarena/rel/088/oa088p.zip
Source2:        %{name}.sh
# From https://github.com/flathub/ws.openarena.OpenArena/blob/master/ws.openarena.OpenArena.png
Source3:        ws.openarena.OpenArena.png
Source4:        %{name}.desktop
Source5:        %{name}.appdata.xml

# We need 1.36-11 or newer for the new standalone game and protocol cvars
Requires:       quake3 >= 1.36-11
Requires:       hicolor-icon-theme
Requires:       opengl-games-utils
Requires:       rsync
BuildRequires:  ImageMagick
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
Provides:       openarena-data = %{version}-%{release}
Obsoletes:      openarena-data < 0.7.1-4
BuildArch:      noarch

%description
OpenArena is an open-source content package for Quake III Arena licensed under
the GPL, effectively creating a free stand-alone game.

%prep
%setup -q -c
unzip -qq -o %{SOURCE10}
unzip -qq -o %{SOURCE11}
mkdir doc
for file in CHANGES COPYING CREDITS README readme_088.txt; do
    cat %{name}-0.8.1/$file | sed s/\\r// > doc/$file
    touch -r %{name}-0.8.1/$file doc/$file
done

%build
echo We build nothing

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_metainfodir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
mkdir -p $RPM_BUILD_ROOT%{_bindir}

cp -pr %{name}-0.8.1/baseoa $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m755 %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}/%{name}
sed -i -e 's|/usr|%{_prefix}|' $RPM_BUILD_ROOT%{_bindir}/%{name}
ln -s %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}_ded
cp -p %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps/openarena.png
chmod 644 $RPM_BUILD_ROOT%{_datadir}/%{name}/baseoa/*
desktop-file-install --dir=$RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE4}
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/*

mkdir -p $RPM_BUILD_ROOT%{_metainfodir}
install -pm 644 %{SOURCE5} $RPM_BUILD_ROOT%{_metainfodir}/
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/*.appdata.xml

%files
%doc doc/CREDITS doc/README doc/CHANGES doc/*.txt
%license doc/COPYING
%{_bindir}/%{name}*
%{_datadir}/%{name}
%{_metainfodir}/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 08 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.8.8-29
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 24 2022 Daniel Rusek <mail@asciiwolf.com> - 0.8.8-26
- Set PrefersNonDefaultGPU to true

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 05 2021 Gwyn Ciesla <gwync@protonmail.com> - 0.8.8-22
- Desktop correction.

* Tue Jan 05 2021 Gwyn Ciesla <gwync@protonmail.com> - 0.8.8-21
- Source correction.

* Mon Jan 04 2021 Gwyn Ciesla <gwync@protonmail.com> - 0.8.8-20
- Fix 1912072.

* Sun Jan 03 2021 Antonio Trande <sagitter@fedoraproject.org> - 0.8.8-19
- Fix bugzilla #1912072

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Kalev Lember <klember@redhat.com> - 0.8.8-16
- Avoid hardcoding /usr prefix in the launcher shell script
- Install the app icon into hicolor icon theme

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Antonio Trande <sagitter@fedoraproject.org> - 0.8.8-13
- Reinstall license file
- Use metainfodir
- Update and validate appdata file

* Mon Oct 15 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.8.8-12
- Alternate icon image, BZ 1609558.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 0.8.8-5
- Add an AppData file for the software center

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 29 2013 Kalev Lember <kalevlember@gmail.com> - 0.8.8-2
- Include some data files left out from last build

* Fri Jan 25 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 0.8.8-1
- upstream release 0.8.8

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 28 2011 Hans de Goede <hdegoede@redhat.com> - 0.8.5-3
- Update launcher script to work with newer quake3 package + require this

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Nov 12 2010 Hans de Goede <hdegoede@redhat.com> - 0.8.5-2
- Fix compability with network play with official openarena servers (#565763)
- Various specfile cleanups

* Tue Apr 27 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0.8.5-1
- Update to 0.8.5 via patch
- Update spec to match the latest Fedora packaging guidelines

* Tue Jul 28 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 0.8.1-1
- Catching up to a new release in a long time
- new maps, guns, models, textures 
- http://openarena.ws/svn/CHANGES

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jun 06 2008 Michał Bentkowski <mr.ecik at gmail.com> - 0.7.7-2
- Fix permissions...

* Wed Jun 04 2008 Michał Bentkowski <mr.ecik at gmail.com> - 0.7.7-1
- Add patch
- Get rid of macros from Sources

* Wed Apr 23 2008 Michał Bentkowski <mr.ecik at gmail.com> - 0.7.6-1
- New release
- Fix desktop file a bit

* Sun Jan 13 2008 Michał Bentkowski <mr.ecik at gmail.com> - 0.7.1-5
- Fix wrapper to include master server adress

* Sat Jan 05 2008 Michał Bentkowski <mr.ecik at gmail.com> - 0.7.1-4
- Use quake3 package from repo instead of own engine
- No -data subpackage since the main package now contains data
- Now the spec simple creates wrapper and just copy data to proper dir

* Fri Oct 05 2007 Michał Bentkowski <mr.ecik at gmail.com> - 0.7.1-3
- Add support for opengl-games-utils

* Fri Aug 24 2007 Michał Bentkowski <mr.ecik at gmail.com> - 0.7.1-2
- BuildID rebuild
- License tag fix

* Mon Aug 13 2007 Jon Ciesla <limb@jcomserv.net> - 0.7.1-1
- Added 0.7.1 patch. 
- Uses 0.7.0 .zip, took version macro out of URL and setup to accommodate.

* Fri Jul 13 2007 Michał Bentkowski <mr.ecik at gmail.com> - 0.7.0-3
- NO_VM_COMPILED flag on ppc64

* Fri Jul 13 2007 Michał Bentkowski <mr.ecik at gmail.com> - 0.7.0-2
- Add libvorbis-devel BR

* Wed Jul 11 2007 Michał Bentkowski <mr.ecik at gmail.com> - 0.7.0-1
- Update to 0.7.0

* Fri Jan 12 2007 Michał Bentkowski <mr.ecik at gmail.com> - 0.6.0-4
- Get rid of -maltivec flag

* Wed Jan 10 2007 Michał Bentkowski <mr.ecik at gmail.com> - 0.6.0-3
- Do some ppc fixes

* Wed Jan 03 2007 Michał Bentkowski <mr.ecik at gmail.com> - 0.6.0-2
- Add COPYING to data subpackage
- Remove LINUXNOTES from %%doc

* Mon Jan 01 2007 Michał Bentkowski <mr.ecik at gmail.com> - 0.6.0-1
- Initial new year release
