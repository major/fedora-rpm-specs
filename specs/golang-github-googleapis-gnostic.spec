# Generated by go2rpm
%bcond_without check

# https://github.com/googleapis/gnostic
%global goipath         github.com/googleapis/gnostic
Version:                0.5.3

%gometa

%global common_description %{expand:
This package contains a Go command line tool which converts JSON and YAML
OpenAPI descriptions to and from equivalent Protocol Buffer representations.

Protocol Buffers provide a language-neutral, platform-neutral, extensible
mechanism for serializing structured data. gnostic's Protocol Buffer models for
the OpenAPI Specification can be used to generate code that includes data
structures with explicit fields for the elements of an OpenAPI description. This
makes it possible for developers to work with OpenAPI descriptions in type-safe
ways, which is particularly useful in strongly-typed languages like Go and
Swift.

gnostic reads OpenAPI descriptions into these generated data structures, reports
errors, resolves internal dependencies, and writes the results in a binary form
that can be used in any language that is supported by the Protocol Buffer tools.
A plugin interface simplifies integration with API tools written in a variety of
different languages, and when necessary, Protocol Buffer OpenAPI descriptions
can be reexported as JSON or YAML.

gnostic compilation code and OpenAPI Protocol Buffer models are automatically
generated from an OpenAPI JSON Schema. Source code for the generator is in the
generate-gnostic directory.}

%global golicenses     LICENSE
%global godocs         examples CONTRIBUTING.md README.md README-disco.md\\\
                       README-gnostic-report.md README-petstore-builder.md\\\
                       README-report-messages.md README-generate-gnostic.md

Name:           %{goname}
Release:        18%{?dist}
Summary:        Compiler for APIs described by the OpenAPI Specification

# Upstream license specification: Apache-2.0
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/docopt/docopt-go)
BuildRequires:  golang(github.com/golang/protobuf/jsonpb)
BuildRequires:  golang(github.com/golang/protobuf/proto)
BuildRequires:  golang(github.com/golang/protobuf/ptypes)
BuildRequires:  golang(github.com/golang/protobuf/ptypes/any)
BuildRequires:  golang(github.com/stoewer/go-strcase)
BuildRequires:  golang(google.golang.org/genproto/googleapis/api/annotations)
BuildRequires:  golang(google.golang.org/protobuf/compiler/protogen)
BuildRequires:  golang(google.golang.org/protobuf/proto)
BuildRequires:  golang(google.golang.org/protobuf/reflect/protoreflect)
BuildRequires:  golang(google.golang.org/protobuf/runtime/protoimpl)
BuildRequires:  golang(gopkg.in/yaml.v3)

%if %{with check}
# Tests
BuildRequires:  golang(gopkg.in/check.v1)
BuildRequires:  /usr/bin/protoc
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
mv apps/disco/README.md README-disco.md
mv apps/petstore-builder/README.md README-petstore-builder.md
mv apps/report-messages/README.md README-report-messages.md
mv apps/report/README.md README-gnostic-report.md
mv generate-gnostic/README.md README-generate-gnostic.md

%build
%gobuild -o %{gobuilddir}/bin/gnostic %{goipath}
for cmd in apps/report apps/report-messages apps/petstore-builder generate-gnostic apps/disco; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
mv %{gobuilddir}/bin/report %{gobuilddir}/bin/gnostic-report

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
# Needs network
%gocheck -d . \
         -d apps/protoc-gen-openapi	\
         -d generate-gnostic \
         -d compiler \
         -d extensions \
         -d plugins \
         -d plugins/gnostic-complexity \
         -d plugins/gnostic-vocabulary
%endif

%files
%license LICENSE
%doc examples CONTRIBUTING.md README.md README-disco.md README-gnostic-report.md
%doc README-petstore-builder.md README-report-messages.md
%doc README-generate-gnostic.md
%{_bindir}/*

%gopkgfiles

%changelog
* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 0.5.3-16
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 11 2024 Maxwell G <maxwell@gtmx.me> - 0.5.3-14
- Rebuild for golang 1.22.0

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug 10 2022 Maxwell G <gotmax@e.email> - 0.5.3-9
- Rebuild to fix FTBFS

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Maxwell G <gotmax@e.email> - 0.5.3-7
- Rebuild for CVE-2022-{1705,32148,30631,30633,28131,30635,30632,30630,1962} in
  golang

* Sat Jun 18 2022 Robert-André Mauchin <zebob.m@gmail.com> - 0.5.3-6
- Rebuilt for CVE-2022-1996, CVE-2022-24675, CVE-2022-28327, CVE-2022-27191,
  CVE-2022-29526, CVE-2022-30629

* Sat Apr 16 2022 Fabio Alessandro Locati <me@fale.io> - 0.5.3-5
- Rebuilt for CVE-2022-27191

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 19 02:16:11 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.5.3-1
- Update to 0.5.3
- Close: rhbz#1887628

* Fri Aug 14 01:00:35 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.5.1-1
- Update to 0.5.1

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Apr 14 01:03:04 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.1-1
- Update to 0.4.1

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 09 17:27:45 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.0-1
- Initial package
