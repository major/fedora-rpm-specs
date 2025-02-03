%global pypi_name nipype

Name:           python-%{pypi_name}
Version:        1.9.2
Release:        %{autorelease}
Summary:        Neuroimaging in Python: Pipelines and Interfaces

%global forgeurl https://github.com/nipy/nipype
%global tag %{version}
%forgemeta

License:        Apache-2.0
URL:            %forgeurl
Source:         %forgesource

BuildArch:      noarch
BuildRequires:  python3-devel
# Test requirements listed in `nipype/info.py` under `TEST-REQUIRES`
# together with linters, which we don't want.
BuildRequires:  python3dist(pandas)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-env)
BuildRequires:  python3dist(pytest-timeout)
BuildRequires:  python3dist(pytest-xvfb)

%global _description %{expand:
Current neuroimaging software offer users an incredible opportunity to
analyze data using a variety of different algorithms. However, this has
resulted in a heterogeneous collection of specialized applications
without transparent interoperability or a uniform operating interface.

Nipype, an open-source, community-developed initiative under the
umbrella of NiPy, is a Python project that provides a uniform interface
to existing neuroimaging software and facilitates interaction between
these packages within a single workflow. Nipype provides an environment
that encourages interactive exploration of algorithms from different
packages (e.g., AFNI, ANTS, BRAINS, BrainSuite, Camino, FreeSurfer,
FSL, MNE, MRtrix, MNE, Nipy, Slicer, SPM), eases the design of
workflows within and between packages, and reduces the learning curve
necessary to use different packages. Nipype is creating a collaborative
platform for neuroimaging software development in a high-level language
and addressing limitations of existing pipeline systems.

Nipype allows you to:

- easily interact with tools from different software packages
- combine processing steps from different software packages
- develop new workflows faster by reusing common steps from old ones
- process data faster by running it in parallel on many cores/machines
- make your research easily reproducible
- share your processing workflows with the community}

%description %_description


%package -n python3-%{pypi_name}
Summary:        %{summary}
Provides:       nipypecli = %{version}-%{release}
# For converting from DICOM to NIfTI
Recommends:     dcm2niix

%description -n python3-%{pypi_name} %_description


%pyproject_extras_subpkg -n python3-%{pypi_name} data duecredit nipy pybids ssh


%prep
%forgeautosetup -p1

# Exclude data files (used for testing) from installation
sed -r -i 's/package_data/exclude_package_data/' setup.py

# Remove shebangs
find nipype/ -name \*.py -exec sed -i '/env python/d' '{}' \;


%generate_buildrequires
%pyproject_buildrequires -x data,duecredit,nipy,pybids,ssh,xvfbwrapper


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}


%check
# With `-c /dev/null` we circumvent `pyproject.toml`, which has settings
# for running doctests and coverage.
# Report which tests are skipped and why (-rs).
%pytest -v -rs -c /dev/null


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst THANKS.rst
%{_bindir}/nipypecli


%changelog
%autochangelog
