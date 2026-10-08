%global pypi_name unicode-segmentation-rs
%global srcname unicode_segmentation_rs

%global common_description %{expand:
Python bindings for the Rust unicode-segmentation and unicode-width crates.
It provides functions to correctly split strings by words, sentences, or
grapheme clusters according to Unicode Standard Annex #29.}

Name:           python-%{pypi_name}
Version:        0.3.3
Release:        1%{?dist}
Summary:        Unicode segmentation and width for Python using Rust

# The source is MIT (except for certain non-code files licensed CC0-1.0 that do
# not contributing to the licenses of the binary RPMs). Statically linked Rust
# dependencies contribute the following (from the output of
# %%{cargo_license_summary}):
#
# MIT
# MIT OR Apache-2.0
License:        MIT AND (MIT OR Apache-2.0)
URL:            https://github.com/WeblateOrg/unicode-segmentation-rs
Source0:        https://files.pythonhosted.org/packages/source/u/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRequires:  cargo-rpm-macros
BuildRequires:  gcc

BuildRequires:  %{py3_dist pytest}

%description %{common_description}

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{common_description}

%prep
%autosetup -n %{srcname}-%{version}


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
%pytest -v

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%license LICENSE.dependencies
%doc README.md

%changelog
* Tue Sep 29 2026 Manish Tiwari <matiwari@redhat.com> - 0.3.3-1
- Update to version 0.3.3 (close RHBZ#2500824)

* Thu Sep 03 2026 Maxwell G <maxwell@gtmx.me> - 0.2.4-4
- Rebuild with latest Rust compiler to enable SHSTK support

* Wed Jul 22 2026 Python Maint <python-maint@redhat.com> - 0.2.4-3
- Rebuilt for Python 3.15.0b4 ABI change

* Thu Jul 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Thu Jul 02 2026 Benjamin A. Beasley <code@musicinmybrain.net> - 0.2.4-1
- Update to version 0.2.4 (close RHBZ#2496486)
- Update to PyO3 0.29

* Wed Jun 03 2026 Python Maint <python-maint@redhat.com> - 0.2.0-3
- Rebuilt for Python 3.15

* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Tue Dec 16 2025 Sudip Shil <sshil@fedora> - 0.2.0-1
- Initial packaging of python-unicode-segmentation-rs
