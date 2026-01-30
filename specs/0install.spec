# PACKAGING NOTE: We do not currently build either the command-line tool or the
# GUI interface.  They depend on obus (https://github.com/ocaml-community/obus)
# which cannot be built for the version of OCaml currently in Fedora.  For now
# we only build the solver, which is the only part needed by opam anyway.

%global giturl  https://github.com/0install/0install

Name:           0install
Version:        2.18
Release:        %autorelease
Summary:        Decentralized cross-distribution software installation system

# LGPL-2.1-or-later: the project as a whole
# CC0-1.0: share/metainfo/0install.appdata.xml
# LicenseRef-Fedora-Public-Domain: src/sample_client.py
License:        LGPL-2.1-or-later
SourceLicense:  %{license} AND CC0-1.0 AND LicenseRef-Fedora-Public-Domain
URL:            https://0install.net/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{name}-%{version}.tbz
Source1:        %{giturl}/releases/download/v%{version}/%{name}-%{version}.tbz.sig
# Key for Thomas Leonard <talex5@gmail.com>
Source2:        5DD58D70899C454A966D6A5175133C8F94F6E0CC.gpg

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch:    %{ix86}

BuildRequires:  gpgverify
BuildRequires:  ocaml >= 4.08
BuildRequires:  ocaml-dune >= 2.5
BuildRequires:  ocaml-ounit2-devel

%global _desc %{expand:Zero Install is a decentralized cross-distribution software installation
system.  Other features include full support for shared libraries (with a SAT
solver for dependency resolution), sharing between users, and integration with
native platform package managers.  It supports both binary and source
packages, and works on Linux, macOS, Unix and Windows systems.}

%description
%_desc

%package -n     ocaml-0install-solver
Summary:        Package dependency solver

%description -n ocaml-0install-solver
%_desc

This package contains a package dependency resolver based on a SAT solver.
This was originally written for the 0install package manager, but is now
generic and is also used as a solver backend for opam.

The SAT solver is based on MiniSat (http://minisat.se/Papers.html) and the
application to package management is based on OPIUM (Optimal Package
Install/Uninstall Manager).  0install-solver uses a (novel?) strategy to find
the optimal solution extremely quickly (even for a SAT-based solver).

%package -n     ocaml-0install-solver-devel
Summary:        Development files for %{name}-solver
Requires:       ocaml-0install-solver%{?_isa} = %{version}-%{release}

%description -n ocaml-0install-solver-devel
The %{name}-solver-devel package contains libraries and signature files for
developing applications that use %{name}-solver.

%prep
%{gpgverify} --data=%{SOURCE0} --signature=%{SOURCE1} --keyring=%{SOURCE2}
%autosetup

%build
%dune_build -p 0install-solver

%install
%dune_install 0install-solver

%check
%dune_check -p 0install-solver

%files -n ocaml-0install-solver -f .ofiles
%doc CHANGES.md README.md
%license COPYING

%files -n ocaml-0install-solver-devel -f .ofiles-devel

%changelog
%autochangelog
