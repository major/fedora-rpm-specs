%global date 20170403
%global commit0 964d4ef967618e0f43322ea4d4a67e74c06b13dd
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           plantumlqeditor
Version:        1.2
Release:        32.%{date}git%{shortcommit0}%{?dist}
Summary:        Simple editor for PlantUML
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://sourceforge.net/projects/plantumlqeditor/
Source:         https://github.com/borco/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{version}-%{date}git%{shortcommit0}.tar.gz
Patch0:         %{name}-use-system-wide-qtsingleapplication-library.patch

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  /usr/bin/git
BuildRequires:  desktop-file-utils
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-linguist
BuildRequires:  qtsingleapplication-qt5-devel
BuildRequires:  libappstream-glib
# For substituting %%{_javadir} in settings.
BuildRequires:  javapackages-filesystem

Requires:       shared-mime-info
Requires:       hicolor-icon-theme
Requires:       graphviz
Requires:       plantuml


%description
PlantUML QEditor is a simple editor written in Qt5 for PlantUML.

At a glance:

- simple PlantUML editor, with a preview,
- update the diagram while editing,
- code assistant to insert ready-made code snippets,
- written in Qt5, so it should run on all platforms supported by Qt5 and
  PlantUML.

The editor is quite simple: it monitors the editor for changes, and, if any,
runs plantuml to regenerate the image.

The editor also supports an assistant that allows easy insertion of code
snippets into the editor. The assistant is defined by a simple XML and a bunch
of icons, one for each snippet.


%prep
%autosetup -S git -n %{name}-%{commit0}
# remove bundled qtsingleapplication library sources
rm -rf thirdparty/qtsingleapplication

# Set the default configuration values
# so it's ready to use without any extra configuration steps
sed -i "s#/usr/bin/plantuml#%{_javadir}/plantuml.jar#g" settingsconstants.h
sed -i "s#\(reloadAssistantXml(settings.value(SETTINGS_ASSISTANT_XML_PATH\)\().toString());\)#\1, QVariant(\"%{_datadir}/%{name}/assistant.xml\")\2#g" mainwindow.cpp
sed -i "s#\"translations\"#\"%{_datadir}/%{name}/translations\"#g" main.cpp


%build
%{qmake_qt5}
%make_build
lrelease-qt5 translations/*.ts


%install
# install main executable
install -p -m 0755 -D %{name} %{buildroot}%{_bindir}/%{name}

# install assistant data
install -p -m 0644 -D assistant.xml %{buildroot}%{_datadir}/%{name}/assistant.xml
cp -ar icons %{buildroot}%{_datadir}/%{name}/

# install desktop files
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  %{name}.desktop

# install icon file
install -p -m 0644 -D icon.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

# install mimetype association
install -p -m 0644 -D plantumlqeditor-mime.xml %{buildroot}%{_datadir}/mime/packages/%{name}.xml

# install translations
mkdir -p %{buildroot}%{_datadir}/%{name}/translations/
cp -a translations/*.qm %{buildroot}%{_datadir}/%{name}/translations/
%find_lang %{name} --with-qt --without-mo

# install and validate appdata
install -p -m 0644 -D %{name}.appdata.xml %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml

%files -f %{name}.lang
%license COPYING
%doc AUTHORS.md README.md
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/assistant.xml
%dir %{_datadir}/%{name}/icons
%{_datadir}/%{name}/icons/*
%{_datadir}/appdata/*.appdata.xml
%dir %{_datadir}/%{name}/translations


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-32.20170403git964d4ef
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2-31.20170403git964d4ef
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-30.20170403git964d4ef
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-29.20170403git964d4ef
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-28.20170403git964d4ef
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-27.20170403git964d4ef
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-26.20170403git964d4ef
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 10 2023 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.2-25.20170403git964d4ef
- Add BR javapackages-filesystem for substituting correctly %%{_javadir}

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-24.20170403git964d4ef
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-23.20170403git964d4ef
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-22.20170403git964d4ef
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-21.20170403git964d4ef
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-20.20170403git964d4ef
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-19.20170403git964d4ef
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-18.20170403git964d4ef
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 12 2019 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.2-17.20170403git964d4ef
- Rebuild (2nd attempt)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-16.20170403git964d4ef
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-15.20170403git964d4ef
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Feb 24 2018 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.2-14.20170403git964d4ef
- Add missing BR (gcc-c++)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-13.20170403git964d4ef
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2-12.20170403git964d4ef
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-11.20170403git964d4ef
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-10.20170403git964d4ef
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.2-9.20170403git964d4ef
- Remove superfluous {_datadir}/icons/hicolor/scalable/apps

* Tue May 09 2017 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.2-8.20170403git964d4ef
- Switch to use qmake build system.

* Tue Apr 04 2017 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.2-7.20170403git964d4ef
- Use unbundled qtsingleapplication library.

* Tue Apr 04 2017 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.2-6.20170403git964d4ef
- Update to the latest version (fixes license header in source files).

* Mon Mar 06 2017 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.2-5.20170227git95b9e7c
- Update to the latest version (upstream merged AppData PR),
- Adjust to the latest Packaging:Versioning guideline.

* Sat Feb 25 2017 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.2-4.git8dc124b
- Updated references to AppData screenshots 

* Thu Feb 23 2017 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.2-3.git8dc124b
- AppData added.

* Wed Feb 22 2017 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.2-2.git8dc124b
- Initial RPM release.
