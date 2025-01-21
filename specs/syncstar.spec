%global pack syncstar

Name:           %{pack}
Version:        0.2.0
Release:        2%{?dist}
Summary:        Service for creating bootable USB storage devices at community conference kiosks

# The syncstar project is licensed under AGPL-3.0-or-later license, except for the following files
#
# MIT license -
# syncstar/frontend/assets/index-*.css (Read here https://github.com/facebook/react)
# syncstar/frontend/assets/index-*.js (Read here https://github.com/facebook/react)
#
# OFL license -
# syncstar/frontend/assets/mono_*.ttf (Read here https://github.com/JetBrains/JetBrainsMono)
# syncstar/frontend/assets/sans_*.ttf (Read here https://github.com/rsms/inter)

License:        AGPL-3.0-or-later AND MIT
Url:            https://github.com/gridhead/%{pack}
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel

Requires:       coreutils
Requires:       util-linux
Requires:       redis

%description
SyncStar lets users create bootable USB storage devices with the operating
system image of their choice. This application is intended to be deployed on
kiosk devices and electronic signages where conference guests and booth
visitors can avail its services.

%prep
%autosetup -n %{pack}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pack}

%check
%tox

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild


* Sat Dec 21 2024 Akashdeep Dhar <t0xic0der@fedoraproject.org> - 0.2.0-1
- Second release for SyncStar project
- More information can be found on https://github.com/gridhead/syncstar/releases/tag/0.2.0

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Existing release for SyncStar project
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 02 2024 Akashdeep Dhar <t0xic0der@fedoraproject.org> - 0.1.0-1
- Initial release for SyncStar project
- More information can be found on https://github.com/gridhead/syncstar/releases/tag/0.1.0
