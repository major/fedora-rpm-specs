# This package contains generated C header files.  They differ by architecture,
# so this package cannot be noarch, but there are no ELF objects in it.
%global debug_package %{nil}

Name:           ocaml-jst-config
Version:        0.15.1
Release:        4%{?dist}
Summary:        Compile-time configuration for Jane Street libraries

License:        MIT
URL:            https://github.com/janestreet/jst-config
Source0:        %{url}/archive/v%{version}/jst-config-%{version}.tar.gz

BuildRequires:  ocaml >= 4.08.0
BuildRequires:  ocaml-base-devel >= 0.15
BuildRequires:  ocaml-dune-devel >= 2.0.0
BuildRequires:  ocaml-dune-configurator-devel
BuildRequires:  ocaml-ppx-assert-devel >= 0.15

%description
This package defines compile-time constants used in Jane Street libraries
such as Base, Core, and Async.

%package        devel
Summary:        Development files for %{name}

%description    devel
This package defines compile-time constants used in Jane Street libraries
such as Base, Core, and Async.

%prep
%autosetup -n jst-config-%{version}

%build
%dune_build

%install
%dune_install -n

# The generated config_h.ml file is empty, and so the rest of the compiled OCaml
# artifacts likewise contain nothing useful.  No consumers need them either, so
# we remove them.
rm -f %{buildroot}%{ocamldir}/jst-config/*.{a,cma,cmi,cmt,cmx,cmxa,cmxs,ml}

# Removing those artifacts means we also need to remove references to them
sed -ri '/(archive|plugin)/d' \
        %{buildroot}%{ocamldir}/jst-config/{dune-package,META}

%check
%dune_check

%files devel
%license LICENSE.md
%{ocamldir}/jst-config/

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Jerry James <loganjerry@gmail.com> - 0.15.1-2
- Use new OCaml macros

* Sat Jun 18 2022 Richard W.M. Jones <rjones@redhat.com> - 0.15.1-2
- OCaml 4.14.0 rebuild

* Fri Apr 29 2022 Jerry James <loganjerry@gmail.com> - 0.15.1-1
- Version 0.15.1

* Mon Feb 28 2022 Jerry James <loganjerry@gmail.com> - 0.15.0-4
- Version 0.15.0 rerelease

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 0.15.0-3
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 30 2021 Jerry James <loganjerry@gmail.com> - 0.15.0-1
- Version 0.15.0

* Tue Oct 05 2021 Richard W.M. Jones <rjones@redhat.com> - 0.14.1-2
- OCaml 4.13.1 build

* Fri Sep 10 2021 Jerry James <loganjerry@gmail.com> - 0.14.1-1
- Version 0.14.1

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar  2 10:06:44 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 0.14.0-6
- OCaml 4.12.0 build

* Sat Feb 20 2021 Jerry James <loganjerry@gmail.com> - 0.14.0-5
- Rebuild for ocaml-base 0.14.1

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 0.14.0-3
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 0.14.0-2
- OCaml 4.11.0 rebuild

* Fri Jun 19 2020 Jerry James <loganjerry@gmail.com> - 0.14.0-1
- Initial RPM
