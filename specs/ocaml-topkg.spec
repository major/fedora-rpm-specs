%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

# The topkg-care part has dependencies that themselves depend on the main
# package.  We do not build the care part for now.
%bcond care 0

Name:           ocaml-topkg
Version:        1.1.1
Release:        %autorelease
Summary:        The transitory OCaml software packager

License:        ISC
URL:            https://erratique.ch/software/topkg/
VCS:            git:https://erratique.ch/repos/topkg.git
Source:         %{url}releases/topkg-%{version}.tbz

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch:    %{ix86}

BuildRequires:  ocaml >= 4.08.0
BuildRequires:  ocaml-compiler-libs
BuildRequires:  ocaml-findlib >= 1.6.1
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-rpm-macros

%if %{with care}
BuildRequires:  ocaml-bos-devel >= 0.2.1
BuildRequires:  ocaml-cmdliner-devel >= 1.3.0
BuildRequires:  ocaml-fmt-devel >= 0.9.0
BuildRequires:  ocaml-logs-devel
BuildRequires:  ocaml-webbrowser-devel
BuildRequires:  ocaml-opam-format-devel >= 2.0.0
%endif

%global _desc %{expand:Topkg is a packager for distributing OCaml software.  It provides an API to
describe the files a package installs in a given build configuration and to
specify information about the package's distribution, creation and publication
procedures.}

%description
%_desc

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%if %{with care}
%package        care
Summary:        Command line tool for the transitory OCaml software packager
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-ocamlbuild%{?_isa}

%description    care
%_desc

This package provides a command line tool which helps with various aspects of
a package's life cycle: creating and linting a distribution, releasing it on
the web, publishing its documentation, adding it to the OCaml opam repository,
etc.

%package        care-devel
Summary:        Development files for %{name}-care
Requires:       %{name}-care%{?_isa} = %{version}-%{release}
Requires:       ocaml-bos-devel%{?_isa}
Requires:       ocaml-cmdliner-devel%{?_isa}
Requires:       ocaml-fmt-devel%{?_isa}
Requires:       ocaml-logs-devel%{?_isa}
Requires:       ocaml-opam-format-devel%{?_isa}
Requires:       ocaml-webbrowser-devel%{?_isa}

%description    care-devel
The %{name}-care-devel package contains libraries and signature files for
developing applications that use %{name}-care.
%endif

%prep
%autosetup -n topkg-%{version} -p1

%conf
# This package can replace "watermarks" in software that it builds.  However,
# we are building from scratch, rather than using topkg to build itself, so we
# have to do the job manually.
for fil in $(find . -type f); do
  sed -e 's,%%%%PKG_DOC%%%%,%{url}doc/,' \
      -e 's,%%%%PKG_HOMEPAGE%%%%,%{url},' \
      -e 's,%%%%VERSION%%%%,v%{version},' \
      -e 's,%%%%VERSION_NUM%%%%,%{version},' \
      -i.orig $fil
  touch -r $fil.orig $fil
  rm $fil.orig
done

%build
# Build the library and the tests
ocaml pkg/pkg.ml build --pkg-name topkg --dev-pkg false --tests true

%if %{with care}
# Build topkg-care
ocaml pkg/pkg.ml build --pkg-name topkg-care --dev-pkg false --tests true
%endif

%install
%ocaml_install -s

%if %{with care}
%check
ocaml pkg/pkg.ml test
%endif

%files -f .ofiles-topkg
%doc CHANGES.md README.md
%license LICENSE.md

%files devel -f .ofiles-topkg-devel

%if %{with care}
%files care -f .ofiles-care

%files care-devel -f .ofiles-care-devel
%endif

%changelog
%autochangelog
