Name:           python-Rtree
Version:        1.0.1
Release:        %autorelease
Summary:        R-Tree spatial index for Python GIS

# Since the package has a history of arch-dependent bugs (see RHBZ#2055249),
# the base package is arched to flush out any arch-dependent bugs by ensuring
# the tests are run on every architecture. The binary package is still
# pure-Python and correctly noarch. Since there is no compiled code, there is
# no debuginfo to generate.
%global debug_package %{nil}

%global _description %{expand: \
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

# SPDX
License:        MIT
URL:            https://github.com/Toblerity/rtree
Source:         %{pypi_source Rtree}

# Since we are not bundling libspatialindex as upstream does for PyPI wheel
# distribution, do not force setuptools to treat the package as binary/arched
# (which would cause it to be installed in %%python3_sitearch, and would mean
# this package could not properly be noarch).
#
# Since upstream does want to bundle libspatialindex, this is a downstream-only
# patch.
#
# https://bugzilla.redhat.com/show_bug.cgi?id=2050010
Patch:          Rtree-1.0.0-no-bundled-spatialindex.patch

BuildRequires:  spatialindex-devel

BuildRequires:  python3-devel

# For testing:
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(numpy)

%description %{_description}


%package -n python3-rtree
Summary:        %{summary}

BuildArch:      noarch

Requires:       spatialindex

%description -n python3-rtree %{_description}


%prep
%autosetup -n Rtree-%{version} -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files rtree


%check
%pytest --doctest-modules


%files -n python3-rtree -f %{pyproject_files}
# pyproject_files handles LICENSE.txt; verify with “rpm -qL -p …”
%doc README.md


%changelog
%autochangelog
