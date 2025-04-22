%bcond_without tests
%bcond_without doc_html

%global pypi_name NiaARMTS

%global _description %{expand:
Framework for numerical association rule mining in time series data using
stochastic population-based nature-inspired algorithms. It provides tools
to extract association rules from time series datasets while incorporating
key metrics such as support, confidence, inclusion, and amplitude.
Although independent from the NiaARM framework, this software can be viewed
as an extension, with additional support for time series numerical
association rule mining.
}

Name:           python-niaarmts
Version:        0.1.7
Release:        %autorelease
Summary:        Nature-Inspired Algorithms for Time Series Numerical Association Rule Mining

License:        MIT
URL:            https://github.com/firefly-cpp/%{pypi_name}
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-toml-adapt
BuildRequires:  python3-pytest

%if %{with doc_html}
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinxcontrib-bibtex}
BuildRequires:  %{py3_dist sphinx_lv2_theme}
%endif

%description %_description

%package -n python3-niaarmts
Summary:        %{summary}

%description -n python3-niaarmts %_description

%package doc
Summary:        HTML documentation and examples for %{name}

%description doc
HTML documentation and examples for %{name}.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

# Relax pandas and matplotlib dependency versions
toml-adapt -path pyproject.toml -a change -dep pandas -ver X
toml-adapt -path pyproject.toml -a change -dep matplotlib -ver X

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%if %{with doc_html}
sphinx-build -b html docs docs/_build/html \
    -D html_theme=sphinx_lv2_theme
%endif

%install
%pyproject_install
%pyproject_save_files niaarmts

%check
%pyproject_check_import
%if %{with tests}
%pytest
%endif

%files -n python3-niaarmts -f %{pyproject_files}
%license LICENSE
%doc README.md

%files doc
%license LICENSE
%if %{with doc_html}
%doc docs/_build/html
%endif

%changelog
%autochangelog
