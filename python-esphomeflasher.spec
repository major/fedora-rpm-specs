%global pypi_name esphomeflasher

Name:           python-%{pypi_name}
Version:        1.4.0
Release:        %autorelease
Summary:        Simple GUI tool to flash ESPs over USB

License:        MIT
URL:            https://github.com/esphome/esphome-flasher
# PyPI is missing the latest version, so use the GitHub tarball instead
Source0:        %{url}/archive/%{version}/esphome-flasher-%{version}.tar.gz
Source1:        io.esphome.esphomeflasher.desktop
Source2:        io.esphome.esphomeflasher.metainfo.xml

BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  libicns-utils
BuildRequires:  python3-devel
BuildRequires:  sed

%global _description %{expand:
ESPHome-Flasher is a utility app for the ESPHome framework and is designed to
make flashing ESPs with ESPHome as simple as possible.}

%description %_description

%package -n     %{pypi_name}
Summary:        %{summary}

%description -n %{pypi_name} %_description

%prep
%autosetup -p1 -n esphome-flasher-%{version}
# Relax dependencies
sed -i requirements.txt \
    -e 's:esptool.*:esptool>=3.2:' \
    -e 's:wxpython.*:wxpython<5:'
# Extract icons
icns2png -x icon.icns

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
install -Dpm0644 icon_512x512x32.png %{buildroot}%{_datadir}/pixmaps/%{pypi_name}.png
install -Dpm0644 -t %{buildroot}%{_metainfodir} %{SOURCE2}
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%check
%pyproject_check_import

%files -n %{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/%{pypi_name}
%{_datadir}/applications/io.esphome.esphomeflasher.desktop
%{_datadir}/pixmaps/%{pypi_name}.png
%{_metainfodir}/io.esphome.esphomeflasher.metainfo.xml

%changelog
%autochangelog
