# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

# This package contains generated C header files.  They differ by architecture,
# so this package cannot be noarch, but there are no ELF objects in it.
%global debug_package %{nil}

Name:           ocaml-jst-config
Version:        0.17.0
Release:        %autorelease
Summary:        Compile-time configuration for Jane Street libraries

License:        MIT
URL:            https://github.com/janestreet/jst-config
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/jst-config-%{version}.tar.gz
# Use the glibc wrapper for gettid instead of making a bare system call
Patch:          %{name}-gettid.patch

BuildRequires:  ocaml >= 5.1.0
BuildRequires:  ocaml-base-devel >= 0.17
BuildRequires:  ocaml-dune >= 3.11.0
BuildRequires:  ocaml-dune-configurator-devel
BuildRequires:  ocaml-ppx-assert-devel >= 0.17

%description
This package defines compile-time constants used in Jane Street libraries such
as Base, Core, and Async.

%package        devel
Summary:        Development files for %{name}

%description    devel
This package defines compile-time constants used in Jane Street libraries such
as Base, Core, and Async.

%prep
%autosetup -p1 -n jst-config-%{version}

%build
%dune_build

%install
%dune_install -n

# The generated config_h.ml file is empty, and so the rest of the compiled OCaml
# artifacts likewise contain nothing useful.  No consumers need them either, so
# we remove them.
rm -f %{buildroot}%{ocamldir}/jst-config/*.{a,cma,cmi,cmt,cmx,cmxa,cmxs,ml}

# Removing those artifacts means we also need to remove references to them
sed -ri '/(archive|plugin)/d' \
        %{buildroot}%{ocamldir}/jst-config/{dune-package,META}

%check
%dune_check

%files devel
%license LICENSE.md
%{ocamldir}/jst-config/

%changelog
%autochangelog
