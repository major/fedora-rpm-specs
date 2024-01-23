# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

Name:           ocaml-mtime
Version:        2.0.0
Release:        8%{?dist}
Summary:        Monotonic wall-clock time for OCaml

License:        ISC
URL:            https://erratique.ch/software/mtime
Source0:        %{url}/releases/mtime-%{version}.tbz

BuildRequires:  ocaml >= 4.08.0
BuildRequires:  ocaml-compiler-libs
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-rpm-macros
BuildRequires:  ocaml-topkg-devel >= 1.0.3
BuildRequires:  python3

# Do not require ocaml-compiler-libs at runtime
%global __ocaml_requires_opts -i Asttypes -i Build_path_prefix_map -i Cmi_format -i Env -i Ident -i Identifiable -i Load_path -i Location -i Longident -i Misc -i Outcometree -i Parsetree -i Path -i Primitive -i Shape -i Subst -i Toploop -i Type_immediacy -i Types -i Warnings

%description
Mtime has platform independent support for monotonic wall-clock time in
pure OCaml.  This time increases monotonically and is not subject to
operating system calendar time adjustments.  The library has types to
represent nanosecond precision timestamps and time spans.

The additional Mtime_clock library provide access to a system
monotonic clock.

Mtime has no dependencies.  Mtime_clock depends on your system library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n mtime-%{version}

# link with the math library
echo $'\ntrue: cclib(-lm)' >> _tags

%build
ocaml pkg/pkg.ml build --dev-pkg false --tests true

%install
%ocaml_install

%check
ocaml pkg/pkg.ml test

%files -f .ofiles
%doc CHANGES.md README.md
%license LICENSE.md

%files devel -f .ofiles-devel
%if %{with docs}
%doc _build/default/_doc/*
%endif

%changelog
* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 18 2023 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-7
- OCaml 5.1.1 + s390x code gen fix for Fedora 40

* Tue Dec 12 2023 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-6
- OCaml 5.1.1 rebuild for Fedora 40

* Thu Oct 05 2023 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-5
- Bump release and rebuild

* Thu Oct 05 2023 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-4
- OCaml 5.1 rebuild for Fedora 40

* Wed Sep 27 2023 Jerry James <loganjerry@gmail.com> - 2.0.0-3
- Use the %%ocaml_install macro

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-2
- OCaml 5.0 rebuild for Fedora 39

* Mon Jul 10 2023 Jerry James <loganjerry@gmail.com> - 2.0.0-1
- Version 2.0.0

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 1.4.0-5
- Rebuild OCaml packages for F38

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Jerry James <loganjerry@gmail.com> - 1.4.0-2
- Link with the math library
- Use new OCaml macros

* Sat Jun 18 2022 Richard W.M. Jones <rjones@redhat.com> - 1.4.0-2
- OCaml 4.14.0 rebuild

* Mon Feb 28 2022 Jerry James <loganjerry@gmail.com> - 1.4.0-1
- Version 1.4.0

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 1.3.0-3
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec  1 2021 Jerry James <loganjerry@gmail.com> - 1.3.0-1
- Initial RPM
