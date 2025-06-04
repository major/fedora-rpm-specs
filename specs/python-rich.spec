%global pypi_name rich

Name:           python-%{pypi_name}
Version:        14.0.0
Release:        %autorelease
Summary:        Render rich text and beautiful formatting in the terminal

# https://spdx.org/licenses/MIT.html
License:        MIT
URL:            https://github.com/Textualize/rich
Source0:        %{url}/archive/v%{version}/rich-%{version}.tar.gz
# Support pygments 2.19+
Patch:          https://github.com/Textualize/rich/pull/3604.patch
Patch:          https://github.com/Textualize/rich/pull/3608.patch
# Support Python 3.14
Patch:          https://github.com/Textualize/rich/pull/3622.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
# for checks
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(attrs)

%description
Rich is a Python library for rich text and beautiful formatting in the terminal.
The Rich API makes it easy to add color and style to terminal output. Rich can
also render pretty tables, progress bars, markdown, syntax highlighted source
code, tracebacks, and more — out of the box.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
# This was previously misnamed, remove the obsolete in Fedora 38, EPEL 10
Obsoletes:      python-%{pypi_name} < 10.16.1-2

%description -n python3-%{pypi_name}
Rich is a Python library for rich text and beautiful formatting in the terminal.
The Rich API makes it easy to add color and style to terminal output. Rich can
also render pretty tables, progress bars, markdown, syntax highlighted source
code, tracebacks, and more — out of the box.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files rich

%check
# add below to make sure initial build will catch runtime import errors
%pyproject_check_import
# test_assemble_meta fails with Python 3.14
# https://github.com/Textualize/rich/issues/3740
%pytest -vv -k 'not test_attrs_broken_310 and not test_assemble_meta'

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
