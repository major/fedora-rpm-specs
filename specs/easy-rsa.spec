Name:      easy-rsa
Version:   3.2.2
Release:   1%{?dist}

Summary:   Simple shell based CA utility
License:   GPL-2.0-only

URL:       https://github.com/OpenVPN/easy-rsa
Source0:   %{url}/releases/download/v%{version}/EasyRSA-%{version}.tgz

Requires:  openssl
BuildArch: noarch


%description
This is a small RSA key management package, based on the openssl
command line tool, that can be found in the easy-rsa subdirectory
of the OpenVPN distribution. While this tool is primary concerned
with key management for the SSL VPN application space, it can also
be used for building web certificates.


%prep
%autosetup -n EasyRSA-%{version} -p1


%build
#Nothing to build


%install
mkdir -p %{buildroot}%{_datadir}/easy-rsa/%{version}/
(
cd %{buildroot}%{_datadir}/easy-rsa
ln -s %{version} 3.0
ln -s %{version} 3
)
cp -rp easyrsa %{buildroot}%{_datadir}/easy-rsa/%{version}/
cp -rp openssl-easyrsa.cnf %{buildroot}%{_datadir}/easy-rsa/%{version}/
cp -rp x509-types %{buildroot}%{_datadir}/easy-rsa/%{version}/


%files
%doc ChangeLog *.md vars.example
%license gpl-2.0.txt COPYING.md
%{_datadir}/easy-rsa/


%changelog
* Mon Feb 03 2025 Gwyn Ciesla <gwync@protonmail.com> - 3.2.2-1
- 3.2.2

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 16 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.2.1-1
- 3.2.1

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon May 20 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.2.0-1
- 3.2.0

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Oct 16 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.1.7-1
- 3.1.7

* Wed Aug 23 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.1.6-1
- 3.1.6

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 12 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.1.5-1
- 3.1.5

* Thu May 25 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.1.4-1
- 3.1.4

* Sat May 20 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.1.3-1
- 3.1.3

* Sun Mar 05 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.1.2-3
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 17 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.1.2-1
- 3.1.2

* Mon Oct 17 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.1.1-1
- 3.1.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu May 19 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.1.0-1
- 3.1.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 06 2022 Neal Gompa <ngompa@datto.com> - 3.0.8-4
- Minor cleanups and install COPYING.md as license file

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Sep 10 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.0.8-1
- 3.0.8

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 31 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.0.7-1
- 3.0.7

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Xavier Bachelot <xavier@bachelot.org> - 3.0.6-1
- Update to 3.0.6.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Gwyn Ciesla <limburgher@gmail.com> - 3.0.3-1
-3.0.3, fix for new openssl.

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Jon Ciesla <limburgher@gmail.com> - 3.0.1-1
- Latest stable upstream, BZ 1304339.
- Updated path structure, François Kooman fkooman@tuxed.net

* Mon Sep 21 2015 Jon Ciesla <limburgher@gmail.com> - 3.0.0-1
- Latest stable upstream.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 19 2014 Jon Ciesla <limburgher@gmail.com> - 2.2.2-1
- Latest stable upstream.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 14 2013 Jon Ciesla <limburgher@gmail.com> - 2.2.0-2
- Update cp to preserve timestamps.

* Wed May 22 2013 Jon Ciesla <limburgher@gmail.com> - 2.2.0-1
- Create.
