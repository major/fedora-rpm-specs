Name:           gcstar
Version:        1.7.1
Release:        21%{?dist}
Summary:        Personal collections manager

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.gcstar.org/
Source0:        http://download.gna.org/gcstar/gcstar-%{version}.tar.gz
Patch0:         gcstar.path.patch
# We patch gcstar to allow comic volumes to number 1000000
# https://bugzilla.redhat.com/show_bug.cgi?id=1232956
Patch1:         gcstar-comics-volume.patch
BuildArch:      noarch

Requires:      hicolor-icon-theme
Requires:      perl-Gtk2
Provides:      perl(GCItemsLists::GCImageLists) = %{version}
Provides:      perl(GCItemsLists::GCTextLists) = %{version}
Provides:      perl(GCPlugins::GCfilms::GCThemoviedb) = %{version}
Provides:      perl(GCItemsLists::GCListOptions) = %{version}
Provides:      perl(GCItemsLists::GCImageListComponents) = %{version}
Provides:      perl(GCGraphicComponents::GCDoubleLists) = %{version}
Provides:      perl(GCGraphicComponents::GCBaseWidgets) = %{version}
# The last version of gcfilms was 6.4
Obsoletes:     gcfilms <= 6.4
BuildRequires: coreutils
BuildRequires: desktop-file-utils
BuildRequires: perl-generators

%description
GCstar is an application for managing your personal collections.
Detailed information on each item can be automatically retrieved
from the internet and you can store additional data, depending on
the collection type. And also who you've lent your them to. You
may also search and filter your collection by criteria.

%prep
%setup -q -n gcstar
%patch -P0 -p1 -b .path
%patch -P1 -p1


%build

%install
%{__mkdir_p} %{buildroot}%{_prefix}
%{__install} -d %{buildroot}%{_bindir}
%{__install} bin/gcstar %{buildroot}%{_bindir}
%{__install} -d %{buildroot}%{_datadir}
%{__cp} -a share/gcstar %{buildroot}%{_datadir}
chmod 755 %{buildroot}%{_datadir}/%{name}/xslt/applyXSLT.pl
%{__install} -d %{buildroot}%{_datadir}/%{name}/lib
%{__cp} -a lib/gcstar/* %{buildroot}%{_datadir}/%{name}/lib
%{__install} -d %{buildroot}%{_mandir}/man1
%{__install} -m 644 man/gcstar.1 %{buildroot}%{_mandir}/man1
gzip %{buildroot}%{_mandir}/man1/gcstar.1

# Install menu entry
%{__cat} > %{name}.desktop << EOF
[Desktop Entry]
Name=GCstar
Comment=Manage your collections
GenericName=Personal collections manager
Exec=gcstar
Icon=gcstar
Terminal=false
Type=Application
MimeType=application/x-gcstar
Categories=Application;Office;
Encoding=UTF-8
EOF

%{__mkdir_p} %{buildroot}%{_datadir}/applications
desktop-file-install \
    --dir %{buildroot}%{_datadir}/applications  \
    %{name}.desktop

#Mime Type
%{__cat} > %{name}.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<mime-info xmlns="http://www.freedesktop.org/standards/shared-mime-info">
        <mime-type type="application/x-gcstar">
                <comment>GCstar collection</comment>
                <glob pattern="*.gcs"/>
        </mime-type>
</mime-info>
EOF

%{__mkdir_p} %{buildroot}%{_datadir}/mime/packages
cp %{name}.xml %{buildroot}%{_datadir}/mime/packages

# Install app icons
for i in 16 22 24 32 36 48 64 72 96 128 192 256; do
    mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps
    %{__install} -m 644 share/gcstar/icons/%{name}_${i}x${i}.png %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/%{name}.png
done

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
%{__install} -m 644 share/gcstar/icons/gcstar_scalable.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%files
%doc CHANGELOG README
%license LICENSE
%{_datadir}/gcstar
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man1/gcstar.1.gz
%attr(0755,root,root) %{_bindir}/gcstar
%attr(0755,root,root) %{_datadir}/gcstar/helpers/xdg-open
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.7.1-20
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 26 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 1.7.1-2
- Patch gcstar to allow comic book volumes to number 1000000

* Fri Apr 15 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 1.7.1-1
- Update to 1.7.1

* Mon Mar 21 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 1.7.0-13
- Use the program name as the icon name for the scalable icon
- Remove the symbolic icon(which isn't symbolic at all)

* Sat Mar 19 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 1.7.0-12
- Use the program short name as icon tag (#1276144)
- Add coreutils to the BuildRequires
- Use %%license tag

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Oct 02 2014 Rex Dieter <rdieter@fedoraproject.org> 1.7.0-9
- update mime scriptlet

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug 21 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 1.7.0-7
- Indent specfile to improve readability
- Add versions to Requires and Obsoletes
- Remove no-longer-used macros

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.7.0-5
- Perl 5.18 rebuild

* Tue Apr 09 2013 Jon Ciesla <limburgher@gmail.com> - 1.7.0-4
- Drop desktop vendor tag.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Sep 09 2012 Tian <tian@c-sait.net> - 1.7.0-2
  - Explicitely added some internal dependencies required on rawhide

* Wed Sep 05 2012 Tian <tian@c-sait.net> - 1.7.0-1
  - New upstream version http://svn.gna.org/viewcvs/*checkout*/gcstar/tags/GCstar_1_7_0/CHANGELOG

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Aug 07 2011 Tian <tian@c-sait.net> - 1.6.2-1
  - New upstream version http://svn.gna.org/viewcvs/*checkout*/gcstar/tags/GCstar_1_6_2/CHANGELOG
* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Sep 04 2010 Tian <tian@c-sait.net> - 1.6.1-2
  - Added Provides directive as it was not correctly detected
* Wed Sep 01 2010 Tian <tian@c-sait.net> - 1.6.1-1
  - New upstream version http://svn.gna.org/viewcvs/*checkout*/gcstar/tags/GCstar_1_6_1/CHANGELOG
* Sun Nov 29 2009 Tian <tian@c-sait.net> - 1.5.0-2
  - Added Provides directive as it was not correctly detected
* Sat Nov 28 2009 Tian <tian@c-sait.net> - 1.5.0-1
  - New upstream version http://svn.gna.org/viewcvs/*checkout*/gcstar/tags/GCstar_1_5_0/CHANGELOG
* Wed Nov 11 2009 Tian <tian@c-sait.net> - 1.4.3-4
  - Bug 531875
* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Oct 11 2008 Tian <tian@c-sait.net> - 1.4.3-1
  -  Bug 466364
  - New upstream version http://svn.gna.org/viewcvs/*checkout*/gcstar/tags/GCstar_1_4_3/CHANGELOG
* Wed Jul 23 2008 Tian <tian@c-sait.net> - 1.4.1-1
  - New upstream version http://svn.gna.org/viewcvs/*checkout*/gcstar/tags/GCstar_1_4_1/CHANGELOG
* Tue Jun 3  2008 Tian <tian@c-sait.net> - 1.4.0-1
  - New upstream version
* Fri Jan 25 2008 Tian <tian@c-sait.net> - 1.3.2-1
  - New upstream version
* Mon Nov 26 2007 Tian <tian@c-sait.net> - 1.3.0-1
  - New upstream version
* Mon Sep 17 2007 Tian <tian@c-sait.net> - 1.2.2-1
  - New upstream version
* Sun Sep 09 2007 Tian <tian@c-sait.net> - 1.2.0-1
  - New upstream version
* Thu Aug 16 2007 Tian <tian@c-sait.net> - 1.1.1-4
  - Updated license tag
* Sun May 27 2007 Tian <tian@c-sait.net> - 1.1.1-3
  - Added Obsoletes tag
* Fri Feb 23 2007 Tian <tian@c-sait.net> - 1.1.1-2
  - Execution bit on xdg-open
* Fri Feb 16 2007 Tian <tian@c-sait.net> - 1.1.1-1
  - New upstream version
* Sat Dec 16 2006 Tian <tian@c-sait.net> - 1.0.0-1
  - New upstream version
* Sat Oct 28 2006 Tian <tian@c-sait.net> - 0.5.0-4
  - Re-creation of the module because of a problem with previous import
* Sun Oct 22 2006 Tian <tian@c-sait.net> - 0.5.0-3
  - Restored BuildRequires
* Sat Oct 21 2006 Tian <tian@c-sait.net> - 0.5.0-2
  - Changed desktop vendor
  - Removed desktop-file-utils and shared-mime-info from required
  - Fixed icon path in desktop file
* Sat Oct 21 2006 Tian <tian@c-sait.net> - 0.5.0-1
  - First Fedora Extras version.
