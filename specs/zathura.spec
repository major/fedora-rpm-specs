Name:              zathura
Version:           0.5.11
Release:           2%{?dist}
Summary:           A lightweight document viewer
License:           Zlib
URL:               http://pwmt.org/projects/%{name}/
Source0:           http://pwmt.org/projects/%{name}/download/%{name}-%{version}.tar.xz

%if %{undefined flatpak}
BuildRequires:     bash-completion
%endif
#BuildRequires:     binutils
BuildRequires:     cairo-devel
#BuildRequires:     cmake
BuildRequires:     desktop-file-utils
# Needed for mime-type detection : `libmagic` from file
BuildRequires:     file-devel
%if %{undefined flatpak}
BuildRequires:     fish
%endif
BuildRequires:     gcc
BuildRequires:     gettext
BuildRequires:     girara-devel >= 0.4.5
BuildRequires:     glib2-devel >= 2.72
BuildRequires:     gtk3-devel >= 3.24
BuildRequires:     intltool
# Needed to validate appdata
BuildRequires:     libappstream-glib
BuildRequires:     librsvg2-tools
BuildRequires:     libseccomp-devel
BuildRequires:     meson >= 0.61
# Needed to build man pages (/doc subdir)
BuildRequires:     python3-sphinx
BuildRequires:     sqlite-devel >= 3.6.23
BuildRequires:     texlive-lib-devel
BuildRequires:     zsh
# Tests
BuildRequires:     pkgconfig(check) >= 0.11
Buildrequires:     xorg-x11-server-Xvfb

Suggests:          zathura-cb
Suggests:          zathusa-djvu
# poppler is preferred over mupdf
Suggests:          zathura-pdf-poppler
Suggests:          zathura-ps

Suggests:          zathura-bash-completion
Suggests:          zathura-fish-completion
Suggests:          zathura-zsh-completion

%description
Zathura is a highly customizable and functional document viewer.
It provides a minimalistic and space saving interface as well as
an easy usage that mainly focuses on keyboard interaction.

Zathura requires plugins to support document formats.
For instance:
* zathura-pdf-poppler to open PDF files,
* zathura-ps to open PostScript files,
* zathura-djvu to open DjVu files, or
* zathura-cb to open comic book files.

All of these are available as separate packages in Fedora.
A zathura-plugins-all package is available should you want
to install all available plugins.

%package devel
Summary:           Development files for the zathura PDF viewer
Requires:          %{name}%{?_isa} = %{version}-%{release}
Requires:          pkgconfig

%description devel
libraries and header files for the zathura PDF viewer.

%package plugins-all
Summary:           Zathura plugins (all plugins)
Requires:          zathura-cb
Requires:          zathura-djvu
# poppler is preferred over mupdf
Requires:          zathura-pdf-poppler
Requires:          zathura-ps

%description plugins-all
This package installs all available Zathura plugins.

%package bash-completion
Summary:           bash-completion files for zathura
BuildArch:         noarch
Requires:          bash-completion
Requires:          %{name} = %{version}-%{release}

%description bash-completion
This package provides %{summary}.

%package fish-completion
Summary:           fish-completion files for zathura
BuildArch:         noarch
Requires:          fish
Requires:          %{name} = %{version}-%{release}

%description fish-completion
This package provides %{summary}.

%package zsh-completion
Summary:           zsh-completion files for zathura
BuildArch:         noarch
Requires:          zsh
Requires:          %{name} = %{version}-%{release}

%description zsh-completion
This package provides %{summary}.

%prep
%autosetup

%build
%meson -Dsynctex=enabled -Dseccomp=enabled -Dtests=enabled
%meson_build

%install
%meson_install
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%find_lang zathura

%check
# Leave out flaky sandbox test which is either skipped or fails strangely:
%meson_test validate-desktop validate-appdata document types utils session

%files -f zathura.lang
%license LICENSE
%doc README.md
%{_bindir}/*
%{_mandir}/man*/*
%{_datadir}/applications/*
#Directories without known owners: /usr/share/dbus-1, /usr/share/dbus-1/interfaces.  Would Requires dbus ?
%{_datadir}/dbus-1/interfaces/org.pwmt.zathura.xml
%{_datadir}/icons/hicolor/*/apps/org.pwmt.zathura.png
%{_datadir}/icons/hicolor/*/apps/org.pwmt.zathura.svg
%{_datadir}/metainfo/org.pwmt.zathura.appdata.xml

%files devel
%{_includedir}/zathura
%{_libdir}/pkgconfig/zathura.pc

%files plugins-all

%files bash-completion
%{_datadir}/bash-completion/completions/zathura

%files fish-completion
%{_datadir}/fish/vendor_completions.d/zathura.fish

%files zsh-completion
%{_datadir}/zsh/site-functions/_zathura


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Dec 18 2024 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.5.11-1
- Update to 0.5.11 (rh#2302671)

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu May 30 2024 Michael J Gruber <mjg@fedoraproject.org> - 0.5.6-2
- Fix build on i686

* Thu May 09 2024 Michael J Gruber <mjg@fedoraproject.org> - 0.5.6-1
- feat: update to 0.5.6 (rhbz#2279581)

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Dec 09 2023 Michael J Gruber <mjg@fedoraproject.org> - 0.5.4-1
- feat: update to 0.5.4 (rhbz#2253676)
- enable test suite

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jan 30 2023 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.5.2-4
- Rebuild for girara 0.3.9

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 03 2022 Alain Vigne <avigne@fedoraproject.org> - 0.5.2-2
- Fix noarch build

* Thu Dec 01 2022 Alain Vigne <avigne@fedoraproject.org> - 0.5.2-1
- Update to 0.5.2 (rhbz#2125415)
- SPDX license identifier

* Tue Jul 26 2022 Alain Vigne <avigne@fedoraproject.org> - 0.4.9-1
- Update to 0.4.9

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Nov 10 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.4.8-2
- Fix build

* Tue Oct 5 2021 Mosaab Alzoubi <moceap [AT] fedoraproject [DOT] org> - 0.4.8-1
- Update to 0.4.8

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Oct 31 2020 Petr Šabata <contyk@redhat.com> - 0.4.7-1
- 0.4.7 bump

* Mon Sep 21 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.4.6-2
- Remove no longer needed fish workaround
- Use new vendor completion directory for fish

* Mon Aug 17 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.4.6-1
- Update to new upstream release

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 15 2020 Petr Šabata <contyk@redhat.com> - 0.4.5-1
- 0.4.5 bump
- Introduce the fish-completion subpackage

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 07 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.4.3-4
- Includes patch to correctly set the application ID
- Corrects icon and application window grouping on wayland

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Petr Šabata <contyk@redhat.com> - 0.4.3-1
- 0.4.3 bump
- Now includes more icons!
- Based on Ankur Sinha's PR, https://src.fedoraproject.org/rpms/zathura/pull-request/1

* Fri Nov 16 2018 Petr Šabata <contyk@redhat.com> - 0.4.1-1
- 0.4.1 bump
- Introducing bash and zsh completion subpackages
- Fixes rhbz#1649839

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 25 2018 Petr Šabata <contyk@redhat.com> - 0.4.0-1
- 0.4.0 bump
- Dropping the icon patch (included upstream)

* Tue Apr 24 2018 Petr Šabata <contyk@redhat.com> - 0.3.9-2
- Validate the desktop file
- Install the icon into the correct location

* Mon Apr 09 2018 Petr Šabata <contyk@redhat.com> - 0.3.9-1
- 0.3.9 bump

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 15 2017 Petr Šabata <contyk@redhat.com> - 0.3.7-1
- 0.3.7 bump

* Tue Apr 19 2016 Petr Šabata <contyk@redhat.com> - 0.3.6-1
- 0.3.6 bump

* Fri Feb 26 2016 Petr Šabata <contyk@redhat.com> - 0.3.5-1
- 0.3.5 bump
- Add very weak dependencies (via suggests) on the plugins

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Petr Šabata <contyk@redhat.com> - 0.3.4-2
- Re-enable synctex support via libsynctex

* Mon Dec 21 2015 Petr Šabata <contyk@redhat.com> - 0.3.4-1
- 0.3.4 bump

* Wed Jul 01 2015 Petr Šabata <contyk@redhat.com> - 0.3.3-3
- Zathura should create and own the plugin directory

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 09 2015 Petr Šabata <contyk@redhat.com> - 0.3.3-1
- 0.3.3 bump
- Fix the dep list, install LICENSE with the %%license macro

* Wed Nov 12 2014 Petr Šabata <contyk@redhat.com> - 0.3.2-1
- 0.3.2 bugfix bump

* Fri Oct 31 2014 Petr Šabata <contyk@redhat.com> - 0.3.1-1
- 0.3.1 bugfix bump

* Fri Oct 17 2014 Petr Šabata <contyk@redhat.com> - 0.3.0-1
- 0.3.0 bump

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 26 2014 Petr Šabata <contyk@redhat.com> - 0.2.9-1
- 0.2.9 bump

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 07 2014 François Cami <fcami@fedoraproject.org> - 0.2.7-4
- Add zathura-cb to zathura-plugins-all.

* Sun Mar 23 2014 François Cami <fcami@fedoraproject.org> - 0.2.7-3
- Gratuitous release bump.

* Thu Mar 06 2014 François Cami <fcami@fedoraproject.org> - 0.2.7-2
- Rebuilt for rawhide.

* Wed Mar 05 2014 François Cami <fcami@fedoraproject.org> - 0.2.7-1
- Update to 0.2.7.

* Sat Dec 28 2013 François Cami <fcami@fedoraproject.org> - 0.2.6-1
- Update to latest upstream.

* Sat Aug 31 2013 François Cami <fcami@fedoraproject.org> - 0.2.4-1
- New upstream release

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 28 2013 François Cami <fcami@fedoraproject.org> - 0.2.3-6
- backport cdece5922982b06e1a86dfb7dfc8cf3d225f06f0

* Tue May 28 2013 François Cami <fcami@fedoraproject.org> - 0.2.3-5
- backport cf96d52790bc8d05a9e556e33af0b6fec1a4cb0e

* Tue May 28 2013 François Cami <fcami@fedoraproject.org> - 0.2.3-4
- rewrite summary.

* Mon May 27 2013 François Cami <fcami@fedoraproject.org> - 0.2.3-3
- add a zathura-plugins-all subpackage.

* Mon May 27 2013 François Cami <fcami@fedoraproject.org> - 0.2.3-2
- rewrite description.

* Tue May 21 2013 Petr Šabata <contyk@redhat.com> - 0.2.3-1
- 0.2.3 build
- Use more macros

* Sun May 12 2013 François Cami <fcami@fedoraproject.org> - 0.2.2-2
- add a note about plugins to avoid future occurrences of #962097

* Fri Feb 22 2013 Kevin Fenzi <kevin@scrye.com> 0.2.2-1
- Update to 0.2.2

* Thu Feb 14 2013 Michal Schmidt <mschmidt@redhat.com> 0.2.1-2
- fix building of manpages
- use parallel make

* Mon Nov 05 2012 Kevin Fenzi <kevin@scrye.com> 0.2.1-1
- Update to 0.2.1

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.8.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May 16 2012 Marek Kasik <mkasik@redhat.com> - 0.0.8.5-4
- Rebuild (poppler-0.20.0)

* Sat Mar 31 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.0.8.5-3
- Fix FTBFS on recent releases
- Update URLs
- Cleanup SPEC

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 15 2011 François Cami <fcami@fedoraproject.org> - 0.0.8.5-1
- Update to latest upstream.

* Fri Oct 28 2011 Rex Dieter <rdieter@fedoraproject.org> - 0.0.8.3-6
- rebuild(poppler)

* Fri Sep 30 2011 Marek Kasik <mkasik@redhat.com> - 0.0.8.3-5
- Rebuild (poppler-0.18.0)

* Mon Sep 19 2011 Marek Kasik <mkasik@redhat.com> - 0.0.8.3-4
- Rebuild (poppler-0.17.3)

* Fri Jul 15 2011 Marek Kasik <mkasik@redhat.com> - 0.0.8.3-3
- Rebuild (poppler-0.17.0)

* Sat Apr 02 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.0.8.3-2
- It's update-desktop-database, not update-mime-database

* Fri Apr 01 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.0.8.3-1
- Update to 0.0.8.3
- Drop patch for poppler >= 0.15 (no longer needed)
- Run update-mime-database in %%post and %%postun

* Sun Mar 13 2011 Marek Kasik <mkasik@redhat.com> - 0.0.8.2-5
- Rebuild (poppler-0.16.3)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 01 2011 Rex Dieter <rdieter@fedoraproject.org> - 0.0.8.2-3
- rebuild (poppler)

* Wed Dec 15 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.0.8.2-2
- rebuild (poppler)

* Wed Dec 01 2010 François Cami <fcami@đedoraproject.ort> - 0.0.8.2-1
- new upstream version + drop merged patch (dso build fix)

* Sat Nov 06 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.0.8.1-8
- rebuilt (poppler)

* Wed Oct  6 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 0.0.8.1-7
- rebuild and fix for new poppler

* Fri Aug 20 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.0.8.1-6
- rebuild (poppler)

* Sun Aug 15 2010 François Cami <fcami@fedoraproject.org> 0.0.8.1-5
- switch to sed (Kevin Fenzi).
- use desktop-file-validate on the desktop file (Kevin Fenzi).

* Sun Aug 15 2010 François Cami <fcami@fedoraproject.org> 0.0.8.1-4
- change zathura.desktop Version to 1.0.

* Sat Aug 14 2010 François Cami <fcami@fedoraproject.org> 0.0.8.1-3
- add CFLAGS (Kevin Fenzi).
- use the debug target to generate the debuginfo rpm properly.
- add zathura.desktop file and install it.

* Sat Aug 14 2010 François Cami <fcami@fedoraproject.org> 0.0.8.1-2
- fix licensing, thanks to Dennis Johnson's review.

* Tue Aug 10 2010 François Cami <fcami@fedoraproject.org> 0.0.8.1-1
- initial package.

