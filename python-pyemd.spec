%global desc %{expand: \
PyEMD is a Python wrapper for Ofir Pele and Michael Werman's implementation of
the Earth Mover's Distance that allows it to be used with NumPy. If you use
this code, please cite the papers listed in the README.rst file.}

Name:           python-pyemd
Version:        1.0.0
Release:        %autorelease
Summary:        Fast EMD for Python


License:        MIT
URL:            https://github.com/wmayner/pyemd
Source0:        %{pypi_source pyemd}

%description
%{desc}

%package -n python3-pyemd
Summary:        %{summary}
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pytest}

%description -n python3-pyemd
%{desc}


%prep
%autosetup -n pyemd-%{version}

# don't install dev files
sed -i 's/include_package_data=True/include_package_data=False/' setup.py

# use numpy, not oldest-supported-numpy
sed -i 's/oldest-supported-numpy/numpy/' pyproject.toml

sed -i '/\/usr\/bin\/env python3/ d' src/pyemd/__init__.py
sed -i '/\/usr\/bin\/env python3/ d' src/pyemd/emd.pyx

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pyemd

%check
export PYTHONPATH=%{buildroot}/%{python3_sitearch}
%{pytest}

%files -n python3-pyemd -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
