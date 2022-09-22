%bcond_with bootstrap

%global srcname contourpy

Name:           python-%{srcname}
Version:        1.0.5
Release:        %autorelease
Summary:        Python library for calculating contours in 2D quadrilateral grids

License:        BSD
URL:            https://contourpy.readthedocs.io/
Source0:        %pypi_source %{srcname}

BuildRequires:  python3-devel
BuildRequires:  gcc-c++

%global _description %{expand:
ContourPy is a Python library for calculating contours of 2D quadrilateral
grids. It is written in C++11 and wrapped using pybind11.

It contains the 2005 and 2014 algorithms used in Matplotlib as well as a newer
algorithm that includes more features and is available in both serial and
multithreaded versions. It provides an easy way for Python libraries to use
contouring algorithms without having to include Matplotlib as a dependency.
}

%description %{_description}

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}

%prep
%autosetup -n %{srcname}-%{version} -p1
%if %{with bootstrap}
sed -i -e '/matplotlib/d' setup.cfg
%endif

%generate_buildrequires
%pyproject_buildrequires -r -x bokeh,test-no-codebase

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%pytest %{?with_bootstrap:-k 'not needs_mpl'}

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
