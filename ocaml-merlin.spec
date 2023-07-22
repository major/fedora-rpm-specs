# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%global ocamlver 500

Name:           ocaml-merlin
Version:        4.9
Release:        3%{?dist}
Summary:        Context sensitive completion for OCaml

# The entire source is MIT except:
# QPL:
# - src/ocaml/driver/pparse.ml{,i}
# - src/ocaml/preprocess/lexer_ident.mll
# - src/ocaml/preprocess/lexer_raw.ml{i,l}
# LGPL-2.1-only WITH OCaml-LGPL-linking-exception
# - src/ocaml/preprocess/parser_raw.mly
# - upstream/ocaml_413/parsing/parser.mly
# - upstream/ocaml_413/utils/domainstate.ml{,i}.c
# - upstream/ocaml_414/parsing/parser.mly
# - upstream/ocaml_414/utils/domainstate.ml{,i}.c
License:        MIT AND QPL-1.0 AND LGPL-2.1-only WITH OCaml-LGPL-linking-exception
URL:            https://ocaml.github.io/merlin/
Source0:        https://github.com/ocaml/merlin/releases/download/v%{version}-%{ocamlver}/merlin-%{version}-%{ocamlver}.tbz

# Fix the tests to work with /usr/lib64 as well as /usr/lib
Patch0001:      0001-Use-usr-lib64-for-Fedora.patch

BuildRequires:  emacs
BuildRequires:  emacs-auto-complete
BuildRequires:  emacs-company-mode
BuildRequires:  emacs-iedit
BuildRequires:  jq
BuildRequires:  ocaml >= 5.0
BuildRequires:  ocaml-caml-mode
BuildRequires:  ocaml-csexp-devel >= 1.5.1
BuildRequires:  ocaml-dune >= 2.9.0
BuildRequires:  ocaml-findlib-devel >= 1.6.0
BuildRequires:  ocaml-ppxlib-devel
BuildRequires:  ocaml-source
BuildRequires:  ocaml-yojson-devel >= 2.0.0
BuildRequires:  vim-enhanced

Requires:       dot-merlin-reader%{?_isa} = %{version}-%{release}

Recommends:     ocaml-source

%global _desc %{expand:
Merlin is an assistant for editing OCaml code.  It aims to provide the
features available in modern IDEs: error reporting, auto completion,
source browsing and much more.}

%description %_desc

You should also install a package that integrates with your editor of
choice, such as emacs-merlin or vim-merlin.

%package        lib
Summary:        Library access to the merlin protocol
Requires:       ocaml-csexp-devel%{?_isa}

%description    lib
These libraries provides access to low-level compiler interfaces and the
standard higher-level merlin protocol.  The library is provided as-is,
is not thoroughly documented, and its public API might break with any
new release.

%package     -n dot-merlin-reader
License:        MIT
Summary:        Merlin configuration file reader

%description -n dot-merlin-reader
This package contains a helper process that reads .merlin files and gives
the normalized content to merlin.

%package     -n emacs-merlin
License:        MIT
Summary:        Context sensitive completion for OCaml in Emacs
BuildArch:      noarch
Requires:       ocaml-merlin = %{version}-%{release}
Requires:       emacs(bin) >= %{?_emacs_version}%{!?_emacs_version:0}
Requires:       emacs-caml-mode

Recommends:     emacs-auto-complete
Recommends:     emacs-company-mode
Recommends:     emacs-iedit

%description -n emacs-merlin %_desc

This package contains the Emacs interface to merlin.

%package     -n vim-merlin
License:        MIT
Summary:        Context sensitive completion for OCaml in Vim
BuildArch:      noarch
Requires:       ocaml-merlin = %{version}-%{release}
Requires:       vim-filesystem

%description -n vim-merlin %_desc

This package contains the Vim interface to merlin.

%prep
%autosetup -n merlin-%{version}-%{ocamlver} -p1

%build
%dune_build @install

%install
%dune_install -s -n

# Reinstall vim files to Fedora default location
mkdir -p %{buildroot}%{vimfiles_root}
mv %{buildroot}%{_datadir}/merlin/vim/* %{buildroot}%{vimfiles_root}
rm -fr %{buildroot}%{_datadir}/merlin

# Generate the autoload file for the Emacs interface and byte compile
cd %{buildroot}%{_emacs_sitelispdir}
emacs -batch --no-init-file --no-site-file \
  --eval "(progn (setq generated-autoload-file \"$PWD/merlin-autoloads.el\" backup-inhibited t) (update-directory-autoloads \".\"))"
mkdir -p %{buildroot}%{_emacs_sitestartdir}
mv merlin-autoloads.el %{buildroot}%{_emacs_sitestartdir}
%_emacs_bytecompile *.el
cd -

%check
%dune_check

%files
%doc featuremap.* CHANGES.md README.md
%license LICENSE
%{_bindir}/ocamlmerlin
%{_bindir}/ocamlmerlin-server
%{ocamldir}/merlin/

%files lib -f .ofiles-merlin-lib
%license LICENSE

%files -n dot-merlin-reader -f .ofiles-dot-merlin-reader
%license LICENSE

%files -n emacs-merlin
%{_emacs_sitelispdir}/merlin*
%{_emacs_sitestartdir}/merlin-autoloads.el

%files -n vim-merlin
%{vimfiles_root}/*/*

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Richard W.M. Jones <rjones@redhat.com> - 4.9-2
- OCaml 5.0 rebuild for Fedora 39

* Mon Jul 10 2023 Jerry James <loganjerry@gmail.com> - 4.9-1
- Version 4.9
- New ocaml-merlin-lib subpackage

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 4.5-5
- Rebuild OCaml packages for F38

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 12 2022 Jerry James <loganjerry@gmail.com> - 4.5-3
- Convert License tags to SPDX

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Jerry James <loganjerry@gmail.com> - 4.5-2
- Use new OCaml macros

* Sun Jun 19 2022 Richard W.M. Jones <rjones@redhat.com> - 4.5-2
- OCaml 4.14.0 rebuild

* Wed Apr 27 2022 Jerry James <loganjerry@gmail.com> - 4.5-1
- Version 4.5

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 4.4-3
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 23 2021 Jerry James <loganjerry@gmail.com> - 4.4-1
- Version 4.4
- OCaml 4.13 is now fully supported, so drop related patches

* Mon Oct 04 2021 Richard W.M. Jones <rjones@redhat.com> - 4.3.1-2
- OCaml 4.13.1 build

* Tue Jul 27 2021 Jerry James <loganjerry@gmail.com> - 4.3.1-1
- Version 4.3.1
- Drop upstreamed -emacs patch

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Apr 13 2021 Jerry James <loganjerry@gmail.com> - 4.2-1
- Version 4.2
- Drop upstreamed -iedit patch
- Add -emacs patch to fix various Emacs issues
- Add -textrel patch to fix FTBFS on i386

* Fri Mar 26 2021 Jerry James <loganjerry@gmail.com> - 4.1-2
- Fix tests on 64-bit systems with the -test-lib64 patch
- Add -emacs-iedit patch to adapt to recent iedit changes
- Build with auto-complete, company-mode, and caml-mode support
- Add subpackages: dot-merlin-reader, emacs-merlin, and vim-merlin
- Generate autoloads for the Emacs interface

* Mon Mar  1 2021 Richard W.M. Jones <rjones@redhat.com> - 4.1-1
- New upstream version 4.1.
- OCaml 4.12.0 build

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7-0.4.preview1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 3.3.7-0.3.preview1
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 3.3.7-0.2.preview1
- OCaml 4.11.0 rebuild

* Fri Aug  7 2020 Robin Lee <cheeselee@fedoraproject.org> - 3.3.7-0.1.preview1
- Update to 3.3.7-preview1

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.4-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Apr 18 2020 Robin Lee <cheeselee@fedoraproject.org> - 3.3.4-1
- Update to 3.3.4 final

* Tue Mar  3 2020 Robin Lee <cheeselee@fedoraproject.org> - 3.3.4-0.1.preview1
- Update to 3.3.4-preview1, supports OCaml 4.10 (BZ#1799817, BZ#1809312)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec  1 2019 Robin Lee <cheeselee@fedoraproject.org> - 3.3.3-1
- Release 3.3.3 (RHBZ#1778280)
- Fix Release tag (RHBZ#1777835)

* Sat Aug  3 2019 Robin Lee <cheeselee@fedoraproject.org> - 3.3.2-1
- Update to 3.3.2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 28 2019 Robin Lee <cheeselee@fedoraproject.org> - 3.3.1-1
- Update to 3.3.1 (BZ#1703452)

* Sun Mar 31 2019 Robin Lee <cheeselee@fedoraproject.org> - 3.2.2-2
- Fix ocaml library path

* Fri Mar  1 2019 Robin Lee <cheeselee@fedoraproject.org> - 3.2.2-1
- Initial packaging
