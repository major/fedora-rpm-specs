Name:           inkscape-silhouette
Version:        1.29
Release:        %autorelease
Summary:        Plotter software

License:        GPL-2.0-only AND GPL-2.0-or-later
URL:            https://github.com/fablabnbg/inkscape-silhouette
VCS:            git:https://github.com/fablabnbg/inkscape-silhouette.git
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# Use Python3 in all executable Python files
Patch:          python3.patch

BuildRequires:  inkscape
BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pyusb)
BuildRequires:  umockdev-devel
BuildArch:      noarch

Requires: inkscape
Requires: python3dist(cssselect)
Requires: python3dist(lxml)
Requires: python3dist(matplotlib)
Requires: python3dist(numpy)
Requires: python3dist(pyusb)
Requires: python3dist(tinycss2)
Requires: python3dist(xmltodict)

%description
An application for controlling 2D plotters, cutters, engravers, and CNC
machines.

%package doc
Summary: Examples

%description doc
Examples for Inkscape Silhouette.

%prep
%autosetup -p1 -n %{name}-%{version}
# Remove bundled unused libusb
# https://github.com/fablabnbg/inkscape-silhouette/pull/186
rm -r silhouette/pyusb-1.0.2/

%generate_buildrequires
%pyproject_buildrequires

%build
%make_build mo

%install
find silhouette -type f -exec install -Dm 755 "{}" \
  "%{buildroot}%{_datadir}/inkscape/extensions/silhouette/{}" \;
install -Dpm 755 render_silhouette_regmarks.py \
  %{buildroot}%{_datadir}/inkscape/extensions/render_silhouette_regmarks.py
install -Dpm 755 sendto_silhouette.py \
  %{buildroot}%{_datadir}/inkscape/extensions/sendto_silhouette.py
install -Dpm 755 silhouette_multi.py \
  %{buildroot}%{_datadir}/inkscape/extensions/silhouette_multi.py
install -Dpm 644 silhouette_multi.inx \
  %{buildroot}%{_datadir}/inkscape/extensions/silhouette_multi.inx
install -Dpm 644 sendto_silhouette.inx \
  %{buildroot}%{_datadir}/inkscape/extensions/sendto_silhouette.inx
install -Dpm 644 render_silhouette_regmarks.inx \
  %{buildroot}%{_datadir}/inkscape/extensions/render_silhouette_regmarks.inx
find locale -type f -exec install -Dm 644 "{}" \
  "%{buildroot}%{_datadir}/{}" \;
install -Dpm 644 silhouette-udev.rules \
  %{buildroot}%{_prefix}/lib/udev/rules.d/40-silhouette-udev.rules
install -Dpm 644 silhouette-icon.png \
  %{buildroot}%{_prefix}/lib/udev/silhouette-icon.png
install -Dpm 644 silhouette-udev-notify.sh \
  %{buildroot}%{_prefix}/lib/udev/silhouette-udev-notify.sh
install -Dpm 644 templates/silhouette-cameo-registration-marks-a4.svg \
  %{buildroot}%{_datadir}/inkscape/templates/silhouette-cameo-registration-marks-a4.svg

%find_lang %{name}

%check
%pytest test


%files -f %{name}.lang
%doc README.md
%doc USERGUIDE.md
%doc HISTORY.txt
%license LICENSE
%{_datadir}/inkscape/extensions/*silhouette*.py
%{_datadir}/inkscape/extensions/*silhouette*.inx
%{_datadir}/inkscape/extensions/silhouette/
%{_datadir}/inkscape/templates/silhouette-cameo-registration-marks-a4.svg
%{_prefix}/lib/udev/rules.d/40-silhouette-udev.rules
%dir %{_prefix}/lib/udev/
%{_prefix}/lib/udev/silhouette-icon.png
%{_prefix}/lib/udev/silhouette-udev-notify.sh

%files doc
%license LICENSE
%doc examples/

%changelog
%autochangelog
