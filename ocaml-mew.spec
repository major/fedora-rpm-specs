%undefine _package_note_flags

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-mew
Version:        0.1.0
Release:        16%{?dist}
Summary:        Modal Editing Witch

License:        MIT
URL:            https://github.com/kandu/mew
Source0:        %{url}/archive/%{version}/mew-%{version}.tar.gz
# Expose a dependency on the math library so RPM can see it
Patch0:         %{name}-mathlib.patch

BuildRequires:  ocaml >= 4.02.3
BuildRequires:  ocaml-dune >= 1.1.0
BuildRequires:  ocaml-ppx-expect-devel
BuildRequires:  ocaml-result-devel
BuildRequires:  ocaml-trie-devel >= 1.0.0

%description
This is the core module of mew, a general modal editing engine generator.
You can provide `Key`, `Mode`, and `Concurrent` modules to define the
real world environment to get the core component of a modal editing
engine.  The core component supports recursive key mappings associated
with user provided modes.  After the core component is generated, you may
extended it with a translator to interpret user key sequences to get a
complete modal editing engine.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-result-devel%{?_isa}
Requires:       ocaml-trie-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n mew-%{version} -p1

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%doc CHANGES.md README.md
%license LICENSE

%files devel -f .ofiles-devel

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Jerry James <loganjerry@gmail.com> - 0.1.0-14
- Run the tests
- Add patch to expose a dependency on libm
- Use new OCaml macros

* Sun Jun 19 2022 Richard W.M. Jones <rjones@redhat.com> - 0.1.0-14
- OCaml 4.14.0 rebuild

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 0.1.0-13
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct 05 2021 Richard W.M. Jones <rjones@redhat.com> - 0.1.0-11
- OCaml 4.13.1 build

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 16 2021 Jerry James <loganjerry@gmail.com> - 0.1.0-9
- Move META to the main package (bz 1982933)
- There is no circular dependency so reenable -docs

* Mon Mar  1 15:56:26 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 0.1.0-8
- OCaml 4.12.0 build
- Make documentation conditional.

* Tue Feb  2 2021 Richard W.M. Jones <rjones@redhat.com> - 0.1.0-7
- Bump and rebuild for updated ocaml-camomile dep (RHBZ#1923853).

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 0.1.0-5
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 0.1.0-4
- OCaml 4.11.0 rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 17 2020 Jerry James <loganjerry@gmail.com> - 0.1.0-1
- Initial RPM
