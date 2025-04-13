%bcond_with pylirc
%bcond_without pulse

Summary: Simple Video for Linux radio card programs
Name:    fmtools
Version: 2.0.8
Release: %autorelease
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     http://benpfaff.org/fmtools

Source0: http://benpfaff.org/fmtools/%{name}-%{version}.tar.gz
Source1: fmcontrol.tar.gz
Source2: http://benpfaff.org/fmtools/tkradio
Source3: http://benpfaff.org/fmtools/tkradio-mute
Source4: fmtools.desktop
Source5: radio.png
Source8: radio.gif
Source6: tkradio.py
Source7: fmlircrc
Patch0: fmcontrol-py3.patch
BuildRequires: autoconf automake
BuildRequires: gcc
BuildRequires: python3-devel

%description
This is a pair of hopefully useful control programs for Video for Linux
(v4l2) radio card drivers.  The focus is on control, so you may find these
programs a bit unfriendly.  Users are encouraged to investigate the source
and create wrappers or new programs based on this design.

fm      - a simple tuner
fmscan  - a simple band scanner

%package tkradio
Summary:       Python/Tk wrapper for fmtools
BuildRequires: desktop-file-utils
BuildRequires: make
Requires:      %{name} = %{version}
Requires:      python3
%{?with_pylirc:Requires: python3-lirc}
Requires:      vorbis-tools, python3-tkinter, alsa-utils
%if %{with pulse}
Requires:      pulseaudio-utils
BuildArch:     noarch
%endif

%description tkradio
This package provides a GUI for %{name}, with lirc support.
The stations are read from the same files used by fmcontrol,
and the lirc configuration file is in $HOME/.fmlircrc

The script fmcontrol.py saves one from remembering frequencies
and volumes when using the "fm" program from %{name}.
All that it does is to tune into a station specified by name, at the
frequency and volume specified in $HOME/.fmrc or $HOME/.radiostations,
or the volume given on the command line.

%prep
%setup -q -a1
%patch -P0 -p1 -b .py3

%build
autoreconf -vif
%configure
%make_build

%install
%make_install
install -pm 0755 %{SOURCE2} %{buildroot}%{_bindir}/tkradio.tcl
install -pm 0755 %{SOURCE3} %{buildroot}%{_bindir}/tkradio-mute.tcl
install -pm 0755 %{SOURCE6} %{buildroot}%{_bindir}/tkradio.py
install -pm 0755 fmcontrol/fmcontrol %{buildroot}%{_bindir}/fmcontrol.py
install -pm 0644 fmcontrol/README README.fmcontrol

# menu entry
desktop-file-install                                    \
        --vendor ""                                     \
        --dir %{buildroot}%{_datadir}/applications      \
        %{SOURCE4}

install -Dpm 0644 %{SOURCE5} %{buildroot}%{_datadir}/pixmaps/radio.png
install -Dpm 0644 %{SOURCE7} %{buildroot}%{_datadir}/%{name}/fmlircrc
install -Dpm 0644 %{SOURCE8} %{buildroot}%{_datadir}/%{name}/radio.gif

%files 
%doc README
%license COPYING
%{_bindir}/fm
%{_bindir}/fmscan
%{_mandir}/man1/fm*.gz

%files tkradio
%doc README.fmcontrol fmcontrol/dot.*
%{_bindir}/tkradio*
%{_bindir}/fmcontrol.py
%{_datadir}/applications/fmtools.desktop
%{_datadir}/pixmaps/radio.png
%{_datadir}/%{name}/fmlircrc
%{_datadir}/%{name}/radio.gif

%changelog
%autochangelog
