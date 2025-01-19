%global commit 8ea7a76324b19e0ea3b1a559cbdfb8da9d038304
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global snapdate 20190325

%global service extract_file

Name:           obs-service-%{service}
# Version comes from what openSUSE has released as in openSUSE:Tools
# From: https://build.opensuse.org/package/show/openSUSE:Tools/obs-service-extract_file
Version:        0.3
Release:        16%{?snapdate:.%{snapdate}git%{shortcommit}}%{?dist}
Summary:        An OBS source service: Extract a file from an archive

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/openSUSE/obs-service-%{service}
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildArch:      noarch
Requires:       cpio
Requires:       bzip2
Requires:       findutils
Requires:       gzip
Requires:       tar
Requires:       unzip
Requires:       xz

%description
This is a source service for openSUSE Build Service.

It supports to extract a file from an archive, for example a spec file from a tar.


%prep
%autosetup -n %{name}-%{commit}


%build
# Nothing to build


%install
mkdir -p %{buildroot}%{_prefix}/lib/obs/service
install -pm 0755 extract_file %{buildroot}%{_prefix}/lib/obs/service
install -pm 0644 extract_file.service %{buildroot}%{_prefix}/lib/obs/service


%files
# In lieu of a proper license file: https://github.com/openSUSE/obs-service-extract_file/issues/13
%license debian/copyright
%dir %{_prefix}/lib/obs
%{_prefix}/lib/obs/service



%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-16.20190325git8ea7a76
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.3-15.20190325git8ea7a76
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-14.20190325git8ea7a76
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-13.20190325git8ea7a76
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-12.20190325git8ea7a76
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-11.20190325git8ea7a76
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-10.20190325git8ea7a76
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-9.20190325git8ea7a76
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-8.20190325git8ea7a76
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-7.20190325git8ea7a76
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-6.20190325git8ea7a76
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-5.20190325git8ea7a76
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-4.20190325git8ea7a76
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-3.20190325git8ea7a76
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 25 2019 Neal Gompa <ngompa13@gmail.com> - 0.3-2.20190325git8ea7a763
- Add findutils dependency

* Mon Mar 25 2019 Neal Gompa <ngompa13@gmail.com> - 0.3-1.20190325git8ea7a763
- Initial packaging
