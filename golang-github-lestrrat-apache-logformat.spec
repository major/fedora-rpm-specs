%bcond_without check

# https://github.com/lestrrat-go/apache-logformat
%global goipath         github.com/lestrrat-go/apache-logformat
Version:                2.0.6

%gometa

%global common_description %{expand:
Port of Perl5's Apache::LogFormat::Compiler to golang.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        7%{?dist}
Summary:        Port of Perl5's Apache::LogFormat::Compiler to golang

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/lestrrat-go/strftime)
BuildRequires:  golang(github.com/pkg/errors)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/facebookgo/clock)
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
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 17 2021 Brandon Perkins <bperkins@redhat.com> - 2.0.6-2
- Update to version 2.0.6 (Fixes rhbz#1960880)

* Wed May 12 2021 Brandon Perkins <bperkins@redhat.com> - 2.0.6-1
- Initial package

