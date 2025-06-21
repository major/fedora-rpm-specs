Name:           quickemu
Version:        4.9.7
Release:        %autorelease
Summary:        Quickly create and run optimized Windows, macOS and Linux virtual machines
License:        MIT

URL:            https://github.com/quickemu-project/quickemu
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# Import an accepted upstream fix that solves VMs crashing due to the use of
# Pipewire on Fedora 41 and above
Patch:          https://github.com/quickemu-project/quickemu/pull/1565.patch

# Import an accepted upstream fix which ensures UEFI Secure Boot functions
# as a user would expect (on Fedora and other distributions), by enabling the
# Microsoft UEFI Secure Boot Platform Keys within VMs
Patch:          https://github.com/quickemu-project/quickemu/pull/1579.patch

BuildArch:      noarch

# The optional dependency 'zsync', used by quickget to download diffs of
# regularly-updated ISOs, is only available from third-party package repos
# so has not been included in this spec.
Requires:       bash
Requires:       coreutils
Requires:       curl
Requires:       edk2-tools
Requires:       genisoimage
Requires:       grep
Requires:       jq
Requires:       mesa-demos
Requires:       pciutils
Requires:       procps
Requires:       python3
Requires:       qemu
Requires:       sed
Requires:       socat
Requires:       spice-gtk-tools
Requires:       swtpm
Requires:       unzip
Requires:       usbutils
Requires:       util-linux
Requires:       xdg-user-dirs
Requires:       xrandr

%description
Quickly create and run optimized Windows, macOS and Linux virtual machines

%prep
%autosetup -p1

%install
# Install binaries
install -Dpm755 chunkcheck %{buildroot}%{_bindir}/chunkcheck
install -Dpm755 quickemu %{buildroot}%{_bindir}/quickemu
install -Dpm755 quickget %{buildroot}%{_bindir}/quickget
install -Dpm755 quickreport %{buildroot}%{_bindir}/quickreport
# Install manpages
install -Dpm644 docs/quickemu_conf.5 %{buildroot}%{_mandir}/man5/quickemu_conf.5
install -Dpm644 docs/quickemu.1 %{buildroot}%{_mandir}/man1/quickemu.1
install -Dpm644 docs/quickget.1 %{buildroot}%{_mandir}/man1/quickget.1

%files
%license LICENSE
%{_bindir}/chunkcheck
%{_bindir}/quickemu
%{_bindir}/quickget
%{_bindir}/quickreport
%{_mandir}/man5/quickemu_conf.5*
%{_mandir}/man1/quickemu.1*
%{_mandir}/man1/quickget.1*

%changelog
%autochangelog
