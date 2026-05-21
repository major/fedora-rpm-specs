# SPDX-License-Identifier: MIT
# Copyright (C) Fedora Project Authors
# License Text: https://spdx.org/licenses/MIT.html

# Compatibility                                                             #
#############################################################################
# This specfile should remain compatible with EPEL 9 and stable Fedoras.    #
# The EPEL 8 specfile is separately maintained,                             #
# but the ansible-prep.sh and ansible-install-license.sh scripts are shared #
# across branches.                                                          #
#############################################################################

# TODO: Re-enable docs and tests once possible
%bcond docs 0
%bcond tests 0

# disable the python -s shbang flag as we want to be able to find non system modules
# NB: We cannot use https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_py3_shebang_S on RHEL 9.
%global py3_shebang_flags %(echo %{py3_shebang_flags} | sed 's|s||')

# Roles' files and templates should not be mangled.
# These files are installed on remote systems which may or may not have the
# same filesystem layout as Fedora.
%global __brp_mangle_shebangs_exclude_from ^%{python3_sitelib}/ansible_collections/[^/]+/[^/]+/roles/[^/]+/(files|templates)/.*$
%global __requires_exclude_from %{?__requires_exclude_from:%__requires_exclude_from|}%{__brp_mangle_shebangs_exclude_from}

%if 0%{?rhel} >= 8
# ansible-core package is built against Python 3.11 in RHEL 8 and RHEL 9 which
# is not the default version.
%global python3_pkgversion 3.11
%endif

Name:           ansible
Summary:        Curated set of Ansible collections included in addition to ansible-core
Version:        13.7.0
%global uversion %{version_no_tilde %{quote:%nil}}
Release:        %autorelease

# In addition to GPL-3.0-or-later, the following licenses apply.
# License text that solely exists in file headers were not considered.
# Instead, the overall license was determined by searching for license files
# This is the only the practical way to handle license scanning for a project
# of this size.
# All collections must be primarily licensed under GPL-3.0-or-later, so top
# level license files are excluded.
# find /usr/share/licenses/ansible -type f | grep -vEe '(COPYING|LICENSE)(\.(txt|md))?$' -e 'GPL' | xargs -n1 basename | sort -u
#
# Apache-2.0.txt
# Apache-license.txt
# BSD-2-Clause.txt
# BSD-3-Clause.txt
# MIT.txt
# MPL-2.0.txt
# PSF-2.0.txt
# PSF-license.txt
License:        GPL-3.0-or-later AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND MIT AND MPL-2.0 AND PSF-2.0
Source0:        %{pypi_source %{name} %{uversion}}
Source1:        ansible-prep.sh
Source2:        ansible-install-licenses.sh

Url:            https://ansible.com
BuildArch:      noarch

BuildRequires:  dos2unix
BuildRequires:  findutils
BuildRequires:  python%{python3_pkgversion}-devel

%if %{with tests}
# TODO build-requires
%endif

%if %{with docs}
# TODO build-requires
%endif


%description
Ansible is a radically simple model-driven configuration management,
multi-node deployment, and remote task execution system. Ansible works
over SSH and does not require any software or daemons to be installed
on remote nodes. Extension modules can be written in any language and
are transferred to managed machines automatically.

This package provides a curated set of Ansible collections included in addition
to ansible-core.


%prep
%autosetup -N -n %{name}-%{uversion}

# Relax ansible-core dependency to avoid FTI bugs on EPEL
#
# This is necessary, because the EPEL ansible maintainers don't have control
# over ansible-core in RHEL, and it's difficult to time updates across
# repositories. I have tried to stick to upstream's version constraints, but
# that's apparently not working too well. This change gives us a grace period
# to properly release and test new ansible major versions after RHEL rebases
# ansible-core. The lower version constraints can stay in place.

sed "s|ansible-core ~=|ansible-core >=|" setup.cfg > setup.cfg.bak
# Verify
set -o pipefail
grep -B1 "ansible-core >=" setup.cfg.bak | grep -F 'install_requires ='
%if %{defined rhel}
mv setup.cfg.bak setup.cfg
%endif

# ansible-prep.sh
%{S:1}

(
mkdir licenses docs
cd ansible_collections
# ansible-license-install.sh
%{S:2} \
    "$(readlink -f ../licenses)" \
    "$(readlink -f ../docs)" \
)


%generate_buildrequires
%pyproject_buildrequires


%build
%py3_shebang_fix ansible_collections

%pyproject_wheel


%install
%pyproject_install
# This adds over a minute to the build due to the size of the ansible package.
# It's better to manually specify the paths in %%files...
# %%pyproject_save_files ansible_collections

mkdir -p %{buildroot}%{_licensedir}/ansible %{buildroot}%{_docdir}/ansible
mv licenses %{buildroot}%{_licensedir}/ansible/ansible_collections
mv docs %{buildroot}%{_pkgdocdir}/ansible_collections


%check
%if %{with tests}
# TODO: Run tests
%endif


%files
%license COPYING
%license %{_licensedir}/ansible/ansible_collections/
%doc README.rst PKG-INFO porting_guide_*.rst CHANGELOG-v*.rst
%doc %{_pkgdocdir}/ansible_collections/
%{_bindir}/ansible-community
# Note (dmsimard): This ansible package installs collections to the python sitelib to mirror the UX
# when installing the ansible package from PyPi.
# This allows users to install individual collections manually with ansible-galaxy (~/.ansible/collections/ansible_collections)
# or via standalone distribution packages to datadir (/usr/share).
# Both will have precedence over the collections installed in the python sitelib.
%{python3_sitelib}/ansible_collections/
%{python3_sitelib}/ansible-%{uversion}.dist-info/


%changelog
%autochangelog
