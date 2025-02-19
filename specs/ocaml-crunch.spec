%global giturl  https://github.com/mirage/ocaml-crunch

Name:           ocaml-crunch
Version:        4.0.0
Release:        %autorelease
Summary:        Convert a filesystem into a static OCaml module

License:        ISC
URL:            http://mirage.github.io/ocaml-crunch/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/crunch-%{version}.tbz

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch:    %{ix86}

BuildRequires:  ocaml >= 4.08.0
BuildRequires:  ocaml-cmdliner-devel >= 1.1
BuildRequires:  ocaml-dune >= 2.5
BuildRequires:  ocaml-ptime-devel

%description
Crunch takes a directory of files and compiles them into a standalone
OCaml module which serves the contents directly from memory.  This can
be convenient for libraries that need a few embedded files (such as a
web server) and do not want to deal with all the trouble of file
configuration.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-ptime-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n crunch-%{version}

%build
%dune_build

%install
%dune_install

# Unable to test due to missing dependencies:
# https://github.com/mirage/mirage-kv
# https://github.com/mirage/mirage-kv-mem
#
#%%check
#%%dune_check

%files -f .ofiles
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
