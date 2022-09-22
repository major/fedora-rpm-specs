%global commit 59bf23181b7fd61471ea567c8a57dbdd36fca753
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20170704

# For rpmdev-bumpspec
%global baserelease 9

%define service recompress

Name:           obs-service-%{service}
Version:        0.3.1
Release:        %{baserelease}%{?commitdate:.git%{commitdate}.%{shortcommit}}%{?dist}
Summary:        An OBS source service: Recompress files
License:        GPLv2+
URL:            https://github.com/openSUSE/obs-service-%{service}
Source:         %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
BuildRequires:  make
Requires:       bzip2
Requires:       gzip
Requires:       xz
BuildArch:      noarch

%description
This is a source service for openSUSE Build Service.

It supports to compress, uncompress or recompress files from or to

 none : No Compression
 gz   : Gzip Compression
 bz2  : Bzip2 Compression
 xz   : XZ Compression


%prep
%autosetup -n %{name}-%{commit} -p1

%build
# Nothing to build

%install
%make_install

%files
# In lieu of a proper license file: https://github.com/openSUSE/obs-service-recompress/issues/13
%license debian/copyright
%doc README.md
%dir %{_prefix}/lib/obs
%{_prefix}/lib/obs/service

%changelog
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

