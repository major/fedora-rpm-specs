# This specfile is licensed under:
#
# Copyright (C) 2023 Maxwell G <maxwell@gtmx.me>
# SPDX-License-Identifier: MIT
# License text: https://spdx.org/licenses/MIT.html

Name:           tomcli
Version:        0.1.2
Release:        2%{?dist}
Summary:        CLI for working with TOML files. Pronounced "tom clee."

License:        MIT
URL:            https://sr.ht/~gotmax23/tomcli
%global furl    https://git.sr.ht/~gotmax23/tomcli
Source0:        %{furl}/refs/download/v%{version}/tomcli-%{version}.tar.gz
Source1:        %{furl}/refs/download/v%{version}/tomcli-%{version}.tar.gz.asc
Source2:        https://meta.sr.ht/~gotmax23.pgp

BuildArch:      noarch
BuildRequires:  gnupg2
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pytest}

# One of the TOML backends is required
Requires:       (%{py3_dist tomcli[tomlkit]} or %{py3_dist tomcli[tomli]})
# Prefer the tomlkit backend
Suggests:       %{py3_dist tomcli[tomlkit]}
# Recommend the 'all' extra
Recommends:     %{py3_dist tomcli[all]}


%description
tomcli is a CLI for working with TOML files. Pronounced "tom clee."


%prep
%gpgverify -d0 -s1 -k2
%autosetup -p1


%generate_buildrequires
%pyproject_buildrequires -x all,tomlkit,tomli,test %{?el9:-w}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files tomcli

mkdir -p %{buildroot}%{bash_completions_dir}
mkdir -p %{buildroot}%{fish_completions_dir}
mkdir -p %{buildroot}%{zsh_completions_dir}

(
export PYTHONPATH="%{buildroot}%{python3_sitelib}"
export _TYPER_COMPLETE_TEST_DISABLE_SHELL_DETECTION=1
for command in %{buildroot}%{_bindir}/tomcli*; do
    $command --show-completion=bash > "%{buildroot}%{bash_completions_dir}/$(basename $command)"
    $command --show-completion=fish > "%{buildroot}%{fish_completions_dir}/$(basename $command).fish"
    $command --show-completion=zsh > "%{buildroot}%{zsh_completions_dir}/_$(basename $command)"
done
)


%check
%pytest


%pyproject_extras_subpkg -n tomcli all tomli tomlkit


%files -f %{pyproject_files}
# I prefer not to rely on %%pyproject_save_files to mark files with %%license.
# Also, Fedora's hatchling supports the current draft of PEP 639, but EPEL 9's
# does not.
%license LICENSES/*.txt
%doc README.md
%doc NEWS.md
%{_bindir}/tomcli*
%{bash_completions_dir}/tomcli*
%{fish_completions_dir}/tomcli*.fish
%{zsh_completions_dir}/_tomcli*


%changelog
* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 0.1.2-2
- Rebuilt for Python 3.12

* Sat May 20 2023 Maxwell G <maxwell@gtmx.me> - 0.1.2-1
- Update to 0.1.2.

* Wed May 03 2023 Maxwell G <maxwell@gtmx.me> - 0.1.1-1
- Initial package. Closes rhbz#2186902.
