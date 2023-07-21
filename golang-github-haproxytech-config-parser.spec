%bcond_without check

# https://github.com/haproxytech/config-parser
%global goipath         github.com/haproxytech/config-parser
Version:                4.0.0~rc2
%global commit          12e472fc123e747c019d30f230cbb989df695354

%gometa

%global goaltipaths     %{goipath}/v4

%global common_description %{expand:
HAProxy configuration parser.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        7%{?dist}
Summary:        HAProxy configuration parser

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/gofrs/flock)
BuildRequires:  golang(github.com/google/renameio)
BuildRequires:  golang(github.com/haproxytech/go-logger)

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0~rc2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0~rc2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0~rc2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0~rc2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 13 2021 Brandon Perkins <bperkins@redhat.com> - 4.0.0~rc2-3
- Update to commit 12e472fc123e747c019d30f230cbb989df695354 (Fixes rhbz#2011802)

* Mon Nov 01 2021 Brandon Perkins <bperkins@redhat.com> - 4.0.0~rc2-2
- Update to commit f9021b6ca61c847038a362aa62f4c0b7758c517f (Fixes rhbz#2011802)

* Fri Oct 08 2021 Brandon Perkins <bperkins@redhat.com> - 4.0.0~rc2-1
- Update to commit 7d06e7638ee9194f02df56a91de90c51341aaba9 (Fixes rhbz#2011802)

* Thu Sep 09 2021 Brandon Perkins <bperkins@redhat.com> - 4.0.0~rc1-3
- Update to commit 0a376da86e89ca30da8c649efd754b8a5e4be9d9 (Fixes rhbz#1979324)

* Tue Aug 10 2021 Brandon Perkins <bperkins@redhat.com> - 4.0.0~rc1-2
- Update to commit 340f1b3664db3b1640a3c75b5ffd73e55e85fb27 (Fixes rhbz#1979324)

* Mon Aug 09 2021 Brandon Perkins <bperkins@redhat.com> - 4.0.0~rc1-1
- Update to version 4.0.0-rc1 (Fixes rhbz#1979324)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Mar 19 2021 Brandon Perkins <bperkins@redhat.com> - 3.1.0-1
- Update to version 3.1.0 (Fixes rhbz#1940974)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 17 16:15:02 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 3.0.0-1
- Update to 3.0.0
- Close: rhbz#1916916

* Wed Jan 13 2021 Brandon Perkins <bperkins@redhat.com> - 3.0.0~rc2-2
- Modify gosource so that Source0 resolves correctly  (Fixes rhbz#1912980)

* Tue Jan 12 2021 Brandon Perkins <bperkins@redhat.com> - 3.0.0~rc2-1
- Update to version 3.0.0-rc2 (Fixes rhbz#1912980)

* Thu Sep 03 2020 Brandon Perkins <bperkins@redhat.com> - 2.0.5-1
- Update to version 2.0.5 (Fixes rhbz#1875169)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Brandon Perkins <bperkins@redhat.com> - 2.0.4-1
- Update to version 2.0.4 (Fixes rhbz#1859324)
- Add golang(github.com/google/renameio) BuildRequires

* Mon May 18 2020 Brandon Perkins <bperkins@redhat.com> - 2.0.2-1
- Update to version 2.0.2

* Mon Apr 27 2020 Brandon Perkins <bperkins@redhat.com> - 2.0.1-1
- Upgrade to version 2.0.1

* Mon Mar 02 2020 Brandon Perkins <bperkins@redhat.com> - 1.2.0-1
- Upgrade to version 1.2.0
- Clean changelog

* Wed Nov 13 2019 Brandon Perkins <bperkins@redhat.com> - 1.1.10-1
- Initial package

