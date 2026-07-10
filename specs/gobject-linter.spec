%global commit 0a8b69c0691b67d7daf9e32d3d8738f18ca1d61d
%global shortcommit %(c=%{commit}; echo ${c:0:7})                                                                                          
%global commitdate 20260505

Name:           gobject-linter
Version:        0~%{commitdate}.git%{shortcommit}
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
Source:         %{url}/archive/gobject-linter-%{commit}.tar.gz

# https://bugzilla.redhat.com/show_bug.cgi?id=2420885
Patch0001:      gobject-linter-0-fedora-tree-sitter-version.patch

BuildRequires:  cargo-rpm-macros

%description
A tree-sitter-based linter for GObject/C applications.

%prep
%autosetup -p1 -n gobject-linter-%{commit}
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
