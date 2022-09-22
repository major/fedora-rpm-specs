# https://github.com/andybalholm/cascadia
%global goipath         github.com/andybalholm/cascadia
Version:                1.2.0

%gometa

%global common_description %{expand:
The Cascadia package implements CSS selectors for use with the parse trees
produced by the html package.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        8%{?dist}
Summary:        CSS selector library in Go

# Upstream license specification: BSD-2-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(golang.org/x/net/html)

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%check
%gocheck

%gopkgfiles

%changelog
* Mon Jul 25 2022 Maxwell G <gotmax@e.email> - 1.2.0-8
- Remove unneeded empty subpackage

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 17 2022 Robert-André Mauchin <zebob.m@gmail.com> - 1.2.0-6
- Rebuilt for CVE-2022-1996, CVE-2022-24675, CVE-2022-28327, CVE-2022-27191,
  CVE-2022-29526, CVE-2022-30629

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 14 2020 Athos Ribeiro <athoscr@fedoraproject.org> - 1.2.0-1
- Update to latest version

* Sun Feb 16 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.0-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 16 00:06:11 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.0-1
- Release 1.0.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.20161224git349dd02
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20161224git349dd02
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20161224git349dd02
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 11 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0-0.1.20161224git349dd02
- First package for Fedora
