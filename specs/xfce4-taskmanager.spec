%global majorversion 1.5

Name:           xfce4-taskmanager
Version:        1.5.8
Release:        %autorelease
Summary:        Taskmanager for the Xfce desktop environment

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://goodies.xfce.org/projects/applications/%{name}
Source0:        http://archive.xfce.org/src/apps/%{name}/%{majorversion}/%{name}-%{version}.tar.bz2

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  libxfce4ui-devel
BuildRequires:  libXmu-devel
BuildRequires:  gettext
BuildRequires:  desktop-file-utils

%description
A simple taskmanager for the Xfce desktop environment.


%prep
%setup -q


%build
%configure --enable-gtk3

%make_build


%install
%make_install

%find_lang %{name}

desktop-file-install \
    --delete-original \
    --add-category GTK \
    --add-category Monitor \
    --add-category X-Xfce \
    --remove-category Utility \
    --dir %{buildroot}%{_datadir}/applications \
    %{buildroot}%{_datadir}/applications/%{name}.desktop



%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS THANKS
%{_bindir}/%{name}
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/org.xfce.taskmanager.*
%{_datadir}/icons/hicolor/scalable/actions/xc_crosshair-symbolic.svg

%changelog
%autochangelog
