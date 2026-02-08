%global giturl  https://github.com/OCamlPro/alt-ergo

Name:		alt-ergo
Version:	2.4.3
Release:	%autorelease
Summary:	Automated theorem prover including linear arithmetic

License:	CECILL-C
URL:		https://alt-ergo.ocamlpro.com/
VCS:		git:%{giturl}.git
Source:		%{giturl}/archive/v%{version}-free/%{name}-free-%{version}.tar.gz
# Fedora does not need the forward compatibility seq and stdlib-shims packages
Patch:		%{name}-forward-compat.patch
# Silence a deprecation warning
Patch:		%{name}-deprecation.patch
# Do not store architecture-specific plugins in /usr/share
Patch:		%{name}-datadir.patch
# Avoid warnings due to misplaced inline attributes
Patch:		%{name}-inline-error.patch
# Permit use of cmdliner 2.x
Patch:		%{name}-cmdliner.patch

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch:	%{ix86}

BuildRequires:	make
BuildRequires:	ocaml >= 4.05.0
BuildRequires:	ocaml-cmdliner-devel >= 1.1.0
BuildRequires:	ocaml-dune >= 3.0
BuildRequires:	ocaml-dune-build-info-devel
BuildRequires:	ocaml-dune-configurator-devel
BuildRequires:	ocaml-menhir
BuildRequires:	ocaml-num-devel
BuildRequires:	ocaml-ocplib-simplex-devel >= 0.4.1
BuildRequires:	ocaml-psmt2-frontend-devel >= 0.4
BuildRequires:	ocaml-zarith-devel >= 1.4
BuildRequires:	ocaml-zip-devel >= 1.07

# This can be removed when F48 reaches EOL
Obsoletes:	alt-ergo-gui < 2.4
Obsoletes:	ocaml-alt-ergo-lib < 2.4
Obsoletes:	ocaml-alt-ergo-lib-devel < 2.4
Obsoletes:	ocaml-alt-ergo-parsers < 2.4
Obsoletes:	ocaml-alt-ergo-parsers-devel < 2.4
Provides:	alt-ergo-gui = %{version}-%{release}
Provides:	ocaml-alt-ergo-lib = %{version}-%{release}
Provides:	ocaml-alt-ergo-lib-devel = %{version}-%{release}
Provides:	ocaml-alt-ergo-parsers = %{version}-%{release}
Provides:	ocaml-alt-ergo-parsers-devel = %{version}-%{release}

# Filter out Requires with no matching Provides
%global __requires_exclude ocaml\\\(AltErgoLib.*\\\)

%description
Alt-Ergo is an automated theorem prover implemented in OCaml.  It is based on
CC(X) - a congruence closure algorithm parameterized by an equational theory
X.  This algorithm is reminiscent of the Shostak algorithm.  Currently CC(X)
is instantiated by the theory of linear arithmetics.  Alt-Ergo also contains a
home made SAT-solver and an instantiation mechanism by which it fully supports
quantifiers.

%prep
%autosetup -n %{name}-%{version}-free -p1

%conf
# Unzip an example
cd examples/AB-Why3-plugin
unzip p4_34.why.zip
rm p4_34.why.zip
cd -

%ifnarch %{ocaml_native_compiler}
# Do not require native plugins
sed -i '/cmxs/d' plugins/fm-simplex/dune
%endif

# This is not an autoconf-generated script.  Do NOT use %%configure.
./configure --prefix=%{_prefix} --libdir=%{ocamldir} --mandir=%{_mandir}

%build
%make_build

%install
%dune_install

# Fix permissions
chmod 0755 %{buildroot}%{_datadir}/%{name}-free/plugins/*.cmxs

# The install target in the Makefile puts these in the wrong place
mv %{buildroot}%{_datadir}/%{name}-free/{plugins,preludes} \
   %{buildroot}%{ocamldir}/%{name}-free
rmdir %{buildroot}%{_datadir}/%{name}-free

# Put something interesting into the META file
cat > %{buildroot}%{ocamldir}/%{name}-free/META << EOF
version = "%{version}"
description = "Automated theorem prover including linear arithmetic"
requires = ""
EOF

%check
%dune_check

%files
%doc CHANGES.md README.md examples rsc/publications/*.pdf
%{_bindir}/%{name}
%{_mandir}/man1/alt-ergo.1*
%{ocamldir}/%{name}-free/

%changelog
%autochangelog
