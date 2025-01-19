# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%global giturl  https://github.com/OCamlPro/ocp-indent

Name:           ocaml-ocp-indent
Version:        1.8.2
Release:        32%{?dist}
Summary:        A simple tool to indent OCaml programs

# The entire source code is LGPL with the OCaml linking exception except
# src/approx_tokens.ml is QPL-1.0
License:        LGPL-2.1-only WITH OCaml-LGPL-linking-exception AND QPL-1.0
URL:            https://www.typerex.org/ocp-indent.html
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/%{version}/ocp-indent-%{version}.tar.gz
# Update the Emacs interface for Emacs 27.1
Patch:          %{name}-emacs.patch
# Fix use of ISO8859-1 characters at the beginnings of lines
# https://github.com/OCamlPro/ocp-indent/issues/318
Patch:          %{name}-nonbreaking-space.patch

BuildRequires:  emacs-nw
BuildRequires:  emacs-tuareg
BuildRequires:  ocaml
BuildRequires:  ocaml-cmdliner-devel >= 1.0.0
BuildRequires:  ocaml-dune >= 1.0
BuildRequires:  ocaml-findlib-devel
BuildRequires:  vim-enhanced

Requires:       emacs-filesystem >= %{?_emacs_version}%{!?_emacs_version:0}
Requires:       vim-filesystem

%description
Ocp-indent is a simple tool and library to indent OCaml code.  It is
based on an approximate, tolerant OCaml parser and a simple stack
machine; this is much faster and more reliable than using regexps.
Presets and configuration options are available, with the possibility to
set them project-wide.  Ocp-indent supports most common syntax
extensions, and is extensible for others.

Includes:

- An indentor program, callable from the command-line or from within
  editors
- Bindings for popular editors
- A library that can be directly used by editor writers, or just for
  fault-tolerant/approximate parsing.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-findlib-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n ocp-indent-%{version} -p1

%build
%dune_build

%install
%dune_install
sed -i '\@%{_datadir}/ocp-indent@d' .ofiles .ofiles-devel

# Reinstall vim files to Fedora default location
mkdir -p %{buildroot}%{vimfiles_root}
mv %{buildroot}%{_datadir}/ocp-indent/vim/* %{buildroot}%{vimfiles_root}
rm -fr %{buildroot}%{_datadir}/ocp-indent

# Generate the autoload file for the Emacs interface and byte compile
cd %{buildroot}%{_emacs_sitelispdir}
emacs -batch --no-init-file --no-site-file \
  --eval "(let ((backup-inhibited t)) (loaddefs-generate \".\" \"$PWD/ocp-indent-loaddefs.el\"))"
mkdir -p %{buildroot}%{_emacs_sitestartdir}
mv ocp-indent-loaddefs.el %{buildroot}%{_emacs_sitestartdir}
%_emacs_bytecompile ocp-indent.el
cd -

%check
#Tests only run on a git checkout
# ./tests/test.sh

%files -f .ofiles
%doc README.md CHANGELOG
%license LICENSE
%{_emacs_sitelispdir}/ocp-indent.elc
%{_emacs_sitestartdir}/ocp-indent-loaddefs.el
%{vimfiles_root}/indent/ocaml.vim

%files devel -f .ofiles-devel

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jan  9 2025 Jerry James <loganjerry@gmail.com> - 1.8.2-31
- OCaml 5.3.0 rebuild for Fedora 42

* Fri Aug  9 2024 Jerry James <loganjerry@gmail.com> - 1.8.2-30
- Generate loaddefs instead of deprecated autoloads

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 19 2024 Richard W.M. Jones <rjones@redhat.com> - 1.8.2-28
- OCaml 5.2.0 ppc64le fix

* Wed May 29 2024 Richard W.M. Jones <rjones@redhat.com> - 1.8.2-27
- OCaml 5.2.0 for Fedora 41

* Fri Feb  2 2024 Jerry James <loganjerry@gmail.com> - 1.8.2-26
- Rebuild for changed ocamlx(Dynlink) hash

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 18 2023 Richard W.M. Jones <rjones@redhat.com> - 1.8.2-23
- OCaml 5.1.1 + s390x code gen fix for Fedora 40

* Tue Dec 12 2023 Richard W.M. Jones <rjones@redhat.com> - 1.8.2-22
- OCaml 5.1.1 rebuild for Fedora 40

* Thu Oct 05 2023 Richard W.M. Jones <rjones@redhat.com> - 1.8.2-21
- OCaml 5.1 rebuild for Fedora 40

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Richard W.M. Jones <rjones@redhat.com> - 1.8.2-19
- OCaml 5.0 rebuild for Fedora 39

* Mon Jul 10 2023 Jerry James <loganjerry@gmail.com> - 1.8.2-18
- OCaml 5.0.0 rebuild

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 1.8.2-17
- Rebuild OCaml packages for F38

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Sep 20 2022 Jerry James <loganjerry@gmail.com> - 1.8.2-15
- Rebuild for ocaml-cmdliner 1.1.1
- Update the Emacs patch for Emacs 28
- Add -nonbreaking-space patch to fix ISO8859-1 output to UTF-8 terminals
- Convert License tag to SPDX

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 28 2022 Jerry James <loganjerry@gmail.com> - 1.8.2-13
- Use new OCaml macros

* Sun Jun 19 2022 Richard W.M. Jones <rjones@redhat.com> - 1.8.2-13
- OCaml 4.14.0 rebuild

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 1.8.2-12
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 04 2021 Richard W.M. Jones <rjones@redhat.com> - 1.8.2-10
- OCaml 4.13.1 build

* Thu Jul 29 2021 Jerry James <loganjerry@gmail.com> - 1.8.2-9
- Rebuild for changed ocamlx(Dynlink)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 19 2021 Jerry James <loganjerry@gmail.com> - 1.8.2-8
- There is no circular dependency so always build docs

* Mon Mar 15 2021 Richard W.M. Jones <rjones@redhat.com> - 1.8.2-7
- Bump and rebuild for updated ocaml-findlib.

* Mon Mar  1 16:57:58 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 1.8.2-6
- OCaml 4.12.0 build
- Make ocaml-odoc dependency conditional.

* Tue Feb 23 2021 Jerry James <loganjerry@gmail.com> - 1.8.2-5
- Spec file cleanup
- Add -emacs patch to adapt to Emacs 27.1
- Build documentation with odoc
- Fix non-Unicode man page
- Generate autoloads for the Emacs interface
- Byte compile the Emacs interface

* Sat Feb 20 2021 Jerry James <loganjerry@gmail.com> - 1.8.2-5
- Rebuild for changed dynlink dependency

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 1.8.2-3
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.8.2-2
- OCaml 4.11.0 rebuild

* Sun Aug  9 2020 Robin Lee <cheeselee@fedoraproject.org> - 1.8.2-1
- Update to 1.8.2

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-13
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 1.7.0-11
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.7.0-10
- OCaml 4.11.0 pre-release attempt 2

* Fri Apr 03 2020 Richard W.M. Jones <rjones@redhat.com> - 1.7.0-9
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 1.7.0-8
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 1.7.0-6
- OCaml 4.10.0+beta1 rebuild.
- Use dune install --destdir option.

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 1.7.0-5
- OCaml 4.09.0 (final) rebuild.

* Wed Sep 18 2019 Richard W.M. Jones <rjones@redhat.com> - 1.7.0-4
- Bump release and rebuild.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Apr  6 2019 Robin Lee <cheeselee@fedoraproject.org> - 1.7.0-2
- Make cmxs files executable to properly generate debuginfo

* Fri Apr  5 2019 Robin Lee <cheeselee@fedoraproject.org> - 1.7.0-1
- Initial packaging

