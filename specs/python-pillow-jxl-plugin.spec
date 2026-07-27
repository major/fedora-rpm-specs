Name:           python-pillow-jxl-plugin
Version:        1.3.8
Release:        %autorelease
Summary:        Pillow plugin for JPEG-XL
# GPL-3.0-or-later for code
# CC-BY and CC-BY-SA for test images
SourceLicense:  GPL-3.0-or-later AND CC-BY-4.0 AND CC-BY-SA-4.0

# BSD-2-Clause OR Apache-2.0 OR MIT
# GPL-3.0-or-later
# MIT OR Apache-2.0
# Unlicense OR MIT
# Zlib OR Apache-2.0 OR MIT
License:        %{shrink:
    GPL-3.0-or-later AND
    (Apache-2.0 OR MIT) AND
    (Apache-2.0 OR MIT OR Zlib) AND
    (BSD-2-Clause OR Apache-2.0 OR MIT) AND
    (Unlicense OR MIT)
    }
# LICENSE.dependencies contains a full license breakdown

URL:            https://github.com/Isotr0py/pillow-jpegxl-plugin
Source:         %{url}/archive/v%{version}/pillow-jpegxl-plugin-%{version}.tar.gz

# drop custom build system that is unnecessary and only breaks stuff
Patch:          0001-Unconditionally-dynamically-link-libjxl.patch

# Allow older jpgegxl-rs 0.12–0.14; upstream has updated to 0.15 without
# source-code changes, but coordination with glycin is needed to avoid a compat
# package.
#
# https://github.com/Isotr0py/pillow-jpegxl-plugin/commit/3b36d36d7593ab524745aba6d456bcc11b7b97b8
# https://github.com/Isotr0py/pillow-jpegxl-plugin/commit/042967a1ee8d819ef053e9822349363db5c920e9
# https://github.com/Isotr0py/pillow-jpegxl-plugin/commit/c5369ab39bec720399a7aeefe0f48087ab7cb578
Patch:          0002-Allow-jpegxl-rs-as-old-as-0.12.patch

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
%autosetup -n pillow-jpegxl-plugin-%{version} -p1
%cargo_prep

%generate_buildrequires
%pyproject_buildrequires
%cargo_generate_buildrequires

%build
# write license summary and breakdown
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l pillow_jxl

%check
%pyproject_check_import

%files -n python3-pillow-jxl-plugin -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
