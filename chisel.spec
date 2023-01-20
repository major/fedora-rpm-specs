%bcond_without check

# https://github.com/jpillora/chisel
%global goipath         github.com/jpillora/chisel
Version:                1.7.7
%global tag             v1.7.7

%gometa

%global common_description %{expand:
A fast TCP tunnel over HTTP.}

%global godocs          example README.md

Name:           chisel
Release:        6%{?dist}
Summary:        TCP tunnel over HTTP

License:        MIT

URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/armon/go-socks5)
BuildRequires:  golang(github.com/fsnotify/fsnotify)
BuildRequires:  golang(github.com/gorilla/websocket)
BuildRequires:  golang(github.com/jpillora/backoff)
BuildRequires:  golang(github.com/jpillora/requestlog)
BuildRequires:  golang(github.com/jpillora/sizestr)
BuildRequires:  golang(golang.org/x/crypto/ssh)

%description
%{common_description}

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/chisel %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%doc example README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Maxwell G <gotmax@e.email> - 1.7.7-4
- Rebuild for CVE-2022-{1705,32148,30631,30633,28131,30635,30632,30630,1962} in
  golang

* Fri Jun 17 2022 Robert-André Mauchin <zebob.m@gmail.com> - 1.7.7-3
- Rebuilt for CVE-2022-1996, CVE-2022-24675, CVE-2022-28327, CVE-2022-27191,
  CVE-2022-29526, CVE-2022-30629

* Sat Apr 16 2022 Fabio Alessandro Locati <me@fale.io> - 1.7.7-2
- Rebuilt for CVE-2022-27191

* Wed Feb 23 2022 Fabian Affolter <mail@fabian-affolter.ch> - 1.7.7-1
- Update to latest upstream release 1.7.7 (closes rhbz#2048610)

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar 01 2021 Fabian Affolter <mail@fabian-affolter.ch> - 1.7.6-1
- Update to latest upstream release 1.7.6 (#1930557)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 2021 Fabian Affolter <mail@fabian-affolter.ch> - 1.7.4-1
- Update to latest upstream release 1.7.4 (#1916086)

* Wed Nov 25 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.7.3-1
- Update to latest upstream release 1.7.3 (#1898460)

* Sun Oct 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.7.2-1
- Update ot latest upstream release 1.7.2 (#1889172)

* Mon Sep 21 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.7.1-1
- Update ot latest upstream release 1.7.1 (#1880651)

* Fri Sep 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.7.0-1
- Update ot latest upstream release 1.7.0 (#1880651)

* Fri Sep 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.6.0-1
- Update ot latest upstream release 1.6.0

* Fri Jul 31 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.5.0-1
- Update ot latest upstream release 1.5.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Feb 27 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.2-1
- Initial package for Fedora
