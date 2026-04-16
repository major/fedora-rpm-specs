Name:           bubblemail
Version:        1.12
Release:        %autorelease
Summary:        Extensible mail notification service

License:        GPL-2.0-only
URL:            http://bubblemail.free.fr/
Source0:        https://framagit.org/razer/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  folks-devel
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  python3-devel
BuildRequires:  python3-pillow
BuildRequires:  python3-pyxdg
BuildRequires:  vala
Requires:       folks
Requires:       gnome-keyring
Requires:       hicolor-icon-theme
Requires:       libsecret
Requires:       python3-gobject
Requires:       python3-dbus
Requires:       python3-requests
Requires:       python3-gstreamer1
Requires:       python3-pyxdg
Requires:       python3-pysocks
Recommends:     gnome-online-accounts
Recommends:     gnome-shell-extension-bubblemail

%description
Bubblemail is a D-Bus service providing a list of the new and unread user's mail
from local mailboxes, pop, imap, and gnome online accounts. It includes a
libnotify frontend to create notifications and can be used by other frontends as
well.

%prep
%autosetup -p1 -n %{name}-v%{version}
sed -i '1{\@^#!/usr/bin/env python@d}' \
        bubblemail/plugins/spamfilterplugin.py \
        bubblemail/plugins/userscriptplugin.py
%py3_shebang_fix data/bin/bubblemail
%py3_shebang_fix data/bin/bubblemaild
        
%conf
%meson        

%build
%meson_build

%install
%meson_install
%find_lang %{name}
cat %{name}.lang >> %{pyproject_files}

%check
appstream-util validate-relax --nonet \
        %{buildroot}%{_metainfodir}/*.appdata.xml
desktop-file-validate \
        %{buildroot}/%{_datadir}/applications/*.desktop

%files -f %{pyproject_files}
%license LICENSE.txt
%doc AUTHORS CHANGELOG.md CONTRIBUTING.md README.md
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}d.1*
%{_sysconfdir}/xdg/autostart/%{name}d.desktop
%{_bindir}/%{name}
%{_bindir}/%{name}-avatar-provider
%{_bindir}/%{name}d
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/%{name}.svg
%{_metainfodir}/%{name}.appdata.xml
%{python3_sitelib}/%{name}

%changelog
%autochangelog
