# Created by pyp2rpm-3.3.5
%global pypi_name fixit

%global common_description %{expand:
Fixit is a lint framework that complements Flake8. It’s based on LibCST
which makes it possible to provide auto-fixes. Lint rules are made easy to
build through pattern matching, a test toolkit, and utility helpers (e.g.
scope analysis) for non-trivial boilerplate. It is optimized for efficiency,
easy to customize and comes with many builtin lint rules.}

Name:           python-%{pypi_name}
Version:        0.1.4
Release:        %autorelease
Summary:        A lint framework that writes better Python code for you

License:        MIT
URL:            https://github.com/Instagram/Fixit
# PyPI tarball doesn't include docs
Source0:        %{url}/archive/v%{version}/Fixit-%{version}.tar.gz
Patch0:         %{url}/pull/206.patch#/%{name}-0.1.4-importlib_resources_builtin.patch
BuildArch:      noarch

BuildRequires:  sed
BuildRequires:  python3-devel
BuildRequires:  python3-docs
BuildRequires:  python3-ipykernel
BuildRequires:  python3dist(codecov) >= 2.0.15
BuildRequires:  python3dist(coverage) >= 4.5.4
BuildRequires:  python3dist(diff-cover) >= 3.0.1
BuildRequires:  python3dist(flake8) >= 3.8.1
BuildRequires:  python3dist(libcst) >= 0.3.10
BuildRequires:  python3dist(nbsphinx) >= 0.7.1
BuildRequires:  python3dist(prompt-toolkit) >= 2.0.9
BuildRequires:  python3dist(pyyaml) >= 5.2
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx-rtd-theme) >= 0.5
BuildRequires:  python3dist(pytest)

%description
%{common_description}

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
%{common_description}

%package        doc
Summary:        %{name} documentation
Requires:       python3-docs

%description    doc
Documentation for %{name}

%prep
%autosetup -n Fixit-%{version} -p1
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# Use local intersphinx inventory
sed -r \
    -e 's|https://docs.python.org/3|%{_docdir}/python3-docs/html|' \
    -i docs/source/conf.py

%build
%py3_build
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%pytest

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst CHANGELOG.md
%{_bindir}/fixit
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%files doc
%doc html
%license LICENSE

%changelog
%autochangelog
