%global pypi_name QtAwesome
%global simple_name qtawesome

%global fa5_version 5.15.4
%global fa6_version 6.7.2

Name:       python-%{pypi_name}
Version:    1.4.0
Release:    %autorelease

Summary:    FontAwesome icons in PyQt and PySide applications
# MIT: QtAwesome code and the bundled phosphor and remixicon fonts
# CC-BY-4.0: the bundled codicon font
# Apache-2.0: the bundled material design icons fonts
# OFL-1.1: the bundled elusive icons font
# OFL-1.1-RFN: the bundled fontawesome icon fonts
License:    MIT AND CC-BY-4.0 AND Apache-2.0 AND OFL-1.1 AND OFL-1.1-RFN
URL:        https://github.com/spyder-ide/%{simple_name}

Source:     %{pypi_source %{simple_name}}

BuildArch:  noarch

BuildRequires:  python3-devel

%description
QtAwesome enables iconic fonts such as Font Awesome and Elusive.

It is a port to Python - PyQt / PySide of the QtAwesome C++ library by 
Rick Blommers.

%package -n     python3-%{pypi_name}
Summary:    FontAwesome icons in PyQt and PySide applications
%{?python_provide:%python_provide python3-%{pypi_name}}

#provides font files
#./qtawesome/fonts/codicon.ttf
Provides:   bundled(codicon-fonts) = 0.0.36
#./qtawesome/fonts/elusiveicons-webfont.ttf
Provides:   bundled(elusiveicons-fonts) = 2
#./qtawesome/fonts/materialdesignicons5-webfont.ttf
Provides:   bundled(materialdesignicons5-fonts) = 5.9.55
#./qtawesome/fonts/materialdesignicons6-webfont.ttf
Provides:   bundled(materialdesignicons6-fonts) = 6.9.96
#./qtawesome/fonts/phosphor.ttf
Provides:   bundled(phosphor-fonts) = 1.3
#./qtawesome/fonts/remixicon.ttf
Provides:   bundled(remixicon-fonts) = 2.5
Requires:   fontawesome-fonts-web

%description -n python3-%{pypi_name}

QtAwesome enables iconic fonts such as Font Awesome and Elusive.

It is a port to Python - PyQt / PySide of the QtAwesome C++ library by 
Rick Blommers.

%prep
%autosetup -n %{simple_name}-%{version}

# Fix end of line encoding
sed -i 's/\r//' README.md

# Don't use the bundled fonts.
# This disables verifying the checksum of font files.
sed -i '/^SYSTEM_FONTS = /s/False/True/' qtawesome/iconic_font.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l qtawesome

# Unbundle the fontawesome 5.x/6.x fonts
# Version 6 is backwards compatible with version 5
rm %{buildroot}%{python3_sitelib}/qtawesome/fonts/fontawesome5-*.ttf
ln -s %{_datadir}/fontawesome/webfonts/fa-brands-400.ttf \
      %{buildroot}%{python3_sitelib}/qtawesome/fonts/fontawesome5-brands-webfont-%{fa5_version}.ttf
ln -s %{_datadir}/fontawesome/webfonts/fa-regular-400.ttf \
      %{buildroot}%{python3_sitelib}/qtawesome/fonts/fontawesome5-regular-webfont-%{fa5_version}.ttf
ln -s %{_datadir}/fontawesome/webfonts/fa-solid-900.ttf \
      %{buildroot}%{python3_sitelib}/qtawesome/fonts/fontawesome5-solid-webfont-%{fa5_version}.ttf
rm %{buildroot}%{python3_sitelib}/qtawesome/fonts/fontawesome6-*.ttf
ln -s %{_datadir}/fontawesome/webfonts/fa-brands-400.ttf \
      %{buildroot}%{python3_sitelib}/qtawesome/fonts/fontawesome6-brands-webfont-%{fa6_version}.ttf
ln -s %{_datadir}/fontawesome/webfonts/fa-regular-400.ttf \
      %{buildroot}%{python3_sitelib}/qtawesome/fonts/fontawesome6-regular-webfont-%{fa6_version}.ttf
ln -s %{_datadir}/fontawesome/webfonts/fa-solid-900.ttf \
      %{buildroot}%{python3_sitelib}/qtawesome/fonts/fontawesome6-solid-webfont-%{fa6_version}.ttf

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%{_bindir}/qta-browser
# Script is aimed at Windows users
# https://github.com/spyder-ide/qtawesome/issues/244
%exclude %{_bindir}/qta-install-fonts-all-users

%changelog
%autochangelog
