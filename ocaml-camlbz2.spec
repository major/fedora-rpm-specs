%undefine _package_note_flags

Name:           ocaml-camlbz2
Version:        0.7.0
Release:        7%{?dist}
Summary:        OCaml bindings for bzip2

# The usual OCaml linking exception applies
License:        LGPLv2+ with exceptions
URL:            https://gitlab.com/irill/camlbz2
Source0:        %{url}/-/archive/%{version}/camlbz2-%{version}.tar.gz
# Generate useful debuginfo
Patch0:         %{name}-debuginfo.patch
# Use Stdlib instead of the deprecated Pervasives
Patch1:         %{name}-pervasives.patch
# Make the C code const-correct
# https://gitlab.com/irill/camlbz2/-/merge_requests/1
Patch2:         %{name}-const.patch
# Unbundle the OCaml io.h header file
Patch3:         %{name}-io-h.patch

BuildRequires:  automake
BuildRequires:  make
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  python3

%description
This package contains OCaml bindings for bzip2.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       bzip2-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n camlbz2-%{version} -p1

# Generate the configure script
autoreconf -fi -I .

# Make sure we don't use the bundled copy of io.h
rm io.h

%build
%configure
# FIXME: parallel builds often fail due to missing dependencies
make
make doc

%install
# %%make_install sets the wrong DESTDIR
export OCAMLFIND_DESTDIR=%{buildroot}%{ocamldir}
mkdir -p $OCAMLFIND_DESTDIR/stublibs
make install DESTDIR=$OCAMLFIND_DESTDIR INSTALL='%{_bindir}/install -p'

%ocaml_files

# This does not work because it requires a missing test.ml file
#%%check
#make test

%files -f .ofiles
%doc BUGS ChangeLog README
%license COPYING LICENSE

%files devel -f .ofiles-devel
%doc doc/*

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Jerry James <loganjerry@gmail.com> - 0.7.0-6
- Use new OCaml macros

* Sat Jun 18 2022 Richard W.M. Jones <rjones@redhat.com> - 0.7.0-6
- OCaml 4.14.0 rebuild

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 0.7.0-5
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct 05 2021 Richard W.M. Jones <rjones@redhat.com> - 0.7.0-3
- OCaml 4.13.1 build

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Apr 16 2021 Jerry James <loganjerry@gmail.com> - 0.7.0-1
- Initial package
