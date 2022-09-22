Name:		shaman
Version:	1.1
Release:	16%{?dist}
Summary:	Man pages viewer

License:	GPLv3+
URL:		http://sites.google.com/site/mohammedisam2000/home/projects/
Source0:	%{url}/%{name}-%{version}.tar.gz
BuildArch:	noarch
ExclusiveArch:  %{java_arches} noarch

Requires: java-1.8.0
Requires: hicolor-icon-theme
BuildRequires: make
BuildRequires: desktop-file-utils, libappstream-glib, texinfo
BuildRequires: java-devel, javapackages-tools

%description
Shaman is a software package that allows the user to view, search and run 
through the manual pages that are installed on the system in a Graphical User 
Interface (GUI). The aim is to make reading man pages an easy task for 
newcomers to the GNU/Linux system.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
install -m 0644 -p -D info/shaman.info* %{buildroot}%{_infodir}/shaman.info
install -d %{buildroot}%{_mandir}/man1/
install -d %{buildroot}%{_docdir}/shaman/
install -m 0644 -p -D man/man1/shaman.1* %{buildroot}%{_mandir}/man1/
#install the JAR
mkdir -p %{buildroot}%{_javadir}/
install -p -m 644 shaman.jar %{buildroot}%{_javadir}/shaman.jar

#install app icons
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/24x24/apps/
cp -p shaman-256.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/shaman.png
cp -p shaman-48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/shaman.png
cp -p shaman-24.png %{buildroot}%{_datadir}/icons/hicolor/24x24/apps/shaman.png
mkdir -p %{buildroot}%{_datadir}/metainfo/
mkdir -p %{buildroot}%{_datadir}/appdata/
cp -p shaman.appdata.xml %{buildroot}%{_datadir}/metainfo/shaman.appdata.xml
#cp -p shaman.appdata.xml %%{buildroot}%%{_datadir}/appdata/shaman.appdata.xml
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml

%jpackage_script mima.shaman.Shaman "" "" %{name} shaman true

%files
%{_bindir}/*
%{_javadir}/*
%{_mandir}/man1/shaman.1*
%{_infodir}/*
%{_docdir}/shaman
%{_datadir}/applications/%{name}.desktop
%{_metainfodir}/%{name}.appdata.xml
#%%{_datadir}/appdata/%%{name}.appdata.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%%doc AUTHORS NEWS README ChangeLog

%license COPYING

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 1.1-15
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.1-14
- Rebuilt for java-17-openjdk as system jdk

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 1.1-9
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jul 07 2018 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.1-4
- Removed install directions of appdata.xml file

* Sat Jul 07 2018 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.1-3
- Fixed install directions of appdata.xml file

* Sat Jul 07 2018 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.1-2
- Added installing appdata.xml file to appdata dir, to fix build
  error on f27

* Thu Jun 28 2018 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.1-1
- Changed BuildArch to noarch
- Fixed .desktop file
- Removed THANKS file from install

* Tue Jun 26 2018 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.0-5
- Fixed the spec file (added %%jpackage_script BuildRequires clause)

* Tue Jun 26 2018 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.0-4
- Fixed the spec file (added BuildRequires clauses)

* Tue Jun 26 2018 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.0-3
- Fixed the spec file

* Sun Jun 10 2018 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.0-2
- Fixed the spec file

* Mon Jun 4 2018 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.0-1
- First release
