Name:           thonny
Version:        4.1.4
Release:        %autorelease
Summary:        Python IDE for beginners

# Code is MIT, toolbar icons are EPL-1.0
# Vendored python-pipkin is MIT
License:        MIT AND EPL-1.0
URL:            https://thonny.org
Source:         %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-tkinter
BuildRequires:  python3-filelock
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  xorg-x11-server-Xvfb
# To compile the localization files
BuildRequires:  babel

Requires:       python3-tkinter
# Pip is necessary for pip_gui plugin, therefore explicit Requires
Requires:       python3-pip
# Unbundled library needs to be explicitly Required
Requires:       python3-filelock
Requires:       hicolor-icon-theme

# Vendored library - not yet packaged in Fedora
Provides:       bundled(python3dist(pipkin)) = 2.0~b2

Recommends:     python3-asttokens
Recommends:     python3-distro
Recommends:     zenity
Recommends:     xsel

%description
Thonny is a simple Python IDE with features useful for learning programming.
It comes with a debugger which is able to visualize all the conceptual steps
taken to run a Python program (executing statements, evaluating expressions,
maintaining the call stack). There is a GUI for installing 3rd party packages
and special mode for learning about references.

%prep
%autosetup -p1

# Remove localization helper scripts, we don't need them in the package
rm thonny/locale/compile_mo.bat thonny/locale/update_pot.bat thonny/locale/thonny.pot

# Remove the vendored python-filelock
rm -r thonny/vendored_libs/filelock/

%generate_buildrequires
%pyproject_buildrequires

%build
# Don't use the upstream compiled language files, compile them during the build
rm thonny/locale/*/LC_MESSAGES/*.mo
pybabel compile -d thonny/locale/ -D thonny
rm thonny/locale/*/LC_MESSAGES/*.po

%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files thonny

install -m 0644 -D -T packaging/icons/thonny-256x256.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/thonny.png
install -m 0644 -D -T packaging/icons/thonny-128x128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/thonny.png
install -m 0644 -D -T packaging/icons/thonny-64x64.png   %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/thonny.png
install -m 0644 -D -T packaging/icons/thonny-48x48.png   %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/thonny.png
install -m 0644 -D -T packaging/icons/thonny-32x32.png   %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/thonny.png
install -m 0644 -D -T packaging/icons/thonny-22x22.png   %{buildroot}%{_datadir}/icons/hicolor/22x22/apps/thonny.png
install -m 0644 -D -T packaging/icons/thonny-16x16.png   %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/thonny.png

install -D -m 0644 -t %{buildroot}%{_datadir}/metainfo                    packaging/linux/org.thonny.Thonny.appdata.xml
install -D -m 0644 -t %{buildroot}%{_mandir}/man1                         packaging/linux/thonny.1
desktop-file-install --dir=%{buildroot}%{_datadir}/applications           packaging/linux/org.thonny.Thonny.desktop

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.thonny.Thonny.appdata.xml


%check
%global __pytest xvfb-run %__pytest
%pytest --pyargs thonny

%files -f %{pyproject_files}
%license licenses/ECLIPSE-ICONS-LICENSE.txt
%doc README.rst CHANGELOG.rst CREDITS.rst
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/thonny.png
%{_datadir}/applications/org.thonny.Thonny.desktop
%{_datadir}/metainfo/org.thonny.Thonny.appdata.xml
%{_mandir}/man1/thonny.1*


%changelog
%autochangelog
