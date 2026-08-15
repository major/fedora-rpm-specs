# Review at https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=219986
# VCS   https://gitlab.xfce.org/panel-plugins/xfce4-smartbookmark-plugin

%global _hardened_build 1
%global minor_version 0.6
%global xfceversion 4.20

Name:           xfce4-smartbookmark-plugin
Version:        0.6.0
Release:        %autorelease
Summary:        Smart bookmarks for the Xfce panel

License:        GPL-2.0-or-later
URL:            https://docs.xfce.org/panel-plugins/xfce4-smartbookmark-plugin/start
Source0:        https://archive.xfce.org/src/panel-plugins/%{name}/%{minor_version}/%{name}-%{version}.tar.xz
# vendor specific patches
Patch:          %{name}-%{version}-redhat.patch

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  libxfce4util-devel >= %{xfceversion}
BuildRequires:  meson
BuildRequires:  xfce4-panel-devel >= %{xfceversion}

Requires:       webclient
Requires:       xfce4-panel >= %{xfceversion}

%description
A plugin which allows you to do a search directly on Internet on sites like 
Google or Red Hat Bugzilla. It allows you to send requests directly to your 
browser and perform custom searches.

%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install
# Rename non-standard hye locale to hy
if [ -d %{buildroot}%{_datadir}/locale/hye ]; then
    mv %{buildroot}%{_datadir}/locale/hye %{buildroot}%{_datadir}/locale/hy
fi

%find_lang %{name}


%check
%meson_test
%files -f %{name}.lang
%doc AUTHORS ChangeLog
%license COPYING
%{_libdir}/xfce4/panel/plugins/*.so
%{_datadir}/xfce4/panel/plugins/*.desktop


%changelog
%autochangelog
