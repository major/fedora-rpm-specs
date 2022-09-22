%global pypi_name noiseprotocol

Name:           python-%{pypi_name}
Version:        0.3.1
Release:        %autorelease
Summary:        Python 3 implementation of Noise Protocol Framework

License:        MIT
URL:            https://github.com/plizonczyk/noiseprotocol
# PyPI is missing tests, so use the GitHub tarball instead
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme

%global _description %{expand:
noiseprotocol is a Python 3 implementation of Noise Protocol Framework.}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%package -n python-%{pypi_name}-doc
Summary:        Documentation and examples for %{name}

%description -n python-%{pypi_name}-doc
This package contains additional documentation and examples for
%{name}.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

# Fix permissions
chmod -x README.md

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel
make -C docs html SPHINXBUILD="python3 -msphinx"

%install
%pyproject_install
%pyproject_save_files noise

# Clean out examples
rm -r %{buildroot}%{python3_sitelib}/examples

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md

%files -n python-%{pypi_name}-doc
%license LICENSE
%doc docs/_build/html examples

%changelog
%autochangelog
