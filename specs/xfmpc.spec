%global majorver 0.4

Name:           xfmpc
Version:        0.4.0
Release:        %autorelease
Summary:        A MPD client for the Xfce desktop environment

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://goodies.xfce.org/projects/applications/%{name}
Source0:        http://archive.xfce.org/src/apps/%{name}/%{majorver}/%{name}-%{version}.tar.xz

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  libxfce4ui-devel >= 4.8.0
BuildRequires:  libmpd-devel >= 0.15.0
BuildRequires:  meson
BuildRequires:  desktop-file-utils
BuildRequires:  vala
 
%description
Xfmpc is a a graphical GTK+ MPD client for the Xfce desktop environment.
It is focusing on low footprint and easy usage.


%prep
%setup -q


%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

desktop-file-install                         \
        --dir %{buildroot}%{_datadir}/applications         \
        --delete-original                                       \
        %{buildroot}%{_datadir}/applications/%{name}.desktop


%files -f %{name}.lang
%license COPYING
%doc AUTHORS IDEAS NEWS THANKS
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1.gz


%changelog
%autochangelog
