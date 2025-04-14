%global srcname aplpy

Name:           APLpy
Version:        2.2.0
Release:        %autorelease
Summary:        The Astronomical Plotting Library in Python

# SPDX license is MIT
License:        MIT
URL:            http://aplpy.github.com
Source0:        %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel 

%description
APLpy (the Astronomical Plotting Library in Python) is a Python module aimed at 
producing publication-quality plots of astronomical imaging data in FITS format.
The module uses Matplotlib, a powerful and interactive plotting package. It is
capable of creating output files in several graphical formats, including EPS,
PDF, PS, PNG, and SVG.

%package -n python3-APLpy
Summary:        The Astronomical Plotting Library in Python
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires: python3dist(setuptools)

%description -n python3-APLpy
APLpy (the Astronomical Plotting Library in Python) is a Python module aimed at 
producing publication-quality plots of astronomical imaging data in FITS format.
The module uses Matplotlib, a powerful and interactive plotting package. It is
capable of creating output files in several graphical formats, including EPS,
PDF, PS, PNG, and SVG.

%prep
%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install 

%pyproject_save_files -l aplpy

%check
%pyproject_check_import -t

%files -n python3-APLpy -f %{pyproject_files}
%doc CHANGES.md CITATION README.rst

%changelog
%autochangelog
