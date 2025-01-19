Name:           pari-nftables
Version:        20080929
Release:        9%{?dist}
Summary:        PARI/GP Computer Algebra System number field tables

# See http://pari.math.u-bordeaux.fr/packages.html for license information.
License:        GPL-2.0-or-later
URL:            https://pari.math.u-bordeaux.fr/packages.html
Source0:        https://pari.math.u-bordeaux.fr/pub/pari/packages/nftables.tgz
Source1:        https://pari.math.u-bordeaux.fr/pub/pari/packages/nftables.tgz.asc
# Public key 0xedef8d6a, Karim Belabas <Karim.Belabas@math.u-bordeaux.fr>
Source2:        gpgkey-dd6754092ef692988cfcdcbad49a9c20edef8d6a.gpg

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
BuildArch:      noarch

BuildRequires:  gnupg2
BuildRequires:  parallel

%description
This package contains the optional PARI package nftables, which provides the
historical megrez number fields tables (errors fixed, 1/10th the size, easier
to use).  These tables can be queried by readvec.

%prep
# Verify the source file
%{gpgverify} --data=%{SOURCE0} --signature=%{SOURCE1} --keyring=%{SOURCE2}

%autosetup -c

# We'll ship the README as %%doc
mv nftables/README .

%build
# Pari can read compressed data files, so save space
parallel %{?_smp_mflags} --no-notice gzip --best ::: nftables/*.gp

%install
mkdir -p %{buildroot}%{_datadir}/pari
cp -a nftables %{buildroot}%{_datadir}/pari

%files
%doc README
%{_datadir}/pari/

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20080929-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20080929-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20080929-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20080929-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 16 2024 Jerry James <loganjerry@gmail.com> - 20080929-5
- Stop building for 32-bit x86

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20080929-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20080929-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 12 2022 Jerry James <loganjerry@gmail.com> - 20080929-3
- Convert License tag to SPDX

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20080929-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20080929-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 11 2021 Jerry James <loganjerry@gmail.com> - 20080929-1
- Initial RPM
