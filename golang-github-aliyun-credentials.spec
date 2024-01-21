%bcond_without check

# https://github.com/aliyun/credentials-go
%global goipath         github.com/aliyun/credentials-go
Version:                1.1.3

%gometa

%global common_description %{expand:
Alibaba Cloud (Aliyun) Credentials for Go.}

%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README-CN.md README.md

Name:           %{goname}
Release:        7%{?dist}
Summary:        Alibaba Cloud (Aliyun) Credentials for Go

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/alibabacloud-go/debug/debug)
BuildRequires:  golang(github.com/alibabacloud-go/tea/tea)
BuildRequires:  golang(gopkg.in/ini.v1)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
%endif

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
* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 17 2022 Robert-André Mauchin <zebob.m@gmail.com> - 1.1.3-3
- Rebuilt for CVE-2022-1996, CVE-2022-24675, CVE-2022-28327, CVE-2022-27191,
  CVE-2022-29526, CVE-2022-30629

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct 07 2021 Brandon Perkins <bperkins@redhat.com> - 1.1.3-1
- Update to version 1.1.3 (Fixes rhbz#2004764)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 08 2020 Brandon Perkins <bperkins@redhat.com> - 1.1.2-1
- Update to version 1.1.2 (Fixes rhbz#1876320)

* Sun Aug 02 2020 Brandon Perkins <bperkins@redhat.com> - 1.1.1-2
- Update summary and description for clarity and consistency

* Fri Jul 31 2020 Brandon Perkins <bperkins@redhat.com> - 1.1.1-1
- Update to version 1.1.1 (Fixes rhbz#1811177)
- Remove patch for fixed https://github.com/aliyun/credentials-go/pull/22

* Wed Jul 29 2020 Brandon Perkins <bperkins@redhat.com> - 1.1.0-1
- Update to version 1.1.0 (Fixes rhbz#1811177)
- Enable check stage
- Include patch for https://github.com/aliyun/credentials-go/pull/22

* Tue Jul 28 2020 Brandon Perkins <bperkins@redhat.com> - 0.0.1-2
- Update to release 2 (Fixes rhbz#1811177)
- Clean changelog

* Wed Mar 04 2020 Brandon Perkins <bperkins@redhat.com> - 0.0.1-1
- Disable check stage
- Update to version 0.0.1
- Add golang(github.com/alibabacloud-go/tea/tea) BuildRequires

* Fri Nov 22 2019 Brandon Perkins <bperkins@redhat.com> - 0-0.1.20191122gitc03d72d
- Initial package

