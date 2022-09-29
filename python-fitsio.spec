%global srcname fitsio
%global sum A full featured python library to read from and write to FITS files


Name:           python-%{srcname}
Version:        1.1.8
Release:        %autorelease
Summary:        %{sum}

License:        GPLv2+
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        %{pypi_source}

# Patch to force usage of Fedora cfitsio instead of bundled copy
Patch0:         %{name}-use-system-cfitsio.patch

# General
BuildRequires:  cfitsio-devel
BuildRequires:  gcc
# Python 3
BuildRequires:  python3-devel


%description
%{sum}.

%package -n python3-%{srcname}
Summary:        %{sum}

%description -n python3-%{srcname}
%{sum}.


%prep
%autosetup -p1 -n %{srcname}-%{version}

sed -i "s,@INCLUDEDIR@,%{_includedir}/cfitsio,g" setup.py
sed -i "s,@LIBDIR@,%{_libdir},g" setup.py

# Remove egg files from source
rm -r %{srcname}.egg-info


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files fitsio


%check
%pyproject_check_import


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.txt
%doc README.md


%changelog
%autochangelog
