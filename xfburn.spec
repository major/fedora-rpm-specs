# Review: https://bugzilla.redhat.com/show_bug.cgi?id=473679

%global majorversion 0.7

Name:           xfburn
Version:        0.7.0
Release:        %autorelease
Summary:        Simple CD burning tool for Xfce

License:        GPLv2+
URL:            http://goodies.xfce.org/projects/applications/%{name}
#VCS: git:git://git.xfce.org/apps/xfburn
Source0:        http://archive.xfce.org/src/apps/%{name}/%{majorversion}/%{name}-%{version}.tar.bz2

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  libxfce4ui-devel >= 4.12.0
BuildRequires:  exo-devel
BuildRequires:  libburn-devel >= 0.4.2
BuildRequires:  libisofs-devel >= 0.6.2
BuildRequires:  dbus-glib-devel >= 0.34 
BuildRequires:  gstreamer1-devel >= 0.10.2
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  gtk2-devel >= 2.10.0
BuildRequires:  desktop-file-utils 
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libgudev1-devel
BuildRequires:  libappstream-glib
Requires:       hicolor-icon-theme

%description
Xfburn is a simple CD/DVD burning tool based on libburnia libraries. It can 
blank CD-RWs, burn and create iso images, as well as burn personal 
compositions of data to either CD or DVD.


%prep
%autosetup -p1

# fix appdata installation location
sed -i 's/\$(datadir)\/appdata/\$(datadir)\/metainfo/' Makefile.in


%build
%configure
%make_build


%install
%make_install INSTALL='install -p'

%find_lang %{name}
desktop-file-install --vendor ""                            \
    --dir %{buildroot}%{_datadir}/applications              \
    --delete-original                                       \
    --add-category=Utility                                  \
    %{buildroot}%{_datadir}/applications/%{name}.desktop

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.xfce.%{name}.appdata.xml

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS TODO
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/Thunar/sendto/*.desktop
%{_datadir}/icons/hicolor/*/stock/media/stock_%{name}*.png
%{_datadir}/icons/hicolor/scalable/stock/media/stock_%{name}*.svg
%{_datadir}/metainfo/org.xfce.%{name}.appdata.xml
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/*.ui
%{_mandir}/man1/%{name}.*


%changelog
%autochangelog
