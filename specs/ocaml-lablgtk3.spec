# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%global giturl  https://github.com/garrigue/lablgtk

Name:           ocaml-lablgtk3
Version:        3.1.5
Release:        4%{?dist}
Summary:        OCaml interface to gtk3

License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
URL:            https://garrigue.github.io/lablgtk/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/%{version}/lablgtk3-%{version}.tar.gz

BuildRequires:  help2man
BuildRequires:  ocaml >= 4.12.0
BuildRequires:  ocaml-cairo-devel >= 0.6
BuildRequires:  ocaml-camlp-streams-devel >= 5.0
BuildRequires:  ocaml-dune >= 1.8.0
BuildRequires:  ocaml-dune-configurator-devel
BuildRequires:  pkgconfig(goocanvas-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-3.0)
BuildRequires:  pkgconfig(gtkspell3-3.0)
BuildRequires:  pkgconfig(librsvg-2.0)

# This can be removed when F40 reaches EOL
Obsoletes:      ocaml-lablgtk3-doc < 3.1.2-5

%global _description %{expand:
LablGTK3 is an Objective Caml interface to gtk3.  It uses the rich
type system of Objective Caml to provide a strongly typed, yet very
comfortable, object-oriented interface to gtk3.}

%description %_description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gtk3-devel%{?_isa}
Requires:       ocaml-cairo-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%package        goocanvas2
Summary:        OCaml interface to GooCanvas
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    goocanvas2 %_description

This package contains OCaml bindings for the GTK3 GooCanvas library.

%package        goocanvas2-devel
Summary:        Development files for %{name}-goocanvas2
Requires:       %{name}-goocanvas2%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       goocanvas2-devel%{?_isa}

%description    goocanvas2-devel
The %{name}-goocanvas2-devel package contains libraries and signature
files for developing applications that use %{name}-goocanvas2.

%package        gtkspell3
Summary:        OCaml interface to gtkspell3
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    gtkspell3 %_description

This package contains OCaml bindings for gtkspell3.

%package        gtkspell3-devel
Summary:        Development files for %{name}-gtkspell3
Requires:       %{name}-gtkspell3%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       gtkspell3-devel%{?_isa}

%description    gtkspell3-devel
The %{name}-gtkspell3-devel package contains libraries and signature
files for developing applications that use %{name}-gtkspell3.

%package        rsvg2
Summary:        OCaml interface to librsvg2
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    rsvg2 %_description

This package contains OCaml bindings for librsvg2.

%package        rsvg2-devel
Summary:        Development files for %{name}-rsvg2
Requires:       %{name}-rsvg2%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       librsvg2-devel%{?_isa}

%description    rsvg2-devel
The %{name}-rsvg2-devel package contains libraries and signature
files for developing applications that use %{name}-rsvg2.

%package        sourceview3
Summary:        OCaml interface to gtksourceview3
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    sourceview3 %_description

This package contains OCaml bindings for gtksourceview3.

%package        sourceview3-devel
Summary:        Development files for %{name}-sourceview3
Requires:       %{name}-sourceview3%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       gtksourceview3-devel%{?_isa}

%description    sourceview3-devel
The %{name}-sourceview3-devel package contains libraries and signature
files for developing applications that use %{name}-sourceview3.

%prep
%autosetup -n lablgtk-%{version} -p1

%conf
# This file is empty, so drop it before we make assemble the docs
rm doc/FAQ.text

# Make sure we do not use the bundled copy of xml-light
rm -fr tools/instrospection/xml-light

%build
export LABLGTK_EXTRA_FLAGS=-g
%dune_build

# Make the man pages
HELP2MAN="-N --version-string=%{version}"
cd _build/install/default/bin
help2man $HELP2MAN -N -o ../../../../gdk_pixbuf_mlsource3.1 \
  -n 'Generate pixel data' ./gdk_pixbuf_mlsource3
help2man $HELP2MAN -N -o ../../../../lablgladecc3.1 \
  -n 'GTK interface compiler' ./lablgladecc3
cd -

%install
%dune_install -s

# Install the man pages
mkdir -p %{buildroot}%{_mandir}/man1
cp -p gdk_pixbuf_mlsource3.1 lablgladecc3.1 %{buildroot}%{_mandir}/man1

%check
%dune_check

%files -f .ofiles-lablgtk3
%doc CHANGES.md CHANGELOG.API README.md doc
%license LGPL LICENSE
%{_mandir}/man1/gdk_pixbuf_mlsource3.1*
%{_mandir}/man1/lablgladecc3.1*

%files devel -f .ofiles-lablgtk3-devel

%files goocanvas2 -f .ofiles-lablgtk3-goocanvas2

%files goocanvas2-devel -f .ofiles-lablgtk3-goocanvas2-devel

%files gtkspell3 -f .ofiles-lablgtk3-gtkspell3

%files gtkspell3-devel -f .ofiles-lablgtk3-gtkspell3-devel

%files rsvg2 -f .ofiles-lablgtk3-rsvg2

%files rsvg2-devel -f .ofiles-lablgtk3-rsvg2-devel

%files sourceview3 -f .ofiles-lablgtk3-sourceview3

%files sourceview3-devel -f .ofiles-lablgtk3-sourceview3-devel

%changelog
* Fri Jan 10 2025 Jerry James <loganjerry@gmail.com> - 3.1.5-4
- OCaml 5.3.0 rebuild for Fedora 42

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 19 2024 Richard W.M. Jones <rjones@redhat.com> - 3.1.5-2
- OCaml 5.2.0 ppc64le fix

* Mon Jun 10 2024 Jerry James <loganjerry@gmail.com> - 3.1.5-1
- Version 3.1.5
- Drop upstreamed patch for incompatible pointer error

* Wed May 29 2024 Richard W.M. Jones <rjones@redhat.com> - 3.1.4-2
- OCaml 5.2.0 for Fedora 41

* Fri Feb  2 2024 Jerry James <loganjerry@gmail.com> - 3.1.4-1
- Version 3.1.4
- Add rsvg2 subpackage
- Add patch to fix an incompatible pointer error

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 18 2023 Richard W.M. Jones <rjones@redhat.com> - 3.1.3-9
- OCaml 5.1.1 + s390x code gen fix for Fedora 40

* Tue Dec 12 2023 Richard W.M. Jones <rjones@redhat.com> - 3.1.3-8
- OCaml 5.1.1 rebuild for Fedora 40

* Thu Oct 05 2023 Richard W.M. Jones <rjones@redhat.com> - 3.1.3-7
- OCaml 5.1 rebuild for Fedora 40

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Richard W.M. Jones <rjones@redhat.com> - 3.1.3-5
- OCaml 5.0 rebuild for Fedora 39

* Mon Jul 10 2023 Jerry James <loganjerry@gmail.com> - 3.1.3-4
- OCaml 5.0.0 rebuild

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 3.1.3-3
- Rebuild OCaml packages for F38

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Oct 12 2022 Jerry James <loganjerry@gmail.com> - 3.1.3-1
- Version 3.1.3
- Convert License tag to SPDX
- Drop xml-light patch; that code is not built anyway

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Jerry James <loganjerry@gmail.com> - 3.1.2-4
- Use new OCaml macros

* Sat Jun 18 2022 Richard W.M. Jones <rjones@redhat.com> - 3.1.2-4
- OCaml 4.14.0 rebuild

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 3.1.2-3
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 27 2021 Jerry James <loganjerry@gmail.com> - 3.1.2-1
- Version 3.1.2
- Drop upstreamed -vadjustment patch
- Add -goocanvas2 and -goocanvas2-devel subpackages

* Tue Oct 05 2021 Richard W.M. Jones <rjones@redhat.com> - 3.1.1-9
- OCaml 4.13.1 build

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 17 2021 Jerry James <loganjerry@gmail.com> - 3.1.1-7
- Add ocaml-findlib BR to get ocamldoc META file
- Build documentation with ocamldoc instead of odoc

* Tue Jun 22 2021 Jerry James <loganjerry@gmail.com> - 3.1.1-6
- Rebuild for ocaml-lablgtk without gnomeui
- Add -vadjustment patch to fix layout issue

* Mon Mar  1 15:56:21 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 3.1.1-5
- OCaml 4.12.0 build

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 3.1.1-3
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 3.1.1-2
- OCaml 4.11.0 rebuild

* Wed Aug  5 2020 Jerry James <loganjerry@gmail.com> - 3.1.1-1
- Version 3.1.1
- Drop upstreamed -fno-common patch

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 3.1.0-6
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Wed Apr 22 2020 Richard W.M. Jones <rjones@redhat.com> - 3.1.0-5
- OCaml 4.11.0 pre-release attempt 2

* Sat Apr 04 2020 Richard W.M. Jones <rjones@redhat.com> - 3.1.0-4
- Bump release and rebuild.

* Sat Apr 04 2020 Richard W.M. Jones <rjones@redhat.com> - 3.1.0-3
- Update all OCaml dependencies for RPM 4.16.

* Sat Mar  7 2020 Jerry James <loganjerry@gmail.com> - 3.1.0-2
- Build documentation with odoc
- Add _isa flags to Requires in the devel subpackage

* Wed Jan 29 2020 Jerry James <loganjerry@gmail.com> - 3.1.0-1
- Initial RPM
