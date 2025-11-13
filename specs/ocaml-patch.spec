%global giturl  https://github.com/hannesm/patch

Name:           ocaml-patch
Version:        3.1.0
Release:        %autorelease
Summary:        Parse unified and git diff output and apply patches in memory

# Some test files are covered by BSD-2-Clause, but we do not distribute them
# in any binary package.
License:        ISC
URL:            https://hannesm.github.io/patch/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/v%{version}/patch-%{version}.tar.gz
# Large test files
Source1:        https://codeberg.org/kit-ty-kate/ocaml-patch-tests/archive/main.tar.gz#/ocaml-patch-tests.tar.gz

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch:    %{ix86}

BuildRequires:  help2man
BuildRequires:  ocaml >= 4.14
BuildRequires:  ocaml-dune >= 3.0

# Test dependencies
# The ocaml-crowbar package is only available on x86_64
%ifarch %{x86_64}
BuildRequires:  ocaml-alcotest-devel
BuildRequires:  ocaml-crowbar-devel
%endif

%description
The patch module lets you apply your unified diffs in pure OCaml.

The loosely specified `diff` file format is widely used for transmitting
differences of line-based information.  The motivating example is opam, which
is able to validate updates being cryptographically signed by providing a
unified diff.  In addition, some support for the git diff format is available.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%package     -n opatch
Summary:        Command line tool to apply a diff to a directory

%description -n opatch
This package contains a pure OCaml command line tool to apply a unified or git
patch to a directory.

%prep
%autosetup -n patch-%{version}
tar -C test/data/external --strip-components=1 -xf %{SOURCE1}

%build
%dune_build

%install
%dune_install -s

# Skip a useless empty META file
rm %{buildroot}%{ocamldir}/opatch/META
sed -i '/META/d' .ofiles-opatch

# Create a man patch for opatch
mkdir -p %{buildroot}%{_mandir}/man1
help2man -N -n 'Apply a diff to a directory' \
  -o %{buildroot}%{_mandir}/man1/opatch.1 %{buildroot}%{_bindir}/opatch

%ifarch %{x86_64}
%check
%dune_check
%endif

%files -f .ofiles-patch
%doc CHANGES.md README.md
%license LICENSE.md

%files devel -f .ofiles-patch-devel

%files -n opatch -f .ofiles-opatch -f .ofiles-opatch-devel
%{_mandir}/man1/opatch.1*

%changelog
%autochangelog
