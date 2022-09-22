Name:     signify
Version:  30
Release:  7%{?dist}
Summary:  Sign and verify signatures on files

License:  ISC and MIT and BSD and Public Domain
URL:      https://github.com/aperezdc/%{name}
Source0:  %url/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:  %url/releases/download/v%{version}/%{name}-%{version}.tar.xz.asc
Source2:  https://keys.openpgp.org/vks/v1/by-fingerprint/5AA3BC334FD7E3369E7C77B291C559DBE4C9123B
# Replace install command with \$(INSTALL) variable to keep timestamp with %%make_install
Patch0:   https://github.com/aperezdc/signify/commit/a12d866b673972b41802d0fdd20f4e65699da44e.patch#/signify-30-install.patch

BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  pkgconfig(libbsd)

%description
The signify utility creates and verifies cryptographic signatures, as used
by the OpenBSD release maintainers.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1
# remove upstream bundled optional library libwaive from source
rm -rf libwaive

%build
%set_build_flags
%make_build

%install
%make_install PREFIX=%{_prefix}

%check
make check

%files
%license COPYING
%doc CHANGELOG.md README.md
%{_bindir}/signify
%{_mandir}/man1/signify.*

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 30-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Robert Scheck <robert@fedoraproject.org> - 30-6
- Spec file improvements by Robert-André Mauchin
  - Add tarball signature verification
  - Add patch to keep files timestamps
  - Rewrite summary (no encrypt)
  - Add Public Domain License
- Switch to upstream commit for keeping file timestamps

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 30-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 30-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Feb 28 2021 Marcus Müller <marcus@hostalia.de> - 30-3
- Fixed License tag
- rid of unescaped macros in %%changelog

* Wed Feb 24 2021 Marcus Müller <marcus@hostalia.de> - 30-2
- enable tests

* Wed Feb 24 2021 Marcus Müller <marcus@hostalia.de> - 30-1
- Bump upstream version
- Include the upstreamed license file
- Add newlines to changelog
- set LD explicitly (thanks sagitter)

* Sat Jan 11 2020 Marcus Müller <marcus@hostalia.de> - 27-2
- removed bundled library libwaive from source

* Fri Jan 10 2020 Marcus Müller <marcus@hostalia.de> - 27-1
- updated to release v27
- prepared `%%check` for as soon as regression tests are released
- fixed `%%set_build_flags` (thanks Antonio <anto.trande@gmail.com>)
- proper _prefix (thanks Vít Ondruch <vondruch@redhat.com>)

* Fri Nov 01 2019 Marcus Müller <marcus@hostalia.de> - 26-1
- Initial import
