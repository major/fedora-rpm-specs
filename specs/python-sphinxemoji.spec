%global _description %{expand:
An extension to use emoji codes in your Sphinx documentation.}

Name:           python-sphinxemoji
Version:        0.3.2
Release:        %{autorelease}
Summary:        Use emoji codes in your Sphinx documentation

# spdx
License:        BSD-3-Clause
URL:            https://pypi.org/pypi/sphinxemoji
Source0:        %{pypi_source sphinxemoji}

BuildArch:      noarch

%description %_description

%package -n python3-sphinxemoji
Summary:        %{summary}
BuildRequires:  python3-devel

%description -n python3-sphinxemoji %_description

%prep
%autosetup -n sphinxemoji-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files sphinxemoji

%check
# No tests

%files -n python3-sphinxemoji -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
