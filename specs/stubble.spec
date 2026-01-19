%global commit b5e720e4a080bf4e7cc2edc09c19d73db21b401a
%global commitdate 20251118
%global shortcommit %(c=%{commit}; echo ${c:0:7})

# This builds an UEFI binary, not a Linux ELF binary, disable distro cflags and debug pkg
%undefine _auto_set_build_flags
%global debug_package %{nil}

Name:           stubble
Version:        0.0~%{commitdate}git%{shortcommit}
Release:        3%{?dist}
Summary:        UEFI kernel boot stub with auto-DTB selection
License:        LGPL-2.1-or-later
URL:            https://github.com/ubuntu/%{name}
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Patch1:         0001-Makefile-Add-fPIC-to-CFLAGS.patch
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  python3-pyelftools
# This is only useful on aarch64
ExclusiveArch:  %{arm64}

%description
A minimal UEFI kernel boot stub that serves a single purpose:

Loading machine specific device trees embedded within a kernel image.

stubble is compatible with systemd-stub(7) and ukify(1).


%prep
%autosetup -C -p1


%build
%make_build


%install
%make_install


%files
%license LICENSE.LGPL2.1
%doc README.md
%{_prefix}/lib/%{name}/
%{_datadir}/%{name}/


%changelog
* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.0~20251118gitb5e720e-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Sun Jan 11 2026 Hans de Goede <johannes.goede@oss.qualcomm.com> - 0.0~20251118gitb5e720e-2
- Use %%{url} for Source0
- Use %%{arm64} for ExclusiveArch
- Use 1 line per BuildRequires

* Sun Dec 14 2025 Hans de Goede <johannes.goede@oss.qualcomm.com> - 0.0~20251118gitb5e720e-1
- Move the git snapshot date + hash to the version field
- Use %%undefine _auto_set_build_flags, %%make_build, %%make_install
- Add trailing slash after stubble directory listings in %%files

* Sat Dec 13 2025 Hans de Goede <johannes.goede@oss.qualcomm.com> - 0.0-2.20251118gitb5e720e
- Add ExclusiveArch: aarch64

* Sat Dec 13 2025 Hans de Goede <johannes.goede@oss.qualcomm.com> - 0.0-1.20251118gitb5e720e
- Initial Fedora stubble package
