%bcond_without check

# https://github.com/haproxytech/models
%global goipath         github.com/haproxytech/models
Version:                2.2.0

%gometa

# %%global extractdir      %%(echo %%{extractdir} | sed -e 's/~/-/g')
# %%global gosource        %%(echo %%{gosource} | sed -e 's/~/-/g')

%global goaltipaths     %{goipath}/v2

%global common_description %{expand:
HAProxy Go structs for API.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        6%{?dist}
Summary:        HAProxy Go structs for API

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/go-openapi/errors)
BuildRequires:  golang(github.com/go-openapi/strfmt)
BuildRequires:  golang(github.com/go-openapi/swag)
BuildRequires:  golang(github.com/go-openapi/validate)

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
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 17 16:34:07 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 2.2.0-1
- Update to 2.2.0
- Close: rhbz#1916917

* Wed Jan 13 2021 Brandon Perkins <bperkins@redhat.com> - 2.2.0~rc1-2
- Modify gosource so that Source0 resolves correctly  (Fixes rhbz#1914252)

* Tue Jan 12 2021 Brandon Perkins <bperkins@redhat.com> - 2.2.0~rc1-1
- Update to version 2.2.0-rc1 (Fixes rhbz#1914252)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Brandon Perkins <bperkins@redhat.com> - 2.1.0-1
- Update to version 2.1.0 (Fixes rhbz#1859326)

* Mon May 18 2020 Brandon Perkins <bperkins@redhat.com> - 2.0.2-1
- Update to version 2.0.2

* Fri May 08 2020 Brandon Perkins <bperkins@redhat.com> - 2.0.1-1
- Update to version 2.0.1

* Mon Apr 27 2020 Brandon Perkins <bperkins@redhat.com> - 2.0.0-1
- Upgrade to version 2.0.0

* Mon Mar 02 2020 Brandon Perkins <bperkins@redhat.com> - 1.2.4-2
- Clean changelog

* Wed Nov 13 2019 Brandon Perkins <bperkins@redhat.com> - 1.2.4-1
- Initial package

