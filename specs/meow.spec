Name:		meow
Version:	2.1.5
Release:	%autorelease
Summary:	Print ASCII cats to your terminal

# The entire source is MIT. The following output from %%{cargo_license_summary}
# reflects the licenses of statically-linked Rust library dependencies. See
# LICENSES.dependencies for a full breakdown.
#
# Apache-2.0 OR MIT
# BSD-2-Clause OR Apache-2.0 OR MIT
# MIT
# MIT OR Apache-2.0
License:	%{shrink:
	MIT AND
	(Apache-2.0 OR MIT) AND
	(BSD-2-Clause OR Apache-2.0 OR MIT)
}
URL:		https://github.com/pixelsergey/meow
Source:		%{url}/archive/v%{version}/meow-v%{version}.tar.gz

BuildRequires:	cargo-rpm-macros >= 24
BuildRequires:	help2man
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:	%{ix86}

%description
This is a simple app to print ASCII cats directly to your terminal.
Run `meow` for a single cat, `meow -c <COUNT>` for more cats,
or `meow -l` if you think that you are literally the cat that will be printed.

%prep
%autosetup
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build
%{cargo_license} > LICENSE.dependencies
%{cargo_license_summary}

%install
install -p -D target/rpm/meow-cli %{buildroot}%{_bindir}/meow
install -d %{buildroot}%{_mandir}/man1
help2man --no-info --name='%{summary}' --version-string='%{version}' \
	--output=%{buildroot}%{_mandir}/man1/meow.1 \
	%{buildroot}%{_bindir}/meow

%check
%cargo_test

%files
%{_bindir}/meow
%{_mandir}/man1/meow.1*
%license LICENSE
%license LICENSE.dependencies
%doc README.md

%changelog
%autochangelog
