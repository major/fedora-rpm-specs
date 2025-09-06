%global srcname munkres

Name:           python-%{srcname}
Version:        1.1.4
Release:        %autorelease
Summary:        A Munkres algorithm for Python

License:        Apache-2.0
URL:            http://software.clapper.org/munkres/
Source0:        https://github.com/bmc/munkres/archive/release-%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
Buildarch:      noarch

%description
The Munkres module provides an implementation of the Munkres algorithm (also
called the Hungarian algorithm or the Kuhn-Munkres algorithm). The algorithm
models an assignment problem as an NxM cost matrix, where each element
represents the cost of assigning the ith worker to the jth job, and it figures
out the least-cost solution, choosing a single item from each row and column in
the matrix, such that no row and no column are used more than once.

%package -n python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  pyproject-rpm-macros

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
The Munkres module provides an implementation of the Munkres algorithm (also
called the Hungarian algorithm or the Kuhn-Munkres algorithm). The algorithm
models an assignment problem as an NxM cost matrix, where each element
represents the cost of assigning the ith worker to the jth job, and it figures
out the least-cost solution, choosing a single item from each row and column in
the matrix, such that no row and no column are used more than once.

%generate_buildrequires
%pyproject_buildrequires -r

%prep
%autosetup -n %{srcname}-release-%{version}
# Remove deprecated universal wheel option if present
[ -f setup.cfg ] && sed -i '/^\[bdist_wheel\]/,/^\[/ s/^universal\s*=.*$//' setup.cfg


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%files -n python3-%{srcname} -f %{pyproject_files}
%doc CHANGELOG.md README.md
%license LICENSE.md

%autochangelog
