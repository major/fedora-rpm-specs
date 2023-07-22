%bcond_without check

# https://github.com/labbsr0x/bindman-dns-webhook
%global goipath         github.com/labbsr0x/bindman-dns-webhook
Version:                1.0.2

%gometa

%global common_description %{expand:
Go library to define the webhook needed by a Bindman DNS Manager in order to
ease out integrations among clients and managers.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        8%{?dist}
Summary:        Go library for Bindman DNS Manager
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/go-errors/errors)
BuildRequires:  golang(github.com/gorilla/mux)
BuildRequires:  golang(github.com/labbsr0x/goh/gohclient)
BuildRequires:  golang(github.com/prometheus/client_golang/prometheus)
BuildRequires:  golang(github.com/prometheus/client_golang/prometheus/promhttp)
BuildRequires:  golang(github.com/sirupsen/logrus)

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
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug 10 2022 Maxwell G <gotmax@e.email> - 1.0.2-6
- Rebuild to fix FTBFS

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 21:14:50 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.2-1
- Update to 1.0.2

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 31 2019 Carl George <carl@george.computer> - 1.0.0-1
- Initial package rhbz#1747627
