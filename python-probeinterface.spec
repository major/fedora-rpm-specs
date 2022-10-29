# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond_without doc_pdf

Name:           python-probeinterface
Version:        0.2.14
Release:        %autorelease
Summary:        Handles probe layout, geometry, and wiring to device

# SPDX
License:        MIT
URL:            https://github.com/SpikeInterface/probeinterface
# The GitHub tarball has documentation, examples, and tests; the PyPI one does
# not.
Source0:        %{url}/archive/%{version}/probeinterface-%{version}.tar.gz
# Probe definitions are normally downloaded at runtime. We can get tests and
# examples that rely on probe definitions to work in an offline environment by
# pre-populating the local cache. See also
# https://github.com/SpikeInterface/probeinterface/issues/70.
#
# This URL comes from probeinterface/library.py, where it is called public_url.
%global probe_url https://web.gin.g-node.org/spikeinterface/probeinterface_library/raw/master
Source1:        %{probe_url}/neuronexus/A1x32-Poly3-10mm-50-177/A1x32-Poly3-10mm-50-177.json
Source2:        %{probe_url}/cambridgeneurotech/ASSY-156-P-1/ASSY-156-P-1.json

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
%endif

%global common_description %{expand:
A Python package to handle the layout, geometry, and wiring of silicon probes
for extracellular electrophysiology experiments.

Goals

Make a lightweight package to handle:

  • probe contact geometry (both 2D and 3D layouts)
  • probe shape (contour of the probe, shape of channel contact, …)
  • probe wiring to device (the physical layout often doesn’t match the channel
    ordering)
  • combining several probes into a device with global geometry + global wiring
  • exporting probe geometry data into JSON files
  • loading existing probe geometry files (Neuronexus, imec, Cambridge
    Neurotech…) Started here

Bonus:

  • optional plotting (based on matplotlib)
  • load/save geometry using common formats (PRB, CSV, NWB, …)
  • handle SI length units correctly um/mm/…

Target users/project:

  • spikeinterface team: integrate this into spikeextractor for channel
    location
  • neo team: handle array_annotations for AnalogSignal
  • spikeforest team: use this package for plotting probe activity
  • phy team: integrate for probe display
  • spyking-circus team: handle probe with this package
  • kilosort team: handle probe with this package
  • tridesclous team: handle probe with this package
  • open ephys team: automatically generate channel map configuration files}

%description %{common_description}


%package -n     python3-probeinterface
Summary:        %{summary}

%description -n python3-probeinterface %{common_description}


%package        doc
Summary:        Documentation for probeinterface

%description    doc %{common_description}


%prep
%autosetup -n probeinterface-%{version} -p1

# Do not require an exact matplotlib version to build documentation:
sed -r -i 's/(matplotlib)==/\1>=/' pyproject.toml

# Pre-populate the probe definition cache
PROBE_CACHE="${HOME}/.config/probeinterface/library"
install -t "${PROBE_CACHE}/neuronexus" -p -m 0644 -D '%{SOURCE1}'
install -t "${PROBE_CACHE}/cambridgeneurotech" -p -m 0644 -D '%{SOURCE2}'


%generate_buildrequires
%pyproject_buildrequires -x test%{?with_doc_pdf:,docs}


%build
%pyproject_wheel

%if %{with doc_pdf}
PYTHONPATH="${PWD}" %make_build -C doc latex SPHINXOPTS='%{?_smp_mflags}'
%make_build -C doc/_build/latex LATEXMKOPTS='-quiet'
%endif


%install
%pyproject_install
%pyproject_save_files probeinterface


%check
# Skip tests that unconditionally download probe interface definitions and
# bypass the cache.
# https://github.com/SpikeInterface/probeinterface/issues/70.
k="${k-}${k+ and }not test_download_probeinterface_file"
k="${k-}${k+ and }not test_get_from_cache"

%pytest -k "${k-}"


%files -n python3-probeinterface -f %{pyproject_files}
# pyproject-rpm-macros handles the LICENSE file; verify with “rpm -qL -p …”
%doc README.md


%files doc
%license LICENSE
%doc examples
%if %{with doc_pdf}
%doc doc/_build/latex/probeinterface.pdf
%endif


%changelog
%autochangelog
