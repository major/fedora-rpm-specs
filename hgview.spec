%define curses 1
Name:           hgview
Version:        1.14.0
Release:        13%{?dist}
Summary:        Mercurial interactive Qt based history viewer

License:        GPLv2+
URL:            http://www.logilab.org/project/hgview
Source0:        http://download.logilab.org/pub/%{name}/%{name}-%{version}.tar.gz
# http://www.logilab.org/ticket/112566
Source1:        %{name}.png
# http://www.logilab.org/ticket/103668
Patch1:         hgview-man-path.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-PyQt5-devel
BuildRequires:  asciidoc
BuildRequires:  xmlto
BuildRequires:  mercurial
BuildRequires:  desktop-file-utils

Requires:       %{name}-common = %{version}-%{release}
Requires:       python3-docutils
Requires:       python3-PyQt5
Requires:       python3-qscintilla-qt5

%if %{curses}
%else
Obsoletes:      %{name}-curses <= %{version}
Provides:       %{name}-curses == %{version}
%endif

%description
hgview is a simple tool aiming at visually navigating Mercurial repository
history. It has been written with efficiency in mind, both in terms
of computational efficiency and user experience efficiency.

This main package provides a Qt based GUI.
%if %{curses}
A curses based UI is also available.
%endif

%if %{curses}
%package -n %{name}-curses
Summary:        Mercurial interactive curses based history viewer
Requires:       %{name}-common = %{version}-%{release}
Requires:       python3-urwid, python3-pygments, python3-inotify

%description -n %{name}-curses
hgview is a simple tool aiming at visually navigating Mercurial repository
history. It has been written with efficiency in mind, both in terms
of computational efficiency and user experience efficiency.

This package provides a curses based UI. A Qt based GUI is also available.
%endif


%package -n %{name}-common
Summary:        Common files for the hgview Mercurial interactive history viewer
Requires:       mercurial

%description -n %{name}-common
hgview is a simple tool aiming at visually navigating Mercurial repository
history. It has been written with efficiency in mind, both in terms
of computational efficiency and user experience efficiency.

This package provides common files for the Qt and curses based UIs.


%prep
%setup -q
%patch1


%build
%{__python3} setup.py build


%install
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

# Mercurial do not have a noarch hgext directory - storing the extension in
# hgviewlib seems like the least bad option.
mv $RPM_BUILD_ROOT%{python3_sitelib}/hgext3rd/hgview $RPM_BUILD_ROOT%{python3_sitelib}/hgviewlib/
rm $RPM_BUILD_ROOT%{python3_sitelib}/hgext3rd/__init__.py
rm $RPM_BUILD_ROOT%{python3_sitelib}/hgext3rd/__pycache__/__init__.*.py*
rmdir $RPM_BUILD_ROOT%{python3_sitelib}/hgext3rd/__pycache__

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/mercurial/hgrc.d/
cat > $RPM_BUILD_ROOT%{_sysconfdir}/mercurial/hgrc.d/hgview.rc << EOT
[extensions]
# Enable hgview extension to be able to invoke hgview as 'hg hgview' or 'hg qv'.
#hgview = %{python3_sitelib}/hgviewlib/hgview.py

[hgview]
# hgview will by default use the qt interface if available - set interface to
# curses for console mode.
#interface = qt
#interface = curses
EOT

# http://www.logilab.org/ticket/112566
cat > %{name}.desktop << EOT
[Desktop Entry]
Type=Application
Name=hgview
GenericName=Version Control GUI
Comment=GUI application for using Mercurial
Icon=hgview
Exec=hgview -I qt
Categories=Development;RevisionControl;
EOT
desktop-file-install --dir=$RPM_BUILD_ROOT%{_datadir}/applications %{name}.desktop

install -m 644 -D -p %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<!--
BugReportURL: https://www.logilab.org/ticket/265434
SentUpstream: 2014-09-18
-->
<application>
  <id type="desktop">hgview.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <name>HgView</name>
  <summary>Graphical tree viewer for Mecurial repositories</summary>
  <description>
    <p>
     HgView is a tool to visually navigate the tree and history of a Mecurial repository.
     HgView has a wide range of features for browsing and interacting with a Mecurial
     repository graphically, including:
    <ul>
      <li>Key-based navigation of the revisions history of a repository</li>
      <li>Automatic refresh of the revision graph when the repository is modified</li>
      <li>Display of the current working directory as a special node in the graph</li>
    </ul>
    </p>
  </description>
  <url type="homepage">http://www.logilab.org/project/hgview</url>
  <screenshots>
    <screenshot type="default">https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/hgview/a.png</screenshot>
  </screenshots>
  <!-- FIXME: change this to an upstream email address for spec updates
  <updatecontact>someone_who_cares@upstream_project.org</updatecontact>
   -->
</application>
EOF

rm $RPM_BUILD_ROOT%{_datadir}/doc/%{name}/examples/description.css


%files
%{python3_sitelib}/hgviewlib/qt5/
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%if %{curses}
%files -n %{name}-curses
%{python3_sitelib}/hgviewlib/curses/
%else
%exclude %{python3_sitelib}/hgviewlib/curses/
%endif

%files -n %{name}-common
%doc COPYING README.rst
%{_mandir}/man1/%{name}.1.*
%config(noreplace) %{_sysconfdir}/mercurial/hgrc.d/hgview.rc
%{_bindir}/%{name}
%{python3_sitelib}/%{name}-*.egg-info
%dir %{python3_sitelib}/hgviewlib/
%{python3_sitelib}/hgviewlib/*.py
%{python3_sitelib}/hgviewlib/__pycache__/
%{python3_sitelib}/hgviewlib/hgview/
%{python3_sitelib}/hgviewlib/hgpatches


%changelog
* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 1.14.0-11
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 1.14.0-8
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.14.0-5
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan  3 04:21:47 CET 2021 Mads Kiilerich <mads@kiilerich.com> - 1.14.0-3
- Switch to require mercurial instead of mercurial-py3

* Mon Oct  5 14:14:38 CEST 2020 Mads Kiilerich <mads@kiilerich.com> - 1.14.0-2
- BuildRequires:  python3-setuptools

* Sat Aug 01 2020 Mads Kiilerich <mads@kiilerich.com> - 1.14.0-1
- hgview 1.14.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-0.20200509hg5b29e57a74ae
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.14-0.20200508hg5b29e57a74ae
- Rebuilt for Python 3.9

* Wed May 06 2020 Mads Kiilerich <mads@kiilerich.com> - 1.14-0.20200507hg5b29e57a74ae
- hgview 1.14 development shapshot with Qt5 support - Fedora no longer supports Qt4

* Wed Feb 12 2020 Mads Kiilerich <mads@kiilerich.com> - 1.13.1-1
- hgview 1.13.1
- depend on python3-PyQt4

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 17 2019 Mads Kiilerich <mads@kiilerich.com> - 1.13.0-2
- switch to Python 3 and re-enable curses UI

* Sun Nov 17 2019 Mads Kiilerich <mads@kiilerich.com> - 1.13.0-1
- hgview 1.13.0
- workaround for sip module moving into PyQt4

* Sun Oct 13 2019 Mads Kiilerich <mads@kiilerich.com> - 1.12.0-4
- Fix macro usage to actually skip hgview-curses ...

* Sat Oct 05 2019 Mads Kiilerich <mads@kiilerich.com> - 1.12.0-3
- Obsolete / provide hgview-curses from main package to give smooth upgrade path

* Sat Oct 05 2019 Mads Kiilerich <mads@kiilerich.com> - 1.12.0-2
- Drop hgview-curses - python2-urwid is gone and we have no python3 Mercurial

* Sat Sep 07 2019 Mads Kiilerich <mads@kiilerich.com> - 1.12.0-1
- hgview 1.12.0

* Fri Aug 09 2019 Mads Kiilerich <mads@kiilerich.com> - 1.10.6-1
- hgview 1.10.6

* Fri Jul 26 2019 Mads Kiilerich <mads@kiilerich.com> - 1.10.5-4
- hgview 1.10.5
- Clarify python2-sip is needed
- Additional fixes that has been proposed upstream

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 16 2018 Mads Kiilerich <mads@kiilerich.com> - 1.10.2-1
- hgview 1.10.2

* Mon Jul 16 2018 Mads Kiilerich <mads@kiilerich.com> - 1.9.0-8
- Clarify python2 dependency - fix build failure

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Mads Kiilerich <mads@kiilerich.com> - 1.9.0-1
- hgview 1.9.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 1.8.2-2
- Add an AppData file for the software center

* Sun Aug 31 2014 Mads Kiilerich <mads@kiilerich.com> - 1.8.2-1
- hgview 1.8.2

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Mads Kiilerich <mads@kiilerich.com> - 1.8.1-1
- hgview 1.8.1

* Sat Feb 08 2014 Mads Kiilerich <mads@kiilerich.com> - 1.8.0-1
- hgview 1.8.0

* Sun Sep 01 2013 Mads Kiilerich <mads@kiilerich.com> - 1.7.1-6
- First official Fedora package

* Sat Jun 22 2013 Mads Kiilerich <mads@kiilerich.com> - 1.7.1-5
- Don't assume there is a noarch hgext directory - just use hgviewlib.

* Wed Jun 12 2013 Mads Kiilerich <mads@kiilerich.com> - 1.7.1-4
- Update python dependency to python2-devel
- Preserve timestamp of pixmap png

* Sun Jun 09 2013 Mads Kiilerich <mads@kiilerich.com> - 1.7.1-3
- Move duplicate files to -common package

* Wed Jun 05 2013 Mads Kiilerich <mads@kiilerich.com> - 1.7.1-2
- Relax the requirements to Mercurial version
- Use explicit path to hg extension to make it work on 64 bit

* Sat Mar 09 2013 Mads Kiilerich <mads@kiilerich.com> - 1.7.1-1
- hgview-1.7.1

* Sat Nov 24 2012 Mads Kiilerich <mads@kiilerich.com> - 1.7.0-1
- hgview-1.7.0

* Mon Nov 05 2012 Mads Kiilerich <mads@kiilerich.com> - 1.6.2-2
- claim support for Mercurial 2.4.x

* Sat Aug 25 2012 Mads Kiilerich <mads@kiilerich.com> - 1.6.2-1
- hgview-1.6.2

* Thu Feb 16 2012 Mads Kiilerich <mads@kiilerich.com> - 1.5.0-1
- hgview-1.5.0
- make qt and curses support optional

* Thu Nov 03 2011 Mads Kiilerich <mads@kiilerich.com> - 1.4.0-2
- Update package description
- Update spec to the new curses UI introduced in 1.4.0
- Install Mercurial configuration template, nothing enabled by default
- Drop docs ChangeLog (outdated) and README (no relevant information for package users)
- Don't set python_sitelib and don't clean $RPM_BUILD_ROOT

* Fri Oct 07 2011 Mads Kiilerich <mads@kiilerich.com> - 1.4.0-1
- hgview-1.4.0

* Sat Sep 10 2011 Mads Kiilerich <mads@kiilerich.com> - 1.3.0-2
- Minor tweaks to requirements and use of macros, based on comments from Volker
  Fröhlich

* Thu Sep 08 2011 Mads Kiilerich <mads@kiilerich.com> - 1.3.0-1
- Initial package for Fedora
