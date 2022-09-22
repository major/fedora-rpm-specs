# Require deprecated nose so disabled
# we test in mock though and all tes pass
# Upstream issue filed:
# https://github.com/mariomulansky/PySpike/issues/48
%bcond_with tests

%global _description %{expand:
PySpike is a Python library for the numerical analysis of spike train
similarity. Its core functionality is the implementation of the ISI-distance
[1] and SPIKE-distance [2] as well as SPIKE-Synchronization [3]. It provides
functions to compute multivariate profiles, distance matrices, as well as
averaging and general spike train processing. All computation intensive parts
are implemented in C via Cython to reach a competitive performance (factor
100-200 over plain Python).

PySpike provides the same fundamental functionality as the SPIKY framework for
Matlab, which additionally contains spike-train generators, more spike train
distance measures and many visualization routines.

If you use PySpike in your research, please cite our SoftwareX publication on
PySpike:

Mario Mulansky, Thomas Kreuz, PySpike - A Python library for analyzing spike
train synchrony, SoftwareX, (2016), ISSN 2352-7110,
http://dx.doi.org/10.1016/j.softx.2016.07.006.

Additionally, depending on the used methods: ISI-distance [1], SPIKE-distance
[2] or SPIKE-Synchronization [3], please cite one or more of the following
publications:

[1] Kreuz T, Haas JS, Morelli A, Abarbanel HDI, Politi A, Measuring spike train
synchrony. J Neurosci Methods 165, 151 (2007)

[2] Kreuz T, Chicharro D, Houghton C, Andrzejak RG, Mormann F, Monitoring spike
train synchrony. J Neurophysiol 109, 1457 (2013)

[3] Kreuz T, Mulansky M and Bozanic N, SPIKY: A graphical user interface for
monitoring spike train synchrony, J Neurophysiol, JNeurophysiol 113, 3432
(2015)

Documentation is available at http://mariomulansky.github.io/PySpike/
}

Name:           python-pyspike
Version:        0.7.0
Release:        %autorelease
Summary:        Library for the numerical analysis of spike train similarity

License:        BSD
URL:            https://github.com/mariomulansky/PySpike/
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  python3-devel

%description %_description

%package -n python3-pyspike
Summary:        %{summary}
BuildRequires:  python3-Cython
BuildRequires:  gcc

%if %{with tests}
BuildRequires:  python3-nose
BuildRequires:  %{py3_dist scipy}
%endif

%description -n python3-pyspike %_description

%prep
%autosetup -n PySpike-%{version}

# Comment out to remove /usr/bin/env shebangs
# Can use something similar to correct/remove /usr/bin/python shebangs also
# find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

# Tests require these to be built in-place
# https://github.com/mariomulansky/PySpike/blob/master/.travis.yml
%if %{with tests}
%{set_build_flags}
%{python3} %{py_setup} %{?py_setup_args} build_ext --inplace
%endif

%install
%pyproject_install
%pyproject_save_files pyspike

%check
%if %{with tests}
# https://github.com/mariomulansky/PySpike/blob/master/.travis.yml
nosetests
nosetests test/numeric
%endif

%files -n python3-pyspike -f %{pyproject_files}
%license License.txt

%changelog
%autochangelog
