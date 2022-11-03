%undefine _package_note_flags

Name:           ocaml-time-now
Version:        0.15.0
Release:        9%{?dist}
Summary:        Get the current time in OCaml

License:        MIT
URL:            https://github.com/janestreet/time_now
Source0:        %{url}/archive/v%{version}/time_now-%{version}.tar.gz

BuildRequires:  ocaml >= 4.08.0
BuildRequires:  ocaml-base-devel >= 0.15
BuildRequires:  ocaml-dune >= 2.0.0
BuildRequires:  ocaml-jane-street-headers-devel >= 0.15
BuildRequires:  ocaml-jst-config-devel >= 0.15
BuildRequires:  ocaml-ppx-base-devel >= 0.15
BuildRequires:  ocaml-ppx-optcomp-devel >= 0.15

%description
This package provides a single OCaml function to report the current time
in nanoseconds since the start of the Unix epoch.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-base-devel%{?_isa}
Requires:       ocaml-jane-street-headers-devel
Requires:       ocaml-ppx-compare-devel%{?_isa}
Requires:       ocaml-ppx-enumerate-devel%{?_isa}
Requires:       ocaml-ppx-hash-devel%{?_isa}
Requires:       ocaml-ppx-sexp-conv-devel%{?_isa}
Requires:       ocaml-sexplib0-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n time_now-%{version}

%build
%dune_build

# Relink the stublibs with Fedora link flags
cd _build/default/src
ocamlmklib -g -ldopt '%{build_ldflags}' -o time_now_stubs \
  $(ar t libtime_now_stubs.a)
cd -

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
* Tue Nov  1 2022 Jerry James <loganjerry@gmail.com> - 0.15.0-9
- Rebuild for ocaml-ppxlib 0.28.0

* Thu Aug 18 2022 Jerry James <loganjerry@gmail.com> - 0.15.0-8
- Rebuild for ocaml-ppxlib 0.27.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Jerry James <loganjerry@gmail.com> - 0.15.0-6
- Use new OCaml macros

* Sun Jun 19 2022 Richard W.M. Jones <rjones@redhat.com> - 0.15.0-6
- OCaml 4.14.0 rebuild

* Mon Feb 28 2022 Jerry James <loganjerry@gmail.com> - 0.15.0-5
- Version 0.15.0 rerelease

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 0.15.0-4
- OCaml 4.13.1 rebuild to remove package notes

* Thu Feb  3 2022 Jerry James <loganjerry@gmail.com> - 0.15.0-3
- Conditionally build docs to avoid circular dependency on odoc

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 27 2021 Jerry James <loganjerry@gmail.com> - 0.15.0-2
- Rebuild for ocaml-ppxlib 0.24.0

* Tue Nov 30 2021 Jerry James <loganjerry@gmail.com> - 0.15.0-1
- Version 0.15.0

* Tue Oct 05 2021 Richard W.M. Jones <rjones@redhat.com> - 0.14.0-12
- OCaml 4.13.1 build

* Wed Sep  1 2021 Jerry James <loganjerry@gmail.com> - 0.14.0-11
- Rebuild for ocaml-ppxlib 0.23.0

* Tue Aug 17 2021 Jerry James <loganjerry@gmail.com> - 0.14.0-10
- Rebuild for ocaml-ppx-optcomp 0.14.3

* Thu Jul 29 2021 Jerry James <loganjerry@gmail.com> - 0.14.0-9
- Rebuild for ocaml-ppxlib 0.22.2

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar  2 10:21:39 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 0.14.0-7
- OCaml 4.12.0 build

* Sat Feb 20 2021 Jerry James <loganjerry@gmail.com> - 0.14.0-6
- Rebuild for ocaml-base 0.14.1

* Tue Feb  2 2021 Richard W.M. Jones <rjones@redhat.com> - 0.14.0-5
- Bump and rebuild for updated ocaml Dynlink dependency.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 0.14.0-3
- OCaml 4.11.1 rebuild

* Mon Aug 24 2020 Richard W.M. Jones <rjones@redhat.com> - 0.14.0-2
- OCaml 4.11.0 rebuild

* Mon Jun 22 2020 Jerry James <loganjerry@gmail.com> - 0.14.0-1
- Initial RPM
