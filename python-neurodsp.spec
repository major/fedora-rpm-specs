%bcond_without tests

%global pypi_name neurodsp

%global _description %{expand:
NeuroDSP is package of tools to analyze and simulate neural 
time series, using digital signal processing.

Available modules in NeuroDSP include:

* filt : Filter data with bandpass, highpass, lowpass, or
notch filters
* burst : Detect bursting oscillations in neural signals
* rhythm : Find and analyze rhythmic and recurrent patterns
in time series
* spectral : Compute spectral domain features such as power
spectra
* timefrequency : Estimate instantaneous measures of
oscillatory activity
* sim : Simulate time series, including periodic and
aperiodic signal components
* plts : Plotting functions

If you use this code in your project, please cite:

Cole, S., Donoghue, T., Gao, R., & Voytek, B. (2019).
NeuroDSP: A package for neural digital signal processing.
Journal of Open Source Software, 4(36), 1272.
https://doi.org/10.21105/joss.01272}

Name:           python-%{pypi_name}
Version:        2.1.0
Release:        5%{?dist}
Summary:        A tool for digital signal processing for neural time series

License:        ASL 2.0
URL:            https://neurodsp-tools.github.io/
Source0:        https://github.com/neurodsp-tools/%{pypi_name}/archive/%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist numpy}
BuildRequires:  %{py3_dist scipy}
BuildRequires:  %{py3_dist matplotlib}

%if %{with tests}
BuildRequires:  python3-pytest
%endif

%py_provides python3-%{pypi_name}

%description -n python3-%{pypi_name} %_description

%prep
# No keyring/signature from the upstream to verify the source
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%build
%py3_build
# cannot build the docs, as it downloads additional datasets (through mne).

%install
%py3_install

%check
%if %{with tests}
# Deselected tests that require internet
%pytest --deselect neurodsp/tests/utils/test_download.py
%endif

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst paper/*
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{pypi_name}

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 2.1.0-4
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 03 2021 Aniket Pradhan <major AT fedoraproject DOT org> - 2.1.0-1
- Update to v2.1.0
- Remove patch as it is no longer required
- Use pytest macro
- Remove automatic dependency generator
- Use py_provides macro

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.0.0-8
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Aniket Pradhan <major AT fedoraproject DOT org> - 2.0.0-5
- Added setuptools to BuildRequires

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-4
- Rebuilt for Python 3.9

* Sat Feb 08 2020 Aniket Pradhan <major AT fedoraproject DOT org> - 2.0.0-3
- Removed gnupg from BuildRequires
- Added a patch to fix some test failures

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 11 2019 Aniket Pradhan <major AT fedoraproject DOT org> - 2.0.0-1
- Initial build
