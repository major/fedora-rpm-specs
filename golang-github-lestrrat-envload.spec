%bcond_without check

# https://github.com/lestrrat-go/envload
%global goipath         github.com/lestrrat-go/envload
%global commit          a3eb8ddeffccdbca0eb6dd6cc7c7950c040a6546

%gometa

%global common_description %{expand:
Restore and load environment variables.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.7%{?dist}
Summary:        Restore and load environment variables

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

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
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 26 2022 Brandon Perkins <bperkins@redhat.com> - 0-0.5
- Tests build requires "golang(github.com/stretchr/testify/assert)"

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 17 2021 Brandon Perkins <bperkins@redhat.com> - 0-0.2
- Update to git commit a3eb8dd (Fixes rhbz#1960878)

* Wed May 12 2021 Brandon Perkins <bperkins@redhat.com> - 0-0.1.20210512gita3eb8dd
- Initial package

