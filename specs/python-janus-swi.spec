%global giturl  https://github.com/SWI-Prolog/packages-swipy

Name:           python-janus-swi
Version:        1.5.2
Release:        %autorelease
Summary:        Bidirectional interface between SWI Prolog and Python

License:        BSD-2-Clause
URL:            https://www.swi-prolog.org/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/janus-%{version}.tar.gz

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pytest}
BuildRequires:  swi-prolog-core-packages

%global common_desc %{expand:
This package implements a ready-to-use bidirectional interface between
SWI Prolog and Python.}

%description
%common_desc

%package -n python3-janus-swi
Summary:        Bidirectional interface between SWI Prolog and Python
Requires:       swi-prolog-core-packages

%description -n python3-janus-swi
%common_desc

%prep
%autosetup -n packages-swipy-janus-%{version}

%conf
# Avoid unwanted rpaths
sed -i 's|-rpath={props\["PLLIBDIR"\]},||' setup.py

%generate_buildrequires
%pyproject_buildrequires

%build
# Do not pass -pthread to the compiler or linker
export LDSHARED="gcc -shared"

%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L janus_swi

%check
%pytest

%files -n python3-janus-swi -f %{pyproject_files}
%doc README.md
%exclude %{python3_sitearch}/janus_swi/*.c

%changelog
%autochangelog
