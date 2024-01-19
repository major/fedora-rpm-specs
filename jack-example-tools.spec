%global jack_tools \
    alsa_in \
    alsa_out \
    jack_alias \
    jack_bufsize \
    jack_connect \
    jack_disconnect \
    jack_evmon \
    jack_freewheel \
    jack_iodelay \
    jack_load \
    jack_load_test \
    jack_lsp \
    jack_midi_dump \
    jack_monitor_client \
    jack_netsource \
    jack_property \
    jack_samplerate \
    jack_transport \
    jack_tw \
    jack_unload \
    jack_wait

%global jack_tools_server %{nil}

%global jack_tools_inprocess \
    zalsa_in.so \
    zalsa_out.so

%global jack_examples \
    jack_control_client \
    jack_cpu_load \
    jack_rec \
    jack_impulse_grabber \
    jack_latent_client \
    jack_metro \
    jack_midiseq \
    jack_midisine \
    jack_midi_latency_test \
    jack_net_master \
    jack_net_slave \
    jack_showtime \
    jack_simdtests \
    jack_simple_client \
    jack_transport_client \
    jack_thru_client \
    jack_zombie

%global jack_examples_server \
    jack_server_control

%global jack_examples_inprocess \
    jack_inprocess.so \
    jack_internal_metro.so \
    jack_intime.so

Summary: Examples and tools for JACK
Name: jack-example-tools
Version: 4
Release: %autorelease
URL: https://github.com/jackaudio/%{name}
License: GPL-2.0-or-later
Source0: https://github.com/jackaudio/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# https://github.com/jackaudio/jack-example-tools/pull/82
Patch: 0001-Don-t-use-gethostbyname.patch
# https://github.com/jackaudio/jack-example-tools/pull/84
Patch: 0001-Add-LGPL-v2.1-license-text.patch
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: meson
# Don’t use pkgconfig(jack) because both
# pipewire-jack-audio-connection-kit-devel and jack-audio-connection-kit-devel
# provide it.
BuildRequires: jack-audio-connection-kit-devel >= 1.9.20
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(opus)
BuildRequires: pkgconfig(readline)
BuildRequires: pkgconfig(samplerate)
BuildRequires: pkgconfig(sndfile)
BuildRequires: zita-alsa-pcmi-devel
BuildRequires: zita-resampler-devel

%description
This package contains official examples and tools from the JACK project.

%package common
Summary: Common files for jack-example-tools
BuildArch: noarch

%description common
This package contains common files for the official examples and tools from the
JACK project.

%package -n jack-tools
Summary: Tools for JACK
Requires: %{name}-common = %{version}-%{release}

%description -n jack-tools
This package contains official tools from the JACK project.

%package -n jack-tools-server
Summary: Tools for the JACK audio server
# zalsa is GPLv3+ licensed
License: GPL-2.0-or-later AND GPL-3.0-or-later
Requires: %{name}-common = %{version}-%{release}
Requires: jack-audio-connection-kit%{?_isa}

%description -n jack-tools-server
This package contains tools to be used with the JACK audio server.

%package -n jack-examples
Summary: Examples for JACK
# jack_midi_latency_test is LGPLv2.1+ licensed
License: GPL-2.0-or-later AND LGPL-2.1-or-later
Requires: %{name}-common = %{version}-%{release}

%description -n jack-examples
This package contains official examples from the JACK project.

%package -n jack-examples-server
Summary: Examples for the JACK audio server
Requires: %{name}-common = %{version}-%{release}
Requires: jack-audio-connection-kit%{?_isa}

%description -n jack-examples-server
This package contains examples for integrating with the JACK audio server.

%prep
%autosetup -p1
ln LICENSE LICENSE.GPLv2
ln LICENSE.LGPL LICENSE.LGPLv2.1
ln tools/zalsa/LICENSE LICENSE.GPLv3

%build
%meson
%meson_build

%install
%meson_install

function build_files() {
    local pkg="$1"
    local dir="$2"
    local files="$3"
    local file

    touch "${pkg}-files.txt"

    for file in $files; do
        echo "${dir}/${file}"
        if [  "$dir" = "%{_bindir}" -a -e "%{buildroot}%{_mandir}/man1/${file}.1" ]; then
            echo "%{_mandir}/man1/${file}.1*"
        fi
    done >> "${pkg}-files.txt"
}

build_files jack-tools %{_bindir} "%{jack_tools}"
build_files jack-tools-server %{_bindir} "%{jack_tools_server}"
build_files jack-tools-server %{_libdir}/jack "%{jack_tools_inprocess}"
build_files jack-examples %{_bindir} "%{jack_examples}"
build_files jack-examples-server %{_bindir} "%{jack_examples_server}"
build_files jack-examples-server %{_libdir}/jack "%{jack_examples_inprocess}"

%check
%meson_test

%files common
%doc CHANGELOG.md README.md
%license LICENSE.GPLv2 LICENSE.GPLv3 LICENSE.LGPLv2.1

%files -n jack-tools -f jack-tools-files.txt
%files -n jack-tools-server -f jack-tools-server-files.txt
%files -n jack-examples -f jack-examples-files.txt
%files -n jack-examples-server -f jack-examples-server-files.txt

%changelog
%autochangelog
