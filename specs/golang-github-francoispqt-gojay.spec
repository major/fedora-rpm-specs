# Generated by go2rpm 1
%ifnarch %{ix86} %{arm}
%bcond_without check
%endif

# https://github.com/francoispqt/gojay
%global goipath         github.com/francoispqt/gojay
Version:                1.2.13

%gometa

%global common_description %{expand:
GoJay is a performant JSON encoder/decoder for Golang (currently the most
performant, see benchmarks).

It has a simple API and doesn't use reflection. It relies on small interfaces to
decode/encode structures and slices.

Gojay also comes with powerful stream decoding features and an even faster
Unsafe API.}

%global golicenses      LICENSE
%global godocs          examples README.md

Name:           %{goname}
Release:        16%{?dist}
Summary:        Fastest JSON encoder/decoder with powerful stream API for Golang

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/go-errors/errors)
BuildRequires:  golang(github.com/mailru/easyjson)
BuildRequires:  golang(github.com/mailru/easyjson/jlexer)
BuildRequires:  golang(github.com/mailru/easyjson/jwriter)
BuildRequires:  golang(github.com/viant/toolbox)
BuildRequires:  golang(github.com/viant/toolbox/url)
BuildRequires:  golang(golang.org/x/net/websocket)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/buger/jsonparser)
BuildRequires:  golang(github.com/json-iterator/go)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
BuildRequires:  golang(github.com/viant/assertly)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%build
for cmd in gojay; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck -d gojay/codegen/test/embedded_struct
%endif

%files
%license LICENSE
%doc gojay/README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.13-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 11 2024 Maxwell G <maxwell@gtmx.me> - 1.2.13-15
- Rebuild for golang 1.22.0

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.13-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.13-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.13-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.13-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug 10 2022 Maxwell G <gotmax@e.email> - 1.2.13-10
- Rebuild to fix FTBFS

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.13-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Maxwell G <gotmax@e.email> - 1.2.13-8
- Rebuild for CVE-2022-{1705,32148,30631,30633,28131,30635,30632,30630,1962} in
  golang

* Sat Jun 18 2022 Robert-André Mauchin <zebob.m@gmail.com> - 1.2.13-7
- Rebuilt for CVE-2022-1996, CVE-2022-24675, CVE-2022-28327, CVE-2022-27191,
  CVE-2022-29526, CVE-2022-30629

* Sat Apr 16 2022 Fabio Alessandro Locati <me@fale.io> - 1.2.13-6
- Rebuilt for CVE-2022-27191

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Feb 13 01:23:04 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.2.13-1
- Initial package