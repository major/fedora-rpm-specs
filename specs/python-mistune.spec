%bcond doc 1

Name:           python-mistune
Version:        3.2.1
Release:        %autorelease
Summary:        Markdown parser for Python

License:        BSD-3-Clause
URL:            https://github.com/lepture/mistune
Source:         %{url}/archive/v%{version}/mistune-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
# The dev dependency group is too broad-scoped, we only need pytest.
BuildRequires:  python3dist(pytest)

%global common_description %{expand:
The fastest markdown parser in pure Python, inspired by marked.}

%description %{common_description}

%package -n python3-mistune
Summary:        %{summary}

%description -n python3-mistune %{common_description}

%if %{with doc}
%package doc
Summary:        Documentation for %{name}

%description doc
%{common_description}

This is the documentation package for %{name}.
%endif

%prep
%autosetup -p1 -n mistune-%{version}

# replace shibuya theme which is not available in Fedora with sphinx read the docs theme
sed -i 's/html_theme = "shibuya"/html_theme = "sphinx_rtd_theme"/' docs/conf.py
sed -i "s/shibuya/sphinx-rtd-theme/" pyproject.toml

%generate_buildrequires
%pyproject_buildrequires %{?with_doc:-g docs}

%build
%pyproject_wheel

%if %{with doc}
# generate html docs
PYTHONPATH=$PWD/build/lib sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%pyproject_install
%pyproject_save_files mistune

%check
%pytest

%files -n python3-mistune -f %{pyproject_files}
%doc README.rst

%if %{with doc}
%files doc
%doc html
%license LICENSE
%endif

%changelog
%autochangelog
