%global srcname fiona
%global Srcname Fiona

Name:           python-%{srcname}
Version:        1.8.21
#global         pre rc1
%global         uversion %{version}%{?pre}
Release:        %autorelease
Summary:        Fiona reads and writes spatial data files

License:        BSD
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://github.com/Toblerity/%{Srcname}/archive/%{uversion}/%{Srcname}-%{uversion}.tar.gz
# https://github.com/Toblerity/Fiona/issues/935
Patch0001:      0001-Skip-DGN-in-test_write_or_driver_error-too.patch
Patch0002:      0002-Add-pytz-to-test-requirements.patch
Patch0003:      0003-Expand-build-requirement-limits.patch

BuildRequires:  gcc-c++
BuildRequires:  gdal >= 1.8
BuildRequires:  gdal-devel >= 1.8

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
%pyproject_buildrequires -r -x s3,calc,test

%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%check
export LANG=C.UTF-8

rm -rf fiona  # Needed to not load the unbuilt library.

# Skip debian tests since we are not on debian
# FIXME pytest segfaults
%{pytest} -m "not network and not wheel" -k "not debian" -ra || :


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst CHANGES.txt CREDITS.txt
%{_bindir}/fio


%changelog
%autochangelog
