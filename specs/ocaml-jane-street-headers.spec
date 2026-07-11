# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%global srcname jane-street-headers

# This package creates no ELF files, but cannot be noarch since the install
# location is under _libdir.
%global debug_package %{nil}

Name:           ocaml-%{srcname}
Version:        0.17.0
Release:        %autorelease
Summary:        Jane Street header files

License:        MIT
URL:            https://github.com/janestreet/jane-street-headers
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildSystem:    dune
BuildRequires:  ocaml >= 5.1.0
BuildRequires:  ocaml-dune >= 3.11.0

%description
This package contains C header files shared between various Jane Street
packages.

%package        devel
Summary:        Development files for %{name}

%description    devel
This package contains C header files shared between various Jane Street
packages.

%prep
%autosetup -n %{srcname}-%{version}

%install -a
# The generated jane_street_headers.ml file is empty, and so the rest of the
# compiled OCaml artifacts likewise contain nothing useful.  No consumers need
# them either; we remove them.
rm -f %{buildroot}%{ocamldir}/%{srcname}/*.{cma,cmi,cmt,cmx,cmxa,cmxs,ml}

# Removing those artifacts means we also need to remove references to them
sed -ri '/(archive|plugin)/d' \
        %{buildroot}%{ocamldir}/%{srcname}/{dune-package,META}

%files devel
%doc README.org
%license LICENSE.md
%{ocamldir}/%{srcname}/

%changelog
%autochangelog
