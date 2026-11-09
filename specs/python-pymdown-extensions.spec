%global pypi_name pymdown-extensions

Name:           python-%{pypi_name}
Version:        12.3
Release:        %autorelease
Summary:        Extension pack for Python Markdown

# Most of the package is MIT except two files (highlight.py and superfences.py)
License:        MIT and BSD-2-Clause
URL:            https://facelessuser.github.io/pymdown-extensions
Source:         %{pypi_source pymdown_extensions}

BuildArch:      noarch
 
%description
PyMdown Extensions (pymdownx) is a collection of extensions for Python
Markdown.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%description -n python3-%{pypi_name}
PyMdown Extensions (pymdownx) is a collection of extensions for Python
Markdown.

%pyproject_extras_subpkg -n python3-pymdown-extensions extra

%prep
%autosetup -n pymdown_extensions-%{version} -p1

# EL10 only has markdown 3.5
# https://issues.redhat.com/browse/RHEL-74397
%if 0%{?el10}
sed -i 's/"Markdown>=3.6"/"Markdown>=3.5"/' pyproject.toml
%endif

%generate_buildrequires
%pyproject_buildrequires -x extra

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pymdownx

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE.md
%doc README.md

%changelog
%autochangelog
