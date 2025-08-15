Name:           python-Rtree
Version:        1.4.0
Release:        %autorelease
Summary:        R-Tree spatial index for Python GIS

# Since the package has a history of arch-dependent bugs (see RHBZ#2055249),
# the base package is arched to flush out any arch-dependent bugs by ensuring
# the tests are run on every architecture. The binary package is still
# pure-Python and correctly noarch. Since there is no compiled code, there is
# no debuginfo to generate.
%global debug_package %{nil}

# SPDX
License:        MIT
URL:            https://github.com/Toblerity/rtree
Source:         %{pypi_source rtree}

# Treat as pure Python since libspatialindex is not bundled
#
# Since we are not bundling libspatialindex as upstream does for PyPI wheel
# distribution, do not force setuptools to treat the package as binary/arched
# (which would cause it to be installed in %%python3_sitearch, and would mean
# this package could not properly be noarch).
#
# Since upstream does want to bundle libspatialindex, this is a downstream-only
# patch.
#
# https://bugzilla.redhat.com/show_bug.cgi?id=2050010
Patch:          0001-Treat-as-pure-Python-since-libspatialindex-is-not-bu.patch

BuildSystem:            pyproject
BuildOption(install):   -l rtree

BuildRequires:  spatialindex-devel

# For testing:
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist numpy}

%global common_description %{expand:
Rtree is a ctypes Python wrapper of libspatialindex that provides a number of
advanced spatial indexing features for the spatially curious Python user. These
features include:

  • Nearest neighbor search
  • Intersection search
  • Multi-dimensional indexes
  • Clustered indexes (store Python pickles directly with index entries)
  • Bulk loading
  • Deletion
  • Disk serialization
  • Custom storage implementation (to implement spatial indexing in ZODB, for
    example)}

%description %{common_description}


%package -n python3-rtree
Summary:        %{summary}

BuildArch:      noarch

Requires:       spatialindex

%description -n python3-rtree %{common_description}


%check -a
%pytest --doctest-modules tests rtree


%files -n python3-rtree -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
