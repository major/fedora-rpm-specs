%bcond_without check
%global udevdir %(pkg-config --variable=udevdir udev)

# prevent library files from being installed
%global cargo_install_lib 0

Name:           huion-switcher
Version:        0.6.0
Release:        %autorelease
Summary:        Utility to switch Huion tablets into tablet mode

SourceLicense:  GPL-2.0-only
License:        GPL-2.0-only AND MIT AND (MIT OR Apache-2.0)
# LICENSE.dependencies contains a full license breakdown

URL:            https://github.com/whot/huion-switcher
Source:         https://github.com/whot/huion-switcher/archive/refs/tags/%{version}.tar.gz

BuildRequires:  cargo-rpm-macros >= 26
BuildRequires:  cargo
BuildRequires:  pkgconfig(udev) pkgconfig(libusb)
Requires:       udev

%global _description %{expand:
Utility to switch Huion tablets into tablet mode.}

%description %{_description}

%prep
%autosetup -n %{name}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
install -D -m 755 -t %{buildroot}/%{udevdir}/ target/release/huion-switcher
install -D -m 644 -t %{buildroot}/%{udevdir}/rules.d/ 80-huion-switcher.rules
install -D -m 644  huion-switcher.man %{buildroot}/%{_mandir}/man1/huion-switcher.1

%if %{with check}
%check
%cargo_test
%endif

%files
%license LICENSE
%license LICENSE.dependencies
%doc README.md
%{udevdir}/huion-switcher
%{_mandir}/man1/huion-switcher.1*
%{udevdir}/rules.d/80-huion-switcher.rules

%changelog
%autochangelog
