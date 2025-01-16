Summary:   Fedora AppStream metadata
Name:      appstream-data
Version:   42
Release:   %autorelease
BuildArch: noarch
License:   CC0-1.0 AND CC-BY-1.0 AND CC-BY-SA-1.0 AND GFDL-1.1-or-later
URL:       https://github.com/hughsie/appstream-glib
Source1:   https://dl.fedoraproject.org/pub/alt/screenshots/f%{version}/fedora-%{version}.xml.gz
Source2:   https://dl.fedoraproject.org/pub/alt/screenshots/f%{version}/fedora-%{version}-icons.tar.gz
Source3:   gstreamer-non-free.xml
Source4:   other-repos.xml

BuildRequires: libappstream-glib

%description
This package provides the distribution specific AppStream metadata required
for the GNOME and KDE software centers. The appstream data is built weekly with
/usr/bin/appstream-builder, combining the data from RPM packages in official
repositories and the extra data in fedora-appstream.

%install

DESTDIR=%{buildroot} appstream-util install-origin fedora %{SOURCE1} %{SOURCE2}
DESTDIR=%{buildroot} appstream-util install \
	%{SOURCE3} %{SOURCE4}

# Move to the "correct" path for appstream 0.16 / 1.0
mv %{buildroot}%{_datadir}/app-info %{buildroot}%{_datadir}/swcatalog
mv %{buildroot}%{_datadir}/swcatalog/xmls %{buildroot}%{_datadir}/swcatalog/xml


%check
if ! gunzip -c %{buildroot}%{_datadir}/swcatalog/xml/fedora.xml.gz | grep -q '<pkgname>gstreamer1-plugin-openh264</pkgname>' ; then
    echo "missing gstreamer1-plugin-openh264"
    exit 1
fi

%files
%attr(0644,root,root) %{_datadir}/swcatalog/xml/*
%{_datadir}/swcatalog/icons/fedora/*/*.png
%dir %{_datadir}/swcatalog
%dir %{_datadir}/swcatalog/icons
%dir %{_datadir}/swcatalog/icons/fedora
%dir %{_datadir}/swcatalog/icons/fedora/64x64
%dir %{_datadir}/swcatalog/icons/fedora/128x128
%dir %{_datadir}/swcatalog/xml

%changelog
%autochangelog
