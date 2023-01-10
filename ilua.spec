Name:           ilua
Version:        0.2.1
Release:        12%{?dist}
Summary:        Portable Lua kernel for Jupyter

# The package contains the Lua logo, which has some modification restrictions.
# It was permitted by legal, but advised not to declare the license in the tag:
# https://lists.fedoraproject.org/archives/list/legal@lists.fedoraproject.org/thread/UDFBEBDR4NTSP6TATQEONDJAYHSYXUUQ/
# Hence, only listing the license of the code.
# ilua is GPLv2
# Bundled lua files in ilua/ext are all MIT
License:        GPLv2 and MIT
URL:            https://github.com/guysv/ilua
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
%if 0%{?fedora} >= 38 || 0%{?rhel} >= 10
ExcludeArch:    %{ix86}
%endif

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

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
%pyproject_buildrequires -r

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
%license LICENSE
%doc README.md CHANGES.md
%{_bindir}/ilua
%dir %{_datadir}/jupyter/kernels/lua/
%{_datadir}/jupyter/kernels/lua/*.json
%{_datadir}/jupyter/kernels/lua/*.png
%license %{_datadir}/jupyter/kernels/lua/logo-license.txt

%changelog
* Sun Jan 08 2023 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.1-12
- Drop support for i686

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 02 2021 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-8
- Run a smoke test when building the package

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.2.1-7
- Rebuilt for Python 3.10

* Thu Feb 11 2021 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-6
- Prperly own site-packages/ilua/__pycache__

* Sat Feb 06 2021 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-5
- Declare bundled Lua libraries, MIT-licensed

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Sep 03 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-3
- Include the Lua logo from upstream

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 11 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-1
- Initial package (#1834280)
