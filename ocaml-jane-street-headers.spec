# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%global srcname jane-street-headers

# This package creates no ELF files, but cannot be noarch since the install
# location is under _libdir.
%global debug_package %{nil}

Name:           ocaml-%{srcname}
Version:        0.16.0
Release:        3%{?dist}
Summary:        Jane Street header files

License:        MIT
URL:            https://github.com/janestreet/jane-street-headers
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  ocaml >= 4.14.0
BuildRequires:  ocaml-dune >= 2.0.0

%description
This package contains C header files shared between various Jane Street
packages.

%package        devel
Summary:        Development files for %{name}

%description    devel
This package contains C header files shared between various Jane Street
packages.

%prep
%autosetup -n %{srcname}-%{version}

%build
%dune_build

%install
%dune_install

# The generated jane_street_headers.ml file is empty, and so the rest of the
# compiled OCaml artifacts likewise contain nothing useful.  No consumers need
# them either; we remove them.
rm -f %{buildroot}%{ocamldir}/%{srcname}/*.{cma,cmi,cmt,cmx,cmxa,cmxs,ml}

# Removing those artifacts means we also need to remove references to them
sed -ri '/(archive|plugin)/d' \
        %{buildroot}%{ocamldir}/%{srcname}/{dune-package,META}

%files devel
%doc README.org
%license LICENSE.md
%{ocamldir}/%{srcname}/

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Richard W.M. Jones <rjones@redhat.com> - 0.16.0-2
- OCaml 5.0 rebuild for Fedora 39

* Mon Jul 10 2023 Jerry James <loganjerry@gmail.com> - 0.16.0-1
- Version 0.16.0

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 0.15.0-8
- Rebuild OCaml packages for F38

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Jerry James <loganjerry@gmail.com> - 0.15.0-5
- Use new OCaml macros

* Sat Jun 18 2022 Richard W.M. Jones <rjones@redhat.com> - 0.15.0-5
- OCaml 4.14.0 rebuild

* Mon Feb 28 2022 Jerry James <loganjerry@gmail.com> - 0.15.0-4
- Version 0.15.0 rerelease

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 0.15.0-3
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 30 2021 Jerry James <loganjerry@gmail.com> - 0.15.0-1
- Version 0.15.0

* Mon Oct 04 2021 Richard W.M. Jones <rjones@redhat.com> - 0.14.0-7
- OCaml 4.13.1 build

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar  1 17:37:12 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 0.14.0-5
- OCaml 4.12.0 build

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 0.14.0-3
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 0.14.0-2
- OCaml 4.11.0 rebuild

* Thu Jun 18 2020 Jerry James <loganjerry@gmail.com> - 0.14.0-1
- Initial RPM
