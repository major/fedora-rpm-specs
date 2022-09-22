%bcond_without check

# https://github.com/vultr/govultr
%global goipath         github.com/vultr/govultr
Version:                1.1.1

%gometa

%global common_description %{expand:
The official Vultr Go client - GoVultr allows you to interact with the Vultr V1
API.}

%global golicenses      LICENSE
%global godocs          README.md CHANGELOG.md

Name:           %{goname}
Release:        5%{?dist}
Summary:        Vultr Go API client

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/hashicorp/go-retryablehttp)

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
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 16:19:51 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 1.1.1-1
- Update to 1.1.1

* Tue Aug 04 18:23:56 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.2-1
- Update to 0.4.2

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 31 2019 Carl George <carl@george.computer> - 0.1.4-1
- Initial package rhbz#1747623
