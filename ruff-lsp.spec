%bcond_without  check

Name:           ruff-lsp
Version:        0.0.52
Release:        1%{?dist}
Summary:        A Language Server Protocol implementation for Ruff

License:        MIT
URL:            https://github.com/astral-sh/ruff-lsp
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# ruff is not built for %%{ix86}
# See https://src.fedoraproject.org/rpms/ruff/blob/c7b8ef7bdc8cb947fae7c1c67157c6fab8e9c417/f/ruff.spec#_47
ExcludeArch:	%{ix86}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  ruff
BuildRequires:  help2man
# Test dependencies
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist python-lsp-jsonrpc}
BuildRequires:  %{py3_dist pytest-asyncio}

Requires:       ruff

%description
A Language Server Protocol implementation for Ruff,
an extremely fast Python linter and code formatter, written in Rust.

Ruff can be used to replace Flake8 (plus dozens of plugins),
Black, isort, pyupgrade, and more, all while executing tens or
hundreds of times faster than any individual tool.

ruff-lsp enables Ruff to be used in any editor that supports the LSP,
including Neovim, Sublime Text, Emacs and more. For Visual Studio Code,
check out the Ruff VS Code extension.

ruff-lsp supports surfacing Ruff diagnostics and providing Code Actions
to fix them, but is intended to be used alongside another Python LSP in
order to support features like navigation and autocompletion.


%prep
%autosetup -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l ruff_lsp

install -d '%{buildroot}%{_mandir}/man1'
%py3_test_envvars help2man --no-info --output='%{buildroot}%{_mandir}/man1/ruff-lsp.1' ruff-lsp


%check
%if %{with check}
%pytest
%else
%pyproject_check_import
%endif


%files -f %{pyproject_files}
%{_bindir}/ruff-lsp
%{_mandir}/man1/ruff-lsp.1*
%doc README.md

%changelog
* Wed Feb 21 2024 blinxen <h-k-81@hotmailcom> - 0.0.52-1
- Update to version 0.52.0
- Changelog: https://github.com/astral-sh/ruff-lsp/releases/tag/v0.0.52

* Tue Jan 30 2024 blinxen <h-k-81@hotmailcom> - 0.0.50-1
- Update to version 0.50.0
- Changelog: https://github.com/astral-sh/ruff-lsp/releases/tag/v0.0.50

* Thu Jan 18 2024 blinxen <h-k-81@hotmailcom> - 0.0.49-1
- Applied various improvements from package reviewer

* Sat Jan 13 2024 blinxen <h-k-81@hotmailcom> - 0.0.49-1
- Initial package
