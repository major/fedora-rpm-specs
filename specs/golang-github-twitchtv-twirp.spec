# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/twitchtv/twirp
%global goipath         github.com/twitchtv/twirp
Version:                8.1.0

%gometa

%global common_description %{expand:
A simple RPC framework with protobuf service definitions.}

%global golicenses      LICENSE NOTICE
%global godocs          docs example CONTRIBUTING.md PROTOCOL.md README.md

Name:           %{goname}
Release:        13%{?dist}
Summary:        A simple RPC framework with protobuf service definitions

# Upstream license specification: Apache-2.0
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(google.golang.org/protobuf/encoding/protojson)
BuildRequires:  golang(google.golang.org/protobuf/proto)
BuildRequires:  golang(google.golang.org/protobuf/reflect/protoreflect)
BuildRequires:  golang(google.golang.org/protobuf/runtime/protoimpl)
BuildRequires:  golang(google.golang.org/protobuf/types/descriptorpb)
BuildRequires:  golang(google.golang.org/protobuf/types/known/emptypb)
BuildRequires:  golang(google.golang.org/protobuf/types/known/wrapperspb)
BuildRequires:  golang(google.golang.org/protobuf/types/pluginpb)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
# remove vendored tools
rm -r _tools

%build
for cmd in protoc-gen-twirp clientcompat clientcompat/gocompat; do
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
%license LICENSE NOTICE
%doc docs example CONTRIBUTING.md PROTOCOL.md README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 8.1.0-13
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 11 2024 Maxwell G <maxwell@gtmx.me> - 8.1.0-11
- Rebuild for golang 1.22.0

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Maxwell G <gotmax@e.email> - 8.1.0-5
- Rebuild for CVE-2022-{1705,32148,30631,30633,28131,30635,30632,30630,1962} in
  golang

* Sat Jun 18 2022 Robert-André Mauchin <zebob.m@gmail.com> - 8.1.0-4
- Rebuilt for CVE-2022-1996, CVE-2022-24675, CVE-2022-28327, CVE-2022-27191,
  CVE-2022-29526, CVE-2022-30629

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jun 19 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 8.1.0-1
- Initial package
