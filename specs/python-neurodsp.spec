%global pypi_name neurodsp

Name:           python-%{pypi_name}
Version:        2.3.0
Release:        %autorelease
Summary:        A tool for digital signal processing for neural time series

%global forgeurl https://github.com/neurodsp-tools/neurodsp
%global tag %{version}
%forgemeta

License:        Apache-2.0
URL:            https://neurodsp-tools.github.io/
Source:         %forgesource

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pytest}

%global _description %{expand:
NeuroDSP is package of tools to analyze and simulate neural 
time series, using digital signal processing.

Available modules in NeuroDSP include:

* filt : Filter data with bandpass, highpass, lowpass, or notch filters
* burst : Detect bursting oscillations in neural signals
* rhythm : Find and analyze rhythmic and recurrent patterns in time series
* spectral : Compute spectral domain features such as power spectra
* timefrequency : Estimate instantaneous measures of oscillatory activity
* sim : Simulate time series, including periodic and aperiodic signal
  components
* plts : Plotting functions

If you use this code in your project, please cite:

Cole, S., Donoghue, T., Gao, R., & Voytek, B. (2019).
NeuroDSP: A package for neural digital signal processing.
Journal of Open Source Software, 4(36), 1272.
https://doi.org/10.21105/joss.01272}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%prep
%forgeautosetup -p1

%generate_buildrequires
%pyproject_buildrequires requirements.txt

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l neurodsp

%check
# Deselected tests that require internet
%pytest -r fEs --deselect neurodsp/tests/utils/test_download.py

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc CITATION.cff README.rst paper/

%changelog
%autochangelog
