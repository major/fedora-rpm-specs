Name:           convertall
Version:        0.8.0
Release:        %autorelease
Summary:        Unit converter
License:        GPL-2.0-or-later
URL:            https://bellz.org/ConvertAll-py/
Source:         https://github.com/doug-101/ConvertAll-py/releases/download/v%{version}/convertall-%{version}.tar.gz
# use XDG_CONFIG_HOME
Patch:          xdg-config.patch
# upstream patches post 0.8.0
Patch:          0001-tweak-unit-data-formulas-to-work-better-with-dart-fl.patch
Patch:          0003-added-units-teenth-Bohr-radius-kip-dunam-MGD-MLD-mm-.patch

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pyqt5}
Requires:       hicolor-icon-theme
Requires:       python3
Requires:       %{py3_dist pyqt5}

BuildArch:      noarch

%description
With ConvertAll, you can combine the units any way you want. If you want
to convert from inches per decade, that's fine. Or from meter-pounds. Or
from cubic nautical miles. The units don't have to make sense to anyone
else.


%prep
%autosetup -n ConvertAll -p1


%build


%install
./install.py \
  -b %{buildroot} \
  -d %{_docdir}/%{name} \
  -i %{_datadir}/%{name}/icons \
  -p %{_prefix}
%py_byte_compile %{python3} %{buildroot}%{_datadir}/%{name}

# desktop files
install -D -m0644 icons/%{name}_sm.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}-icon.png
install -D -m0644 icons/%{name}_med.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}-icon.png
install -D -m0644 icons/%{name}_lg.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}-icon.png

mkdir -p %{buildroot}%{_metainfodir}
cat > %{buildroot}%{_metainfodir}/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<component type="desktop">
  <id>com.bellz.ConvertAll</id>
  <metadata_license>CC0-1.0</metadata_license>
  <project_license>GPL-2.0-or-later</project_license>
  <name>ConvertAll</name>
  <developer_name>Doug Bell</developer_name>
  <summary>A flexible unit converter</summary>
  <url type="homepage">https://bellz.org/ConvertAll-py/</url>
  <url type="bugtracker">https://github.com/doug-101/ConvertAll-py/issues</url>
  <content_rating type="oars-1.0" />
  <description>
    <p>With ConvertAll, you can combine the units any way you want. If you want to convert from inches 
       per decade, that's fine. Or from meter-pounds. Or from cubic nautical miles. The units don't have
       to make sense to anyone else.</p>
  </description>
  <screenshots>
    <screenshot type="default">
      <image>https://bellz.org/ConvertAll-py/convertall.png</image>
    </screenshot>
  </screenshots>
  <launchable type="desktop-id">convertall.desktop</launchable>
  <releases>
    <release version="%{version}" date="%(date +%F -r %{SOURCE0})" />
  </releases>
</component>
EOF

# unwanted files
find %{buildroot}%{_docdir}/%{name} -delete
rm -f %{buildroot}%{_datadir}/%{name}/%{name}.{pro,spec}
rm -f %{buildroot}%{_datadir}/%{name}/translations/{*.ts,qt_*.qm}

%find_lang %{name} --with-qt --without-mo


%check
%{python3} source/convertall.py -q mile^2/hr acre/s
# 1.0 mile^2 / hr = 0.17777778 acre / s
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop


%files -f %{name}.lang
%license doc/LICENSE
%doc doc/README*.html
%{_bindir}/convertall
%{_datadir}/applications/convertall.desktop
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.py
%{_datadir}/%{name}/__pycache__
%{_datadir}/%{name}/data/
%{_datadir}/%{name}/icons/
%dir %{_datadir}/%{name}/translations
%{_datadir}/icons/hicolor/*/apps/%{name}-icon.*
%{_metainfodir}/%{name}.appdata.xml


%changelog
%autochangelog
