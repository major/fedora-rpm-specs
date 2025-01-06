# Review at https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=215241

%global minor_version 0.5
%global thunar_version 1.8.0
%global xfceversion 4.16

Name:           thunar-archive-plugin
Version:        0.5.3
Release:        %autorelease
Summary:        Archive plugin for the Thunar file manager

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://goodies.xfce.org/projects/thunar-plugins/%{name}
Source0:        http://archive.xfce.org/src/thunar-plugins/%{name}/%{minor_version}/%{name}-%{version}.tar.bz2
#VCS:           git:git://git.xfce.org/thunar-plugins/thunar-archive-plugin

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  exo >= 0.12.0
BuildRequires:  libxfce4util-devel >= %{xfceversion}
BuildRequires:  Thunar-devel >= %{thunar_version}
BuildRequires:  libxml2-devel
BuildRequires:  gettext
Requires:       Thunar >= %{thunar_version}

%description
The Thunar Archive Plugin allows you to create and extract archive files using 
the file context menus in the Thunar file manager. Starting with version 0.2.0, 
the plugin provides a generic scripting interface for archive managers. 


%prep
%setup -q


%build
%configure

%make_build


%install
%make_install

find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%find_lang %{name}

%if (0%{?fedora} && 0%{?fedora} < 19) || (0%{?rhel} && 0%{?rhel} < 7)
# On Fedora < 19 we need to install file-roller.tap as gnome-file-roller.tap,
# because the name # has to match the basename of the desktop-file in
# %%{_datadir}/applications.
mv %{buildroot}%{_libexecdir}/thunar-archive-plugin/file-roller.tap \
    %{buildroot}%{_libexecdir}/thunar-archive-plugin/gnome-file-roller.tap
%endif

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog THANKS NEWS
%doc scripts/template.tap
%{_libdir}/thunarx-*/thunar-archive-plugin.so
%{_libexecdir}/thunar-archive-plugin/
%{_datadir}/icons/hicolor/*/*/*


%changelog
%autochangelog
