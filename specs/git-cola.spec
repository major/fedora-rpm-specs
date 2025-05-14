Name:           git-cola
Version:        4.13.0
Release:        %autorelease
Summary:        A sleek and powerful git GUI

License:        GPL-2.0-or-later
URL:            https://git-cola.github.io
Source0:        https://github.com/git-cola/git-cola/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  git
BuildRequires:  xmlto
BuildRequires:  libappstream-glib
BuildRequires:  rsync
BuildRequires:  python%{python3_pkgversion}-sphinx
BuildRequires:  make

# Test dependencies:
BuildRequires:  python%{python3_pkgversion}dist(pytest)
BuildRequires:  python%{python3_pkgversion}-pyqt6
BuildRequires:  python-unversioned-command

Requires:       python%{python3_pkgversion}-pyqt6
Requires:       git
Requires:       hicolor-icon-theme
Requires:       python%{python3_pkgversion}dist(qtpy)

Recommends:     python%{python3_pkgversion}dist(notify2)
Recommends:     python%{python3_pkgversion}dist(send2trash) >= 1.7.1

%ifarch %{qt6_qtwebengine_arches}
Recommends:     python%{python3_pkgversion}-pyqt6-webengine
%endif

%description
git-cola is a powerful git GUI with a slick and intuitive user interface.


%prep
%autosetup -p1

# fix #!/usr/bin/env python to #!/usr/bin/python3 everywhere
find . -type f -exec sh -c "head {} -n 1 | grep ^#\!\ \*/usr/bin/env\ python >/dev/null && sed -i -e sX^#\!\ \*/usr/bin/env\ python\ \*"\\\$"X#\!/usr/bin/python%{python3_pkgversion}Xg {}" \;

# Remove vendorized polib.py
rm cola/polib.py


%generate_buildrequires
%pyproject_buildrequires


%build
%global makeopts PYTHON="%{__python3}" SPHINXBUILD="$(ls /usr/bin/sphinx-build*|tail -n1)" NO_PRIVATE_LIBS=1 NO_VENDOR_LIBS=1
%pyproject_wheel
make %{makeopts} doc


%install
%pyproject_install
%pyproject_save_files cola
%py_byte_compile %{__python3} %{buildroot}%{_datadir}/git-cola/lib/
make DESTDIR=%{buildroot} prefix=%{_prefix} %{makeopts} \
  install-desktop-files \
  install-doc \
  install-html \
  install-icons \
  install-metainfo


%check
%pytest test
desktop-file-validate %{buildroot}%{_datadir}/applications/git-cola-folder-handler.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/git-cola.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/git-dag.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*.appdata.xml

%files
%license LICENSE
%doc README.md
%{_bindir}/cola
%{_bindir}/git-*
%{_datadir}/applications/git*.desktop
%{_datadir}/metainfo/git*.appdata.xml
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_docdir}/%{name}
%{_mandir}/man1/git*.1*
%{python3_sitelib}/cola
%{python3_sitelib}/git_cola*dist-info


%changelog
%autochangelog
