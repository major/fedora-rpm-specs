%global pypi_name pybbi

Name:           python-%{pypi_name}
Version:        0.4.1
Release:        %{autorelease}
Summary:        Python bindings to the UCSC source for Big Binary Indexed (bigWig/bigBed) files

%global forgeurl https://github.com/nvictus/pybbi
%global tag v%{version}
%forgemeta

# include/oligTm.h and src/oligoTm.c are BSD-4-Clause
License:        MIT AND BSD-4-Clause
URL:            %forgeurl
Source:         %forgesource

# Do not use function pointers of unspecified arguments
# Fixes compatiblity with C23 / GCC 15
Patch:          %{forgeurl}/pull/57.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libpng)

# for %%pyproject_buildrequires -p:
BuildRequires:  pyproject-rpm-macros >= 1.15

%global _description %{expand:
Python interface to Jim Kent's Big Binary Indexed file (BBI) library
from the UCSC Genome Browser source tree using Cython.

This provides read-level access to local and remote bigWig and bigBed
files but no write capabilitites. The main feature is fast retrieval of
range queries into numpy arrays.}

%description %_description


%package -n python3-%{pypi_name}
Summary:        %{summary}
Recommends:     python3dist(pandas)

%description -n python3-%{pypi_name} %_description


%prep
%forgeautosetup -p1

# Allow building with NumPy 1.x
sed -r \
    -e 's/(numpy)[ >=]*2.*"/\1"/' \
    -i pyproject.toml


%generate_buildrequires
%pyproject_buildrequires -x test -p


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l bbi


%check
# Skip tests requiring network
k="${k-}${k+ and }not test_sigs"
k="${k-}${k+ and }not test_aws_403_redirect"
k="${k-}${k+ and }not test_chromsizes"
k="${k-}${k+ and }not test_fetch_remote"
# Test segfaults on `bigBedExample.bb`
k="${k-}${k+ and }not test_fetch_intervals"
%pytest -v --import-mode=importlib ${k+-k }"${k-}"


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md CITATION.cff


%changelog
%autochangelog
