# Require mpi for tests, and seem to hang in Mock, so disabled by default
%bcond_with tests

%global _description %{expand: \
SpyKING CIRCUS is a python code to allow fast spike sorting on multi channel
recordings. A publication on the algorithm can be found at
https://elifesciences.org/articles/34518.

It has been tested on datasets coming from in vitro retina with 252 electrodes
MEA, from in vivo hippocampus with tetrodes, in vivo and in vitro cortex data
with 30 and up to 4225 channels, with good results. Synthetic tests on these
data show that cells firing at more than 0.5Hz can be detected, and their
spikes recovered with error rates at around 1%, even resolving overlapping
spikes and synchronous firing. It seems to be compatible with optogenetic
stimulation, based on experimental data obtained in the retina.}


%global forgeurl  https://github.com/spyking-circus/spyking-circus

Name:           python-spyking-circus
Version:        1.1.0
Release:        %autorelease
Summary:        Fast and scalable spike sorting of large-scale extracellular recordings

%global tag  %{version}
%forgemeta

# spdx
License:        CECILL-2.1
URL:            %forgeurl
Source0:        %forgesource

# We install the probe files to datadir
Patch0:         set-probe-datadir.patch
BuildArch:      noarch

%description %_description


%package -n python3-spyking-circus
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  /usr/bin/patch
%if %{with tests}
BuildRequires:  mpich-devel
BuildRequires:  python3-mpi4py-mpich
BuildRequires:  openmpi-devel
BuildRequires:  python3-mpi4py-openmpi
BuildRequires:  python3-pytest
%endif

%description -n python3-spyking-circus %_description


%package -n python3-spyking-circus-common
Summary:        Common files for %{name}

%description -n python3-spyking-circus-common %_description

# MPICH meta package
%package -n python3-spyking-circus-mpich
Summary:        Meta package for %{name}
Requires:       python3-mpi4py-mpich
Requires:       python3-spyking-circus%{?_isa} = %{version}-%{release}

%description -n python3-spyking-circus-mpich %_description

# OpenMPI meta package
%package -n python3-spyking-circus-openmpi
Summary:        Meta package for %{name}
Requires:       python3-mpi4py-openmpi
Requires:       python3-spyking-circus%{?_isa} = %{version}-%{release}

%description -n python3-spyking-circus-openmpi %_description

%prep
%forgeautosetup -S patch

# Set the path to datadir
sed -i "s|SED_ME|%{_datadir}/spyking-circus/|" setup.py

# remove mpi4py from requires, we add it manually
sed -i "s/'mpi4py', //" setup.py

# Remove env
find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

# Remove nose from tests: we use pytest
sed -i 's/nose,//' tests/__init__.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
# remove duplicate installed files
mkdir -m 0755 -p $RPM_BUILD_ROOT/%{_datadir}/spyking-circus/
mv $RPM_BUILD_ROOT/%{python3_sitelib}/usr/share/spyking-circus/* $RPM_BUILD_ROOT/%{_datadir}/spyking-circus/
rm -rf $RPM_BUILD_ROOT/%{python3_sitelib}/usr/

%pyproject_save_files -l circus

%check
%if %{with tests}
%{_mpich_load}
%{pytest} tests/
%{_mpich_unload}

%{_openmpi_load}
%{pytest} tests/
%{_openmpi_unload}
%endif

%files -n python3-spyking-circus -f %{pyproject_files}
%doc README.rst
%{_bindir}/circus-artefacts
%{_bindir}/circus-folders
%{_bindir}/circus-gui-matlab
%{_bindir}/circus-gui-python
%{_bindir}/circus-multi
%{_bindir}/spyking-circus
%{_bindir}/spyking-circus-launcher
%{_bindir}/spyking-circus-subtask
%{_datadir}/spyking-circus

%changelog
%autochangelog
