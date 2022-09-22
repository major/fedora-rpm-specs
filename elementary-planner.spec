%global appname planner
%global uuid    com.github.alainm23.%{appname}

Name:           elementary-%{appname}
Version:        3.0.7
Release:        %autorelease
# Oops: https://github.com/alainm23/planner/releases/tag/6.2.3
Epoch:          1

Summary:        Task manager with Todoist support designed for GNU/Linux

License:        GPLv3+
URL:            https://github.com/alainm23/planner
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.40.3

BuildRequires:  pkgconfig(gee-0.8) >= 0.8.5
BuildRequires:  pkgconfig(granite) >= 5.2.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.6.0
BuildRequires:  pkgconfig(gtksourceview-4)
BuildRequires:  pkgconfig(libecal-2.0)
BuildRequires:  pkgconfig(libedataserver-1.2) >= 3.8.0
BuildRequires:  pkgconfig(libgdata)
BuildRequires:  pkgconfig(libhandy-1) >= 0.90.0
BuildRequires:  pkgconfig(libical-glib)
BuildRequires:  pkgconfig(libpeas-1.0)
BuildRequires:  pkgconfig(webkit2gtk-4.0)

Requires:       hicolor-icon-theme

%description
How Planner works:

1. Collect your Ideas - The Inbox is your default task list in Planner. When
   you add a task, it goes straight to your Inbox unless you specify that the
   task goes into a project.

2. Get Organized - Create a project for each of your goals, then add the steps
   to reach them. Review these regularly to stay on top of things.

3. Calendar and Events - See your calendar events and plan your time
   effectively. Planner will remind you on the right day.

4. Be even more organized - Add a duedate to your tasks, create labels, use
   checklists.

Support for Todoist:

  - Synchronize your Projects, Task and Sections thanks to Todoist.
  - Support for Todoist offline: Work without an internet connection and when
    everything is reconnected it will be synchronized.

    * Planner not created by, affiliated with, or supported by Doist

Other features:

  - Reminders notifications
  - Quick Find
  - Night mode


%prep
%autosetup -n %{appname}-%{version}


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{uuid}

# Remove SVG icon dupes
rm -r   %{buildroot}%{_datadir}/icons/hicolor/*@2/      \
        %{buildroot}%{_datadir}/icons/hicolor/48x48/    \
        %{buildroot}%{_datadir}/icons/hicolor/64x64/


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{uuid}.lang
%license LICENSE
%doc README.md AUTHORS
%{_bindir}/%{uuid}
%{_bindir}/%{uuid}.quick-add
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.svg
%{_metainfodir}/*.xml


%changelog
%autochangelog
