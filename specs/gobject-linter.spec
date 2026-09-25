Name:           gobject-linter
Version:        0.1.2
Release:        %autorelease
Summary:        A tree-sitter-based linter for GObject/C applications

SourceLicense:  MIT
# (Apache-2.0 OR MIT) AND BSD-3-Clause
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# Apache-2.0 OR MIT
# MIT
# MIT AND Unicode-DFS-2016 AND BSD-2-Clause AND BSD-3-Clause AND LicenseRef-Fedora-Public-Domain
# MIT OR Apache-2.0
# MPL-2.0
# Unlicense OR MIT
License:        %{shrink:
	MIT
	AND BSD-2-Clause
	AND BSD-3-Clause
	AND MPL-2.0
	AND Unicode-DFS-2016
	AND LicenseRef-Fedora-Public-Domain
	AND (Apache-2.0 OR MIT)
	AND (Unlicense OR MIT)
}
# LICENSE.dependencies contains a full license breakdown

URL:            https://github.com/bilelmoussaoui/gobject-linter
Source:         %{url}/archive/gobject-linter-%{version}.tar.gz

BuildRequires:  cargo-rpm-macros

%description
A tree-sitter-based linter for GObject/C applications.

%prep
%autosetup -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires -t

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
install -Dpm 0755 target/rpm/gobject-linter -t %{buildroot}%{_bindir}

%check
%cargo_test

%files
%license LICENSE
%license LICENSE.dependencies
%doc README.md
%{_bindir}/gobject-linter

%changelog
%autochangelog
