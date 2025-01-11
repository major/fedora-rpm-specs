# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           prooftree
Version:        0.14
Release:        5%{?dist}
Summary:        Proof tree visualization for Proof General

License:        GPL-3.0-or-later
URL:            https://askra.de/software/prooftree/
VCS:            git:%{url}.git
Source:         %{url}/releases/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-lablgtk-devel
BuildRequires:  ocaml-ocamldoc

%description
Prooftree is a program for proof-tree visualization during interactive
proof development in a theorem prover.  It is currently being developed
for Coq and Proof General.  Prooftree helps against getting lost between
different subgoals in interactive proof development.  It clearly shows
where the current subgoal comes from and thus helps in developing the
right plan for solving it.

Prooftree uses different colors for the already proven subgoals, the
current branch in the proof and the still open subgoals.  Sequent texts
are not displayed in the proof tree itself, but they are shown as a
tool-tip when the mouse rests over a sequent symbol.  Long proof
commands are abbreviated in the tree display, but show up in full length
as tool-tip.  Both, sequents and proof commands, can be shown in the
display below the tree (on single click) or in a separate window (on
double or shift-click).

Prooftree can mark the proof command that introduced a certain
existential variable and thus help to locate the problem when Coq says:
No more subgoals but non-instantiated existential variables.

%prep
%autosetup

# Preserve timestamps when installing
sed -i 's/cp /cp -p /' Makefile.in

# Adapt to OCaml 5.x
sed -i 's/-I \$(LABLGTKDIR)/& -I +unix/' Makefile.in

%build
# Not an autoconf-generated script.  Do not use %%configure.
./configure --prefix %{_prefix}
%make_build

%install
%make_install

%files
%license COPYING
%doc README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Fri Jan 10 2025 Jerry James <loganjerry@gmail.com> - 0.14-5
- OCaml 5.3.0 rebuild for Fedora 42

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 19 2024 Richard W.M. Jones <rjones@redhat.com> - 0.14-3
- OCaml 5.2.0 ppc64le fix

* Wed May 29 2024 Richard W.M. Jones <rjones@redhat.com> - 0.14-2
- OCaml 5.2.0 for Fedora 41

* Thu May 23 2024 Jerry James <loganjerry@gmail.com> - 0.14-1
- Version 0.14

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 18 2023 Richard W.M. Jones <rjones@redhat.com> - 0.13-29
- OCaml 5.1.1 + s390x code gen fix for Fedora 40

* Tue Dec 12 2023 Richard W.M. Jones <rjones@redhat.com> - 0.13-28
- OCaml 5.1.1 rebuild for Fedora 40

* Thu Oct 05 2023 Richard W.M. Jones <rjones@redhat.com> - 0.13-27
- OCaml 5.1 rebuild for Fedora 40

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Richard W.M. Jones <rjones@redhat.com> - 0.13-25
- OCaml 5.0 rebuild for Fedora 39

* Mon Jul 10 2023 Jerry James <loganjerry@gmail.com> - 0.13-24
- OCaml 5.0.0 rebuild

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 0.13-23
- Rebuild OCaml packages for F38

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 12 2022 Jerry James <loganjerry@gmail.com> - 0.13-21
- Convert License tag to SPDX

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jun 18 2022 Richard W.M. Jones <rjones@redhat.com> - 0.13-20
- OCaml 4.14.0 rebuild

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 0.13-19
- OCaml 4.13.1 rebuild to remove package notes

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 04 2021 Richard W.M. Jones <rjones@redhat.com> - 0.13-17
- OCaml 4.13.1 build

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 22 2021 Jerry James <loganjerry@gmail.com> - 0.13-15
- Rebuild for ocaml-lablgtk without gnomeui

* Mon Mar  1 15:56:07 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 0.13-14
- OCaml 4.12.0 build

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 0.13-12
- OCaml 4.11.1 rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-11
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan  3 2017 Jerry James <loganjerry@gmail.com> - 0.13-1
- New upstream version
- Drop all patches; all upstreamed

* Wed Oct 26 2016 Jerry James <loganjerry@gmail.com> - 0.12-1
- Initial RPM
