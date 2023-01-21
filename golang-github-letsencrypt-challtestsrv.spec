%bcond_without check

# https://github.com/letsencrypt/challtestsrv
%global goipath         github.com/letsencrypt/challtestsrv
Version:                1.2.1

%gometa

%global common_description %{expand:
Small TEST-ONLY server for mock DNS & responding to HTTP-01, DNS-01, and TLS-
ALPN-01 ACME challenges.}

%global golicenses      LICENSE
%global godocs          CODE_OF_CONDUCT.md README.md

Name:           %{goname}
Release:        4%{?dist}
Summary:        Small TEST-ONLY server for mock ACME challenges

# Upstream license specification: MPL-2.0
License:        MPLv2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/miekg/dns)

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
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 22 2021 Paul Wouters <paul.wouters@aiven.io> - 1.2.1-1
- Initial package
