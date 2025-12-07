%define gettext_package redhat-menus

Summary: Configuration and data files for the desktop menus
Name: redhat-menus
Version: 12.0.2
Release: %autorelease
URL: http://www.redhat.com
#FIXME-> There is no hosting website for this project.
Source0: %{name}-%{version}.tar.gz
License: GPL-1.0-or-later
BuildArch: noarch
BuildRequires: make
BuildRequires:  gcc
BuildRequires: desktop-file-utils
BuildRequires: intltool

%description
This package contains the XML files that describe the menu layout for
GNOME and KDE, and the .desktop files that define the names and icons
of "subdirectories" in the menus.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

%find_lang %{gettext_package}

# create the settings-merged to prevent gamin from looking for it
# in a loop
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/xdg/menus/settings-merged ||:

%files  -f %{gettext_package}.lang
%doc COPYING
%dir %{_sysconfdir}/xdg/menus
%dir %{_sysconfdir}/xdg/menus/applications-merged
%dir %{_sysconfdir}/xdg/menus/preferences-merged
%dir %{_sysconfdir}/xdg/menus/preferences-post-merged
%dir %{_sysconfdir}/xdg/menus/settings-merged
%config %{_sysconfdir}/xdg/menus/*.menu
%exclude %{_datadir}/desktop-menu-patches/*.desktop
%{_datadir}/desktop-directories/*.directory

%changelog
%autochangelog
