Name:           wavbreaker
Version:        0.16
Release:        %autorelease
Summary:        GUI tool to losslessly split WAV, MP2 and MP3 files into multiple parts

%global app_id net.sourceforge.wavbreaker

# The entire source is GPL-2.0-or-later, except for the AppData XML file, which
# is FSFAP.
License:        GPL-2.0-or-later AND FSFAP
URL:            https://wavbreaker.sourceforge.io
Source:         https://github.com/thp/wavbreaker/archive/%{version}/wavbreaker-%{version}.tar.gz

# Drop AppData ‘content_rating’ to fix #26
# https://github.com/thp/wavbreaker/pull/27
#
# Fixes:
#
# AppData XML file does not pass appstream CLI validation
# https://github.com/thp/wavbreaker/issues/26
Patch:          https://github.com/thp/wavbreaker/pull/27.patch

BuildRequires:  gcc
BuildRequires:  meson

BuildRequires:  pkgconfig(ao)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
# Optional; provides MP2/MP3 support.
BuildRequires:  pkgconfig(libmpg123)
# Optional; provides Ogg Vorbis support.
BuildRequires:  pkgconfig(vorbisfile)

BuildRequires:  desktop-file-utils
BuildRequires:  gettext

# Still required by guidelines for now
# (https://pagure.io/packaging-committee/issue/1053):
BuildRequires:  libappstream-glib
# Matches what gnome-software and others use:
BuildRequires:  appstream

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
%autosetup -p1 -n wavbreaker-%{version}
# Since we install any contrib scripts as documentation with the execute bit
# unset, we remove any shebangs rather than applying:
#   %%py3_shebang_fix contrib/
# Note also that this package neither BuildRequires nor Requires a Python
# interpreter.
find contrib/ -type f -name '*.py' -print -exec sed -r -i '1{/^#!/d}' '{}' '+'


%build
%meson -Dmp3=true -Dogg_vorbis=true
%meson_build


%install
%meson_install
%find_lang wavbreaker


%check
desktop-file-validate \
  %{buildroot}%{_datadir}/applications/%{app_id}.desktop

# Still required by guidelines for now
# (https://pagure.io/packaging-committee/issue/1053):
appstream-util validate-relax --nonet \
    %{buildroot}/%{_metainfodir}/%{app_id}.appdata.xml
# Matches what gnome-software and others use:
appstreamcli validate --no-net --explain \
    %{buildroot}/%{_metainfodir}/%{app_id}.appdata.xml


%files -f wavbreaker.lang
%license COPYING

%doc AUTHORS
%doc CHANGELOG.md
%doc CONTRIBUTORS
%doc README.md
%doc contrib/

%{_bindir}/wavbreaker
%{_bindir}/wavcli

%{_metainfodir}/%{app_id}.appdata.xml
%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{app_id}.svg

%{_mandir}/man1/wavbreaker.1*
%{_mandir}/man1/wavcli.1*


%changelog
%autochangelog
