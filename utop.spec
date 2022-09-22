%undefine _package_note_flags

# The OCaml code is byte compiled, not native compiled, so there are no ELF
# objects in the binary RPM.
%global debug_package %{nil}

Name:           utop
Version:        2.9.2
Release:        4%{?dist}
Summary:        Improved toplevel for OCaml

License:        BSD-3-Clause
URL:            https://github.com/ocaml-community/utop
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tbz

BuildRequires:  ocaml >= 4.03.0
BuildRequires:  ocaml-camomile-devel
BuildRequires:  ocaml-cppo >= 1.1.2
BuildRequires:  ocaml-dune >= 1.0
BuildRequires:  ocaml-findlib >= 1.7.2
BuildRequires:  ocaml-lambda-term-devel >= 3.1.0
BuildRequires:  ocaml-lwt-react-devel
BuildRequires:  ocaml-react-devel >= 1.0.0

# for utop.el
BuildRequires:  emacs
BuildRequires:  emacs-tuareg

Provides:       ocaml-%{name}%{?_isa} = %{version}-%{release}

%description
utop is an improved toplevel (i.e., Read-Eval-Print Loop) for
OCaml. It can run in a terminal or in Emacs. It supports line
editing, history, real-time and context sensitive completion,
colors, and more.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-findlib%{?_isa}
Requires:       ocaml-lambda-term-devel%{?_isa}

%description devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%package -n emacs-utop
Summary:        Emacs front end for utop
BuildArch:      noarch
Requires:       emacs(bin) >= %{?_emacs_version}%{!?_emacs_version:0}
Requires:       emacs-tuareg
Recommends:     emacs-company

%description -n emacs-utop
This package contains an Emacs front end for utop, an improved toplevel
for OCaml.

%prep
%autosetup

%build
%dune_build

cd src/top
emacs -batch --no-init-file --no-site-file \
    --eval "(progn (setq generated-autoload-file \"$PWD/utop-autoloads.el\" backup-inhibited t) (update-directory-autoloads \".\"))"
%_emacs_bytecompile utop.el
cd -

%install
%dune_install

# Install the Emacs interface
mkdir -p %{buildroot}%{_emacs_sitestartdir}
cp -p src/top/utop-autoloads.* %{buildroot}%{_emacs_sitestartdir}
cp -p src/top/utop.elc %{buildroot}%{_emacs_sitelispdir}

%files -f .ofiles
%license LICENSE
%doc README.md CHANGES.md

%files devel -f .ofiles-devel

%files -n emacs-utop
%{_emacs_sitelispdir}/%{name}.el*
%{_emacs_sitestartdir}/%{name}-autoloads.el*

%changelog
* Thu Aug 18 2022 Jerry James <loganjerry@gmail.com> - 2.9.2-4
- Rebuild for ocaml-lwt 5.6.1
- Convert License tag to SPDX

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Jerry James <loganjerry@gmail.com> - 2.9.2-2
- Use new OCaml macros

* Sun Jun 19 2022 Richard W.M. Jones <rjones@redhat.com> - 2.9.2-2
- OCaml 4.14.0 rebuild

* Thu Jun 16 2022 Jerry James <loganjerry@gmail.com> - 2.9.2-1
- Version 2.9.2

* Wed Apr 27 2022 Jerry James <loganjerry@gmail.com> - 2.9.1-1
- Version 2.9.1

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 2.9.0-3
- OCaml 4.13.1 rebuild to remove package notes

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 10 2021 Jerry James <loganjerry@gmail.com> - 2.9.0-1
- Version 2.9.0

* Tue Oct 05 2021 Richard W.M. Jones <rjones@redhat.com> - 2.8.0-3
- OCaml 4.13.1 build

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 18 2021 Jerry James <loganjerry@gmail.com> - 2.8.0-1
- Version 2.8.0
- New emacs-utop package to hold the Emacs interface

* Thu Jun  3 2021 Richard W.M. Jones <rjones@redhat.com> - 2.7.0-6
- Rebuild for new ocaml-lwt.

* Mon Mar 15 2021 Richard W.M. Jones <rjones@redhat.com> - 2.7.0-5
- Bump and rebuild for updated ocaml-findlib.

* Mon Mar  1 19:52:15 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 2.7.0-4
- OCaml 4.12.0 build

* Sat Feb 20 2021 Jerry James <loganjerry@gmail.com> - 2.7.0-3
- Rebuild for ocaml-lwt 5.4.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 11 2021 Jerry James <loganjerry@gmail.com> - 2.7.0-1
- Version 2.7.0

* Wed Sep 02 2020 Richard W.M. Jones <rjones@redhat.com> - 2.6.0-3
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 2.6.0-2
- OCaml 4.11.0 rebuild

* Fri Aug  7 2020 Jerry James <loganjerry@gmail.com> - 2.6.0-1
- Update to 2.6.0
- Add ocaml-lwt-react-devel and ocaml-react-devel BRs
- Drop unneeded ocaml-bisect-ppx, ocaml-seq, and opam-installer BRs

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 2.4.3-3
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Wed Apr 22 2020 Richard W.M. Jones <rjones@redhat.com> - 2.4.3-2
- OCaml 4.11.0 pre-release attempt 2

* Thu Apr 16 2020 Jerry James <loganjerry@gmail.com> - 2.4.3-1
- Update to 2.4.3
- Add ocaml-bisect-ppx-devel BR
- Remove man page manipulations; they are installed where we want them now

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 05 2019 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.4.2-2
- Require -devel packages of lwt and lambda-term for build step

* Wed Oct 16 2019 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.4.2-1
- Update to 2.4.2

* Mon Aug 12 2019 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.4.1-1
- Update to 2.4.1

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 09 2019 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.3.0-2
- Update build scripts

* Fri Feb 01 2019 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.3.0-1
- Update to 2.3.0

* Mon Dec 03 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.2.0-4
- Update URLs

* Mon Dec 03 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.2.0-3
- Rebuild with lambda-term 1.13

* Sun Aug 12 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.2.0-2
- Fix installing man pages

* Sun Jul 15 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.2.0-1
- Update to 2.2.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr 29 2018 Sergey Avseyev <sergey.avseyev@gmail.com> 2.1.0-2
- Rebuild with findlib 1.8.0

* Mon Mar 05 2018 Sergey Avseyev <sergey.avseyev@gmail.com> 2.1.0-1
- Initial packaging.
