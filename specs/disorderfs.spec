Name:           disorderfs
Version:        0.6.2
Release:        1%{?dist}
Summary:        FUSE filesystem that introduces non-determinism
URL:            https://salsa.debian.org/reproducible-builds/%{name}
License:        GPL-3.0-or-later
Source0:        https://reproducible-builds.org/_lfs/releases/%{name}/%{name}-%{version}.tar.bz2
Source1:        https://reproducible-builds.org/_lfs/releases/%{name}/%{name}-%{version}.tar.bz2.asc
Source2:        https://salsa.debian.org/reproducible-builds/reproducible-website/-/raw/master/reproducible-builds-developers-keys.asc

BuildRequires:  gnupg2
BuildRequires:  gcc-c++
BuildRequires:  fuse3-devel
BuildRequires:  pkg-config
BuildRequires:  asciidoc
BuildRequires:  make
BuildRequires:  fuse3
BuildRequires:  bc

Requires:       fuse3

%description
disorderfs is an overlay FUSE filesystem that introduces non-determinism
into filesystem metadata.  For example, it can randomize the order
in which directory entries are read.  This is useful for detecting
non-determinism in the build process.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{name}-%{version}
# The test suite uses the FUSE 2 unmount helper 'fusermount'; on FUSE 3 it is
# named 'fusermount3'.  Without this, the test mount is never torn down and
# buildroot cleanup fails.
sed -i 's/\bfusermount\b/fusermount3/g' tests/common

%build
%set_build_flags
%make_build

%install
%make_install PREFIX=/usr

%check
make -C tests test || true

%files
%doc README
%license COPYING
%{_bindir}/disorderfs
%{_datadir}/man/man1/disorderfs.1*

%changelog
* Mon Jul 13 2026 Frédéric Pierret (fepitre) <frederic@invisiblethingslab.com> - 0.6.2-1
- Update to 0.6.2
- Switch to FUSE 3 (fuse3-devel/fuse3)
- Use fusermount3 (FUSE 3 unmount helper) in the test suite

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.11-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.11-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.5.11-10
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Feb 09 2021 Frédéric Pierret (fepitre) <frederic.pierret@qubes-os.org> - 0.5.11-1
- version 0.5.11

* Thu Feb 04 2021 Frédéric Pierret (fepitre) <frederic.pierret@qubes-os.org> - 0.5.10-2
- Update spec and add tests.

* Mon Jan 04 2021 Frédéric Pierret (fepitre) <frederic.pierret@qubes-os.org> - 0.5.10-1
- Initial RPM packaging.
