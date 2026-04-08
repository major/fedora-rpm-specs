#                        TO WHOM IT MAY CONCERN
#
# Don't add patches, dist-git is the upstream repository for this package.


Name:           redhat-systemd-presets
# Please only bump the version in the rawhide branch, all other branches
# should leave the version alone.
Version:        102
Release:        %autorelease
Summary:        Red Hat family systemd presets
URL:            https://src.fedoraproject.org/rpms/redhat-systemd-presets
License:        MIT

# License
Source1:        LICENSE

# Common preset files
Source10:       85-display-manager.preset
Source11:       90-default.preset
Source12:       90-default-user.preset
Source13:       99-default-disable.preset

# Desktop preset files
Source27:       81-desktop.preset

# Atomic desktop preset files
Source37:       81-atomic-desktop.preset

BuildRequires:  systemd-rpm-macros

BuildArch:      noarch

# Allow only one provider
Provides:       distribution-systemd-presets
Conflicts:      distribution-systemd-presets

Requires:       %{name}-common = %{version}-%{release}

%description
Red Hat family systemd preset files that determine which services are enabled by default.
# See https://docs.fedoraproject.org/en-US/packaging-guidelines/DefaultServices/ for details.

%files
%license LICENSE

%dnl ----------------------------------------------------------

%package common
Summary:        Common systemd presets for the Red Hat family
# Ensures that this is considered merely a separation detail
Requires:       %{name} = %{version}-%{release}
# From the split from fedora-release
Conflicts:      fedora-release-common < 45-0.5
Obsoletes:      fedora-release-common < 45-0.5
# Allow only one provider
Provides:       distribution-systemd-presets-common
Conflicts:      distribution-systemd-presets-common

%description common
Red Hat family systemd preset files common to all distributions and variants
that determine which services are enabled by default.

%files common
%dir %{_presetdir}
%{_presetdir}/85-display-manager.preset
%{_presetdir}/90-default.preset
%{_presetdir}/99-default-disable.preset
%dir %{_userpresetdir}
%{_userpresetdir}/90-default-user.preset
%{_userpresetdir}/99-default-disable.preset

%dnl ----------------------------------------------------------

%package desktop
Summary:        Desktop systemd presets for the Red Hat family
Requires:       %{name}-common = %{version}-%{release}
# From the split from fedora-release
Conflicts:      fedora-release-variant < 45-0.5
# Deal with all the identity flavors that had this file
%global fedora_flavor_obsoletes() \
Obsoletes:      fedora-release-identity-%{1} < 45-0.5

%fedora_flavor_obsoletes budgie
%fedora_flavor_obsoletes budgie-atomic
%fedora_flavor_obsoletes cinnamon
%fedora_flavor_obsoletes cosmic
%fedora_flavor_obsoletes cosmic-atomic
%fedora_flavor_obsoletes designsuite
%fedora_flavor_obsoletes i3
%fedora_flavor_obsoletes kde-desktop
%fedora_flavor_obsoletes kde-mobile
%fedora_flavor_obsoletes kinoite
%fedora_flavor_obsoletes kinoite-mobile
%fedora_flavor_obsoletes lxde
%fedora_flavor_obsoletes lxqt
%fedora_flavor_obsoletes matecompiz
%fedora_flavor_obsoletes miraclewm
%fedora_flavor_obsoletes miraclewm-atomic
%fedora_flavor_obsoletes mobility
%fedora_flavor_obsoletes silverblue
%fedora_flavor_obsoletes soas
%fedora_flavor_obsoletes sway
%fedora_flavor_obsoletes sway-atomic
%fedora_flavor_obsoletes workstation
%fedora_flavor_obsoletes xfce

# Allow only one provider
Provides:       distribution-systemd-presets-desktop
Conflicts:      distribution-systemd-presets-desktop

%description desktop
Red Hat family systemd preset files for all desktop variants
that determine which services are enabled by default.

%files desktop
%{_presetdir}/81-desktop.preset

%dnl ----------------------------------------------------------

%package desktop-atomic
Summary:        Atomic Desktop systemd presets for the Red Hat family
Requires:       %{name}-desktop = %{version}-%{release}
Conflicts:      fedora-release-ostree-desktop < 45-0.5
Obsoletes:      fedora-release-ostree-desktop < 45-0.5
# Allow only one provider
Provides:       distribution-systemd-presets-desktop-atomic
Conflicts:      distribution-systemd-presets-desktop-atomic

%description desktop-atomic
Red Hat family systemd preset files for all atomic desktop variants
that determine which services are enabled by default.

%files desktop-atomic
%{_presetdir}/81-atomic-desktop.preset

%dnl ----------------------------------------------------------


%prep
%autosetup -T -c


%build
# Nothing to do


%install
# Install licenses
install -pm 0644 %{SOURCE1} LICENSE

# Default system wide
install -Dm0644 %{SOURCE10} -t %{buildroot}%{_presetdir}/
install -Dm0644 %{SOURCE11} -t %{buildroot}%{_presetdir}/
install -Dm0644 %{SOURCE12} -t %{buildroot}%{_userpresetdir}/
# The same file is installed in two places with identical contents
install -Dm0644 %{SOURCE13} -t %{buildroot}%{_presetdir}/
install -Dm0644 %{SOURCE13} -t %{buildroot}%{_userpresetdir}/

# Common desktop preset
install -Dm0644 %{SOURCE27} -t %{buildroot}%{_presetdir}/

# Atomic Desktop specific preset
install -Dm0644 %{SOURCE37} -t %{buildroot}%{_presetdir}/


%changelog
%autochangelog
