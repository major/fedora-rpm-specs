%global srcname aw-qt
%global commit 6ab7e3f13934b80a92e596452bea9de766c5446e
%global short_commit %(c=%{commit}; echo ${c:0:7})

Name:           python-%{srcname}
Version:        0^20250329.%{short_commit}
Release:        %autorelease
Summary:        Service manager and tray icon managing aw-server and watchers, built with Qt

License:        MPL-2.0
URL:            https://github.com/ActivityWatch/aw-qt
Source0:        %{url}/archive/%{commit}/%{srcname}-%{short_commit}.tar.gz
Source1:        https://raw.githubusercontent.com/ActivityWatch/media/cb597f7c2e2b135505fe5d6b3042960a638892cf/logo/logo.png
Source2:        https://raw.githubusercontent.com/ActivityWatch/media/cb597f7c2e2b135505fe5d6b3042960a638892cf/logo/logo-128.png
Patch:          0001-Avoid-FTBFS-on-upcoming-Fedora.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  help2man
BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme
Requires:       python3dist(pyqt6-base)

%global _description %{expand:
A service manager and tray icon managing aw-server and watchers, built with Qt.}

%description %{_description}

%package -n python3-%{srcname}
Summary:    %{summary}

%description -n python3-%{srcname} %{_description}

%prep
%autosetup -n %{srcname}-%{commit}

# copy icons
cp -p %{SOURCE1} %{SOURCE2} .

# the build process somehow doesn't bundle the logo.png icon
sed -ri 's/\("icons:logo.png"\)/.fromTheme("activitywatch")/' aw_qt/trayicon.py

# dependency generator seems to not harvest following mandatory
# dependencies from tool.poetry.group.pyqt.dependencies
sed -ri '/^[[:blank:]]*aw-core\b/a PyQt6 = "^6.5.3"' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files aw_qt

mkdir -p %{buildroot}%{_mandir}/man1
	
export PYTHONPATH="$PYTHONPATH:%{buildroot}%{python3_sitelib}"
help2man --no-discard-stderr %{buildroot}%{_bindir}/%{srcname} -o %{buildroot}%{_mandir}/man1/%{srcname}.1

desktop-file-install -m 0644 --dir=%{buildroot}%{_datadir}/applications %{_builddir}/%{srcname}-%{commit}/resources/%{srcname}.desktop
install -Dm 0644 logo-128.png %{buildroot}/%{_datadir}/icons/hicolor/128x128/apps/activitywatch.png
install -Dm 0644 logo.png %{buildroot}/%{_datadir}/icons/hicolor/512x512/apps/activitywatch.png

%check
%pyproject_check_import
export QT_QPA_PLATFORM=offscreen
export PATH="$PATH:%{buildroot}%{_bindir}"
export PYTHONPATH="$PYTHONPATH:%{buildroot}%{python3_sitelib}"
%{python3} tests/integration_tests.py --no-modules

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
%license LICENSE.txt
%{_mandir}/man1/%{srcname}.1*
%{_bindir}/%{srcname}
%{_datadir}/icons/hicolor/128x128/apps/activitywatch.png
%{_datadir}/icons/hicolor/512x512/apps/activitywatch.png
%{_datadir}/applications/%{srcname}.desktop

%changelog
%autochangelog
