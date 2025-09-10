%global pypi_name aeidon

Name:           python-%{pypi_name}
Version:        1.15
Release:        25%{?dist}
Summary:        Subtitle file manipulation library

License:        GPL-3.0-or-later
URL:            https://pypi.org/project/%{pypi_name}/
Source0:        %{pypi_source %{pypi_name}}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  gettext

%description
Aeidon is a library for reading, writing and manipulating
text-based subtitle files.

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
Aeidon is a library for reading, writing and manipulating
text-based subtitle files.

%prep
%autosetup -n %{pypi_name}-%{version}
# we want to package aeidon, not gaupol
# the setup.py file is for gaupol
mv setup.py setup_gaupol.py
sed 's/from setup import/from setup_gaupol import/' setup-aeidon.py > setup.py

%generate_buildrequires
rm -rf aeidon/data/{headers,patterns}  # setup.py fails if this was already created
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
* Mon Sep 08 2025 Miro Hrončok <mhroncok@redhat.com> - 1.15-25
- Package the aeidon package, not gaupol
- Fixes: rhbz#2391739

* Tue Sep 02 2025 Sudip Shil <sshil@redhat.com> - 1.15-24
- Remove gaupol dist-info to avoid Provides: python3dist(gaupol) (rhbz#2392348)

* Tue Aug 26 2025 Sudip Shil <sshil@redhat.com> - 1.15-23
- Initial packaging from official PyPI source
