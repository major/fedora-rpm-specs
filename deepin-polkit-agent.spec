%global repo dde-polkit-agent

Name:           deepin-polkit-agent
Version:        5.4.17
Release:        %autorelease
Summary:        Deepin Polkit Agent
# migrated to SPDX
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dde-polkit-agent
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  dtkwidget-devel >= 5.1.1
BuildRequires:  pkgconfig(dframeworkdbus)
BuildRequires:  pkgconfig(polkit-qt5-1)
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5MultimediaWidgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  qt5-linguist
BuildRequires: make

%description
DDE Polkit Agent is the polkit agent used in Deepin Desktop Environment.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for %{name}.

%prep
%setup -q -n %{repo}-%{version}

# https://github.com/linuxdeepin/developer-center/issues/1721
sed -i 's/bool is_deepin = true/bool is_deepin = false/' policykitlistener.cpp

# https://github.com/linuxdeepin/dde-polkit-agent/issues/26
sed -i '/setCancel/d' policykitlistener.cpp

%build
# help find (and prefer) qt5 utilities, e.g. qmake, lrelease
export PATH=%{_qt5_bindir}:$PATH
%qmake_qt5 PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%doc README.md
%license LICENSE
%{_prefix}/lib/polkit-1-dde/
%{_datadir}/%{repo}/

%files devel
%{_includedir}/dpa/

%changelog
%autochangelog
