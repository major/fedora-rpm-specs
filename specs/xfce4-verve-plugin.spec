# Review at https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=238348
# VCS   https://gitlab.xfce.org/panel-plugins/xfce4-verve-plugin
%global minor_version 2.1

Name:           xfce4-verve-plugin
Version:        2.1.0
Release:        %autorelease
Summary:        Comfortable command line plugin for the Xfce panel

License:        GPL-2.0-or-later
URL:            https://docs.xfce.org/panel-plugins/xfce4-verve-plugin/start
Source0:        https://archive.xfce.org/src/panel-plugins/%{name}/%{minor_version}/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libxfce4ui-devel
BuildRequires:  libxfce4util-devel
BuildRequires:  meson
BuildRequires:  pcre2-devel >= 10.0
BuildRequires:  xfce4-panel-devel

Requires:       xfce4-panel
Provides:       verve-plugin = %{version}

%description
This plugin is like the (quite old) xfce4-minicmd-plugin, except that it ships 
more cool features, such as:
* Command history
* Auto-completion (including command history)
* Open URLs and eMail addresses in your favourite applications
* Focus grabbing via D-BUS (so you can bind a shortcut to it)
* Custom input field width

%prep
%autosetup

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
%license COPYING
%doc AUTHORS NEWS README.md THANKS
%{_libdir}/xfce4/panel/plugins/libverve.so
%{_datadir}/xfce4/panel/plugins/*.desktop

%changelog
%autochangelog
