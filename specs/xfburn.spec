# Review: https://bugzilla.redhat.com/show_bug.cgi?id=473679

%global majorversion 0.8

Name:           xfburn
Version:        0.8.0
Release:        %autorelease
Summary:        Simple CD burning tool for Xfce

License:        GPL-2.0-or-later
URL:            https://docs.xfce.org/apps/xfburn/start
#VCS: git:https://gitlab.xfce.org/apps/xfburn.git
Source0:        https://archive.xfce.org/src/apps/%{name}/%{majorversion}/%{name}-%{version}.tar.bz2

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  libxfce4ui-devel >= 4.18.0
BuildRequires:  exo-devel >= 4.18.0
BuildRequires:  libburn-devel
BuildRequires:  libisofs-devel
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  gtk3-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libgudev1-devel
BuildRequires:  libappstream-glib
BuildRequires:  docbook-style-xsl
Requires:       hicolor-icon-theme

%description
Xfburn is a simple CD/DVD burning tool based on libburnia libraries. It can 
blank CD-RWs, burn and create iso images, as well as burn personal 
compositions of data to either CD or DVD.


%prep
%autosetup -p1


%conf
%meson

%build
%meson_build


%install
%meson_install

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
