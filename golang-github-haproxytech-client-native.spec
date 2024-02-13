%bcond_without check

# https://github.com/haproxytech/client-native
%global goipath         github.com/haproxytech/client-native
Version:                2.5.3

%gometa

%global goaltipaths     %{goipath}/v2

%global common_description %{expand:
Go client for HAProxy configuration and runtime API.}

%global golicenses      LICENSE
%global godocs          README.md runtime/README.md e2e/README.md\\\
                        specification/README.md specification/copyright.txt

Name:           %{goname}
Release:        10%{?dist}
Summary:        Go client for HAProxy configuration and runtime API

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/go-openapi/errors)
BuildRequires:  golang(github.com/go-openapi/strfmt)
BuildRequires:  golang(github.com/go-openapi/swag)
BuildRequires:  golang(github.com/go-openapi/validate)
BuildRequires:  golang(github.com/google/go-cmp/cmp)
BuildRequires:  golang(github.com/google/renameio)
BuildRequires:  golang(github.com/google/uuid)
BuildRequires:  golang(github.com/haproxytech/config-parser/v4)
BuildRequires:  golang(github.com/haproxytech/config-parser/v4/common)
BuildRequires:  golang(github.com/haproxytech/config-parser/v4/errors)
BuildRequires:  golang(github.com/haproxytech/config-parser/v4/options)
BuildRequires:  golang(github.com/haproxytech/config-parser/v4/params)
BuildRequires:  golang(github.com/haproxytech/config-parser/v4/parsers)
BuildRequires:  golang(github.com/haproxytech/config-parser/v4/parsers/actions)
BuildRequires:  golang(github.com/haproxytech/config-parser/v4/parsers/filters)
BuildRequires:  golang(github.com/haproxytech/config-parser/v4/parsers/http/actions)
BuildRequires:  golang(github.com/haproxytech/config-parser/v4/parsers/stats/settings)
BuildRequires:  golang(github.com/haproxytech/config-parser/v4/parsers/tcp/actions)
BuildRequires:  golang(github.com/haproxytech/config-parser/v4/parsers/tcp/types)
BuildRequires:  golang(github.com/haproxytech/config-parser/v4/spoe)
BuildRequires:  golang(github.com/haproxytech/config-parser/v4/spoe/types)
BuildRequires:  golang(github.com/haproxytech/config-parser/v4/types)
BuildRequires:  golang(github.com/kballard/go-shellquote)
BuildRequires:  golang(github.com/mitchellh/mapstructure)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(gopkg.in/yaml.v2)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
BuildRequires:  golang(github.com/stretchr/testify/suite)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
mv runtime/README.md README-runtime.md
mv e2e/README.md README-e2e.md
mv specification/README.md README-specification.md

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc README.md README-runtime.md README-e2e.md README-specification.md
%doc specification/copyright.txt

%gopkgfiles

%changelog
* Sun Feb 11 2024 Maxwell G <maxwell@gtmx.me> - 2.5.3-10
- Rebuild for golang 1.22.0

* Mon Jan 29 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jun 18 2022 Robert-André Mauchin <zebob.m@gmail.com> - 2.5.3-3
- Rebuilt for CVE-2022-1996, CVE-2022-24675, CVE-2022-28327, CVE-2022-27191,
  CVE-2022-29526, CVE-2022-30629

* Sat Apr 16 2022 Fabio Alessandro Locati <me@fale.io> - 2.5.3-2
- Rebuilt for CVE-2022-27191

* Wed Jan 26 2022 Brandon Perkins <bperkins@redhat.com> - 2.5.3-1
- Update to version 2.5.3 (Fixes rhbz#2039021)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 13 2021 Brandon Perkins <bperkins@redhat.com> - 2.5.2-1
- Update to version 2.5.2 (Fixes rhbz#2029629)

* Mon Nov 01 2021 Brandon Perkins <bperkins@redhat.com> - 2.5.1-1
- Update to version 2.5.1 (Fixes rhbz#2015159)

* Fri Oct 08 2021 Brandon Perkins <bperkins@redhat.com> - 2.4.5-1
- Update to version 2.4.5 (Fixes rhbz#1965745)

* Thu Sep 09 2021 Brandon Perkins <bperkins@redhat.com> - 2.4.4-1
- Update to version 2.4.4 (Fixes rhbz#1965745)

* Tue Aug 10 2021 Brandon Perkins <bperkins@redhat.com> - 2.4.2-2
- Update to version 2.4.2 (Fixes rhbz#1965745)

* Mon Aug 09 2021 Brandon Perkins <bperkins@redhat.com> - 2.4.2-1
- Update to version 2.4.2 (Fixes rhbz#1965745)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 15 2021 Brandon Perkins <bperkins@redhat.com> - 2.4.1-1
- Update to version 2.4.1 (Fixes rhbz#1965745)

* Wed May 12 2021 Brandon Perkins <bperkins@redhat.com> - 2.4.0-1
- Update to version 2.4.0 (Fixes rhbz#1958440)

* Thu Apr 22 2021 Brandon Perkins <bperkins@redhat.com> - 2.3.0-1
- Update to version 2.3.0 (Fixes rhbz#1952232)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 17 16:03:58 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 2.2.0-1
- Update to 2.2.0
- Close: rhbz#1916915

* Wed Jan 13 2021 Brandon Perkins <bperkins@redhat.com> - 2.2.0~rc1-2
- Modify gosource so that Source0 resolves correctly  (Fixes rhbz#1914253)

* Tue Jan 12 2021 Brandon Perkins <bperkins@redhat.com> - 2.2.0~rc1-1
- Update to version 2.2.0-rc1 (Fixes rhbz#1914253)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Brandon Perkins <bperkins@redhat.com> - 2.1.0-1
- Update to version 2.1.0 (Fixes rhbz#1859323)

* Mon May 18 2020 Brandon Perkins <bperkins@redhat.com> - 2.0.2-1
- Update to version 2.0.2

* Fri May 08 2020 Brandon Perkins <bperkins@redhat.com> - 2.0.1-1
- Update to version 2.0.1

* Mon Apr 27 2020 Brandon Perkins <bperkins@redhat.com> - 2.0.0-1
- Upgrade to version 2.0.0

* Wed Apr 15 2020 Brandon Perkins <bperkins@redhat.com> - 1.2.7-1
- Update to version 1.2.7

* Tue Apr 14 2020 Brandon Perkins <bperkins@redhat.com> - 1.2.6-4
- Add specific versions for haproxytech BuildRequires

* Mon Apr 13 2020 Brandon Perkins <bperkins@redhat.com> - 1.2.6-3
- Remove runtime/README.md

* Mon Mar 02 2020 Brandon Perkins <bperkins@redhat.com> - 1.2.6-2
- Clean changelog

* Wed Nov 13 2019 Brandon Perkins <bperkins@redhat.com> - 1.2.6-1
- Initial package

