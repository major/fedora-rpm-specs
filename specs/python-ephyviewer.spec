%global forgeurl https://github.com/NeuralEnsemble/ephyviewer

%bcond tests 1

Name:           python-ephyviewer
Version:        1.7.0
Release:        %autorelease
Summary:        Simple viewers for ephys signals, events, video and more
%global tag %{version}
%forgemeta
# SPDX
License:        MIT
URL:            https://ephyviewer.readthedocs.io/
Source:         %forgesource
# Fix compatibility with matplotlib >= 3.9
# https://github.com/NeuralEnsemble/ephyviewer/pull/184
Patch:          %{forgeurl}/pull/185.patch

# Fix for neo 0.13.4
Patch:          %{forgeurl}/pull/188.patch

# python-pyedflib does not support s390x
# https://src.fedoraproject.org/rpms/python-pyedflib/blob/rawhide/f/python-pyedflib.spec
#
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    s390x %{ix86}
BuildArch:      noarch
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  %{py3_dist pytest-xvfb}
%endif

%global _description %{expand:
ephyviewer is a Python library based on pyqtgraph for building custom viewers
for electrophysiological signals, video, events, epochs, spike trains, data
tables, and time-frequency representations of signals. It also provides an
epoch encoder for creating annotations.

Documentation is available at
https://ephyviewer.readthedocs.io/}

%description %_description


%package -n python3-ephyviewer
Summary:        %{summary}

%description -n python3-ephyviewer %_description


%prep
%forgeautosetup -p1

# spikeinterface and av optional and not yet packaged
# https://pagure.io/neuro-sig/NeuroFedora/issue/473
# av: bindings for ffmpeg so we'll need to see if it can be included in Fedora
# remove pytest-cov and coveralls
sed -i \
  -e '/spikeinterface/ d' \
  -e '/av/ d' \
  -e '/pytest-cov/ d' \
  -e '/coveralls/ d' \
  requirements-tests.txt


%generate_buildrequires
%pyproject_buildrequires -x tests


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l ephyviewer


%check
%if %{with tests}
# These require network access (at least DNS).
k="${k-}${k+ and }not test_neo_rawio_sources"
k="${k-}${k+ and }not test_neoviewer"
# These require python3dist(av), not packaged.
k="${k-}${k+ and }not test_VideoMultiFileSource"
k="${k-}${k+ and }not test_mainviewer2"
k="${k-}${k+ and }not test_videoviewer"
# These require python3dist(spikeinterface), not packaged.
k="${k-}${k+ and }not test_spikeinterface_sources"
k="${k-}${k+ and }not test_spikeinterface_viewer"
%pytest -r fEs ${k+-k "${k-}"}
%endif


%files -n python3-ephyviewer -f %{pyproject_files}
%doc README.*
%{_bindir}/ephyviewer


%changelog
%autochangelog
