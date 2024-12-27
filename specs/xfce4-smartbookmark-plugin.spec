# Review at https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=219986

%global _hardened_build 1
%global minor_version 0.5
%global xfceversion 4.16

Name:           xfce4-smartbookmark-plugin
Version:        0.5.3
Release:        %autorelease
Summary:        Smart bookmarks for the Xfce panel

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://goodies.xfce.org/projects/panel-plugins/%{name}
Source0:        http://archive.xfce.org/src/panel-plugins/%{name}/%{minor_version}/%{name}-%{version}.tar.bz2
# vendor specific patches
Patch10:        %{name}-%{version}-redhat.patch

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  xfce4-panel-devel >= %{xfceversion}
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  gettext
BuildRequires:  intltool
Requires:       xfce4-panel >= %{xfceversion}
Requires:       webclient

%description
A plugin which allows you to do a search directly on Internet on sites like 
Google or Red Hat Bugzilla. It allows you to send requests directly to your 
browser and perform custom searches.

%prep
%autosetup -p1


%build
%configure --disable-static
%make_build


%install
%make_install
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'
chmod 755 %{buildroot}/%{_libdir}/xfce4/panel/plugins/*.so
%find_lang %{name}


%files -f %{name}.lang
%doc AUTHORS ChangeLog
%license COPYING
%{_libdir}/xfce4/panel/plugins/*.so
%{_datadir}/xfce4/panel/plugins/*.desktop


%changelog
%autochangelog
