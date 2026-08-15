Name:		mink-idl-compiler
Version:	1.0.1
Release:	%autorelease
Summary:	Mink IDL compiler

License:	%{shrink:
    BSD-3-Clause
    AND MIT
    AND Unicode-3.0
    AND Unicode-DFS-2016
    AND (Apache-2.0 OR MIT)
    AND (Unlicense OR MIT)
}
# LICENSE.dependencies contains a full license breakdown

URL:		https://github.com/qualcomm/mink-idl-compiler
Source:		%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

ExclusiveArch:	%{rust_arches}

BuildRequires:	cargo
BuildRequires:	cargo-rpm-macros

%description
Mink Interface Description Language (IDL) describes programming interfaces
that can be used to communicate across security domain boundaries.

The Mink IDL compiler generates target language header files which include
bindings for Mink interfaces and their associates structures. The generated
header files introduce proxy functions that facilitate method invocation
using Mink's Object_invoke IPC mechanism.

%prep
%autosetup
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires -t

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
install -Dpm 0755 target/release/idlc %{buildroot}%{_bindir}/idlc

%check
%cargo_test

%files
%license LICENSE.txt
%license LICENSE.dependencies
%doc README.md
%{_bindir}/idlc

%changelog
%autochangelog
