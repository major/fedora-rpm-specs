%undefine _package_note_flags

Name:           ocaml-zmq
Version:        5.2.1
Release:        1%{?dist}
Summary:        ZeroMQ bindings for OCaml

License:        MIT
URL:            https://github.com/issuu/ocaml-zmq
Source0:        %{url}/releases/download/%{version}/zmq-%{version}.tbz

BuildRequires:  ocaml >= 4.03.0
BuildRequires:  ocaml-dune >= 2.7
BuildRequires:  ocaml-dune-configurator-devel
BuildRequires:  ocaml-lwt-devel >= 2.6.0
BuildRequires:  ocaml-ounit2-devel
BuildRequires:  pkgconfig(libzmq)

# This can be removed when F40 reaches EOL
Obsoletes:      ocaml-zmq-doc < 5.1.5-3

%description
This library contains basic OCaml bindings for ZeroMQ.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files
for developing applications that use %{name}.

%package        lwt
Summary:        LWT-aware ZeroMQ bindings for OCaml
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    lwt
This library contains lwt-aware OCaml bindings for ZeroMQ.

%package        lwt-devel
Summary:        Development files for %{name}-lwt
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-lwt%{?_isa} = %{version}-%{release}
Requires:       ocaml-lwt-devel%{?_isa}

%description    lwt-devel
The %{name}-lwt-devel package contains libraries and signature
files for developing applications that use %{name}-lwt.

%prep
%autosetup -n zmq-%{version}

# We cannot build the async-aware bindings until ocaml-async-kernel and
# ocaml-async-unix have been added to Fedora.
rm -fr zmq-async*

%build
%dune_build

# Relink the stublib with Fedora flags
cd _build/default/zmq/src
ocamlmklib -g -ldopt "%{build_ldflags}" -o zmq_stubs \
  $(ar t libzmq_stubs.a) -lzmq
cd -

%install
%dune_install -s

# We don't want a fake zmq-async install
rm -fr %{buildroot}%{ocamldir}/zmq-async

%check
%dune_check

%files -f .ofiles-zmq
%doc CHANGES.md README.md
%license LICENSE.md

%files devel -f .ofiles-zmq-devel

%files lwt -f .ofiles-zmq-lwt

%files lwt-devel -f .ofiles-zmq-lwt-devel

%changelog
* Wed Nov  2 2022 Jerry James <loganjerry@gmail.com> - 5.2.1-1
- Version 5.2.1

* Sat Oct 29 2022 Jerry James <loganjerry@gmail.com> - 5.2.0-1
- Version 5.2.0
- Drop ocaml-stdint dependency

* Mon Oct 17 2022 Jerry James <loganjerry@gmail.com> - 5.1.5-5
- Rebuild for ocaml-stdint 0.7.1

* Thu Aug 18 2022 Jerry James <loganjerry@gmail.com> - 5.1.5-4
- Rebuild for ocaml-lwt 5.6.1

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Jerry James <loganjerry@gmail.com> - 5.1.5-2
- Use new OCaml macros

* Sun Jun 19 2022 Richard W.M. Jones <rjones@redhat.com> - 5.1.5-2
- OCaml 4.14.0 rebuild

* Thu Mar 24 2022 Jerry James <loganjerry@gmail.com> - 5.1.5-1
- Version 5.1.5

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 5.1.4-3
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct 19 2021 Jerry James <loganjerry@gmail.com> - 5.1.4-1
- Version 5.1.4
- Drop upstreamed ocaml 4.13 patch

* Tue Oct 05 2021 Richard W.M. Jones <rjones@redhat.com> - 5.1.3-14
- OCaml 4.13.1 build

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar  1 23:40:32 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 5.1.3-12
- OCaml 4.12.0 build

* Sat Feb 20 2021 Jerry James <loganjerry@gmail.com> - 5.1.3-12
- Rebuild for changed ocaml-stdint hashes

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec  2 2020 Jerry James <loganjerry@gmail.com> - 5.1.3-9
- Rebuild for ocaml-stdint 0.7.0

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 5.1.3-8
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 5.1.3-7
- OCaml 4.11.0 rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.3-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 5.1.3-4
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Wed Apr 22 2020 Richard W.M. Jones <rjones@redhat.com> - 5.1.3-3
- OCaml 4.11.0 pre-release attempt 2

* Sat Apr 04 2020 Richard W.M. Jones <rjones@redhat.com> - 5.1.3-2
- Update all OCaml dependencies for RPM 4.16.

* Fri Feb  7 2020 Jerry James <loganjerry@gmail.com> - 5.1.3-1
- Initial RPM
