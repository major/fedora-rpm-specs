%bcond_without check

# https://github.com/lestrrat-go/strftime
%global goipath         github.com/lestrrat-go/strftime
Version:                1.0.5

%gometa

%global common_description %{expand:
Fast strftime for Go.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        5%{?dist}
Summary:        Fast strftime for Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/pkg/errors)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/lestrrat-go/envload)
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
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul 15 2021 Brandon Perkins <bperkins@redhat.com> - 1.0.5-1
- Update to version 1.0.5 (Fixes rhbz#1982390)

* Mon May 17 2021 Brandon Perkins <bperkins@redhat.com> - 1.0.4-2
- Update to version 1.0.4 (Fixes rhbz#1960879)

* Wed May 12 2021 Brandon Perkins <bperkins@redhat.com> - 1.0.4-1
- Initial package

