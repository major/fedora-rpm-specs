%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-uunf
Version:        17.0.0
Release:        %autorelease
Summary:        Unicode text normalization for OCaml

License:        ISC
URL:            https://erratique.ch/software/uunf
VCS:            git:https://erratique.ch/repos/uunf.git
Source0:        %{url}/releases/uunf-%{version}.tbz
# Test-only file
Source1:        https://www.unicode.org/Public/%{version}/ucd/NormalizationTest.txt

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch:    %{ix86}

BuildRequires:  ocaml >= 4.14.0
BuildRequires:  ocaml-cmdliner-devel >= 1.1.0
BuildRequires:  ocaml-compiler-libs
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-rpm-macros
BuildRequires:  ocaml-topkg-devel >= 1.1.0
BuildRequires:  ocaml-uucd-devel >= 17.0.0
BuildRequires:  ocaml-uutf-devel >= 1.0.0

%description
Uunf is an OCaml library for normalizing Unicode text.  It supports all
Unicode normalization forms (http://www.unicode.org/reports/tr15/).  The
library is independent from any I/O mechanism or Unicode text data structure
and it can process text without a complete in-memory representation.

Uunf depends only on Uutf for support of OCaml UTF-X encoded strings.  It is
distributed under the ISC license.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-uutf-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n uunf-%{version} -p1
cp -p %{SOURCE1} test

%build
ocaml pkg/pkg.ml build \
  --dev-pkg false \
  --with-uutf true \
  --with-cmdliner true \
  --tests false

%install
# Install the binary and library
%ocaml_install

# Generate the man page
mkdir -p %{buildroot}%{_mandir}/man1
%{buildroot}/%{_bindir}/unftrip --help=groff > %{buildroot}%{_mandir}/man1/unftrip.1

# FIXME: The tests now require b0
#%%check
#ocaml pkg/pkg.ml test

%files -f .ofiles
%license LICENSE.md
%doc README.md CHANGES.md
%{_mandir}/man1/unftrip.1*

%files devel -f .ofiles-devel

%changelog
%autochangelog
