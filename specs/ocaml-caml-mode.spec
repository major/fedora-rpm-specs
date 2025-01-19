%global srcname caml-mode

# This package installs into an arch-specific directory, but contains no
# ELF files.
%global debug_package %{nil}

Name:           ocaml-%{srcname}
Version:        4.9
Release:        10%{?dist}
Summary:        Opam file for caml-mode

# GPL-2.0-or-later: the project as a whole
# GPL-1.0-or-later: camldebug.el
License:        GPL-2.0-or-later AND GPL-1.0-or-later
URL:            https://github.com/ocaml/caml-mode
VCS:            git:%{url}.git
Source0:        %{url}/releases/download/%{version}/%{srcname}-%{version}.tgz
# Opam file omitted from recent releases
Source1:        https://raw.githubusercontent.com/ocaml/opam-repository/master/packages/%{srcname}/%{srcname}.%{version}/opam

BuildRequires:  emacs-nw
BuildRequires:  make

Requires:       emacs-%{srcname} = %{version}-%{release}
Requires:       ocaml(runtime)

%description
This package contains the opam file for emacs-%{srcname}.  Install
this only if you want opam to know that caml-mode is available.
If you just want to use caml-mode, install emacs-%{srcname}.

%package     -n emacs-%{srcname}
Summary:        Emacs mode for editing OCaml source code
BuildArch:      noarch
Requires:       emacs(bin) >= %{?_emacs_version}%{!?_emacs_version:0}

%description -n emacs-%{srcname}
This package provides a caml-mode for Emacs, for editing OCaml programs,
as well as an inferior-caml-mode, to run a toplevel.  Caml-mode supports
indentation, compilation and error retrieving, and sending phrases to
the toplevel.  There is also support for hilit, font-lock and imenu.

%prep
%autosetup -n %{srcname}-%{version}

%build
%make_build ocamltags

%install
export INSTALL_BIN=%{buildroot}%{_bindir}
export INSTALL_DIR=%{buildroot}%{_emacs_sitelispdir}/%{srcname}
mkdir -p %{buildroot}%{_bindir}
make install install-ocamltags

# Install the opam file
mkdir -p %{buildroot}%{ocamldir}/%{srcname}
sed '/opam-version/aname: "caml-mode"\nversion: "%{version}"' %{SOURCE1} > \
  %{buildroot}%{ocamldir}/%{srcname}/opam
touch -r %{SOURCE1} %{buildroot}%{ocamldir}/%{srcname}/opam

# Generate autoloads for the emacs interface
mkdir -p %{buildroot}%{_emacs_sitestartdir}
cd %{buildroot}%{_emacs_sitelispdir}/%{srcname}
emacs -batch --no-init-file --no-site-file \
  --eval "(let ((backup-inhibited t)) (loaddefs-generate \".\" \"%{buildroot}%{_emacs_sitestartdir}/caml-mode-loaddefs.el\"))"
cd -

%files
%{ocamldir}/%{srcname}/

%files -n emacs-%{srcname}
%doc CHANGES.md README.itz README.md
%license COPYING
%{_bindir}/ocamltags
%{_emacs_sitelispdir}/%{srcname}/
%{_emacs_sitestartdir}/caml-mode-loaddefs.el

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Aug  9 2024 Jerry James <loganjerry@gmail.com> - 4.9-9
- Generate loaddefs instead of deprecated autoloads

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 12 2022 Jerry James <loganjerry@gmail.com> - 4.9-3
- Convert the License tag to SPDX

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Jerry James <loganjerry@gmail.com> - 4.9-2
- Change emacs BR to emacs-nox
- Use new OCaml macros

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Oct  6 2021 Jerry James <loganjerry@gmail.com> - 4.9-1
- Version 4.9
- Drop upstreamed -emacs patch

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar  9 2021 Jerry James <loganjerry@gmail.com> - 4.06-1
- Initial RPM
