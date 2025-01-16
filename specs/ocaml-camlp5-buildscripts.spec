%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-camlp5-buildscripts
Version:        0.04
Release:        %autorelease
Summary:        Sysadmin scripts for camlp5 projects

License:        MIT
URL:            https://github.com/camlp5/camlp5-buildscripts
VCS:            git:%{url}.git
Source:         %{url}/archive/%{version}/camlp5-buildscripts-%{version}.tar.gz

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch:    %{ix86}

BuildRequires:  asciidoc
BuildRequires:  make
BuildRequires:  not-ocamlfind >= 0.01
BuildRequires:  ocaml >= 4.10.0
BuildRequires:  ocaml-bos-devel >= 0.2.1
BuildRequires:  ocaml-cppo
BuildRequires:  ocaml-fmt-devel
BuildRequires:  ocaml-mdx-devel >= 2.2.1
BuildRequires:  ocaml-re-devel >= 1.10.4

%description
Sysadmin scripts written in OCaml (and Perl precursors), for use with
Camlp5 and Camlp5-based projects.  These scripts allow removing a
dependency on Perl for such projects.

%prep
%autosetup -n camlp5-buildscripts-%{version}

%conf
# Build native executables when possible
%ifarch %{ocaml_native_compiler}
sed -i 's/ocamlc/ocamlopt/' src/Makefile
%endif

# Generate debuginfo
sed -i 's/-linkpkg/-g &/' src/Makefile

%build
%make_build
asciidoc README.asciidoc

%install
export OCAMLFIND_DESTDIR=%{buildroot}%{ocamldir}
mkdir -p $OCAMLFIND_DESTDIR
%make_install

# The META file is empty.  Let's put something interesting into it.
cat > %{buildroot}%{ocamldir}/camlp5-buildscripts/META << EOF
description = "Sysadmin scripts for camlp5 projects"
version = "%{version}"
requires = ""
EOF

%check
make test

%files
%doc CHANGES README.html
%license LICENSE
%{ocamldir}/

%changelog
%autochangelog
