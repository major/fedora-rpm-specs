%bcond_without check
%bcond bootstrap 0

%if %{with bootstrap}
%global debug_package %{nil}
%endif

%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif

# https://github.com/jpillora/chisel
%global goipath         github.com/jpillora/chisel
Version:                1.10.1
%global tag             v1.10.1

%gometa

%global common_description %{expand:
A fast TCP tunnel over HTTP.}

%global golicenses      LICENSE
%global godocs          example README.md

Name:           chisel
Release:        2%{?dist}
Summary:        TCP tunnel over HTTP

License:        MIT

URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep -A

%if %{without bootstrap}
%generate_buildrequires
%go_generate_buildrequires
%endif

%if %{without bootstrap}
%build
export LDFLAGS="-X %{import_path}/share.BuildVersion=${version}"
%gobuild -o %{gobuilddir}/bin/chisel %{goipath}
%endif

%install
%gopkginstall
%if %{without bootstrap}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%endif

%if %{without bootstrap}
%if %{with check}
%check
%gocheck
%endif
%endif

%if %{without bootstrap}
%files
%license LICENSE
%doc example README.md
%{_bindir}/chisel
%endif

%gopkgfiles

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Oct 06 2024 Fabian Affolter <mail@fabian-affolter.ch> - 1.10.1-1
- Update to latest upstream release 1.10.1 (closes rhbz#2316742)

* Tue Sep 17 2024 Fabian Affolter <mail@fabian-affolter.ch> - 1.10.0-1
- Update to new upstream version (closes rhbz#2303131)
- Set version (closes rhbz#2265825)
- Fix CVE-2024-43798 (closes rhbz#2308435, closes rhbz#2308436)

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 11 2024 Maxwell G <maxwell@gtmx.me> - 1.9.1-5
- Rebuild for golang 1.22.0

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Sep 09 2023 Filipe Rosset <rosset.filipe@gmail.com> - 1.9.1-2
- Update to 1.9.1 fixes rhbz#2234344

* Sun Aug 20 2023 Filipe Rosset <rosset.filipe@gmail.com> - 1.9.0-1
- Update to 1.9.0 fixes rhbz#2113146 rhbz#2163065 rhbz#2165257

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

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
