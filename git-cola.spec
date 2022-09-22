Name:           git-cola
Version:        3.12.0
Release:        %autorelease
Summary:        A sleek and powerful git GUI

License:        GPLv2+
URL:            https://git-cola.github.io
Source0:        https://github.com/git-cola/git-cola/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  git
BuildRequires:  xmlto
BuildRequires:  libappstream-glib
BuildRequires:  rsync
BuildRequires:  python%{python3_pkgversion}-qt5
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-sphinx
BuildRequires: make

Requires:       python%{python3_pkgversion}-qt5
Requires:       git
Requires:       hicolor-icon-theme
Requires:       python%{python3_pkgversion}dist(qtpy)

%if 0%{?rhel} == 0
# RHEL 7 doesn't support suggests and webengine isn't available
Suggests:       python%{python3_pkgversion}-qt5-webkit
Suggests:       python%{python3_pkgversion}-qt5-webengine
%endif

%description
git-cola is a powerful git GUI with a slick and intuitive user interface.


%prep
%setup -q

# fix #!/usr/bin/env python to #!/usr/bin/python3 everywhere
find . -type f -exec sh -c "head {} -n 1 | grep ^#\!\ \*/usr/bin/env\ python >/dev/null && sed -i -e sX^#\!\ \*/usr/bin/env\ python\ \*"\\\$"X#\!/usr/bin/python%{python3_pkgversion}Xg {}" \;


%build
%global makeopts PYTHON="%{__python3}" SPHINXBUILD="$(ls /usr/bin/sphinx-build*|tail -n1)" NO_PRIVATE_LIBS=1 NO_VENDOR_LIBS=1
make %{?_smp_mflags} %{makeopts}
make %{makeopts} doc


%install
make DESTDIR=%{buildroot} prefix=%{_prefix} %{makeopts} install
%py_byte_compile %{__python3} %{buildroot}%{_datadir}/git-cola/lib/
make DESTDIR=%{buildroot} prefix=%{_prefix} %{makeopts} install-doc
make DESTDIR=%{buildroot} prefix=%{_prefix} %{makeopts} install-html
%find_lang %{name}


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/git-cola-folder-handler.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/git-cola.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/git-dag.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*.appdata.xml

%files -f %{name}.lang
%doc COPYING COPYRIGHT README.md
%{_bindir}/cola
%{_bindir}/git-*
%{_datadir}/applications/git*.desktop
%{_datadir}/metainfo/git*.appdata.xml
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_docdir}/%{name}
%{_mandir}/man1/git*.1*
%{python3_sitelib}/cola
%{python3_sitelib}/git_cola*egg-info


%changelog
%autochangelog
