%bcond_without check

# https://github.com/alibabacloud-go/tea
%global goipath         github.com/alibabacloud-go/tea
Version:                1.1.17

%gometa

%global common_description %{expand:
Alibaba Cloud (Aliyun) support for TEA OpenAPI DSL.}

%global golicenses      LICENSE
%global godocs          README-CN.md README.md

Name:           %{goname}
Release:        7%{?dist}
Summary:        Alibaba Cloud (Aliyun) support for TEA OpenAPI DSL

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/alibabacloud-go/debug/debug)
BuildRequires:  golang(github.com/json-iterator/go)
BuildRequires:  golang(github.com/modern-go/reflect2)
BuildRequires:  golang(golang.org/x/net/proxy)

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%ifarch armv7hl i686
# Skip 'tea' tests due to 64-bit tests that will fail
%gocheck -d 'tea'
%else
%gocheck
%endif
%endif

%gopkgfiles

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.17-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 17 2022 Robert-André Mauchin <zebob.m@gmail.com> - 1.1.17-5
- Rebuilt for CVE-2022-1996, CVE-2022-24675, CVE-2022-28327, CVE-2022-27191,
  CVE-2022-29526, CVE-2022-30629

* Wed Jan 26 2022 Brandon Perkins <bperkins@redhat.com> - 1.1.17-4
- remove 'unset LDFLAGS' with fix to redhat-rpm-config

* Thu Jan 20 2022 Brandon Perkins <bperkins@redhat.com> - 1.1.17-3
- don't use LDFLAGS='-Wl,-z relro ' from redhat-rpm-config to avoid error:
  "flag provided but not defined: -Wl,-z,relro"

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 16 2021 Brandon Perkins <bperkins@redhat.com> - 1.1.17-1
- Update to version 1.1.17 (Fixes rhbz#1985269)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Brandon Perkins <bperkins@redhat.com> - 1.1.16-1
- Update to version 1.1.16 (Fixes rhbz#1962194)

* Wed Jan 27 2021 Brandon Perkins <bperkins@redhat.com> - 1.1.15-1
- Update to version 1.1.15 (Fixes rhbz#1920813)
- Add new golang(github.com/json-iterator/go) and
  golang(github.com/modern-go/reflect2) BuildRequires
- Skip 'tea' tests due to 64-bit tests that will fail

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 21 2021 Brandon Perkins <bperkins@redhat.com> - 1.1.14-1
- Update to version 1.1.14 (Fixes rhbz#1917438)

* Wed Jan  6 2021 Brandon Perkins <bperkins@redhat.com> - 1.1.13-1
- Update to version 1.1.13 (Fixes rhbz#1913305)

* Mon Nov 30 2020 Brandon Perkins <bperkins@redhat.com> - 1.1.12-1
- Update to version 1.1.12 (Fixes rhbz#1902686)

* Mon Oct 19 2020 Brandon Perkins <bperkins@redhat.com> - 1.1.11-1
- Update to version 1.1.11 (Fixes rhbz#1889458)

* Tue Sep 08 2020 Brandon Perkins <bperkins@redhat.com> - 1.1.10-1
- Update to version 1.1.10 (Fixes rhbz#1876623)

* Sun Aug 23 2020 Brandon Perkins <bperkins@redhat.com> - 1.1.8-1
- Update to version 1.1.8 (Fixes rhbz#1871444)

* Sun Aug 02 2020 Brandon Perkins <bperkins@redhat.com> - 1.1.7-2
- Update summary and description for clarity and consistency

* Tue Jul 28 2020 Brandon Perkins <bperkins@redhat.com> - 1.1.7-1
- Update to version 1.1.7 (Fixes rhbz#1811174)
- Enable check stage
- Clean changelog

* Thu Mar 05 2020 Brandon Perkins <bperkins@redhat.com> - 0.0.7-1
- Initial package

