%global pypi_name obspy
%global common_description %{expand:
ObsPy is an open-source project providing a Python framework for processing
seismological data. It provides parsers for common file formats, clients to
access data centers and seismological signal processing routines which allow
the manipulation of seismological time series.}

Name:          python-%{pypi_name}
Version:       1.5.1
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
# Fedora-specific. Builds against system libmseed.
Patch:         python-obspy-0001-Build-against-a-system-wide-libmseed.patch
BuildRequires: gcc
BuildRequires: libmseed-devel
%ifnarch %{ix86}
BuildRequires: natural-earth-map-data-110m
BuildRequires: natural-earth-map-data-50m
BuildRequires: python3-cartopy
%endif
BuildRequires: python3-pytest
BuildSystem:   pyproject
BuildOption(install): -l %{pypi_name}

%description %{common_description}

%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name} %{common_description}

%check
%pyproject_check_import -e 'obspy.lib.*'
%ifarch %{ix86}
# python3-cartopy is ExcludeArch: %%{ix86}, so the map-plotting tests cannot run
# here. Every test in these two classes needs cartopy, as does this one.
deselect="--deselect obspy/core/tests/test_inventory.py::TestInventoryCartopy"
deselect="$deselect --deselect obspy/core/tests/test_network.py::TestNetworkCartopy"
deselect="$deselect --deselect obspy/core/tests/test_event.py::TestEvent::test_plot_farfield_without_quiver_with_maps"
%endif
# Run from the install dir, not %{_builddir}: pytest anchors rootdir/conftest
# discovery on cwd, so from the source checkout it loads the in-tree obspy/
# (whose obspy/lib/ has no compiled .so — they're built into sitearch) and
# dies in conftest at _load_cdll("signal"). cd'ing here makes the installed
# obspy the only one on the path. --pyargs alone is not enough.
cd %{buildroot}%{python3_sitearch}
%pytest --pyargs obspy -p no:cacheprovider -o 'addopts=--tb=native --continue-on-collection-errors -ra' ${deselect-}


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%{_bindir}/obspy-*

%changelog
%autochangelog
