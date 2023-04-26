%global srcname fiona
%global Srcname Fiona

Name:           python-%{srcname}
Version:        1.9.3
#global         pre rc1
%global         uversion %{version}%{?pre}
Release:        %autorelease
Summary:        Fiona reads and writes spatial data files

License:        BSD-3-Clause
URL:            https://fiona.readthedocs.io
Source0:        https://github.com/Toblerity/%{Srcname}/archive/%{uversion}/%{Srcname}-%{uversion}.tar.gz
Patch:          0001-Expand-build-requirement-limits.patch
Patch:          0002-Remove-self-referencing-dependencies.patch

BuildRequires:  gcc-c++
BuildRequires:  gdal >= 3.1
BuildRequires:  gdal-devel >= 3.1

%description
Fiona is designed to be simple and dependable. It focuses on reading and
writing data in standard Python IO style and relies upon familiar Python types
and protocols such as files, dictionaries, mappings, and iterators instead of
classes specific to OGR. Fiona can read and write real-world data using
multi-layered GIS formats and zipped virtual file systems and integrates
readily with other Python GIS packages such as pyproj, Rtree, and Shapely.


%package -n python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel

Recommends:     python3-boto3
Recommends:     python3-shapely

%description -n python3-%{srcname}
Fiona is designed to be simple and dependable. It focuses on reading and
writing data in standard Python IO style and relies upon familiar Python types
and protocols such as files, dictionaries, mappings, and iterators instead of
classes specific to OGR. Fiona can read and write real-world data using
multi-layered GIS formats and zipped virtual file systems and integrates
readily with other Python GIS packages such as pyproj, Rtree, and Shapely.


%prep
%autosetup -n %{Srcname}-%{uversion} -p1

%generate_buildrequires
%pyproject_buildrequires -x s3,calc,test

%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%check
export LANG=C.UTF-8

rm -rf fiona  # Needed to not load the unbuilt library.

# Skip debian tests since we are not on debian
%{pytest} -m "not network and not wheel" -k "not debian" -ra


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst CHANGES.txt CREDITS.txt
%{_bindir}/fio


%changelog
%autochangelog
