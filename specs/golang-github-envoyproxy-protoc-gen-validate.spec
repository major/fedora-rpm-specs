# Generated by go2rpm 1
%bcond_without check

# https://github.com/envoyproxy/protoc-gen-validate
%global goipath         github.com/envoyproxy/protoc-gen-validate
Version:                0.4.1

%gometa

%global common_description %{expand:
Protoc plugin to generate polyglot message validators.}

%global golicenses      LICENSE NOTICE
%global godocs          CODE_OF_CONDUCT.md requirements.txt\\\
                        rule_comparison.md README.md java/RELEASING.md

Name:           %{goname}
Release:        15%{?dist}
Summary:        Protoc plugin to generate polyglot message validators

# Upstream license specification: Apache-2.0
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/golang/protobuf/proto)
BuildRequires:  golang(github.com/golang/protobuf/protoc-gen-go/descriptor)
BuildRequires:  golang(github.com/golang/protobuf/ptypes)
BuildRequires:  golang(github.com/golang/protobuf/ptypes/any)
BuildRequires:  golang(github.com/golang/protobuf/ptypes/duration)
BuildRequires:  golang(github.com/golang/protobuf/ptypes/timestamp)
BuildRequires:  golang(github.com/golang/protobuf/ptypes/wrappers)
BuildRequires:  golang(github.com/iancoleman/strcase)
BuildRequires:  golang(github.com/lyft/protoc-gen-star)
BuildRequires:  golang(github.com/lyft/protoc-gen-star/lang/go)
BuildRequires:  golang(golang.org/x/net/context)

%description
%{common_description}

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/protoc-gen-validate %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE NOTICE
%doc CODE_OF_CONDUCT.md requirements.txt rule_comparison.md README.md
%doc java/RELEASING.md
%{_bindir}/*

%gopkgfiles

%changelog
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 0.4.1-15
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 11 2024 Maxwell G <maxwell@gtmx.me> - 0.4.1-13
- Rebuild for golang 1.22.0

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Maxwell G <gotmax@e.email> - 0.4.1-7
- Rebuild for CVE-2022-{1705,32148,30631,30633,28131,30635,30632,30630,1962} in
  golang

* Sat Jun 18 2022 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.1-6
- Rebuilt for CVE-2022-1996, CVE-2022-24675, CVE-2022-28327, CVE-2022-27191,
  CVE-2022-29526, CVE-2022-30629

* Sat Apr 16 2022 Fabio Alessandro Locati <me@fale.io> - 0.4.1-5
- Rebuilt for CVE-2022-27191

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Sep 03 20:50:51 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.1-1
- Initial package