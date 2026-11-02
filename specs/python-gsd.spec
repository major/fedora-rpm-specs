%global forgeurl https://github.com/glotzerlab/gsd
Version:        5.0.1
%forgemeta

Name:           python-gsd
Release:        %autorelease
Summary:        Read and write GSD files for use with HOOMD-blue

License:        BSD-2-Clause
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist cython}
BuildRequires:  %{py3_dist numpy}
BuildRequires:  %{py3_dist pytest}

BuildSystem:    pyproject
BuildOption(prep): -n gsd-%{version}
BuildOption(install): -l gsd

%global _description %{expand:
The GSD file format is the native file format for HOOMD-blue. GSD files store
trajectories of the HOOMD-blue system state in a binary file with efficient
random access to frames. GSD allows all particle and topology properties to vary
from one frame to the next. Use the GSD Python API to specify the initial
condition for a HOOMD-blue simulation or analyze trajectory output with a
script. Read a GSD trajectory with a visualization tool to explore the behavior
of the simulation.}

%description %_description

%package -n     python3-gsd
Summary:        %{summary}

%description -n python3-gsd %_description

%prep
%autosetup -p1 -n gsd-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files gsd
# Remove development source files
find %{buildroot}%{python3_sitearch}/gsd/ -name "*.c" -delete
find %{buildroot}%{python3_sitearch}/gsd/ -name "*.h" -delete
# Filter out these deleted files from pyproject_files
sed -i -E '\#(gsd/fl\.c|gsd/gsd\.c|gsd/gsd\.h)$#d' %{pyproject_files}

%check
%pyproject_check_import

# Remove local gsd directory to prevent pytest from importing the uncompiled local source files
rm -rf gsd
# reading little-endian files on big-endian is unsupported
# https://github.com/glotzerlab/gsd/issues/12
%pytest -v --pyargs gsd \
    --basetemp=$(mktemp -d -p /tmp) \
    -k "not test_gsd_v1_read and not test_gsd_v1_upgrade_read and not test_gsd_v1_write and not test_gsd_v1_upgrade_write"

%files -n python3-gsd -f %{pyproject_files}
%{_bindir}/gsd

%changelog
%autochangelog
