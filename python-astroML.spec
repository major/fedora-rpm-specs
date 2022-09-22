%global srcname astroML

Name:           python-%{srcname}
Version:        1.0.2.post1
Release:        %autorelease
Summary:        Python tools for machine learning and data mining in Astronomy

License:        BSD
URL:            http://www.astroml.org/
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel


%global _description\
AstroML is a Python module for machine learning and data mining built on\
numpy, scipy, scikit-learn, and matplotlib, and distributed under the\
3-clause BSD license. It contains a growing library of statistical and\
machine learning routines for analyzing astronomical data in python,\
loaders for several open astronomical datasets, and a large suite of\
examples of analyzing and visualizing astronomical datasets.\

%description %_description


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description


%package doc
Summary:        Docs and examples for the %{srcname} package

%description doc
Documentation and examples for %{srcname}.


%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -x test


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%check
%pyproject_check_import
%pytest -q %{srcname}/tests


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.rst
%doc CHANGES.rst README.rst

%files doc
%license LICENSE.rst
%doc CHANGES.rst README.rst examples

%changelog
%autochangelog
