# Generated by go2rpm
%bcond_without check

# https://github.com/google/martian
%global goipath         github.com/google/martian
Version:                3.1.0

%global goaltipaths     github.com/google/martian/v3

%gometa

%global common_description %{expand:
Martian Proxy is a programmable HTTP proxy designed to be used for testing.

Martian is a great tool to use if you want to:

 - Verify that all (or some subset) of requests are secure
 - Mock external services at the network layer
 - Inject headers, modify cookies or perform other mutations of HTTP requests
   and responses
 - Verify that pingbacks happen when you think they should
 - Unwrap encrypted traffic (requires install of CA certificate in browser)

By taking advantage of Go cross-compilation, Martian can be deployed anywhere
that Go can target.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        20%{?dist}
Summary:        Library for building custom HTTP/S proxies

# Upstream license specification: Apache-2.0
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            %{gourl}
Source0:        %{gosource}
# https://github.com/google/martian/issues/309
Patch0:         0001-Bypass-flag.Parse-in-init.patch

BuildRequires:  golang(golang.org/x/net/websocket)

%description
%{common_description}

%gopkg

%prep
%goprep
%patch -P0 -p1

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
# https://github.com/google/martian/issues/271
# cmd/proxy: needs network
%gocheck -t marbl -t static -d body -d cmd/proxy -d trafficshape
%endif

%files
%license %{golicenses}
%doc %{godocs}
%{_bindir}/*

%gopkgfiles

%changelog
* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 3.1.0-18
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 11 2024 Maxwell G <maxwell@gtmx.me> - 3.1.0-16
- Rebuild for golang 1.22.0

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Maxwell G <gotmax@e.email> - 3.1.0-10
- Rebuild for CVE-2022-{1705,32148,30631,30633,28131,30635,30632,30630,1962} in
  golang

* Sat Jun 18 2022 Robert-André Mauchin <zebob.m@gmail.com> - 3.1.0-9
- Rebuilt for CVE-2022-1996, CVE-2022-24675, CVE-2022-28327, CVE-2022-27191,
  CVE-2022-29526, CVE-2022-30629

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 19 01:27:35 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 3.1.0-1
- Update to 3.1.0
- Close: rhbz#1889552

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 22 17:58:38 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 3.0.0-4
- Add alternate goipath

* Fri Jan 31 16:35:28 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 3.0.0-3
- Fix FTBFS with Go 1.13+

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 22:59:12 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 3.0.0-1
- Release 3.0.0

* Tue Apr 23 10:11:39 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 2.1.0-3
- Update to new packaging

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 05 2018 Robert-André Mauchin <zebob.m@gmail.com> - 2.1.0-1
- First package for Fedora
