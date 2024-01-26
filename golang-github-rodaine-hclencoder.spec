%bcond_without check

# https://github.com/rodaine/hclencoder
%global goipath         github.com/rodaine/hclencoder
%global commit          aaa140ee61ed812af9a40790e08803fb3ae1adc0

%gometa

%global common_description %{expand:
HCL Encoder/Marshaller - Convert Go Types into HCL files.}

%global golicenses      LICENSE
%global godocs          readme.md

Name:           %{goname}
Version:        0
Release:        0.9%{?dist}
Summary:        HCL Encoder/Marshaller - Convert Go Types into HCL files

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/hashicorp/hcl/hcl/ast)
BuildRequires:  golang(github.com/hashicorp/hcl/hcl/printer)
BuildRequires:  golang(github.com/hashicorp/hcl/hcl/token)

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
* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 17 2021 Brandon Perkins <bperkins@redhat.com> - 0-0.2
- Update to git commit aaa140e (Fixes rhbz#1960876)

* Wed May 12 2021 Brandon Perkins <bperkins@redhat.com> - 0-0.1.20210512gitaaa140e
- Initial package

