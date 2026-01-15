# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%global giturl  https://github.com/ocaml/graphics

Name:           ocaml-graphics
Version:        5.2.0
Release:        %autorelease
Summary:        Portable drawing primitives for OCaml

License:        LGPL-2.1-only WITH OCaml-LGPL-linking-exception
URL:            https://ocaml.github.io/graphics/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/%{version}/graphics-%{version}.tar.gz

BuildRequires:  ocaml >= 4.09.0
BuildRequires:  ocaml-dune >= 2.7
BuildRequires:  ocaml-dune-configurator-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xft)

%description
The graphics library provides a set of portable drawing primitives.  Drawing
takes place in a separate window that is created when `Graphics.open_graph` is
called.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libX11-devel%{?_isa}
Requires:       libXft-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains developer documentation for
%{name}.

%prep
%autosetup -n graphics-%{version}

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%doc CHANGES.md README.md
%license LICENSE

%files devel -f .ofiles-devel

%files doc
%license LICENSE
%doc examples

%changelog
%autochangelog
