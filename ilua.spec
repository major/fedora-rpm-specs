Name:           ilua
Version:        0.2.1
Release:        %autorelease
Summary:        Portable Lua kernel for Jupyter

# The package contains the Lua logo, which has some modification restrictions.
# It was permitted by legal, but advised not to declare the license in the tag:
# https://lists.fedoraproject.org/archives/list/legal@lists.fedoraproject.org/thread/UDFBEBDR4NTSP6TATQEONDJAYHSYXUUQ/
# Hence, only listing the license of the code.
# ilua is GPL-2.0-only
# Bundled lua files in ilua/ext are all MIT
License:        GPL-2.0-only AND MIT
URL:            https://github.com/guysv/ilua
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# Twisted 23+ started using posix_nspawn in spawnProcess().
# For unknown reasons, this breaks ilua.
# Report: https://github.com/guysv/ilua/issues/30
# As a workaround, we force the old twisted behavior (fork)
# by setting a convenient internal attribute:
Patch:          ilua-never-use-spawn.patch

BuildArch:      noarch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  python3-devel

# For %%check
BuildRequires:  lua
BuildRequires:  /usr/bin/jupyter-console

Requires:       python-jupyter-filesystem
Recommends:     lua

# From ilua/ext. Versions are specified in the files and in scripts/getdeps.sh
# Note: inspect.lua has 3.1.0 in the file, but is from the 3.1.1 tag
Provides:       bundled(lua-inspect) = 3.1.1
Provides:       bundled(lua-json) = 0.1.1
Provides:       bundled(lua-netstring) = 0.2.0

%description
ILua is a feature-packed, portable console and Jupyter kernel for the Lua
language. It is Lua-implementation agnostic, should work with any Lua
interpreter out of the box.

%prep
%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files ilua

%check
# assert we can start the console ad run a simple command
# note 1: sleep because the kernel takes a while to start
# note 2: make sure the command is not Python compatible to fail if not executed in Lua
export PYTHONPATH=%{buildroot}%{python3_sitelib}
export JUPYTER_PATH=%{buildroot}%{_datadir}/jupyter
(sleep 5 && echo 'print("assert" .. "me")') | jupyter-console --simple-prompt --kernel=lua 2>&1 | tee check.log
grep assertme check.log
grep Traceback check.log && exit 1 || true

%files -f %pyproject_files
%doc README.md CHANGES.md
%{_bindir}/ilua
%dir %{_datadir}/jupyter/kernels/lua/
%{_datadir}/jupyter/kernels/lua/*.json
%{_datadir}/jupyter/kernels/lua/*.png
%license %{_datadir}/jupyter/kernels/lua/logo-license.txt

%changelog
%autochangelog
