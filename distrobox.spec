%global debug_package %{nil}

# https://github.com/89luca89/distrobox/issues/127
%global __brp_mangle_shebangs_exclude_from %{_bindir}/distrobox-(export|init)$

%global forgeurl https://github.com/89luca89/distrobox
%global tag %{version}

Name:    distrobox
Version: 1.5.0.1

%forgemeta

Release: %autorelease
Summary: Another tool for containerized command line environments on Linux 
License: GPLv3
URL:     %{forgeurl}
Source:  %{forgesource}

BuildArch: noarch

BuildRequires: ImageMagick

Requires: (podman or %{_bindir}/docker)
Requires: %{_bindir}/basename
Requires: %{_bindir}/find
Requires: %{_bindir}/grep
Requires: %{_bindir}/sed
Requires: hicolor-icon-theme

Suggests: bash-completions

%description
Use any linux distribution inside your terminal. Distrobox uses podman 
or docker to create containers using the linux distribution of your 
choice. Created container will be tightly integrated with the host, 
allowing to share the HOME directory of the user, external storage, 
external usb devices and graphical apps (X11/Wayland) and audio.

%prep
%forgesetup

%build

%install
./install -P %{buildroot}/%{_prefix}

#install -d -m0755 %{buildroot}%{_docdir}/%{name}
#install -m 0644 docs/*.md %{buildroot}%{_docdir}/%{name}

# Move the icon 
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
mv %{buildroot}%{_datadir}/icons/terminal-distrobox-icon.svg \
   %{buildroot}%{_datadir}/icons/hicolor/scalable/apps

# Generate more icon sizes
for sz in 16 22 24 32 36 48 64 72 96 128 256; do
  mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${sz}x${sz}/apps
  convert terminal-distrobox-icon.svg -resize ${sz}x${sz} \
    %{buildroot}%{_datadir}/icons/hicolor/${sz}x${sz}/apps/terminal-distrobox-icon.png
done

%check
%{buildroot}%{_bindir}/%{name} list -V
for i in create enter export init list rm stop host-exec; do
    %{buildroot}%{_bindir}/%{name}-$i -V
done

%files
%license COPYING.md
%{_mandir}/man1/%{name}*
%{_bindir}/%{name}
%{_bindir}/%{name}-create
%{_bindir}/%{name}-enter
%{_bindir}/%{name}-export
%{_bindir}/%{name}-init
%{_bindir}/%{name}-list
%{_bindir}/%{name}-rm
%{_bindir}/%{name}-stop
%{_bindir}/%{name}-host-exec
%{_bindir}/%{name}-ephemeral
%{_bindir}/%{name}-generate-entry
%{_bindir}/%{name}-upgrade
%{_bindir}/%{name}-assemble
%{_datadir}/icons/hicolor/*/apps/terminal-distrobox-icon.png
%{_datadir}/icons/hicolor/scalable/apps/terminal-distrobox-icon.svg
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/%{name}*

%changelog
%autochangelog
