# exclude provate provides
%global __provides_exclude_from ^%{_libdir}/%{name}/plugins/.*\.so$

Name:           qstardict
Version:        4.0.0
Release:        %autorelease
Summary:        StarDict clone written using Qt
License:        GPL-3.0-or-later
URL:            https://qstardict.ylsoftware.com/
Source0:        https://github.com/a-rodin/qstardict/archive/%{version}/qstardict-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  glib2-devel
BuildRequires:  zlib-devel
BuildRequires:  libzim-devel
BuildRequires:  desktop-file-utils
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-linguist

# This project is using private headers
BuildRequires:  qt6-qtbase-private-devel

%description
QStarDict is a StarDict clone written using Qt. The user interface
is similar to StarDict.

Main features:
* Full support of StarDict dictionaries
* Working from the system tray
* Scanning mouse selection and showing pop-up windows with translation of
selected words
* Translations reformatting
* Pronouncing of the translated words
* Plugins support

%prep
%autosetup -n %{name}-%{version}

%build
%qmake_qt6 PLUGINS_DIR=%{_libdir}/%{name}/plugins QMAKE_LRELEASE=lrelease-qt6
make %{?_smp_mflags}

%install
make install INSTALL_ROOT=%{buildroot}

install -pDm644 qstardict/qstardict.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

rm -fr %{buildroot}%{_docdir}

%files
%doc AUTHORS ChangeLog README.md THANKS
%license COPYING
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
%autochangelog
