
# avoid empty debuginfo package
%define debug_package %{nil}

# trim changelog included in binary rpms
%global _changelog_trimtime %(date +%s -d "1 year ago")

Name:    eric
Summary: Python IDE
Version: 24.3
Release: %autorelease

License: GPLv3+
URL:     https://eric-ide.python-projects.org
Source0: https://downloads.sourceforge.net/sourceforge/eric-ide/%{name}7-%{version}.tar.gz
BuildArch: noarch
# webengine not available on all archs
ExclusiveArch: %{qt6_qtwebengine_arches} noarch

Source30: eric-32.png
Source31: eric-48.png
Source32: eric-64.png

## downstream patches
# sane defaults: disable version check, qt5/qt6 configuration
Patch100: eric7-23.9-defaults.patch

BuildRequires: desktop-file-utils
BuildRequires: python3-devel python3
BuildRequires: python3-pyqt6
BuildRequires: python3-pyqt6-charts
BuildRequires: python3-pyqt6-webengine
BuildRequires: python3-qscintilla-qt6
%if 0%{?fedora}
BuildRequires: libappstream-glib
%endif

Provides: eric7 = %{version}-%{release}

Requires: python3-pyqt6
Requires: python3-pyqt6-charts
Requires: python3-pyqt6-webengine
Requires: python3-qscintilla-qt6
Requires: python3dist(asttokens)
Requires: python3dist(black)
Requires: python3dist(chardet)
Requires: python3dist(coverage)
Requires: python3dist(chardet)
Requires: python3dist(docutils)
Requires: python3dist(editorconfig)
Requires: python3dist(isort)
Requires: python3dist(jedi)
Requires: python3dist(markdown)
Requires: python3dist(packaging)
Requires: python3dist(parso)
Requires: python3dist(pip)
Requires: python3dist(pygments)
Requires: python3dist(pyyaml)
Requires: python3dist(semver)
Requires: python3dist(tomlkit)
Requires: python3dist(trove-classifiers)
Requires: python3dist(wheel)
Recommends: python3-docs
Recommends: qt6-doc-html
Recommends: qt6-qttranslations

%description
eric7 is a full featured Python IDE.


%prep
%autosetup -p1 -n eric7-%{version}


%build
# Empty build


%install
%{__python3} install.py \
  -i %{buildroot}/ \
  -b %{_bindir} \
  -d %{python3_sitelib} \
  -z

# icons
install -m644 -p -D %{SOURCE30} %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/eric.png
install -m644 -p -D %{SOURCE32} %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/eric.png

# non-standard category
desktop-file-edit --remove-category=MicroPython %{buildroot}%{_datadir}/applications/eric7_mpy.desktop

%find_lang %{name} --with-qt --all-name

## unpackaged files
# duplicate file
rm -fv  %{buildroot}%{_datadir}/appdata/eric7.appdata.xml
# deprecated icons
rm -rfv %{buildroot}%{_datadir}/icons/eric*
rm -fv  %{buildroot}%{python3_sitelib}/eric7/LICENSE.txt

sed -i -e 's|-i %{buildroot}/||' %{buildroot}%{python3_sitelib}/eric7/eric7install.json


%check
%if 0%{?fedora}
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/eric7.appdata.xml
%endif
test "$(grep '^Exec' %{buildroot}%{_datadir}/applications/eric7_ide.desktop)" = "Exec=%{_bindir}/eric7_ide"
desktop-file-validate %{buildroot}%{_datadir}/applications/eric7_browser.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/eric7_ide.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/eric7_mpy.desktop


%files -f %{name}.lang
%doc eric/docs/README.md
%doc eric/docs/THANKS
%license eric/docs/LICENSE.txt
%{_bindir}/eric7*
%pycached %{python3_sitelib}/eric7config.py
%dir %{python3_sitelib}/eric7/
%pycached %{python3_sitelib}/eric7/*.py
%exclude %{python3_sitelib}/eric7/*.pyw
%{python3_sitelib}/eric7/icons/
%{python3_sitelib}/eric7/pixmaps/
%{python3_sitelib}/eric7/[A-Z]*/
%{python3_sitelib}/eric7/*.ekj
%{python3_sitelib}/eric7/*.json
%dir %{python3_sitelib}/eric7/i18n/
%{python3_sitelib}/eric7plugins/
%{_metainfodir}/eric7.appdata.xml
%{_datadir}/applications/eric7_browser.desktop
%{_datadir}/applications/eric7_ide.desktop
%{_datadir}/applications/eric7_mpy.desktop
%{_datadir}/icons/hicolor/*/apps/eric*
%{_datadir}/qt6/qsci/api/MicroPython/
%{_datadir}/qt6/qsci/api/Python3/
%{_datadir}/qt6/qsci/api/QSS/


%changelog
%autochangelog
