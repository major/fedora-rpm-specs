%global pypi_name unicode-segmentation-rs
%global srcname unicode_segmentation_rs

%global common_description %{expand:
Python bindings for the Rust unicode-segmentation and unicode-width crates.
It provides functions to correctly split strings by words, sentences, or
grapheme clusters according to Unicode Standard Annex #29.}

Name:           python-%{pypi_name}
Version:        0.2.0
Release:        2%{?dist}
Summary:        Unicode segmentation and width for Python using Rust

License:        MIT AND (MIT OR Apache-2.0)
URL:            https://github.com/WeblateOrg/unicode-segmentation-rs
Source0:        https://files.pythonhosted.org/packages/source/u/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  cargo-rpm-macros
BuildRequires:  gcc

%description %{common_description}

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{common_description}

%prep
%autosetup -n %{srcname}-%{version}

rm -f Cargo.lock

sed -i 's/maturin>=1.10/maturin>=1.9/' pyproject.toml

sed -i 's/"generate-import-lib",//g' Cargo.toml
sed -i 's/, "generate-import-lib"//g' Cargo.toml

%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires
%pyproject_buildrequires

%build
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies

%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%license LICENSE.dependencies
%doc README.md

%changelog
* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Tue Dec 16 2025 Sudip Shil <sshil@fedora> - 0.2.0-1
- Initial packaging of python-unicode-segmentation-rs
