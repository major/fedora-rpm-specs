%define service recompress

Name:           obs-service-%{service}
Version:        0.5.2
Release:        3%{?dist}
Summary:        An OBS source service: Recompress files
License:        GPL-2.0-or-later
URL:            https://github.com/openSUSE/obs-service-%{service}
Source:         %{url}/archive/refs/tags/%{version}.tar.gz#./%{name}-%{version}.tar.gz
BuildRequires:  make
BuildRequires:  gzip
BuildRequires:  bzip2
BuildRequires:  xz
BuildRequires:  zstd
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(File::Copy)
BuildRequires:  /usr/bin/prove
Requires:       bzip2
Requires:       gzip
Requires:       xz
Requires:       zstd

BuildArch:      noarch

%description
This is a source service for openSUSE Build Service.

It supports to compress, uncompress or recompress files from or to

 none : No Compression
 gz   : Gzip Compression
 bz2  : Bzip2 Compression
 xz   : XZ Compression


%prep
%autosetup -p1

%build
# Nothing to build

%install
%make_install

%check
%make_build test

%files
# In lieu of a proper license file: https://github.com/openSUSE/obs-service-recompress/issues/13
%license debian/copyright
%doc README.md
%dir %{_prefix}/lib/obs
%{_prefix}/lib/obs/service

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Feb  1 2024 Dan Čermák <dan.cermak@cgc-instruments.com> - 0.5.2-1
- New upstream release 0.5.2

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-13.git20170704.59bf231
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-12.git20170704.59bf231
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-11.git20170704.59bf231
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-10.git20170704.59bf231
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-9.git20170704.59bf231
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-8.git20170704.59bf231
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-7.git20170704.59bf231
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-6.git20170704.59bf231
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-5.git20170704.59bf231
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-4.git20170704.59bf231
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 31 2019 Neal Gompa <ngompa13@gmail.com> - 0.3.1-3.git20170704.59bf231
- Rebuild again to deal with random Koji+Bodhi breakage

* Tue Dec 31 2019 Neal Gompa <ngompa13@gmail.com> - 0.3.1-2.git20170704.59bf231
- Rebuild to deal with random Koji+Bodhi breakage

* Fri Dec 27 2019 Neal Gompa <ngompa13@gmail.com> - 0.3.1-1.git20170704.59bf231
- Initial packaging

