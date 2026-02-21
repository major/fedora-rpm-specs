Name:           syncplay
Version:        1.7.5
Release:        %autorelease
Summary:        Synchronize playback of various video players via internet

License:        Apache-2.0 AND MIT AND BSD-3-Clause AND CC-BY-3.0
URL:            https://syncplay.pl
Source0:        https://github.com/Syncplay/syncplay/archive/refs/tags/v%{version}/syncplay-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  desktop-file-utils
BuildRequires:  python3-devel
Requires:       hicolor-icon-theme

%description
Solution to synchronize video playback across multiple instances of mpv, VLC,
MPC-HC and MPC-BE over the Internet.
Syncplay synchronizes the position and play state of multiple media players so
that the viewers can watch the same thing at the same time. This means that
when one person pauses/unpauses playback or seeks (jumps position) within their
media player then this will be replicated across all media players connected to
the same server and in the same 'room' (viewing session). When a new person
joins they will also be synchronised. Syncplay also includes text-based chat so
you can discuss a video as you watch it (or you could use third-party Voice
over IP software to talk over a video).


%prep
%autosetup -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{name}

# Install desktop files
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  syncplay/resources/*.desktop

# Install icons
for size in 256 128 96 64 48 32 24 16; do
  install -Dpm 0644 \
    syncplay/resources/hicolor/${size}x${size}/apps/syncplay.png \
    %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/syncplay.png
done

# Install man pages
install -Dpm 0644 docs/syncplay.1 %{buildroot}/%{_mandir}/man1/syncplay.1
install -Dpm 0644 docs/syncplay-server.1 %{buildroot}/%{_mandir}/man1/syncplay-server.1


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/syncplay.desktop


%files -f %{pyproject_files}
%license LICENSE syncplay/resources/third-party-notices.txt
%doc README.md
%{_bindir}/syncplay
%{_bindir}/syncplay-server
%{_datadir}/applications/syncplay.desktop
%{_datadir}/applications/syncplay-server.desktop
%{_datadir}/icons/hicolor/*/apps/syncplay.png
%{_mandir}/man1/syncplay.1.*
%{_mandir}/man1/syncplay-server.1.*


%changelog
%autochangelog

