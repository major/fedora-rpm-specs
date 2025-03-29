%global pypi_name pillow_jxl_plugin

Name:           python-pillow-jxl-plugin
Version:        1.3.2
Release:        %autorelease
Summary:        Pillow plugin for JPEG-XL
# GPL-3.0-or-later for code
# CC-BY and CC-BY-SA for test images
SourceLicense:  GPL-3.0-or-later and CC-BY-4.0 and CC-BY-SA-4.0

# Apache-2.0 OR MIT
# GPL-3.0-or-later
# MIT
# MIT OR Apache-2.0
# Unlicense OR MIT
License:        GPL-3.0-or-later AND MIT AND (Apache-2.0 OR MIT) AND (Unlicense OR MIT)
# LICENSE.dependencies contains a full license breakdown

URL:            https://github.com/Isotr0py/pillow-jpegxl-plugin
Source:         %{pypi_source %{pypi_name}}

# Add documentation of test data licensing
Patch:          https://github.com/Isotr0py/pillow-jpegxl-plugin/commit/a8cb1918e2f1c0e20e5188dbe496186f106ead43.patch

# drop custom build system that is unnecessary and only breaks stuff
Patch:          0001-Unconditionally-dynamically-link-libjxl.patch

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  python3-devel
BuildRequires:  jpegxl-devel
BuildRequires:  libstdc++-devel

%global _description %{expand:
Pillow plugin for JPEG-XL, using Rust for bindings.}

%description %{_description}

%package     -n python3-pillow-jxl-plugin
Summary:        Pillow plugin for JPEG-XL

%description -n python3-pillow-jxl-plugin %{_description}

%prep
%autosetup -n %{pypi_name}-%{version} -p1
%cargo_prep

%generate_buildrequires
%pyproject_buildrequires
%cargo_generate_buildrequires

%build
%pyproject_wheel

# write license summary and breakdown
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
%pyproject_install
%pyproject_save_files pillow_jxl

%check
%pyproject_check_import

%files -n python3-pillow-jxl-plugin -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
