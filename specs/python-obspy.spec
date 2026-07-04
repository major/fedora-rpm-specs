%global pypi_name obspy
%global common_description %{expand:
ObsPy is an open-source project providing a Python framework for processing
seismological data. It provides parsers for common file formats, clients to
access data centers and seismological signal processing routines which allow
the manipulation of seismological time series.}

Name:          python-%{pypi_name}
Version:       1.5.0
Release:       %autorelease
Summary:       A Python Toolbox for seismology/seismological observatories
License:       LGPL-3.0-only
# miniSEED record parsing segfaults on big-endian s390x in libmseed's
# ms_detect (persists with system libmseed 2.19.5, not a bundled-copy or
# strict-aliasing artifact).
ExcludeArch:   s390x
URL:           https://github.com/obspy/obspy
VCS:           git:%{url}.git
Source:        %{pypi_source %pypi_name}
# Bacported from upstream's master branch
Patch:         python-obspy-0001-fix-Replace-unused-capture-groups-in-taup-seismic_ph.patch
# Fedora-specific. Builds against system libmseed.
Patch:         python-obspy-0002-Build-against-a-system-wide-libmseed.patch
BuildRequires: libmseed-devel
#BuildRequires: python3-cartopy
BuildRequires: python3-pytest
BuildRequires: gcc
BuildSystem:   pyproject
BuildOption(install): -l %{pypi_name}

%description %{common_description}

%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name} %{common_description}

%check
%pyproject_check_import -e 'obspy.lib.*'
# Run from the install dir, not %{_builddir}: pytest anchors rootdir/conftest
# discovery on cwd, so from the source checkout it loads the in-tree obspy/
# (whose obspy/lib/ has no compiled .so — they're built into sitearch) and
# dies in conftest at _load_cdll("signal"). cd'ing here makes the installed
# obspy the only one on the path. --pyargs alone is not enough.
cd %{buildroot}%{python3_sitearch}
%pytest --pyargs obspy -p no:cacheprovider -o 'addopts=--tb=native --continue-on-collection-errors -ra'

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%{_bindir}/obspy-*

%changelog
%autochangelog
