Name:           pyhoca-gui
Version:        0.6.1.1
Release:        %autorelease
Summary:        Graphical X2Go client written in (wx)Python

License:        AGPL-3.0-or-later
URL:            https://www.x2go.org/
Source0:        https://code.x2go.org/releases/source/%{name}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-distutils-extra
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
# Requires are in /usr/bin/pyhoca and not found by dependency generator
Requires:       python%{python3_pkgversion}-cups
Requires:       python%{python3_pkgversion}-setproctitle
Requires:       python%{python3_pkgversion}-x2go >= 0.5.0.0
Requires:       libnotify
Requires:       python%{python3_pkgversion}-gobject-base
Requires:       python%{python3_pkgversion}-wxpython4

%description
X2Go is a server based computing environment with:
   - session resuming
   - low bandwidth support
   - LDAP support
   - client side mass storage mounting support
   - client side printing support
   - audio support
   - authentication by smartcard and USB stick

PyHoca-GUI is a slim X2Go client that docks to the desktop's
notification area and allows multiple X2Go session handling.


%prep
%autosetup -p1


%generate_buildrequires
%pyproject_buildrequires


%build
# Fix shebang of pyhoca-gui executable.
%py3_shebang_fix %{name}
%{__python3} setup.py build_i18n
%pyproject_wheel


%install
%pyproject_install
rm -r %{buildroot}%{python3_sitelib}%{_datadir}/locale
mv %{buildroot}%{python3_sitelib}%{_datadir}/* %{buildroot}%{_datadir}/
%pyproject_save_files -l pyhoca
mkdir -p %{buildroot}%{_bindir}/
cp -p %{name} %{buildroot}%{_bindir}/
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%find_lang PyHoca-GUI


%files -f PyHoca-GUI.lang -f %{pyproject_files}
%doc README TODO
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/PyHoca/
%{_datadir}/pixmaps/pyhoca_x2go-logo-ubuntu.svg
%{_datadir}/pyhoca
%{_mandir}/man1/%{name}.1*
%{python3_sitelib}/PyHoca_GUI-*-nspkg.pth


%changelog
%autochangelog
