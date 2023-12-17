Name:           wavbreaker
Version:        0.11
Release:        %autorelease
Summary:        GUI tool to losslessly split WAV, MP2 and MP3 files into multiple parts

# The entire source is GPL-2.0-or-later, except the following build-system
# files, which do not contribute to the licenses of the binary RPMs. We do not
# enumerate their exact licenses except to confirm that all of the licenses
# mentioned in them are allowed for code in Fedora.
License:        GPL-2.0-or-later
URL:            https://wavbreaker.sourceforge.io
Source:         https://github.com/thp/wavbreaker/archive/wavbreaker-%{version}/wavbreaker-wavbreaker-%{version}.tar.gz

Patch:          wavbreaker-0.10-format-security.patch

BuildRequires:  autoconf
BuildRequires:  automake

BuildRequires:  make
BuildRequires:  gcc

BuildRequires:  alsa-lib-devel
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libpulse-simple)
BuildRequires:  pkgconfig(libxml-2.0)

BuildRequires:  desktop-file-utils
BuildRequires:  gettext

%description
This application’s purpose in life is to take a WAV file and break it up into
multiple WAV files. It makes a clean break at the correct position to burn the
files to an Audio CD without any dead air between the tracks.

wavbreaker also supports breaking up MP2 and MP3 files without re-encoding
meaning it’s fast and there is no generational loss. Decoding (using mpg123) is
only done for playback and waveform display.

The GUI displays a waveform summary of the entire file at the top. The middle
portion displays a zoomed-in view that allows you to select where to start
playing and where it will make the break. The bottom portion contains a list of
track breaks. You may change file names and uncheck parts that you do not want
to have written out to disk when saving.

There is also a command line tool wavmerge to merge WAV files together. If you
download a show and don’t like how it was tracked, you can merge them together
with wavmerge and then break them back up with wavbreaker. The wavmerge tool
will only work on files that have the same format (for example, 44.100 Hz
sample rate, 16-bit sample size, etc.).


%prep
%autosetup -p1 -n wavbreaker-wavbreaker-%{version}


%build
# Upstream has an autogen.sh script, but it is overcomplicated and doesn’t add
# anything compared to autoreconf.
autoreconf --force --install --verbose
%configure
%make_build


%install
%make_install
%find_lang wavbreaker


%check
desktop-file-validate \
  %{buildroot}%{_datadir}/applications/wavbreaker.desktop


%files -f wavbreaker.lang
%license COPYING

%doc AUTHORS
%doc CONTRIBUTORS
%doc ChangeLog
%doc NEWS
%doc README
%doc README.PulseAudio

%{_bindir}/wavbreaker
%{_bindir}/wavinfo
%{_bindir}/wavmerge

%{_datadir}/applications/wavbreaker.desktop
%{_datadir}/icons/hicolor/*/apps/wavbreaker.png
%{_datadir}/icons/hicolor/scalable/apps/wavbreaker.svg
%{_datadir}/pixmaps/wavbreaker.png

%{_mandir}/man1/wavbreaker.1*
%{_mandir}/man1/wavinfo.1*
%{_mandir}/man1/wavmerge.1*


%changelog
%autochangelog
