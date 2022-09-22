%bcond_without check

# https://github.com/GehirnInc/crypt
%global goipath         github.com/GehirnInc/crypt
%global commit          bb7000b8a962b094f1ddb4ae071dfcbd6490d2e9

%gometa

%global common_description %{expand:
Pure Go crypt(3) Implementation.}

%global golicenses      LICENSE
%global godocs          AUTHORS.md README.rst

Name:           %{goname}
Version:        0
Release:        0.10%{?dist}
Summary:        Pure Go crypt(3) Implementation

# Upstream license specification: BSD-2-Clause
License:        BSD
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
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jan 25 2022 Brandon Perkins <bperkins@redhat.com> - 0-0.9
- Tests build requires "golang(github.com/stretchr/testify/assert)" (Fixes rhbz#2045507)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 15 2020 Brandon Perkins <bperkins@redhat.com> - 0-0.3.20200415gitbb7000b
- New method to check is key has supported format

* Mon Mar 02 2020 Brandon Perkins <bperkins@redhat.com> - 0-0.2.20200302git6c0105a
- Clean changelog

* Wed Nov 13 2019 Brandon Perkins <bperkins@redhat.com> - 0-0.1.20191113git6c0105a
- Initial package

