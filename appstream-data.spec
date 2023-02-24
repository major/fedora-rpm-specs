Summary:   Fedora AppStream metadata
Name:      appstream-data
Version:   39
Release:   %autorelease
BuildArch: noarch
License:   CC0-1.0 AND CC-BY-1.0 AND CC-BY-SA-1.0 AND GFDL-1.1-or-later
URL:       https://github.com/hughsie/appstream-glib
Source1:   https://dl.fedoraproject.org/pub/alt/screenshots/f%{version}/fedora-%{version}.xml.gz
Source2:   https://dl.fedoraproject.org/pub/alt/screenshots/f%{version}/fedora-%{version}-icons.tar.gz
Source3:   https://raw.githubusercontent.com/hughsie/fedora-appstream/master/appstream-extra/adobe-flash.xml
Source4:   https://raw.githubusercontent.com/hughsie/fedora-appstream/master/appstream-extra/google-chrome.xml
Source5:   https://raw.githubusercontent.com/hughsie/fedora-appstream/master/appstream-extra/gstreamer-non-free.xml
Source6:   https://raw.githubusercontent.com/hughsie/fedora-appstream/master/appstream-extra/other-repos.xml
Source7:   https://raw.githubusercontent.com/hughsie/fedora-appstream/master/appstream-extra/fedora-categories.xml
Source8:   https://raw.githubusercontent.com/hughsie/fedora-appstream/master/appstream-extra/fedora-popular.xml

BuildRequires: libappstream-glib

%description
This package provides the distribution specific AppStream metadata required
for the GNOME and KDE software centers. The appstream data is built weekly with
/usr/bin/appstream-builder, combining the data from RPM packages in official
repositories and the extra data in fedora-appstream.

%install

DESTDIR=%{buildroot} appstream-util install-origin fedora %{SOURCE1} %{SOURCE2}
DESTDIR=%{buildroot} appstream-util install \
	%{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} %{SOURCE7} %{SOURCE8}

%check
if ! gunzip -c %{buildroot}%{_datadir}/app-info/xmls/fedora.xml.gz | grep -q '<pkgname>gstreamer1-plugin-openh264</pkgname>' ; then
    echo "missing gstreamer1-plugin-openh264"
    exit 1
fi

%files
%attr(0644,root,root) %{_datadir}/app-info/xmls/*
%{_datadir}/app-info/icons/fedora/*/*.png
%dir %{_datadir}/app-info
%dir %{_datadir}/app-info/icons
%dir %{_datadir}/app-info/icons/fedora
%dir %{_datadir}/app-info/icons/fedora/64x64
%dir %{_datadir}/app-info/icons/fedora/128x128
%dir %{_datadir}/app-info/xmls

%changelog
%autochangelog
