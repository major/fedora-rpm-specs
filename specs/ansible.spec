# SPDX-License-Identifier: MIT
# Copyright (C) Fedora Project Authors
# License Text: https://spdx.org/licenses/MIT.html

# disable the python -s shbang flag as we want to be able to find non system modules
%undefine _py3_shebang_s

# Roles' files and templates should not be mangled.
# These files are installed on remote systems which may or may not have the
# same filesystem layout as Fedora.
%global __brp_mangle_shebangs_exclude_from ^%{python3_sitelib}/ansible_collections/[^/]+/[^/]+/roles/[^/]+/(files|templates)/.*$
%global __requires_exclude_from %{?__requires_exclude_from:%__requires_exclude_from|}%{__brp_mangle_shebangs_exclude_from}

Name:           ansible
Summary:        Curated set of Ansible collections included in addition to ansible-core
Version:        14.2.0
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

URL:            https://ansible.com
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

# ansible-prep.sh
%{S:1}

mkdir licenses docs
cd ansible_collections
# ansible-license-install.sh
%{S:2} \
    "$(readlink -f ../licenses)" \
    "$(readlink -f ../docs)" \
cd -


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
