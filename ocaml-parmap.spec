%undefine _package_note_flags

Name:           ocaml-parmap
Version:        1.2.5
Release:        1%{?dist}
Summary:        OCaml library for exploiting multicore architectures

License:        LGPL-2.0-or-later WITH OCaml-LGPL-linking-exception
URL:            https://rdicosmo.github.io/parmap/
Source0:        https://github.com/rdicosmo/parmap/archive/%{version}/parmap-%{version}.tar.gz

BuildRequires:  ocaml >= 4.03.0
BuildRequires:  ocaml-dune >= 2.7
BuildRequires:  ocaml-dune-configurator-devel
BuildRequires:  ocaml-graphics-devel

%description
Parmap is a minimalistic library for exploiting multicore architectures
in OCaml programs with minimal modifications: if you want to use your
many cores to accelerate an operation which happens to be a map, fold or
map/fold (map-reduce), just use Parmap's parmap, parfold and parmapfold
primitives in place of the standard List.map and friends, and specify
the number of subprocesses to use with the optional parameter ~ncores.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n parmap-%{version}

# Some tests exhaust memory on the 32-bit builders; scale them down
# See https://github.com/rdicosmo/parmap/issues/92
%if 0%{?__isa_bits} == 32
sed -i 's/10000000/1000000/' tests/{float,simple}scale.ml
%endif

%build
%dune_build

# Relink the stublibs with $RPM_LD_FLAGS.
cd _build/default/src
ocamlmklib -g -ldopt '%{build_ldflags}' -o parmap_stubs \
  $(ar t libparmap_stubs.a)
cd -

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%doc AUTHORS CHANGES README.md
%license LICENSE

%files devel -f .ofiles-devel

%changelog
* Mon Nov 28 2022 Jerry James <loganjerry@gmail.com> - 1.2.5-1
- Version 1.2.5

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Jerry James <loganjerry@gmail.com> - 1.2.4-5
- Use new OCaml macros

* Sun Jun 19 2022 Richard W.M. Jones <rjones@redhat.com> - 1.2.4-5
- OCaml 4.14.0 rebuild

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 1.2.4-4
- Bump release and rebuild.

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 1.2.4-3
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan  4 2022 Jerry James <loganjerry@gmail.com> - 1.2.4-1
- Version 1.2.4

* Tue Oct 05 2021 Richard W.M. Jones <rjones@redhat.com> - 1.2.3-3
- OCaml 4.13.1 build

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May  3 2021 Jerry James <loganjerry@gmail.com> - 1.2.3-1
- Version 1.2.3

* Wed Apr 28 2021 Jerry James <loganjerry@gmail.com> - 1.2.1-1
- Version 1.2.1
- Drop upstreamed -float-array patch

* Fri Apr 16 2021 Jerry James <loganjerry@gmail.com> - 1.2-1
- Initial package
