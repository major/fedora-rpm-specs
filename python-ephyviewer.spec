%bcond_without tests

Name:           python-ephyviewer
Version:        1.5.1
Release:        %autorelease
Summary:        Simple viewers for ephys signals, events, video and more

License:        MIT
URL:            https://github.com/NeuralEnsemble/ephyviewer
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest


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
# needs Xvfb
BuildRequires:  xorg-x11-server-Xvfb

%description -n python3-ephyviewer %_description


%prep
%autosetup -n ephyviewer-%{version}

# spikeinterface and av optional and not yet packaged
# https://pagure.io/neuro-sig/NeuroFedora/issue/473
# av: bindings for ffmpeg so we'll need to see if it can be included in Fedora
# remove pytest-cov
sed -i -e '/spikeinterface/ d' -e '/av/ d' -e '/pytest-cov/ d' requirements-tests.txt


%generate_buildrequires
%pyproject_buildrequires -r -x tests


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files ephyviewer

%check
%if %{with tests}

# some tests segfault with xvfb, so we disable these
# other tests that require unpackaged extra modules or download data
xvfb-run -a -s "-screen 0 1920x1200x24 -ac +extension GLX" pytest-3 \
    -k "not test_spiketrainviewer and not test_timefreqviewer and not test_traceviewer and not test_VideoMultiFileSource and not test_spikeinterface_sources and not test_spikeinterface_viewer and not test_videoviewer and not test_neo_rawio_sources and not test_mainviewer2 and not test_neoviewer"
%endif

%files -n python3-ephyviewer -f %{pyproject_files}
%doc README.*
%{_bindir}/ephyviewer


%changelog
%autochangelog
