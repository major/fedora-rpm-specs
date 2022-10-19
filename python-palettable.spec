%global _description %{expand:
Palettable (formerly brewer2mpl) is a library of color palettes for Python.

It's written in pure Python with no dependencies, but it can supply
color maps for matplotlib. You can use Palettable to customize matplotlib
plots or supply colors for a web application.}

Name:           python-palettable
Version:        3.3.0
Release:        %{autorelease}
Summary:        Library of color palettes for Python
BuildArch:      noarch

License:        MIT AND BSD-2-Clause AND Apache-2.0
URL:            https://pypi.org/pypi/palettable
Source0:        %{pypi_source palettable}

%description %_description

%package -n python3-palettable
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%description -n python3-palettable %_description


%prep
%autosetup -p1 -n palettable-%{version}

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files palettable


%check
%{pytest}


%files -n python3-palettable -f %{pyproject_files}
%doc README.rst
%license license.txt
%license palettable/colorbrewer/data/colorbrewer_licence.txt

%changelog
%autochangelog
