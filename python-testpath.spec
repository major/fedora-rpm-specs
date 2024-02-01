%bcond_without docs

Name:           python-testpath
Version:        0.6.0
Release:        %autorelease
Summary:        Test utilities for code working with files and commands

License:        BSD-3-Clause
URL:            https://github.com/jupyter/testpath

Source0:        %{pypi_source testpath}

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with docs}
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
%endif

%global _description %{expand:
Testpath is a collection of utilities for Python code working with files and
commands.

It contains functions to check things on the filesystem, and tools for
mocking system commands and recording calls to those.}

%description %_description


%package -n     python3-testpath
Summary:        %summary

%description -n python3-testpath %_description


%if %{with docs}
%package        doc
Summary:        %{name} documentation
%description doc
Documentation for %{name}.
%endif


%prep
%autosetup -n testpath-%{version}

# The exe files are only needed on Microsoft Windows
rm -f testpath/*.exe


%generate_buildrequires
%pyproject_buildrequires -x test


%build
%pyproject_wheel

%if %{with docs}
# generate html docs
sphinx-build-3 doc html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif


%install
%pyproject_install
%pyproject_save_files testpath


%check
%pytest


%files -n python3-testpath -f %{pyproject_files}
%doc README.rst
%license LICENSE

%if %{with docs}
%files doc
%doc html
%endif


%changelog
%autochangelog
