Name:       python-neatdend
Version:    0.9.2
Release:    %autorelease
Summary:    NEAT (NEural Analysis Toolkit)

License:    GPLv3
URL:        https://github.com/unibe-cns/NEAT
Source0:    %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# Patches: https://github.com/sanjayankur31/NEAT/tree/fedora-v0.9.2
# Support all arches for Neuron libs
# issue filed: https://github.com/unibe-cns/NEAT/issues/142
Patch0:     0001-feat-support-all-arches.patch
Patch1:	    https://github.com/unibe-cns/NEAT/commit/504b39822b9913e5a8c6aff65df840cc2e31167d.patch	    
# Fix compatibility with recent Matplotlib
Patch2:     https://github.com/unibe-cns/NEAT/commit/8eb1f4be85da0c8fdbcbac627c5198a67e29b22c.patch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  gcc gcc-c++
BuildRequires:  git-core
BuildRequires:  python3-neuron
BuildRequires:  neuron-devel

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

%global _description %{expand:
NEAT is a python library for the study,
simulation and simplification of morphological neuron models.}

%description %_description

%package -n python3-neatdend
Summary:        %{summary}

%description -n python3-neatdend %_description


%prep
%autosetup -n NEAT-%{version} -S git

sed -i 's/^numpy~=1.20.2/numpy>=1.20.2/' requirements/requirements.txt
sed -i 's/^matplotlib~=3.4.1/matplotlib>=3.4.1/' requirements/requirements.txt
sed -i 's/^pytest~=5.3.2/pytest>=5.3.2/' requirements/requirements.txt
sed -i 's/^scikit_learn~=0.24.2/scikit_learn>=0.24.2/' requirements/requirements.txt
sed -i 's/^scipy~=1.6.3/scipy>=1.6.3/' requirements/requirements.txt
sed -i 's/^sympy~=1.7.1/sympy>=1.7.1/' requirements/requirements.txt
sed -i 's/^cython~=0.29.4/cython>=3.0.0/' requirements/requirements.txt

%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l neat

%check
# a few tests fail on i686.
# Upstream report: https://github.com/unibe-cns/NEAT/issues/142#issuecomment-1107874903
%ifnarch %{ix86}
# we need to run these in a different directory to ensure that the module isn't
# imported from the source directory
mkdir testdir && pushd testdir
# Python path must be defined so that compilechannels uses the installed module
PYTHONPATH=$RPM_BUILD_ROOT/%{python3_sitelib}:$RPM_BUILD_ROOT/%{python3_sitearch} $RPM_BUILD_ROOT/%{_bindir}/compilechannels default
%pytest ../
popd
%endif

# remove files generated for the tests
rm -rf find $RPM_BUILD_ROOT/%{python3_sitearch}/neat/tools/simtools/neuron/mech/*.mod
rm -rf find $RPM_BUILD_ROOT/%{python3_sitearch}/neat/tools/simtools/neuron/%{_arch}

%files -n python3-neatdend -f %{pyproject_files}
%doc README.rst CODE_OF_CONDUCT.rst CONTRIBUTING.rst CONTRIBUTORS.rst
%{_bindir}/compilechannels

%changelog
%autochangelog
