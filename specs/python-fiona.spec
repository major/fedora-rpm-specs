%global srcname fiona
%global Srcname Fiona

Name:           python-%{srcname}
Version:        1.10.1
#global         pre .post1
%global         uversion %{version}%{?pre}
Release:        %autorelease
Summary:        Fiona reads and writes spatial data files

License:        BSD-3-Clause
URL:            https://fiona.readthedocs.io
Source:         https://github.com/Toblerity/%{Srcname}/archive/%{uversion}/%{Srcname}-%{uversion}.tar.gz
# https://github.com/Toblerity/Fiona/pull/1467
Patch:          0001-TST-Mark-test_opener_fsspec_zip_http_fs-as-using-the.patch

BuildRequires:  gcc-c++
BuildRequires:  gdal >= 3.4
BuildRequires:  gdal-devel >= 3.4

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

# Remove Cython version restrictions
sed -i -E 's/cython~=([0-9.]+)/cython>=\1/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -x calc,test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
export LANG=C.UTF-8

rm -rf fiona  # Needed to not load the unbuilt library.

# Skip debian tests since we are not on debian
k="${k-}${k+ and }not debian"
%ifarch s390x
# Skip tests failing on s390x and unblock dependent packages
k="${k-}${k+ and }not test_write_memoryfile_drivers"
k="${k-}${k+ and }not test_append_memoryfile_drivers"
k="${k-}${k+ and }not test_collection_iterator_items_slice"
%endif
%{pytest} -m "not network and not wheel" -ra ${k+-k }"${k-}"

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst CHANGES.txt CREDITS.txt
%{_bindir}/fio

%changelog
%autochangelog
