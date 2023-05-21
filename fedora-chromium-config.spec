Name:           fedora-chromium-config
Version:        3.0
Release:        %autorelease
Summary:        Fedora customizations for Chromium/Chrome
License:        GPLv2+
# The upstream for this is a dist-git
URL:            https://src.fedoraproject.org/rpms/fedora-chromium-config
Source0:        https://src.fedoraproject.org/rpms/fedora-chromium-config/raw/master/f/LICENSE

# Chrome/Chromium Extensions to improve behavior on Fedora
# GNOME
Source100:      gphhapmejobijbbhgpjhcjognlahblep.json
# KDE Plasma
Source101:      cimiefiiaegbelhefglklhhakcgmhkai.json


# Configuration to support Kerberos GSSAPI logins to the Fedora Account System
Source200:      00_gssapi.json
Source201:      %{name}-tmpfiles.conf

BuildArch:      noarch

# For the _tmpfilesdir macro
BuildRequires:  systemd-rpm-macros

Obsoletes:      fedora-user-agent-chrome < 1.0
Obsoletes:      %{name} < 2.0-4

# Starting with Chromium 83, the Kerberos support works properly
Conflicts:      chromium < 83

Conflicts:     %{name} < %{version}-%{release}
Conflicts:     %{name} > %{version}-%{release}

Recommends:     (%{name}-gnome if gnome-shell)
Recommends:     (%{name}-kde if plasma-desktop)


%description
This package is used to install customizations for Chromium/Chrome that are
recommended by Fedora.

%package gssapi
Obsoletes: %{name} < 2.0-4
Conflicts:     %{name} < %{version}-%{release}
Conflicts:     %{name} > %{version}-%{release}
Summary: GSSAPI support for Fedora Services

%description gssapi
This package provides a GSSAPI configuration that enables access to some Fedora
Project services. To add support for other domains, replace the symlink
/etc/chromium/policies/recommended/00_gssapi.json with your own content.


%package gnome
Conflicts:     %{name} < %{version}-%{release}
Conflicts:     %{name} > %{version}-%{release}
Summary: GNOME integration for Chrome
URL: https://chrome.google.com/webstore/detail/gnome-shell-integration/gphhapmejobijbbhgpjhcjognlahblep


%description gnome
Chrome/Chromium extension to improve integration with the GNOME desktop.


%package kde
Conflicts:     %{name} < %{version}-%{release}
Conflicts:     %{name} > %{version}-%{release}
Summary: KDE Plasma integration for Chrome
URL: https://chrome.google.com/webstore/detail/plasma-integration/cimiefiiaegbelhefglklhhakcgmhkai
Requires: plasma-browser-integration >= 5.13


%description kde
Chrome/Chromium extension to improve integration with the KDE Plasma desktop.


%prep
mkdir -p %{_builddir}/licenses
cp -a %{SOURCE0} %{_builddir}/licenses/


%build


%install
# Install the FAS kerberos configuration for Chrome
# The recommended policy directory does not merge identical keys and we don't want
# to accidentally override any configuration that a site has installed here, so
# we install it as 00_gssapi.json. If another file is present in this directory
# that includes the same keys and a filename that sorts alphabetically higher,
# it will supersede this file. "00" is chosen to sort as low as possible.
mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 0644 %{SOURCE201} %{buildroot}%{_tmpfilesdir}/%{name}-tmpfiles.conf

mkdir -p %{buildroot}%{_sysconfdir}/opt/chrome/policies/recommended \
         %{buildroot}%{_sysconfdir}/chromium/policies/recommended \
         %{buildroot}%{_datadir}/chromium/policies/recommended

cp -a %{SOURCE200} %{buildroot}%{_datadir}/chromium/policies/recommended

# Add KDE Plasma Extension
# https://chrome.google.com/webstore/detail/plasma-integration/cimiefiiaegbelhefglklhhakcgmhkai
mkdir -p %{buildroot}%{_datadir}/google-chrome/extensions
mkdir -p %{buildroot}%{_datadir}/chromium/extensions

cp -a %{SOURCE100} %{SOURCE101} %{buildroot}%{_datadir}/google-chrome/extensions
cp -a %{SOURCE100} %{SOURCE101} %{buildroot}%{_datadir}/chromium/extensions



%files
%license licenses/LICENSE

%files gssapi
%license licenses/LICENSE

# GSSAPI default configuration for fedoraproject.org
%{_datadir}/chromium/policies/recommended/00_gssapi.json

# Chromium GSSAPI configuration symlinks
# By default, the Chromium configuration is symlinked to the
# default configuration in /usr/share/chromium using tmpfiles.d
%dir %{_sysconfdir}/chromium/
%dir %{_sysconfdir}/chromium/policies
%dir %{_sysconfdir}/chromium/policies/recommended
%ghost %{_sysconfdir}/chromium/policies/recommended/00_gssapi.json

# Google Chrome GSSAPI configuration symlinks
# By default, the Chrome configuration is symlinked to the Chromium
# policy. That way there is a single place to modify both together.
%dir %{_sysconfdir}/opt/chrome/
%dir %{_sysconfdir}/opt/chrome/policies
%dir %{_sysconfdir}/opt/chrome/policies/recommended
%ghost %{_sysconfdir}/opt/chrome/policies/recommended/00_gssapi.json

# systemd-tmpfilesd configuration for symlinks
%{_tmpfilesdir}/%{name}-tmpfiles.conf


%files gnome
%license licenses/LICENSE

%dir %{_datadir}/google-chrome
%dir %{_datadir}/google-chrome/extensions
%dir %{_datadir}/chromium
%dir %{_datadir}/chromium/extensions
%{_datadir}/google-chrome/extensions/gphhapmejobijbbhgpjhcjognlahblep.json
%{_datadir}/chromium/extensions/gphhapmejobijbbhgpjhcjognlahblep.json

%files kde
%license licenses/LICENSE

%dir %{_datadir}/google-chrome
%dir %{_datadir}/google-chrome/extensions
%dir %{_datadir}/chromium
%dir %{_datadir}/chromium/extensions
%{_datadir}/google-chrome/extensions/cimiefiiaegbelhefglklhhakcgmhkai.json
%{_datadir}/chromium/extensions/cimiefiiaegbelhefglklhhakcgmhkai.json


%changelog
%autochangelog
