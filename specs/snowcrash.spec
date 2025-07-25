# Generated by go2rpm 1.2
%bcond_without check

# https://github.com/redcode-labs/SNOWCRASH
%global goipath         github.com/redcode-labs/SNOWCRASH
%global commit          49b99ad798a7937d16ceaf5e183555aa498619da

%gometa

%global common_description %{expand:
A polyglot payload generator.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           snowcrash
Version:        0
Release:        0.16%{?dist}
Summary:        Polyglot payload generator

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/akamensky/argparse)
BuildRequires:  golang(github.com/chzyer/readline)
BuildRequires:  golang(github.com/common-nighthawk/go-figure)
BuildRequires:  golang(github.com/fatih/color)
BuildRequires:  golang(github.com/gobuffalo/packr)
BuildRequires:  golang(github.com/olekukonko/tablewriter)

%description
%{common_description}

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/snowcrash %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 11 2024 Maxwell G <maxwell@gtmx.me> - 0-0.13
- Rebuild for golang 1.22.0

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Maxwell G <gotmax@e.email> - 0-0.8
- Rebuild for CVE-2022-{1705,32148,30631,30633,28131,30635,30632,30630,1962} in
  golang

* Sat Jun 18 2022 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.7
- Rebuilt for CVE-2022-1996, CVE-2022-24675, CVE-2022-28327, CVE-2022-27191,
  CVE-2022-29526, CVE-2022-30629

* Sat Apr 16 2022 Fabio Alessandro Locati <me@fale.io> - 0-0.6
- Rebuilt for CVE-2022-27191

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 17 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0-0.2.20200925git49b99ad
- Rename binary in the first place and don't move it (#1888976)

* Fri Oct 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0-0.1.20200925git49b99ad
- Initial package