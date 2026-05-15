Name:           python-pyspike
Version:        0.9.0
Release:        %autorelease
Summary:        Library for the numerical analysis of spike train similarity

License:        BSD-2-Clause
URL:            https://github.com/mariomulansky/PySpike
Source:         %{url}/archive/v%{version}/PySpike-%{version}.tar.gz

BuildRequires:  gcc

# Test dependencies are documented in Readme.rst:
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist scipy}

%global _description %{expand:
PySpike is a Python library for the numerical analysis of spike train
similarity. Its core functionality is the implementation of the ISI-distance[1]
and SPIKE-distance[2], SPIKE-Synchronization [3], as well as their adaptive
generalizations[4]. It provides functions to compute multivariate profiles,
distance matrices, as well as averaging and general spike train processing. All
computation intensive parts are implemented in C via Cython to reach a
competitive performance (factor 100-200 over plain Python).

PySpike provides the same fundamental functionality as the SPIKY framework for
Matlab, which additionally contains spike-train generators, more spike train
distance measures and many visualization routines.

If you use PySpike in your research, please cite our SoftwareX publication on
PySpike:

Mario Mulansky, Thomas Kreuz, *PySpike - A Python library for analyzing spike
train synchrony*, Software X 5, 183 (2016)

Additionally, depending on the used methods: ISI-distance [1], SPIKE-distance
[2], SPIKE-Synchronization [3], or their adaptive generalizations [4], please
cite one or more of the following publications:

[1] Kreuz T, Haas JS, Morelli A, Abarbanel HDI, Politi A, Measuring spike train
synchrony. J Neurosci Methods 165, 151 (2007)

[2] Kreuz T, Chicharro D, Houghton C, Andrzejak RG, Mormann F, Monitoring spike
train synchrony. J Neurophysiol 109, 1457 (2013)

[3] Kreuz T, Mulansky M and Bozanic N, *SPIKY: A graphical user interface for
monitoring spike train synchrony*, J Neurophysiol 113, 3432 (2015)

[4] Satuvuori E, Mulansky M, Bozanic N, Malvestio I, Zeldenrust F, Lenk K, and
Kreuz T, Measures of spike train synchrony for data with multiple time-scales,
J Neurosci Methods 287, 25 (2017)

Documentation is available at http://mariomulansky.github.io/PySpike/}

%description %_description

%package -n python3-pyspike
Summary:        %{summary}

%description -n python3-pyspike %_description

%prep
%autosetup -n PySpike-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l pyspike

%check
%pyproject_check_import
%pytest -v

%files -n python3-pyspike -f %{pyproject_files}
%doc Readme.rst
%doc Changelog
%doc Contributors.txt
%doc examples/

%changelog
%autochangelog
