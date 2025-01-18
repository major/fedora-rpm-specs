%global upstreamname debian-archive-keyring

Name:           debian-keyring
Version:        2023.4
Release:        5%{?dist}
Summary:        GnuPG archive keys of the Debian archive

License:        LicenseRef-Fedora-Public-Domain
URL:            http://packages.debian.org/unstable/admin/%{upstreamname}
Source0:        http://ftp.debian.org/debian/pool/main/d/%{upstreamname}/%{upstreamname}_%{version}.tar.xz
# Use gpg2
Patch0:         debian-keyring_gpg2.patch

BuildArch:      noarch
BuildRequires:  jetring
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  keyrings-filesystem
Requires:       keyrings-filesystem

%description
The Debian project digitally signs its Release files. This package contains the
archive keys used for that.

%prep
%autosetup -p1 -n %{upstreamname}


%build
make


%install
%make_install


%files
%doc README
%exclude %{_sysconfdir}/apt/trusted.gpg.d
%{_keyringsdir}/*.gpg


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2023.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2023.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2023.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2023.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Aug 05 2023 Sandro Mani <manisandro@gmail.com> - 2023.4-1
- Update to 2023.4

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2023.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Mar 31 2023 Sandro Mani <manisandro@gmail.com> - 2023.3-1
- Update to 2023.3

* Sun Mar 19 2023 Sandro Mani <manisandro@gmail.com> - 2023.2-1
- Update to 2023.2

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2021.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2021.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2021.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2021.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Sandro Mani <manisandro@gmail.com> - 2021.1.1-1
- Update to 2021.1.1

* Thu Feb 25 2021 Sandro Mani <manisandro@gmail.com> - 2021.1-1
- Update to 2021.1

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2019.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2019.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 23 2019 Sandro Mani <manisandro@gmail.com> - 2019.1-1
- Update to 2019.1

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 29 2018 Sandro Mani <manisandro@gmail.com> - 2018.1-1
- Update to 2018.1

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 17 2017 Sandro Mani <manisandro@gmail.com> - 2017.7-1
- Update to 2017.7

* Thu Sep 07 2017 Sandro Mani <manisandro@gmail.com> - 2017.6-1
- Update to 2017.6

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2017.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 29 2017 Sandro Mani <manisandro@gmail.com> - 2017.5-1
- Update to 2017.5

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2014.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2014.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2014.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Dec 01 2014 Sandro Mani <manisandro@gmail.com> -  2014.1-3
- Update to 2014.3

* Mon Sep 01 2014 Sandro Mani <manisandro@gmail.com> -  2014.1-1
- Update to 2014.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2012.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Sep 23 2013 Sandro Mani <manisandro@gmail.com> - 2012.4-2
- Add keyrings-filesystem Requires and BuildRequires.

* Thu Sep 19 2013 Sandro Mani <manisandro@gmail.com> - 2012.4-1
- Initial package
