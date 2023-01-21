%global revision 625
%global revision_date 20180421

Name:           light-themes
Version:        16.10
Release:        15.%{revision_date}bzr%{revision}%{?dist}
Summary:        Themes for Ubuntu

License:        CC-BY-SA
URL:            https://launchpad.net/ubuntu-themes/
Source0:        %{name}-bzr%{revision}.tar.xz
# light-themes is based on ubuntu-themes project, which contains copyrighted
# trademarks. Therefore we use this script to remove them before shipping
# it. Invoke this script to generate the light-themes tarball
Source1:        %{name}-generate-tarball.sh
# Fix DMZ cursor theme name in index.theme files (named "DMZ-White" in Ubuntu,
# "dmz" in Fedora)
Patch0:         %{name}-16.10-cursor.patch
# Fix Ubuntu icon dependency themes in index.theme files (themes renamed from
# "ubuntu-mono-*" to "Monochrome-*" in Fedora for copyright reasons)
Patch1:         %{name}-14.04-icons.patch
BuildArch:      noarch

%description
This project gathers together what ubuntu-artworks, ubuntu-mono and light-themes
in one package as they all define what Ubuntu is.


%package -n light-theme-gnome
Summary:        Ambiance and Radiance GNOME themes
Requires:       dmz-cursor-themes
Requires:       gtk-murrine-engine
Requires:       monochrome-icon-theme = %{version}-%{release}
Provides:       light-gtk2-theme = %{version}-%{release}
Provides:       light-gtk3-theme = %{version}-%{release}
Provides:       light-metacity-theme = %{version}-%{release}
Obsoletes:      light-gtk2-theme < 14.04-10.20151001bzr455
Obsoletes:      light-gtk3-theme < 14.04-10.20151001bzr455
Obsoletes:      light-metacity-theme < 14.04-10.20151001bzr455

%description -n light-theme-gnome
Includes matching Ambiance and Radiance GNOME themes.
* Ambiance is a light-on-dark theme
* Radiance is a dark-on-light theme
Introduced as the default themes in Ubuntu 10.04 LTS.


%package -n monochrome-icon-theme
Summary:        Icons for the panel, designed in a simplified monochrome style
Requires:       adwaita-icon-theme
Requires:       hicolor-icon-theme
Requires:       humanity-icon-theme

%description -n monochrome-icon-theme
Dark and Light panel icons to make your desktop beautiful.


%prep
%autosetup -n %{name}-bzr%{revision} -p0

# Remove useless Unity themes
rm -r */unity/

# Delete dead symlinks
find -L . -type l -exec rm {} \;


%build


%install
# Install GTK themes
install -dm 0755 $RPM_BUILD_ROOT%{_datadir}/themes/
cp -a Ambiance/ Radiance/ $RPM_BUILD_ROOT%{_datadir}/themes/

# Install icon themes
install -dm 0755 $RPM_BUILD_ROOT%{_datadir}/icons/
cp -a ubuntu-mono-dark/ $RPM_BUILD_ROOT%{_datadir}/icons/Monochrome-dark/
cp -a ubuntu-mono-light/ $RPM_BUILD_ROOT%{_datadir}/icons/Monochrome-light/


# /usr/share/themes/Radiance/gtk-3.0/assets was a directory on previous
# versions. It's now a symlink
# See https://fedoraproject.org/wiki/Packaging:Directory_Replacement#Scriptlet_to_replace_a_directory
%pretrans -p <lua> -n light-theme-gnome
path = "%{_datadir}/themes/Radiance/gtk-3.0/assets"
st = posix.stat(path)
if st and st.type == "directory" then
    status = os.rename(path, path .. ".rpmmoved")
    if not status then
        suffix = 0
        while not status do
            suffix = suffix + 1
            status = os.rename(path .. ".rpmmoved", path .. ".rpmmoved." .. suffix)
        end
        os.rename(path, path .. ".rpmmoved")
    end
end


%files -n light-theme-gnome
%{_datadir}/themes/*/


%files -n monochrome-icon-theme
%doc debian/changelog
%license debian/copyright
%{_datadir}/icons/Monochrome-dark/
%ghost %{_datadir}/icons/Monochrome-dark/icon-theme.cache
%{_datadir}/icons/Monochrome-light/
%ghost %{_datadir}/icons/Monochrome-light/icon-theme.cache


%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 16.10-15.20180421bzr625
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 16.10-14.20180421bzr625
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 16.10-13.20180421bzr625
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 16.10-12.20180421bzr625
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 16.10-11.20180421bzr625
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 16.10-10.20180421bzr625
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 16.10-9.20180421bzr625
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 16.10-8.20180421bzr625
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 16.10-7.20180421bzr625
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 23 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 16.10-6.20180421bzr625
- Synchronise with version bundled in Ubuntu 18.04

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 16.10-5.20171012bzr584
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 16.10-4.20171012bzr584
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 22 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 16.10-3.20171012bzr584
- Fix upgrade paths

* Thu Oct 19 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 16.10-2.20170918bzr563
- Synchronise with version bundled in Ubuntu 17.10

* Fri Jul 28 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 16.10-1.20170918bzr563
- Synchronise with version bundled in Ubuntu 17.10
- Spec clean up
- Merge gtk2, gtk3 and metacity subpackages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 14.04-7.20151001bzr455
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 22 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 14.04-6.20151001bzr455
- Synchronise with version bundled in Ubuntu 15.10

* Thu Jun 18 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 14.04-5.20150410bzr434
- Add patch to better support CSD applications
- Drop useless dependency on gtk-unico-engine
- Fix directories owned by the light-theme-gnome subpackage
- Use %%license tag

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.04-4.20150410bzr434
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 03 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 14.04-3.20150410bzr434
- Synchronise with version bundled in Ubuntu 15.04

* Mon Jan 05 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 14.04-2.20141217bzr408
- Update to the latest development version available in Ubuntu 13.10
- Drop Requires on metacity for light-metacity-theme (not needed by GNOME)

* Sun Oct 12 2014 Mohamed El Morabity <melmorabity@fedoraproject.org> - 14.04-1.20140929bzr399
- Update to the latest development version available in Ubuntu 14.10
- Drop useless Login icon theme

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.04-0.2.20140410bzr378
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 13 2014 Mohamed El Morabity <melmorabity@fedoraproject.org> - 14.04-0.1.20140410bzr378
- Synchronise with version bundled in Ubuntu 14.04

* Wed Nov 20 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 13.10-0.3.20131014bzr324
- Fix deps

* Tue Nov 12 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 13.10-0.2.20131014bzr324
- Synchronise with version bundled in Ubuntu 13.10

* Mon Sep 02 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 13.10-0.1.20130812bzr307
- Update to the latest development version available in Ubuntu 13.10

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.04-0.2.20130412bzr283
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun May 12 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 13.04-0.1.20130412bzr283
- Rebase to ubuntu-themes upstream project
- Synchronise with version bundled in Ubuntu 13.04
- Add new monochrome-icon-theme subpackage

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.93-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Sep 29 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.1.93-1
- Update to 0.1.93

* Fri Sep 21 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.1.92-1.0ubuntu1
- Update to 0.1.92-0ubuntu1

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.11-2.0ubuntu1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jul 15 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.1.11-1.0ubuntu1
- Update to 0.1.11-0ubuntu1

* Thu Feb 16 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.1.8.29-1
- Update to 0.1.8.29

* Sat Feb 04 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.1.8.27.1-1
- Update to 0.1.8.27.1

* Sun Jan 22 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.1.8.26-2
- Rebuilt

* Sun Jan 22 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.1.8.26-1
- Update to 0.1.8.26

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.8.25-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec 09 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.1.8.25-5
- Fix description in light-theme-gnome

* Tue Nov 29 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.1.8.25-4
- Rename source RPM to light-themes
- Split light-theme-gnome into four packages: light-metacity-theme,
  light-gtk2-theme, light-gtk3-theme, light-theme-gnome
- Remove useless Unity theme files

* Sun Nov 20 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.1.8.25-3
- Fix dependency on monochrome-icon-theme

* Tue Oct 11 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.1.8.25-2
- Fix dependency on mono-icon-theme

* Sun Oct 09 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.1.8.25-1
- Initial RPM release
