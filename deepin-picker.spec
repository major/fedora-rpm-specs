Name:           deepin-picker
Version:        5.0.28
Release:        %autorelease
Summary:        A color picker tool for deepin
License:        GPLv3+
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# fix lang code duplications
Patch0002: 0002-Fix-lang-code-in-desktop-entry-file.patch

BuildRequires: gcc-c++
BuildRequires: desktop-file-utils
%if 0%{?openeuler}
BuildRequires: qt5-devel
%else
BuildRequires: qt5-linguist
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5X11Extras)
Requires:      hicolor-icon-theme
%endif
BuildRequires: libxcb-devel
BuildRequires: libXext-devel
BuildRequires: libX11-devel
BuildRequires: libXtst-devel

BuildRequires: pkgconfig(dtkwidget)
BuildRequires: pkgconfig(dtkgui)
BuildRequires: pkgconfig(libexif)
BuildRequires: pkgconfig(xcb-util)
BuildRequires: make

%description
%{summary}.

%prep
%autosetup -p1

%build
# help find (and prefer) qt5 utilities, e.g. qmake, lrelease
export PATH=%{_qt5_bindir}:$PATH
mkdir build && pushd build
%qmake_qt5 ../
%make_build
popd

%install
%make_install -C build INSTALL_ROOT="%buildroot"

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/dbus-1/services/com.deepin.Picker.service
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg


%changelog
%autochangelog
