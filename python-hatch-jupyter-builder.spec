Name:           python-hatch-jupyter-builder
Version:        0.8.2
Release:        1%{?dist}
Summary:        A hatch plugin to help build Jupyter packages
License:        BSD-3-Clause
URL:            https://pypi.org/project/hatch-jupyter-builder/
Source:         %{pypi_source hatch_jupyter_builder}

BuildArch:      noarch
BuildRequires:  python3-devel
# Test deps, upstream contains pre-commit, pytest-cov etc.
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-mock
BuildRequires:  python3-tomli

%global _description %{expand:
This provides a build hook plugin for Hatch that adds
a build step for use with Jupyter packages.}


%description %_description

%package -n     python3-hatch-jupyter-builder
Summary:        %{summary}

%description -n python3-hatch-jupyter-builder %_description


%prep
%autosetup -p1 -n hatch_jupyter_builder-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files hatch_jupyter_builder


%check
# Skipped tests installs from internet
%pytest -k "not test_hatch_build"


%files -n python3-hatch-jupyter-builder -f %{pyproject_files}
%doc README.md
%{_bindir}/hatch-jupyter-builder


%changelog
* Wed Dec 14 2022 Lumír Balhar <lbalhar@redhat.com> - 0.8.2-1
- Update to 0.8.2 (rhbz#2152911)

* Mon Nov 28 2022 Lumír Balhar <lbalhar@redhat.com> - 0.8.1-1
- Initial package