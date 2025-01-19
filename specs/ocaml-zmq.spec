# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%global giturl  https://github.com/issuu/ocaml-zmq

Name:           ocaml-zmq
Version:        5.3.0
Release:        7%{?dist}
Summary:        ZeroMQ bindings for OCaml

License:        MIT
URL:            https://engineering.issuu.com/ocaml-zmq/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/%{version}/zmq-%{version}.tbz

BuildRequires:  ocaml >= 4.04.1
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
Requires:       zeromq-devel%{?_isa}

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
%autosetup -n zmq-%{version} -p1

%conf
# We cannot build the async-aware bindings until ocaml-async-kernel and
# ocaml-async-unix have been added to Fedora.
rm -fr zmq-async*

# We cannot build the eio-aware bindings until ocaml-eio and
# ocaml-eio-main have been added to Fedora.
rm -fr zmq-eio*

# Work around for ocaml-zmq 5.2.2.  See if later versions fixed this.
# https://github.com/issuu/ocaml-zmq/issues/128
sed -i 's/sleep 10/&00/' zmq/test/zmq_test.ml

%build
%dune_build

%install
%dune_install -s

# We don't want a fake zmq-async install
rm -fr %{buildroot}%{ocamldir}/zmq-async

# We don't want a fake zmq-eio install
rm -fr %{buildroot}%{ocamldir}/zmq-eio

%check
%dune_check

%files -f .ofiles-zmq
%doc CHANGES.md README.md
%license LICENSE.md

%files devel -f .ofiles-zmq-devel

%files lwt -f .ofiles-zmq-lwt

%files lwt-devel -f .ofiles-zmq-lwt-devel

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jan  9 2025 Jerry James <loganjerry@gmail.com> - 5.3.0-6
- OCaml 5.3.0 rebuild for Fedora 42

* Tue Oct 08 2024 Richard W.M. Jones <rjones@redhat.com> - 5.3.0-5
- Rebuild for ocaml-lwt 5.8.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 19 2024 Richard W.M. Jones <rjones@redhat.com> - 5.3.0-3
- OCaml 5.2.0 ppc64le fix

* Wed May 29 2024 Richard W.M. Jones <rjones@redhat.com> - 5.3.0-2
- OCaml 5.2.0 for Fedora 41

* Thu May 23 2024 Jerry James <loganjerry@gmail.com> - 5.3.0-1
- Version 5.3.0

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 18 2023 Richard W.M. Jones <rjones@redhat.com> - 5.2.2-3
- OCaml 5.1.1 + s390x code gen fix for Fedora 40

* Tue Dec 12 2023 Richard W.M. Jones <rjones@redhat.com> - 5.2.2-2
- OCaml 5.1.1 rebuild for Fedora 40

* Tue Nov 14 2023 Jerry James <loganjerry@gmail.com> - 5.2.2-1
- Version 5.2.2
- Drop upstreamed func-type patch

* Thu Oct 05 2023 Richard W.M. Jones <rjones@redhat.com> - 5.2.1-8
- OCaml 5.1 rebuild for Fedora 40

* Wed Oct  4 2023 Jerry James <loganjerry@gmail.com> - 5.2.1-7
- Bump up sleep values in tests for slower architectures

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Jerry James <loganjerry@gmail.com> - 5.2.1-6
- Add patch to fix test failure on s390x

* Wed Jul 12 2023 Richard W.M. Jones <rjones@redhat.com> - 5.2.1-6
- OCaml 5.0 rebuild for Fedora 39

* Mon Jul 10 2023 Jerry James <loganjerry@gmail.com> - 5.2.1-5
- OCaml 5.0.0 rebuild

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 5.2.1-4
- Bump release and rebuild

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 5.2.1-3
- Rebuild OCaml packages for F38

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

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
