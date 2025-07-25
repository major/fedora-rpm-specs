# Generated by go2rpm 1
%bcond_without check

# https://github.com/projectdiscovery/httpx
%global goipath         github.com/projectdiscovery/httpx
Version:                1.0.2

%gometa

%global common_description %{expand:
Httpx is a fast and multi-purpose HTTP toolkit allow to run multiple probers
using retryablehttp library, it is designed to maintain the result reliability
with increased threads.}

%global golicenses      LICENSE.md
%global godocs          README.md

Name:           %{goname}
Release:        10%{?dist}
Summary:        Fast and multi-purpose HTTP toolkit

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/coocood/freecache)
BuildRequires:  golang(github.com/hbakhtiyor/strsim)
BuildRequires:  golang(github.com/logrusorgru/aurora)
BuildRequires:  golang(github.com/microcosm-cc/bluemonday)
BuildRequires:  golang(github.com/miekg/dns)
BuildRequires:  golang(github.com/projectdiscovery/cdncheck)
BuildRequires:  golang(github.com/projectdiscovery/fdmax/autofdmax)
BuildRequires:  golang(github.com/projectdiscovery/gologger)
BuildRequires:  golang(github.com/projectdiscovery/mapcidr)
BuildRequires:  golang(github.com/projectdiscovery/rawhttp)
BuildRequires:  golang(github.com/projectdiscovery/retryablehttp-go)
BuildRequires:  golang(github.com/remeh/sizedwaitgroup)
BuildRequires:  golang(github.com/rs/xid)
BuildRequires:  golang(golang.org/x/net/html)
BuildRequires:  golang(golang.org/x/net/http2)
BuildRequires:  golang(golang.org/x/text/encoding/simplifiedchinese)
BuildRequires:  golang(golang.org/x/text/encoding/traditionalchinese)
BuildRequires:  golang(golang.org/x/text/transform)

%description
%{common_description}

%gopkg

%prep
%goprep

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE.md
%doc README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 22 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.2-1
- Initial package