Name:           python-pyscipopt
Version:        5.5.0
Release:        %autorelease
Summary:        Python interface and modeling environment for SCIP

License:        MIT
URL:            https://github.com/scipopt/PySCIPOpt
# Two Python sources in the tutorial are licensed WTFNMFPL. Until legal review
# is completed, we must filter these from the source archive.
#
# https://gitlab.com/fedora/legal/fedora-license-data/-/issues/663
#
# The filtered source archive is produced using Source1:
#   ./get_source %%{version}
# Source:         %%{url}/archive/v%%{version}/PySCIPOpt-%%{version}.tar.gz
Source0:        PySCIPOpt-%{version}-filtered.tar.gz
Source1:        get_source

# Remove bogus execute permission and shebang line from sudoku example
# https://github.com/scipopt/PySCIPOpt/pull/1008
Patch:          %{url}/pull/1008.patch

BuildSystem:            pyproject
BuildOption(install):   -l pyscipopt

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
# Furthermore, dependency libscip is ExcludeArch: %%{ix86}.
ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  libscip-devel

BuildRequires:  %{py3_dist pytest}

%global common_description %{expand:
This project provides an interface from Python to the SCIP Optimization Suite.}

%description %{common_description}


%package -n python3-pyscipopt
Summary:        %{summary}

%description -n python3-pyscipopt %{common_description}


%package examples
Summary:        Examples for PySCIPOpt

BuildArch:      noarch

%description examples
%{summary}.


%prep -a
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_beware_of_rpath
sed -r -i 's/^([[:blank:]]*)(.*-Wl,-rpath)/\1# \2/' setup.py


%build -p
export CFLAGS="${CFLAGS} -I/usr/include/scip"


%check -a
%pytest -v


%files -n python3-pyscipopt -f %{pyproject_files}
%doc CHANGELOG.md
%doc CITATION.bib
%doc README.md


%files examples
%license LICENSE
%doc examples/*


%changelog
%autochangelog
